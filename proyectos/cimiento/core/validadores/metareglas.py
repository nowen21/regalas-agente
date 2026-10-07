"""`20` · El estándar contra sus propias meta-reglas.

El [checklist del estándar](../../../../base/20-meta-reglas/checklist.md) tiene
veinte filas y su §4 dice cuáles puede decidir un programa solo: **5, 6, 7, 10,
12, 13, 14, 15, 18, 19 y 20**. Eso es lo que se comprueba acá, y por eso no se
inventan criterios: la especificación ya estaba escrita.

| Fila | Meta-regla | Qué se comprueba |
|---|---|---|
| 5 | `M3` | ninguna regla nombra lenguaje, framework, motor, nube ni herramienta |
| 6 | `M4` | el ID es `<PREFIJO><n>`, el prefijo es exclusivo del capítulo y está en la tabla de letras |
| 7 | `M5` | el encabezado es `##` (o `#` si la regla ocupa su propio archivo) |
| 10 | `M5` | el cuerpo cabe en cuatro líneas |
| 13 | `M5` | la marca es una de las tres de la lista cerrada |
| 14 | `M7` | la dependencia se declara en una de las tres formas, y el ID existe |
| 15 | `M7` | ninguna dependencia da vueltas en círculo ni manda sobre una `[BLINDADA]` |
| 18 | `M9` | la regla está clasificada en `validadores/reglas-validables.md` |
| 19 | `M10` | la versión de `VERSION` tiene su entrada en el `CHANGELOG.md` |

Se suma `M14`: que la regla traiga su bloque de checklist con resultado y contra
qué versión se aplicó. Las filas que faltan piden **leer y entender** la regla y
no se simulan: una comprobación que se equivoca vale menos que ninguna.

Corre sobre el estándar mismo. `M16` vive aparte, en `CatalogoDelProyecto`,
porque el catálogo de reglas propias vive en el proyecto.

Piezas: `Regla` y `CuerpoDeReglas` leen `base/`; `Sello` juzga el bloque de
checklist de una regla; `Metareglas` y `CatalogoDelProyecto` son los validadores.
"""
import os
import re

from ..comun import AVISO, FALLA, Archivos, Git, Hallazgo, Markdown, Proyecto
from ..comun.proyecto import EXCLUIDAS
from .base import Validador
from .marcas import Marcas

BASE = "base"
LETRAS = "base/20-meta-reglas/estructura-regla.md"
VALIDABLES = "validadores/reglas-validables.md"
CATALOGO_PROYECTO = ".agente/reglas-proyecto.md"

# `EP-004·HU-002` · Lo que importa no es el nivel del título sino la forma del
# identificador: las reglas del capítulo 16 se escriben con `###` y durante dos
# meses no existieron para el programa. Se aceptan hasta cuatro almohadillas.
_REGLA = re.compile(r"^(#{1,4})\s+([A-Z]{1,4}\d+(?:\.\d+)?)\s*·\s*(.+?)\s*$")
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
# La derogación puede citar una o varias sucesoras, con capítulo o sin él: lo
# que fija `M5` es la forma, no cuántas la reemplazan.
_DEROGADA = re.compile(r"\[DEROGADA en [\d.]+ → ver [^\]]+\]")

# Fila 10 · cuatro líneas del molde a ochenta columnas. Se mide en caracteres y
# no en saltos de línea: el mismo cuerpo a veces va en un renglón y a veces cortado.
LIMITE_CUERPO = 320

# El enlace se mide por lo que se lee: `[texto](destino)` cuenta como `texto`.
_ENLACE_MD = re.compile(r"\[([^\]]*)\]\([^)]*\)")

# Fila 5 · nombres propios de tecnología. Lista corta y defendible: producto,
# marca o lenguaje concreto. No entran las palabras que el estándar adoptó como
# concepto propio (git, markdown) ni los formatos de datos.
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

# `EP-005·HU-012` y `EP-005·HU-023` · Quién hace cumplir la regla y a qué tareas
# aplica **no son la regla**: contarlas en el cuerpo reprobaba la fila 10 y
# vencía sellos sin haber cambiado qué se exige.
_FUERA_DEL_CUERPO = ("**Quién la hace cumplir:", "**Nadie la hace cumplir:",
                     "**Aplica a:**")


