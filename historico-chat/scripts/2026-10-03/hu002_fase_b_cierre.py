# -*- coding: utf-8 -*-
"""Fase B de la HU-002: resultado de las pruebas, lo implementado, el estado y la fila en la HU."""
import glob
import io
import os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
HU_DIR = glob.glob(os.path.join(RAIZ, "documentacion", "epicas", "EP-023-*", "HU-002-*"))[0]
HU_DOC = "HU-002-cada-documento-sale-del-anterior.md"
FASE = "B-EP-023-HU-002-el-agente-recibe-los-acuerdos-y-el-plan-marca-lo-suyo"
D = os.path.join(HU_DIR, FASE)

RESULTADO = """# Resultado de Pruebas · Fase `{f}`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `{f}` |
| **HU** | [HU-002](../{hu}) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), versión 1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-03 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Repositorio del estándar en la máquina local, rama `main`, sobre el commit `6034476` más los cambios de la fase, versión 50.0.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-04 | Alta | `test_los_acuerdos_llegan.py` (5 pruebas) | La fase recién creada recibe los acuerdos de todos los CA de su HU; con plan, solo los de sus CA; con el commit anotado o vieja y cerrada, deja de estar en curso; la nueva con cierre y sin commit sigue en curso | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-04 | Alta | `test_los_acuerdos_llegan.py` (4 pruebas) y el enganche sobre el repositorio | Llegan los acuerdos de los análisis aprobados del pendiente; con un tope pequeño, los que no caben llegan nombrados con su tema y su número; con una entrada dañada el enganche sale con 0; el instalador lo registra | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-05 | Alta | `test_los_acuerdos_llegan.py` (6 pruebas) | La plantilla tiene la columna; la decisión sin acuerdo ni marca, la que cita un acuerdo que no existe y la tabla sin la columna fallan; la cita válida y la propuesta pasan; el plan aprobado con 49.0.0 no se revisa | Aprobado | EV-02 | Ninguno |
| CP-004 | RNF-06 | Media | `validar.py flujo` | Ninguna tarea sin su criterio; queda el aviso de que la especificación son los criterios de la HU | Aprobado | EV-02 | Ninguno |

**Correspondencia con el plan:** 4 casos en el plan, 4 acá.

**Qué salió distinto de lo esperado:** el mapa del sitio no lista los enganches uno por uno; la carpeta `adaptadores/claude-code/` ya los cubre, así que solo se sumó `acuerdos.py`.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Marcas de `00·ID8` en lo que escribió la fase | `validar.py marcas --preparados` | Ninguna nueva |
| 2 | Coherencia del estándar y origen de cada punto | `validar.py estandar` y `validar.py origen` | Sin fallas |
| 3 | Que los programas que cambió la fase sigan andando | Las 93 pruebas de `origen.py` y del instalador | Pasan |
| 4 | Lo que entrega el enganche sobre este repositorio | Correrlo con la fase en curso | Entrega los acuerdos 3 y 4 del análisis 10 |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-04 | CP-001, CP-002 | Aprobado | Sí |
| CA-05 | CP-003 | Aprobado | Sí |
| RNF-06 | CP-004 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 3 de 3 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 4 de 4 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple. Espera la aprobación del usuario.

**Justificación:** los CA-04 y CA-05 y el RNF-06 tienen sus casos ejecutados y aprobados. Las pruebas de la fase pasan: 15 de `test_los_acuerdos_llegan.py`.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa, enganche e instalador | `validadores/acuerdos.py`, `adaptadores/claude-code/hook_acuerdos.py`, `validadores/instalar.py` |
| EV-02 | Plantilla, validador y pruebas | `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md`, `validadores/origen.py`, `validadores/tests/test_los_acuerdos_llegan.py` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-03 | 4 | 0 | Primera ejecución |
"""

