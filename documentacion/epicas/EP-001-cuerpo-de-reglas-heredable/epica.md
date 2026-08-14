# EP-001 — Cuerpo de reglas heredable y en capas

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | EP-001 |
| **Brief de origen** | [brief.md](../../../brief.md) |
| **Iniciativa** | Que una IA que programa trabaje siempre igual |
| **Producto** | Estándar de agente para desarrollo de software |
| **Tipo** | Técnica (habilitadora) |
| **Prioridad** | Must |
| **Estimación** | L |
| **Horizonte** | Primera entrega |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Propuesta |

## 2. Resumen ejecutivo

Hoy no hay ningún documento que le diga a la IA cómo se trabaja. Cada chat empieza en blanco y la persona vuelve a explicar lo mismo: que no toque datos reales, que no publique sin permiso, que escriba pruebas, que documente la decisión. Cuando se le olvida explicar algo, la IA decide por su cuenta.

Esta épica construye ese documento: un cuerpo de reglas escritas que la IA lee antes de actuar. Las reglas no se copian dentro de cada proyecto. Viven en un solo lugar y los proyectos las heredan, de modo que corregir una regla la corrige en todos.

Las reglas se organizan en capas para que lo que protege datos y publicaciones no lo pueda aflojar nadie, y lo demás sí se pueda ajustar cuando un proyecto tenga una razón.

## 3. Problema y oportunidad

### 3.1 Situación actual

Las instrucciones viven en la cabeza de la persona y se repiten en cada chat. Cuando se repiten mal o se olvidan, la IA reinventa el diseño, contradice lo que ya se había decidido o hace algo que no se puede deshacer.

### 3.2 Impacto de no hacerlo

Todo lo demás que se quiera construir queda sin piso. No se puede comprobar el cumplimiento de algo que no está escrito, no se puede versionar, y no se puede heredar de un proyecto a otro.

### 3.3 Evidencia

| Fuente | Hallazgo |
|---|---|
| Trabajo previo con la IA en varios proyectos | La misma instrucción se repitió chat tras chat, y las veces que se omitió hubo una decisión que hubo que deshacer |
| Sesiones donde se tocó configuración sensible | Sin una regla escrita, la IA asume que puede |

## 4. Objetivo y propuesta de valor

**Objetivo.** Que exista un cuerpo de reglas escrito, único, agnóstico del lenguaje y del framework, que cualquier proyecto herede sin copiarlo.

**Hipótesis de valor.** Si las reglas están escritas y la IA las lee antes de actuar, dos sesiones distintas del mismo proyecto van a resolver igual el mismo caso. Se sabrá cuando una decisión tomada en enero se sostenga en una sesión de marzo sin que nadie la vuelva a explicar.

### 4.1 Beneficios esperados

| Beneficiario | Beneficio | Tipo |
|---|---|---|
| Quien trabaja con la IA | Deja de repetir instrucciones en cada chat | Cualitativo |
| Proyecto nuevo | Arranca con todo lo aprendido en los anteriores | Cualitativo |
| Proyecto viejo | Una corrección de regla le llega sin tocarle nada | Cualitativo |

## 5. Alcance

### 5.1 Dentro del alcance

- Reglas de comportamiento de la IA y de trabajo de ingeniería, que sirvan a cualquier lenguaje y cualquier framework.
- Capas con precedencia declarada: un núcleo que nadie sobrescribe y convenciones ajustables por proyecto.
- Un formato fijo de regla: identificador propio, una sola exigencia, ejemplo de lo incorrecto y de lo correcto, dependencias declaradas.
- La regla que gobierna cómo se escriben las reglas.
- El mecanismo por el que un proyecto declara sus ajustes de capa propia sin tocar el cuerpo central.

### 5.2 Fuera del alcance

- Reglas que solo sirvan a un lenguaje, a un framework o a un cliente.
- Comprobar automáticamente que las reglas se cumplan. Eso es EP-004.
- Numerar versiones y avisar de desactualización. Eso es EP-002.

### 5.3 Diferido

- Reglas opcionales de temas que todavía no tocan estos proyectos, como despliegue, observabilidad o registros inmutables. Se retoman cuando un proyecto real las necesite.

