"""Revisión de arranque de sesión: la señal de que el estándar se cargó.

Responde tres preguntas al abrir una sesión en un proyecto:

  1. ¿Cumple `02·F13`? (existe `proyectos/`)
  2. ¿El `CLAUDE.md` está al día con la plantilla central? (`01·C18`)
  3. ¿Los enganches automáticos están puestos?

**Por qué existe:** C18 manda sincronizar el `CLAUDE.md`, y era una regla que
el agente cumplía si se acordaba, sin dejar señal cuando no. Esto la vuelve un
hecho comprobable. La llama el enganche `SessionStart` (`hook_sesion.py`).
"""
import os
import re

from ..comun import AVISO, FALLA, Hallazgo, Markdown, Proyecto
from ..comun.enganches import ENGANCHES_GIT
from ..validadores.base import Validador
from ..validadores.version import VersionDelEstandar

PLANTILLA_CLAUDE = "plantillas/CLAUDE.md.plantilla"

# La plantilla marca lo que hay que reemplazar con «comillas angulares». Se
# excluye «…»: es cómo se nombra a un marcador cuando el texto habla de ellos,
# y tratarlo como hueco reprobaría una frase bien escrita.
_SIN_LLENAR = re.compile(r"«(?!…»)[^»\n]+»")

# Se compara contra la línea `ESTANDAR="…"` del propio enganche: la ruta del
# validador está partida entre la variable y su uso, y buscarla entera daba
# siempre «apunta a otro estándar».
_ESTANDAR_EN_HOOK = re.compile(r'^ESTANDAR="([^"]+)"', re.MULTILINE)


