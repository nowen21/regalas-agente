# -*- coding: utf-8 -*-
"""Qué reglas pide **esta** solicitud del usuario.

**El problema que cierra.** Al abrir la sesión llegan literales los capítulos
`00` y `01`, y del resto solo el índice, con la orden de leer el archivo antes
de tocar el tema. Esa orden depende de que el agente se acuerde de cumplirla, y
cuando no se acuerda trabaja sin la regla y nadie se entera. Es el mismo patrón
que ya falló con el arranque: una promesa en vez de un hecho.

**Lo que hace.** Lee el mensaje del usuario y devuelve el **texto completo** de
las reglas que ese mensaje pide, con su presupuesto y con el porqué de cada
una. No resume: una regla resumida es una regla distinta.

**No hay archivo de índice, a propósito.** Armarlo desde las reglas mismas
cuesta 0,20 s para las 257, medido el 2026-09-16. Un índice generado ahorraría
eso y agregaría lo que este repositorio ya sabe que duele: una copia que se
queda vieja sin avisar. Se arma cada vez y siempre corresponde a lo que hay en
`base/`.

**De qué se ocupa y de qué no.** Recupera de los capítulos que al arrancar solo
llegan como índice (`02` en adelante), más las **blindadas** del núcleo cuando
el mensaje nombra una acción que no se deshace. Los capítulos `00` y `01` no se
recuperan por semejanza: esos rigen todos los turnos y no dependen del tema.

**La derogada nunca va sola.** Inyectar una regla que dejó de regir es peor que
no inyectar ninguna, así que va marcada y con su reemplazo al lado, o no va.
"""
import os
import re
import unicodedata

import comun
import metareglas
from comun import RAIZ

# Cuánto se permite inyectar por turno. El recordatorio fijo del enganche pesa
# menos de 1 KB, así que esto es el grueso de lo que se agrega a un mensaje.
TOPE = 10 * 1024

# Un identificador citado en el mensaje: `02·F24`, `F24`, `13·DOC22`. Se acepta
# solo si existe en el índice, que es lo que descarta un `B2C` o un `PPT`.
_CITA = re.compile(r"(?:(\d{2})·)?\b([A-Z]{1,4}\d+(?:\.\d+)?)\b")

# Palabras que no distinguen nada y ensucian el puntaje.
_VACIAS = frozenset("""
para pero porque como cuando donde desde hasta sobre entre cada todo toda
todos todas este esta estos estas ese esa esos esas aquel esto eso nada algo
alguien alguno alguna cual cuales quien quienes cuanto cuanta mucho mucha
poco poca otro otra otros otras mismo misma tanto tanta segun ademas tambien
solo solamente siempre nunca ahora luego antes despues entonces aunque
mientras sino salvo hacer hace hecho haces haber habia tiene tienen tener
puede pueden poder debe deben deber estar estan estado siendo ser soy eres
que los las del con por una uno unos unas sus mis tus nos les lles
favor gracias entiendo entonces bueno bien mal ver vea vean mira miren
archivo archivos carpeta carpetas proyecto proyectos regla reglas estandar
cambio cambios cambiar cambie cambia nuevo nueva nuevos nuevas viejo vieja
cosa cosas forma formas parte partes punto puntos caso casos tema temas
trabajo trabajar tarea tareas detecta detectar detecto funciona funcionar
sirve sirven queda quedar quedo agente herramienta esto eso aquello
""".split())

# **De dónde sale esta lista.** No de una teoría del idioma: de ver qué
# traía de más. El 2026-09-16, la pregunta «¿ya detecta el nuevo cambio?»
# recuperó `D2`, `T1`, `G6` y `EST1`, ninguna de ellas del tema, porque
# «cambio» está en el título de medio estándar. Una palabra que aparece en
# todas partes no distingue nada, y el ruido enseña a ignorar el aviso.

