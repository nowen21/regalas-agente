# Plan de Trabajo · Fase A-EP-029-HU-008-danar-a-proposito (módulo pruebas de Cimiento)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-029-HU-008-danar-a-proposito` |
| **Épica** | `EP-029` |
| **HU** | [`HU-008`](../HU-008-un-comando-dana-el-codigo-a-proposito-y-dice-que-danos-no-detectan-las-pruebas.md), una sola (`F12.1`) |
| **Módulo** | Pruebas de Cimiento, `proyectos/cimiento/core/pruebas/` |
| **Especificación del módulo** | La HU-008 y la [épica EP-029](../../epica.md) |
| **Fecha apertura** | 2026-10-09 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 148](../../../../../historico-chat/resumenes/2026-10-08/pendientes/148-probar-que-las-pruebas-sirven-con-un-solo-comando/analisis-1.md), el 2026-10-09, en el turno 13, con la versión 56.8.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Fase nueva. Sale del análisis 1 del pendiente 148, acuerdos 1 y 2, punto 1 de «Lo que se tiene que hacer».

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-008` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-008-un-comando-dana-el-codigo-a-proposito-y-dice-que-danos-no-detectan-las-pruebas.md#ca-01--dice-qué-daños-detectan-las-pruebas-y-cuáles-no) | ☑ |
| [CA-02](../HU-008-un-comando-dana-el-codigo-a-proposito-y-dice-que-danos-no-detectan-las-pruebas.md#ca-02--el-código-queda-como-estaba-pase-lo-que-pase) | ☑ |
| [CA-03](../HU-008-un-comando-dana-el-codigo-a-proposito-y-dice-que-danos-no-detectan-las-pruebas.md#ca-03--sin-pruebas-que-pasen-no-daña-nada) | ☑ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** `manage.py danar_a_proposito --danos «archivo» --pruebas "«orden»"` daña el código según la lista, corre las pruebas con cada daño, deja todo como estaba y dice qué daños detectaron las pruebas y cuáles no.

**Fuera de alcance:** generar los daños solo; una pantalla para el comando.

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

Cimiento no tiene nada que dañe código. `core/pruebas/` corre y mide pruebas (`revisar.py`, comandos `marcar_pruebas` y `revisar_pruebas`). `core.comun.consola.preparar_salida` ya pone la consola en UTF-8. Los 19 guiones de `historico-chat/scripts/2026-08-2*/sabotaj*.py` traen la lista de daños como tuplas (nombre, archivo, texto original, texto dañado) y las lecciones que el comando resuelve de una vez.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/pruebas/danar.py` | Crear | Lógica | Leer la lista, dañar, correr, devolver y reportar |
| `proyectos/cimiento/core/pruebas/management/commands/danar_a_proposito.py` | Crear | Comando | La entrada de consola |
| `proyectos/cimiento/core/pruebas/tests_danar.py` | Crear | Test | |

### 2.2 Matriz de dependencias del refactor

No aplica.

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

No aplica: es la consola.

### 2.5 Permisos / roles a sembrar  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| La lista de daños es un JSON: una lista de objetos con `nombre`, `archivo`, `antes` y `despues` | Un formato propio por bloques | JSON guarda textos de varias líneas sin inventar reglas de escape | Propuesta del agente |
| Se detecta el daño por el código de salida de la orden, o por pasarse del tiempo | Leer el texto «OK» de la salida | El código de salida vale para cualquier lenguaje; leer el texto falló dos veces (`S-060`, `S-068`) | Acuerdo 1 |
| Los archivos que el daño crea se hallan comparando la lista de archivos de la carpeta antes y después de cada daño, sin mirar `.git`, `.venv` ni `node_modules` | Pedir la lista de rastros conocidos | El rastro de `sabotaje_e.py` no era conocido de antemano | Acuerdo 1 |
| La foto de archivos se toma después de la corrida sin daños | Antes de esa corrida | Lo que las pruebas crean siempre (cachés) no es rastro del daño | Propuesta del agente |
| Las copias van a una carpeta temporal fuera del proyecto | Junto al archivo | Una copia dentro del proyecto la verían las pruebas | Acuerdo 1 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

El comando es su propia contraria: devuelve cada archivo desde su copia y borra lo que el daño creó, dentro de la misma corrida.

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | `danar.py`: leer y revisar la lista, corrida sin daños, dañar, correr, devolver, limpiar y comprobar | Lógica | 1,5 h | — | EV-01 |
| T-02 | El comando `danar_a_proposito`, con la tabla de resultados | Comando | 0,5 h | T-01 | EV-01 |
| T-03 | Pruebas sobre un proyecto de juguete en una carpeta temporal | Test | 1 h | T-01, T-02 | EV-01 |

**Total estimado:** 3 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Pruebas de Django | EV-01 | 2026-10-09 | ☑ |
| CA-02 | Pruebas de Django | EV-01 | 2026-10-09 | ☑ |
| CA-03 | Pruebas de Django | EV-01 | 2026-10-09 | ☑ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | Una carpeta temporal con un módulo y su prueba, corrida con el Python de Cimiento |
| Usuarios de prueba | Ninguno |
| Datos precargados | Ninguno |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

No aplica: no cambia la base.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `08·T1`, `08·T8`, `00·N3`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que un daño quede puesto | El proyecto queda roto | Devolver en `try/finally` y comprobar al final cada archivo contra su copia | Abierto |
| B-02 | Que un daño cuelgue las pruebas | El comando no termina | Tiempo máximo por corrida, `--tiempo`, 600 s por defecto | Abierto |

## 11. Definition of Done

- [x] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [x] Pruebas en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

Las 3 tareas quedaron hechas el 2026-10-09, con la versión 56.8.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** DEF-01, el .pyc viejo, corregido en la fase (S-362); cerrar_fase lee un solo caso por fila de la matriz y el resultado se completó a mano.
