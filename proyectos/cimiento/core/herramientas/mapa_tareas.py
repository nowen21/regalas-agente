"""`EP-005·HU-023` · El mapa de qué reglas aplican a cada tarea.

El agente no carga todas las reglas al arrancar: antes de cada tarea lee las que
le aplican. Cada regla dice a qué tareas aplica con su línea `**Aplica a:**`, y
el mapa sale de leerlas. **Lo escribe un programa y no una persona**: un mapa
escrito a mano envejece sin que nadie lo note.

Las tareas son una lista cerrada, en `base/tareas.md`; la que una regla nombra y
la lista no trae no entra al mapa, y la reporta `sin_lista()`.

Escribe además, por tarea, **las reglas completas**, en `base/reglas-por-tarea/`:
el texto de un enganche se corta en 10.000 caracteres y las reglas de una tarea
suman hasta 218.000. Los recorridos saltan esa carpeta, porque son copias.

Piezas: `MapaDeTareas` arma y escribe; `MapaDeTareasAlDia` comprueba que lo
escrito coincida con lo que dicen las reglas.
"""
import io
import os
import re

from ..comun import FALLA, Archivos, Hallazgo, Proyecto
from ..comun.consola import preparar_salida
from ..validadores.base import Validador
from ..validadores.citas import IndiceDeReglas
from ..validadores.metareglas import CuerpoDeReglas

TAREAS = "base/tareas.md"
MAPA = "base/mapa-de-tareas.md"
POR_TAREA = "base/reglas-por-tarea"

# Cuántos caracteres lleva cada archivo por tarea como máximo: el agente los
# lee con un comando, cuya salida se corta pasados 30.000 caracteres.
PARTE = 25000

# Una fila de la tabla de `base/tareas.md`: `| \`recibir-pedido\` | … |`.
_TAREA = re.compile(r"^\|\s*`([a-z][a-z-]*)`\s*\|")
_APLICA = re.compile(r"(?m)^\*\*Aplica a:\*\*\s*(.+?)\s*$")
# La marca del encabezado no es parte del nombre de la regla.
_MARCA = re.compile(r"\s*(`\[[^\]]+\]`|\*opt-in\*)\s*$")
_ENLACE = re.compile(r"(\[[^\]\n]*\]\()([^)\s]+)(\))")