# Lo que **no se puede fallar**: el mensaje nombra una acción de las que no se
# deshacen, o un tema con capítulo propio. La semejanza de palabras acierta
# casi siempre y «casi» no alcanza para `N4`, así que estas van por lista.
#
# Cada entrada es `(términos, identificadores o capítulos)`. Un capítulo trae
# sus reglas vigentes; un identificador, esa sola.
DISPARADORES = (
    (("commit", "commitear", "push", "pushear", "rama", "ramas", "git",
      "versionar", "subir"), ("N2", "09")),
    (("borrar", "borre", "eliminar", "elimine", "truncar", "vaciar",
      "migrar", "migracion", "produccion", "restaurar", "respaldo"),
     ("N4", "N5", "N7", "03")),
    (("credencial", "credenciales", "clave", "claves", "contrasena",
      "token", "secreto", "secretos", "llave"), ("N6", "04")),
    (("publicar", "instalar", "desinstalar", "descargar", "externo",
      "internet", "servicio"), ("N8", "10")),
    (("prueba", "pruebas", "test", "tests", "suite", "cobertura"), ("08",)),
    (("documentar", "documento", "documentacion", "readme", "especificacion",
      "glosario", "trazabilidad", "historia", "epica"), ("13",)),
    (("plan", "planear", "planificar", "fase", "fases", "etapa", "alcance"),
     ("02",)),
    (("seguridad", "vulnerabilidad", "inyeccion", "permiso", "permisos",
      "autenticacion", "autorizacion"), ("04",)),
    (("privacidad", "personales", "cedula", "anonimizar", "enmascarar"),
     ("12",)),
    (("error", "errores", "excepcion", "log", "logs", "registro"), ("05",)),
    (("rendimiento", "lento", "lentitud", "consulta", "consultas", "indice"),
     ("06",)),
    (("dependencia", "dependencias", "paquete", "paquetes", "libreria",
      "version"), ("10",)),
    (("configuracion", "entorno", "entornos", "variable", "variables"),
     ("11",)),
    (("refactor", "refactorizar", "limpieza", "duplicado", "complejidad"),
     ("07", "14")),
    (("interfaz", "pantalla", "boton", "formulario", "usabilidad"), ("17",)),
    (("despliegue", "desplegar", "servidor", "contenedor", "docker"), ("18",)),
    (("observabilidad", "monitoreo", "metrica", "metricas", "alerta"), ("19",)),
)

# Los capítulos que rigen todos los turnos. No se recuperan por semejanza: al
# arrancar llegan enteros, y el enganche de cada turno recuerda los suyos.
SIEMPRE = ("00", "01")


def _limpio(texto):
    """Minúsculas y sin tildes, que es como se comparan dos palabras acá."""
    sin = unicodedata.normalize("NFKD", texto or "")
    sin = "".join(c for c in sin if not unicodedata.combining(c))
    return sin.lower()


def _terminos(texto):
    """Las palabras con las que vale la pena comparar."""
    return {p for p in re.findall(r"[a-z]{4,}", _limpio(texto))
            if p not in _VACIAS}


def indice(raiz=None):
    """`{id: regla}` de todas las reglas de `base/`, como las lee `metareglas`."""
    return {r.id: r for r in metareglas.reglas(raiz or RAIZ)}


def _ejemplo(regla):
    """El bloque `INCORRECTO / CORRECTO` de la regla, o `""`.

    **`regla.ejemplo` es un booleano**, no el texto: dice si la regla trae
    ejemplo, que es lo que el checklist necesita saber. El texto hay que
    sacarlo del archivo, y vale la pena: el ejemplo es la mitad que evita
    interpretar mal el cuerpo.
    """
    dentro, bloque = False, []
    for linea in (regla.texto or "").splitlines():
        if linea.startswith("```"):
            if dentro:
                break
            dentro = True
            continue
        if dentro:
            bloque.append(linea)
    texto = "\n".join(bloque).strip()
    return texto if "INCORRECTO" in texto else ""


