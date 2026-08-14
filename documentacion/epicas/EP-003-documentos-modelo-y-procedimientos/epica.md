# EP-003 — Documentos modelo y procedimientos guiados

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | EP-003 |
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

Tener reglas escritas no alcanza. Una regla dice qué se exige, pero no dice cómo se ve un documento que la cumple ni en qué orden se hacen las cosas. Sin eso, cada sesión inventa su propio formato y dos trabajos parecidos terminan documentados de forma distinta.

Esta épica entrega dos cosas que van juntas. Los documentos modelo, que son esqueletos para copiar y llenar: el brief, la épica, la historia de usuario, el plan de trabajo, el plan de pruebas, la especificación de un módulo. Y los procedimientos, que son instrucciones paso a paso que la IA sigue para producir cada uno de esos documentos y para pasar de un paso al siguiente.

El resultado es que el trabajo deja de depender de cómo la IA se sienta ese día. Sigue un libreto.

## 3. Problema y oportunidad

### 3.1 Situación actual

Cuando se le pide a la IA que documente algo, cada vez sale distinto: distinto orden, distintas secciones, distinto nivel de detalle. Comparar dos trabajos, o retomar uno viejo, cuesta más de lo que debería.

### 3.2 Impacto de no hacerlo

Las reglas quedan como buenas intenciones. Nadie sabe cómo se ve el cumplimiento, así que tampoco se puede revisar ni comprobar después.

### 3.3 Evidencia

| Fuente | Hallazgo |
|---|---|
| Documentos producidos en sesiones distintas del mismo proyecto | Mismo tipo de documento, estructuras diferentes, secciones que aparecen y desaparecen |

## 4. Objetivo y propuesta de valor

**Objetivo.** Que exista un modelo para cada documento del trabajo y un procedimiento para cada paso, de modo que dos sesiones distintas produzcan lo mismo.

**Hipótesis de valor.** Si el formato viene dado y el paso a paso está escrito, la IA deja de improvisar la forma y usa el esfuerzo en el contenido. Se sabrá cuando dos sesiones separadas produzcan documentos que se puedan comparar renglón por renglón.

### 4.1 Beneficios esperados

| Beneficiario | Beneficio | Tipo |
|---|---|---|
| Quien lee después | Encuentra siempre lo mismo en el mismo lugar | Cualitativo |
| La IA | No gasta contexto decidiendo la forma | Cualitativo |
| El proyecto | Los documentos se pueden revisar y comprobar, porque tienen forma conocida | Cualitativo |

## 5. Alcance

### 5.1 Dentro del alcance

- Documentos modelo para cada paso del trabajo, con los espacios por llenar marcados.
- Procedimientos activables para la IA, uno por rol del trabajo: analizar, proponer alcance, escribir la especificación, diseñar, planear, implementar, revisar, cerrar.
- Un procedimiento que dirija a los demás en orden y controle que no se salte un paso.
- Los puntos donde una persona tiene que aprobar antes de seguir.

### 5.2 Fuera del alcance

- Comprobar automáticamente que un documento quedó completo. Eso es EP-004.
- Llevar los modelos a cada proyecto. Eso es EP-007.
- El contenido de los documentos de un proyecto real.

### 5.3 Diferido

- Modelos de temas opcionales, como despliegue o postmortem de incidente. Se agregan cuando un proyecto los pida.

## 5.4 Alcance funcional completo

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Finalidad | Que cada documento del trabajo tenga forma conocida y cada paso tenga libreto |
| 2 | Actores | La IA, que sigue el procedimiento y llena el modelo; la persona, que aprueba en los puntos de corte |
| 3 | Información | Cada modelo define qué secciones tiene el documento y qué va en cada una; cada procedimiento define los pasos, sus entradas y su salida |
| 4 | Campos | Un modelo tiene espacios por llenar, marcados de forma que se note cuando quedaron vacíos. El detalle de cada marca baja a la historia de usuario |
| 5 | Validaciones | Un documento entregado con espacios sin llenar no está terminado; un procedimiento no arranca sin la entrada que necesita |
| 6 | Reglas de negocio | Sin especificación acordada no hay código; sin plan aprobado no hay código; el alcance se acuerda antes de descomponer |
| 7 | Estados y transiciones | Un documento está en borrador, en revisión o aprobado. Un paso del flujo está pendiente, en curso o cerrado |
| 8 | Operaciones | Copiar un modelo, llenarlo, pedir aprobación, pasar al paso siguiente, devolverse a un paso anterior |
| 9 | Restricciones | La IA no salta un paso ni aprueba en nombre de la persona |
| 10 | Relaciones | Brief da origen a épicas, la épica a historias, la historia a fases, la fase a sus planes. Cada documento apunta al de arriba y al de abajo |
| 11 | Consultas | Se necesita poder ver en qué paso va un trabajo y qué falta para cerrar |
| 12 | Mensajes | Cuando un procedimiento necesita una aprobación, lo pide en el chat y espera |
| 13 | Errores | Falta la entrada del paso, el modelo quedó incompleto, se intentó saltar una aprobación |
| 14 | Permisos | Solo la persona aprueba. La IA propone |
| 15 | Auditoría | Queda escrito qué se decidió en cada paso y quién lo aprobó |
| 16 | Resultado final | La épica está completa cuando un trabajo puede recorrerse de punta a punta usando solo los modelos y los procedimientos, sin inventar formato |

**Detalle adicional**

| # | Pregunta | Respuesta |
|---|---|---|
| 19 | Catálogos | Los modelos son el catálogo. Viven en un solo lugar y los proyectos los copian |
| 22 | Configurabilidad | Un proyecto puede agregar secciones propias a un modelo, sin quitar las que trae |
| 26 | Idioma | Español de Colombia, entendible por quien no sabe del tema |

