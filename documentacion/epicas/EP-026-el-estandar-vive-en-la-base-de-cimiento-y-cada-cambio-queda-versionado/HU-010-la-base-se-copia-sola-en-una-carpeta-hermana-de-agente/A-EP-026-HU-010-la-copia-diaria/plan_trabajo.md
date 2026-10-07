# Plan de Trabajo · Fase A-EP-026-HU-010-la-copia-diaria (módulo Historia de Cimiento)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-026-HU-010-la-copia-diaria` |
| **Épica** | `EP-026` |
| **HU** | [`HU-010`](../HU-010-la-base-se-copia-sola-en-una-carpeta-hermana-de-agente.md), una sola (`F12.1`) |
| **Módulo** | Historia de Cimiento, `proyectos/cimiento/core/historia/` |
| **Especificación del módulo** | La HU-010 y la [épica EP-026](../../epica.md) |
| **Fecha apertura** | 2026-10-06 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 132](../../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md), el 2026-10-06, con la versión 56.0.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Fase nueva. Sale del análisis 1 del pendiente 132, acuerdos 23, 24 y 25.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-010` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-010-la-base-se-copia-sola-en-una-carpeta-hermana-de-agente.md#ca-01--la-copia-del-día-se-hace-sola) | ☐ |
| [CA-02](../HU-010-la-base-se-copia-sola-en-una-carpeta-hermana-de-agente.md#ca-02--se-guardan-las-últimas-7) | ☐ |
| [CA-03](../HU-010-la-base-se-copia-sola-en-una-carpeta-hermana-de-agente.md#ca-03--la-copia-va-sin-claves-y-se-restaura) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** una copia diaria de la base, sola y en segundo plano, de la que se guardan 7 y que se puede comprobar.

**Fuera de alcance:** copias fuera de esta máquina.

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`core/enganches/niveles.py` (`NivelesDelProyecto.ajustes`) sabe conectarse a la base sin Django, con el `.env` de Cimiento. El enganche `adaptadores/claude-code/hook_sesion.py` corre al abrir cada sesión. La carpeta del estándar es `C:\Ing. Jose\ia\agente`; su hermana, `C:\Ing. Jose\ia\cimiento-copias`, no existe todavía.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/historia/copia.py` | Crear | Lógica | Copiar, guardar 7, probar; sin Django |
| `proyectos/cimiento/core/historia/management/__init__.py` | Crear | Orden | |
| `proyectos/cimiento/core/historia/management/commands/__init__.py` | Crear | Orden | |
| `proyectos/cimiento/core/historia/management/commands/copiar_base.py` | Crear | Orden | |
| `proyectos/cimiento/core/historia/management/commands/probar_copia.py` | Crear | Orden | |
| `proyectos/cimiento/core/historia/tests_copia.py` | Crear | Test | |
| `adaptadores/claude-code/hook_sesion.py` | Modificar | Enganche | Lanza la copia del día |

### 2.2 Matriz de dependencias del refactor

No aplica.

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

No aplica: corre sola; a mano, `manage.py copiar_base` y `manage.py probar_copia`.

### 2.5 Permisos / roles a sembrar  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| La copia la escribe Python con PyMySQL | `mysqldump` | No depende de dónde esté instalado MariaDB, y corre con lo que ya usan los enganches | Propuesta del agente |
| La lanza el inicio de sesión, en segundo plano | Una tarea programada de Windows | La tarea programada es un cambio del sistema fuera del proyecto (`04·S9`); el inicio de sesión ya corre cada día que se trabaja | Propuesta del agente |
| La carpeta se calcula como hermana del estándar | Un ajuste editable | Es la ruta exacta acordada; editable, dejaría escribir en cualquier parte | Acuerdo 23 |
| Las sesiones del navegador van sin filas | Copiarlas | Su llave deja entrar sin contraseña (`00·N6`) | `00·N6` |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

| Acción | Contraria |
|---|---|
| Copiar la base | Restaurarla desde una copia (`probar_copia` lo hace en una base aparte) |

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Copiar la base a un `.sql`, sin sesiones | Lógica | 1,5 h | — | EV-01 |
| T-02 | Guardar 7 y la copia del día una sola vez | Lógica | 0,5 h | T-01 | EV-01 |
| T-03 | Probar la restauración en una base aparte | Lógica | 1 h | T-01 | EV-01 |
| T-04 | El inicio de sesión la lanza y avisa si la última falló | Enganche | 0,5 h | T-02 | EV-01 |
| T-05 | Pruebas | Test | 1 h | T-01 a T-04 | EV-01 |

**Total estimado:** 4,5 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03, T-04, T-05

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Pruebas de Django | EV-01 | | ☐ |
| CA-02 | Pruebas de Django | EV-01 | | ☐ |
| CA-03 | Pruebas de Django | EV-01 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La base de pruebas de Django y una carpeta temporal |
| Usuarios de prueba | Ninguno |
| Datos precargados | Ninguno |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit; las copias ya hechas se pueden dejar o borrar a mano.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

No aplica: no cambia la base.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `00·N6`, `00·N7`, `04·S9`, `02·F30`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Otra sesión escribe en la misma carpeta y el freno se lo cobra a esta | Detiene órdenes de consola | Se anota y se sigue | Abierto |

## 11. Definition of Done

- [ ] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [ ] Pruebas en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

**Hallazgos al ejecutar:** ninguno todavía.
