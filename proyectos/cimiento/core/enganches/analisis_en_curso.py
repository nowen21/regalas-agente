"""`EP-023 · HU-001 · fase B` · La conversación pasa sola al análisis prendido.

**Qué resuelve.** Hasta la versión 40.0.0, lo que pasaba la conversación al
análisis era un guion que se prendía y se apagaba a mano en cada análisis (H-2
del 2026-09-30). Acá vive el trabajo que no depende de la herramienta; el
enganche que lo llama está en `adaptadores/claude-code/`.

**Los tres controles** (análisis 2 del pendiente 103, conclusión 2):

- **Prender**, con «Analicemos: el pendiente N». «Analicemos» sin pendiente no
  prende nada: sigue siendo analizar en el chat.
- **Pausar**, con «Pare». Los turnos en pausa no entran; queda una línea que
  dice cuáles fueron (conclusión 4).
- **Apagar**, con «Apruebo el análisis». La herramienta pone la marca con la
  fecha y el turno, y borra el estado cuando la respuesta a ese turno ya entró.

**Un análisis prendido por sesión** (sesión del 2026-10-04, que reemplaza la
conclusión 6 y el punto 4 del análisis 3). Cada sesión guarda su estado aparte,
en `historico-chat/.estado/analisis-en-curso/`, y se reconoce por su
transcripción. Lo que no deja prender es solo esto: que la misma sesión tenga
otro análisis sin aprobar, o que otra sesión tenga prendido el mismo pendiente.
Un análisis aprobado con HU por construir ya no bloquea a nadie: Cimiento tiene
que poder abrir otro análisis mientras uno se construye.

El archivo único de antes (`analisis-en-curso.txt`) se sigue leyendo: es de la
sesión cuya transcripción nombra, y quien no dice su sesión lo usa como siempre.

**El estado vive en la base de Cimiento** (`EP-025·HU-023`) cuando el proyecto
está registrado y la base responde: una fila por sesión. Si no, sigue en su
archivo, porque pasar la conversación no se puede caer. Lo que quedó en archivo
pasa solo a la base en la siguiente lectura, y el archivo se borra. Sin sesión
se lee la fila más reciente, que es lo que leía el archivo único.

**Se prende desde un turno anterior** con «Analicemos: el pendiente N desde el
turno T» (`EP-025·HU-023`).

**Lo que no hace, y se declara.** No copia el hallazgo ni el pendiente en el
análisis nuevo, y no corrige las palabras copiadas: la conversación no se edita
(análisis 1, conclusión 21).
"""
import glob
import os
import re
import time
import unicodedata

from ..comun import Archivos, Proyecto
from .niveles import BaseSinRespuesta
from .origen import LectorDeAnalisis, OrigenDeCadaPunto

ESTADO = os.path.join("historico-chat", ".estado", "analisis-en-curso.txt")
ESTADOS = os.path.join("historico-chat", ".estado", "analisis-en-curso")
PLANTILLA = os.path.join("plantillas", "analisis.md")
FIN = "> acá termina la conversación"
APORTA = "Lo que aporta al análisis principal"
LISTA = "## Lista de análisis"

# «Corrija» deja corregir las herramientas del proceso en esa respuesta, sin
# abrir análisis (análisis 16 del pendiente 103, acuerdo 2). Vale un solo turno:
# el mensaje siguiente lo borra.
CORRIJA = os.path.join("historico-chat", ".estado", "corrija.txt")

_ANALISIS = re.compile(r"^analisis-(\d+)\.md$")
_APROBADO = re.compile(r"^> \*\*Aprobado\*\*", re.M)
_TURNO_APROBADO = re.compile(r"^> \*\*Aprobado\*\* .*?en el turno (\d+)", re.M)
_TURNO = re.compile(r"^### (\d+) · Usuario", re.M)
_PENDIENTE = re.compile(r"\bpendiente\s+(\d+)\b")
_DESDE = re.compile(r"\bdesde el turno\s+(\d+)\b")
_HU = re.compile(r"\bHU[- ]0*(\d+)\b")
_EPICA = re.compile(r"\bEP-0*(\d+)\b")
_RESULTADO = re.compile(r"^\*\*Resultado:\*\* *(\S.*?)\s*$", re.M)
_SUMA = re.compile(r"^\*\*Lo que suma al análisis principal:\*\* *(\S.*?)\s*$", re.M)
_FILA = re.compile(r"^\| *\d+ *\|", re.M)
_HALLAZGO_TITULO = re.compile(r"^### (H-\d+)\b", re.M)
_DE_DONDE_SALE = re.compile(r"^\|[^|\n]*De dónde sale[^|\n]*\|(.*)\|\s*$", re.M)

