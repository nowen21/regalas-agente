# Plan de Trabajo · Fase A-EP-029-HU-003-aviso-commit-e-instalacion (módulo Pruebas de Cimiento)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-029-HU-003-aviso-commit-e-instalacion` |
| **Épica** | `EP-029` |
| **HU** | [`HU-003`](../HU-003-al-empezar-a-trabajar-cimiento-avisa-si-la-revision-falta-o-esta-vencida.md), una sola (`F12.1`) |
| **Módulo** | Pruebas de Cimiento: `core/pruebas/`, con sus llamadas desde el arranque, el commit, el instalador y el desinstalador |
| **Especificación del módulo** | La HU-003: sus CA y sus reglas de negocio |
| **Fecha apertura** | 2026-10-08 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 141](../../../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-1.md), el 2026-10-08, con la versión 56.8.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Nueva funcionalidad: sale del análisis 1 del pendiente 141, puntos 7, 8 y 11; la lista de archivos sigue la R-19 de los análisis 2 y 3.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-003` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-003-al-empezar-a-trabajar-cimiento-avisa-si-la-revision-falta-o-esta-vencida.md#ca-01--el-aviso-al-empezar-a-trabajar) | ☑ |
| [CA-02](../HU-003-al-empezar-a-trabajar-cimiento-avisa-si-la-revision-falta-o-esta-vencida.md#ca-02--no-dejar-guardar-rechaza-el-commit) | ☑ |
| [CA-03](../HU-003-al-empezar-a-trabajar-cimiento-avisa-si-la-revision-falta-o-esta-vencida.md#ca-03--el-instalador-pone-la-herramienta-y-el-desinstalador-quita-la-suya) | ☑ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que al empezar a trabajar Cimiento avise si la revisión falta o está vencida, que «no dejar guardar» rechace el commit, y que el instalador ponga la herramienta que revisa.

**Fuera de alcance:** instalar PCOV, que es una extensión de PHP; la copia local (HU-004).

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

El arranque (`core/enganches/sesion.py`, `ArranqueDeSesion.validar`) junta hallazgos que `hook_sesion.py` le muestra al usuario. Los enganches leen la base sin Django con `NivelesDelProyecto.consultar_juntas` (`core/enganches/niveles.py`) y los ajustes con `ConfiguracionDelProyecto` (`core/enganches/configuracion.py`). El enganche `pre-commit` es `PLANTILLA_PRE_COMMIT` de `core/herramientas/instalar.py` y llama subcomandos de `validar.py`; un subcomando nuevo entra solo a la corrida completa (`tests_validar.py`, CP-004). El instalador arma su lista de pasos en `Instalador.instalar`; el desinstalador, en `Desinstalador.desinstalar`. Lo que pide Django (R-19): `instalada_por_cimiento` genera una sola migración, `pruebas/0003_instalada_por_cimiento.py`. Pantallas nuevas: ninguna, así que no hay menú, tablas, ayuda ni manual que agregar (R-19).

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/pruebas/models.py` | Modificar | Modelo | `instalada_por_cimiento` |
| `proyectos/cimiento/core/pruebas/migrations/0003_instalada_por_cimiento.py` | Crear | Migración | El campo nuevo |
| `proyectos/cimiento/core/pruebas/aviso.py` | Crear | Dominio | Compara opciones y revisión, sin Django |
| `proyectos/cimiento/core/pruebas/parte.py` | Crear | Dominio | Pone y quita la herramienta según el lenguaje, sin Django |
| `proyectos/cimiento/core/pruebas/management/commands/marcar_pruebas.py` | Crear | Orden | Anota en la base si el proyecto tiene la parte y quién la puso |
| `proyectos/cimiento/core/pruebas/tests_aviso.py` | Crear | Test | |
| `proyectos/cimiento/core/enganches/sesion.py` | Modificar | Enganche | El aviso en el arranque |
| `proyectos/cimiento/core/herramientas/validar.py` | Modificar | Validador | El subcomando `pruebas` |
| `proyectos/cimiento/core/herramientas/instalar.py` | Modificar | Instalador | El paso que pone la parte y la línea del `pre-commit` |
| `proyectos/cimiento/core/herramientas/desinstalar.py` | Modificar | Instalador | El paso que quita lo que puso Cimiento |
| `proyectos/cimiento/core/pruebas/lenguaje.py` | Modificar | Dominio | Recibe `python_del_proyecto`, que no depende de Django, para que la usen la revisión y el instalador; se agregó al plan antes de tocarlo |
| `proyectos/cimiento/core/pruebas/revisar.py` | Modificar | Dominio | Usa `python_del_proyecto` de `lenguaje.py` en vez de su copia; se agregó al plan antes de tocarlo |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

| Lo que cambia | Quién lo usa | Se prueba con |
|---|---|---|
| `ArranqueDeSesion.validar` | `hook_sesion.py` | `core.enganches` |
| `PLANTILLA_PRE_COMMIT` y los pasos del instalador | Toda instalación | `core.herramientas`, `core.enganches` |
| Los subcomandos de `validar.py` | La corrida completa | `core.herramientas.tests_validar` |

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

Ninguna nueva.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

El mensaje de arranque de cada sesión y el rechazo del commit.

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| El commit se revisa con un subcomando de `validar.py` | Un enganche aparte | Es el canal que ya usa el `pre-commit` | Propuesta del agente |
| La parte que revisa solo se pone en proyectos registrados fuera de la carpeta temporal | Ponerla siempre | Las pruebas instalan en carpetas temporales y no deben instalar paquetes | Pendiente 110, acuerdo 3 (propuesta del agente) |
| PCOV no se instala: se dice cómo instalarlo | Instalarlo | Es una extensión de PHP, depende de cada máquina | RN-05 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

| Acción | Su contraria |
|---|---|
| El instalador pone coverage.py | El desinstalador la quita, si la puso Cimiento |
| `marcar_pruebas` anota la parte | `marcar_pruebas --quitar` la borra |

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | El aviso sin Django y su lugar en el arranque | Enganche | 2 h | Ninguna | EV-01 |
| T-02 | El subcomando `pruebas` y la línea del `pre-commit` | Validador | 1 h | T-01 | EV-01 |
| T-03 | `instalada_por_cimiento`, `marcar_pruebas`, poner y quitar la parte | Instalador | 3 h | Ninguna | EV-01 |
| T-04 | Pruebas y regresión | Test | 2 h | T-01 a T-03 | EV-01 |

**Total estimado:** 8 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03, T-04.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Prueba de Django | EV-01 | 2026-10-08 | ☑ |
| CA-02 | Prueba de Django | EV-01 | 2026-10-08 | ☑ |
| CA-03 | Prueba de Django, con las órdenes simuladas | EV-01 | 2026-10-08 | ☑ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La base de pruebas de Django; la lectura sin Django va con `TransactionTestCase` |
| Usuarios de prueba | Ninguno |
| Datos precargados | Proyectos en carpetas temporales; las órdenes de pip se simulan |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit, `manage.py migrate pruebas 0002` y volver a instalar los proyectos para que su `pre-commit` vuelva al de antes.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Aditiva. Un proyecto sin volver a instalar sigue con su `pre-commit` anterior y solo recibe el aviso de arranque: el cambio de versión es MAYOR (análisis 1, «El entorno»).

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `02·F30`, `08·T3`, `00·ID7`, `20·M3`, `20·M10`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Ninguno | | | |

## 11. Definition of Done

- [x] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [x] Pruebas en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

**Hallazgos al ejecutar:** ninguno todavía.
