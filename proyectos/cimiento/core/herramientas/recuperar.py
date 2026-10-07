"""Qué reglas pide **esta** solicitud del usuario.

**El problema que cierra.** Al abrir la sesión no se cargan las reglas: la
herramienta acepta 10.000 caracteres por enganche y el cuerpo de reglas pesa
mucho más (`EP-005·HU-009·CA-04`). Si leerlas dependiera de que el agente se
acuerde, trabajaría sin la regla y nadie se enteraría.

**Lo que hace.** Lee el mensaje del usuario, reconoce qué tareas pide y le
entrega al agente las reglas que el mapa de tareas pone bajo ellas: las de las
tareas que van en **todo** mensaje, con su título y dónde viven, y las de las
tareas que **este** mensaje pide, completas mientras quepan en el presupuesto y
nombradas las que no quepan.

**Por qué por tareas y no por semejanza** (`EP-005·HU-023`, fase `B`). Hasta el
2026-09-28 elegía comparando palabras del mensaje con el título de cada regla, y
con los mensajes reales de esa sesión falló: «suba a git» no trajo nada y un
pedido de redacción trajo una regla de índices. Cada regla dice ahora a qué
tareas aplica, y las palabras que señalan cada tarea están escritas en
`base/tareas.md`: no hay nada que adivinar.

**La derogada nunca va.** Inyectar una regla que dejó de regir es peor que no
inyectar ninguna.
"""
import os
import re
import unicodedata

from ..comun import Archivos, Proyecto
from ..validadores.metareglas import CuerpoDeReglas
from .mapa_tareas import MapaDeTareas

# Cuánto se permite inyectar por turno. Por encima de 10 KB la herramienta deja
# ver solo el comienzo; el enganche le suma su recordatorio y la medición de la
# respuesta anterior, que juntos no pasan de 1 KB (medido el 2026-09-28).
TOPE = 10 * 1024 - 1536

# Un identificador citado en el mensaje: `02·F24`, `F24`, `13·DOC22`. Se acepta
# solo si existe en el índice, que es lo que descarta un `B2C` o un `PPT`.
_CITA = re.compile(r"(?:(\d{2})·)?\b([A-Z]{1,4}\d+(?:\.\d+)?)\b")

# La marca del encabezado no hace falta en el bloque de todo mensaje.
_MARCA = re.compile(r"\s*(`\[[^\]]+\]`|\*opt-in\*)\s*$")

# Lo que el editor le agrega al mensaje sin que el usuario lo escriba: «qué
# sigue?» traía reglas de documentos porque la ruta del archivo abierto decía `.md`.
_DEL_EDITOR = re.compile(r"<(ide_[a-z_]+|system-reminder)>.*?</\1>", re.S)

# Donde empieza una frase: el comienzo del mensaje, o después de un punto, un
# signo de cierre o un salto de línea.
_FRASE = re.compile(r"(?:^|[.!?\n])\s*[¿¡«\"'(]*\s*([a-z0-9]+)")

PALABRAS = "base/01-conducta/palabras-clave.md"

# Una fila de la lista cerrada: la palabra en negrita y, si trae, sus otras
# formas después de la coma («**Hágalo**, aplique»).
_FILA_PALABRA = re.compile(r"^\|\s*\*\*([^*]+)\*\*([^|]*)\|")

# `EP-026·HU-004` · Sin base no hay estándar: no se trabaja (acuerdo 9).
SIN_BASE = ("[SIN BASE NO HAY REGLAS: NO SE TRABAJA]\n"
            "La base de Cimiento no responde (%s), y de ella salen las reglas. No hacer "
            "nada que cambie el proyecto: decirle al usuario, en una línea, que la base no "
            "responde y que hay que prenderla. El freno no deja modificar mientras tanto.")

_ENCABEZADO = ("[REGLAS QUE PIDE ESTA SOLICITUD, RECUPERADAS Y OBLIGATORIAS]\n"
               "Rigen esta respuesta. Ante cualquier "
               "choque gana el núcleo, y el desempate es el de `20·M6`.\n")