# Lo que no es del repositorio: local, generado o de terceros.
FUERA = {".git", ".venv", "venv", "__pycache__", "node_modules", "terceros"}


def _leer(ruta):
    return Archivos().leer(ruta)


def _escribir(ruta, texto):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(texto)


# La base de cada proyecto, decidida una vez por proceso: un enganche crea
# varios `AnalisisEnCurso` y no tiene por qué preguntar cada vez.
_BASES = {}
_PASADOS = set()


def _base_de(raiz):
    """El `EstadoEnBase` del proyecto si está registrado y la base responde, o None."""
    clave = os.path.normcase(os.path.abspath(raiz))
    if clave not in _BASES:
        from .estado_en_base import EstadoEnBase
        base = EstadoEnBase(raiz)
        try:
            _BASES[clave] = base if base.proyecto_id() else None
        except BaseSinRespuesta:
            _BASES[clave] = None
    return _BASES[clave]


class AnalisisEnCurso:
    """El análisis que recibe la conversación de una sesión, y sus tres controles.

    `transcripcion` es la de la sesión que llama. Sin ella se usa el archivo
    único de antes, para quien todavía no dice de qué sesión viene. `base` es
    dónde vive el estado: None lo decide (`_base_de`), False obliga al archivo.
    """

    def __init__(self, raiz, transcripcion="", base=None):
        self.raiz = raiz
        self.transcripcion = os.path.normpath(os.path.abspath(transcripcion)) if transcripcion else ""
        self._base = base

    @property
    def base(self):
        if self._base is None:
            self._base = _base_de(self.raiz) or False
        return self._base or None

    def _relativa(self, ruta):
        return os.path.relpath(ruta, self.raiz).replace(os.sep, "/")

    def _de_fila(self, dato):
        pausas = []
        for tramo in filter(None, (dato.get("pausas") or "").split(",")):
            a, b = tramo.split("-")
            pausas.append((int(a), int(b)))
        return {"analisis": os.path.normpath(os.path.join(self.raiz, dato["analisis"])),
                "transcripcion": os.path.normpath(os.path.join(self.raiz, dato["sesion"])),
                "desde": dato["desde"], "pausa": dato.get("pausa"), "pausas": pausas}

    def _a_fila(self, estado):
        return {"sesion": self._relativa(estado["transcripcion"]), "analisis": self._relativa(estado["analisis"]),
                "desde": estado["desde"], "pausa": estado.get("pausa"),
                "pausas": ",".join("%d-%d" % p for p in estado.get("pausas") or [])}

    def _archivos_de_estado(self):
        rutas = [os.path.join(self.raiz, ESTADO)]
        carpeta = os.path.join(self.raiz, ESTADOS)
        if os.path.isdir(carpeta):
            rutas += [os.path.join(carpeta, n) for n in sorted(os.listdir(carpeta)) if n.endswith(".txt")]
        return rutas

    def pasar_archivos_a_la_base(self):
        """Lo que quedó en archivo pasa a la base y el archivo se borra. Una vez por proceso."""
        clave = os.path.normcase(os.path.abspath(self.raiz))
        if clave in _PASADOS or not self.base:
            return
        for ruta in self._archivos_de_estado():
            estado = self._leer_archivo(ruta)
            if estado:
                self.base.guardar(self._a_fila(estado))
                os.remove(ruta)
        _PASADOS.add(clave)

    # ── el texto ──────────────────────────────────────────────────────────

    @staticmethod
    def limpio(texto):
        """Minúsculas y sin tildes, que es como se comparan las palabras."""
        sin = unicodedata.normalize("NFD", texto or "")
        sin = "".join(c for c in sin if unicodedata.category(c) != "Mn")
        return sin.lower().strip()

    seccion = staticmethod(LectorDeAnalisis.seccion)

    # ── el estado ─────────────────────────────────────────────────────────

    def _leer_archivo(self, ruta):
        """El estado guardado en `ruta`, o None."""
        if not os.path.isfile(ruta):
            return None
        datos = {}
        for linea in _leer(ruta).splitlines():
            if "=" in linea:
                clave, valor = linea.split("=", 1)
                datos[clave.strip()] = valor.strip()
        if not {"analisis", "transcripcion", "desde"} <= datos.keys():
            return None
        pausas = []
        for tramo in filter(None, datos.get("pausas", "").split(",")):
            a, b = tramo.split("-")
            pausas.append((int(a), int(b)))
        return {
            "analisis": os.path.normpath(os.path.join(self.raiz, datos["analisis"])),
            "transcripcion": os.path.normpath(os.path.join(self.raiz, datos["transcripcion"])),
            "desde": int(datos["desde"]),
            "pausa": int(datos["pausa"]) if datos.get("pausa") else None,
            "pausas": pausas,
        }

    def ruta_estado(self):
        """Dónde está el estado de esta sesión.

        El archivo único de antes, si es de esta sesión o si no se dijo cuál;
        si no, el de la sesión en `ESTADOS/`, con el nombre de su transcripción.
        """
        unico = os.path.join(self.raiz, ESTADO)
        if not self.transcripcion:
            return unico
        viejo = self._leer_archivo(unico)
        if viejo and os.path.normcase(viejo["transcripcion"]) == os.path.normcase(self.transcripcion):
            return unico
        nombre = os.path.splitext(os.path.basename(self.transcripcion))[0] + ".txt"
        return os.path.join(self.raiz, ESTADOS, nombre)

    def leer_estado(self):
        """`{analisis, transcripcion, desde, pausa, pausas}` con rutas absolutas, o None."""
        if self.base:
            try:
                self.pasar_archivos_a_la_base()
                dato = (self.base.leer(self._relativa(self.transcripcion)) if self.transcripcion
                        else self.base.mas_reciente())
                return self._de_fila(dato) if dato else None
            except BaseSinRespuesta:
                pass                        # sin base, el archivo: la conversación no se cae
        return self._leer_archivo(self.ruta_estado())

    def estados(self):
        """Los estados de todas las sesiones: los de la base, o el archivo único y los de `ESTADOS/`."""
        if self.base:
            try:
                self.pasar_archivos_a_la_base()
                return [self._de_fila(d) for d in self.base.filas()]
            except BaseSinRespuesta:
                pass
        return [e for e in map(self._leer_archivo, self._archivos_de_estado()) if e]

    def guardar_estado(self, estado):
        if self.base:
            try:
                # Primero lo viejo: si no, el archivo de esta sesión pisaría lo nuevo al leerse.
                self.pasar_archivos_a_la_base()
                self.base.guardar(self._a_fila(estado))
                return
            except BaseSinRespuesta:
                pass
        lineas = [
            "analisis=" + os.path.relpath(estado["analisis"], self.raiz).replace(os.sep, "/"),
            "transcripcion=" + os.path.relpath(estado["transcripcion"], self.raiz).replace(os.sep, "/"),
            "desde=%d" % estado["desde"],
        ]
        if estado.get("pausa"):
            lineas.append("pausa=%d" % estado["pausa"])
        if estado.get("pausas"):
            lineas.append("pausas=" + ",".join("%d-%d" % p for p in estado["pausas"]))
        _escribir(self.ruta_estado(), "\n".join(lineas) + "\n")

    def borrar_estado(self):
        if self.base:
            try:
                estado = self.leer_estado()
                if estado:
                    self.base.borrar(self._relativa(estado["transcripcion"]))
                return
            except BaseSinRespuesta:
                pass
        ruta = self.ruta_estado()
        if os.path.isfile(ruta):
            os.remove(ruta)

    def marcar_corrija(self, turno):
        _escribir(os.path.join(self.raiz, CORRIJA), "turno=%d\n" % turno)

    def borrar_corrija(self):
        ruta = os.path.join(self.raiz, CORRIJA)
        if os.path.isfile(ruta):
            os.remove(ruta)

    def corrija_activo(self):
        return os.path.isfile(os.path.join(self.raiz, CORRIJA))

    @staticmethod
    def ultimo_turno(transcripcion):
        """El número del último turno del usuario en la transcripción, o 0."""
        numeros = ([int(n) for n in _TURNO.findall(_leer(transcripcion))]
                   if transcripcion and os.path.isfile(transcripcion) else [])
        return max(numeros) if numeros else 0

    # ── pendientes y análisis ─────────────────────────────────────────────

    def _carpetas_con_pendiente(self):
        for carpeta, subcarpetas, archivos in os.walk(self.raiz):
            subcarpetas[:] = [s for s in subcarpetas if s not in FUERA]
            if "pendiente.md" in archivos:
                yield carpeta

    def carpeta_del_pendiente(self, numero):
        """La carpeta `N-<slug>/` que tiene el `pendiente.md` del pendiente N, o ""."""
        for carpeta in self._carpetas_con_pendiente():
            if os.path.basename(carpeta).split("-", 1)[0] == str(numero):
                return carpeta
        return ""

    @staticmethod
    def analisis_de(carpeta):
        """Los `analisis-N.md` de la carpeta, ordenados por N."""
        salida = []
        for nombre in os.listdir(carpeta):
            m = _ANALISIS.match(nombre)
            if m:
                salida.append((int(m.group(1)), os.path.join(carpeta, nombre)))
        return [ruta for _, ruta in sorted(salida)]

    @staticmethod
    def aprobado(ruta):
        return bool(_APROBADO.search(_leer(ruta)))

    @staticmethod
    def turno_aprobado(ruta):
        """El turno en que se aprobó el análisis, o `None`."""
        m = _TURNO_APROBADO.search(_leer(ruta)) if os.path.isfile(ruta) else None
        return int(m.group(1)) if m else None

    def hu_terminada(self, epica, hu):
        patron = os.path.join(self.raiz, "documentacion", "epicas")
        if not os.path.isdir(patron):
            return False
        for e in os.listdir(patron):
            if not re.match(r"EP-0*%d-" % epica, e):
                continue
            for h in os.listdir(os.path.join(patron, e)):
                if re.match(r"HU-0*%d-" % hu, h):
                    archivo = os.path.join(patron, e, h, h + ".md")
                    if os.path.isfile(archivo):
                        return bool(re.search(r"^\| \*\*Estado\*\* \|\s*Terminada", _leer(archivo), re.M))
        return False

    def plan_pendiente(self, ruta):
        """Las HU de la columna «Pasó a» del análisis que todavía no terminan."""
        texto = _leer(ruta)
        if "## Lo que se tiene que hacer" not in texto:
            return []
        tabla = texto.split("## Lo que se tiene que hacer", 1)[1]
        faltan = []
        for linea in tabla.splitlines():
            if not linea.startswith("|"):
                continue
            celda = linea.rstrip("|").split("|")[-1]
            # Lo hecho «de una y sin fase» nombra archivos, no HU por terminar:
            # sus rutas traían HU de otras épicas y el análisis no se cerraba nunca.
            if "de una y sin fase" in celda:
                continue
            for ep, hu in self.hu_con_su_epica(celda):
                if not self.hu_terminada(ep, hu):
                    faltan.append("EP-%03d HU-%03d" % (ep, hu))
        return sorted(set(faltan))

    @staticmethod
    def hu_con_su_epica(celda):
        """`[(épica, HU)]` de la celda: cada HU con la última épica nombrada antes."""
        marcas = sorted([(m.start(), "ep", int(m.group(1))) for m in _EPICA.finditer(celda)]
                        + [(m.start(), "hu", int(m.group(1))) for m in _HU.finditer(celda)])
        salida, ep = [], None
        for _, clase, numero in marcas:
            if clase == "ep":
                ep = numero
            elif ep is not None:
                salida.append((ep, numero))
        return salida

    def abiertos(self):
        """`[(ruta del análisis, por qué sigue abierto)]` de todo el repositorio."""
        salida = []
        for carpeta in self._carpetas_con_pendiente():
            rutas = self.analisis_de(carpeta)
            if not rutas:
                continue
            ultimo = rutas[-1]
            if not self.aprobado(ultimo):
                salida.append((ultimo, "no está aprobado"))
                continue
            faltan = self.plan_pendiente(ultimo)
            if faltan:
                salida.append((ultimo, "su plan no se ha cumplido: falta " + ", ".join(faltan)))
        return salida

    def nuevo_analisis(self, carpeta):
        """El análisis que se prende: el último si sigue sin aprobar, o el siguiente."""
        rutas = self.analisis_de(carpeta)
        if rutas and not self.aprobado(rutas[-1]):
            return rutas[-1]
        numero = len(rutas) + 1
        ruta = os.path.join(carpeta, "analisis-%d.md" % numero)
        plantilla = os.path.join(Proyecto.estandar(), PLANTILLA)
        texto = _leer(plantilla) if os.path.isfile(plantilla) else (
            "# Análisis «N»\n\n## Conversación\n\n> La escribe el enganche.\n\n" + FIN + "\n")
        _escribir(ruta, texto.replace("# Análisis «N»", "# Análisis %d" % numero, 1))
        return ruta

    # ── los tres controles ────────────────────────────────────────────────

    @classmethod
    def pendiente_pedido(cls, mensaje):
        """El N de «Analicemos: el pendiente N», o None si el mensaje no lo pide."""
        limpio = cls.limpio(mensaje)
        if not limpio.startswith("analicemos"):
            return None
        m = _PENDIENTE.search(limpio.split("\n", 1)[0])
        return int(m.group(1)) if m else None

    @classmethod
    def turno_pedido(cls, mensaje):
        """El T de «Analicemos: el pendiente N desde el turno T», o None (`EP-025·HU-023`)."""
        limpio = cls.limpio(mensaje)
        if not limpio.startswith("analicemos"):
            return None
        m = _DESDE.search(limpio.split("\n", 1)[0])
        return int(m.group(1)) if m else None

    def prender(self, numero, transcripcion, turno, desde=None):
        """Prende el análisis del pendiente. Devuelve `(prendido, mensaje)`.

        Con `desde`, la conversación entra desde ese turno; si ya estaba
        prendido, se corre hasta ahí (`EP-025·HU-023`).
        """
        if desde is not None and not 1 <= desde <= turno:
            return False, "no se prende: el turno %d no existe, van del 1 al %d" % (desde, turno)
        carpeta = self.carpeta_del_pendiente(numero)
        if not carpeta:
            return False, "no hay una carpeta con el pendiente %d" % numero
        carpeta = os.path.normpath(carpeta)
        propia = os.path.normcase(transcripcion and os.path.normpath(os.path.abspath(transcripcion)) or "")
        for otro in self.estados():
            if (os.path.normcase(otro["transcripcion"]) != propia
                    and os.path.dirname(otro["analisis"]) == carpeta
                    and not self.aprobado(otro["analisis"])):
                return False, ("no se prende: el pendiente %d ya tiene su análisis prendido en la sesión de %s"
                               % (numero, os.path.basename(otro["transcripcion"])))
        estado = self.leer_estado()
        if (estado and os.path.dirname(estado["analisis"]) != carpeta
                and os.path.isfile(estado["analisis"]) and not self.aprobado(estado["analisis"])):
            return False, ("no se prende: esta sesión tiene prendido el análisis %s, sin aprobar"
                           % os.path.relpath(estado["analisis"], self.raiz).replace(os.sep, "/"))
        if (estado and os.path.dirname(estado["analisis"]) == os.path.normpath(carpeta)
                and not self.aprobado(estado["analisis"])):
            cambio = False
            if estado.get("pausa"):
                estado["pausas"].append((estado["pausa"], turno - 1))
                estado["pausa"] = None
                cambio = True
            if desde is not None and desde != estado["desde"]:
                estado["desde"] = desde
                cambio = True
            if cambio:
                self.guardar_estado(estado)
            return True, ("sigue prendido, desde el turno %d" % desde) if desde is not None else "sigue prendido"
        analisis = self.nuevo_analisis(carpeta)
        inicio = desde if desde is not None else turno
        self.guardar_estado({"analisis": analisis, "transcripcion": transcripcion,
                             "desde": inicio, "pausa": None, "pausas": []})
        return True, "prendido desde el turno %d" % inicio

    def pausar(self, turno):
        estado = self.leer_estado()
        if not estado or estado.get("pausa"):
            return False
        estado["pausa"] = turno
        self.guardar_estado(estado)
        return True

    # ── aprobar ───────────────────────────────────────────────────────────

    @classmethod
    def aporte(cls, texto):
        """`(resultado, lo que suma)` de «Lo que aporta al análisis principal», o `None`."""
        parte = cls.seccion(texto, APORTA)
        resultado, suma = _RESULTADO.search(parte), _SUMA.search(parte)
        if not (resultado and suma):
            return None
        return resultado.group(1).strip(), suma.group(1).strip()

    @classmethod
    def faltantes(cls, texto):
        """Lo que le falta a un análisis para poder aprobarse (análisis 9, CA-25 y CA-26)."""
        salida = []
        if not _FILA.search(cls.seccion(texto, "Lo que se tiene que hacer")):
            salida.append("falta al menos una fila en «Lo que se tiene que hacer»")
        if cls.aporte(texto) is None:
            salida.append("falta «%s», con el resultado y lo que suma" % APORTA)
        return salida

    @classmethod
    def hallazgo_en_el_pendiente(cls, ruta):
        """`EP-023 · HU-003 · CA-09` · El hallazgo del análisis tiene que estar en su pendiente.

        Cada análisis aprobado deja el pendiente en su versión siguiente, con su
        hallazgo en «De dónde sale» (análisis 11 del pendiente 103, acuerdo 5). El
        análisis 1 no se revisa: es el que origina el pendiente.
        """
        m = _ANALISIS.match(os.path.basename(ruta))
        if not m or int(m.group(1)) == 1:
            return []
        h = _HALLAZGO_TITULO.search(cls.seccion(_leer(ruta), "Hallazgo"))
        if not h:
            return ["falta el número del hallazgo (H-N) en el título de «Hallazgo»"]
        pendiente = os.path.join(os.path.dirname(ruta), "pendiente.md")
        fila = _DE_DONDE_SALE.search(_leer(pendiente)) if os.path.isfile(pendiente) else None
        if not fila or not re.search(r"\b%s\b" % re.escape(h.group(1)), fila.group(1)):
            return ["falta el %s en «De dónde sale» del pendiente: pasarlo a su versión siguiente antes de aprobar"
                    % h.group(1)]
        return []

    def por_que_no_se_aprueba(self):
        """Lo que le falta al análisis prendido para aprobarse; vacío si nada.

        Además de `faltantes()`, corre la revisión de origen: el punto que no dice
        de dónde sale, o que cita algo que no existe, se corrige antes de aprobar
        (análisis 14 del pendiente 103, acuerdo 4).
        """
        estado = self.leer_estado()
        if not estado or not os.path.isfile(estado["analisis"]):
            return []
        return (self.faltantes(_leer(estado["analisis"])) + self.hallazgo_en_el_pendiente(estado["analisis"])
                + OrigenDeCadaPunto.revisar_uno(estado["analisis"]))

    @staticmethod
    def version():
        """La versión del estándar que corre, la que queda en la marca de aprobado."""
        ruta = os.path.join(Proyecto.estandar(), "VERSION")
        return _leer(ruta).strip() if os.path.isfile(ruta) else ""

    def principal_de(self, ruta):
        """El análisis principal del alcance de `ruta`: el primero que aparece subiendo.

        Un módulo con su propio `analisis/<nombre>-analisis-principal.md` lo usa; si
        no lo tiene, se llega al del proyecto (análisis 9, punto 5 de «Lo acordado»).
        """
        raiz = os.path.abspath(self.raiz)
        carpeta = os.path.dirname(os.path.abspath(ruta))
        while True:
            hallados = sorted(glob.glob(os.path.join(carpeta, "analisis", "*analisis-principal*.md")))
            if hallados:
                return hallados[0]
            if os.path.normcase(carpeta) == os.path.normcase(raiz) or os.path.dirname(carpeta) == carpeta:
                return None
            carpeta = os.path.dirname(carpeta)

    @staticmethod
    def nombre_del_analisis(ruta):
        """El texto del enlace en la «Lista de análisis»."""
        m = _ANALISIS.match(os.path.basename(ruta))
        if m:
            p = re.match(r"^(\d+)-", os.path.basename(os.path.dirname(ruta)))
            return "Análisis %s del pendiente %s" % (m.group(1), p.group(1)) if p else "Análisis %s" % m.group(1)
        return _leer(ruta).split("\n", 1)[0].lstrip("# ").strip()

    def anotar_en_principal(self, ruta, fecha):
        """Pasa tal cual lo que suma el análisis al principal de su alcance (CA-24).

        Lo que suma va al final de la redacción y la fila al final de la «Lista de
        análisis». Devuelve la ruta del principal, o `None` si no hay dónde anotarlo.
        """
        datos = self.aporte(_leer(ruta))
        principal = self.principal_de(ruta)
        if not datos or not principal:
            return None
        texto = _leer(principal)
        i = texto.find(LISTA)
        if i < 0:
            return None
        resultado, suma = datos
        enlace = os.path.relpath(ruta, os.path.dirname(principal)).replace(os.sep, "/")
        fila = "| %s | %s | [%s](%s) |\n" % (fecha, resultado.rstrip("."), self.nombre_del_analisis(ruta), enlace)
        _escribir(principal, texto[:i].rstrip("\n") + " " + suma + "\n\n" + texto[i:].rstrip("\n") + "\n" + fila)
        return principal

    def aprobar(self, turno, fecha):
        """Pone la marca «Aprobado» con la fecha, el turno y la versión, una sola vez.

        No la pone si `por_que_no_se_aprueba()` encuentra algo. Puesta la marca,
        pasa lo que el análisis suma al análisis principal.
        """
        estado = self.leer_estado()
        if not estado or not os.path.isfile(estado["analisis"]):
            return False
        texto = _leer(estado["analisis"])
        if _APROBADO.search(texto) or self.por_que_no_se_aprueba():
            return False
        con = ", con la versión %s" % self.version() if self.version() else ""
        marca = ("> **Aprobado** por el usuario el %s, en el turno %d%s. Desde ese momento "
                 "este análisis no se reescribe.\n" % (fecha, turno, con))
        primera, _, resto = texto.partition("\n")
        _escribir(estado["analisis"], primera + "\n\n" + marca + resto)
        self.anotar_en_principal(estado["analisis"], fecha)
        return True

    # ── pasar la conversación ─────────────────────────────────────────────

    @staticmethod
    def bloques(texto):
        """`[(turno, bloque)]` de la transcripción, desde cada `### N · Usuario`."""
        marcas = list(_TURNO.finditer(texto))
        salida = []
        for i, m in enumerate(marcas):
            fin = marcas[i + 1].start() if i + 1 < len(marcas) else len(texto)
            salida.append((int(m.group(1)), texto[m.start():fin].rstrip() + "\n"))
        return salida

    @staticmethod
    def limpiar(bloque):
        # La transcripción separa el turno de su hora con raya larga; el análisis
        # sigue `00·ID8`, así que ahí va una coma (análisis 2, conclusión 5).
        bloque = re.sub(r"^(### \d+ · Usuario|\*\*Agente\*\*) — ", r"\1, ", bloque, flags=re.M)
        # Los puntos suspensivos de un solo carácter pasan a tres puntos: el
        # commit los rechaza (análisis 14 del pendiente 103, acuerdo 6).
        bloque = bloque.replace("…", "...")
        # Las marcas que la herramienta le pone al mensaje no son palabras del
        # usuario (conclusión 10).
        bloque = re.sub(r"</?pasted_content[^>]*>", "", bloque)
        bloque = re.sub(r"<ide_(?:opened_file|selection)>.*?</ide_(?:opened_file|selection)>", "", bloque, flags=re.S)
        bloque = re.sub(r"^> *\n(?=> *\n)", "", bloque, flags=re.M)
        return bloque

    def conversacion(self, estado):
        """El texto que va en la sección «Conversación», con las pausas marcadas."""
        raiz = self.raiz
        texto = _leer(estado["transcripcion"]) if os.path.isfile(estado["transcripcion"]) else ""
        tramos = list(estado.get("pausas") or [])
        if estado.get("pausa"):
            tramos.append((estado["pausa"], 10 ** 9))
        partes, anunciados = [], set()
        # Lo que llega después del turno que lo aprobó no entra (`13·DOC24`).
        tope = self.turno_aprobado(estado["analisis"])
        for turno, bloque in self.bloques(texto):
            if turno < estado["desde"] or (tope is not None and turno > tope):
                continue
            tramo = next((t for t in tramos if t[0] <= turno <= t[1]), None)
            if tramo:
                if tramo not in anunciados:
                    anunciados.add(tramo)
                    if tramo[1] >= 10 ** 9:
                        partes.append("> En pausa desde el turno %d.\n" % tramo[0])
                    elif tramo[0] == tramo[1]:
                        partes.append("> Turno %d en pausa.\n" % tramo[0])
                    else:
                        partes.append("> Turnos %d a %d en pausa.\n" % tramo)
                continue
            partes.append(self.limpiar(bloque))
        cuerpo = "\n".join(partes)
        carpeta = os.path.dirname(estado["analisis"])
        subir = "../" * len(os.path.relpath(carpeta, raiz).split(os.sep))

        def ajustar(m):
            ruta = m.group(1)
            if not os.path.exists(os.path.join(raiz, ruta.split("#")[0])) and \
                    os.path.exists(os.path.join(carpeta, ruta.split("#")[0])):
                return m.group(0)
            return "](" + subir + ruta + ")"

        cuerpo = re.sub(r"\]\((?!https?:|#|\.\./)([^)]+)\)", ajustar, cuerpo)

        # Un enlace cuyo destino ya no existe (se movió después de la respuesta)
        # pasa como texto: lo dicho se conserva y el análisis no queda roto.
        def vigente(m):
            destino = m.group(2).split("#")[0]
            if re.match(r"https?:", destino) or os.path.exists(os.path.normpath(os.path.join(carpeta, destino))):
                return m.group(0)
            return "%s (`%s`, ya no está ahí)" % (m.group(1), destino.replace("../", "").lstrip("./"))

        return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", vigente, cuerpo)

    def pasar(self):
        """Copia la conversación al análisis prendido; apaga si ya se aprobó."""
        estado = self.leer_estado()
        if not estado or not os.path.isfile(estado["analisis"]):
            return False
        texto = _leer(estado["analisis"])
        if "## Conversación" not in texto or FIN not in texto:
            return False
        inicio = texto.index("## Conversación")
        nota = texto.find("\n> ", inicio)
        inicio = texto.index("\n\n", nota + 1) + 2 if nota != -1 else inicio + len("## Conversación\n\n")
        fin = texto.rindex(FIN)
        nuevo = texto[:inicio] + self.conversacion(estado) + "\n" + texto[fin:]
        if nuevo != texto:
            _escribir(estado["analisis"], nuevo)
        # Se apaga cuando la respuesta al turno que lo aprobó ya entró. Al cerrar
        # ese turno puede no estar todavía, porque el histórico la escribe en el
        # mismo evento; por eso también se apaga apenas llega el turno siguiente.
        tope = self.turno_aprobado(estado["analisis"])
        if tope is not None:
            transcripcion = _leer(estado["transcripcion"]) if os.path.isfile(estado["transcripcion"]) else ""
            bloques = dict(self.bloques(transcripcion))
            siguiente = any(n > tope for n in bloques)
            respondido = "\n**Agente**" in bloques.get(tope, "")
            if siguiente or respondido:
                self.borrar_estado()
        return True

    # ── el aviso ──────────────────────────────────────────────────────────

    def aviso(self, nota=""):
        """La línea que el agente recibe en cada mensaje."""
        estado = self.leer_estado()
        if not estado:
            linea = "Ningún análisis está prendido: la conversación no entra a ninguno."
        else:
            rel = os.path.relpath(estado["analisis"], self.raiz).replace(os.sep, "/")
            if estado.get("pausa"):
                linea = "El análisis %s está en pausa desde el turno %d." % (rel, estado["pausa"])
            else:
                linea = "La conversación entra al análisis %s." % rel
        return "[ANÁLISIS EN CURSO] " + linea + (" " + nota[0].upper() + nota[1:] + "." if nota else "")

    @staticmethod
    def esperar(transcripcion, segundos=5.0):
        """Espera a que el histórico anote el turno; los dos corren en el mismo evento."""
        if not transcripcion or not os.path.isfile(transcripcion):
            return
        antes = os.path.getmtime(transcripcion)
        limite = time.time() + segundos
        while time.time() < limite:
            time.sleep(0.25)
            if os.path.getmtime(transcripcion) != antes:
                time.sleep(0.5)
                return
