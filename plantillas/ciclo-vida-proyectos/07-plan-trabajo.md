# Plan de Trabajo · Fase «A-EP01-HU03-Descripción» (módulo «M»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba acepta el alcance y el costo. El requisito vive en la HU, el detalle de las pruebas en el `plan_pruebas` de la misma fase, y lo que quedó hecho en el `funcionalidad_implementada.md` del cierre.

> Todo documento creado con esta plantilla se redacta aplicando estas reglas. Esta nota se borra al llenarla.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |

> Plantilla del `plan_trabajo` de una fase. Responde las 13 preguntas de [`02·F14`](../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) sobre una línea base verificada ([`02·F16`](../../base/02-flujo-de-trabajo/reglas/F16-declara-los-cinco-componentes-de-cada-intervencion-del-plan.md), [`02·F17`](../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)). Se guarda en la carpeta de la fase (ruta `02·F12.13`, identificador `02·F12.6`) como `plan_trabajo.md`, junto con su `plan_pruebas`. No se toca código hasta que los dos estén aprobados ([`02·F4`](../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)).
>
> Al llenarla se reemplazan los `«…»`, se borran las secciones *(opcional)* que no apliquen y se borran todas las notas como esta. El párrafo «Para qué sirve este documento» se queda: le dice a quien abra el plan dentro de un año qué está leyendo.

## 0. Identificación y origen  ·  [`02·F14`](../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

> Identifica la fase (su identificador, la épica, la HU, el módulo, la fecha y la rama), dice de dónde sale y lista los CA de la HU que se compromete a cumplir.

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `«A-EP01-HU03-Descripción»` |
| **Épica** | `EP«01»` |
| **HU** | `HU«03»`, una sola (`F12.1`) |
| **Módulo** | «M» ([`13·DOC13`](../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)) |
| **Especificación del módulo** | «enlace a la especificación · [`02·F2`](../../base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md)» |
| **Fecha apertura** | AAAA-MM-DD |
| **Rama** | `«feature/<identificador-de-fase>»` |
| *(opcional)* Sprint · Dev · Revisor · QA | «…» |

