# Plan de Trabajo · Fase A-EP-025-HU-029-reinicio-solo (módulo El gasto)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-029-reinicio-solo` |
| **Épica** | `EP-025` |
| **HU** | [`HU-029`](../HU-029-el-vigilante-se-reinicia-solo-cuando-cambia-su-codigo.md), una sola (`F12.1`) |
| **Módulo** | El gasto: `core/consumo/` |
| **Especificación del módulo** | Los CA de la HU-029 |
| **Fecha apertura** | 2026-10-08 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | El usuario, con «apruebo» a la opción 1, el 2026-10-08, con la versión 58.0.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): la de la `HU-011`, que creó el vigilante, y la de la `HU-025`, que le quitó los relojes.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-029` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-029-el-vigilante-se-reinicia-solo-cuando-cambia-su-codigo.md#ca-01--un-cambio-de-código-reinicia-el-vigilante) | ☐ |
| [CA-02](../HU-029-el-vigilante-se-reinicia-solo-cuando-cambia-su-codigo.md#ca-02--el-relevo-no-deja-al-consumo-sin-vigilante) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que el vigilante del consumo se reinicie solo, con relevo, cuando cambia el código de Cimiento.

**Fuera de alcance:** arrancarlo cuando no está corriendo.

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`vigilante.py` vigila la carpeta de Claude Code con `watchdog` y espera sin despertar; `test_no_tiene_relojes` prohíbe `sleep(`, `CADA` y `time.monotonic` en ese archivo. `vigilar_consumo` guarda el número de proceso en `.agente/vigilar-consumo.pid` y no arranca si ya hay uno vivo. El vigilante de esta máquina quedó detenido el 2026-10-08 por orden del usuario.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/consumo/reinicio.py` | Crear | Lógica | Qué cuenta como código, la calma y el relevo |
| `proyectos/cimiento/core/consumo/vigilante.py` | Modificar | Lógica | Vigila también el código de Cimiento |
| `proyectos/cimiento/core/consumo/management/commands/vigilar_consumo.py` | Modificar | Orden | Le da al vigilante cómo arrancar el nuevo |
| `proyectos/cimiento/core/consumo/tests_reinicio.py` | Crear | Test | |
| `proyectos/cimiento/core/ayuda/templates/ayuda/secciones/gasto.html` | Modificar | Plantilla | El manual dice que se reinicia solo |
| `proyectos/cimiento/README.md` | Modificar | Documento | |
| `historico-chat/scripts/2026-10-08/README.md` | Modificar | Índice | |
| `historico-chat/scripts/2026-10-08/salida_reinicio.txt` | Crear | Evidencia | El número de proceso antes y después de un cambio de código |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

| Lo que cambia | Quién lo usa | Se prueba con |
|---|---|---|
| `vigilante.py`, `vigilar_consumo.py` | El arranque de sesión de Windows | `core.consumo` |

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

Ninguna nueva.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

Ninguno: corre por debajo.

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| El código se vigila con el mismo `watchdog` | Revisar la fecha de los archivos cada cierto tiempo | Sin relojes | Análisis 1 del pendiente 124, acuerdos 4 y 6 |
| El reinicio va en `reinicio.py`, aparte | Ponerlo en `vigilante.py` | La espera de calma y la del relevo son esperas acotadas; `vigilante.py` sigue sin ninguna | `test_no_tiene_relojes` |
| El viejo se detiene solo cuando el nuevo escribió su número | Detenerse apenas lanza el nuevo | Si el nuevo falla, el consumo no queda sin vigilante | RN-04 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

El reinicio no es una acción del usuario. `vigilar_consumo --parar` sigue deteniéndolo.

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | `reinicio.py` y vigilar el código | Lógica | 1 h | Ninguna | EV-01 |
| T-02 | Pruebas y el reinicio de verdad | Test | 0,5 h | T-01 | EV-01, EV-02 |
| T-03 | Manual y README | Documento | 0,25 h | T-01 | EV-01 |

**Total estimado:** 1,75 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Prueba de Django | EV-01 | | ☐ |
| CA-02 | Prueba de Django y reinicio de verdad | EV-01, EV-02 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |
| EV-02 | El relevo en esta máquina | `historico-chat/scripts/2026-10-08/salida_reinicio.txt` |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La base de pruebas de Django; esta máquina para el relevo |
| Usuarios de prueba | Ninguno |
| Datos precargados | Ninguno |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit y reiniciar el vigilante a mano.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Sin datos. El vigilante que esté corriendo con el código anterior hay que reiniciarlo una última vez a mano; desde ahí se reinicia solo.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `04·S10`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | El vigilante de esta máquina está detenido y el agente no puede arrancarlo | Sin él no se prueba el relevo de verdad | Lo arranca el usuario una vez | Resuelto: lo arrancó el 2026-10-08 a las 15:01 |

## 11. Definition of Done

- [ ] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [ ] Pruebas en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

**Hallazgos al ejecutar:** ninguno todavía.
