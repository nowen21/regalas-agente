"""El plan y los padres de cada fase: `02·F14`, `02·F17`, `02·F0`, `02·F2` y `02·F18`.

Recorre `documentacion/epicas/…/<fase>/` (la misma estructura que `fases`) y
comprueba sin criterio:

- F0: cada fase tiene sus **padres**: la épica y la HU de las que cuelga existen
  como documento, no solo como carpeta.
- F2: el plan **declara su especificación** y esa especificación existe; y, del
  otro lado, ningún módulo de `.agente/dominio.md` queda sin la suya.
- F14: el plan responde las 13 preguntas obligatorias, que la plantilla numera
  como secciones `## 0.` a `## 13.`; se marca cuáles faltan.
- F17: el plan no deja **incertidumbre** sin resolver: `TBD`, `(o similar)`,
  `(o donde esté)`, `(o parecido)`. La línea base debe ir verificada.
- F18: toda intervención del plan cuelga de un **criterio de aceptación**.
- F4 y F8: el plan aprobado desde 48.0.0 dice quién lo aprobó y cuándo, y su §2.1
  trae solo rutas exactas (`EP-023·HU-007`). Es FALLA: ya se aprobó.

No juzga el contenido de cada sección, que es humano. **AVISO** en lo demás: un
plan en curso puede estar incompleto a propósito. Los planes que preceden a esta
plantilla marcarán secciones faltantes: no conforman a F14, y no es un falso positivo.
"""
import os
import re

from ..comun import AVISO, FALLA, Hallazgo, Markdown
from ..enganches.plan_vs_hecho import PlanDeTrabajo
from .base import Validador
from .declaracion import DOMINIO, Declaracion
from .epicas import PENDIENTES, Epicas
from .version import VersionDelEstandar

CARPETA = "documentacion/epicas"

# F14 · las secciones que la plantilla numera 0..13 (una por bloque de preguntas).
_SECCIONES = list(range(0, 14))
_ENCABEZADO = re.compile(r"(?m)^#{1,4}\s*(\d{1,2})\.")

# F17 · marcas de que la línea base no se verificó.
_INCERTIDUMBRE = re.compile(
    r"(?i)\bTBD\b|\bpor\s+definir\b|\(o\s+(similar|donde\s+est[eé]|parecid[oa]|equivalente)\)")

# F18 · el desglose por criterio de aceptación.
_CA = re.compile(r"\bCA-(\d+)\b")
_TITULO_CA = re.compile(r"(?m)^#{2,4}\s*(CA-\d+|RNF)\b")
_TITULO = re.compile(r"(?m)^(#{1,4})\s*(.+?)\s*$")
_TAREA = re.compile(r"^\|\s*`?(T-\d+)`?\s*\|")
_SOPORTE = re.compile(r"(?i)soporte\s+(?:técnico\s+)?(?:de\s+)?CA-\d+")

# F2 · el marcador que la plantilla trae sin llenar en la fila de la especificación.
_SIN_LLENAR = re.compile(r"(?i)^\[?enlace\b|^«|^\.\.\.$")


