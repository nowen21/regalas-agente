# -*- coding: utf-8 -*-
"""Cierra los documentos de la fase de la HU-006 de EP-025 (2026-10-05).

Se corrió una vez, desde la raíz del estándar, después de que el ciclo 2 de la
HU-003 desbloqueó la fase.
"""
import glob
import io
import os

EPICA = "documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens"
FASE = glob.glob(os.path.join(EPICA, "HU-006*", "A-*"))[0]

RESULTADO = '''# Resultado de Pruebas · Fase `A-EP-025-HU-006-lectura-de-los-jsonl`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-006-lectura-de-los-jsonl` |
| **HU** | [HU-006](../HU-006-el-gasto-de-cada-llamada-queda-guardado.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), versión 1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-05 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Máquina local, rama `main`, sobre el commit `29a30ad` más los cambios sin guardar; base de pruebas y base real en MariaDB 11.4.9; versión 54.2.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `ElLector` (6 pruebas), `LaOrdenGuardaSinDuplicar.test_guarda_lo_de_la_muestra` y `manage.py leer_consumo` contra la base real | Dos llamadas, dos enganches y un archivo, con proyecto y sesión; la orden real leyó los 12 proyectos sin error | Aprobado | EV-01, EV-02 | Ninguno |
| CP-002 | CA-02 | Alta | `test_dos_veces_no_duplica_y_no_vuelve_a_abrir`, `test_lo_nuevo_se_suma` y la orden real repetida | Las mismas cantidades; una llamada más al agregarla; en la segunda corrida real, 11 de 12 proyectos sin nada nuevo (el otro es esta sesión, que sigue escribiendo) | Aprobado | EV-01, EV-02 | Ninguno |
| CP-003 | CA-03 | Media | `test_una_linea_ilegible_se_salta`, `test_la_ultima_linea_sin_salto_queda_para_despues`, `test_la_linea_completada_despues_se_guarda` | Lo legible queda; la línea sin salto entra en la lectura siguiente | Aprobado | EV-01 | Ninguno |
| CP-004 | CA-04 | Media | `test_la_suma_de_la_sesion_cuenta_una_vez_la_llamada_partida` y `LaLecturaDelConsumoQuedaProgramada` (5 pruebas) | Dos consumos, no tres; la simulación no corre nada; en Windows, `schtasks /Create`; «ya estaba»; «OMITIDO» fuera de Windows | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 4 casos en el plan, 4 acá.

**Qué salió distinto de lo esperado:** la primera corrida real falló por D-01 de la HU-003 (la tabla de la plataforma vieja). Se corrigió allá, en su ciclo 2, y esta fase se volvió a correr.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | La orden contra la base real | `manage.py leer_consumo` | 12 proyectos; el estándar: 7531 llamadas y 35.796.810 tokens de entrada |
| 2 | Los miles con punto, como en Colombia | `manage.py leer_consumo --proyecto dp_card` | «2.678.636 tokens de entrada» |
| 3 | Las pruebas del instalador que tocó la fase | `PrepararCimiento`, `LaLecturaDelConsumoQuedaProgramada`, `PyMySQLParaElFreno` | 16 pruebas, todas pasan |

## 4. Defectos encontrados

Ninguno de esta fase.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |
| CA-04 | CP-004 | Aprobado | Sí |
| RNF-01 | CP-001 | `test_no_guarda_texto` | Sí |
| RNF-02 | CP-002 | Un archivo sin cambios no se abre | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 4 de 4 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 4 de 4 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los cuatro criterios pasan en la base de pruebas y la orden lee los proyectos reales.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/consumo/` (12 pruebas en `tests.py`) y `proyectos/cimiento/core/herramientas/tests_instalacion.py` |
| EV-02 | Base real | Tablas `consumo_*` de la base `cimiento` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-05 | 4 | 0 | Primera ejecución |
'''