### 5.4 Alcance funcional completo

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Finalidad | Que la IA tenga qué leer antes de actuar, y que ese texto sea el mismo para todos los proyectos |
| 2 | Actores | Quien escribe reglas (una persona), quien las lee y aplica (la IA), quien las cita (especificaciones, commits, trabajo cerrado) |
| 3 | Información | Cada regla se identifica por un capítulo y un identificador propio, y lleva su exigencia, su ejemplo y sus dependencias |
| 4 | Campos | Una regla tiene campos definidos: identificador, título, exigencia, ejemplo incorrecto, ejemplo correcto, dependencias, excepciones, si es comprobable. El detalle de cada campo baja a la historia de usuario |
| 5 | Validaciones | El identificador es único y no repite el prefijo del capítulo; la exigencia es una sola; el ejemplo está presente; la dependencia apunta a una regla que existe |
| 6 | Reglas de negocio | Una regla nueva solo existe si hay un criterio que la respalde; un tema tiene un solo capítulo dueño; antes de crear una regla se busca si ya existe |
| 7 | Estados y transiciones | Una regla está vigente o derogada. De vigente pasa a derogada, nunca a borrada |
| 8 | Operaciones | Crear regla, corregir su redacción, derogarla, moverla de capítulo, declarar que depende de otra |
| 9 | Restricciones | No se borra ni se renumera ninguna regla; no entra al cuerpo central nada que dependa de un lenguaje o de un cliente |
| 10 | Relaciones | Una regla puede depender de otra y puede tener excepciones declaradas. Los capítulos se citan entre sí |
| 11 | Consultas | Se necesita poder listar las reglas de un capítulo y encontrar una por su identificador |
| 12 | Mensajes | No aplica porque no hay interfaz de usuario en esta épica |
| 13 | Errores | Una cita a una regla que no existe, o a una derogada, tiene que notarse |
| 14 | Permisos | No aplica porque el control lo da el repositorio, no el sistema |
| 15 | Auditoría | Cada cambio de regla queda en el historial del repositorio |
| 16 | Resultado final | La épica está completa cuando un proyecto puede leer el cuerpo de reglas desde un solo lugar, con sus capas y su precedencia, y ninguna regla vive duplicada |

**Detalle adicional**

| # | Pregunta | Respuesta |
|---|---|---|
| 22 | Configurabilidad | Un proyecto ajusta las convenciones desde su propia capa, sin editar el cuerpo central |
| 25 | Convivencia | No reemplaza nada. Es lo primero que existe |
| 26 | Idioma | Español de Colombia, escrito para que lo entienda quien no sabe del tema |

## 6. Usuarios y actores

| Actor | Rol en el proceso | Necesidad principal |
|---|---|---|
| La persona que define el estándar | Escribe, corrige y deroga reglas | Que la regla quede escrita una sola vez y en el lugar correcto |
| La IA | Lee las reglas y las aplica | Encontrar la regla que aplica al caso, sin ambigüedad |
| Un proyecto | Hereda las reglas | Recibir el cuerpo completo sin copiarlo |

**Volumetría estimada.** Varias decenas de capítulos y algunos cientos de reglas. Un solo usuario que escribe.

## 7. Criterios de aceptación de la épica

- [ ] **CAE-01** Existe un cuerpo de reglas agnóstico del lenguaje y del framework, con capas y precedencia declarada.
- [ ] **CAE-02** Ninguna regla del núcleo se puede aflojar desde la capa de un proyecto ni desde una instrucción del chat.
- [ ] **CAE-03** Toda regla tiene identificador único y estable, una sola exigencia y ejemplo de lo incorrecto y de lo correcto.
- [ ] **CAE-04** Un proyecto puede declarar sus ajustes propios sin editar el cuerpo central.
- [ ] **CAE-05** Existe la regla que gobierna cómo se escriben las demás.

## 8. Métricas de éxito

| Métrica | Línea base | Meta | Cuándo se mide | Dónde |
|---|---|---|---|---|
| Instrucciones que hay que repetir en un chat nuevo | Todas, hoy | Ninguna que ya esté escrita como regla | Al terminar la épica | Observación de una sesión real |
| Reglas duplicadas en dos capítulos | Sin medir | Cero | Al terminar la épica | Revisión del cuerpo |