FUNCIONALIDAD = """# Funcionalidad implementada · Fase `{f}` (módulo `validadores/`, `adaptadores/claude-code/` y `plantillas/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `{f}` |
| **Módulo** | `validadores/`, `adaptadores/claude-code/` y `plantillas/` |
| **Especificación del módulo** | Los CA-04 y CA-05 de la [HU-002](../{hu}) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md) |
| **HU / CA cubiertas** | HU-002 (CA-04 y CA-05) |
| **Fecha de cierre** | 2026-10-03 |
| **Versión del estándar al cerrar** | 50.0.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Con cada mensaje, el agente recibe los acuerdos de los que sale lo que trabaja: los de la fase en curso, siguiendo el «Sale de» de sus criterios, y los de los análisis aprobados del pendiente del análisis prendido. Cada decisión del plan dice de qué acuerdo sale o que es propuesta del agente, y la revisión de origen detiene la que no dice ninguna de las dos.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-04: los acuerdos llegan con cada mensaje | Programa, enganche e instalador | `validadores/acuerdos.py`, `adaptadores/claude-code/hook_acuerdos.py`, `validadores/instalar.py` | ✅ | CP-001, CP-002 |
| CA-05: la decisión del plan dice de dónde sale | Plantilla y validador | `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md`, `validadores/origen.py` | ✅ | CP-003 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 6 tareas del plan quedaron hechas; cada una está en la tabla del plan con su archivo y su caso de prueba, y el [`resultado_pruebas.md`](resultado_pruebas.md) dice qué salió de cada caso.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

- Pruebas: las de la fase, que nombra la sección 3.5 de su plan de pruebas, y las de los programas que cambió.
- Defectos abiertos que se aceptaron: ninguno.

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

El enganche corre solo con cada mensaje, una vez que el instalador lo registra. `python validadores/validar.py origen` revisa las decisiones de los planes aprobados desde 50.0.0.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| La fase vieja cerrada se reconoce por su cierre y por no traer la aprobación con versión | 105 de 240 fases cerraron antes de que se anotara el commit; sin esto quedarían en curso para siempre | Por escribir |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] `CHANGELOG.md` y `VERSION`.
- [x] `anatomia/mapa-del-sitio.md`: el programa nuevo.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Cada proyecto lo recibe al adoptar la 50.0.0 con el instalador, que registra el enganche nuevo.
"""


def cambiar(p, pares):
    t = io.open(p, encoding="utf-8").read()
    for a, b in pares:
        assert t.count(a) == 1, (p, a)
        t = t.replace(a, b)
    io.open(p, "w", encoding="utf-8", newline="\n").write(t)


def main():
    for nombre, molde in (("resultado_pruebas.md", RESULTADO), ("funcionalidad_implementada.md", FUNCIONALIDAD)):
        io.open(os.path.join(D, nombre), "w", encoding="utf-8", newline="\n").write(molde.format(f=FASE, hu=HU_DOC))
    cambiar(os.path.join(D, "estado-fase.md"), [
        ("**Estación actual:** 8, implementador. **Última puerta pasada:** 7.", "**Estación actual:** 12, commit. **Última puerta pasada:** 11."),
        ("| 8 | Implementador | implementado + pruebas verdes | ☐ |", "| 8 | Implementador | implementado + pruebas verdes | ☑ Las 6 tareas; las pruebas de la fase pasan |"),
        ("| 9 | Verificador | trazabilidad sin faltantes | ☐ |", "| 9 | Verificador | trazabilidad sin faltantes | ☑ `flujo` y `origen` sin fallas |"),
        ("| 10 | Crítico | sin hallazgos graves | ☐ |", "| 10 | Crítico | sin hallazgos graves | ☑ Ninguno |"),
        ("| 11 | Cierre documental + señales | docs y señales al día | ☐ |", "| 11 | Cierre documental + señales | docs y señales al día | ☑ Resultado de pruebas, cierre, HU y registro de cambios |"),
        ("**Hechas:** 0 de 6.", "**Hechas:** 6 de 6."),
        ("| **Concepto** | Sin ejecutar |", "| **Concepto** | Cumple |"),
        ("| **CA cumplidos** | 0 de 2 |", "| **CA cumplidos** | 2 de 2 |"),
        ("## 3. Pendiente / preguntas abiertas\n\nNinguna.\n", "## 3. Pendiente / preguntas abiertas\n\n- Que el usuario apruebe la fase y autorice el commit.\n"),
    ])
    p = os.path.join(D, "plan_pruebas.md")
    t = io.open(p, encoding="utf-8").read()
    for c in ("CA-04 | CP-001", "CA-04 | CP-002", "CA-05 | CP-003", "RNF-06 | CP-004"):
        i = t.index("| HU-002 | " + c)
        j = t.index("\n", i)
        assert t[i:j].endswith("☐ |")
        t = t[:i] + t[i:j][:-3] + "☑ |" + t[j:]
    io.open(p, "w", encoding="utf-8", newline="\n").write(t)
    cambiar(os.path.join(HU_DIR, HU_DOC), [
        ("plan_pruebas.md) | Pendiente | Planes aprobados; en ejecución |",
         "plan_pruebas.md) | [resultado](%s/resultado_pruebas.md) | Cumple; espera la aprobación |" % FASE)])


if __name__ == "__main__":
    main()
