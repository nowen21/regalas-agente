"""Corre las pruebas de `validadores/tests/` y **dice cuántas corrió**.

**El caso que lo hizo falta.** La carpeta tenía 67 archivos y 650 pruebas, y
ningún comando las ejecutaba: la orden documentada se caía antes de correr nada
porque faltaba el `__init__.py`, y una prueba escrita para cazar un defecto que
tuvimos seis días en rojo nunca se corrió (`S-075`).

**Cero pruebas es rojo.** `unittest discover` sobre una carpeta vacía termina
en 0: un silencio que se lee como éxito, que es el defecto, no su arreglo.

**Un solo proceso, y está medido**: cargados juntos dan las mismas fallas que
uno por uno. **Se puede pedir un subconjunto**, que es lo que hace cumplible
`02·F5`; un nombre que no existe es rojo, no una corrida vacía en verde.

No sustituye a `pruebas.py`: son dos suites y siguen separadas.
"""
import importlib.util
import io
import os
import re
import subprocess
import sys
import time
import unittest

from ..comun import AVISO, FALLA, Hallazgo, Proyecto
from ..validadores.base import Validador

CARPETA = os.path.join("validadores", "tests")

# `EP-005·HU-021` fase B · La otra batería de este repositorio. Cimiento corre
# sus pruebas con su marco, no con `unittest` a secas: se le pide por su punto
# de entrada. Estuvieron fuera de esta corrida hasta el 2026-08-31, y ese día
# una subida de versión las puso en rojo y se supo por la tarde (`S-097`).
PLATAFORMA = os.path.join("proyectos", "cimiento")

# El sello de la última corrida completa. Es estado de trabajo de esta máquina,
# no memoria del proyecto, así que no se versiona. **Va en su propia carpeta**:
# en `.tocado/` se contaba como el registro de una sesión viva.
SELLO = os.path.join("historico-chat", ".estado", "internas.txt")

ORDEN = "`python validadores/validar.py internas` (tarda ~10 min; no detiene el push)"

# Lo que el corredor de Cimiento imprime al terminar: `Ran 187 tests in 28.638s`.
_CUANTAS = re.compile(r"^Ran (\d+) tests? in ", re.MULTILINE)
_FALLAS = re.compile(r"FAILED \(([^)]*)\)")
_CUENTA = re.compile(r"(failures|errors)=(\d+)")


