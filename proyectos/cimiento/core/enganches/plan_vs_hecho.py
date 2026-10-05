"""`EP-004 · HU-013` · Lo hecho contra el plan aprobado.

**Qué compara.** Un plan de trabajo declara en su §2.1 qué archivos va a tocar,
y `02·F8` exige que se toquen **esos**. Un plan de pruebas declara sus casos y
la fase sus criterios, y cada criterio tiene que tener quien lo compruebe. Las
dos cosas se comprobaban leyendo, o sea casi nunca.

**Contra qué se comparan los archivos tocados: contra el commit del que salió la
fase** (decisión 22 del pendiente 59). La rama arrastra trabajo ajeno y lo sin
guardar cambia mientras se mira; el commit de origen es el único punto fijo.

**Avisa, nunca detiene**, salvo en el commit: un archivo de más puede ser un
descubrimiento legítimo que se aprobó, y eso no se ve desde el disco. Lo que el
programa dice es **que la lista no cuadra**; si cuadra la explicación, lo lee
una persona.

**Lo que no compara, y se declara:** si los pasos que el resultado dice haber
ejecutado son los que el plan de pruebas escribió. Eso es criterio humano
(decisión 10 del pendiente 59), y así está en `reglas-validables.md`.

`PlanDeTrabajo` lee el plan; `PlanContraLoHecho` es el validador. Lo que manda
hacer el análisis prendido lo sabe el freno: se importa dentro del método,
porque el freno a su vez lee el plan con `PlanDeTrabajo`.
"""
import os
import re

from ..comun import AVISO, FALLA, Git, Hallazgo, Markdown, Proyecto
from ..validadores.base import Validador
from .autorizado import Autorizaciones

# La tabla de archivos del plan: su §2.1. Se buscan rutas entre comillas
# invertidas, que es como el molde las escribe.
_SECCION_ARCHIVOS = re.compile(r"(?ms)^###\s*2\.1[^\n]*\n(.*?)(?=^###\s|\Z)")
_RUTA = re.compile(r"`([\w][\w./\\-]*\.[\w]{1,5}|[\w][\w./\\-]*/)`")

# Los casos del plan de pruebas y los criterios que la fase declara cubrir.
_CASO = re.compile(r"(?m)^###?\s*(CP-\d+)")
_CRITERIO_EN_PLAN = re.compile(r"\b(CA-\d+)\b")

# Lo que nunca cuenta como «archivo tocado de más»: los documentos de la propia
# fase. Escribir el resultado de las pruebas **es** ejecutar la fase.
DE_LA_FASE = ("plan_trabajo.md", "plan_pruebas.md", "resultado_pruebas.md",
              "estado-fase.md", "funcionalidad_implementada.md", "README.md")

# `EP-023·HU-007` · Desde esta versión el plan dice quién lo aprobó y con qué
# versión, su §2.1 trae solo rutas exactas y el commit se compara con ella. Los
# planes aprobados antes no se revisan: se escribieron con otro molde.
DESDE = (48, 0, 0)
_APROBACION = re.compile(r"^\|?\s*\*\*Aprobación\*\*[^:|\n]*[:|]\s*(.*)$", re.M)
_VERSION = re.compile(r"con la versión\s*\**v?(\d+)\.(\d+)\.(\d+)")
_FECHA = re.compile(r",?\s*el\s+(\d{4}-\d{2}-\d{2})\b")
_SOLO_RUTAS = re.compile(r"`[^`*\s]*[^`*\s/]`(?:\s*,\s*`[^`*\s]*[^`*\s/]`)*")

_IMPORTA = r"^\s*(?:import\s+%s\b|from\s+%s\s+import\b)"
_ANALISIS_EN_EL_COMMIT = re.compile(r"/pendientes/[^/]+/analisis-\d+\.md$")

