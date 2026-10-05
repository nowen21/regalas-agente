"""Lo que una sesión deja: crea el resumen, dice qué le falta y qué sigue abierto.

No escribe hallazgos ni los interpreta: reconocer uno es criterio, y el criterio
no lo tiene un programa. Lo que sí hace es que el hueco se vea. Tres cosas, y
ninguna más:

- **Crear** el archivo del resumen al abrir la sesión, con el modelo puesto.
- **Decir qué falta**: si no hay ningún hallazgo, o si nadie dijo todavía si la
  sesión se puede cerrar.
- **Buscar lo que sigue abierto del propósito** de la sesión, para que quien la
  retoma no tenga que ir a buscarlo.

El resumen se llama igual que la transcripción, sin la fecha, y vive en la
carpeta del día: `historico-chat/resumenes/AAAA-MM-DD/«tema».md`. Los dos nombres
se mueven juntos cuando la sesión se renombra; de eso se encarga el histórico.

Lo exige `13·DOC22`; el modelo es `plantillas/sesion.md`.
"""
import os
import re

from ..comun import Proyecto
from ..validadores.pendientes import Pendientes

CARPETA = "historico-chat"
RESUMENES = "resumenes"
MODELO = os.path.join("plantillas", "sesion.md")

# `### H-1 · título del hallazgo`
_HALLAZGO = re.compile(r"^### (H-\d+) · (.+)$", re.MULTILINE)


def _campo(nombre, vineta="- "):
    """El valor de un campo del resumen, en la fila de tabla del molde (desde la
    39.5.0) o en la viñeta de los resúmenes anteriores, que no se reescriben. El
    molde pasó a tabla porque la viñeta llena es una marca de `00·ID8`."""
    return re.compile(r"^(?:" + re.escape(vineta) + r"\*\*" + re.escape(nombre)
                      + r":\*\*|\| " + re.escape(nombre) + r" \|)\s*(.+?)\s*\|?\s*$",
                      re.MULTILINE)


_ESTADO = _campo("Estado")
_PENDIENTE = _campo("Pendiente")

# La sección de cierre y sus casillas.
_CIERRE = "## ¿Se puede cerrar la sesión?"
_SIN_MARCAR = re.compile(r"^\|.*☐", re.MULTILINE)

# `### 3 · título`: un hallazgo escrito sin la `H-` que el molde pide.
_CASI_HALLAZGO = re.compile(r"^### \d+ · (.+)$", re.MULTILINE)

_CORRIJA = re.compile(r"^\|\s*Corregido con «Corrija»\s*\|", re.M)

# Queda dentro del resumen cuando ya se avisó, para no repetir el aviso.
MARCA_VACIO = "<!-- aviso: resumen sin hallazgos -->"
MARCA_CIERRE = "<!-- aviso: falta decir si la sesión se puede cerrar -->"
MARCA_MOLDE = "<!-- aviso: hallazgos sin la H del molde -->"


def _leer(ruta):
    with open(ruta, encoding="utf-8") as f:
        return f.read()


def _escribir(ruta, texto):
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