def _mostrar(ruta):
    """Cómo se nombra una ruta en un mensaje: desde la carpeta del estándar si
    queda adentro, completa si no."""
    estandar = Proyecto.estandar()
    return Proyecto(estandar).mostrar(ruta) if estandar else os.path.abspath(ruta).replace("\\", "/")


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
        self.texto = ""             # todo el trozo de la regla, sin su encabezado

    @property
    def capitulo(self):
        """El capítulo dueño, deducido de la ruta: `20-meta-reglas` da `20`."""
        for parte in _mostrar(self.archivo).split("/"):
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

        `20·M15` exige que toda cita lleve su enlace, y cada uno cuesta unos
        cincuenta caracteres que nadie lee: contar el marcado castigaba justo a
        la regla que cita bien (27 de 108 reglas largas lo eran solo por eso).
        """
        return sum(len(_ENLACE_MD.sub(r"\1", t)) for _, t in self.cuerpo)


class CuerpoDeReglas:
    """Leer las reglas de `base/` y lo que las acompaña. No juzga nada."""

    @staticmethod
    def es_el_estandar(raiz):
        """Si esa carpeta **es** el estándar y no un proyecto que lo usa: solo el
        estándar tiene el cuerpo de reglas y su número de versión."""
        raiz = os.path.abspath(raiz or Proyecto.estandar())
        return (os.path.isdir(os.path.join(raiz, "base"))
                and os.path.isfile(os.path.join(raiz, "VERSION")))

    @staticmethod
    def _recorrer(proyecto, archivos):
        """Los `.md` de `base/`: del lector si sabe recorrer (el estándar en la base,
        `EP-026·HU-004`); si no, del disco."""
        if hasattr(archivos, "recorrer"):
            return archivos.recorrer(BASE, EXCLUIDAS)
        return proyecto.recorrer_md(BASE)

    @staticmethod
    def _definidas_arriba(proyecto, archivos):
        """Los IDs definidos con `#` o `##`, en una pasada previa: en el orden del
        árbol, el anexo que **nombra** a `M19` se lee antes que su archivo."""
        arriba = set()
        for archivo in CuerpoDeReglas._recorrer(proyecto, archivos):
            for _, linea in Markdown.lineas_utiles(archivos.leer(archivo)):
                m = _REGLA.match(linea)
                if not m or len(m.group(1)) > 2:
                    continue
                if len(m.group(1)) == 1 and not os.path.basename(archivo).startswith(m.group(2) + "-"):
                    continue
                arriba.add(m.group(2))
        return arriba

    @classmethod
    def leer(cls, raiz=None, archivos=None):
        """Todas las reglas de `base/`, en orden de archivo.

        Lo que va dentro de un bloque cercado no cuenta: ahí las reglas son
        ejemplos del molde, no reglas del estándar.
        """
        proyecto = Proyecto(raiz or Proyecto.estandar())
        archivos = archivos or Archivos()
        salida = []
        arriba = cls._definidas_arriba(proyecto, archivos)
        for archivo in cls._recorrer(proyecto, archivos):
            texto = archivos.leer(archivo)
            actual, en_ejemplo = None, False
            for n, linea in Markdown.lineas_utiles(texto):
                m = _REGLA.match(linea)
                if m:
                    # Un `#` solo es regla si el archivo se llama como ella: los
                    # anexos abren igual y son el material que la regla enlaza.
                    if len(m.group(1)) == 1 and not os.path.basename(archivo).startswith(m.group(2) + "-"):
                        actual = None
                        continue
                    # Un `###` con forma de regla es la regla (capítulo 16) o un
                    # eco de una definida arriba (anexo que nombra a `M19`): `M4`
                    # exige el ID único, así que el ya definido es eco.
                    if len(m.group(1)) >= 3 and m.group(2) in arriba:
                        actual = None
                        continue
                    actual = Regla(m.group(2), m.group(3), len(m.group(1)), archivo, n, linea)
                    salida.append(actual)
                    en_ejemplo = False
                    continue
                if actual is None:
                    continue
                if linea.startswith("#") or linea.strip() == "---":
                    actual = None
                    continue
                if linea.strip().startswith("**Excepción**") or linea.strip().startswith(_FUERA_DEL_CUERPO):
                    en_ejemplo = True       # de aquí para abajo ya no es el cuerpo
                if not en_ejemplo and linea.strip() and not linea.startswith(">"):
                    actual.cuerpo.append((n, linea.strip()))
            # El ejemplo vive en un bloque cercado, que `lineas_utiles` se salta:
            # se busca sobre el texto completo, acotado al trozo de cada regla.
            cls._marcar_ejemplos(texto, [r for r in salida if r.archivo == archivo])
        return salida

    @staticmethod
    def _marcar_ejemplos(texto, del_archivo):
        lineas = texto.splitlines()
        for i, regla in enumerate(del_archivo):
            fin = del_archivo[i + 1].linea - 1 if i + 1 < len(del_archivo) else len(lineas)
            trozo = "\n".join(lineas[regla.linea:fin])
            regla.texto = trozo
            regla.ejemplo = "INCORRECTO" in trozo and "CORRECTO" in trozo

    @staticmethod
    def letras_registradas(raiz, archivos=None):
        """Los prefijos que `estructura-regla.md` declara ocupados."""
        texto = (archivos or Archivos()).leer(os.path.join(raiz, *LETRAS.split("/")))
        letras = set()
        for _, linea in Markdown.lineas_utiles(texto):
            m = re.match(r"^\|\s*`([A-Z]{1,4})`\s*\|", linea)
            if m:
                letras.add(m.group(1))
        return letras

    @staticmethod
    def clasificadas(raiz, archivos=None):
        """Los IDs que `reglas-validables.md` menciona, sin importar en qué lista."""
        texto = (archivos or Archivos()).leer(os.path.join(raiz, *VALIDABLES.split("/")))
        return set(re.findall(r"\b([A-Z]{1,4}\d+(?:\.\d+)?)\b", texto))

    @staticmethod
    def dependencias(regla):
        """`[(forma, id)]` declaradas en el cuerpo, en cualquiera de sus escrituras."""
        cuerpo = " ".join(t for _, t in regla.cuerpo)
        salida = [(m.group(1), m.group(3)) for m in _DEPENDENCIA_ENLAZADA.finditer(cuerpo)]
        salida += [(m.group(1), m.group(3)) for m in _DEPENDENCIA.finditer(cuerpo)]
        vistas, unicas = set(), []
        for forma, id_ in salida:
            if (forma, id_) not in vistas:
                vistas.add((forma, id_))
                unicas.append((forma, id_))
        return unicas


# La tabla del sello: cada bloque empieza en una fila del checklist.
_BLOQUES_DEL_SELLO = {"A": 1, "B": 5, "C": 7, "D": 14, "E": 18}
_FILA_DEL_SELLO = re.compile(r"(?m)^\|\s*([A-E])\s*·[^|]*\|[^|]*\|([^|]*)\|")
_FILA_EN_PROSA = re.compile(r"\*\*Filas? ([\d,\s]*\d)")
_TOTALES_DEL_SELLO = re.compile(r"\*\*20 filas:\s*(\d+)\s*✅\s*·\s*(\d+)\s*❌\s*·\s*(\d+)\s*N/A")
_REPRUEBA = "❌"


class Sello:
    """El bloque de checklist de una regla: si está, si se contradice y si venció."""

    # `{carpeta: {archivo: fecha}}`: git se pregunta una vez por carpeta.
    _tocados = {}

    @classmethod
    def fechas_de_cambio(cls, carpeta):
        """`{ruta absoluta: fecha del último cambio}`, en **una sola** pasada.

        Se pregunta a git y no al disco: la fecha del sistema de archivos cambia
        con un `clone`, un `checkout` o un antivirus. Y de una vez, no por
        archivo: doscientas invocaciones llevaban la corrida a minutos.
        """
        carpeta = os.path.abspath(carpeta)
        if carpeta in cls._tocados:
            return cls._tocados[carpeta]
        fechas = {}
        salida = Git(carpeta, espera=120).correr("log", "--format=%cs", "--name-only", "--", ".")
        if salida:
            raiz = Git(carpeta, espera=30).correr("rev-parse", "--show-toplevel").strip()
            fecha = ""
            for linea in salida.splitlines():
                linea = linea.strip()
                if not linea:
                    continue
                if re.fullmatch(r"\d{4}-\d{2}-\d{2}", linea):
                    fecha = linea
                    continue
                # `git log` va del más nuevo al más viejo: la primera vez que se
                # ve un archivo es su último cambio.
                fechas.setdefault(os.path.normpath(os.path.join(raiz, linea)), fecha)
        cls._tocados[carpeta] = fechas
        return fechas

    @classmethod
    def tocado_el(cls, archivo):
        """La fecha del último cambio, o `""` si no hay dato: sin dato no se
        inventa un vencimiento."""
        archivo = os.path.abspath(archivo)
        return cls.fechas_de_cambio(os.path.dirname(archivo)).get(archivo, "")

    @staticmethod
    def sin_declaracion(texto):
        """El texto sin las líneas que no son la regla (quién la hace cumplir, a
        qué tareas aplica), y sin el renglón en blanco que dejan al salir."""
        quedan = []
        for linea in texto.split("\n"):
            if linea.strip().startswith(_FUERA_DEL_CUERPO):
                continue
            if not linea.strip() and quedan and not quedan[-1].strip():
                continue
            quedan.append(linea)
        return "\n".join(quedan)

    @classmethod
    def cambio_de_verdad(cls, regla):
        """¿El texto de **esta** regla difiere del guardado en `HEAD`?

        Sin control de versiones no hay con qué comparar, y entonces se cree lo
        que dice la fecha: `True`. Se compara en el repositorio del archivo de
        la regla (el viejo usaba siempre el del estándar).
        """
        carpeta = os.path.dirname(os.path.abspath(regla.archivo))
        repo = Git(carpeta, espera=30).correr("rev-parse", "--show-toplevel").strip()
        if not repo:
            return True
        rel = os.path.relpath(os.path.abspath(regla.archivo), repo).replace("\\", "/")
        guardado = Git(repo, espera=30).correr("show", "HEAD:%s" % rel)
        marca = "## %s " % regla.id
        if marca not in guardado:
            return True                 # archivo o regla nuevos: su sello es nuevo también
        # `regla.texto` no trae el encabezado: se le quita también al guardado.
        antes = guardado[guardado.index(marca):].split("\n", 1)[1]
        antes = antes.split("### Checklist")[0]
        ahora = regla.texto.split("### Checklist")[0]
        # Ni la tipografía ni la línea de quién la hace cumplir vencen un sello:
        # no cambian ninguna respuesta del checklist.
        antes = cls.sin_declaracion(Marcas.limpiar(antes)[0])
        ahora = cls.sin_declaracion(Marcas.limpiar(ahora)[0])
        return antes.strip() != ahora.strip()

    @classmethod
    def vencido(cls, regla):
        """`52` · El sello dice «vale mientras el texto no cambie», y se mira.

        Hacen falta las dos: que el archivo se haya tocado después del sello
        **y** que el cuerpo de esa regla difiera del guardado. Solo con la fecha
        daba 119 avisos, porque editar una regla vencía a sus vecinas.
        """
        if regla.derogada:
            return []
        m = _SELLADO_EL.search(regla.texto)
        if not m:
            return []
        sellado = m.group(1)
        tocado = cls.tocado_el(regla.archivo)
        if not tocado or tocado <= sellado or not cls.cambio_de_verdad(regla):
            return []
        return [Hallazgo(
            AVISO, regla.archivo, regla.linea,
            "el sello de `%s` se aplicó el %s y el archivo se tocó el %s: el propio bloque dice "
            "que queda **anulado** si el texto cambia, así que hay que volver a aplicarle el "
            "checklist" % (regla.id, sellado, tocado))]

    @staticmethod
    def filas_marcadas(sello):
        """Qué filas trae la tabla del sello en ❌, por número de fila."""
        marcadas = set()
        for m in _FILA_DEL_SELLO.finditer(sello):
            inicio = _BLOQUES_DEL_SELLO[m.group(1)]
            for i, celda in enumerate(m.group(2).split()):
                if celda == _REPRUEBA:
                    marcadas.add(inicio + i)
        return marcadas

    @staticmethod
    def filas_en_prosa(sello):
        """Qué filas nombra el texto del sello: «**Fila 9 ·**», «**Filas 8, 9 y 10**»."""
        filas = set()
        for grupo in _FILA_EN_PROSA.findall(sello):
            filas |= set(int(n) for n in re.findall(r"\d+", grupo))
        return filas

    @classmethod
    def se_contradice(cls, regla):
        """El texto del sello reprueba una fila y su tabla la da por buena.

        **Es la tabla la que se lee.** Se reporta una sola dirección: la tabla
        puede marcar más de lo que el texto desglosa. Y un CUMPLE no compara su
        prosa, que suele contar lo que se corrigió; solo no puede traer ❌.
        """
        if regla.derogada:
            return []
        m = _CHECKLIST.search(regla.texto)
        if not m:
            return []
        sello = regla.texto[m.start():]
        marcadas = cls.filas_marcadas(sello)
        if m.group(1) == "CUMPLE":
            if not marcadas:
                return []
            return [Hallazgo(FALLA, regla.archivo, regla.linea,
                             "el sello de `%s` dice CUMPLE y su tabla trae ❌ en la fila %d"
                             % (regla.id, sorted(marcadas)[0]))]
        faltan = sorted(cls.filas_en_prosa(sello) - marcadas)
        if not faltan:
            return []
        if len(faltan) == 1:
            cuales = "la fila %d" % faltan[0]
        else:
            cuales = "las filas " + ", ".join(str(f) for f in faltan[:-1]) + " y %d" % faltan[-1]
        return [Hallazgo(
            FALLA, regla.archivo, regla.linea,
            "el sello de `%s` reprueba en su texto %s y su tabla la da por buena — la tabla es la "
            "que se lee, así que el sello afirma lo contrario de lo que dice" % (regla.id, cuales))]

    @staticmethod
    def cuenta_de_la_tabla(sello):
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

    @classmethod
    def totales(cls, regla):
        """La línea de totales dice una cosa y la tabla otra. Si la tabla no suma
        20, el defecto es ese y se dice así."""
        if regla.derogada:
            return []
        m = _CHECKLIST.search(regla.texto)
        if not m:
            return []
        sello = regla.texto[m.start():]
        d = _TOTALES_DEL_SELLO.search(sello)
        if not d:
            return []
        cuenta = cls.cuenta_de_la_tabla(sello)
        if sum(cuenta) != 20:
            return [Hallazgo(FALLA, regla.archivo, regla.linea,
                             "la tabla del sello de `%s` tiene %d casillas y el checklist son 20 filas"
                             % (regla.id, sum(cuenta)))]
        dice = tuple(int(x) for x in d.groups())
        if dice == cuenta:
            return []
        return [Hallazgo(
            FALLA, regla.archivo, regla.linea,
            "el sello de `%s` se resume como %d ✅ · %d ❌ · %d N/A y su tabla tiene %d ✅ · %d ❌ · "
            "%d N/A" % ((regla.id,) + dice + cuenta))]

    @staticmethod
    def uno_solo(regla):
        """Dos bloques de checklist en la misma regla: un sello se reemplaza, no se apila."""
        if regla.derogada:
            return []
        cuantos = len(_CHECKLIST.findall(regla.texto))
        if cuantos < 2:
            return []
        return [Hallazgo(
            FALLA, regla.archivo, regla.linea,
            "`%s` trae %d bloques de checklist — el sello se reemplaza, no se apila: quien lee de "
            "arriba abajo se queda con el viejo" % (regla.id, cuantos))]

    @staticmethod
    def m14(regla):
        """`M14` · El bloque está, dice CUMPLE y dice contra qué versión se aplicó."""
        if regla.derogada:
            return []
        m = _CHECKLIST.search(regla.texto)
        if not m:
            return [Hallazgo(AVISO, regla.archivo, regla.linea,
                             "`%s` no trae su bloque de checklist — M14: ninguna regla nace fuera "
                             "del procedimiento" % regla.id)]
        hallazgos = []
        if m.group(1) != "CUMPLE":
            hallazgos.append(Hallazgo(FALLA, regla.archivo, regla.linea,
                                      "el checklist de `%s` dice %s — M14: sin CUMPLE la regla no se "
                                      "publica" % (regla.id, m.group(1))))
        if not _CONTRA.search(regla.texto):
            hallazgos.append(Hallazgo(AVISO, regla.archivo, regla.linea,
                                      "el checklist de `%s` no dice contra qué versión se aplicó (M14)"
                                      % regla.id))
        return hallazgos


# `M17` · Lo que volvía ilegible la entrada del registro.
_ENTRADA = re.compile(r"(?m)^## (\d+\.\d+\.\d+) — ")
_SOLO_FECHA = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_JERGA_DE_LA_CASA = re.compile(
    r"(?i)\b(fase|épica|checklist|validador|enganche|meta-?regla|opt-in|"
    r"trazabilidad|derogad\w+|retrodocument\w+)\b")
_CITA_CON_CAPITULO = re.compile(r"\d{2}·[A-Z]{1,4}\d+")
_RUTA_DE_ARCHIVO = re.compile(r"[\w.-]+/[\w./-]*\.(?:md|py|plantilla)|[\w-]+\.(?:md|py|plantilla)")


class Metareglas(Validador):
    """El cuerpo de reglas de `base/` contra las filas del checklist que un
    programa puede decidir solo."""

    nombre = "metareglas"
    regla = "20·M1, 20·M3, 20·M4, 20·M5, 20·M7, 20·M9, 20·M10, 20·M14, 20·M17"
    descripcion = "el cuerpo de reglas contra el checklist del capítulo 20"

    def validar(self):
        raiz = self.proyecto.raiz
        # Pendiente 81 · Un proyecto no tiene cuerpo de reglas: reportar sobre él
        # daba una falla y cuatro avisos, los cinco falsos.
        if not CuerpoDeReglas.es_el_estandar(raiz):
            return [Hallazgo(
                AVISO, raiz, 0,
                "esta carpeta no es el estándar, así que no tiene meta-reglas que comprobar — para "
                "revisar las reglas propias de un proyecto es `validar.py metareglas --catalogo "
                "<proyecto>`")]
        catalogo = CuerpoDeReglas.leer(raiz, self.archivos)
        indice = {r.id: r for r in catalogo}
        letras = CuerpoDeReglas.letras_registradas(raiz, self.archivos)
        clasificadas = CuerpoDeReglas.clasificadas(raiz, self.archivos)
        por_prefijo = {}
        for r in catalogo:
            por_prefijo.setdefault(r.prefijo, set()).add(r.capitulo)

        hallazgos = []
        for r in catalogo:
            hallazgos += self.fila5_tecnologia(r)
            hallazgos += self.fila6_identificador(r, letras, por_prefijo)
            hallazgos += self.fila7_10_12_13_formato(r)
            hallazgos += self.fila14_15_dependencias(r, indice)
            hallazgos += self.fila18_clasificada(r, clasificadas)
            hallazgos += Sello.m14(r)
            hallazgos += Sello.vencido(r)
            hallazgos += Sello.se_contradice(r)
            hallazgos += Sello.totales(r)
            hallazgos += Sello.uno_solo(r)
        return (hallazgos + self.fila19_version(raiz, self.archivos)
                + self.entrada_llana(raiz, self.archivos)
                + self.blindada_solo_en_el_nucleo(catalogo)
                + self.identificador_repetido(catalogo))

    @staticmethod
    def fila5_tecnologia(regla):
        return [Hallazgo(AVISO, regla.archivo, n,
                         "`%s` nombra «%s» — M3 pide que la base sirva a cualquier proyecto (fila 5)"
                         % (regla.id, m.group(1)))
                for n, linea in regla.cuerpo for m in _TECNOLOGIA.finditer(linea)]

    @staticmethod
    def fila6_identificador(regla, letras, por_prefijo):
        hallazgos = []
        if "." in regla.id and not regla.derogada:
            hallazgos.append(Hallazgo(AVISO, regla.archivo, regla.linea,
                                      "el ID `%s` no es `<PREFIJO><n>` — M4 no admite decimales (fila 6)"
                                      % regla.id))
        if regla.prefijo not in letras:
            hallazgos.append(Hallazgo(FALLA, regla.archivo, regla.linea,
                                      "el prefijo `%s` no está en la tabla de letras ocupadas de `%s` "
                                      "(M4 · fila 6)" % (regla.prefijo, LETRAS)))
        capitulos = por_prefijo.get(regla.prefijo, set())
        if len(capitulos) > 1:
            hallazgos.append(Hallazgo(FALLA, regla.archivo, regla.linea,
                                      "el prefijo `%s` se usa en más de un capítulo (%s) — M4 lo exige "
                                      "exclusivo (fila 6)" % (regla.prefijo, ", ".join(sorted(capitulos)))))
        return hallazgos

    @staticmethod
    def fila7_10_12_13_formato(regla):
        hallazgos = []
        if regla.nivel > 2:
            hallazgos.append(Hallazgo(FALLA, regla.archivo, regla.linea,
                                      "`%s` abre con `%s` — M5 pide `##` (fila 7)"
                                      % (regla.id, "#" * regla.nivel)))
        if regla.largo() > LIMITE_CUERPO and not regla.derogada:
            hallazgos.append(Hallazgo(AVISO, regla.archivo, regla.linea,
                                      "el cuerpo de `%s` mide %d caracteres y el molde da para %d "
                                      "(cuatro líneas · M5 · fila 10)"
                                      % (regla.id, regla.largo(), LIMITE_CUERPO)))
        if not regla.cuerpo:
            hallazgos.append(Hallazgo(FALLA, regla.archivo, regla.linea,
                                      "`%s` no tiene cuerpo — M5 pide nombre y cuerpo siempre" % regla.id))
        marca = regla.encabezado
        for conocida in _MARCAS:
            marca = marca.replace(conocida, "")
        marca = _DEROGADA.sub("", marca)
        sospecha = re.search(r"`\[[^\]]+\]`|\[[A-ZÁÉÍÓÚ][^\]]*\](?!\()", marca)
        if sospecha:
            hallazgos.append(Hallazgo(AVISO, regla.archivo, regla.linea,
                                      "`%s` lleva la marca «%s», que no es ninguna de las tres de M5 "
                                      "(fila 13)" % (regla.id, sospecha.group(0))))
        return hallazgos

    @staticmethod
    def blindada_solo_en_el_nucleo(reglas):
        """`M1` · La marca `[BLINDADA]` solo la lleva una regla del núcleo.

        Es la mitad de `M1` que un programa puede juzgar, y la vía por la que se
        saltaría un nivel de la jerarquía sin que nadie lo note. Se ancla al
        **encabezado**: la palabra aparece en prosa en varios archivos.
        """
        return [Hallazgo(
            FALLA, r.archivo, r.linea,
            "`%s` se declara `[BLINDADA]` fuera del núcleo — M1: la marca es del capítulo "
            "`00 · Núcleo blindado`, y ponerla en otro sitio salta un nivel de la jerarquía en vez "
            "de respetarlo" % r.id)
            for r in reglas
            if r.blindada and not r.archivo.replace("\\", "/").endswith("00-nucleo-blindado.md")]

    @staticmethod
    def fila14_15_dependencias(regla, indice):
        hallazgos = []
        for forma, id_ in CuerpoDeReglas.dependencias(regla):
            if id_ not in indice:
                hallazgos.append(Hallazgo(FALLA, regla.archivo, regla.linea,
                                          "`%s` declara `%s %s` y esa regla no existe (M7 · fila 14)"
                                          % (regla.id, forma, id_)))
                continue
            if id_ == regla.id:
                hallazgos.append(Hallazgo(FALLA, regla.archivo, regla.linea,
                                          "`%s` depende de sí misma (M7 · fila 15)" % regla.id))
                continue
            otra = indice[id_]
            if otra.blindada and forma in ("extiende", "deroga") and not regla.blindada:
                hallazgos.append(Hallazgo(FALLA, regla.archivo, regla.linea,
                                          "`%s` %s `%s`, que está `[BLINDADA]` — M7 lo prohíbe (fila 15)"
                                          % (regla.id, forma, id_)))
            for forma_otra, id_otra in CuerpoDeReglas.dependencias(otra):
                if id_otra == regla.id and forma_otra != "deroga" and forma != "deroga":
                    hallazgos.append(Hallazgo(FALLA, regla.archivo, regla.linea,
                                              "`%s` y `%s` dependen una de la otra — M7 prohíbe el "
                                              "círculo (fila 15)" % (regla.id, id_)))
        return hallazgos

    @staticmethod
    def fila18_clasificada(regla, clasificadas):
        """`M9` · Detiene: una regla publicada sin decir si se comprueba es un
        defecto. La derogada queda exenta porque dejó de regir."""
        if regla.id in clasificadas or regla.derogada:
            return []
        return [Hallazgo(FALLA, regla.archivo, regla.linea,
                         "`%s` no aparece en `%s` — M9 pide que toda regla declare si es validable "
                         "(fila 18)" % (regla.id, VALIDABLES))]

    @staticmethod
    def fila19_version(raiz, archivos=None):
        """`M10` · La versión de `VERSION` tiene su entrada en el registro.

        Sin el dato no se afirma: leer devuelve vacío cuando falta el archivo,
        y la falla salía como «`VERSION` dice  y…», con el hueco del número.
        """
        archivos = archivos or Archivos()
        version = archivos.leer(os.path.join(raiz, "VERSION")).strip()
        cambios = archivos.leer(os.path.join(raiz, "CHANGELOG.md"))
        if not version or not cambios:
            return []
        if re.search(r"(?m)^##\s+%s\b" % re.escape(version), cambios):
            return []
        return [Hallazgo(FALLA, os.path.join(raiz, "CHANGELOG.md"), 0,
                         "`VERSION` dice %s y el CHANGELOG no tiene su entrada — M10 (fila 19)" % version)]

    @staticmethod
    def entrada_llana(raiz, archivos=None):
        """`M17` · La entrada vigente del registro abre sin jerga ni rutas.

        Se mira solo el primer párrafo de la entrada de la versión vigente: un
        cambio de norma no reabre lo cerrado (`20·M10`), y reportar las viejas
        sepultaría la única que todavía se puede arreglar.
        """
        archivos = archivos or Archivos()
        version = archivos.leer(os.path.join(raiz, "VERSION")).strip()
        cambios = archivos.leer(os.path.join(raiz, "CHANGELOG.md"))
        m = _ENTRADA.search(cambios)
        if not m or m.group(1) != version:
            return []                   # sin entrada, ya se queja la fila 19
        sig = _ENTRADA.search(cambios, m.end())
        cuerpo = cambios[m.end():sig.start() if sig else len(cambios)]
        parrafos = [p.strip() for p in cuerpo.split("\n\n") if p.strip()]
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
        return [Hallazgo(AVISO, os.path.join(raiz, "CHANGELOG.md"), 0,
                         "la entrada de la %s abre con %s — `M17` pide qué cambió y por qué, en dos "
                         "frases que se entiendan sin conocer el proyecto" % (version, " y ".join(motivos)))]

    @staticmethod
    def identificador_repetido(catalogo):
        """`M4` · Un identificador se usa una vez; la segunda es un choque.

        Las derogadas cuentan igual: su ID no se reutiliza (`M11`), y ese es el
        caso en que alguien lo repetiría sin querer.
        """
        por_id = {}
        for r in catalogo:
            por_id.setdefault(r.id, []).append(r)
        hallazgos = []
        for id_, reglas in sorted(por_id.items()):
            if len(reglas) < 2:
                continue
            donde = " · ".join("%s:%d" % (_mostrar(r.archivo), r.linea) for r in reglas)
            for r in reglas:
                hallazgos.append(Hallazgo(
                    FALLA, r.archivo, r.linea,
                    "el identificador `%s` está usado %d veces (%s) — M4 lo exige único, y una cita a "
                    "`%s` no sabría a cuál va (fila 6)" % (id_, len(reglas), donde, id_)))
        return hallazgos


# `EP-001·HU-006` · Un ajuste del proyecto no afloja el núcleo. Se mira solo el
# verbo con que la propia regla declara su respaldo: endurecer una `[BLINDADA]`
# es legítimo; aflojarla, derogarla o reemplazarla, no. Contradecirla sin
# decirlo no se lee de un verbo, y esto no lo promete.
_AFLOJAN = ("afloja", "aflojan", "ablanda", "ablandan", "relaja", "relajan",
            "deroga", "derogan", "anula", "anulan", "suspende", "suspenden",
            "reemplaza", "reemplazan", "exceptúa", "exceptua", "excepciona",
            "contradice", "contradicen", "extiende", "extienden")


class CatalogoDelProyecto(Validador):
    """`M16` · Toda regla `P` del proyecto nombra la regla de base que concreta.

    Que el criterio citado sea el que la `P` concreta lo decide quien lee; que
    **haya** respaldo y que el ID exista, no.
    """

    nombre = "catalogo"
    regla = "20·M16, 20·M7"
    descripcion = "las reglas propias del proyecto y su respaldo en base/"

    def __init__(self, proyecto, archivos=None, estandar=None):
        super().__init__(proyecto, archivos)
        self.estandar = estandar or Proyecto.estandar()

    @staticmethod
    def afloja_una_blindada(respaldo, blindadas):
        """`(verbo, id)` si el respaldo declara aflojar una blindada; si no, `None`."""
        bajo = respaldo.lower()
        verbo = next((v for v in _AFLOJAN if re.search(r"\b%s\b" % re.escape(v), bajo)), None)
        if not verbo:
            return None
        for id_ in re.findall(r"([A-Z]{1,4}\d+(?:\.\d+)?)", respaldo):
            if id_ in blindadas:
                return verbo, id_
        return None

    def validar(self):
        ruta = self.proyecto.ruta(CATALOGO_PROYECTO)
        if not os.path.isfile(ruta):
            return [Hallazgo(AVISO, ruta, 0, "el proyecto no tiene `%s`" % CATALOGO_PROYECTO)]
        del_estandar = CuerpoDeReglas.leer(self.estandar, self.archivos)
        indice = {r.id for r in del_estandar}
        blindadas = {r.id for r in del_estandar if r.blindada}
        hallazgos = []
        actual, linea_actual, respaldo = None, 0, None
        for n, linea in Markdown.lineas_utiles(self.archivos.leer(ruta)):
            m = re.match(r"^#{2,4}\s+(P\d+)\s*·", linea)
            if m:
                if actual is not None:
                    hallazgos += self._cerrar(ruta, actual, linea_actual, respaldo, indice, blindadas)
                actual, linea_actual, respaldo = m.group(1), n, None
            elif actual and re.match(r"^\s*[-*]?\s*\*\*Respaldo", linea):
                respaldo = linea
        if actual is not None:
            hallazgos += self._cerrar(ruta, actual, linea_actual, respaldo, indice, blindadas)
        return hallazgos

    def _cerrar(self, ruta, actual, linea, respaldo, indice, blindadas):
        hallazgos = []
        afloja = self.afloja_una_blindada(respaldo or "", blindadas)
        if afloja:
            hallazgos.append(Hallazgo(
                FALLA, ruta, linea,
                "`%s` declara que %s `%s`, que está `[BLINDADA]` — M7 lo prohíbe: un ajuste del "
                "proyecto endurece el núcleo, nunca lo afloja" % (actual, afloja[0], afloja[1])))
        if not respaldo:
            hallazgos.append(Hallazgo(FALLA, ruta, linea,
                                      "`%s` no declara su **Respaldo** — M16: ninguna regla de proyecto "
                                      "se sostiene sola" % actual))
            return hallazgos
        if not [c for c in re.findall(r"([A-Z]{1,4}\d+(?:\.\d+)?)", respaldo) if c in indice]:
            hallazgos.append(Hallazgo(FALLA, ruta, linea,
                                      "el respaldo de `%s` no cita ninguna regla de `base/` que exista "
                                      "(M16)" % actual))
        return hallazgos