class RecuperadorDeReglas:
    """Elige y arma las reglas que se le entregan al agente con cada mensaje."""

    def __init__(self, raiz=None, archivos=None):
        self.raiz = raiz or Proyecto.estandar()
        # `EP-026·HU-004` · El estándar se lee de la base. Sin base no hay reglas
        # que dar, y `como_texto` lo dice (análisis 1 del pendiente 132, acuerdo 9).
        self.sin_base = ""
        if archivos is None:
            from ..enganches.niveles import BaseSinRespuesta
            from ..estandar.en_base import fuente
            try:
                archivos = fuente(self.raiz)
            except BaseSinRespuesta as error:
                self.sin_base = str(error)
                archivos = Archivos()
        self.archivos = archivos
        self.mapa = MapaDeTareas(self.raiz, self.archivos)
        self._capitulos = {}

    def capitulo(self, regla):
        """El capítulo de la regla, calculado una vez: `Regla.capitulo` resuelve su
        ruta en disco, y la medición de `elegir` lo pide miles de veces por mensaje."""
        clave = (regla.archivo, regla.id)
        if clave not in self._capitulos:
            self._capitulos[clave] = regla.capitulo
        return self._capitulos[clave]

    # ── el texto del mensaje ──────────────────────────────────────────────

    @staticmethod
    def limpio(texto):
        """Minúsculas y sin tildes, que es como se comparan dos palabras acá."""
        sin = unicodedata.normalize("NFKD", texto or "")
        sin = "".join(c for c in sin if not unicodedata.combining(c))
        return sin.lower()

    @classmethod
    def palabras(cls, texto):
        """Todas las palabras, de cualquier largo: «git» cuenta igual que «commit»."""
        return set(re.findall(r"[a-z0-9]+", cls.limpio(texto)))

    @staticmethod
    def lo_que_escribio(mensaje):
        """El mensaje sin lo que agregó el editor."""
        return _DEL_EDITOR.sub(" ", mensaje or "")

    @classmethod
    def palabras_de_inicio(cls, mensaje):
        """La primera palabra de cada frase del mensaje, sin tildes y en minúscula."""
        return [m.group(1) for m in _FRASE.finditer(cls.limpio(mensaje))]

    # ── el proyecto ───────────────────────────────────────────────────────

    @classmethod
    def opt_in_apagados(cls, proyecto, archivos=None, configuracion=None):
        """Los capítulos opt-in que este proyecto tiene apagados.

        `EP-026·HU-009` · De la base de Cimiento, si lo tiene registrado. Si no, o
        si no responde, de su `CLAUDE.md`. Sin proyecto o sin archivo no se apaga
        nada: se prefiere ofrecer de más antes que callar una regla que sí rige."""
        if not proyecto:
            return frozenset()
        from ..enganches.configuracion import ConfiguracionDelProyecto
        from ..proyectos import opt_in

        configuracion = configuracion or ConfiguracionDelProyecto(proyecto)
        efectivos = configuracion.efectivos()
        if configuracion.registrado:
            return opt_in.apagados_segun(efectivos)
        return frozenset(c for c, prendido in opt_in.del_claude_md(proyecto, archivos or Archivos()).items()
                         if not prendido)

    # ── las reglas y las palabras ─────────────────────────────────────────

    def indice(self):
        """`{id: regla}` de todas las reglas de `base/`."""
        return {r.id: r for r in CuerpoDeReglas.leer(self.raiz, self.archivos)}

    def palabras_de_la_lista(self):
        """`[palabra]` de `01·C28`, en el orden de la lista y como se escriben."""
        texto = self.archivos.leer(os.path.join(self.raiz, *PALABRAS.split("/")))
        salida = []
        for linea in texto.splitlines():
            m = _FILA_PALABRA.match(linea.strip())
            if m:
                salida.append(m.group(1).strip())
                salida += [p.strip() for p in m.group(2).split(",") if p.strip()]
        return salida

    def palabra_clave(self, mensaje):
        """`EP-025·HU-010` · La palabra de `01·C28` con que abre el mensaje, como la
        escribe la lista en su primera columna («aplique» da «Hágalo»), o ""."""
        texto = self.archivos.leer(os.path.join(self.raiz, *PALABRAS.split("/")))
        principal = {}
        for linea in texto.splitlines():
            m = _FILA_PALABRA.match(linea.strip())
            if m:
                nombre = m.group(1).strip()
                for variante in [nombre] + [p.strip() for p in m.group(2).split(",") if p.strip()]:
                    principal.setdefault(self.limpio(variante), nombre)
        for palabra in self.palabras_de_inicio(self.lo_que_escribio(mensaje)):
            if palabra in principal:
                return principal[palabra]
        return ""

    def trae_palabra_clave(self, mensaje):
        """¿Alguna frase del mensaje abre con una palabra de `01·C28`?"""
        lista = {self.limpio(p) for p in self.palabras_de_la_lista()}
        return bool(lista & set(self.palabras_de_inicio(self.lo_que_escribio(mensaje))))

    def aviso_sin_palabra(self):
        """`EP-005·HU-023` · Lo que recibe el agente cuando el mensaje no trae la
        palabra: no actúa, recuerda la lista y espera (pedido del 2026-09-29)."""
        lista = ", ".join("«%s»" % p for p in self.palabras_de_la_lista())
        return ("[EL MENSAJE NO ABRE CON UNA PALABRA DE `01·C28`]\n"
                "No hacer nada: recordarle al usuario, en una línea, que falta la "
                "palabra que dice qué se espera, y esperar su respuesta. Las "
                "palabras son: " + lista + ".")

    def tareas_del_mensaje(self, mensaje):
        """`{tarea: palabras clave que la piden}`, sin las que van siempre.

        `EP-005·HU-023·RN-07` · **Solo cuenta la palabra clave** de `01·C28`, y solo
        abriendo el mensaje o una de sus frases: «reglas» en una pregunta traía
        las reglas de cambiar el estándar.
        """
        dichas = set(self.palabras_de_inicio(self.lo_que_escribio(mensaje)))
        salida = {}
        for tarea, suyas in self.mapa.palabras_clave().items():
            comunes = dichas & suyas
            if comunes:
                salida[tarea] = comunes
        return salida

    @staticmethod
    def citadas(mensaje, idx):
        """Los identificadores que el mensaje nombra, si de verdad existen."""
        encontrados = []
        for m in _CITA.finditer(mensaje or ""):
            id = m.group(2)
            if id in idx and id not in encontrados:
                encontrados.append(id)
        return encontrados

    @staticmethod
    def cadena(ids, idx):
        """Lo que las elegidas extienden, derogan o de lo que dependen."""
        salida = {}
        for id in ids:
            regla = idx.get(id)
            if not regla:
                continue
            for forma, otro in CuerpoDeReglas.dependencias(regla):
                if otro in idx and otro not in ids:
                    salida.setdefault(otro, "%s `%s`" % (forma, id))
        return salida

    # ── elegir ────────────────────────────────────────────────────────────

    def elegir(self, mensaje, tope=TOPE, proyecto=None):
        """`(elegidas, descartadas, siempre)` para este mensaje.

        - `elegidas`: `[(id, motivo)]` que entran completas, ya recortadas al
          presupuesto que deja el bloque de `siempre`.
        - `descartadas`: las de las tareas del mensaje que no cupieron. Van
          **nombradas**: callar lo que quedó afuera repite el defecto del arranque.
        - `siempre`: `[id]` de las reglas de las tareas que van en todo mensaje.
        """
        mensaje = self.lo_que_escribio(mensaje)
        idx = self.indice()
        por_tarea = self.mapa.reglas_por_tarea()
        apagados = self.opt_in_apagados(proyecto, self.archivos)

        def rige(id):
            return id in idx and not idx[id].derogada and self.capitulo(idx[id]) not in apagados

        fijas = []
        for tarea in self.mapa.siempre():
            for regla in por_tarea.get(tarea, []):
                if rige(regla.id) and regla.id not in fijas:
                    fijas.append(regla.id)

        # **La cita explícita manda:** si el mensaje nombra la regla, llega aunque
        # su capítulo opt-in esté apagado, con la advertencia al lado.
        motivos = {}
        for id in self.citadas(mensaje, idx):
            if idx[id].derogada:
                continue
            motivos[id] = "el mensaje la cita"
            if self.capitulo(idx[id]) in apagados:
                motivos[id] += " (capítulo opt-in, apagado en este proyecto)"
        del_mensaje = self.tareas_del_mensaje(mensaje)
        for tarea, comunes in del_mensaje.items():
            motivo = "tarea `%s`: palabra clave «%s»" % (tarea, "», «".join(sorted(comunes)))
            for regla in por_tarea.get(tarea, []):
                if rige(regla.id):
                    motivos.setdefault(regla.id, motivo)
        for id, motivo in self.cadena(list(motivos), idx).items():
            if rige(id):
                motivos.setdefault(id, motivo)

        # De lo que más pesa a lo que menos: lo citado, lo blindado, lo que rige
        # todo mensaje y después el orden de `base/`. Nada se ordena por parecido.
        def orden(id):
            regla = idx[id]
            citada = motivos[id].startswith("el mensaje la cita")
            return (0 if citada else 1, 0 if regla.blindada else 1,
                    0 if id in fijas else 1, self.capitulo(regla), regla.linea)

        # **Todo lo que se inyecta cuenta contra el tope**: se mide el texto que
        # de verdad saldría, regla por regla.
        candidatas = sorted(motivos, key=orden)
        elegidas = []

        # La que rige todo mensaje y no cupo completa ya llega en su bloque.
        def fuera(dentro):
            return [i for i in candidatas if i not in dentro and i not in fijas]

        for id in candidatas:
            prueba = elegidas + [(id, motivos[id])]
            resto = fuera({i for i, _ in prueba})
            if len(self.armar(prueba, resto, fijas, idx, list(del_mensaje)).encode("utf-8")) <= tope:
                elegidas = prueba
        return elegidas, fuera({i for i, _ in elegidas}), fijas

    # ── armar el texto ────────────────────────────────────────────────────

    def pieza(self, regla, motivo):
        """Lo que ocupa una regla completa: su línea de motivo y su cuerpo. Se mide
        el texto exacto: estimarlo dejaba el total unos bytes sobre el tope."""
        sello = " `[BLINDADA]`" if regla.blindada else ""
        return "<<< %s·%s%s  ·  %s >>>\n%s\n\n" % (self.capitulo(regla), regla.id, sello,
                                                   motivo, self.mapa.cuerpo(regla))

    def archivos_de_tareas(self, tareas):
        """Los archivos de reglas completas de esas tareas, relativos a la raíz."""
        salida = []
        for t in tareas:
            for ruta in self.mapa.archivos_de(t):
                salida.append(os.path.relpath(ruta, self.raiz).replace(os.sep, "/"))
        return salida

    def _donde(self, rutas):
        """`EP-026·HU-006` · Dónde leer las reglas completas: con el estándar en la
        base, con `ver_estandar`; los archivos de `base/` quedaron quietos."""
        texto = ", ".join(rutas)
        if hasattr(self.archivos, "recorrer"):
            return texto + "; se leen de la base con `manage.py ver_estandar <ruta>`"
        return texto

    def bloque_descartadas(self, ids, idx, tareas=()):
        """Las que no cupieron, y el archivo donde están completas."""
        if not ids:
            return ""
        donde = self._donde(self.archivos_de_tareas(tareas) or ["base/reglas-por-tarea/"])
        return ("[DE LAS TAREAS DE ESTE MENSAJE, NO CUPIERON: están completas en "
                + donde + "]\n  "
                + ", ".join("%s·%s" % (self.capitulo(idx[i]), i) for i in ids) + "\n")

    def bloque_siempre(self, fijas, idx):
        """Las reglas de todo mensaje: identificador y título. Sin la ruta de cada
        una, que la dice el mapa: así el bloque deja lugar a las de la tarea."""
        if not fijas:
            return ""
        donde = self._donde(self.archivos_de_tareas(self.mapa.siempre()))
        lineas = ["[LAS QUE RIGEN TODO MENSAJE: completas en %s]" % donde]
        for id in fijas:
            regla = idx[id]
            lineas.append("  %s·%s · %s" % (self.capitulo(regla), id, _MARCA.sub("", regla.titulo)))
        return "\n".join(lineas)

    def armar(self, elegidas, descartadas, fijas, idx, tareas=()):
        """El texto tal como se inyecta. Lo usan `como_texto` y la medición."""
        lineas = [_ENCABEZADO]
        for id, motivo in elegidas:
            lineas.append(self.pieza(idx[id], motivo).rstrip("\n") + "\n")
        if descartadas:
            lineas.append(self.bloque_descartadas(descartadas, idx, tareas))
        # La que ya va completa no se repite en el bloque de todo mensaje.
        completas = {i for i, _ in elegidas}
        bloque = self.bloque_siempre([i for i in fijas if i not in completas], idx)
        if bloque:
            lineas.append(bloque)
        return "\n".join(lineas).strip()

    def como_texto(self, mensaje, tope=TOPE, proyecto=None):
        """El bloque que se le inyecta al agente, o `""` si no hay reglas que dar.
        **Dice qué trae y por qué**: lo que no se explica no se puede auditar."""
        # `EP-005·HU-024` · Un aviso interno de Claude Code no lo escribió el usuario:
        # no se le aplican sus reglas ni el aviso de `01·C28`.
        from core.enganches.historico import es_aviso_interno
        if es_aviso_interno(mensaje):
            return ""
        if self.sin_base:
            return SIN_BASE % self.sin_base
        idx = self.indice()
        if not self.trae_palabra_clave(mensaje):
            # La regla que el mensaje cita llega igual: «00 id9» corrige la
            # respuesta anterior, y el agente necesita el texto de lo citado.
            piezas = [self.pieza(idx[i], "el mensaje la cita")
                      for i in self.citadas(self.lo_que_escribio(mensaje), idx)
                      if not idx[i].derogada]
            return (self.aviso_sin_palabra() + "\n\n" + "".join(piezas)).strip()
        elegidas, descartadas, fijas = self.elegir(mensaje, tope, proyecto)
        if not elegidas and not fijas:
            return ""
        return self.armar(elegidas, descartadas, fijas, idx, list(self.tareas_del_mensaje(mensaje)))
