# -*- coding: utf-8 -*-
"""Los cierres (`funcionalidad_implementada.md`) de las cuatro fases del 2026-10-02 que no lo tenían, y la
estación del commit marcada en su estado. Cada cierre sale de su plan, su resultado de pruebas y su commit."""
import glob
import os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
EPICA = glob.glob(os.path.join(RAIZ, "documentacion", "epicas", "EP-023-*"))[0]

FASES = [
    {
        "carpeta": "HU-001-*/D-EP-023-HU-001-*", "hu": "HU-001", "hu_md": "HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes.md",
        "modulo": "`plantillas/`, `validadores/`, `analisis/` y `base/13-documentacion/`", "cas": "CA-17 a CA-26",
        "version": "44.0.0", "commit": "79356eb",
        "resumen": "Todo análisis nuevo consulta las recomendaciones, considera dónde más puede pasar lo mismo, ordena sus HU por su dependencia y dice lo que suma al análisis principal. Aprobar un análisis pone la versión en la marca, no aprueba sin filas ni sin «Lo que aporta», y pasa lo que suma al principal. El análisis principal es la redacción que forman los aportes de los diez análisis.",
        "items": [("CA-17 a CA-19: «Dónde más puede pasar», la tabla de HU con su orden y las recomendaciones", "Plantilla y validador", "`plantillas/analisis.md`, `plantillas/recomendaciones-del-analisis.md`, `plantillas/ciclo-vida-proyectos/03-epica.md`, `validadores/analisis.py`", "CP-001 a CP-003"),
                  ("CA-20 y CA-24: el análisis principal y lo que suma cada análisis", "Documento, programa y validador", "`analisis/proyecto-2026-10-02-analisis-principal.md`, `validadores/analisis_en_curso.py`, `validadores/analisis.py`", "CP-004, CP-009"),
                  ("CA-21: medir la respuesta antes de entregarla", "Documento", "`plantillas/recomendaciones-del-analisis.md`, R-17", "CP-005"),
                  ("CA-22: lo nuevo no reabre lo aprobado", "Validador", "`validadores/analisis.py`, `validadores/analisis_en_curso.py`", "CP-006"),
                  ("CA-23: `DOC25` anota todo análisis aprobado", "Regla", "`base/13-documentacion/reglas/DOC25-reescribe-el-analisis-principal-con-su-lista-de-cambios.md`", "CP-008"),
                  ("CA-25 y CA-26: sin filas o sin «Lo que aporta» no se aprueba", "Programa", "`validadores/analisis_en_curso.py`, `adaptadores/claude-code/hook_analisis.py`", "CP-010, CP-011")],
        "tareas": "21", "uso": "Al aprobar un análisis con «Apruebo el análisis», el programa revisa que tenga filas en «Lo que se tiene que hacer» y la sección «Lo que aporta», y pasa lo que suma al análisis principal. `python validadores/validar.py analisis` revisa lo que exige la 44.0.0 y avisa del análisis que no está en la «Lista de análisis».",
        "decision": ("El principal de su alcance se busca subiendo de carpeta", "Cubre el módulo con principal propio sin pedir otro dato; se descartó pedir el alcance en cada análisis"),
        "deuda": "Ninguna. Salió el hallazgo H-12 (las pruebas de la plataforma escriben en el registro real de auditoría), anotado en el resumen de la sesión.",
        "fuera": "Ninguno.",
    },
    {
        "carpeta": "HU-003-*/A-EP-023-HU-003-*", "hu": "HU-003", "hu_md": "HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde.md",
        "modulo": "`plantillas/`, `validadores/` y `base/`", "cas": "CA-01 a CA-08",
        "version": "45.0.0", "commit": "d11f0ea",
        "resumen": "El hallazgo trae qué pasó, por qué importa y el enlace a su pendiente; el pendiente trae de dónde sale, el problema y por qué importa. Su estado y por dónde se retoma se calculan siguiendo los enlaces. Cada pendiente nuevo vive en una carpeta `pendientes/` de su dueño, la numeración es una sola y un programa arma el índice en `documentacion/pendientes.md`. El 103 pasó a `EP-023/pendientes/`.",
        "items": [("CA-01, CA-07 y CA-08: dónde vive el pendiente y `pendientes/` como historia", "Regla, validador, programa e instalador", "`base/20-meta-reglas/base.md`, `02·F13`, `validadores/fases.py`, `validadores/flujo.py`, `validadores/pendientes.py`, `validadores/andamio.py`, `validadores/instalar.py`", "CP-001, CP-007, CP-008"),
                  ("CA-02: las plantillas con solo sus campos", "Plantilla", "`plantillas/pendiente.md`, `plantillas/pendiente-de-seguimiento.md`, `plantillas/pendiente-reportado.md`, `plantillas/sesion.md`", "CP-002"),
                  ("CA-03 a CA-05: los validadores, el cierre calculado y el hallazgo de dos campos", "Validador y regla", "`validadores/pendientes.py`, `validadores/resumen.py`, `13·DOC22`", "CP-003 a CP-005"),
                  ("CA-06: sin «Proyecto de origen»", "Regla y plantilla", "`02·F24`, las plantillas del pendiente", "CP-006")],
        "tareas": "16", "uso": "`python validadores/andamio.py pendiente <slug> [--hu <épica>/<HU>]` crea el pendiente como carpeta en su dueño. `python validadores/validar.py pendientes --indice` escribe el índice. El estado del hallazgo y del pendiente no se escribe: lo calculan `resumen.py` y `pendientes.py`.",
        "decision": ("El 103 pasó a `EP-023/pendientes/`", "Su dueño es EP-023 y el análisis 8 pide `pendientes/` y nada más; los pendientes viejos no se tocan y pasan cuando se vayan a trabajar"),
        "deuda": "| `cerrar.py` sigue usando «Proyecto de origen» para avisar a los proyectos de los pendientes viejos | Diferido por el plan | El plan dejó `cerrar.py` fuera de alcance |",
        "fuera": "`validadores/flujo.py`, que también tomaba `pendientes/` como una HU; se ajustó dentro de la T-11.",
    },
    {
        "carpeta": "HU-006-*/A-EP-023-HU-006-*", "hu": "HU-006", "hu_md": "HU-006-lo-aprendido-incluye-las-lecciones.md",
        "modulo": "`memoria/`, `plantillas/` y `validadores/`", "cas": "CA-01 y CA-02",
        "version": "46.0.0", "commit": "d5e33a3",
        "resumen": "El almacén de señales acepta el tipo `leccion`. La tabla de lecciones del análisis enlaza la señal de cada una y dice qué recomendación complementa o crea. El validador lo exige a los análisis aprobados desde la 46.0.0.",
        "items": [("CA-01: la lección tiene su categoría y el análisis la enlaza", "Programa, plantilla y validador", "`memoria/memoria.py`, `memoria/esquema.sql`, `documentacion/senales.md`, `plantillas/analisis.md`, `validadores/analisis.py`", "CP-001, CP-003"),
                  ("CA-02: las lecciones alimentan las recomendaciones", "Plantilla y validador", "`plantillas/analisis.md`, `validadores/analisis.py`", "CP-002, CP-003")],
        "tareas": "6", "uso": "`python memoria/memoria.py add --tipo leccion ...` guarda la lección; la tabla de lecciones enlaza su `S-NNN` y dice «complementa R-n», «nueva R-n» o «no aplica».",
        "decision": ("El tipo se llama `leccion`, sin tilde", "Los tipos del almacén se escriben sin tilde, como `decision` y `restriccion`"),
        "deuda": "Ninguna.",
        "fuera": "Ninguno.",
    },
    {
        "carpeta": "HU-004-*/A-EP-023-HU-004-*", "hu": "HU-004", "hu_md": "HU-004-un-hallazgo-detiene-la-ejecucion-y-vuelve-al-analisis.md",
        "modulo": "`base/`, `plantillas/` y `validadores/`", "cas": "CA-01 a CA-07",
        "version": "47.0.0", "commit": "cfcc89d",
        "resumen": "Un hallazgo al ejecutar un plan lo detiene y vuelve al análisis; el plan pasa a su versión siguiente con aprobación nueva, y la fase cerrada se reabre si el hallazgo es sobre lo que construyó. La fase y su HU no pueden decir que cerraron mientras el análisis del hallazgo siga sin aprobar, y el plan dice cuántos hallazgos salieron.",
        "items": [("CA-01, CA-03, CA-04, CA-05 y CA-07: las reglas", "Regla", "`02·F8`, `02·F9`, `02·F28`, `13·DOC12`, `13·DOC24`, `base/02-flujo-de-trabajo/base.md`, `base/02-flujo-de-trabajo/nomenclatura-de-fases.md`", "CP-001, CP-003 a CP-005, CP-007"),
                  ("CA-02: un hallazgo detiene y nada cierra", "Plantilla y validador", "`plantillas/ciclo-vida-proyectos/10-estado-fase.md`, `validadores/fases.py`", "CP-002"),
                  ("CA-06: el plan registra sus hallazgos", "Plantilla", "`plantillas/ciclo-vida-proyectos/07-plan-trabajo.md`", "CP-006")],
        "tareas": "9", "uso": "Cuando aparece un hallazgo al ejecutar, se detiene el trabajo, se abre el análisis siguiente del pendiente y el estado de la fase anota el motivo. `python validadores/validar.py fases` falla si la fase o la HU dicen que cerraron con ese análisis sin aprobar.",
        "decision": ("El anexo de `02·F12` se ajustó con una línea fechada", "El usuario lo aprobó en el análisis 1 del pendiente 103 (punto 18); el texto literal anterior quedó como estaba"),
        "deuda": "Ninguna. Salió el hallazgo H-13 (los planes se escribían sin leer lo que el análisis decidió), anotado en el resumen de la sesión.",
        "fuera": "Ninguno.",
    },
]

