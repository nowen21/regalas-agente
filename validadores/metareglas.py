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


def _sello_vencido(regla):
    """`52` · El sello dice «vale mientras el texto no cambie», y nada lo mira.

    Cada bloque de checklist cierra con esa frase. Una regla puede editarse y
    seguir mostrando un CUMPLE que se aplicó contra otro texto, otra versión y
    otro día — y quien la lee ve un sello y confía. Es peor que no tener
    sello: el que no lo tiene al menos no engaña.

    **Se compara por fecha, no por huella del texto.** La huella detectaría el
    cambio exacto, pero obliga a recalcular el sello de las ~70 reglas que hoy
    están bien: mucho riesgo para hacer visible algo que la fecha ya hace
    visible. Si esto produce demasiado ruido, la huella queda como el paso
    siguiente, ya con datos.

    El precio de la fecha está asumido y se dice: un cambio de una coma
    también vence el sello, y un cambio sin confirmar no se ve.
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
    return [Hallazgo(
        AVISO, regla.archivo, regla.linea,
        f"el sello de `{regla.id}` se aplicó el {sellado} y el archivo se "
        f"tocó el {tocado}: el propio bloque dice que queda **anulado** si el "
        f"texto cambia, así que hay que volver a aplicarle el checklist")]


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
    return hallazgos + _fila19_version(raiz)


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
