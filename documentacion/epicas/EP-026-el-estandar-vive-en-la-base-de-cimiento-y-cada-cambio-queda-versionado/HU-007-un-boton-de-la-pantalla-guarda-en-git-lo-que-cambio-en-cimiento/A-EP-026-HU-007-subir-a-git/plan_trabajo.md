# Plan de Trabajo · Fase A-EP-026-HU-007-subir-a-git (módulo Estándar en la base)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-026-HU-007-subir-a-git` |
| **Épica** | `EP-026` |
| **HU** | [`HU-007`](../HU-007-un-boton-de-la-pantalla-guarda-en-git-lo-que-cambio-en-cimiento.md), una sola (`F12.1`) |
| **Módulo** | Estándar en la base, `proyectos/cimiento/core/estandar/` |
| **Especificación del módulo** | La HU-007 y la [épica EP-026](../../epica.md) |
| **Fecha apertura** | 2026-10-06 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 132](../../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md), el 2026-10-06, con la versión 56.0.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Fase nueva. Usa `CambiosPorSesion` (`EP-025·HU-016`). Sale del análisis 1 del pendiente 132, acuerdos 3, 8 y 22.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-007` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-007-un-boton-de-la-pantalla-guarda-en-git-lo-que-cambio-en-cimiento.md#ca-01--se-ve-lo-que-cambió-cada-sesión) | ☐ |
| [CA-02](../HU-007-un-boton-de-la-pantalla-guarda-en-git-lo-que-cambio-en-cimiento.md#ca-02--el-botón-hace-el-commit-de-una-sesión) | ☐ |
| [CA-03](../HU-007-un-boton-de-la-pantalla-guarda-en-git-lo-que-cambio-en-cimiento.md#ca-03--si-falla-nada-queda-a-medias) | ☐ |
| [CA-04](../HU-007-un-boton-de-la-pantalla-guarda-en-git-lo-que-cambio-en-cimiento.md#ca-04--consulta-no-hace-commits) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** hacer y subir desde la pantalla el commit de lo que cambió una sesión.

**Fuera de alcance:** resolver lo que tocaron dos sesiones.

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`CambiosPorSesion` (`core/herramientas/cambios.py`) reparte lo cambiado por sesión con `repartir`, prepara lo de una con `preparar` y lo suelta con `soltar`. Las sesiones se anotan en `historico-chat/.tocado/` (`core/validadores/sesiones.py`). El commit corre los controles del `pre-commit` del repositorio.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/estandar/subir.py` | Crear | Lógica | Commit y subida, con su contraria |
| `proyectos/cimiento/core/estandar/views.py` | Modificar | Vista | `SubirAGit` |
| `proyectos/cimiento/core/estandar/urls.py` | Modificar | Rutas | |
| `proyectos/cimiento/core/estandar/templates/estandar/git.html` | Crear | Plantilla | |
| `proyectos/cimiento/core/estandar/templates/estandar/lista.html` | Modificar | Plantilla | Enlace |
| `proyectos/cimiento/core/estandar/tests_git.py` | Crear | Test | |
| `proyectos/cimiento/core/ayuda/secciones.py` | Modificar | Ayuda | La pantalla en la sección del estándar |
| `proyectos/cimiento/core/ayuda/templates/ayuda/secciones/estandar.html` | Modificar | Ayuda | |

### 2.2 Matriz de dependencias del refactor

No aplica: usa `CambiosPorSesion` sin cambiarlo.

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

| Ruta | Método | Quién |
|---|---|---|
| `/estandar/git/` | GET | Toda cuenta |
| `/estandar/git/` | POST | Administrador |

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

«Estándar» → «Subir a git».

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| El mensaje se arma con tres campos: asunto, la idea del usuario y lo que hizo el agente | Un solo campo | Así sale siempre en el orden de la convención del repositorio | Propuesta del agente |
| Si el commit falla, se suelta lo preparado | Dejarlo preparado | Lo preparado entraría en el commit siguiente (pendiente 126) | Propuesta del agente |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

| Acción | Contraria |
|---|---|
| Preparar lo de una sesión | Soltarlo, que se hace solo si el commit falla |
| Commit | `git revert`, a mano, con su propia aprobación |

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Commit y subida desde un programa | Lógica | 1 h | — | EV-01 |
| T-02 | Pantalla «Subir a git» y ayuda | Vista | 1 h | T-01 | EV-01 |
| T-03 | Pruebas con un repositorio temporal | Test | 1 h | T-01, T-02 | EV-01 |

**Total estimado:** 3 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Pruebas de Django | EV-01 | | ☐ |
| CA-02 | Pruebas de Django | EV-01 | | ☐ |
| CA-03 | Pruebas de Django | EV-01 | | ☐ |
| CA-04 | Pruebas de Django | EV-01 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | Un repositorio git temporal y la base de pruebas de Django |
| Usuarios de prueba | Una cuenta administradora y una de consulta |
| Datos precargados | Dos sesiones anotadas en `.tocado` |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit de la fase.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

No aplica: no cambia la base.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `00·N2`, `00·N3`, `00·N6`, `09·G2`, `02·F30`.

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