MOLDE = """# Funcionalidad implementada · Fase `{fase}` (módulo {modulo})   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `{fase}` |
| **Módulo** | {modulo} |
| **Especificación del módulo** | Los {cas} de la [{hu}](../{hu_md}) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md) |
| **HU / CA cubiertas** | {hu} ({cas}) |
| **Fecha de cierre** | 2026-10-02 |
| **Versión del estándar al cerrar** | {version} |
| **Commit** | `{commit}` |

## 1. Qué se implementó, resumen

{resumen}

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
{items}

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las {tareas} tareas del plan quedaron hechas; cada una está en la tabla del plan con su archivo y su caso de prueba, y el [`resultado_pruebas.md`](resultado_pruebas.md) dice qué salió de cada caso.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): {fuera}

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

- Pruebas: las de la fase, que nombra la sección 3.5 de su plan de pruebas.
- Defectos abiertos que se aceptaron: ninguno.

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

{uso}

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| {dec} | {por} | Por escribir |

## 6. Deuda técnica y pendientes generados

{deuda}

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] `CHANGELOG.md` y `VERSION`.
- [ ] Mapa de dependencias: N/A, el estándar no lo mantiene.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Cada proyecto lo recibe al adoptar la {version} con el instalador.
"""


def main():
    for f in FASES:
        carpeta = glob.glob(os.path.join(EPICA, *f["carpeta"].split("/")))[0]
        fase = os.path.basename(carpeta)
        items = "\n".join("| %s | %s | %s | ✅ | %s |" % i for i in f["items"])
        deuda = f["deuda"]
        if deuda.startswith("|"):
            deuda = "| Deuda | Origen | Por qué |\n|---|---|---|\n" + deuda
        texto = MOLDE.format(fase=fase, modulo=f["modulo"], cas=f["cas"], hu=f["hu"], hu_md=f["hu_md"],
                             version=f["version"], commit=f["commit"], resumen=f["resumen"], items=items,
                             tareas=f["tareas"], fuera=f["fuera"], uso=f["uso"], dec=f["decision"][0],
                             por=f["decision"][1], deuda=deuda)
        with open(os.path.join(carpeta, "funcionalidad_implementada.md"), "w", encoding="utf-8", newline="\n") as s:
            s.write(texto)
        estado = os.path.join(carpeta, "estado-fase.md")
        with open(estado, encoding="utf-8") as e:
            t = e.read()
        t = t.replace("| 12 | Commit | 👤 autorizado | ☐ |", "| 12 | Commit | 👤 autorizado | ✅ `%s` |" % f["commit"])
        with open(estado, "w", encoding="utf-8", newline="\n") as e:
            e.write(t)


if __name__ == "__main__":
    main()