FUNCIONALIDAD = '''# Funcionalidad implementada · Fase `A-EP-025-HU-006-lectura-de-los-jsonl` (módulo `proyectos/cimiento/core/consumo/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-006-lectura-de-los-jsonl` |
| **Módulo** | `proyectos/cimiento/core/consumo/`, `adaptadores/claude-code/hook_presupuesto.py`, `proyectos/cimiento/core/herramientas/` |
| **Especificación del módulo** | Los CA de la [HU-006](../HU-006-el-gasto-de-cada-llamada-queda-guardado.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-006 (CA-01 a CA-04) |
| **Fecha de cierre** | 2026-10-05 |
| **Versión del estándar al cerrar** | 54.2.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

`manage.py leer_consumo` lee los registros de Claude Code de cada proyecto activo y guarda en la base de Cimiento cada llamada con sus tokens, cada enganche con su tamaño y cada archivo leído. Repetirla no duplica. La instalación la programa una vez al día. `hook_presupuesto.py` cuenta cada llamada una sola vez: antes la contaba unas tres.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Programa | `proyectos/cimiento/core/consumo/lector.py`, `proyectos/cimiento/core/consumo/models.py`, `proyectos/cimiento/core/consumo/guardar.py`, `proyectos/cimiento/core/consumo/management/commands/leer_consumo.py` | ✅ | CP-001 |
| CA-02 | Programa | `proyectos/cimiento/core/consumo/models.py`, `proyectos/cimiento/core/consumo/guardar.py` | ✅ | CP-002 |
| CA-03 | Programa | `proyectos/cimiento/core/consumo/lector.py` | ✅ | CP-003 |
| CA-04 | Programa | `adaptadores/claude-code/hook_presupuesto.py`, `proyectos/cimiento/core/herramientas/instalar.py`, `validadores/instalar.py` | ✅ | CP-004 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 8 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

`python manage.py leer_consumo`, o con `--proyecto «nombre»` para uno solo. En Windows la corre la tarea programada «Cimiento leer consumo».

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Una llamada se cuenta una vez por su `message.id` | Claude Code parte una llamada en varias líneas con el mismo `usage` (H-5 del resumen del 2026-10-04, sesión 3) | No hace falta: está en el lector y en su prueba |
| Los tokens de un enganche o de un archivo se estiman con 3,5 caracteres por token | El registro no trae los tokens de cada pieza; la constante vive en un solo lugar | No hace falta |

## 6. Deuda técnica y pendientes generados

Ninguno.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

No aplica.

## 8. Despliegue, si aplica  ·  `13·DOC4`

La instalación del estándar corre `preparar_base` y programa la lectura.
'''


def escribir(ruta, texto):
    with io.open(ruta, "w", encoding="utf-8", newline="") as f:
        f.write(texto)


def cambiar(ruta, pares, al_final=""):
    texto = io.open(ruta, encoding="utf-8").read()
    for viejo, nuevo in pares:
        assert viejo in texto, (ruta, viejo[:70])
        texto = texto.replace(viejo, nuevo, 1)
    escribir(ruta, texto + al_final)


escribir(os.path.join(FASE, "resultado_pruebas.md"), RESULTADO)
escribir(os.path.join(FASE, "funcionalidad_implementada.md"), FUNCIONALIDAD)
cambiar(os.path.join(FASE, "estado-fase.md"), [
    ("**Estación actual:** 8, implementador. **Última puerta pasada:** 7.",
     "**Estación actual:** 12, commit. **Última puerta pasada:** 11."),
    ("| 8 | Implementador | implementado + pruebas verdes | ☐ |",
     "| 8 | Implementador | implementado + pruebas verdes | ☑ Las 8 tareas |"),
    ("| 9 | Verificador | trazabilidad sin faltantes | ☐ |",
     "| 9 | Verificador | trazabilidad sin faltantes | ☑ Sin fallas |"),
    ("| 10 | Crítico | sin hallazgos graves | ☐ |",
     "| 10 | Crítico | sin hallazgos graves | ☑ Ninguno |"),
    ("| 11 | Cierre documental + señales | docs y señales al día | ☐ |",
     "| 11 | Cierre documental + señales | docs y señales al día | ☑ Resultado, funcionalidad, HU y épica |"),
    ("**Hechas:** 7 de 8 (falta el cierre). **Bloqueadas:** T-08, por el hallazgo de la sección 4.",
     "**Hechas:** 8 de 8. **Bloqueadas:** ninguna."),
    ("| **Concepto** | Todavía no se ejecutó |\n| **CA cumplidos** | 0 de 4 |",
     "| **Concepto** | Cumple |\n| **CA cumplidos** | 4 de 4 |"),
    ("vuelve al análisis (análisis 2 del pendiente 119).", "vuelve al análisis."),
], "\n**Desbloqueada el 2026-10-05.** Se corrigió en el ciclo 2 de la fase de la HU-003, por orden del "
   "usuario: la base se respaldó, se reinició con las migraciones y se llenó con los proyectos que existen.\n")
cambiar(glob.glob(os.path.join(EPICA, "HU-006*", "HU-006-*.md"))[0], [
    ("[resultado_pruebas.md](A-EP-025-HU-006-lectura-de-los-jsonl/resultado_pruebas.md) | En curso |",
     "[resultado_pruebas.md](A-EP-025-HU-006-lectura-de-los-jsonl/resultado_pruebas.md) | Terminada |"),
])
cambiar(os.path.join(EPICA, "epica.md"), [
    ("| El gasto de cada llamada queda guardado | Must | N/A | N/A | Backlog |",
     "| El gasto de cada llamada queda guardado | Must | N/A | N/A | Terminada |"),
    ("| Sin datos guardados no hay qué mostrar | Backlog |",
     "| Sin datos guardados no hay qué mostrar | Terminada |"),
])
print("HU-006 cerrada en sus documentos")