def _cuerpo(regla):
    """Lo que se inyecta de una regla: encabezado, cuerpo y ejemplo.

    **Sin el sello del checklist**, por lo mismo que lo quita `cargador.py`: es
    el registro de que alguien la revisó, y no le sirve a quien tiene que
    obedecerla.
    """
    partes = [regla.encabezado.strip()]
    partes += [t for _, t in regla.cuerpo]
    ejemplo = _ejemplo(regla)
    if ejemplo:
        partes.append("```\n" + ejemplo + "\n```")
    return "\n".join(p for p in partes if p).strip()


def _citadas(mensaje, idx):
    """Los identificadores que el mensaje nombra, si de verdad existen."""
    encontrados = []
    for m in _CITA.finditer(mensaje or ""):
        id = m.group(2)
        if id in idx and id not in encontrados:
            encontrados.append(id)
    return encontrados


def _de_los_disparadores(terminos, idx):
    """Lo que la lista obliga a traer: `({id: motivo}, {capitulo: motivo})`.

    **Un capítulo no entra entero.** «commit» traía las once reglas del `09`,
    que es casi lo mismo que mandar el índice y deja al agente buscando. El
    capítulo entra como tema, y después se eligen sus mejores reglas contra el
    mensaje. Lo que sí entra completo es el identificador nombrado acá: `N4` no
    se decide por semejanza.
    """
    obligados, capitulos = {}, {}
    for palabras, destinos in DISPARADORES:
        cuales = terminos.intersection(palabras)
        if not cuales:
            continue
        motivo = "el mensaje dice «%s»" % "», «".join(sorted(cuales))
        for destino in destinos:
            if len(destino) == 2 and destino.isdigit():
                capitulos.setdefault(destino, motivo)
            elif destino in idx:
                obligados.setdefault(destino, motivo)
    return obligados, capitulos


def _por_semejanza(terminos, idx, capitulo=None):
    """`{id: puntaje}` por las palabras que comparten mensaje y regla.

    El título pesa más que el cuerpo: una palabra en el título dice de qué
    trata la regla, y en el cuerpo puede ser del ejemplo.
    """
    puntajes = {}
    for id, regla in idx.items():
        if regla.derogada:
            continue
        if capitulo is None and regla.capitulo in SIEMPRE:
            continue
        if capitulo is not None and regla.capitulo != capitulo:
            continue
        del_titulo = terminos.intersection(_terminos(regla.titulo))
        del_cuerpo = terminos.intersection(
            _terminos(" ".join(t for _, t in regla.cuerpo)))
        punto = 6 * len(del_titulo) + len(del_cuerpo - del_titulo)
        if punto:
            puntajes[id] = punto
    return puntajes


def _cadena(ids, idx):
    """Lo que las elegidas extienden, derogan o de lo que dependen.

    Sin esto se inyecta media cadena: la regla que dice «extiende `C7`» sin
    `C7` al lado obliga a suponer qué decía la otra.
    """
    salida = {}
    for id in ids:
        regla = idx.get(id)
        if not regla:
            continue
        for forma, otro in metareglas._dependencias(regla):
            if otro in idx and otro not in ids:
                salida.setdefault(otro, "%s `%s`" % (forma, id))
    return salida


def _orden(id, idx):
    """La precedencia: primero el núcleo, después por capítulo."""
    regla = idx[id]
    return (0 if regla.blindada else 1, regla.capitulo, regla.linea)