## 9. Historias de usuario

| ID | Título | Prioridad | Estimación |
|---|---|---|---|
| [HU-001](HU-001-formato-unico-de-regla/HU-001-formato-unico-de-regla.md) | Formato único para escribir una regla | Must | M |
| [HU-002](HU-002-capas-y-precedencia/HU-002-capas-y-precedencia.md) | Capas de reglas y orden de precedencia | Must | S |
| [HU-003](HU-003-nucleo-que-no-se-sobrescribe/HU-003-nucleo-que-no-se-sobrescribe.md) | El núcleo de reglas que no se sobrescribe | Must | M |
| [HU-004](HU-004-conducta-de-la-ia/HU-004-conducta-de-la-ia.md) | Reglas de conducta de la IA | Must | M |
| [HU-005](HU-005-convenciones-de-ingenieria/HU-005-convenciones-de-ingenieria.md) | Convenciones de ingeniería agnósticas | Must | L |
| [HU-006](HU-006-capa-propia-del-proyecto/HU-006-capa-propia-del-proyecto.md) | La capa propia de cada proyecto | Must | M |
| [HU-007](HU-007-regla-de-las-reglas/HU-007-regla-de-las-reglas.md) | La regla que gobierna cómo se escriben las reglas | Must | M |
| [HU-008](HU-008-derogacion-sin-borrar/HU-008-derogacion-sin-borrar.md) | Derogar una regla sin borrarla ni renumerarla | Must | S |

Sin estimar en puntos todavía.

## 10. Consideraciones técnicas

### 10.1 Componentes afectados

| Componente | Impacto | Observaciones |
|---|---|---|
| Cuerpo de reglas | Nuevo | Es lo que crea esta épica |
| Capa de proyecto | Nuevo | Solo el mecanismo, no el contenido de ningún proyecto |

### 10.2 Decisiones de arquitectura

- Las reglas son archivos de texto plano en el repositorio, no una base de datos ni un servicio. Se leen sin herramientas y se versionan con el mismo historial del código.
- El identificador de la regla es estable de por vida, porque el trabajo cerrado la cita por ese nombre.

### 10.4 Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| Legibilidad | Lo entiende quien no sabe del tema |
| Idioma | Español de Colombia, sin las marcas que delatan generación automática |
| Portabilidad | No depende de ningún lenguaje ni framework |

## 11. Dependencias

Ninguna. Es la primera épica: todas las demás dependen de esta.

## 12. Riesgos

| ID | Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|---|
| R-01 | Que entre al cuerpo central una regla que solo sirve a un stack | Alta | Alto | La regla de las reglas exige que sea agnóstica antes de aceptarla |
| R-02 | Que el cuerpo crezca tanto que la IA no lo lea completo | Media | Alto | Un tema, un capítulo, un dueño. Nada duplicado |
| R-03 | Que dos reglas se contradigan | Media | Alto | Precedencia declarada y dependencias explícitas entre reglas |

## 13. Supuestos y restricciones

**Supuestos**

- Quien escribe las reglas tiene la experiencia de los proyectos donde nació cada una.
- La IA lee archivos de texto del repositorio al abrir sesión.

**Restricciones**

- Una sola persona escribe. No hay equipo ni presupuesto.
- Todo tiene que servir a cualquier proyecto, sin importar el lenguaje.

## 14. Hoja de ruta

| Fase | Contenido | HU |
|---|---|---|
| Fase 1 | El molde y las capas | HU-001, HU-002, HU-007 |
| Fase 2 | El núcleo y la conducta | HU-003, HU-004 |
| Fase 3 | Las convenciones de ingeniería | HU-005 |
| Fase 4 | La capa de proyecto y la derogación | HU-006, HU-008 |

## 15. Definition of Ready

- [ ] Alcance delimitado, dentro y fuera
- [ ] Formato de regla acordado
- [ ] Historias identificadas

## 16. Definition of Done

- [ ] Todas las historias obligatorias aceptadas
- [ ] Criterios de aceptación verificados
- [ ] Ninguna regla del cuerpo depende de un lenguaje o de un cliente
- [ ] Ninguna regla duplica a otra

## 17. Bitácora de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-13 | Ing. José Dúmar Jiménez Ruíz | Creación de la épica desde el brief |
