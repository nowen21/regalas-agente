#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El estándar contra sus propias meta-reglas — capítulo `20`.

El [checklist del estándar](../base/20-meta-reglas/checklist.md) tiene veinte
filas y su §4 dice cuáles puede decidir un script solo: **5, 6, 7, 10, 12, 13,
14, 15, 18, 19 y 20**. Eso es exactamente lo que hace este validador, y por eso
no inventa criterios: la especificación ya estaba escrita.

| Fila | Meta-regla | Qué se comprueba aquí |
|---|---|---|
| 5 | `M3` | ninguna regla nombra lenguaje, framework, motor, nube ni herramienta |
| 6 | `M4` | el ID es `<PREFIJO><n>`, el prefijo es exclusivo del capítulo y está en la tabla de letras ocupadas |
| 7 | `M5` | el encabezado es `##` (o `#` si la regla ocupa su propio archivo) |
| 10 | `M5` | el cuerpo cabe en cuatro líneas |
| 12 | `M5` | está el ejemplo INCORRECTO / CORRECTO |
| 13 | `M5` | la marca es una de las tres de la lista cerrada |
| 14 | `M7` | la dependencia se declara en una de las tres formas, y el ID existe |
| 15 | `M7` | ninguna dependencia da vueltas en círculo ni manda sobre una `[BLINDADA]` |
| 18 | `M9` | la regla está clasificada en `validadores/reglas-validables.md` |
| 19 | `M10` | la versión de `VERSION` tiene su entrada en el `CHANGELOG.md` |
| 20 | `M4` | que las citas resuelvan ya lo comprueba `citas.py`; aquí no se repite |

Se suma `M14`: que la regla traiga su bloque de checklist con resultado y contra
qué versión se aplicó. Que de verdad haya recorrido los nueve pasos no lo decide
un script; que el bloque esté y diga qué dio, sí.

Las nueve filas que faltan (1, 2, 3, 4, 8, 9, 11, 16, 17) piden **leer y
entender** la regla. No se simulan aquí: una comprobación que se equivoca vale
menos que ninguna.