def elegir(mensaje, raiz=None, tope=TOPE):
    """`(elegidas, descartadas, temas)` para este mensaje.

    `elegidas` es `[(id, motivo)]` en orden de precedencia y ya recortado al
    presupuesto. `descartadas` es lo que quedó afuera por el tope. `temas` son
    los capítulos que el mensaje nombró y de los que **ninguna** regla destacó:
    van como puntero, porque decir «el capítulo 09 rige esto» es más honesto
    que mandar sus once reglas o que callar.

    Las tres se devuelven **por escrito**: un recuperador que no dice qué dejó
    afuera repite el defecto del arranque, que fallaba en silencio.
    """
    idx = indice(raiz)
    terminos = _terminos(mensaje)

    motivos = {}
    for id in _citadas(mensaje, idx):
        motivos[id] = "el mensaje la cita"

    obligados, capitulos = _de_los_disparadores(terminos, idx)
    for id, motivo in obligados.items():
        motivos.setdefault(id, motivo)

    # De cada capítulo disparado por tema, sus tres mejores contra el mensaje.
    # Si ninguna destaca, el capítulo queda como puntero y no como volcado.
    temas = {}
    for capitulo, motivo in capitulos.items():
        mejores = sorted(_por_semejanza(terminos, idx, capitulo).items(),
                         key=lambda p: -p[1])[:3]
        mejores = [(i, p) for i, p in mejores if p >= 6]
        if not mejores:
            temas[capitulo] = motivo
            continue
        for id, _ in mejores:
            motivos.setdefault(id, motivo)

    # La semejanza suelta aporta las mejores, y solo si el título coincide:
    # abrirle la puerta a todas las que comparten una palabra del cuerpo
    # devuelve medio estándar.
    for id, punto in sorted(_por_semejanza(terminos, idx).items(),
                            key=lambda p: -p[1])[:4]:
        if punto >= 6:
            motivos.setdefault(id, "coincide con su título")

    for id, motivo in _cadena(list(motivos), idx).items():
        motivos.setdefault(id, motivo)

    # La derogada no va: su reemplazo ya entró por la cadena, y mandar las dos
    # obliga a adivinar cuál rige.
    for id in list(motivos):
        if idx[id].derogada:
            del motivos[id]

    elegidas, descartadas, gasto = [], [], 0
    for id in sorted(motivos, key=lambda i: _orden(i, idx)):
        pieza = len(_cuerpo(idx[id]).encode("utf-8")) + 64
        if gasto + pieza > tope:
            descartadas.append(id)
            continue
        elegidas.append((id, motivos[id]))
        gasto += pieza
    return elegidas, descartadas, temas


def como_texto(mensaje, raiz=None, tope=TOPE):
    """El bloque que se le inyecta al agente, o `""` si el mensaje no pide nada.

    **Dice qué trae y por qué.** Un recuperador que entrega reglas sin decir
    cuáles eligió no se puede auditar, y el turno siguiente no sabe si trabajó
    con la regla o sin ella.
    """
    idx = indice(raiz)
    elegidas, descartadas, temas = elegir(mensaje, raiz, tope)
    if not elegidas and not temas:
        return ""

    lineas = ["[REGLAS QUE PIDE ESTA SOLICITUD, RECUPERADAS Y OBLIGATORIAS]",
              "Rigen esta respuesta igual que las del arranque. Ante cualquier "
              "choque gana el núcleo, y el desempate es el de `20·M6`.",
              ""]
    for id, motivo in elegidas:
        regla = idx[id]
        sello = " `[BLINDADA]`" if regla.blindada else ""
        lineas.append("<<< %s·%s%s  ·  %s >>>" % (regla.capitulo, id, sello,
                                                  motivo))
        lineas.append(_cuerpo(regla))
        lineas.append("")
    if temas:
        lineas.append("[CAPÍTULOS QUE ESTE MENSAJE TOCA, SIN CARGAR]")
        for capitulo, motivo in sorted(temas.items()):
            lineas.append("  base/%s  (%s). Leerlo con Read antes de tocar "
                          "su tema." % (capitulo, motivo))
        lineas.append("")
    if descartadas:
        lineas.append("[NO CUPO EN EL PRESUPUESTO]")
        lineas.append("  " + ", ".join(sorted(descartadas))
                      + ". Leerlas con Read antes de tocar su tema.")
    return "\n".join(lineas).strip()


if __name__ == "__main__":
    comun.no_es_punto_de_entrada("recuperar")