class PruebasDelEstandar(Validador):
    """Las pruebas de `validadores/tests/` y la batería de Cimiento, contadas aparte.

    Apunta a la raíz que se le da; quien la pide desde `validar.py` le da la
    del estándar, porque son las pruebas **del estándar**, no las del proyecto.
    """

    nombre = "internas"
    regla = "08·T5"
    descripcion = "corre las pruebas del propio estándar y dice cuántas corrió"

    def __init__(self, proyecto=None, archivos=None, solo=None):
        super().__init__(proyecto or Proyecto.estandar(), archivos)
        self.solo = solo

    @property
    def raiz(self):
        return self.proyecto.raiz

    def carpeta(self):
        return os.path.join(self.raiz, CARPETA)

    def plataforma(self):
        """La carpeta de Cimiento, exista o no."""
        return os.path.join(self.raiz, PLATAFORMA)

    @staticmethod
    def archivos_de(carpeta):
        """Los archivos de prueba, ordenados. Vacío si la carpeta no está."""
        if not os.path.isdir(carpeta):
            return []
        return sorted(n for n in os.listdir(carpeta) if n.startswith("test") and n.endswith(".py"))

    # ── Correr ────────────────────────────────────────────────────────────

    @staticmethod
    def _cargar(carpeta, nombre):
        """`(modulo, None)` o `(None, error)`. Por ruta y no por importación
        normal: así funciona esté o no la carpeta armada como paquete, y un
        archivo que no carga **se reporta** en vez de tumbar la corrida
        (`EP-004·HU-003`)."""
        ruta = os.path.join(carpeta, nombre)
        marca = "corredor_" + nombre[:-3]
        spec = importlib.util.spec_from_file_location(marca, ruta)
        if spec is None or spec.loader is None:
            return (None, "no se pudo leer como módulo de Python")
        modulo = importlib.util.module_from_spec(spec)
        sys.modules[marca] = modulo
        try:
            spec.loader.exec_module(modulo)
        except Exception as e:                                  # noqa: BLE001
            del sys.modules[marca]
            return (None, "%s: %s" % (type(e).__name__, e))
        return (modulo, None)

    @staticmethod
    def _sin_ruido(funcion):
        """Corre `funcion` con la salida de las pruebas tapada: imprimen
        bastante y enterrarían el conteo. Se tapa la salida, **no los errores**."""
        antes = sys.stdout
        sys.stdout = io.open(os.devnull, "w", encoding="utf-8")
        try:
            return funcion()
        finally:
            sys.stdout.close()
            sys.stdout = antes

    def correr(self, solo=None):
        """`(resultado, hallazgos, nombres)`. `solo` es una lista de nombres de
        archivo; sin ella van todos."""
        carpeta = self.carpeta()
        hallazgos = []
        if not os.path.isdir(carpeta) and self.hay_plataforma():
            # Desde el 2026-10-05 las pruebas del estándar viven en `core/` y las
            # corre la batería de Cimiento (análisis 1 del pendiente 116, fila 21):
            # sin la carpeta vieja no falta nada.
            return (None, [], [])
        if not os.path.isdir(carpeta):
            return (None, [Hallazgo(FALLA, carpeta, 0,
                                    "no existe la carpeta de pruebas — no se "
                                    "comprobó nada, y eso no es lo mismo que estar "
                                    "bien (08·T5)")], [])

        disponibles = self.archivos_de(carpeta)
        if solo:
            pedidos, faltantes = [], []
            for n in solo:
                n = n if n.endswith(".py") else n + ".py"
                (pedidos if n in disponibles else faltantes).append(n)
            for n in faltantes:
                hallazgos.append(Hallazgo(
                    FALLA, carpeta, 0,
                    "se pidió `%s` y no está en la carpeta — un nombre mal "
                    "escrito no puede terminar en una corrida vacía y verde" % n))
            disponibles = pedidos

        suite = unittest.TestSuite()
        cargador = unittest.TestLoader()
        corridos = []
        for nombre in disponibles:
            modulo, error = self._cargar(carpeta, nombre)
            if error:
                hallazgos.append(Hallazgo(FALLA, os.path.join(carpeta, nombre), 0,
                                          "no se pudo cargar — %s" % error))
                continue
            suite.addTests(cargador.loadTestsFromModule(modulo))
            corridos.append(nombre)

        resultado = unittest.TestResult()
        self._sin_ruido(lambda: suite.run(resultado))

        if resultado.testsRun == 0:
            hallazgos.append(Hallazgo(
                FALLA, carpeta, 0,
                "se corrieron **0 pruebas** — cero no es verde: quiere decir "
                "que no se comprobó nada (08·T5)"))

        for caso, traza in list(resultado.failures) + list(resultado.errors):
            hallazgos.append(Hallazgo(
                FALLA, os.path.join(carpeta, self._archivo_de(caso, corridos)), 0,
                "%s — %s" % (self._nombre_de(caso), self._ultima_linea(traza))))

        return (resultado, hallazgos, corridos)

    @staticmethod
    def _archivo_de(caso, corridos):
        """De qué archivo salió el caso. `?` si no se puede saber, sin inventar."""
        marca = getattr(caso, "__module__", "") or ""
        if marca.startswith("corredor_"):
            candidato = marca[len("corredor_"):] + ".py"
            if candidato in corridos:
                return candidato
        return "?"

    @staticmethod
    def _nombre_de(caso):
        try:
            return caso.id().split(".", 1)[-1]
        except Exception:                                       # noqa: BLE001
            return str(caso)

    @staticmethod
    def _ultima_linea(traza):
        lineas = [l.strip() for l in (traza or "").splitlines() if l.strip()]
        return lineas[-1][:160] if lineas else "sin detalle"

    def hay_plataforma(self):
        return os.path.isfile(os.path.join(self.plataforma(), "manage.py"))

    def python_de_la_plataforma(self):
        """El Python del entorno de Cimiento si lo tiene, que es el que trae el
        conector de su base; si no, el que corre esto."""
        for partes in (("Scripts", "python.exe"), ("bin", "python")):
            ruta = os.path.join(self.plataforma(), ".venv", *partes)
            if os.path.isfile(ruta):
                return ruta
        return sys.executable

    def correr_la_plataforma(self, etiquetas=None):
        """`(hallazgos, cuantas)` de la batería de Cimiento.

        **Se le pide por su punto de entrada**, que es como se corre de verdad:
        cargar sus archivos a mano daría un número que nadie más obtiene. **Si
        no está, se dice**: un proyecto que hereda el estándar no la tiene, y
        saltársela en silencio es lo mismo que no mirarla.
        """
        carpeta = self.plataforma()
        entrada = os.path.join(carpeta, "manage.py")
        if not os.path.isfile(entrada):
            return ([Hallazgo(AVISO, carpeta, 0,
                              "no hay plataforma en este repositorio: no se corrió "
                              "su batería. No es lo mismo que estar en verde")], 0)
        try:
            corrida = subprocess.run(
                [self.python_de_la_plataforma(), "manage.py", "test", "--verbosity", "1"] + list(etiquetas or []),
                cwd=carpeta, capture_output=True, text=True, encoding="utf-8",
                errors="replace", timeout=900)
        except (OSError, subprocess.SubprocessError) as falla:
            return ([Hallazgo(FALLA, entrada, 0,
                              "no se pudo correr la batería de la plataforma: %s" % falla)], 0)

        salida = (corrida.stdout or "") + (corrida.stderr or "")
        m = _CUANTAS.search(salida)
        cuantas = int(m.group(1)) if m else 0

        if cuantas == 0:
            return ([Hallazgo(
                FALLA, carpeta, 0,
                "la batería de la plataforma corrió **0 pruebas** — cero no es "
                "verde: quiere decir que no se comprobó nada (08·T5)")], 0)

        hallazgos = []
        roto = _FALLAS.search(salida)
        if roto or corrida.returncode != 0:
            detalle = dict((c, int(n)) for c, n in _CUENTA.findall(roto.group(1) if roto else ""))
            hallazgos.append(Hallazgo(
                FALLA, carpeta, 0,
                "la batería de la plataforma falló: %d prueba(s) · %d falla(s) · "
                "%d error(es) — se corre con `python manage.py test` desde "
                "`plataforma/`"
                % (cuantas, detalle.get("failures", 0), detalle.get("errors", 0))))
        return (hallazgos, cuantas)

    def validar(self):
        """`[Hallazgo]`, más el resumen como aviso."""
        resultado, hallazgos, corridos = self.correr(self.solo)

        # La otra batería entra solo en la corrida entera: arrastrarla a una
        # fase que pide dos archivos convertiría `02·F5` en un peaje.
        de_la_plataforma, cuantas_alla = ([], 0)
        if not self.solo:
            de_la_plataforma, cuantas_alla = self.correr_la_plataforma()
            hallazgos += de_la_plataforma
        elif resultado is None and self.hay_plataforma():
            # Sin la carpeta vieja, lo que se pide son pruebas de `core/`, por
            # su nombre de módulo: `core.validadores.tests_parecidas`.
            de_la_plataforma, cuantas_alla = self.correr_la_plataforma(self.solo)
            hallazgos += de_la_plataforma

        if resultado is None and self.hay_plataforma():
            if not self.solo:
                self.sellar(len([h for h in hallazgos if h.severidad == FALLA]))
            hallazgos.append(Hallazgo(AVISO, self.plataforma(), 0,
                                      "%d prueba(s) de Cimiento" % cuantas_alla))

        if resultado is not None:
            # Se sella la corrida entera, con su resultado; un subconjunto no:
            # diría «esto se comprobó» sobre lo que no se miró.
            if not self.solo:
                self.sellar(len([h for h in hallazgos if h.severidad == FALLA]))
            cuenta = ("%d prueba(s) en %d archivo(s) · %d falla(s) · %d error(es)"
                      % (resultado.testsRun, len(corridos),
                         len(resultado.failures), len(resultado.errors)))
            if not self.solo:
                # Las dos baterías se dicen juntas y se cuentan aparte: sumarlas
                # escondería cuál de las dos se cayó.
                cuenta += " · y %d prueba(s) de la plataforma" % cuantas_alla
            hallazgos.append(Hallazgo(AVISO, self.carpeta(), 0, cuenta))
        return hallazgos

    # ── El sello y el reclamo ─────────────────────────────────────────────

    def sellar(self, fallas=0, cuando=None):
        """Deja constancia de la última corrida entera, **y de cómo le fue**.

        Se sella toda corrida entera, no solo la limpia: sellando solo el verde,
        el reclamo decía «nunca corrieron» sobre una carpeta que había corrido
        dos veces ese día, y un aviso que manda a hacer algo que no cambia nada
        se apaga.
        """
        ruta = os.path.join(self.raiz, SELLO)
        carpeta = os.path.dirname(ruta)
        if not os.path.isdir(carpeta):
            os.makedirs(carpeta)
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write("%s\n%d\n" % (cuando or time.strftime("%Y-%m-%d %H:%M:%S"), fallas))
        return ruta

    def _sello(self):
        """`(cuando, fallas)` de la última corrida entera. `None` si no hay."""
        ruta = os.path.join(self.raiz, SELLO)
        if not os.path.isfile(ruta):
            return None
        try:
            with io.open(ruta, encoding="utf-8") as f:
                lineas = [l.strip() for l in f if l.strip()]
            # Un sello viejo trae solo la fecha: aquella versión solo sellaba el
            # verde, así que se lee como corrida limpia.
            return (lineas[0], int(lineas[1]) if len(lineas) > 1 else 0)
        except (OSError, ValueError, IndexError):
            return None

    def _ultimo_commit(self):
        """La hora del último commit. `None` si acá no hay repositorio."""
        try:
            salida = subprocess.check_output(["git", "log", "-1", "--format=%ct"],
                                             cwd=self.raiz, stderr=subprocess.DEVNULL)
            return float(salida.decode("ascii", "replace").strip())
        except (OSError, ValueError, subprocess.CalledProcessError):
            return None

    def reclamo(self):
        """Dice si hace falta correr las pruebas, y **por qué**.

        **Reclama, no corre**: las 650 tardan 9,6 minutos y el repositorio hace
        16 commits por día; un peaje así se apaga en una tarde. Esto cuesta leer
        un archivo. Los tres motivos se dicen distinto porque llevan a cosas
        distintas: nunca corrieron, la última dejó fallas, o hay trabajo que no
        vieron.
        """
        ruta = os.path.join(self.raiz, SELLO)
        sello = self._sello()
        if sello is None:
            return [Hallazgo(AVISO, ruta, 0,
                             "las pruebas del estándar nunca corrieron en esta "
                             "copia — " + ORDEN)]
        cuando, fallas = sello
        if fallas:
            return [Hallazgo(AVISO, ruta, 0,
                             "la última corrida de las pruebas del estándar "
                             "(%s) dejó **%d falla(s)** — %s" % (cuando, fallas, ORDEN))]
        commit = self._ultimo_commit()
        if commit is None or os.path.getmtime(ruta) >= commit:
            return []
        return [Hallazgo(AVISO, ruta, 0,
                         "hay commits posteriores a la última corrida de las "
                         "pruebas del estándar (%s) — %s" % (cuando, ORDEN))]