class MapaDeTareas:
    """Las tareas de la lista cerrada, sus reglas y los archivos que salen de ellas."""

    def __init__(self, raiz=None, archivos=None):
        self.raiz = Proyecto(raiz or Proyecto.estandar()).raiz
        self.archivos = archivos or Archivos()

    def _ruta(self, relativa):
        return os.path.join(self.raiz, *relativa.split("/"))

    # ── La lista de tareas ────────────────────────────────────────────────

    def _filas(self):
        """`[(tarea, [celdas])]` de la tabla de tareas. La de acciones tiene dos
        columnas y no entra: la de tareas tiene cuatro."""
        salida = []
        for linea in self.archivos.leer(self._ruta(TAREAS)).splitlines():
            m = _TAREA.match(linea.strip())
            if m:
                celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
                if len(celdas) >= 4:
                    salida.append((m.group(1), celdas))
        return salida

    def tareas(self):
        """Los nombres de la lista cerrada, en su orden."""
        return [t for t, _ in self._filas()]

    def palabras_clave(self):
        """`{tarea: {palabras clave}}` de la tercera columna (`01·C28`). La que dice
        `siempre` va con el conjunto vacío: no la pide ninguna palabra."""
        salida = {}
        for tarea, celdas in self._filas():
            texto = celdas[2] if len(celdas) > 2 else ""
            salida[tarea] = {p.strip().lower() for p in texto.split(",")
                             if p.strip() and p.strip().lower() != "siempre"}
        return salida

    def siempre(self):
        """Las tareas que van en todo mensaje: su tercera columna dice `siempre`."""
        return [t for t, celdas in self._filas() if len(celdas) > 2 and celdas[2].strip().lower() == "siempre"]

    def acciones(self):
        """`{tarea: [(clase, [valores])]}` de la cuarta columna: `escribe en
        base/ plantillas/` da `("escribe en", ["base/", "plantillas/"])`."""
        salida = {}
        for tarea, celdas in self._filas():
            specs = []
            for crudo in (celdas[3] if len(celdas) > 3 else "").split(";"):
                partes = crudo.strip().strip("`").split()
                if not partes:
                    continue
                if partes[:2] == ["escribe", "en"]:
                    specs.append(("escribe en", partes[2:]))
                elif partes[0] == "escribe":
                    specs.append(("escribe", partes[1:]))
                else:
                    specs.append((partes[0], partes[1:]))
            salida[tarea] = specs
        return salida

    # ── Las reglas de cada tarea ──────────────────────────────────────────

    def reglas(self):
        """Todas las reglas de `base/`, derogadas incluidas."""
        return CuerpoDeReglas.leer(self.raiz, self.archivos)

    @staticmethod
    def declaradas(regla):
        """Las tareas que la regla nombra en su línea `**Aplica a:**`."""
        m = _APLICA.search(regla.texto)
        if not m:
            return []
        return [t.strip().strip("`") for t in m.group(1).split(",") if t.strip()]

    def reglas_por_tarea(self):
        """`{tarea: [regla]}` de las reglas vigentes, en el orden de `base/`."""
        salida = {t: [] for t in self.tareas()}
        for regla in self.reglas():
            if regla.derogada:
                continue
            for t in self.declaradas(regla):
                if t in salida:
                    salida[t].append(regla)
        return salida

    def sin_lista(self):
        """Las parejas `(regla, tarea)` donde la tarea no está en la lista cerrada."""
        lista = set(self.tareas())
        return [(r, t) for r in self.reglas() if not r.derogada
                for t in self.declaradas(r) if t not in lista]

    # ── El mapa ───────────────────────────────────────────────────────────

    @staticmethod
    def _enlace(regla, desde):
        """La ruta a la regla, relativa a `desde`, con su ancla si no ocupa su archivo entero."""
        ruta = os.path.relpath(regla.archivo, desde).replace(os.sep, "/")
        if regla.nivel == 1:
            return ruta
        return ruta + "#" + IndiceDeReglas.ancla("%s · %s" % (regla.id, regla.titulo))

    @staticmethod
    def _nombre(regla):
        """El título sin la marca y sin raya ni punto medio, que en una lista son prosa."""
        nombre = _MARCA.sub("", regla.titulo)
        nombre = re.sub(r"\s*[—·]\s*$", "", nombre)   # la que precedía a la marca
        return re.sub(r"\s+[—·]\s+", ", ", nombre)

    def armar(self):
        """El texto del mapa: cada tarea de la lista con las reglas que la declaran."""
        por_tarea = self.reglas_por_tarea()
        desde = os.path.dirname(self._ruta(MAPA))
        partes = [
            "# Mapa de tareas",
            "",
            "Qué reglas se leen antes de cada tarea. Lo escribe "
            "`validadores/mapa_tareas.py` leyendo la línea `**Aplica a:**` de cada "
            "regla: no se edita a mano. Para cambiarlo se cambia la regla y se vuelve "
            "a correr el programa.",
            "",
            "Las tareas son las de [base/tareas.md](tareas.md). El texto completo de "
            "las reglas de cada una está en "
            "[base/reglas-por-tarea/](reglas-por-tarea/README.md).",
        ]
        for t in self.tareas():
            partes += ["", "## `%s`" % t, ""]
            if not por_tarea[t]:
                partes.append("Ninguna regla la declara todavía.")
                continue
            for regla in por_tarea[t]:
                # Sin `·` entre identificador y nombre: en una lista es prosa (`00·ID8`).
                partes.append("- [`%s·%s`](%s): %s" % (regla.capitulo, regla.id,
                                                       self._enlace(regla, desde), self._nombre(regla)))
        return "\n".join(partes) + "\n"

    # ── Las reglas completas de cada tarea ────────────────────────────────

    @staticmethod
    def _ejemplo(regla):
        """El bloque `INCORRECTO / CORRECTO` de la regla, o `""`."""
        dentro, bloque = False, []
        for linea in (regla.texto or "").splitlines():
            if linea.startswith("```"):
                if dentro:
                    break
                dentro = True
                continue
            if dentro:
                bloque.append(linea)
        texto = "\n".join(bloque).strip()
        return texto if "INCORRECTO" in texto else ""

    @classmethod
    def cuerpo(cls, regla):
        """Lo que se entrega de una regla: encabezado, cuerpo y ejemplo, sin el sello."""
        partes = [regla.encabezado.strip()] + [t for _, t in regla.cuerpo]
        ejemplo = cls._ejemplo(regla)
        if ejemplo:
            partes.append("```\n" + ejemplo + "\n```")
        return "\n".join(p for p in partes if p).strip()

    @staticmethod
    def _reubicar(texto, origen, destino):
        """Los enlaces relativos de `texto`, que resolvían desde `origen`, vistos
        desde `destino`: la regla se copia a otra carpeta y sin esto quedarían rotos."""
        def cambio(m):
            blanco = m.group(2)
            if re.match(r"^[a-z]+:", blanco) or blanco.startswith("«"):
                return m.group(0)
            ruta, _, ancla = blanco.partition("#")
            absoluta = os.path.normpath(os.path.join(os.path.dirname(origen), ruta)) if ruta else origen
            nueva = os.path.relpath(absoluta, destino).replace(os.sep, "/")
            return m.group(1) + nueva + ("#" + ancla if ancla else "") + m.group(3)
        return _ENLACE.sub(cambio, texto)

    @classmethod
    def _pieza(cls, regla, carpeta):
        """Una regla completa, lista para el archivo de su tarea, con su encabezado en nivel 2."""
        lineas = cls._reubicar(cls.cuerpo(regla), regla.archivo, carpeta).splitlines()
        lineas[0] = "## " + lineas[0].lstrip("#").strip()
        return "\n".join(lineas) + "\n\nFuente: [%s·%s](%s)\n" % (regla.capitulo, regla.id,
                                                                  cls._enlace(regla, carpeta))

    @staticmethod
    def nombres_de(tarea, cuantas):
        """`tarea.md`, o `tarea-1.md`, `tarea-2.md`… si no cabe en uno."""
        if cuantas <= 1:
            return ["%s.md" % tarea]
        return ["%s-%d.md" % (tarea, i) for i in range(1, cuantas + 1)]

    def armar_por_tarea(self):
        """`{nombre de archivo: texto}` de `reglas-por-tarea/`, índice incluido."""
        carpeta = self._ruta(POR_TAREA)
        salida, filas = {}, []
        for tarea, reglas in self.reglas_por_tarea().items():
            grupos, actual, largo = [], [], 0
            for p in [self._pieza(r, carpeta) for r in reglas]:
                if actual and largo + len(p) > PARTE:
                    grupos.append(actual)
                    actual, largo = [], 0
                actual.append(p)
                largo += len(p) + 1
            if actual or not grupos:
                grupos.append(actual)
            nombres = self.nombres_de(tarea, len(grupos))
            for i, (nombre, grupo) in enumerate(zip(nombres, grupos), start=1):
                parte = ", parte %d de %d" % (i, len(grupos)) if len(grupos) > 1 else ""
                cabeza = ["# Reglas de la tarea `%s`%s" % (tarea, parte), "",
                          "Lo escribe `validadores/mapa_tareas.py` desde las reglas de "
                          "`base/`: no se edita a mano. Son las reglas que "
                          "[base/mapa-de-tareas.md](../mapa-de-tareas.md) pone "
                          "bajo esta tarea, completas. Las que llevan *opt-in* rigen "
                          "solo si el proyecto encendió su capítulo en el punto 5.1 "
                          "de su `CLAUDE.md`.", ""]
                salida[nombre] = "\n".join(cabeza) + "\n" + "\n".join(grupo or ["Ninguna regla la declara todavía.\n"])
            filas.append((tarea, len(reglas), nombres))
        indice = ["# Las reglas de cada tarea", "",
                  "El agente lee el archivo de una tarea antes de hacerla, y lo lee "
                  "con la herramienta de lectura: así le llega entero. Lo escribe "
                  "`validadores/mapa_tareas.py`; no se edita a mano.", "",
                  "| Tarea | Reglas | Archivos |", "|---|---:|---|"]
        for tarea, n, nombres in filas:
            indice.append("| `%s` | %d | " % (tarea, n) + ", ".join("[%s](%s)" % (x, x) for x in nombres) + " |")
        salida["README.md"] = "\n".join(indice) + "\n"
        return salida

    def archivos_de(self, tarea):
        """Las rutas absolutas de los archivos de una tarea, como están escritos."""
        carpeta = self._ruta(POR_TAREA)
        if os.path.isfile(os.path.join(carpeta, "%s.md" % tarea)):
            return [os.path.join(carpeta, "%s.md" % tarea)]
        salida, i = [], 1
        while os.path.isfile(os.path.join(carpeta, "%s-%d.md" % (tarea, i))):
            salida.append(os.path.join(carpeta, "%s-%d.md" % (tarea, i)))
            i += 1
        return salida

    def escribir(self):
        """Escribe el mapa y los archivos por tarea, y borra los que sobran.
        Devuelve la ruta del mapa."""
        ruta = self._ruta(MAPA)
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(self.armar())
        carpeta = self._ruta(POR_TAREA)
        os.makedirs(carpeta, exist_ok=True)
        esperados = self.armar_por_tarea()
        for nombre in os.listdir(carpeta):
            if nombre.endswith(".md") and nombre not in esperados:
                os.remove(os.path.join(carpeta, nombre))
        for nombre, texto in esperados.items():
            with io.open(os.path.join(carpeta, nombre), "w", encoding="utf-8", newline="\n") as f:
                f.write(texto)
        return ruta


