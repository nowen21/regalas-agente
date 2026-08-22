# Los entregables documentales del ciclo de vida del software

**Qué es esto.** La lista canónica de documentos que la ingeniería de software (familias IEEE e ISO) exige entregar a lo largo del ciclo, guardada aquí para el análisis en curso de `plantillas/ciclo-vida-proyectos/` (2026-08-21, pedido del usuario: «agregue esa lista a un .md para que no se nos pierda»). **No es norma del estándar todavía**: es material de análisis; lo que de acá se vuelva regla o molde sigue su procedimiento (`20·M14`).

**La idea de fondo que la acompaña** (del usuario, mismo día): cada entregable se **alimenta en su etapa** mientras el trabajo avanza, de modo que cuando el proyecto está listo, «generar los `.docx`» es solo darle forma final a un expediente que ya está escrito. El inventario de funcionalidades que madura hasta manual (`02·F26`) es el primer caso de ese patrón.

---

## La lista canónica, etapa por etapa

### 1. Concepción e inicio

| Entregable | Qué contiene | Norma de referencia |
|---|---|---|
| Documento de visión / propuesta | El problema, los objetivos, el alcance preliminar | — |
| Inventario de funcionalidades | Todo lo que se va a construir, con estado por ítem, aprobado por el usuario | Propio del estándar (`02·F26`) |
| Estudio de factibilidad | Viabilidad técnica, económica y de plazos; alternativas evaluadas | — |
| Acta de constitución y plan de proyecto | Autorización, cronograma, recursos, riesgos | IEEE 1058 |

### 2. Requisitos

| Entregable | Qué contiene | Norma de referencia |
|---|---|---|
| SRS · Especificación de Requisitos de Software | Requisitos funcionales y no funcionales, con identificador, prioridad y criterio de aceptación | IEEE 830 · ISO/IEC/IEEE 29148 |
| Matriz de trazabilidad de requisitos | De dónde viene cada requisito y dónde se implementa | ISO/IEC/IEEE 29148 |

### 3. Diseño

| Entregable | Qué contiene | Norma de referencia |
|---|---|---|
| SDD · Documento de Diseño de Software | Arquitectura, componentes, diseño detallado | IEEE 1016 |
| Modelo de datos y diccionario de datos | Entidades, relaciones, cada campo explicado | — |
| Diseño de interfaz / prototipos | Pantallas, navegación, flujos | — |
| Registro de decisiones de arquitectura | Cada decisión con sus alternativas y su porqué | ADR |

### 4. Construcción

| Entregable | Qué contiene | Norma de referencia |
|---|---|---|
| Documentación técnica del código y de las API | Contratos, convenciones, cómo se extiende | — |

### 5. Pruebas

| Entregable | Qué contiene | Norma de referencia |
|---|---|---|
| Plan de pruebas | Estrategia, casos, cobertura, criterios de salida | ISO/IEC/IEEE 29119-3 |
| Especificación de casos de prueba | Cada caso con pasos y resultado esperado | ISO/IEC/IEEE 29119-3 |
| Informe de ejecución y resultados | Qué se corrió y qué dio, con veredicto por criterio | ISO/IEC/IEEE 29119-3 |
| Registro de defectos | Cada defecto con severidad, estado y cierre | — |

### 6. Entrega y despliegue

| Entregable | Qué contiene | Norma de referencia |
|---|---|---|
| Manual de instalación y despliegue | Cómo se pone en marcha, paso a paso, con reversión | — |
| Manual de usuario | Cómo se usa, escrito para quien usa | ISO/IEC 26514 |
| Manual técnico y de operación | Respaldos, recuperación, monitoreo, para quien mantiene | — |
| Notas de versión | Qué trae cada versión entregada | — |
| Acta de entrega / aceptación | La firma del cliente sobre lo recibido | — |

### 7. Mantenimiento

| Entregable | Qué contiene | Norma de referencia |
|---|---|---|
| Registro de cambios (changelog) | Qué cambió, cuándo y por qué | — |
| Bitácoras de operación | Qué pasa en producción día a día | — |
| Informes de incidentes / postmortem | Qué falló, por qué y qué se corrigió de fondo | — |
| Plan de mantenimiento | Cómo se sostiene y evoluciona lo entregado | — |

---

## El cruce preliminar contra Cimiento (borrador del análisis, 2026-08-21)

| Estado | Entregables |
|---|---|
| ✅ **Existe como molde vivo** | Propuesta (`planteamiento.md`), inventario (`inventario-funcionalidades.md`), épicas/HU con CA, especificación por módulo, plan de trabajo, plan de pruebas, informe de resultados, ADR, cierre de fase, changelog (`CHANGELOG.md` + `versiones`), postmortem, checklist de despliegue |
| ⚠ **Existe repartido, sin consolidado** | SRS (vive en épicas y HU, sin documento único), matriz de trazabilidad (vive por fase en `13·DOC11`, sin vista de proyecto), documento de arquitectura (hay ADR y mapa de dependencias, no el SDD consolidado) |
| ✅ **Molde escrito el 2026-08-21** (frente 2, moldes 12 a 22 del ciclo) | Estudio de factibilidad, acta de constitución/plan de proyecto, modelo de datos y diccionario, diseño de interfaz, documentación de API, manual de instalación, manual técnico/operación, notas de versión, acta de entrega, bitácora de operación, plan de mantenimiento |
| 🔁 **Sin molde a propósito** | Manual de usuario (es el inventario madurado) y las vistas que el generador armará: SRS consolidado, matriz de trazabilidad, registro de defectos consolidado, documento de arquitectura |
| ✅ **El mapa de completitud existe** (2026-08-21) | `validar.py expediente --raiz <proyecto>`: qué entregables hay, cuáles faltan, cuántos espacios «...» le quedan a cada uno y cuál declara no aplicar. Informa, no detiene |
| 🔧 **No existe la pieza** | El generador de las vistas consolidadas y el `.docx`; su casa natural es la interfaz del pendiente 75, y exige una decisión: la dependencia para escribir `.docx` (python-docx) vive en la interfaz, no en `validadores/` |

## La decisión del usuario — 2026-08-21: sin excepciones

**Todos los entregables del ciclo son obligatorios en todo proyecto.** El ciclo del desarrollo de software no hace excepciones y Cimiento tampoco: no hay entregables «opt-in por envergadura». Lo que la envergadura ajusta es la **profundidad** (en un proyecto chico el estudio de factibilidad es una página), nunca la **existencia**. Y el entregable sin materia no se omite: existe y declara «No aplica porque...» con su porqué, el mismo patrón de `02·F14` en los planes. El agente propuso clasificarlos en obligatorios/por-naturaleza/por-contexto y el usuario lo corrigió: «no debe decidir, debe tenerlos».

Sigue siendo de diseño (no de existencia) qué entregables se **alimentan a mano** y cuáles son **vistas que el generador arma** desde las fuentes vivas (SRS consolidado, matriz de trazabilidad, registro de defectos, y posiblemente el SDD desde los ADR): en ambos casos el entregable existe; cambia de dónde sale.

---

**Lo abierto del análisis** (decisiones del usuario, sin tomar):

1. Si la carpeta agrupa solo el camino del ciclo o reorganiza `plantillas/` completa; y si los moldes se numeran por estación.
2. Cómo llega el cambio a los 9 proyectos instalados (MAYOR con reinstalación, o redirecciones).
3. La forma del generador `.docx` y del mapa de completitud (conecta con el [pendiente 75](../pendientes/hecho/los-proyectos-se-administran-desde-cimiento.md): la interfaz es candidata natural a mostrarlo y generarlo).