def _leer(ruta):
    try:
        with open(ruta, encoding="utf-8") as f:
            return f.read()
    except UnicodeDecodeError:
        with open(ruta, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""



def _instalador():
    """La clase del instalador, cargada al usarla: traerla arriba armaba un
    ciclo con los validadores (fila 23 del análisis 1 del pendiente 116)."""
    from ..herramientas.instalar import Instalador
    return Instalador

class ArranqueDeSesion(Validador):
    """Las comprobaciones de arranque, en orden de precedencia.

    `validar.py` no tiene subcomando para esto: lo corre el enganche de inicio
    de sesión. El nombre es el que su descripción venía prometiendo.
    """

    nombre = "sesion"
    regla = "01·C18"
    descripcion = "que el estándar quedó cargado al abrir la sesión"

    def __init__(self, proyecto, archivos=None, estandar=None):
        super().__init__(proyecto, archivos)
        self.estandar = estandar or Proyecto.estandar()

    def revisar_claude_md(self):
        """`01·C18`: el `CLAUDE.md` local contra la plantilla central. Solo se
        informa lo que **falta**, nunca lo que sobra: C18 es aditiva."""
        local = os.path.join(self.proyecto.raiz, "CLAUDE.md")
        plantilla = os.path.join(self.estandar, *PLANTILLA_CLAUDE.split("/"))

        if not os.path.isfile(local):
            return [Hallazgo(FALLA, local, 0, "no existe el CLAUDE.md del proyecto")]
        if not os.path.isfile(plantilla):
            return [Hallazgo(AVISO, plantilla, 0, "no se encontró la plantilla central")]

        texto = _leer(local)
        hallazgos = []

        presentes = {t for _, t in Markdown.encabezados(texto)}
        for _, titulo in Markdown.encabezados(_leer(plantilla)):
            if titulo not in presentes:
                hallazgos.append(Hallazgo(
                    AVISO, local, 0,
                    f"la plantilla central tiene «{titulo}» y este CLAUDE.md no "
                    f"— C18: agregar la sección vacía, sin pisar lo escrito"))

        for n, linea in enumerate(texto.splitlines(), start=1):
            for m in _SIN_LLENAR.finditer(linea):
                hallazgos.append(Hallazgo(FALLA, local, n, f"quedó sin reemplazar: {m.group(0)}"))

        # Comparar títulos no ve un cambio dentro de una sección que ya existe.
        # La fecha sí lo delata: no dice QUÉ cambió, dice que hay que mirar.
        if os.path.getmtime(plantilla) > os.path.getmtime(local):
            hallazgos.append(Hallazgo(
                AVISO, local, 0,
                "la plantilla central cambió después de este CLAUDE.md "
                "— C18: revisar si hay algo nuevo que agregar"))

        return hallazgos

    def revisar_enganches(self, proyecto=None):
        """¿Los enganches de git están puestos y apuntando a este estándar?"""
        proyecto = proyecto or self.proyecto.raiz
        hallazgos = []
        esperado = os.path.normcase(self.estandar.replace(os.sep, "/"))

        for repo in _instalador().repositorios_git(proyecto):
            etiqueta = os.path.relpath(repo, proyecto).replace("\\", "/")
            donde = repo if etiqueta == "." else f"{etiqueta}/"
            for nombre in ENGANCHES_GIT:
                archivo = os.path.join(repo, ".githooks", nombre)
                if not os.path.isfile(archivo):
                    hallazgos.append(Hallazgo(
                        AVISO, donde, 0,
                        f"falta el enganche {nombre} — correr validadores/instalar.py"))
                    continue
                m = _ESTANDAR_EN_HOOK.search(_leer(archivo))
                apunta = os.path.normcase(m.group(1)) if m else None
                if apunta != esperado:
                    hallazgos.append(Hallazgo(
                        AVISO, donde, 0,
                        f"el enganche {nombre} apunta a «{apunta or '?'}» y no a "
                        f"este estándar — reinstalar"))
        return hallazgos

    def validar(self):
        # F13 primero: sin la estructura base lo demás no tiene sentido todavía,
        # y si falta es que el proyecto nunca se instaló.
        if not _instalador().cumple_f13(self.proyecto.raiz):
            return [Hallazgo(FALLA, self.proyecto.raiz, 0,
                             "falta la carpeta `proyectos/` (02·F13): este proyecto "
                             "no está instalado — correr validadores/instalar.py "
                             "--aplicar")]

        # **El aviso de quedarse atrás va acá**: como subcomando suelto no
        # llegaba nunca a un proyecto instalado (pendiente 83).
        return (self.revisar_claude_md()
                + self.revisar_enganches()
                + VersionDelEstandar(self.proyecto, estandar=self.estandar).validar()
                + self.revisar_pruebas())

    def revisar_pruebas(self):
        """`EP-029·HU-003` · Si la revisión de pruebas falta o está vencida, se
        avisa como se avisa lo de la instalación (análisis 1 del pendiente 141,
        acuerdo 7)."""
        from ..pruebas.aviso import RevisionDelProyecto
        textos, _ = RevisionDelProyecto(self.proyecto.raiz, self.estandar).avisos()
        return [Hallazgo(AVISO, self.proyecto.raiz, 0, texto) for texto in textos]

    revisar = validar

    @staticmethod
    def resumen(proyecto, hallazgos):
        """Una línea para mostrarle al usuario al abrir la sesión."""
        nombre = os.path.basename(os.path.abspath(proyecto))
        fallas = sum(1 for h in hallazgos if h.severidad == FALLA)
        avisos = len(hallazgos) - fallas

        if not hallazgos:
            return f"Estándar cargado · {nombre} · F13 ok · CLAUDE.md al día · enganches puestos"

        partes = []
        if fallas:
            partes.append(f"{fallas} falla(s)")
        if avisos:
            partes.append(f"{avisos} aviso(s)")
        detalle = "; ".join(h.mensaje for h in hallazgos[:3])
        if len(hallazgos) > 3:
            detalle += f"; y {len(hallazgos) - 3} más"
        return f"Estándar cargado · {nombre} · {' y '.join(partes)}: {detalle}"