Corre **en seco**, sobre este mismo repositorio: no necesita ningún proyecto.
`M16` es la excepción y por eso vive aparte, en `validar.py metareglas --raiz
<proyecto>`: el catálogo de reglas propias vive en el proyecto.
"""
import os
import re
import subprocess

import comun
from comun import (AVISO, FALLA, Hallazgo, RAIZ, leer, lineas_utiles,
                   recorrer_md, relativo)

BASE = "base"
LETRAS = "base/20-meta-reglas/estructura-regla.md"
VALIDABLES = "validadores/reglas-validables.md"
CATALOGO_PROYECTO = ".agente/reglas-proyecto.md"

_REGLA = re.compile(r"^(#{1,2})\s+([A-Z]{1,4}\d+(?:\.\d+)?)\s*·\s*(.+?)\s*$")
_CERCA = re.compile(r"^\s*(```|~~~)")
_CHECKLIST = re.compile(r"(?m)^###\s+Checklist\s*·\s*\*\*(CUMPLE|NO CUMPLE)\*\*")
_CONTRA = re.compile(r"(?i)contra\s+\*\*v?([\d.]+)\*\*")

# La fecha del sello: «… contra **v20.0.1**, el **2026-08-16**.»
_SELLADO_EL = re.compile(r"(?i)contra\s+\*\*v?[\d.]+\*\*,?\s*el\s+\*\*(\d{4}-\d{2}-\d{2})\*\*")
_DEPENDENCIA = re.compile(r"\((extiende|depende de|deroga)\s+(?:`)?(?:(\d{2})·)?"
                          r"([A-Z]{1,4}\d+(?:\.\d+)?)(?:`)?\)")
_DEPENDENCIA_ENLAZADA = re.compile(
    r"\((extiende|depende de|deroga)\s+\[`(?:(\d{2})·)?"
    r"([A-Z]{1,4}\d+(?:\.\d+)?)`\]\([^)]*\)\)")
_MARCAS = ("[BLINDADA]", "*opt-in*")
# La marca de derogación admite citar más de una regla sucesora, y con capítulo
# o sin él: `[DEROGADA en 3.1.0 → ver F16 y F17]`, `[DEROGADA en 6.0.0 → ver
# 00·ID7]`. Lo que fija `M5` es la forma, no cuántas la reemplazan.
_DEROGADA = re.compile(r"\[DEROGADA en [\d.]+ → ver [^\]]+\]")

# Fila 10 · cuatro líneas del molde, a ochenta columnas, son 320 caracteres. Se
# mide así y no por saltos de línea porque el mismo cuerpo se escribe a veces en
# un renglón largo y a veces cortado, y eso no cambia lo que exige: que quepa.
LIMITE_CUERPO = 320

# El enlace se mide por lo que se lee, no por lo que se escribe: `[texto](destino)`
# cuenta como `texto`. Ver `Regla.largo()`.
_ENLACE_MD = re.compile(r"\[([^\]]*)\]\([^)]*\)")

# Fila 5 · nombres propios de tecnología. Lista corta y defendible: producto,
# marca o lenguaje concreto. No entran las palabras que el estándar ya adoptó
# como concepto propio (git, markdown) ni los formatos de datos.
_TECNOLOGIA = re.compile(
    r"(?i)(?<![\w-])("
    r"laravel|django|rails|symfony|spring|flask|fastapi|express|"
    r"node|node\.js|nodejs|deno|bun|dotnet|\.net|"
    r"softdeletes|"
    r"react|vue\.js|angular|svelte|next\.js|nuxt|"
    r"pytest|phpunit|jest|mocha|vitest|eslint|prettier|phpstan|ruff|flake8|"
    r"composer|npm|yarn|pnpm|pip|poetry|maven|gradle|"
    r"mysql|mariadb|postgres|postgresql|sqlite|oracle|mongodb|redis|"
    r"elasticsearch|kafka|rabbitmq|"
    r"aws|azure|heroku|vercel|netlify|cloudflare|"
    r"docker|kubernetes|terraform|ansible|jenkins|"
    r"eloquent|hibernate|prisma|sequelize|typeorm|alembic|"
    r"python|php|javascript|typescript|java|ruby|kotlin|swift"
    r")(?![\w-])")


class Regla:
    """Una regla de `base/`, con lo que hace falta para juzgarla."""

    def __init__(self, id, titulo, nivel, archivo, linea, encabezado):
        self.id = id
        self.titulo = titulo
        self.nivel = nivel
        self.archivo = archivo
        self.linea = linea
        self.encabezado = encabezado
        self.cuerpo = []            # (línea, texto), sin ejemplos ni excepción
        self.ejemplo = False
        self.texto = ""             # todo, para buscar el checklist

    @property
    def capitulo(self):
        """El capítulo dueño, deducido de la ruta: `20-meta-reglas` → `20`."""
        rel = relativo(self.archivo).split("/")
        for parte in rel:
            m = re.match(r"^(\d{2})-", parte)
            if m:
                return m.group(1)
        return "??"

    @property
    def prefijo(self):
        return re.match(r"^([A-Z]{1,4})", self.id).group(1)

    @property
    def derogada(self):
        return bool(_DEROGADA.search(self.encabezado))

    @property
    def blindada(self):
        return "[BLINDADA]" in self.encabezado

    def largo(self):
        """Lo que ocupa el cuerpo **leído**, no escrito.

        La fila 10 habla de cuatro líneas del molde a ochenta columnas, y quien
        lee ve el texto del enlace, no su destino. Contar el marcado castiga
        justo a la regla que cita bien: [`20·M15`](../base/20-meta-reglas/reglas/M15-toda-cita-a-otra-regla-lleva-su-enlace.md)
        exige que **toda** cita lleve su enlace, y cada uno cuesta unos
        cincuenta caracteres que nadie lee.

        Medido el 2026-08-18: de las 108 reglas que se pasaban del límite,
        **27 se pasaban solo por eso** — `ID3` contaba 561 y son 265; `CFG1`
        contaba 359 y son 234. Dos reglas del estándar tirando en direcciones
        contrarias, y la que perdía era la que se cumplía.
        """
        return sum(len(_ENLACE_MD.sub(r"\1", t)) for _, t in self.cuerpo)


def reglas(raiz=None):
    """Todas las reglas de `base/`, en orden de archivo.

    Lo que va dentro de un bloque cercado no cuenta: ahí las reglas son ejemplos
    del molde (`R7`, `R8`), no reglas del estándar.
    """
    raiz = raiz or RAIZ
    salida = []
    for archivo in recorrer_md(os.path.join(raiz, BASE)):
        texto = leer(archivo)
        actual = None
        en_ejemplo = False
        for n, linea in lineas_utiles(texto):
            m = _REGLA.match(linea)
            if m:
                # Un `#` solo es regla si el archivo se llama como ella. Los
                # anexos abren igual (`# F13 · Estructura base…`) y no son
                # reglas: son el material que la regla enlaza.
                if (len(m.group(1)) == 1
                        and not os.path.basename(archivo).startswith(m.group(2) + "-")):
                    actual = None
                    continue
                actual = Regla(m.group(2), m.group(3), len(m.group(1)),
                               archivo, n, linea)
                salida.append(actual)
                en_ejemplo = False
                continue
            if actual is None:
                continue
            if linea.startswith("#") or linea.strip() == "---":
                actual = None
                continue
            if linea.strip().startswith("**Excepción**"):
                en_ejemplo = True       # de aquí para abajo ya no es el cuerpo
            if not en_ejemplo and linea.strip() and not linea.startswith(">"):
                actual.cuerpo.append((n, linea.strip()))

        # El ejemplo vive dentro de un bloque cercado, que `lineas_utiles`
        # justamente se salta: se busca sobre el texto completo, acotado al
        # trozo de cada regla.
        _marcar_ejemplos(texto, [r for r in salida if r.archivo == archivo])
    return salida


def _marcar_ejemplos(texto, del_archivo):
    lineas = texto.splitlines()
    for i, regla in enumerate(del_archivo):
        ini = regla.linea
        fin = del_archivo[i + 1].linea - 1 if i + 1 < len(del_archivo) else len(lineas)
        trozo = "\n".join(lineas[ini:fin])
        regla.texto = trozo
        regla.ejemplo = "INCORRECTO" in trozo and "CORRECTO" in trozo


def _letras_registradas(raiz):
    """Los prefijos que `estructura-regla.md` declara ocupados."""
    ruta = os.path.join(raiz, *LETRAS.split("/"))
    try:
        texto = leer(ruta)
    except OSError:
        return set()
    letras = set()
    for _, linea in lineas_utiles(texto):
        m = re.match(r"^\|\s*`([A-Z]{1,4})`\s*\|", linea)
        if m:
            letras.add(m.group(1))
    return letras


def _clasificadas(raiz):
    """Los IDs que `reglas-validables.md` menciona, sin importar en qué lista."""
    try:
        texto = leer(os.path.join(raiz, *VALIDABLES.split("/")))
    except OSError:
        return set()
    return set(re.findall(r"\b([A-Z]{1,4}\d+(?:\.\d+)?)\b", texto))


def _dependencias(regla):
    """`[(forma, id)]` declaradas en el cuerpo, en cualquiera de sus escrituras."""
    cuerpo = " ".join(t for _, t in regla.cuerpo)
    salida = [(m.group(1), m.group(3))
              for m in _DEPENDENCIA_ENLAZADA.finditer(cuerpo)]
    salida += [(m.group(1), m.group(3)) for m in _DEPENDENCIA.finditer(cuerpo)]
    vistas, unicas = set(), []
    for forma, id in salida:
        if (forma, id) not in vistas:
            vistas.add((forma, id))
            unicas.append((forma, id))
    return unicas


def _fila5_tecnologia(regla):
    hallazgos = []
    for n, linea in regla.cuerpo:
        for m in _TECNOLOGIA.finditer(linea):
            hallazgos.append(Hallazgo(
                AVISO, regla.archivo, n,
                f"`{regla.id}` nombra «{m.group(1)}» — M3 pide que la base sirva "
                f"a cualquier proyecto (fila 5)"))
    return hallazgos


def _fila6_identificador(regla, letras, por_prefijo):
    hallazgos = []
    if "." in regla.id and not regla.derogada:
        hallazgos.append(Hallazgo(
            AVISO, regla.archivo, regla.linea,
            f"el ID `{regla.id}` no es `<PREFIJO><n>` — M4 no admite decimales "
            f"(fila 6)"))
    if regla.prefijo not in letras:
        hallazgos.append(Hallazgo(
            FALLA, regla.archivo, regla.linea,
            f"el prefijo `{regla.prefijo}` no está en la tabla de letras "
            f"ocupadas de `{LETRAS}` (M4 · fila 6)"))
    capitulos = por_prefijo.get(regla.prefijo, set())
    if len(capitulos) > 1:
        hallazgos.append(Hallazgo(
            FALLA, regla.archivo, regla.linea,
            f"el prefijo `{regla.prefijo}` se usa en más de un capítulo "
            f"({', '.join(sorted(capitulos))}) — M4 lo exige exclusivo (fila 6)"))
    return hallazgos


def _fila7_10_12_13_formato(regla):
    hallazgos = []
    if regla.nivel > 2:
        hallazgos.append(Hallazgo(
            FALLA, regla.archivo, regla.linea,
            f"`{regla.id}` abre con `{'#' * regla.nivel}` — M5 pide `##` "
            f"(fila 7)"))
    if regla.largo() > LIMITE_CUERPO and not regla.derogada:
        hallazgos.append(Hallazgo(
            AVISO, regla.archivo, regla.linea,
            f"el cuerpo de `{regla.id}` mide {regla.largo()} caracteres y el "
            f"molde da para {LIMITE_CUERPO} (cuatro líneas · M5 · fila 10)"))
    if not regla.cuerpo:
        hallazgos.append(Hallazgo(
            FALLA, regla.archivo, regla.linea,
            f"`{regla.id}` no tiene cuerpo — M5 pide nombre y cuerpo siempre"))

    marca = regla.encabezado
    for conocida in _MARCAS:
        marca = marca.replace(conocida, "")
    marca = _DEROGADA.sub("", marca)
    sospecha = re.search(r"`\[[^\]]+\]`|\[[A-ZÁÉÍÓÚ][^\]]*\](?!\()", marca)
    if sospecha:
        hallazgos.append(Hallazgo(
            AVISO, regla.archivo, regla.linea,
            f"`{regla.id}` lleva la marca «{sospecha.group(0)}», que no es "
            f"ninguna de las tres de M5 (fila 13)"))
    return hallazgos


def _blindada_solo_en_el_nucleo(reglas_):
    """`M1` · La marca `[BLINDADA]` solo la lleva una regla del núcleo.

    **Es la única mitad de `M1` que un programa puede juzgar.** Que un nivel
    «no contradiga al de arriba» exige leer las dos reglas y entenderlas; que
    una regla se declare intocable **viviendo fuera del capítulo intocable**, no:
    eso se ve.

    **Y es la vía por la que se rompería la jerarquía sin que nadie lo note.**
    Una regla de capa 2 con la marca queda por encima de las demás sin haber
    pasado por el núcleo — se saltó el nivel en vez de contradecirlo.

    `33` · Anclado al **encabezado**, que es lo que hace usable a este control:
    la palabra `BLINDADA` aparece en prosa en seis archivos, y sin el ancla el
    validador reportaría de más. **Uno que reporta de más se termina apagando**,
    y un control apagado es peor que ninguno porque figura como cubierto.
    """
    hallazgos = []
    for regla in reglas_:
        if not regla.blindada:
            continue
        rel = relativo(regla.archivo).replace("\\", "/")
        if rel.endswith("00-nucleo-blindado.md"):
            continue
        hallazgos.append(Hallazgo(
            FALLA, regla.archivo, regla.linea,
            f"`{regla.id}` se declara `[BLINDADA]` fuera del núcleo — M1: la "
            f"marca es del capítulo `00 · Núcleo blindado`, y ponerla en otro "
            f"sitio salta un nivel de la jerarquía en vez de respetarlo"))
    return hallazgos


def _fila14_15_dependencias(regla, indice):
    hallazgos = []
    for forma, id in _dependencias(regla):
        if id not in indice:
            hallazgos.append(Hallazgo(
                FALLA, regla.archivo, regla.linea,
                f"`{regla.id}` declara `{forma} {id}` y esa regla no existe "
                f"(M7 · fila 14)"))
            continue
        if id == regla.id:
            hallazgos.append(Hallazgo(
                FALLA, regla.archivo, regla.linea,
                f"`{regla.id}` depende de sí misma (M7 · fila 15)"))
            continue
        otra = indice[id]
        if otra.blindada and forma in ("extiende", "deroga") and not regla.blindada:
            hallazgos.append(Hallazgo(
                FALLA, regla.archivo, regla.linea,
                f"`{regla.id}` {forma} `{id}`, que está `[BLINDADA]` — M7 lo "
                f"prohíbe (fila 15)"))
        for forma_otra, id_otra in _dependencias(otra):
            if id_otra == regla.id and forma_otra != "deroga" and forma != "deroga":
                hallazgos.append(Hallazgo(
                    FALLA, regla.archivo, regla.linea,
                    f"`{regla.id}` y `{id}` dependen una de la otra — M7 prohíbe "
                    f"el círculo (fila 15)"))
    return hallazgos


def _fila18_clasificada(regla, clasificadas):
    if regla.id in clasificadas or regla.derogada:
        return []
    return [Hallazgo(
        AVISO, regla.archivo, regla.linea,
        f"`{regla.id}` no aparece en `{VALIDABLES}` — M9 pide que toda regla "
        f"declare si es validable (fila 18)")]


_TOCADOS = {}


def _fechas_de_cambio(carpeta):
    """{ruta absoluta: fecha del último cambio}, en **una sola** pasada.

    Se pregunta al control de versiones y no al disco: la fecha de
    modificación del sistema de archivos cambia con un `clone`, con un
    `checkout` y hasta con un antivirus, así que compararla contra el sello
    daría vencidos falsos en cada máquina nueva.

    Y se pregunta de una vez, no por archivo. Preguntar regla por regla son
    doscientas invocaciones y la corrida pasó de segundos a minutos — una
    comprobación que tarda tanto que estorba se termina desactivando, y
    entonces no comprueba nada.
    """
    carpeta = os.path.abspath(carpeta)
    if carpeta in _TOCADOS:
        return _TOCADOS[carpeta]

    fechas = {}
    try:
        r = subprocess.run(
            ["git", "log", "--format=%cs", "--name-only", "--", "."],
            cwd=carpeta, capture_output=True, text=True, encoding="utf-8",
            errors="replace", timeout=120)
        if r.returncode == 0:
            raiz = subprocess.run(
                ["git", "rev-parse", "--show-toplevel"], cwd=carpeta,
                capture_output=True, text=True, encoding="utf-8",
                errors="replace", timeout=30).stdout.strip()
            fecha = ""
            for linea in r.stdout.splitlines():
                linea = linea.strip()
                if not linea:
                    continue
                if re.fullmatch(r"\d{4}-\d{2}-\d{2}", linea):
                    fecha = linea
                    continue
                # `git log` va del más nuevo al más viejo: la primera vez que
                # se ve un archivo es su último cambio.
                ruta = os.path.normpath(os.path.join(raiz, linea))
                fechas.setdefault(ruta, fecha)
    except (OSError, subprocess.SubprocessError):
        fechas = {}

    _TOCADOS[carpeta] = fechas
    return fechas


def _tocado_el(archivo):
    """La fecha del último cambio, o "" si no hay dato.

    Sin dato **no se inventa un vencimiento**: un hallazgo falso acá enseña a
    ignorar todos los demás.
    """
    archivo = os.path.abspath(archivo)
    return _fechas_de_cambio(os.path.dirname(archivo)).get(archivo, "")


def _cambio_de_verdad(regla):
    """¿El cuerpo de **esta** regla difiere del guardado?

    Sin control de versiones no hay con qué comparar, y entonces se cree lo que
    dice la fecha: se devuelve `True` y el aviso sale igual.
    """
    import subprocess
    rel = os.path.relpath(regla.archivo, RAIZ).replace("\\", "/")
    try:
        r = subprocess.run(["git", "-C", RAIZ, "show", "HEAD:%s" % rel],
                           capture_output=True, text=True, encoding="utf-8",
                           errors="replace", timeout=30)
    except (OSError, subprocess.SubprocessError):
        return True
    if r.returncode:
        return True                     # archivo nuevo: su sello es nuevo también
    marca = "## %s " % regla.id
    if marca not in r.stdout:
        return True                     # la regla no existía: es nueva
    # `regla.texto` **no trae el encabezado**: empieza después. Al comparar hay
    # que quitarlo también del lado guardado, o difieren siempre — que fue el
    # primer intento, y dejaba la comprobación exactamente igual de ruidosa.
    antes = r.stdout[r.stdout.index(marca):].split(chr(10), 1)[1]
    antes = antes.split("### Checklist")[0]
    ahora = regla.texto.split("### Checklist")[0]
    return antes.strip() != ahora.strip()


def _sello_vencido(regla):
    """`52` · El sello dice «vale mientras el texto no cambie», y nada lo mira.

    Cada bloque de checklist cierra con esa frase. Una regla puede editarse y
    seguir mostrando un CUMPLE que se aplicó contra otro texto, otra versión y
    otro día — y quien la lee ve un sello y confía. Es peor que no tener
    sello: el que no lo tiene al menos no engaña.

    **Se comparaba solo por fecha del archivo, y eso reportaba de más.** El
    2026-08-19 dio **119 avisos**: editar una regla vencía el sello de **todas
    las de su capítulo**, porque la fecha es del archivo y el sello es de la
    regla. Un validador que reporta ciento diecinueve cosas no lo lee nadie.

    Ahora hacen falta las dos: que el archivo se haya tocado después del sello
    **y** que el cuerpo de esa regla difiera del que está guardado. Así una
    edición en la regla vecina deja de vencer este sello, y el que de verdad
    cambió se sigue viendo.

    Su propio texto ya anticipaba este paso: *«si esto produce demasiado ruido,
    la huella queda como el paso siguiente, ya con datos»*. Los datos fueron 119.

    **Lo que sigue sin verse:** una regla cambiada y confirmada en el mismo
    movimiento que su sello viejo. Para eso hace falta guardar la huella dentro
    del sello, y eso es trabajo aparte.
    """
    if regla.derogada:
        return []
    m = _SELLADO_EL.search(regla.texto)
    if not m:
        return []                       # sin fecha no hay nada que comparar
    sellado = m.group(1)
    tocado = _tocado_el(regla.archivo)
    if not tocado or tocado <= sellado:
        return []
    if not _cambio_de_verdad(regla):
        return []
    return [Hallazgo(
        AVISO, regla.archivo, regla.linea,
        f"el sello de `{regla.id}` se aplicó el {sellado} y el archivo se "
        f"tocó el {tocado}: el propio bloque dice que queda **anulado** si el "
        f"texto cambia, así que hay que volver a aplicarle el checklist")]


_BLOQUES_DEL_SELLO = {"A": 1, "B": 5, "C": 7, "D": 14, "E": 18}

_FILA_DEL_SELLO = re.compile(
    r"(?m)^\|\s*([A-E])\s*·[^|]*\|[^|]*\|([^|]*)\|")

_FILA_EN_PROSA = re.compile(r"\*\*Filas? ([\d,\s]*\d)")

_REPRUEBA = "❌"


def _filas_marcadas(sello):
    """Qué filas trae la tabla del sello en ❌, por número de fila."""
    marcadas = set()
    for m in _FILA_DEL_SELLO.finditer(sello):
        inicio = _BLOQUES_DEL_SELLO[m.group(1)]
        for i, celda in enumerate(m.group(2).split()):
            if celda == _REPRUEBA:
                marcadas.add(inicio + i)
    return marcadas


def _filas_en_prosa(sello):
    """Qué filas nombra el texto del sello: «**Fila 9 ·**», «**Filas 8, 9 y 10**»."""
    filas = set()
    for grupo in _FILA_EN_PROSA.findall(sello):
        filas |= set(int(n) for n in re.findall(r"\d+", grupo))
    return filas


def _sello_se_contradice(regla):
    """El sello dice en su texto que una fila falla, y su tabla la da por buena.

    **Es la tabla la que se lee.** Nadie recorre veinte filas de prosa: se mira
    el renglón de emoticones y se sigue. Un sello donde el texto reprueba la
    fila 5 y la tabla la muestra en ✅ afirma dos cosas contrarias, y la que
    gana es la falsa.

    Se reporta **una sola dirección**: fila que el texto reprueba y la tabla no.
    Al revés no es defecto — el texto agrupa («son tres reglas en una») y no
    tiene por qué desglosar cada fila que ya marcó la tabla.

    Sale de aplicarle el checklist a los veinte capítulos: seis sellos escritos
    en la misma pasada tenían la tabla y su propio texto en desacuerdo.
    """
    if regla.derogada:
        return []
    m = _CHECKLIST.search(regla.texto)
    if not m:
        return []
    sello = regla.texto[m.start():]
    marcadas = _filas_marcadas(sello)

    if m.group(1) == "CUMPLE":
        # Un sello en CUMPLE no puede traer ❌ en su tabla. Y sus filas
        # nombradas en prosa **no se comparan**: un CUMPLE suele contar qué
        # reprobaba antes de corregirlo, y eso es historia, no veredicto.
        if not marcadas:
            return []
        return [Hallazgo(
            FALLA, regla.archivo, regla.linea,
            f"el sello de `{regla.id}` dice CUMPLE y su tabla trae ❌ en la "
            f"fila {sorted(marcadas)[0]}")]

    faltan = sorted(_filas_en_prosa(sello) - marcadas)
    if not faltan:
        return []
    if len(faltan) == 1:
        cuales = f"la fila {faltan[0]}"
    else:
        cuales = ("las filas " + ", ".join(str(f) for f in faltan[:-1])
                  + f" y {faltan[-1]}")
    return [Hallazgo(
        FALLA, regla.archivo, regla.linea,
        f"el sello de `{regla.id}` reprueba en su texto {cuales} y su tabla "
        f"la da por buena — la tabla es la que se lee, así que el sello "
        f"afirma lo contrario de lo que dice")]


_TOTALES_DEL_SELLO = re.compile(
    r"\*\*20 filas:\s*(\d+)\s*✅\s*·\s*(\d+)\s*❌\s*·\s*(\d+)\s*N/A")


def _cuenta_de_la_tabla(sello):
    """`(✅, ❌, N/A)` contados en la tabla del sello."""
    cuenta = [0, 0, 0]
    for m in _FILA_DEL_SELLO.finditer(sello):
        for celda in m.group(2).split():
            if celda == _REPRUEBA:
                cuenta[1] += 1
            elif celda.upper() == "N/A":
                cuenta[2] += 1
            elif celda == "✅":
                cuenta[0] += 1
    return tuple(cuenta)


def _totales_del_sello(regla):
    """La línea de totales dice una cosa y la tabla de arriba dice otra.

    Es el mismo defecto que `_sello_se_contradice` por el otro lado: el sello
    afirma dos cosas y solo una es cierta. Se cuenta la tabla, que es lo que
    alguien puede verificar renglón por renglón, y se reporta si la línea que
    la resume no coincide.

    **La tabla tiene que sumar 20.** Si no suma, el problema es otro y se dice
    así en vez de corregir un total contra una tabla incompleta.
    """
    if regla.derogada:
        return []
    m = _CHECKLIST.search(regla.texto)
    if not m:
        return []
    sello = regla.texto[m.start():]
    d = _TOTALES_DEL_SELLO.search(sello)
    if not d:
        return []
    cuenta = _cuenta_de_la_tabla(sello)
    if sum(cuenta) != 20:
        return [Hallazgo(
            FALLA, regla.archivo, regla.linea,
            f"la tabla del sello de `{regla.id}` tiene {sum(cuenta)} casillas "
            f"y el checklist son 20 filas")]
    dice = tuple(int(x) for x in d.groups())
    if dice == cuenta:
        return []
    return [Hallazgo(
        FALLA, regla.archivo, regla.linea,
        f"el sello de `{regla.id}` se resume como {dice[0]} ✅ · {dice[1]} ❌ · "
        f"{dice[2]} N/A y su tabla tiene {cuenta[0]} ✅ · {cuenta[1]} ❌ · "
        f"{cuenta[2]} N/A")]


def _un_solo_sello(regla):
    """Dos bloques de checklist en la misma regla: uno de los dos miente.

    Pasó en `M14`, con un sello de la `v2.1.0` encima del de la `v2.2.0`.
    Quien lea de arriba abajo se queda con el viejo, que además tenía mal la
    cuenta. Un sello se **reemplaza**, no se apila.
    """
    if regla.derogada:
        return []
    cuantos = len(_CHECKLIST.findall(regla.texto))
    if cuantos < 2:
        return []
    return [Hallazgo(
        FALLA, regla.archivo, regla.linea,
        f"`{regla.id}` trae {cuantos} bloques de checklist — el sello se "
        f"reemplaza, no se apila: quien lee de arriba abajo se queda con el "
        f"viejo")]


def _m14_checklist(regla):
    if regla.derogada:
        return []
    m = _CHECKLIST.search(regla.texto)
    if not m:
        return [Hallazgo(
            AVISO, regla.archivo, regla.linea,
            f"`{regla.id}` no trae su bloque de checklist — M14: ninguna regla "
            f"nace fuera del procedimiento")]
    hallazgos = []
    if m.group(1) != "CUMPLE":
        hallazgos.append(Hallazgo(
            FALLA, regla.archivo, regla.linea,
            f"el checklist de `{regla.id}` dice {m.group(1)} — M14: sin CUMPLE "
            f"la regla no se publica"))
    if not _CONTRA.search(regla.texto):
        hallazgos.append(Hallazgo(
            AVISO, regla.archivo, regla.linea,
            f"el checklist de `{regla.id}` no dice contra qué versión se aplicó "
            f"(M14)"))
    return hallazgos


def _fila19_version(raiz):
    """M10 · la versión que declara `VERSION` tiene su entrada en el CHANGELOG."""
    try:
        version = leer(os.path.join(raiz, "VERSION")).strip()
        cambios = leer(os.path.join(raiz, "CHANGELOG.md"))
    except OSError:
        return []
    if re.search(rf"(?m)^##\s+{re.escape(version)}\b", cambios):
        return []
    return [Hallazgo(
        FALLA, os.path.join(raiz, "CHANGELOG.md"), 0,
        f"`VERSION` dice {version} y el CHANGELOG no tiene su entrada — M10 "
        f"(fila 19)")]


_ENTRADA = re.compile(r"(?m)^## (\d+\.\d+\.\d+) — ")
_SOLO_FECHA = re.compile(r"^\d{4}-\d{2}-\d{2}$")

_JERGA_DE_LA_CASA = re.compile(
    r"(?i)\b(fase|épica|checklist|validador|enganche|meta-?regla|opt-in|"
    r"trazabilidad|derogad\w+|retrodocument\w+)\b")


def _fila_m17_entrada_llana(raiz):
    """`M17` · la entrada del registro abre sin jerga ni rutas.

    Se mira **solo el primer párrafo** después del encabezado de versión, que
    es lo que alguien lee antes de decidir si sigue. Que la entrada **se
    entienda** lo decide quien lee; lo que se cuenta es lo que la volvía
    ilegible en las 83 anteriores: identificadores de regla, rutas de archivo
    y las palabras que solo significan algo adentro.

    **Solo la entrada de la versión vigente.** [`20·M10`](...) dice que un
    cambio de norma no reabre lo cerrado, y reportar las 83 viejas sepultaría
    la única que todavía se puede arreglar.
    """
    try:
        version = leer(os.path.join(raiz, "VERSION")).strip()
        cambios = leer(os.path.join(raiz, "CHANGELOG.md"))
    except OSError:
        return []

    m = _ENTRADA.search(cambios)
    if not m or m.group(1) != version:
        return []                       # sin entrada, ya se queja la fila 19

    sig = _ENTRADA.search(cambios, m.end())
    cuerpo = cambios[m.end():sig.start() if sig else len(cambios)]
    parrafos = [p.strip() for p in cuerpo.split("\n\n") if p.strip()]
    # La fecha queda pegada al encabezado y no dice nada: no se cuenta.
    parrafos = [p for p in parrafos if not _SOLO_FECHA.match(p)]
    if not parrafos:
        return []
    # El primero suele ser la línea del tipo (MAYOR · MENOR · PARCHE).
    abre = "\n\n".join(parrafos[:2])

    motivos = []
    if _CITA_CON_CAPITULO.search(abre):
        motivos.append("un identificador de regla")
    if _RUTA_DE_ARCHIVO.search(abre):
        motivos.append("una ruta de archivo")
    jerga = sorted({j.lower() for j in _JERGA_DE_LA_CASA.findall(abre)})
    if jerga:
        motivos.append("palabras de la casa (%s)" % ", ".join(jerga))
    if not motivos:
        return []
    return [Hallazgo(
        AVISO, os.path.join(raiz, "CHANGELOG.md"), 0,
        f"la entrada de la {version} abre con {' y '.join(motivos)} — `M17` pide "
        f"qué cambió y por qué, en dos frases que se entiendan sin conocer el proyecto")]


_CITA_CON_CAPITULO = re.compile(r"\d{2}·[A-Z]{1,4}\d+")
_RUTA_DE_ARCHIVO = re.compile(r"[\w.-]+/[\w./-]*\.(?:md|py|plantilla)|[\w-]+\.(?:md|py|plantilla)")


def validar(raiz=None):
    raiz = raiz or RAIZ
    catalogo = reglas(raiz)
    indice = {r.id: r for r in catalogo}
    letras = _letras_registradas(raiz)
    clasificadas = _clasificadas(raiz)

    por_prefijo = {}
    for r in catalogo:
        por_prefijo.setdefault(r.prefijo, set()).add(r.capitulo)

    hallazgos = []
    for r in catalogo:
        hallazgos += _fila5_tecnologia(r)
        hallazgos += _fila6_identificador(r, letras, por_prefijo)
        hallazgos += _fila7_10_12_13_formato(r)
        hallazgos += _fila14_15_dependencias(r, indice)
        hallazgos += _fila18_clasificada(r, clasificadas)
        hallazgos += _m14_checklist(r)
        hallazgos += _sello_vencido(r)
        hallazgos += _sello_se_contradice(r)
        hallazgos += _totales_del_sello(r)
        hallazgos += _un_solo_sello(r)
    return (hallazgos + _fila19_version(raiz) + _fila_m17_entrada_llana(raiz)
            + _blindada_solo_en_el_nucleo(catalogo))


def validar_catalogo(proyecto, raiz=None):
    """`M16` · toda regla `P` del proyecto nombra la regla de base que concreta.

    Es la única meta-regla que no se puede comprobar en seco: el catálogo vive
    en el proyecto. Que el criterio citado sea de verdad el que la `P` concreta
    lo decide quien lee; que **haya** respaldo y que el ID exista, no.
    """
    raiz = raiz or RAIZ
    ruta = os.path.join(os.path.abspath(proyecto), *CATALOGO_PROYECTO.split("/"))
    if not os.path.isfile(ruta):
        return [Hallazgo(AVISO, ruta, 0,
                         f"el proyecto no tiene `{CATALOGO_PROYECTO}`")]

    indice = {r.id for r in reglas(raiz)}
    texto = leer(ruta)
    hallazgos = []
    actual, linea_actual, respaldo = None, 0, None

    def cerrar():
        if actual is None:
            return
        if not respaldo:
            hallazgos.append(Hallazgo(
                FALLA, ruta, linea_actual,
                f"`{actual}` no declara su **Respaldo** — M16: ninguna regla de "
                f"proyecto se sostiene sola"))
            return
        citados = re.findall(r"([A-Z]{1,4}\d+(?:\.\d+)?)", respaldo)
        existentes = [c for c in citados if c in indice]
        if not existentes:
            hallazgos.append(Hallazgo(
                FALLA, ruta, linea_actual,
                f"el respaldo de `{actual}` no cita ninguna regla de `base/` que "
                f"exista (M16)"))

    for n, linea in lineas_utiles(texto):
        m = re.match(r"^#{2,4}\s+(P\d+)\s*·", linea)
        if m:
            cerrar()
            actual, linea_actual, respaldo = m.group(1), n, None
            continue
        if actual and re.match(r"^\s*[-*]?\s*\*\*Respaldo", linea):
            respaldo = linea
    cerrar()
    return hallazgos


if __name__ == "__main__":
    # `53` · Un modulo que se ejecuta solo y no imprime nada dice, con su
    # silencio, lo mismo que diria si hubiera comprobado y estuviera todo bien.
    comun.no_es_punto_de_entrada("metareglas")