class MapaDeTareasAlDia(Validador):
    """`CA-04` y `CA-10` · Lo que no cuadra entre las reglas, la lista y lo escrito.

    Una regla vigente sin tareas (el agente no la encuentra), una tarea que la
    lista no trae (la regla queda fuera sin que se note), y un mapa o un archivo
    por tarea distinto del que el programa escribiría hoy. Donde no hay lista no
    hay nada que reportar: un proyecto no tiene reglas propias en `base/`.
    """

    nombre = "tareas"
    regla = "01·C28"
    descripcion = "toda regla dice a qué tareas aplica y el mapa está al día"

    def validar(self):
        mapa = MapaDeTareas(self.proyecto.raiz, self.archivos)
        if not os.path.isfile(self.proyecto.ruta(TAREAS)):
            return []
        hallazgos = []
        for regla in mapa.reglas():
            if regla.derogada or mapa.declaradas(regla):
                continue
            hallazgos.append(Hallazgo(
                FALLA, regla.archivo, regla.linea,
                "`%s·%s` no dice a qué tareas aplica: le falta su línea **Aplica a:**, y el agente no "
                "la encuentra en el mapa" % (regla.capitulo, regla.id)))
        for regla, t in mapa.sin_lista():
            hallazgos.append(Hallazgo(FALLA, regla.archivo, regla.linea,
                                      "`%s·%s` nombra la tarea `%s`, que no está en %s"
                                      % (regla.capitulo, regla.id, t, TAREAS)))
        ruta = self.proyecto.ruta(MAPA)
        actual = self.archivos.leer(ruta) if os.path.isfile(ruta) else ""
        if actual.replace("\r\n", "\n") != mapa.armar():
            hallazgos.append(Hallazgo(
                FALLA, ruta, 0,
                "el mapa no coincide con lo que dicen las reglas: se cambió una línea **Aplica a:** y "
                "no se volvió a correr `python validadores/mapa_tareas.py`"))
        carpeta = self.proyecto.ruta(POR_TAREA)
        esperados = mapa.armar_por_tarea()
        for nombre, texto in esperados.items():
            ruta = os.path.join(carpeta, nombre)
            actual = self.archivos.leer(ruta) if os.path.isfile(ruta) else None
            if actual is None or actual.replace("\r\n", "\n") != texto:
                hallazgos.append(Hallazgo(
                    FALLA, ruta, 0,
                    "las reglas de esta tarea no coinciden con las de `base/`: se cambió una regla y no "
                    "se volvió a correr `python validadores/mapa_tareas.py`"))
        if os.path.isdir(carpeta):
            for nombre in sorted(os.listdir(carpeta)):
                if nombre.endswith(".md") and nombre not in esperados:
                    hallazgos.append(Hallazgo(FALLA, os.path.join(carpeta, nombre), 0,
                                              "sobra: ninguna tarea lo produce hoy; correr "
                                              "`python validadores/mapa_tareas.py`"))
        return hallazgos


def main(argv=None):
    """Escribe el mapa y las reglas por tarea, y avisa de las tareas fuera de la lista."""
    preparar_salida()
    mapa = MapaDeTareas(Proyecto.desde_argumentos(list(argv or []), Proyecto.estandar()).raiz)
    ruta = mapa.escribir()
    for regla, t in mapa.sin_lista():
        print("[AVISO] %s·%s nombra `%s`, que no está en %s" % (regla.capitulo, regla.id, t, TAREAS))
    print("Mapa escrito en %s, y las reglas por tarea en %s/" % (Proyecto(Proyecto.estandar()).mostrar(ruta), POR_TAREA))
    return 0
