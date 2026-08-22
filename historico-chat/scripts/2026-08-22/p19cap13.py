# -*- coding: utf-8 -*-
import sys, os, glob
sys.path.insert(0, r"C:/Users/user/AppData/Local/Temp/claude/c--Ing--Jose-ia-agente/563dc2f9-c782-46f9-af82-c9bc948b3566/scratchpad")
import p19lib as L
os.chdir(r"c:\Ing. Jose\ia\agente")


def poner_exigencia(archivo, rid, nuevo, nota):
    s = L.leer(archivo)
    ini, fin, _ = L.bloque(s, rid)
    b = s[ini:fin]
    cl = b.find("### Checklist")
    tras = b.find("\n", 0)
    cortes = [i for i in (b.find("\n**Excepción", 0, cl), b.find("\n```", 0, cl)) if i > 0]
    b = b[:tras] + "\n\n" + nuevo.strip() + "\n" + b[min(cortes):]
    L.escribir(archivo, s[:ini] + L.resellar(b, archivo, nota) + s[fin:])


R = "base/13-documentacion/reglas/"
P = "../../../plantillas/ciclo-vida-proyectos/"
F12 = "[`02·F12`](../../02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md), punto 13"
N13 = ("**Recortada al molde el 2026-08-22 (pendiente 19, capítulo `13`):** el sello decía \u2705 en la fila 10 "
       "con el cuerpo pasado de 320; ahora cabe. Lo que salió era porqué o detalle que ya vive en otro archivo, "
       "y queda en [notas/porques-recortados-al-molde.md](../../../notas/porques-recortados-al-molde.md).")

C13 = {
 "DOC5": "Lo que no se reconstruye leyendo el código —una decisión y su motivo, un error resuelto, un supuesto, una alternativa descartada— se registra como **señal**: qué pasó · por qué · dónde · qué se aprendió, con su tipo y a quién sirve. La revertida no se borra: se marca reemplazada y enlaza a la nueva.",
 "DOC7": "Cuando el documento de un módulo consume a otro, el que referencia declara **qué consume y por qué**, y el referenciado registra la recepción en su historial cruzado: fecha, de dónde vino, qué cambió. Los dos lados o ninguno. La mención de paso no cuenta: es analogía, no dependencia.",
 "DOC9": "Al planificar una unidad de trabajo se lee primero el mapa de dependencias del proyecto, cuya ruta declara la capa 3, y se explora el código solo si el mapa no cubre la duda o no coincide con lo que hay. El mapa es la fuente autoritativa de cómo está armado el sistema hoy.",
 "DOC10": "Toda regla que solo vale para este proyecto se escribe en su catálogo, cuya ruta declara la capa 3, numerada `P1`, `P2` y así, para poder citarla; cada `P` que nace o se endurece deja su señal ([`DOC5`](DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)). La que se promueve a `base/` conserva solo su matiz y enlaza a la regla base.",
 "DOC11": "La verificación que exige [`DOC3`](DOC3-verifica-la-trazabilidad-especificacion-implementacion-antes-de-cerrar.md) se escribe en el documento de cierre con la [tabla canónica de cinco columnas](../tabla-de-trazabilidad.md), y todo lo que no sea \u2705 lleva su justificación escrita; el faltante que era de esta unidad se corrige acá, no se difiere.",
 "DOC12": "Toda fase nueva abre declarando de dónde sale, en una de tres formas: **modifica** fases anteriores, nombrándolas; **agrega** lo que no existía; o **ambas**. El formato del bloque está en [`plantillas/ciclo-vida-proyectos/05-fase.md`](" + P + "05-fase.md) y la carpeta de la fase repite el ORIGEN de su especificación.",
 "DOC13": "Un módulo nuevo —dominio funcional propio, con su prefijo de rutas o su especificación separada— se registra en el catálogo de módulos **antes de cerrar** la unidad que lo creó, con lo que pide [`plantillas/catalogo-modulos.md`](../../../plantillas/catalogo-modulos.md). No cuentan la fase de un módulo que ya existe, el arreglo interno ni el componente hijo.",
 "DOC15": "Toda HU se parte de [`plantillas/ciclo-vida-proyectos/04-HU.md`](" + P + "04-HU.md), leída del estándar **cada vez**, y se guarda versionada donde fija " + F12 + ". Se rellena con contenido real: rol concreto, criterios que cubran camino feliz, error y caso borde, sin secciones a medio llenar.",
 "DOC16": "Toda épica se parte de [`plantillas/ciclo-vida-proyectos/03-epica.md`](" + P + "03-epica.md), leída del estándar cada vez, y se guarda donde fija " + F12 + ". Sus criterios son de resultado, no de pantalla, y el enlace con cada HU se escribe en los dos lados (depende de [`02·F0`](../../02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md)).",
 "DOC17": "Ninguna carpeta del árbol de épicas, HU y fases (" + F12 + ") queda muda: cada una tiene un `README.md` que lista **su contenido inmediato**, no el árbol entero, con una frase de qué es cada cosa. Se actualiza en el mismo cambio que crea, mueve o cierra algo.",
 "DOC19": "Todo espacio que quien usa un modelo tiene que reemplazar se marca `«…»`, la misma marca en todos los modelos del proyecto. Se marca lo que llena quien usa el modelo: la sintaxis de un comando que se copia y se pega la llena quien lo corre, y no es un espacio por llenar.",
 "DOC20": "Un documento que salió de un modelo y conserva una sola marca `«…»` sin reemplazar no está terminado y no se presenta como tal: se completa, o se dice qué falta y dónde (depende de [`DOC19`](DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md)). Vale para todo documento que alguien vaya a leer como trabajo cerrado.",
 "DOC22": "Cada sesión deja su resumen en un documento aparte de la transcripción, escrito con el modelo del estándar y llenado **en el momento en que aparece cada hallazgo**, no al cerrar. Cada hallazgo dice si quedó resuelto o abierto, dónde quedó, qué trabajo dispara y con qué pregunta se retoma.",
}
for rid, cuerpo in C13.items():
    poner_exigencia(glob.glob(R + rid + "-*.md")[0], rid, cuerpo, N13)