class PlanDeLaFase(Validador):
    """Lo que el plan de cada fase tiene que traer, y los padres de la fase."""

    nombre = "flujo"
    regla = "02·F14"
    descripcion = "el plan de trabajo y los padres de cada fase"

    @staticmethod
    def revisar_plan(texto):
        """`(faltan_secciones, incertidumbres)` de un plan: los números F14 ausentes
        y los `(línea, fragmento)` dudosos. Aislado de git."""
        presentes = {int(n) for n in _ENCABEZADO.findall(texto)}
        faltan = [n for n in _SECCIONES if n not in presentes]
        incertidumbres = []
        for i, linea in enumerate(texto.splitlines(), 1):
            m = _INCERTIDUMBRE.search(linea)
            if m:
                incertidumbres.append((i, m.group(0)))
        return faltan, incertidumbres

    @staticmethod
    def revisar_ca(texto):
        """`F18`: cómo cuelga cada intervención de su CA.

        Devuelve `(tareas_sueltas, ca_sin_desglose, ca_no_declarados)`: las tareas
        `[(línea, tarea)]` que no viven bajo ningún CA, los CA que la fase declara
        en §0 y no desglosa en §3, y los que aparecen en §3 sin declararse. La fila
        de **soporte técnico** que dice «soporte de CA-x» se admite sin CA propio,
        que es la excepción de la regla.
        """
        seccion, ca_actual = None, None
        declarados, desglosados, sueltas = set(), set(), []
        for n, linea in enumerate(texto.splitlines(), start=1):
            if _TITULO.match(linea):
                m = _ENCABEZADO.match(linea)
                if m:
                    seccion = int(m.group(1))
                marca = _TITULO_CA.match(linea)
                ca_actual = marca.group(1) if marca else None
                if marca and seccion == 3 and marca.group(1) != "RNF":
                    desglosados.add(marca.group(1))
                continue
            if seccion in (None, 0):
                declarados |= {f"CA-{d}" for d in _CA.findall(linea)}
            if seccion == 3 and _TAREA.match(linea) and not ca_actual:
                if not _SOPORTE.search(linea) and not _CA.search(linea):
                    sueltas.append((n, _TAREA.match(linea).group(1)))
        return sueltas, sorted(declarados - desglosados), sorted(desglosados - declarados)

    @staticmethod
    def revisar_especificacion(texto):
        """`F2`: la ruta que el plan declara como especificación del módulo, o "" si
        no la declara o dejó el marcador de la plantilla."""
        for _, fila in Markdown.filas_de(texto, "campo", "valor"):
            if "especificación" not in fila["campo"].lower():
                continue
            crudo = fila["valor"].strip()
            enlace = re.search(r"\]\(([^)\s]+)", crudo)
            if enlace:
                return enlace.group(1)
            valor = Markdown.valor_limpio(crudo)
            if not valor or _SIN_LLENAR.match(valor) or valor.startswith("["):
                return ""
            return valor
        return ""

    @staticmethod
    def especificacion_existe(proyecto, carpeta_fase, ruta):
        """Se busca donde la escribiría cualquiera: relativa al plan, o desde la raíz."""
        ruta = ruta.split("#", 1)[0].replace("\\", "/")
        if not ruta or ruta.startswith(("http://", "https://")):
            return True
        for base in (carpeta_fase, proyecto):
            if os.path.exists(os.path.normpath(os.path.join(base, *ruta.split("/")))):
                return True
        return False

    def modulos_sin_especificacion(self):
        """F2 visto desde el otro lado: un módulo declarado cuya especificación no está."""
        raiz = self.proyecto.raiz
        dominio = os.path.join(raiz, DOMINIO)
        hallazgos = []
        for modulo in Declaracion.leer(self.proyecto, self.archivos).modulos:
            if not modulo.especificacion:
                hallazgos.append(Hallazgo(
                    AVISO, dominio, 0,
                    f"el módulo `{modulo.nombre}` no declara su especificación — F2: sin especificación "
                    f"acordada no hay código"))
                continue
            if not os.path.exists(os.path.normpath(os.path.join(raiz, *modulo.especificacion.split("/")))):
                hallazgos.append(Hallazgo(
                    AVISO, dominio, 0,
                    f"el módulo `{modulo.nombre}` declara la especificación `{modulo.especificacion}` "
                    f"y ese archivo no existe (F2)"))
        return hallazgos

    def _revisar_fase(self, plan, donde):
        texto_plan = self.archivos.leer(plan)
        faltan, incertidumbres = self.revisar_plan(texto_plan)
        hallazgos = []
        # F2 · el plan declara su especificación, y la especificación existe.
        especificacion = self.revisar_especificacion(texto_plan)
        if not especificacion:
            hallazgos.append(Hallazgo(AVISO, donde, 0, "el plan no declara la especificación del módulo "
                                                       "(F2: sin especificación acordada no hay código)"))
        elif not self.especificacion_existe(self.proyecto.raiz, os.path.dirname(plan), especificacion):
            hallazgos.append(Hallazgo(AVISO, donde, 0, f"el plan declara la especificación `{especificacion}` "
                                                       f"y ese archivo no existe (F2)"))
        # F18 · cada intervención cuelga de un CA.
        sueltas, sin_desglose, no_declarados = self.revisar_ca(texto_plan)
        for linea, tarea in sueltas:
            hallazgos.append(Hallazgo(AVISO, donde, linea, f"la intervención `{tarea}` no cuelga de ningún "
                                                           f"criterio de aceptación (F18)"))
        if sin_desglose:
            hallazgos.append(Hallazgo(AVISO, donde, 0, "la fase declara criterios que no desglosa en tareas: "
                                      + ", ".join(sin_desglose) + " (F18)"))
        if no_declarados:
            hallazgos.append(Hallazgo(AVISO, donde, 0, "el plan desglosa criterios que la fase no declaró en §0: "
                                      + ", ".join(no_declarados) + " (F18)"))
        if faltan:
            hallazgos.append(Hallazgo(AVISO, donde, 0, "al plan le faltan secciones de las 13 preguntas (F14): "
                                      + ", ".join(map(str, faltan))))
        for linea, frag in incertidumbres:
            hallazgos.append(Hallazgo(AVISO, donde, linea, f"marca de incertidumbre `{frag}` en el plan — F17 pide "
                                                           f"la línea base verificada"))
        # `EP-023·HU-007` · el plan aprobado desde 48.0.0 dice quién lo aprobó y
        # declara rutas exactas.
        for linea, motivo in PlanDeTrabajo.revisar_aprobado(texto_plan):
            hallazgos.append(Hallazgo(FALLA, donde, linea, motivo))
        return hallazgos

    def validar(self):
        raiz = os.path.join(self.proyecto.raiz, *CARPETA.split("/"))
        if not os.path.isdir(raiz):
            return [Hallazgo(FALLA, self.proyecto.raiz, 0, f"no existe `{CARPETA}` (F12.13)")]
        hallazgos = []
        hay_fases = False
        for nombre_epica in Epicas.subcarpetas(raiz):
            ruta_epica = os.path.join(raiz, nombre_epica)
            # F0 · la épica existe como documento, no solo como carpeta.
            tiene_doc_epica = any(os.path.isfile(os.path.join(ruta_epica, n))
                                  for n in ("epica.md", f"{nombre_epica}.md"))
            epica_con_fases = False
            for nombre_hu in Epicas.subcarpetas(ruta_epica):
                if nombre_hu == PENDIENTES:
                    continue                # EP-023·HU-003 · los pendientes de la épica
                ruta_hu = os.path.join(ruta_epica, nombre_hu)
                tiene_fases = bool([f for f in Epicas.subcarpetas(ruta_hu) if f != PENDIENTES])
                epica_con_fases = epica_con_fases or tiene_fases
                # F0 · la HU existe como documento.
                if tiene_fases and not os.path.isfile(os.path.join(ruta_hu, f"{nombre_hu}.md")):
                    hallazgos.append(Hallazgo(AVISO, f"{CARPETA}/{nombre_epica}/{nombre_hu}", 0,
                                              "hay fases pero la HU no tiene su documento (F0: falta el padre)"))
                for nombre_fase in Epicas.subcarpetas(ruta_hu):
                    plan = os.path.join(ruta_hu, nombre_fase, "plan_trabajo.md")
                    if os.path.isfile(plan):
                        hallazgos += self._revisar_fase(
                            plan, f"{CARPETA}/{nombre_epica}/{nombre_hu}/{nombre_fase}/plan_trabajo.md")
            if epica_con_fases and not tiene_doc_epica:
                hallazgos.append(Hallazgo(AVISO, f"{CARPETA}/{nombre_epica}", 0,
                                          "hay fases pero la épica no tiene su documento (F0: falta el padre)"))
            hay_fases = hay_fases or epica_con_fases
        # F22 · con una derogación sin adoptar no se abre ni se cierra fase. Solo
        # se cobra donde hay fases: sin ellas, el desfase se queda en aviso.
        if hay_fases:
            hallazgos += VersionDelEstandar(self.proyecto, self.archivos).validar_fase()
        return hallazgos + self.modulos_sin_especificacion()