class Resumen:
    """El resumen de una sesión: dónde vive, cómo nace y qué le falta."""

    # ── dónde vive ────────────────────────────────────────────────────────

    @staticmethod
    def ruta_de(raiz, transcripcion):
        """La ruta del resumen que le corresponde a esa transcripción, o "".

        De `2026-08-14-tema.md` sale `resumenes/2026-08-14/tema.md`. Si el nombre
        todavía no tiene tema, el resumen se llama igual que la transcripción sin
        la fecha, y se moverá cuando la sesión se nombre.
        """
        m = re.match(r"^(\d{4}-\d{2}-\d{2})-(.+\.md)$", os.path.basename(transcripcion))
        if not m:
            return ""
        return os.path.join(raiz, CARPETA, RESUMENES, m.group(1), m.group(2))

    # ── crear ─────────────────────────────────────────────────────────────

    @classmethod
    def crear(cls, raiz, transcripcion, estandar=""):
        """Crea el resumen con el modelo puesto. Devuelve su ruta, o "".

        No pisa lo que ya esté escrito. Un proyecto sin carpeta de resúmenes no se
        ve afectado, y eso es a propósito: no todos llevan histórico.
        """
        if not os.path.isdir(os.path.join(raiz, CARPETA, RESUMENES)):
            return ""
        ruta = cls.ruta_de(raiz, transcripcion)
        if not ruta:
            return ""
        if os.path.isfile(ruta):
            return ruta
        modelo = os.path.join(estandar or raiz, MODELO)
        if not os.path.isfile(modelo):
            return ""
        dia = os.path.dirname(ruta)
        try:
            os.makedirs(dia, exist_ok=True)
            _escribir(ruta, cls.desde_modelo(_leer(modelo), os.path.basename(transcripcion)))
        except OSError:
            return ""                       # sin permiso o sin espacio: no detiene
        cls.indexar_dia(dia, os.path.basename(ruta))
        cls.indexar_dias(raiz, os.path.basename(dia))
        return ruta

    @staticmethod
    def desde_modelo(modelo, transcripcion):
        """El cuerpo del resumen nuevo: el modelo, sin ejemplos y sin hallazgos.

        Los hallazgos de ejemplo **no** se copian: uno escrito por el programa se
        contaría como trabajo hecho. Sí se copia la sección de cierre, que es la
        pregunta que hay que responder para poder cerrar la sesión. El encabezado
        no enlaza `plantillas/sesion.md`, que no viaja a los proyectos: enlaza el
        índice del histórico, que el instalador deja en todos.
        """
        fecha = transcripcion[:10]
        partes = modelo.split(_CIERRE, 1)
        cola = ("\n\nNada todavía.\n\n---\n\n" + _CIERRE + partes[1]) if len(partes) > 1 else "\n"
        return (f"# {fecha} · lo que quedó\n\n"
                f"Hallazgos de la sesión transcrita en "
                f"[{CARPETA}/{transcripcion}](../../{transcripcion}). Cómo se llena "
                f"está en [{CARPETA}/README.md](../../README.md). "
                f"La conversación está allá; acá queda lo que la sesión dejó.\n\n"
                f"| Campo | Valor |\n|---|---|\n| Viene de | «...» |\n\n---\n\n"
                f"## Hallazgos de esta sesión{cola}")

    @staticmethod
    def indexar_dia(carpeta, nombre):
        """Agrega la línea al índice del día. Si no hay índice, lo crea."""
        ruta = os.path.join(carpeta, "README.md")
        fecha = os.path.basename(carpeta)
        linea = f"| [{nombre}]({nombre}) | Sin escribir todavía. |\n"
        if not os.path.isfile(ruta):
            _escribir(ruta, f"# {fecha}\n\nResúmenes de las sesiones de este día. "
                            f"Uno por sesión.\n\n| Sesión | Qué dejó |\n|---|---|\n" + linea)
            return
        texto = _leer(ruta)
        if f"({nombre})" in texto:
            return
        _escribir(ruta, texto.rstrip("\n") + "\n" + linea)

    @staticmethod
    def indexar_dias(raiz, dia):
        """Agrega la línea del día al índice de días.

        `32` · El enganche creaba la carpeta del día y el resumen dentro sin tocar
        este índice, y el 2026-08-15 quedó con dos resúmenes que nadie nombraba:
        un resumen fuera del índice es un resumen que nadie va a abrir. Poner el
        nombre de una carpeta en una lista no interpreta nada (`13·DOC22`).
        """
        ruta = os.path.join(raiz, CARPETA, RESUMENES, "README.md")
        if not os.path.isfile(ruta):
            return
        texto = _leer(ruta)
        if f"({dia}/)" in texto:
            return
        # El texto con la ruta desde la raíz (`13·DOC14`); el destino, relativo.
        linea = f"- [{CARPETA}/{RESUMENES}/{dia}/]({dia}/) — sin escribir todavía."
        # Va al final: la sección de días es la última y un día nuevo es el más reciente.
        if "## Días" in texto:
            _escribir(ruta, texto.rstrip("\n") + "\n" + linea + "\n")
        else:
            _escribir(ruta, texto.rstrip("\n") + "\n\n## Días\n\n" + linea + "\n")

    # ── los hallazgos ─────────────────────────────────────────────────────

    @classmethod
    def hallazgos(cls, ruta):
        """Los hallazgos escritos: lista de (id, título, estado)."""
        if not os.path.isfile(ruta):
            return []
        texto = _leer(ruta)
        ids = [(m.group(1), m.group(2), m.start()) for m in _HALLAZGO.finditer(texto)]
        estados = [(m.group(1), m.start()) for m in _ESTADO.finditer(texto)]
        salida = []
        for i, (hid, titulo, pos) in enumerate(ids):
            fin = ids[i + 1][2] if i + 1 < len(ids) else len(texto)
            estado = next((e for e, p in estados if pos < p < fin), "")
            if not estado and _CORRIJA.search(texto[pos:fin]):
                estado = "resuelto"         # corregido con «Corrija» (`02·F8`, excepción)
            if not estado:
                # `EP-023·HU-003` · El hallazgo de la forma nueva no escribe su
                # estado: se calcula. El escrito se lee como siempre.
                estado = cls.estado_calculado(ruta, texto[pos:fin])[0]
            salida.append((hid, titulo, estado.rstrip(".").strip().lower()))
        return salida

    @staticmethod
    def carpeta_del_pendiente(ruta, bloque):
        """La carpeta del pendiente que enlaza el hallazgo, o "" si no enlaza ninguno."""
        m = _PENDIENTE.search(bloque)
        if not m:
            return ""
        for enlace in re.findall(r"\]\(([^)#\s]+)", m.group(1)):
            destino = os.path.normpath(os.path.join(os.path.dirname(ruta), enlace.replace("/", os.sep)))
            if os.path.basename(destino) == "pendiente.md":
                destino = os.path.dirname(destino)
            if os.path.isfile(os.path.join(destino, "pendiente.md")):
                return destino
        return ""

    @classmethod
    def estado_calculado(cls, ruta, bloque):
        """`EP-023·HU-003·CA-05` · (estado, retoma) de un hallazgo, siguiendo su enlace.

        Sin pendiente: «abierto, sin pendiente». Con pendiente abierto: «abierto,
        anotado», y se retoma por el último análisis del pendiente. Con el plan
        cumplido: «resuelto» (análisis 1 del pendiente 103, conclusión 35).
        """
        carpeta = cls.carpeta_del_pendiente(ruta, bloque)
        if not carpeta:
            return "abierto, sin pendiente", ""
        estandar = Proyecto(Proyecto.estandar())
        if Pendientes(estandar).estado(carpeta) == "cerrado":
            return "resuelto", ""
        analisis = Pendientes.analisis_de(carpeta)
        retoma = analisis[-1] if analisis else os.path.join(carpeta, "pendiente.md")
        return "abierto, anotado", estandar.mostrar(retoma)

    @staticmethod
    def falta(ruta):
        """Qué le falta al resumen: lista de claves entre `vacio`, `molde` y `cierre`.

        Son huecos distintos y se avisan por separado, una vez cada uno. **Vacío e
        ilegible no son lo mismo**: decir «vacío» sobre un archivo con quince
        hallazgos escritos como `### N ·` hace que quien lo lee dé el aviso por
        equivocado y siga.
        """
        if not os.path.isfile(ruta):
            return []
        texto = _leer(ruta)
        pendientes = []
        if not _HALLAZGO.search(texto):
            if _CASI_HALLAZGO.search(texto):
                if MARCA_MOLDE not in texto:
                    pendientes.append("molde")
            elif MARCA_VACIO not in texto:
                pendientes.append("vacio")
            return pendientes
        cuerpo = texto.split(_CIERRE, 1)
        sin_cierre = len(cuerpo) < 2 or _SIN_MARCAR.search(cuerpo[1])
        if sin_cierre and MARCA_CIERRE not in texto:
            pendientes.append("cierre")
        return pendientes

    @staticmethod
    def hallazgos_fuera_del_molde(ruta):
        """Los títulos escritos como `### 3 ·` en vez de `### H-3 ·`.

        **Un resumen así queda mudo**: el programa no ve ni un hallazgo y la
        comprobación del cierre tampoco corre. Pasó con tres resúmenes del
        2026-08-17 y 29 hallazgos entre los tres.
        """
        if not os.path.isfile(ruta):
            return []
        texto = _leer(ruta)
        if _HALLAZGO.search(texto):
            return []                       # ya tiene los suyos: no hay nada que decir
        return _CASI_HALLAZGO.findall(texto)

    @staticmethod
    def marcar_avisado(ruta, clave):
        """Deja la marca del aviso dentro del propio resumen, para no repetirlo: un
        registro aparte se desincroniza, y la marca vive donde vive el dato."""
        marca = {"vacio": MARCA_VACIO, "molde": MARCA_MOLDE}.get(clave, MARCA_CIERRE)
        if not os.path.isfile(ruta):
            return
        texto = _leer(ruta)
        if marca in texto:
            return
        try:
            _escribir(ruta, texto.rstrip("\n") + f"\n\n{marca}\n")
        except OSError:
            pass                            # no poder marcarlo no detiene la sesión

    @classmethod
    def sin_resolver(cls, ruta):
        """Los hallazgos del resumen que siguen abiertos: lista de (id, título)."""
        return [(h, t) for h, t, e in cls.hallazgos(ruta) if e.startswith("abierto")]

    # ── lo abierto del propósito ──────────────────────────────────────────

    @staticmethod
    def viene_de(ruta):
        """El propósito declarado de la sesión: el texto de su «viene de», o ""."""
        if not os.path.isfile(ruta):
            return ""
        m = _campo("Viene de", vineta="").search(_leer(ruta))
        if not m:
            return ""
        crudo = m.group(1).strip()
        return "" if crudo.startswith(("«", "—")) else crudo

    @classmethod
    def proposito(cls, raiz, ruta):
        """El hallazgo que la sesión viene a resolver, si sigue abierto.

        Devuelve (ruta del resumen donde vive, id, título, pregunta viva), o None.
        **Solo el del propósito**: los hallazgos de otro tema son ruido, y el ruido
        se deja de leer.
        """
        declarado = cls.viene_de(ruta)
        if not declarado:
            return None
        m = re.search(r"(\d{4}-\d{2}-\d{2})\s*·\s*\[?([^·\]]+?)\s*·\s*\[?(H-\d+)", declarado)
        if not m:
            return None
        fecha, tema, hid = m.group(1), m.group(2).strip(), m.group(3)
        origen = os.path.join(raiz, CARPETA, RESUMENES, fecha, f"{tema}.md")
        if not os.path.isfile(origen):
            return None
        for h, titulo, estado in cls.hallazgos(origen):
            if h == hid and estado.startswith("abierto"):
                return (origen, h, titulo, cls.retoma(origen, h))
        return None

    @classmethod
    def retoma(cls, ruta, hid):
        """El «con qué se retoma» de ese hallazgo, o "" si no lo tiene."""
        texto = _leer(ruta)
        bloque = re.split(r"^### H-\d+ · ", texto, flags=re.MULTILINE)
        for i, m in enumerate(re.finditer(r"^### (H-\d+) · ", texto, re.MULTILINE)):
            if m.group(1) == hid and i + 1 < len(bloque):
                r = _campo("Con qué se retoma").search(bloque[i + 1])
                if r:
                    return r.group(1)
                # En la forma nueva no se escribe: es el último análisis de su pendiente.
                return cls.estado_calculado(ruta, bloque[i + 1])[1]
        return ""