## 6. Usuarios y actores

| Actor | Rol en el proceso | Necesidad principal |
|---|---|---|
| La IA | Sigue el procedimiento y llena el modelo | Un paso a paso sin ambigüedad |
| La persona | Aprueba en los puntos de corte | Ver lo que va a aprobar, completo y en formato conocido |
| Quien retoma el trabajo meses después | Lee los documentos | Encontrar lo mismo en el mismo lugar |

## 7. Criterios de aceptación de la épica

- [ ] **CAE-01** Existe un documento modelo para cada paso del trabajo, con los espacios por llenar marcados.
- [ ] **CAE-02** Existe un procedimiento escrito para cada rol del trabajo.
- [ ] **CAE-03** Existe un procedimiento que dirige a los demás en orden y no deja saltar pasos.
- [ ] **CAE-04** Los puntos donde aprueba una persona están declarados y la IA se detiene en ellos.
- [ ] **CAE-05** Un trabajo de prueba se recorre de punta a punta sin inventar formato.

## 8. Métricas de éxito

| Métrica | Línea base | Meta | Cuándo se mide | Dónde |
|---|---|---|---|---|
| Variación de formato entre dos documentos del mismo tipo | Alta, hoy | Ninguna en las secciones obligatorias | Al terminar la épica | Comparación de dos sesiones |
| Pasos saltados en un trabajo completo | Sin medir | Cero | Al terminar la épica | Recorrido de prueba |

## 9. Historias de usuario

| ID | Título | Prioridad | Estimación |
|---|---|---|---|
| [HU-001](HU-001-marca-de-espacio-por-llenar/HU-001-marca-de-espacio-por-llenar.md) | Definir cómo se marca un espacio por llenar en un modelo | Must | S |
| [HU-002](HU-002-modelos-del-encargo/HU-002-modelos-del-encargo.md) | Crear los modelos del encargo: brief, épica, historia de usuario | Must | M |
| [HU-003](HU-003-modelos-de-la-fase/HU-003-modelos-de-la-fase.md) | Crear los modelos de la fase: plan de trabajo, plan de pruebas, cierre | Must | M |
| [HU-004](HU-004-modelo-de-la-especificacion/HU-004-modelo-de-la-especificacion.md) | Crear el modelo de la especificación de un módulo | Must | M |
| [HU-005](HU-005-modelos-de-la-capa-de-proyecto/HU-005-modelos-de-la-capa-de-proyecto.md) | Crear los modelos de la capa de proyecto: stack, dominio, nombres propios | Must | M |
| [HU-006](HU-006-procedimientos-por-rol/HU-006-procedimientos-por-rol.md) | Escribir los procedimientos de cada rol del trabajo | Must | L |
| [HU-007](HU-007-procedimiento-que-dirige/HU-007-procedimiento-que-dirige.md) | Escribir el procedimiento que dirige a los demás y controla los cortes | Must | L |
| [HU-008](HU-008-puntos-de-aprobacion/HU-008-puntos-de-aprobacion.md) | Declarar los puntos donde aprueba una persona | Must | S |

## 10. Consideraciones técnicas

### 10.1 Componentes afectados

| Componente | Impacto | Observaciones |
|---|---|---|
| Documentos modelo | Nuevo | |
| Procedimientos | Nuevo | |
| Cuerpo de reglas | Modificado | Las reglas del flujo apuntan a estos modelos |

### 10.2 Decisiones de arquitectura

- El modelo se copia al proyecto y se llena ahí. No se llena en el lugar central, porque el contenido es de cada proyecto.
- El procedimiento es texto, no código. Lo aplica quien lo lea, sea la IA o una persona.

### 10.4 Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| Legibilidad | El modelo se entiende sin instructivo aparte |
| Portabilidad | Ningún modelo asume un lenguaje ni un framework |

## 11. Dependencias

| ID | Dependencia | Tipo | Estado |
|---|---|---|---|
| DEP-01 | EP-001, porque los modelos y procedimientos concretan las reglas del flujo | Interna | Bloqueante |

## 12. Riesgos

| ID | Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|---|
| R-01 | Que los modelos sean tan largos que nadie los llene | Alta | Alto | Cada modelo dice qué secciones se borran cuando no aplican |
| R-02 | Que el procedimiento y la regla digan cosas distintas | Media | Alto | El procedimiento cita la regla, no la repite con otras palabras |
| R-03 | Que la IA llene los espacios con relleno para pasar el trámite | Media | Alto | Los espacios sin llenar se dejan marcados, y quien revisa los ve |

## 13. Supuestos y restricciones

**Supuestos**

- La IA puede leer y seguir un procedimiento escrito en texto.

**Restricciones**

- Nada de esto puede depender de un lenguaje ni de una herramienta de gestión de proyectos.

## 14. Hoja de ruta

| Fase | Contenido | HU |
|---|---|---|
| Fase 1 | Marcas y modelos del encargo | HU-001, HU-002 |
| Fase 2 | Modelos de fase, especificación y capa de proyecto | HU-003, HU-004, HU-005 |
| Fase 3 | Procedimientos por rol | HU-006 |
| Fase 4 | Dirección del flujo y cortes de aprobación | HU-007, HU-008 |

## 15. Definition of Ready

- [ ] Lista de documentos del trabajo acordada
- [ ] Lista de roles del trabajo acordada

## 16. Definition of Done

- [ ] Todas las historias obligatorias aceptadas
- [ ] Un trabajo de prueba recorrido de punta a punta
- [ ] Ningún modelo ni procedimiento asume un stack

## 17. Bitácora de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-13 | Ing. José Dúmar Jiménez Ruíz | Creación de la épica desde el brief |
