"""Cierra y reabre una fase (`EP-025·HU-016`).

**Lo que se repite es una funcionalidad de Cimiento, no un guion** (análisis 2
del pendiente 119, acuerdo 6). Las fases de las HU-006 a HU-010 se cerraron con
cinco guiones casi iguales: cambiaban solo los datos de cada fase, y esos datos
ya estaban en su plan y en su plan de pruebas.

**Cerrar va en dos pasadas.** La primera escribe el estado, el resultado y la
funcionalidad con lo que sale de los planes, y deja `«…»` en lo que un programa
no sabe: qué salió, qué se decidió. Mientras quede una marca, no cierra: dice
dónde falta. La segunda, ya sin marcas, cierra: la matriz del plan de pruebas,
el cierre del plan, la fila de la fase en la HU y el estado de la HU y de la
épica. **Solo se escribe un documento que sigue en plantilla**: lo escrito a
mano no se pisa.

**Toda acción trae su contraria** (análisis 3, acuerdo 2): `reabrir` devuelve la
fase a la estación 8 y suma un ciclo nuevo por llenar en el resultado, así que no
se vuelve a cerrar sin decir qué pasó.

Sin `escribir`, simula: calcula todo en memoria y no toca el disco.
"""
import datetime
import io
import os
import re
import subprocess

from ..comun import Proyecto

MARCA = "«…»"
# Lo que la primera pasada no puede saber todavía y la segunda llena sola.
AL_CERRAR = "«se llena al cerrar»"

_FASE = re.compile(r"^([A-Z]{1,3})-EP-\d+-HU-\d+-")
_HU = re.compile(r"^HU-(\d+)-")
_ESTACION = re.compile(r"(?m)^\*\*Estación actual:\*\*.*$")


def _leer(ruta):
    if not os.path.isfile(ruta):
        return ""
    with io.open(ruta, encoding="utf-8") as f:
        return f.read()


def _en_plantilla(texto):
    """Un documento de la fase sigue en plantilla si su título conserva un marcador."""
    primera = texto.split("\n", 1)[0]
    return not texto.strip() or "«" in primera


def _ultima_celda(linea, valor):
    """`| a | b | viejo |` pasa a `| a | b | valor |`."""
    return linea.rstrip().rstrip("|").rsplit("|", 1)[0] + "| %s |" % valor


def _celdas(linea):
    return [c.strip() for c in linea.strip().strip("|").split("|")]


def _seccion(texto, encabezado):
    """`(inicio, fin)` del cuerpo de la sección que abre `encabezado`, hasta la siguiente `## `."""
    m = re.search(r"(?m)^" + re.escape(encabezado) + r".*$", texto)
    if not m:
        return None
    fin = re.compile(r"(?m)^## ").search(texto, m.end())
    return m.end(), fin.start() if fin else len(texto)


def _agregar_a_tabla(texto, encabezado, fila):
    """Agrega `fila` al final de la primera tabla de la sección `encabezado`."""
    tramo = _seccion(texto, encabezado)
    if not tramo:
        raise ValueError("no está la sección «%s»" % encabezado)
    tabla = re.compile(r"(?m)^\|.*\n(?:\|.*\n?)*").search(texto, tramo[0], tramo[1])
    if not tabla:
        raise ValueError("no hay tabla en la sección «%s»" % encabezado)
    bloque = texto[tabla.start():tabla.end()].rstrip("\n")
    resto = texto[tabla.end():]
    return texto[:tabla.start()] + bloque + "\n" + fila + "\n" + ("" if resto.startswith("\n") or not resto
                                                                  else "\n") + resto