**ORIGEN** ([`13·DOC12`](../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

> El ORIGEN dice de dónde sale la fase, qué la motivó y qué relación tiene con las fases que ya existen, para que quien la consulte después sepa si continúa un trabajo previo o empieza uno nuevo. Se elige una de las tres opciones:
> - Modifica fase(s): la fase retoma una o varias fases existentes. Se dice cuáles, con su identificador, y qué retoma de cada una: lo que dejó pendiente (gap) o lo que quedó comprometido para después (promesa).
> - Funcionalidad nueva: la fase agrega algo que no existía y no retoma ninguna fase. Se dice qué introduce que no estaba en el roadmap, es decir, en lo que el proyecto tenía previsto construir.
> - Híbrido: la fase hace las dos cosas. Se dice qué fases modifica y qué funcionalidad nueva introduce.

- Modifica fase(s): «cuáles y qué gap o promesa retoma», con la referencia al cierre de análisis ([`13·DOC8`](../../base/13-documentacion/reglas/DOC8-cierra-todo-analisis-con-su-tabla-de-decisiones.md)) si aplica.
- Funcionalidad nueva: «qué introduce que no estaba en el roadmap».
- Híbrido: «qué fases modifica y qué funcionalidad nueva introduce».

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

> Es la lista de criterios de aceptación de la HU que la fase se compromete a cumplir, cada uno con su estado: ☐ mientras está pendiente y ☑ cuando quedó verificado con evidencia. Todos son de la misma HU (`02·F12.1`). Si la HU tiene varias fases, cada una lista solo los CA que le tocan, y desde la HU se ve qué fase cumple cada CA.

| CA de `HU«03»` que cierra esta fase | Estado |
|---|---|
| CA-01 | ☐ |
| CA-02 | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

> Dice qué busca lograr la fase y hasta dónde llega.

**Objetivo:** ejecutar y verificar los CA de la sección 0 hasta dejarlos cumplidos, con su evidencia en la sección 5.

> El objetivo es el resultado que debe quedar logrado al terminar la fase: qué debe existir, estar disponible o funcionar.

**Resumen de CA a cubrir:**

> Reúne los criterios de aceptación y los requisitos no funcionales de la fase, cada uno con su escenario (camino feliz, error o caso borde), su tipo y su complejidad.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | «Camino feliz» | Funcional | Media |
| CA-02 | «Validación o error» | Funcional | Baja |
| CA-03 | «Caso borde» | Funcional | Alta |
| RNF-01 | «Rendimiento o seguridad» | No funcional | Media |

**Fuera de alcance:**

> Es lo que la fase no hace, aunque alguien podría esperar que sí. Si se va a hacer más adelante, se dice en qué fase.

- «Lo que no se aborda aquí y a qué fase se pasa, si aplica.»

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

> Describe cómo está el proyecto antes de tocarlo, medido contra el repositorio real antes de escribir el plan. No se admiten `(o donde esté)`, `(o similar)`, `TBD` ni `?`: lo que no se puede verificar va como duda en la sección 2.7, no como suposición.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

> Es la lista exacta de archivos que la fase crea o modifica. Fuera de ella no se toca ningún archivo (`02·F8`).

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `«ruta/exacta»` | Nuevo / Modificar | BD / Modelo / Servicio / Endpoint / UI / Test | |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md) (obligatoria si se cambian contratos de código existente)

> Cuando un cambio altera el contrato de un archivo de código (una columna, un método, una relación), esta matriz lista todos los archivos que dependen de él y dejarían de funcionar. Esos archivos también entran en la sección 2.1, y el que no se arregle en esta fase se declara en «Fuera de alcance». Si la fase no cambia contratos, se escribe «No aplica».

| Archivo a refactorizar | Cambio de contrato | Archivos que dependen (rompen) | Dónde rompe |
|---|---|---|---|
| `«archivo A»` | «elimina columna X · renombra método Y · cambia cardinalidad» | `«B» · «C»` | `B: lee X` · `C: carga relación Y` |

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

> Son las rutas o servicios que la fase crea o cambia, y quién puede usarlos: si piden autenticación, qué permiso exigen y sobre qué datos actúan. Si no hay servicios, se escribe «No aplica».

| Método + ruta | Autenticación | Permiso | Alcance |
|---|---|---|---|
| `«VERBO» /...` | «sí o no» | `«permiso»` | «propio o global» |

Contrato de API, si aplica:

```http
«MÉTODO» /api/.../«recurso»
Request:  { }
Response 200: { }
Errores:  400 | 401 | 403 | 404 | 422
```

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

> Dice dónde encuentra el usuario final lo que la fase construye. Si no hay pantalla, se escribe «No aplica» con su motivo.

- Dónde queda accesible al usuario final: «menú, navegación, tablero o enlace desde otra vista, con el archivo de navegación real».

### 2.5 Permisos / roles a sembrar  ·  [`02·F14`](../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q8

> Son los permisos o roles nuevos que hay que crear para que la funcionalidad se pueda usar, con la nomenclatura del proyecto. Si no hay, se escribe «Ninguno».

- «Permisos o roles nuevos.»

### 2.6 Decisiones técnicas

> Registra cada decisión, la alternativa que se descartó y el motivo. La decisión que no es obvia se registra también como señal ([`13·DOC5`](../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)).

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| | | |

### 2.7 Dudas por resolver antes de codificar

> Son las preguntas que deben responderse antes de construir. Ninguna tarea empieza mientras tenga una duda abierta que la bloquee.

| # | Duda | A quién se consulta | Estado |
|---|---|---|---|
| 1 | | usuario / PO | Pendiente / Resuelta |

## 3. Desglose de tareas por criterio de aceptación

> Divide el trabajo en tareas de 4 horas o menos, agrupadas por el CA que cumplen. «Depende de» ordena la ejecución y «Ev.» remite a la evidencia de la sección 5.
>
> Cada `CA-0N` y cada `RNF-0N` se escribe como enlace a su exigencia en la HU, aquí y en las secciones 0 y 5: el plan se lee al lado de la historia, no de memoria.
>
> La tabla no lleva columna de estado. El plan se aprueba y no se vuelve a tocar: el avance en vivo va en `estado-fase.md` §1.2, y lo que se hizo de verdad en `funcionalidad_implementada.md` §2.2. Marcar el avance aquí pisa el plan aprobado y deja sin contra qué comparar.

### CA-01 · «Nombre del escenario»

> Agrupa las tareas que cumplen el CA-01 de la HU, el camino feliz. Cada fila es una tarea con su capa, su estimación, la tarea de la que depende y la evidencia que deja.

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Crear migración `«nombre»` | BD | 1 h | — | |
| T-02 | Definir modelo o entidad | Backend | 1 h | T-01 | |
| T-03 | Implementar lógica en servicio | Backend | 3 h | T-02 | |
| T-04 | Exponer endpoint y validaciones | Backend | 2 h | T-03 | |
| T-05 | Prueba del servicio | Test | 2 h | T-03 | EV-01 |
| T-06 | Consumir API desde la UI | Frontend | 2 h | T-04 | |
| T-07 | Construir vista o componente | Frontend | 3 h | T-06 | EV-02 |

### CA-02 · «Nombre del escenario: validación o error»

> Agrupa las tareas que cumplen el CA-02 de la HU: las validaciones y el manejo de errores.

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-08 | Validaciones de entrada | Backend | 2 h | T-04 | |
| T-09 | Manejo y mensajes de error en UI | Frontend | 2 h | T-07 | EV-03 |
| T-10 | Prueba de caso negativo | Test | 1 h | T-08 | EV-03 |

### RNF · Requisitos no funcionales

> Agrupa las tareas que cumplen los requisitos no funcionales de la HU, con la categoría de cada uno: seguridad, auditoría o rendimiento, entre otras.

| ID | Tarea | Categoría | Est. | Ev. |
|---|---|---|:--:|---|
| T-11 | Verificar autorización por rol | Seguridad | 1 h | EV-04 |
| T-12 | Registrar evento en bitácora | Auditoría | 1 h | EV-05 |
| T-13 | Medir respuesta con «n» registros | Rendimiento | 1 h | EV-06 |

**Total estimado:** «suma» h

## 4. Secuencia de ejecución

> Define el orden de las tareas: cuáles van una tras otra (la ruta crítica) y cuáles pueden avanzar al mismo tiempo. Solo se tocan los archivos de la sección 2.1 ([`02·F8`](../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)); si aparece uno nuevo, se detiene el trabajo, se reporta y se amplía el plan con la aprobación del usuario.

**Ruta crítica:** T-01, T-02, T-03, T-04, T-06, T-07
**Paralelizables:** «tareas independientes que pueden avanzar al mismo tiempo».

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

> Dice cómo se comprueba cada CA y dónde queda su evidencia. Un CA no se marca cumplido sin evidencia. Una fase con un CA en rojo no pasa la puerta de verificación, pero sí puede cerrar, declarando el rojo y a dónde se pasó: cerrar no es aprobar. Los casos de prueba van en el `plan_pruebas`.

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Prueba y verificación manual | EV-01, EV-02 | | ☐ |
| CA-02 | Prueba de caso negativo | EV-03 | | ☐ |
| CA-03 | Prueba con datos límite | EV-07 | | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Reporte de pruebas | `«ruta o enlace»` |
| EV-02 | Captura | `«enlace»` |

## 6. Datos y ambiente de prueba

> Dice dónde y con qué datos se prueba. Nunca se usan datos reales ([`00·N4`](../../base/00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada), [`08·T4`](../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)). El detalle de casos y técnicas va en el `plan_pruebas`.

| Elemento | Detalle |
|---|---|
| Ambiente | «dónde corren las pruebas» |
| Usuarios de prueba | «rol y credencial de prueba, sin claves reales» |
| Datos precargados | «script o conjunto de datos» |

## 7. Reversión / rollback  ·  [`02·F14`](../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

> Es el plan para deshacer lo hecho si algo sale mal. Cada cambio destructivo dice cómo se revierte.

«Reversión del commit, rollback del esquema (`down()`), backfill inverso, feature flag o script de emergencia.»

## 8. Producción y migración incremental  ·  [`02·F14`](../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

> Dice qué pasa con lo que ya está en uso: si el cambio obliga a migrar datos o proyectos, y cómo se hace sin romper lo existente. Se asume que lo que se toca probablemente está en producción.

- Aditivo (columna o tabla nueva): migración nueva, con backfill si aplica.
- Renombrar: migración nueva y reversible. No se edita la migración original de una fase cerrada.
- Eliminar, o cambiar el tipo de un campo con datos: se avisa el riesgo concreto antes de aplicarlo, y lleva su `down()` que reconstruye.
- «Se declara la que aplica, o "No aplica porque...".»

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

> Lista, por su identificador, las reglas del estándar y del proyecto que la fase sigue, para que cada decisión se pueda rastrear.

- Base: «por ejemplo [`02·F8`](../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `04·S...`, [`08·T4`](../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar), [`13·DOC11`](../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)».
- Proyecto: «por ejemplo `P<N>` de `.agente/reglas-proyecto.md`».

## 10. Riesgos y bloqueos

> Registra lo que puede frenar o afectar la fase, su impacto, la acción prevista y si sigue abierto.

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | | Retrasa T-0x | | Abierto / Cerrado |

## 11. Definition of Done

> Es la lista de condiciones que deben cumplirse para dar la fase por terminada.

- [ ] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [ ] Requisitos no funcionales validados
- [ ] Pruebas de la fase en verde, solo las suites que la fase toca ([`02·F5`](../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md))
- [ ] Trazabilidad de la especificación a la implementación sin faltantes ([`13·DOC11`](../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md))
- [ ] Sin errores de linter ni de análisis estático (`07`)
- [ ] Documentación, índices y mapas del proyecto actualizados (`13`)
- [ ] Señales registradas ([`13·DOC5`](../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md))
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))
- *(opcional)* Aceptada por el Product Owner o el usuario

## 12. Seguimiento diario  ·  *(opcional, para equipos)*

> Registra el avance día a día. El avance en vivo va en `estado-fase.md`.

| Fecha | Tareas cerradas | Avance CA | Bloqueos | Ajuste al plan |
|---|---|---|---|---|
| AAAA-MM-DD | T-01, T-02 | CA-01 en curso | Ninguno | — |

## 13. Cierre

> El cierre de la fase no se escribe aquí: va en `funcionalidad_implementada.md` (plantilla `funcionalidad-implementada.md`), con qué se hizo de cada tarea (§2.2), qué se probó (§3), qué se decidió (§5) y qué deuda quedó (§6). Este plan se queda como se aprobó, para comparar lo que se dijo contra lo que pasó.