# `EP-023·HU-008` · La aprobación que viene de un análisis lo enlaza en el lugar
# de «quién»; vale si el análisis está aprobado y su «Lo que se tiene que hacer»
# nombra la HU del plan («`EP-023` HU-008»).
_ANALISIS_QUE_APRUEBA = re.compile(r"\]\(([^)#\s]*analisis-\d+\.md)\)")
_ANALISIS_APROBADO = re.compile(r"^> \*\*Aprobado\*\*", re.M)
_LO_QUE_SE_TIENE_QUE_HACER = re.compile(r"(?ms)^## Lo que se tiene que hacer\s*\n(.*?)(?=^## |\Z)")
_HU_DE_LA_FASE = re.compile(r"-EP-(\d+)-HU-(\d+)-")
_HU_NOMBRADA = re.compile(r"EP-(\d+)`?\s*·?\s*HU-(\d+)")


def _leer(ruta):
    try:
        with open(ruta, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


class PlanDeTrabajo:
    """Lo que se lee de un `plan_trabajo.md`. Todo es estático."""

    @staticmethod
    def declarados(plan_texto):
        """Las rutas que el plan declara en su §2.1, sin repetir."""
        m = _SECCION_ARCHIVOS.search(plan_texto)
        if not m:
            return []
        vistas, salida = set(), []
        for ruta in _RUTA.findall(m.group(1)):
            limpia = ruta.replace("\\", "/").lstrip("./")
            if limpia and limpia not in vistas:
                vistas.add(limpia)
                salida.append(limpia)
        return salida

    @staticmethod
    def cuadra(tocado, declarados):
        """¿Ese archivo tocado está declarado, aunque sea por su carpeta?"""
        for d in declarados:
            if tocado == d or (d.endswith("/") and tocado.startswith(d)):
                return True
            # El plan suele nombrar la carpeta o el archivo sin su ruta completa.
            if tocado.endswith("/" + d) or d.endswith("/" + tocado):
                return True
        return False

    @staticmethod
    def aprobacion(plan_texto):
        """`(quién, fecha, versión)` de la línea de aprobación del plan; lo que no
        diga va en `None`. Sin línea, `None`."""
        m = _APROBACION.search(plan_texto)
        if not m:
            return None
        texto = m.group(1).strip().rstrip("|").strip()
        v = _VERSION.search(texto)
        f = _FECHA.search(texto)
        quien = texto[:f.start()].strip(" ,") if f else ""
        return (quien if quien and "«" not in quien else None,
                f.group(1) if f else None,
                tuple(int(x) for x in v.groups()) if v else None)

    @classmethod
    def aprobado_desde(cls, plan_texto, desde=DESDE):
        """¿El plan se aprobó con esa versión del estándar o una posterior?"""
        a = cls.aprobacion(plan_texto)
        return bool(a and a[2] and a[2] >= desde)

    @classmethod
    def analisis_citado(cls, ruta_plan, plan_texto):
        """La ruta del `analisis-N.md` que la aprobación cita en el lugar de «quién»,
        o `None` si la aprobó una persona (`EP-023·HU-008`)."""
        a = cls.aprobacion(plan_texto)
        m = _ANALISIS_QUE_APRUEBA.search(a[0] or "") if a else None
        if not m:
            return None
        return os.path.normpath(os.path.join(os.path.dirname(ruta_plan), m.group(1)))

    @classmethod
    def aprobado(cls, ruta_plan, plan_texto, desde=DESDE):
        """¿El plan está aprobado? Como `aprobado_desde`, y si la aprobación cita un
        análisis, ese análisis tiene que estar aprobado y nombrar la HU del plan:
        lo que el análisis no contempló pide aprobación otra vez (`02·F4`)."""
        if not cls.aprobado_desde(plan_texto, desde):
            return False
        analisis = cls.analisis_citado(ruta_plan, plan_texto)
        if analisis is None:
            return True
        texto = _leer(analisis)
        hacer = _LO_QUE_SE_TIENE_QUE_HACER.search(texto)
        hu = _HU_DE_LA_FASE.search(os.path.basename(os.path.dirname(os.path.abspath(ruta_plan))))
        if not (_ANALISIS_APROBADO.search(texto) and hacer and hu):
            return False
        epica, numero = int(hu.group(1)), int(hu.group(2))
        return any(int(e) == epica and int(n) == numero for e, n in _HU_NOMBRADA.findall(hacer.group(1)))

    @staticmethod
    def filas_de_archivos(plan_texto):
        """`[(línea, primera celda)]` de la tabla de la §2.1."""
        m = _SECCION_ARCHIVOS.search(plan_texto)
        if not m:
            return []
        antes = plan_texto[:m.start(1)].count("\n")
        for _, filas in Markdown.tablas(m.group(1)):
            return [(antes + n, celdas[0]) for n, celdas in filas if celdas]
        return []

    @classmethod
    def rutas_exactas(cls, plan_texto):
        """Las rutas que declara la §2.1, tal cual están escritas."""
        return [r for _, celda in cls.filas_de_archivos(plan_texto)
                for r in re.findall(r"`([^`]+)`", celda)]

    @classmethod
    def revisar_aprobado(cls, plan_texto):
        """`CA-01` · `[(línea, motivo)]` del plan aprobado desde `DESDE`: la
        aprobación sin quién o sin fecha, y la fila que no es solo rutas exactas."""
        a = cls.aprobacion(plan_texto)
        if not (a and a[2] and a[2] >= DESDE):
            return []
        salida = []
        if not a[0] or not a[1]:
            salida.append((0, "la aprobación no dice quién la dio o cuándo: se escribe "
                              "«quién, el AAAA-MM-DD, con la versión X.Y.Z» (02·F4)"))
        for n, celda in cls.filas_de_archivos(plan_texto):
            if not _SOLO_RUTAS.fullmatch(celda.strip()):
                salida.append((n, "la fila «%s» de la §2.1 no es solo rutas exactas entre "
                                  "comillas invertidas: sin comodines, carpetas ni "
                                  "descripciones (02·F8)" % celda.strip()))
        return salida


class PlanContraLoHecho(Validador):
    """Lo tocado contra lo que el plan declara, y los criterios contra sus casos."""

    nombre = "plan"
    regla = "02·F8"
    descripcion = "lo hecho contra el plan aprobado"

    def __init__(self, proyecto, archivos=None, fase=None, desde=None, estandar=None):
        super().__init__(proyecto, archivos)
        self.fase = fase
        self.desde = desde
        self.estandar = estandar

    def _leer(self, ruta):
        return self.archivos.leer(ruta)

    def _git(self):
        return Git(self.proyecto.raiz)

    @staticmethod
    def _lista(salida):
        return sorted(set(l.strip().replace("\\", "/") for l in salida.splitlines() if l.strip()))

    # ── lo que cambió ─────────────────────────────────────────────────────

    def tocados(self, repo, desde):
        """Los archivos que cambiaron desde ese commit hasta lo que hay hoy."""
        return self._lista(Git(repo).correr("diff", "--name-only", desde))

    def preparados(self):
        """Lo que entra en el próximo commit."""
        return self._lista(self._git().correr("diff", "--cached", "--name-only"))

    def en_rango(self, rango):
        """Los archivos que cambian en un rango de commits, `desde..hasta`."""
        return self._lista(self._git().correr("diff", "--name-only", rango))

    def fases_de(self):
        """Las carpetas de fase del proyecto: las que tienen su plan de trabajo."""
        raiz = os.path.join(self.proyecto.raiz, "documentacion", "epicas")
        salida = []
        for actual, _, archivos in os.walk(raiz):
            if "plan_trabajo.md" in archivos:
                salida.append(actual)
        return sorted(salida)

    # ── la fase contra su plan ────────────────────────────────────────────

    def comparar_archivos(self, carpeta_fase, repo=None, desde=None):
        """`CA-01` · el archivo tocado que el plan no declara."""
        repo = repo or Proyecto.estandar()
        plan = os.path.join(carpeta_fase, "plan_trabajo.md")
        if not os.path.isfile(plan):
            return [Hallazgo(AVISO, carpeta_fase, 0, "no tiene `plan_trabajo.md`: no hay contra qué comparar")]
        dec = PlanDeTrabajo.declarados(self._leer(plan))
        if not dec:
            return [Hallazgo(AVISO, plan, 0,
                             "su §2.1 no declara ningún archivo, o no está escrita "
                             "como el molde: no hay contra qué comparar (02·F8)")]
        if not desde:
            return [Hallazgo(AVISO, plan, 0,
                             "no se dijo desde qué commit comparar — se compara "
                             "contra el commit del que salió la fase (02·F8)")]
        hallazgos = []
        for archivo in self.tocados(repo, desde):
            if os.path.basename(archivo) in DE_LA_FASE:
                continue
            if not PlanDeTrabajo.cuadra(archivo, dec):
                hallazgos.append(Hallazgo(
                    AVISO, archivo, 0,
                    "lo tocó la fase `%s` y su plan no lo declara — o el plan se "
                    "amplió sin escribirlo, o se editó de más (02·F8)"
                    % os.path.basename(carpeta_fase.rstrip("/\\"))))
        return hallazgos

    def comparar_casos(self, carpeta_fase):
        """`CA-02` · el criterio sin caso, y el caso sin criterio."""
        plan = os.path.join(carpeta_fase, "plan_trabajo.md")
        pruebas = os.path.join(carpeta_fase, "plan_pruebas.md")
        if not (os.path.isfile(plan) and os.path.isfile(pruebas)):
            return []
        texto_plan, texto_pruebas = self._leer(plan), self._leer(pruebas)
        criterios = set(_CRITERIO_EN_PLAN.findall(texto_plan))
        cubiertos = set(_CRITERIO_EN_PLAN.findall(texto_pruebas))
        casos = set(_CASO.findall(texto_pruebas))
        hallazgos = [Hallazgo(AVISO, pruebas, 0,
                              f"el plan declara cubrir `{ca}` y el plan de pruebas no lo nombra: "
                              f"ningún caso lo comprueba (13·DOC11)")
                     for ca in sorted(criterios - cubiertos)]
        if criterios and not casos:
            hallazgos.append(Hallazgo(AVISO, pruebas, 0,
                                      "no tiene ningún caso `CP-NNN`, y el plan declara criterios que "
                                      "alguien tiene que comprobar"))
        return hallazgos

    # ── el commit contra el plan ──────────────────────────────────────────

    def comparar_preparados(self):
        """`CA-03` · El archivo del commit que el plan no declara y ninguna regla
        autoriza. Solo cuando el commit toca una fase cuyo plan se aprobó desde
        `DESDE`: sin ese plan no hay contra qué comparar."""
        return self.comparar_archivos_contra_plan(self.preparados())

    def comparar_rango(self, rango):
        """`CA-02` · Lo mismo, sobre lo que trae un rango de commits: lo usa la
        integración continua (análisis 14 del pendiente 103, acuerdo 11)."""
        return self.comparar_archivos_contra_plan(self.en_rango(rango))

    def comparar_archivos_contra_plan(self, archivos):
        """El archivo de la lista que el plan de su fase no declara y ninguna regla autoriza."""
        from .freno import Freno
        raiz = self.proyecto.raiz
        fases = []
        for carpeta in self.fases_de():
            rel = os.path.relpath(carpeta, raiz).replace("\\", "/") + "/"
            # El hash que el post-commit anota en `estado-fase.md` no es trabajo de
            # la fase: solo él no la cuenta como tocada (análisis 16, acuerdo 2).
            if not any(a.startswith(rel) and a != rel + "estado-fase.md" for a in archivos):
                continue
            plan = os.path.join(carpeta, "plan_trabajo.md")
            texto = self._leer(plan)
            if PlanDeTrabajo.aprobado(plan, texto):
                fases.append((rel, set(PlanDeTrabajo.rutas_exactas(texto))))
        if not fases:
            return []
        autorizadas = Autorizaciones(self.archivos).reglas(raiz, self.estandar)
        # Lo que el análisis prendido manda hacer de una: la misma lista que usa
        # el freno (análisis 14 del pendiente 103, acuerdo 5). Y las de todo
        # análisis que entra en el mismo commit, prendido o aprobado: el análisis
        # y lo que mandó hacer se guardan juntos (análisis 16, acuerdo 1).
        freno = Freno(self.proyecto, self.archivos)
        de_una = freno.de_una()
        for archivo in archivos:
            if _ANALISIS_EN_EL_COMMIT.search(archivo):
                ruta = os.path.join(raiz, *archivo.split("/"))
                if os.path.isfile(ruta):
                    de_una |= freno.rutas_de_una(ruta, self.archivos)
        nombres = ", ".join("`%s`" % os.path.basename(rel.rstrip("/")) for rel, _ in fases)
        hallazgos = []
        for archivo in archivos:
            if any(archivo.startswith(rel) or archivo in dec for rel, dec in fases):
                continue                # un documento de la fase, o declarado
            if archivo in de_una or Autorizaciones.quien_autoriza(archivo, autorizadas):
                continue
            hallazgos.append(Hallazgo(FALLA, archivo, 0,
                                      "entra en el commit y ni el plan de %s lo declara ni una regla "
                                      "autoriza escribirlo (02·F8)" % nombres))
        return hallazgos

    # ── todo el proyecto ──────────────────────────────────────────────────

    def validar(self):
        """Sobre la fase pedida, o sobre todas si no se nombra ninguna."""
        from .acuerdos import Acuerdos
        raiz = self.proyecto.raiz
        carpetas = [os.path.abspath(self.fase)] if self.fase else self.fases_de()
        hallazgos = []
        for carpeta in carpetas:
            if self.desde or self.fase:
                hallazgos += self.comparar_archivos(carpeta, raiz, self.desde)
            hallazgos += self.comparar_casos(carpeta)
        # Las pruebas que el plan no declara: en la fase nombrada o en las que
        # están en curso, que son las que todavía pueden corregir su plan.
        en_curso = ([os.path.abspath(self.fase)] if self.fase
                    else [os.path.abspath(r) for r in Acuerdos(self.proyecto, self.archivos).fases_en_curso()])
        for carpeta in en_curso:
            hallazgos += self.pruebas_sin_declarar(carpeta)
        return hallazgos

    def pruebas_que_leen(self, modulos):
        """Las pruebas de Python que importan alguno de los módulos (`nombre` sin `.py`)."""
        salida = set()
        if not modulos:
            return salida
        raiz = self.proyecto.raiz
        patron = re.compile("|".join(_IMPORTA % (re.escape(m), re.escape(m)) for m in modulos), re.M)
        for actual, carpetas, archivos in os.walk(raiz):
            carpetas[:] = [c for c in carpetas if not c.startswith(".") and c not in ("node_modules", "__pycache__")]
            for n in archivos:
                if n.endswith(".py") and (n.startswith("test") or n == "pruebas.py" or "tests" in actual.split(os.sep)):
                    ruta = os.path.join(actual, n)
                    if patron.search(self._leer(ruta)):
                        salida.add(os.path.relpath(ruta, raiz).replace("\\", "/"))
        return salida

    def pruebas_sin_declarar(self, carpeta_fase):
        """Aviso: la prueba que lee un archivo que el plan cambia y que el plan no
        declara (análisis 16 del pendiente 103, acuerdo 2)."""
        plan = os.path.join(carpeta_fase, "plan_trabajo.md")
        texto = self._leer(plan)
        if not PlanDeTrabajo.aprobado(plan, texto):
            return []
        declarados = set(PlanDeTrabajo.rutas_exactas(texto))
        modulos = [os.path.basename(r)[:-3] for r in declarados
                   if r.endswith(".py") and "test" not in os.path.basename(r) and os.path.basename(r) != "pruebas.py"]
        faltan = sorted(self.pruebas_que_leen(modulos) - declarados)
        if not faltan:
            return []
        plan = Proyecto(Proyecto.estandar()).mostrar(os.path.join(carpeta_fase, "plan_trabajo.md"))
        return [Hallazgo(AVISO, plan, 0,
                         "estas pruebas leen lo que el plan cambia y el plan no las declara: "
                         + ", ".join("`%s`" % f for f in faltan))]

    def linea_resumen(self):
        return "Fases con plan: %d" % len(self.fases_de())