class Fase:
    """Una fase de la cadena, leída de sus documentos. Sin `escribir`, simula."""

    def __init__(self, carpeta, hoy=None):
        self.carpeta = os.path.abspath(carpeta)
        self.nombre = os.path.basename(self.carpeta)
        self.carpeta_hu = os.path.dirname(self.carpeta)
        self.hu_dir = os.path.basename(self.carpeta_hu)
        self.carpeta_epica = os.path.dirname(self.carpeta_hu)
        self.epica_md = os.path.join(self.carpeta_epica, "epica.md")
        if not (os.path.isdir(self.carpeta) and _FASE.match(self.nombre) and _HU.match(self.hu_dir)
                and os.path.isfile(self.ruta("plan_trabajo.md")) and os.path.isfile(self.ruta("plan_pruebas.md"))
                and os.path.isfile(self.epica_md)):
            raise ValueError("no es una fase de la cadena: %s" % carpeta)
        self.hu_id = "HU-" + _HU.match(self.hu_dir).group(1)
        self.hu_md = os.path.join(self.carpeta_hu, self.hu_dir + ".md")
        self.hoy = (hoy or datetime.date.today()).isoformat()
        self._textos = {}

    # ── leer y escribir en memoria ────────────────────────────────────────

    def ruta(self, archivo):
        return os.path.join(self.carpeta, archivo)

    def leer(self, ruta):
        return self._textos[ruta] if ruta in self._textos else _leer(ruta)

    def poner(self, ruta, texto):
        if texto != self.leer(ruta):
            self._textos[ruta] = texto

    def guardar(self, escribir):
        """Escribe lo cambiado y devuelve las rutas. Sin `escribir`, solo las nombra."""
        if escribir:
            for ruta, texto in self._textos.items():
                with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
                    f.write(texto)
        return sorted(self._textos)

    # ── lo que dicen los planes ───────────────────────────────────────────

    def plan(self):
        t = self.leer(self.ruta("plan_trabajo.md"))
        if _en_plantilla(t):
            raise ValueError("el plan de trabajo de %s sigue en plantilla" % self.nombre)
        modulo = re.search(r"(?m)^\| \*\*Módulo\*\* \| (.+?) \|$", t)
        aprobacion = re.search(r"(?m)^\*\*Aprobación\*\*[^:]*:\s*(.+)$", t)
        donde = {}
        for bloque in re.split(r"(?m)^### ", t):
            m = re.match(r"(CA-\d+) · ", bloque)
            if m:
                for celda in re.findall(r"(?m)^\| T-\d+ \| [^|]+ \| ([^|]+) \|", bloque):
                    for parte in celda.split(", "):
                        if parte.strip() not in donde.setdefault(m.group(1), []):
                            donde[m.group(1)].append(parte.strip())
        return {
            "cas": re.findall(r"(?m)^\| (CA-\d+) · (.+?) \| [☐☑] \|$", t),
            "tareas": sorted(set(re.findall(r"(?m)^\| (T-\d+) \|", t))),
            "modulo": modulo.group(1) if modulo else MARCA,
            "aprobacion": aprobacion.group(1).strip() if aprobacion else MARCA,
            "tipos": dict(re.findall(r"(?m)^\| (CA-\d+) \| [^|]+ \| ([^|]+?) \| [^|]+ \|$", t)),
            "donde": donde,
        }

    def casos(self):
        """`[(CA, CP, tipo, prioridad)]` de la matriz del plan de pruebas."""
        t = self.leer(self.ruta("plan_pruebas.md"))
        return [(ca, cp, tipo.strip(), prioridad.strip()) for ca, cp, tipo, prioridad in re.findall(
            r"(?m)^\| HU-\d+ \| (CA-\d+) \| (CP-\d+) \| ([^|]+) \| ([^|]+) \| [^|]+ \| [☐☑] \|$", t)]

    @staticmethod
    def version():
        return _leer(os.path.join(Proyecto.estandar(), "VERSION")).strip() or MARCA

    # ── la primera pasada: lo que sale de los planes ──────────────────────

    def _cabecera(self, titulo, modulo):
        sufijo = " (módulo %s)" % modulo.split(", ")[0] if modulo else ""
        return "# %s · Fase `%s`%s   ·   `[CAPA 3]`\n" % (titulo, self.nombre, sufijo)

    def _enlace_hu(self):
        return "[%s](../%s.md)" % (self.hu_id, self.hu_dir)

    def texto_estado(self, plan):
        filas = [
            (1, "Explorador · análisis", "contexto entendido", "☑ " + plan["aprobacion"].split(", el ")[0]),
            (2, "Proponente · alcance", "👤 alcance aprobado", "☑ Con el análisis de origen"),
            (3, "Escritor de épica", "👤 épica aprobada", "☑ " + os.path.basename(self.carpeta_epica)[:6]),
            (4, "Escritor de historia", "👤 HUs aprobadas", "☑ %s, aprobada con el análisis" % self.hu_id),
            (5, "Escritor de especificación", "👤 especificación aprobada", "N/A: la especificación son los CA"),
            (6, "Diseñador", "diseño coherente", "☑"),
            (7, "Planificador de tareas", "👤 plan + pruebas aprobados", "☑ Aprobados por el análisis"),
            (8, "Implementador", "implementado + pruebas verdes", "☑ Las %d tareas" % len(plan["tareas"])),
            (9, "Verificador", "trazabilidad sin faltantes", "☑ Sin fallas"),
            (10, "Crítico", "sin hallazgos graves", "☑ Hallazgos: los del cierre del plan"),
            (11, "Cierre documental + señales", "docs y señales al día", "☑ Resultado, funcionalidad, HU y épica"),
            (12, "Commit", "👤 autorizado", "☐"),
            (13, "Publicación / despliegue", "👤 autorizado", "☐"),
        ]
        tabla = "\n".join("| %d | %s | %s | %s |" % f for f in filas)
        return (self._cabecera("Estado de fase", plan["modulo"]) + "\n"
                "## 0. Identificación\n\n| Campo | Valor |\n|---|---|\n"
                "| **Fase** (identificador · `02·F12.6`) | `%s` |\n| **Módulo** | %s |\n"
                "| **Planteamiento / Épica / HU** | [%s](../../epica.md) · %s |\n"
                "| **Última actualización** | %s |\n\n"
                "## 1. En qué estación va\n\n**Estación actual:** 12, commit. **Última puerta pasada:** 11.\n\n"
                "| # | Estación | Puerta | Estado |\n|---|---|---|---|\n%s\n\n"
                "## 1.2 Avance de las tareas del plan\n\n**Hechas:** %d de %d. **Bloqueadas:** ninguna.\n\n"
                "## 1.1 Veredicto de las pruebas\n\n| Campo | Valor |\n|---|---|\n"
                "| **Concepto** | %s |\n| **CA cumplidos** | %s |\n| **Defectos abiertos aceptados** | %s |\n"
                "| **Fuente** | `resultado_pruebas.md` |\n\n"
                "## 2. Decisiones y señales generadas  ·  `13·DOC5`\n\n"
                "| Decisión / aprendizaje | Señal registrada (id/enlace) |\n|---|---|\n| %s | %s |\n\n"
                "## 3. Pendiente / preguntas abiertas\n\nNinguna.\n\n## 4. Si se bloqueó\n\nNo aplica.\n"
                % (self.nombre, plan["modulo"], os.path.basename(self.carpeta_epica)[:6], self._enlace_hu(),
                   self.hoy, tabla, len(plan["tareas"]), len(plan["tareas"]), AL_CERRAR, AL_CERRAR, MARCA,
                   MARCA, MARCA))

    def texto_resultado(self, plan, casos, corrida):
        """`corrida` es el resumen de `--pruebas` si pasaron; sin ella, lo que pasó queda por decir."""
        n = len(casos)
        paso = "Aprobado" if corrida else MARCA
        filas = "\n".join("| %s | %s | %s | %s | %s | %s | EV-01 | Ninguno |" % (cp, ca, prioridad, MARCA, MARCA, paso)
                          for ca, cp, _tipo, prioridad in casos)
        por_ca = {}
        for ca, cp, _tipo, _prioridad in casos:
            por_ca.setdefault(ca, []).append(cp)
        veredictos = "\n".join("| %s | %s | %s | %s |" % (ca, ", ".join(cps), paso, "Sí" if corrida else MARCA)
                               for ca, cps in por_ca.items())
        resumen = "| 1 | %d | %d | %d | 0 | 0 | 0 |" % (n, n, n) if corrida else "| 1 | %d | %s | %s | %s | %s | %s |" % (
            n, MARCA, MARCA, MARCA, MARCA, MARCA)
        manual = ("| 1 | Las pruebas de la fase | `%s` | %s |" % corrida if corrida
                  else "| 1 | %s | %s | %s |" % (MARCA, MARCA, MARCA))
        return ("# Resultado de Pruebas · Fase `%s`   ·   `[CAPA 3]`\n\n"
                "**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta "
                "fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea "
                "base que se aprobó.\n\n"
                "## 0. Identificación\n\n| Campo | Valor |\n|---|---|\n| **Fase** (`02·F12.6`) | `%s` |\n"
                "| **HU** | %s |\n| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |\n"
                "| **Ciclo** | 1 |\n| **Fecha de ejecución** | %s |\n| **Ejecutado por** | Claude |\n"
                "| **Ambiente y versión** | %s; versión %s |\n\n"
                "## 1. Resumen de la ejecución\n\n"
                "| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |\n"
                "|---|---:|---:|---:|---:|---:|---:|\n%s\n\n**Casos no ejecutados y por qué:** %s\n\n"
                "## 2. Ejecución caso por caso\n\n"
                "| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |\n"
                "|---|---|---|---|---|---|---|---|\n%s\n\n"
                "**Correspondencia con el plan:** %d casos en el plan, %d acá.\n\n"
                "**Qué salió distinto de lo esperado:** %s\n\n"
                "## 3. Verificaciones manuales  ·  `08·T4`\n\n| # | Qué se verificó | Cómo | Resultado |\n"
                "|---|---|---|---|\n%s\n\n## 4. Defectos encontrados\n\n%s\n\n"
                "## 5. Veredicto por criterio de aceptación y requisito no funcional\n\n"
                "| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |\n|---|---|---|---|\n%s\n\n"
                "**Los que no cumplen:** %s\n\n## 5.1 Lo que el plan exigía\n\n"
                "| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |\n|---|---|---|---|---|\n"
                "| Cobertura de exigencias | Plan §12.1 | 100%% | %d de %d | Sí |\n"
                "| Casos ejecutados | Plan §12.1 | 100%% | %s | %s |\n\n"
                "## 6. Veredicto de la fase\n\n**Concepto:** %s.\n\n**Justificación:** %s\n\n"
                "## 7. Evidencias\n\n| ID | Tipo | Dónde está |\n|---|---|---|\n| EV-01 | Programa y pruebas | %s |\n\n"
                "## 8. Ciclos anteriores\n\n| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |\n"
                "|---|---|---:|---:|---|\n| 1 | %s | %s | %s | Primera ejecución |\n"
                % (self.nombre, self.nombre, self._enlace_hu(), self.hoy, MARCA, self.version(), resumen,
                   "ninguno." if corrida else MARCA, filas, n, n, MARCA, manual, MARCA, veredictos,
                   "ninguno." if corrida else MARCA, len(por_ca), len(por_ca),
                   "%d de %d" % (n, n) if corrida else MARCA, "Sí" if corrida else MARCA,
                   "Cumple" if corrida else MARCA, MARCA, MARCA, self.hoy,
                   n if corrida else MARCA, 0 if corrida else MARCA))

    def texto_funcionalidad(self, plan, casos):
        cp_de = {}
        for ca, cp, _tipo, _prioridad in casos:
            cp_de.setdefault(ca, []).append(cp)
        filas = "\n".join("| %s | %s | %s | ✅ | %s |" % (
            ca, plan["tipos"].get(ca, MARCA), ", ".join(plan["donde"].get(ca, [])) or MARCA,
            ", ".join(cp_de.get(ca, [])) or MARCA) for ca, _nombre in plan["cas"])
        cas = [ca for ca, _nombre in plan["cas"]]
        cubiertas = "%s (%s)" % (self.hu_id, "%s a %s" % (cas[0], cas[-1]) if len(cas) > 1 else "".join(cas))
        return (self._cabecera("Funcionalidad implementada", plan["modulo"]) + "\n"
                "## 0. Identificación\n\n| Campo | Valor |\n|---|---|\n"
                "| **Fase** (identificador · `02·F12.6`) | `%s` |\n| **Módulo** | %s |\n"
                "| **Especificación del módulo** | Los CA de la %s |\n"
                "| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |\n"
                "| **HU / CA cubiertas** | %s |\n| **Fecha de cierre** | %s |\n"
                "| **Versión del estándar al cerrar** | %s |\n| **Commit** | Por hacer |\n\n"
                "## 1. Qué se implementó, resumen\n\n%s\n\n"
                "## 2. Trazabilidad  ·  `13·DOC11`\n\n### 2.1 Especificación → implementación\n\n"
                "| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |\n"
                "|---|---|---|---|---|\n%s\n\n**Faltantes / diferimientos:** %s\n\n"
                "### 2.2 Plan de trabajo → ejecución\n\nLas %d tareas del plan quedaron hechas.\n\n"
                "**Tareas que no se hicieron:** %s\n\n**Archivos tocados que el plan no declaraba** (`02·F8`): %s\n\n"
                "**Esfuerzo real contra estimado:** no se midió.\n\n"
                "## 3. Qué se probó  ·  `08` / `02·F5`\n\n| Campo | Valor |\n|---|---|\n"
                "| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |\n| **Veredicto** | %s |\n\n"
                "## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`\n\n%s\n\n"
                "## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`\n\n"
                "| Decisión | Por qué (y qué se descartó) | Señal registrada |\n|---|---|---|\n| %s | %s | %s |\n\n"
                "## 6. Deuda técnica y pendientes generados\n\n%s\n\n"
                "## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`\n\n%s\n\n"
                "## 8. Despliegue, si aplica  ·  `13·DOC4`\n\n%s\n"
                % (self.nombre, plan["modulo"], self._enlace_hu(), cubiertas, self.hoy, self.version(), MARCA, filas,
                   MARCA, len(plan["tareas"]), MARCA, MARCA, AL_CERRAR, MARCA, MARCA, MARCA, MARCA, MARCA, MARCA,
                   MARCA))

    def faltan(self):
        """`[(archivo, línea)]` donde queda un `«…»` en los documentos de cierre."""
        salida = []
        for archivo in ("estado-fase.md", "resultado_pruebas.md", "funcionalidad_implementada.md"):
            for n, linea in enumerate(self.leer(self.ruta(archivo)).split("\n"), 1):
                if MARCA in linea:
                    salida.append((archivo, n))
        return salida

    # ── la segunda pasada: cerrar ─────────────────────────────────────────

    def _veredicto(self):
        r = self.leer(self.ruta("resultado_pruebas.md"))
        concepto = re.search(r"(?m)^\*\*Concepto:\*\*\s*([^.\n]+)", r)
        tramo = _seccion(r, "## 5. ") or (0, 0)
        filas = re.findall(r"(?m)^\| (CA-\d+) \|.*\| (Sí|No) \|$", r[tramo[0]:tramo[1]])
        return (concepto.group(1).strip() if concepto else ""), sum(1 for _ca, si in filas if si == "Sí"), len(filas)

    def _marcar_cerrada(self, plan, hallazgos):
        concepto, cumplidos, total = self._veredicto()
        if not concepto.startswith("Cumple"):
            raise ValueError("el resultado dice «%s»: una fase que no cumple no se cierra" % (concepto or "sin concepto"))
        # Estado: veredicto, y las estaciones 8 a 11 si una reapertura las desmarcó.
        ruta = self.ruta("estado-fase.md")
        t = self.leer(ruta)
        t = re.sub(r"(?m)^(\| \*\*Concepto\*\* \| ).*$", r"\g<1>%s |" % concepto, t)
        t = re.sub(r"(?m)^(\| \*\*CA cumplidos\*\* \| ).*$", r"\g<1>%d de %d |" % (cumplidos, total), t)
        t = _ESTACION.sub("**Estación actual:** 12, commit. **Última puerta pasada:** 11.", t)
        por_defecto = {8: "☑ Las %d tareas" % len(plan["tareas"]), 9: "☑ Sin fallas",
                       10: "☑ Hallazgos: los del cierre del plan", 11: "☑ Resultado, funcionalidad, HU y épica"}
        lineas = t.split("\n")
        for i, linea in enumerate(lineas):
            m = re.match(r"^\| (\d+) \| ", linea)
            if m and int(m.group(1)) in por_defecto and _celdas(linea)[-1] == "☐":
                lineas[i] = _ultima_celda(linea, por_defecto[int(m.group(1))])
        self.poner(ruta, "\n".join(lineas))
        ruta = self.ruta("funcionalidad_implementada.md")
        self.poner(ruta, self.leer(ruta).replace(AL_CERRAR, concepto))
        # Plan de pruebas: la matriz.
        ruta = self.ruta("plan_pruebas.md")
        self.poner(ruta, re.sub(r"(?m)^(\| HU-\d+ \| CA-\d+ \| CP-\d+ \|.*\| )☐( \|)$", r"\g<1>☑\2", self.leer(ruta)))
        # Plan de trabajo: los CA y el cierre.
        ruta = self.ruta("plan_trabajo.md")
        t = re.sub(r"(?m)^(\| CA-\d+ · .+ \| )☐( \|)$", r"\g<1>☑\2", self.leer(ruta))
        tramo = _seccion(t, "## 13.")
        if tramo:
            cuerpo = t[tramo[0]:tramo[1]]
            if "«" in cuerpo:
                cuerpo = ("\n\nLas %d tareas quedaron hechas el %s, con la versión %s. Detalle en "
                          "[`funcionalidad_implementada.md`](funcionalidad_implementada.md).\n\n"
                          "**Hallazgos al ejecutar:** %s.\n" % (len(plan["tareas"]), self.hoy, self.version(), hallazgos))
            elif cuerpo.strip().split("\n")[-1].startswith("**Reabierta**"):
                cuerpo = cuerpo.rstrip("\n") + "\n\nCerrada otra vez el %s, con la versión %s.\n" % (
                    self.hoy, self.version())
            t = t[:tramo[0]] + cuerpo + t[tramo[1]:]
        self.poner(ruta, t)
        self._poner_estado("Terminada")

    def _poner_estado(self, estado):
        """La fila de la fase en la HU, y el estado de la HU y de su fila en la épica."""
        t = self.leer(self.hu_md)
        marca = "`%s`" % self.nombre
        if marca in t:
            t = "\n".join(_ultima_celda(l, estado) if l.startswith("| " + marca) else l for l in t.split("\n"))
        else:
            enlace = lambda archivo: "[%s](%s/%s)" % (archivo, self.nombre, archivo)  # noqa: E731
            cas = [ca for ca, _n in self.plan()["cas"]]
            cubre = "%s a %s" % (cas[0], cas[-1]) if len(cas) > 1 else "".join(cas)
            t = _agregar_a_tabla(t, "## 8.", "| %s | %s | (vacío) | %s | %s | %s | %s |" % (
                marca, cubre, enlace("plan_trabajo.md"), enlace("plan_pruebas.md"), enlace("resultado_pruebas.md"),
                estado))
        tramo = _seccion(t, "## 8.")
        fases = [_celdas(l)[-1] for l in t[tramo[0]:tramo[1]].split("\n") if re.match(r"^\| `[A-Z]", l)]
        de_la_hu = "Terminada" if fases and all(e == "Terminada" for e in fases) else "En curso"
        t = re.sub(r"(?m)^(\| \*\*Estado\*\* \| ).*$", r"\g<1>%s |" % de_la_hu, t, count=1)
        self.poner(self.hu_md, t)
        enlace_hu = "](%s/%s.md)" % (self.hu_dir, self.hu_dir)
        orden = re.compile(r"^\| \d+ \| %s \|" % re.escape(self.hu_id))
        self.poner(self.epica_md, "\n".join(
            _ultima_celda(l, de_la_hu) if l.startswith("|") and (enlace_hu in l or orden.match(l)) else l
            for l in self.leer(self.epica_md).split("\n")))

    @staticmethod
    def correr_pruebas(orden):
        """Corre `orden` desde la carpeta actual. `(pasaron, resumen)`."""
        proceso = subprocess.run(orden, shell=True, capture_output=True, text=True, encoding="utf-8",
                                 errors="replace")
        salida = (proceso.stdout + "\n" + proceso.stderr).strip().split("\n")
        corridas = [l.strip() for l in salida if re.match(r"^Ran \d+ tests?", l.strip())]
        final = [l.strip() for l in salida if re.match(r"^(OK|FAILED)\b", l.strip())]
        resumen = ", ".join((corridas[-1:] + final[-1:])) or (salida[-1].strip() if salida else "sin salida")
        return proceso.returncode == 0, resumen

    def cerrar(self, escribir=False, pruebas=None, hallazgos="ninguno"):
        """`(qué pasó, [archivos tocados], [(archivo, línea) por llenar])`."""
        plan, casos = self.plan(), self.casos()
        if not casos:
            raise ValueError("el plan de pruebas de %s no tiene casos en su matriz" % self.nombre)
        corrida = None
        if pruebas:
            pasaron, resumen = self.correr_pruebas(pruebas)
            if not pasaron:
                raise ValueError("las pruebas fallan (%s): la fase no se cierra" % resumen)
            corrida = (pruebas, resumen)
        for archivo, texto in (("estado-fase.md", lambda: self.texto_estado(plan)),
                               ("resultado_pruebas.md", lambda: self.texto_resultado(plan, casos, corrida)),
                               ("funcionalidad_implementada.md", lambda: self.texto_funcionalidad(plan, casos))):
            if _en_plantilla(self.leer(self.ruta(archivo))):
                self.poner(self.ruta(archivo), texto())
        faltan = self.faltan()
        if faltan:
            return "faltan %d marcas por llenar" % len(faltan), self.guardar(escribir), faltan
        self._marcar_cerrada(plan, hallazgos)
        return "cerrada", self.guardar(escribir), []

    # ── la contraria ──────────────────────────────────────────────────────

    def reabrir(self, motivo, escribir=False):
        """Devuelve la fase a la estación 8. `(qué pasó, [archivos tocados])`."""
        if not (motivo or "").strip():
            raise ValueError("reabrir pide el motivo")
        hu = self.leer(self.hu_md)
        fila = [l for l in hu.split("\n") if l.startswith("| `%s`" % self.nombre)]
        if not fila or _celdas(fila[0])[-1] != "Terminada":
            raise ValueError("%s no está cerrada" % self.nombre)
        motivo = motivo.strip().rstrip(".")
        ruta = self.ruta("estado-fase.md")
        t = _ESTACION.sub("**Estación actual:** 8, implementador. **Última puerta pasada:** 7.", self.leer(ruta))
        t = "\n".join(_ultima_celda(l, "☐") if re.match(r"^\| (9|10|11|12) \| ", l) else l for l in t.split("\n"))
        t = re.sub(r"(?m)^(\| \*\*(?:Concepto|CA cumplidos)\*\* \| ).*$", r"\g<1>%s |" % AL_CERRAR, t)
        t = re.sub(r"(?m)^(## 3\. .*\n\n)Ninguna\.", r"\g<1>", t)
        t = _agregar_parrafo(t, "## 3.", "Reabierta el %s: %s." % (self.hoy, motivo))
        self.poner(ruta, t)
        ruta = self.ruta("funcionalidad_implementada.md")
        self.poner(ruta, re.sub(r"(?m)^(\| \*\*Veredicto\*\* \| ).*$", r"\g<1>%s |" % AL_CERRAR, self.leer(ruta)))
        ruta = self.ruta("resultado_pruebas.md")
        r = self.leer(ruta)
        ciclos = re.findall(r"(?m)^\| (\d+) \| \d{4}-\d{2}-\d{2} \|", r)
        siguiente = max(int(c) for c in ciclos) + 1 if ciclos else 2
        self.poner(ruta, _agregar_a_tabla(r, "## 8.", "| %d | %s | %s | %s | Reabierta: %s |" % (
            siguiente, self.hoy, MARCA, MARCA, motivo)))
        ruta = self.ruta("plan_pruebas.md")
        self.poner(ruta, re.sub(r"(?m)^(\| HU-\d+ \| CA-\d+ \| CP-\d+ \|.*\| )☑( \|)$", r"\g<1>☐\2", self.leer(ruta)))
        ruta = self.ruta("plan_trabajo.md")
        t = re.sub(r"(?m)^(\| CA-\d+ · .+ \| )☑( \|)$", r"\g<1>☐\2", self.leer(ruta))
        self.poner(ruta, t.rstrip("\n") + "\n\n**Reabierta** el %s: %s.\n" % (self.hoy, motivo))
        self._poner_estado("En curso")
        return "reabierta", self.guardar(escribir)


def _agregar_parrafo(texto, encabezado, parrafo):
    tramo = _seccion(texto, encabezado)
    if not tramo:
        return texto.rstrip("\n") + "\n\n" + parrafo + "\n"
    cuerpo = texto[tramo[0]:tramo[1]].rstrip("\n")
    return texto[:tramo[0]] + cuerpo + "\n\n" + parrafo + "\n\n" + texto[tramo[1]:]