L.escribir("base/13-documentacion/tabla-de-trazabilidad.md", """# La tabla canónica de trazabilidad  ·  anexo de `13·DOC11`

> Anexo del capítulo [`13 · Documentación`](base.md). **No es una regla**: no lleva molde ni identificador propio. Es la tabla que [`DOC11`](reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md) manda usar, escrita una sola vez para que no se copie con variaciones.

Se escribe en el documento de cierre de la unidad, con estas cinco columnas y en este orden:

| Ítem de la especificación | Categoría | Ubicación esperada | Estado | Evidencia |
|---|---|---|---|---|
| (frase de la especificación) | (esquema · modelo · servicio · vista · prueba · permiso · ruta · doc) | (archivo real) | \u2705 · \u274c · N/A · parcial | (prueba concreta o commit) |

**Qué se espera de cada estado.** El \u2705 no lleva nada más. El \u274c dice a qué unidad se traslada lo que falta. El **parcial** dice qué parte queda. El **N/A** dice por qué no aplica: un «N/A porque sí» no es justificación.

**Un faltante que debía estar en esta unidad se corrige acá**, no se difiere: diferir es para lo que pertenece a otra unidad.
""")

b13 = "base/13-documentacion/base.md"
s = L.leer(b13)
if "tabla-de-trazabilidad.md" not in s:
    L.escribir(b13, s.rstrip() + "\n\n**Anexo del capítulo:** [la tabla canónica de trazabilidad](tabla-de-trazabilidad.md), que [`DOC11`](reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md) manda usar al cerrar una unidad.\n")

N03 = N13.replace("capítulo `13`", "capítulo `03`").replace("../../../notas/", "../notas/")
poner_exigencia("base/03-datos.md", "D1", "Un dato no se repite ni se guarda en montón: nada de columnas que contienen varios valores, nada de copiar atributos del padre, y nada de valores fijos incrustados en el tipo de la columna, que van a catálogo ([`D4`](#d4--lo-que-puede-cambiar-por-decisión-de-alguien-va-a-catálogo)). Lo uno a muchos va en tabla hija; lo muchos a muchos, en una que las une.", N03)
poner_exigencia("base/03-datos.md", "D9", "Cuando dos procesos pueden tocar el mismo dato a la vez, la integridad se **protege en el almacén**: el valor compartido se actualiza de forma atómica o revalidando la versión al guardar, y la unicidad la garantiza una restricción del propio almacén, porque comprobarla antes de insertar no alcanza.", N03)

N20 = N13.replace("capítulo `13`", "capítulo `20`")
poner_exigencia(glob.glob("base/20-meta-reglas/reglas/M16-*.md")[0], "M16",
 "Cada regla del catálogo de un proyecto ([`13·DOC10`](../../13-documentacion/reglas/DOC10-registra-en-el-catalogo-del-proyecto-toda-regla-propia.md)) declara, con su enlace ([`M15`](M15-toda-cita-a-otra-regla-lleva-su-enlace.md)), la regla de `base/` cuyo criterio concreta o endurece (extiende [`M1`](M1-la-jerarquia-tiene-cuatro-niveles-y-un-solo-orden.md)). Si ninguna la cubre, la de base se escribe primero; hasta entonces la de proyecto no se publica.", N20)

m6 = glob.glob("base/20-meta-reglas/reglas/M6-*.md")[0]
s = L.leer(m6)
ini, fin, _ = L.bloque(s, "M6")
b = s[ini:fin]
cl = b.find("### Checklist")
lista = b[b.find("1. **¿Una es"):b.find("\n```", 0, cl)].strip()
L.escribir("base/20-meta-reglas/desempate.md", """# El orden del desempate  ·  anexo de `20·M6`

> Anexo del capítulo [`20 · Meta-reglas`](base.md). **No es una regla**: no lleva molde ni identificador propio. Es el orden que [`M6`](reglas/M6-ante-un-conflicto-el-desempate-es-este-y-en-este-orden.md) manda seguir, escrito aparte para que la regla quepa en su molde y el orden no se resuma nunca.

Se recorre **de arriba abajo** y se para en el primero que aplique:

""" + lista + """

**El paso 6 es el que importa.** Los cinco primeros resuelven; el sexto reconoce que el estándar tiene un defecto, y ahí la salida no es elegir: es pausar, reportar el choque y arreglar la regla.
""")
poner_exigencia(m6, "M6",
 "Ante un choque entre dos reglas, el desempate se resuelve por el [orden del anexo](../desempate.md), de arriba abajo, parando en el primero que aplique. Está prohibido elegir en silencio o inventar un tercer camino: si sigue empatado es un defecto del estándar, así que se **pausa**, se reporta y se arregla la regla.",
 "**Partida en regla y anexo el 2026-08-22 (pendiente 19, capítulo `20`):** el sello decía \u2705 en la fila 10 con 725 caracteres, más del doble del molde, porque la regla era una lista de seis pasos. Los seis quedan **enteros y sin reescribir** en el [anexo del capítulo](../desempate.md), como se hizo con [`02·F12`](../../02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md), y la regla se queda con la exigencia: se resuelve por ese orden y no se elige en silencio.")
print("listo")
