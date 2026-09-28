# Estado de fase · Fase «A-EP01-HU03-Descripción» (módulo «M»)   ·   `[CAPA 3]`

> Todo documento creado con esta plantilla se redacta aplicando estas reglas. Esta nota se borra al llenarla.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Plantilla del `estado-fase` de una fase: el punto de control del orquestador (`sdd-orchestrator`), que guarda el estado de la fase para que sobreviva a la compactación del contexto, donde se pierden las decisiones. Se escribe o se actualiza en cada puerta que pasa, y al reanudar el director lo lee y sigue desde la última puerta pasada. Se guarda en `documentacion/<modulo>/estado-fase.md`.
>
> Al llenarla se reemplazan los `«…»` y se borran todas las notas como esta.

## 0. Identificación

> Identifica la fase, su módulo y los documentos de los que sale, con la fecha de la última actualización.

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `«A-EP01-HU03-Descripción»` |
| **Módulo** | «M» |
| **Planteamiento / Épica / HU** | «punteros» |
| **Última actualización** | AAAA-MM-DD |

## 1. En qué estación va

> Dice en qué estación de la cadena va la fase y cuál fue la última puerta que pasó. La casilla de cada estación se marca cuando la fase pasa su puerta.

**Estación actual:** «número y nombre». **Última puerta pasada:** «N».

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☐ |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☐ |
| 3 | Escritor de épica | 👤 épica aprobada | ☐ |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☐ |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☐ |
| 6 | Diseñador | diseño coherente | ☐ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☐ |
| 8 | Implementador | implementado + pruebas verdes | ☐ |
| 9 | Verificador | trazabilidad sin faltantes | ☐ |
| 10 | Crítico | sin hallazgos graves | ☐ |
| 11 | Cierre documental + señales | docs y señales al día | ☐ |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

## 1.1 Veredicto de las pruebas

> Es el veredicto de las pruebas de la fase, del que sale el estado de la estación 9. Se copia del §6 del `resultado_pruebas.md` de la fase; no se escribe de memoria ni porque se vio funcionar.

| Campo | Valor |
|---|---|
| **Concepto** | «Cumple / No cumple / Todavía no se ejecutó». Sin estado intermedio: lo que falta hace que sea No cumple |
| **CA cumplidos** | «cuántos de cuántos» |
| **CA en "No"** | «cuáles. Con uno solo, la fase no cierra» |
| **Defectos abiertos aceptados** | «cuáles y quién los aceptó» |
| **Fuente** | «`resultado_pruebas.md`» |

## 1.2 Avance de las tareas del plan

> Es el seguimiento en vivo de las tareas mientras la fase corre. Los identificadores se copian del `plan_trabajo` §3, que no se toca. Al cerrar, esto se consolida en el `funcionalidad_implementada.md` §2.2, que es la verificación de registro.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Uno de [los estados del glosario](«RUTA-ESTANDAR»/base/glosario.md#5--en-qué-estado-está-algo) para una tarea: Pendiente, En curso, Terminada o Bloqueada | «si está bloqueada, por qué» |

**Hechas:** «N de N». **Bloqueadas:** «cuáles».

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

> Registra cada decisión o aprendizaje de la fase que no se recupera leyendo el código, con la señal donde quedó. Si no hubo, se escribe «Ninguna».

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| | |

## 3. Pendiente / preguntas abiertas

> Lista lo que detiene o condiciona el avance de la fase. Si no hay nada abierto, se escribe «Ninguno».

- «Qué falta, qué se está esperando (una aprobación, una respuesta del usuario, una dependencia).»

## 4. Si se bloqueó

> Se llena cuando la fase está detenida. Si no lo está, se escribe «No aplica».

- **Estación:** «N». **Motivo:** «pruebas rojas / hallazgo grave del Crítico / alcance rechazado / dependencia faltante». **Qué falta para desbloquear:** «…».
