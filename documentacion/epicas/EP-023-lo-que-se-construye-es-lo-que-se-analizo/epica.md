# EP-023 · Lo que se construye es lo que se analizó

> El alcance, los criterios y las HU salen de la propuesta final y de «Lo que se tiene que hacer» del [análisis 1](pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-1.md) y del [análisis 2](pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-2.md). Los campos que no son alcance (tipo, prioridad, estimación, beneficios, riesgos, supuestos) son propuesta del agente y esperan la aprobación del usuario.

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | EP-023 |
| **Planteamiento de origen** | El pendiente [Lo que se construye se aparta de lo aprobado](pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/pendiente.md), V3 |
| **Iniciativa / Objetivo estratégico** | Al ejecutar un plan solo aparecen los hallazgos que no se podían prever |
| **Producto / Sistema** | Cimiento |
| **Tipo** | Técnica (habilitadora): cambia cómo trabaja el estándar, no lo que entrega un producto |
| **Prioridad** | Must: la forma de trabajo actual produce los hallazgos que esta épica quiere evitar |
| **Estimación** | L: siete HU y 41 puntos, que tocan reglas, plantillas, validadores y enganches |
| **Horizonte** | Versión 40.0.0 (análisis 1, punto 30) |
| **Product Owner** | Ing. José Dúmar Jiménez Ruíz |
| **Tech Lead / Arquitecto** | N/A |
| **Estado** | Terminada el 2026-10-03: sus siete historias cumplen |

## 2. Resumen ejecutivo

Su resultado: al ejecutar un plan solo aparecen los hallazgos que no se podían prever. Reúne en siete HU los 41 puntos de lo que se tiene que hacer de los análisis 1, 2 y 4: los 32 del análisis 1, menos el 29, que el análisis 2 superó, los 8 del análisis 2 y los 2 del análisis 4. El tercer punto del análisis 4 fue reescribir el contexto de las HU, y ya está hecho.

## 3. Problema y oportunidad

### 3.1 Situación actual

No hay un documento que fije el alcance antes de la HU. Nada obliga a que cada documento salga del anterior. Nada detiene al agente cuando trabaja fuera del plan aprobado. La plantilla del plan no permite comprobarlo con un programa. Y lo que pasa la conversación al análisis hay que configurarlo a mano para cada análisis.

### 3.2 Impacto de no hacerlo

Al ejecutar el plan aparecen hallazgos que se podían evitar, y cada uno se vuelve un pendiente más.

### 3.3 Evidencia

| Fuente | Hallazgo |
|---|---|
| [H-13 de la sesión del 2026-09-28](../../../historico-chat/resumenes/2026-09-28/sesion.md) | Lo que se construye se aparta de lo aprobado |
| [H-2 de la sesión del 2026-09-30](../../../historico-chat/resumenes/2026-09-30/sesion.md) | El enganche del análisis solo sirve para un análisis |

## 4. Objetivo y propuesta de valor

**Objetivo:** al ejecutar un plan solo aparecen los hallazgos que no se podían prever.

**Hipótesis de valor:**
> Si cada reparto de trabajo pasa por un análisis, cada documento sale del anterior y un freno detiene lo que no está en el plan, los hallazgos que salen al ejecutar cada plan bajan a los que no se podían prever. Se sabrá con el número que registra cada plan (análisis 1, punto 24).

### 4.1 Beneficios esperados

| Beneficiario | Beneficio | Tipo |
|---|---|---|
| El usuario | Lo construido es lo que aprobó | Cualitativo |
| Los proyectos que heredan Cimiento | Reciben la herramienta por el instalador, sin configurar nada a mano (análisis 2, punto 8) | Cualitativo |

## 5. Alcance

### 5.1 Dentro del alcance

Los 41 puntos de lo que se tiene que hacer, repartidos en las siete HU de la sección 9.

### 5.2 Fuera del alcance

- Los hallazgos que solo aparecen al construir, como la falla de una herramienta de terceros (análisis 1, conclusión 42).
- Un análisis entre la HU y el plan: de la HU hacia abajo no hay reparto (análisis 1, conclusión 25).

### 5.3 Diferido a fases posteriores

Ninguno.

### 5.4 Alcance funcional completo

N/A: la épica no trata de una entidad con campos, estados y operaciones. Su alcance son los 41 puntos de lo que se tiene que hacer, cada uno con su HU.

## 6. Usuarios y actores

| Actor | Rol en el proceso | Necesidad principal |
|---|---|---|
| El usuario | Plantea la necesidad y aprueba (análisis 1, conclusión 40) | Que se construya lo que aprobó |
| Claude | Ayuda a estructurar, cuestionar y definir (análisis 1, conclusión 40) | Saber cuándo se sale del plan |
| Los proyectos que heredan | Reciben la versión nueva por el instalador | No configurar nada a mano |

## 7. Criterios de aceptación de la épica

- [ ] **CAE-01**. Al ejecutar un plan solo aparecen los hallazgos que no se podían prever.
- [ ] **CAE-02**. Los 41 puntos de lo que se tiene que hacer de los análisis 1, 2 y 4 están cumplidos, cada uno en su HU.

## 8. Métricas de éxito

| Métrica | Línea base | Meta | Plazo de medición | Instrumento |
|---|---|---|---|---|
| Hallazgos que salen al ejecutar cada plan (análisis 1, punto 24) | No se mide hoy | Solo los que no se podían prever | Cada plan que cierre con la versión 40.0.0 o una posterior | El registro de cada plan |

## 9. Historias de usuario

| ID | Título | Puntos de lo que se tiene que hacer | Orden | Estado |
|---|---|---|---|---|
| [HU-001](HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes/HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes.md) | El análisis existe, tiene su forma y revisa las cuatro partes | Análisis 1: 1, 2, 3, 15, 16, 23, 30, 32. Análisis 2: 1 a 6 y 8. Análisis 4: 2 | 1 | Terminada el 2026-10-03 |
| [HU-002](HU-002-cada-documento-sale-del-anterior/HU-002-cada-documento-sale-del-anterior.md) | Cada documento sale del anterior | Análisis 1: 4, 5. Análisis 4: 1 | 3 | Terminada el 2026-10-03 |
| [HU-003](HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde/HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde.md) | El hallazgo y el pendiente tienen solo lo que les corresponde | Análisis 1: 7, 10, 11, 12, 19, 20, 21 | 4 | Terminada el 2026-10-03 |
| [HU-004](HU-004-un-hallazgo-detiene-la-ejecucion-y-vuelve-al-analisis/HU-004-un-hallazgo-detiene-la-ejecucion-y-vuelve-al-analisis.md) | Un hallazgo detiene la ejecución y vuelve al análisis | Análisis 1: 6, 13, 14, 17, 18, 24. Análisis 2: 7 | 5 | Terminada el 2026-10-03 |
| [HU-005](HU-005-nada-se-agrega-fuera-de-lo-pedido/HU-005-nada-se-agrega-fuera-de-lo-pedido.md) | Nada se agrega fuera de lo pedido | Análisis 1: 8, 22, 28 | 2 | Terminada el 2026-10-03 |
| [HU-006](HU-006-lo-aprendido-incluye-las-lecciones/HU-006-lo-aprendido-incluye-las-lecciones.md) | Lo aprendido incluye las lecciones | Análisis 1: 9 | 7 | Terminada el 2026-10-03 |
| [HU-007](HU-007-nada-se-escribe-fuera-del-plan-aprobado/HU-007-nada-se-escribe-fuera-del-plan-aprobado.md) | Nada se escribe fuera del plan aprobado | Análisis 1: 25, 26, 27, 31 | 6 | Terminada el 2026-10-03 |
| [HU-008](HU-008-aprobar-el-analisis-aprueba-lo-que-sale-de-el/HU-008-aprobar-el-analisis-aprueba-lo-que-sale-de-el.md) | «Título» | «Prioridad» | «Estimación» | «…» |

## 10. Consideraciones técnicas

### 10.1 Arquitectura y componentes afectados

Los que nombra cada punto de lo que se tiene que hacer, en su HU.

### 10.2 Decisiones de arquitectura (ADR)

Ninguna.

### 10.3 Integraciones

Ninguna.

### 10.4 Requisitos no funcionales transversales

| Categoría | Requisito |
|---|---|
| **Auditoría y trazabilidad** | Cada punto de cada documento cita de dónde sale (análisis 1, conclusión 39) |
| **Escalabilidad** | Vale para cualquier proyecto que herede Cimiento, sin importar su tamaño ni su stack (análisis 1, conclusión 37) |
| **Rendimiento, seguridad, disponibilidad y accesibilidad** | N/A |

### 10.5 Deuda técnica generada o pagada

Generada: `pendientes/` conserva pendientes con el formato viejo, y los validadores lo aceptan solo ahí (análisis 1, conclusión 38).

## 11. Cumplimiento y normativa

N/A: ninguna norma ni ley aplica (análisis 1 y análisis 2, sección del entorno).

## 12. Dependencias

| ID | Dependencia | Tipo | Responsable | Fecha requerida | Estado |
|---|---|---|---|---|---|
| DEP-01 | Las demás HU se apoyan en el análisis de la HU-001 | Interna | N/A | N/A | Bloqueante |
| DEP-02 | La HU-007 necesita que la HU-004 defina qué pasa con un hallazgo | Interna | N/A | N/A | Bloqueante |

## 13. Riesgos

| ID | Riesgo | Probabilidad | Impacto | Mitigación | Responsable |
|---|---|:--:|:--:|---|---|
| R-01 | Que el freno detenga lo que una regla ya autoriza y se aprenda a ignorar (S-086, S-108) | Media | Alto | La lista de lo autorizado, con la regla que autoriza cada entrada (análisis 1, conclusión 46) | HU-007 |
| R-02 | Que un proyecto no adopte la versión 40.0.0, que deroga `01·C14` y `13·DOC8` | Baja | Alto | `02·F22`: el proyecto que no adopte no abre ni cierra fase (análisis 1, conclusión 48) | HU-001 |
| R-03 | Que la conversación entre en un análisis ya aprobado | Baja | Medio | Se apaga con «Apruebo el análisis», que pone la marca (análisis 2, conclusión 2) | HU-001 |

## 14. Supuestos y restricciones

**Supuestos**
- Algunos hallazgos solo aparecen al construir; la épica baja los evitables, no todos (análisis 1, conclusión 42).

**Restricciones**
- Nada se renumera ni se borra: las reglas se derogan (`20·M11`).
- El análisis 1 no se toca; su punto 29 lo superan los puntos del análisis 2 (análisis 2, conclusión 9).
- Las reglas nuevas extienden lo que existe y no contradicen a otras (análisis 1, conclusión 29).

## 15. Hoja de ruta

El número identifica a la HU y no cambia; el orden de ejecución sale de las dependencias ([análisis 8](pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-8.md), conclusiones 5 y 8).

| Orden | HU | Depende de | Por qué en ese orden | Estado |
|---|---|---|---|---|
| 1 | HU-001, fases A a C | Ninguna | Las demás se apoyan en el análisis | Hecha |
| 2 | HU-005 | HU-001 | Es pequeña y ataca la causa más directa | Hecha |
| 3 | HU-002 | HU-001 | Cada documento sale del anterior | Hecha |
| 4 | HU-001, fase D | Ninguna | Todo análisis que venga usa la plantilla | Hecha |
| 5 | HU-003 | HU-001 | Da la forma del hallazgo y del pendiente que usan la HU-004 y la HU-007, y resuelve las fallas de `fases` y de `pendientes` | Hecha |
| 6 | HU-006 | HU-001, fase D | Las lecciones alimentan las recomendaciones que crea la fase D | Hecha |
| 7 | HU-004 | HU-003 | Detener la ejecución necesita la forma del hallazgo | Hecha |
| 8 | HU-007 | HU-003, HU-004 | El freno anota el hallazgo y vuelve al análisis | Hecha |

Las fechas se fijan al planear cada HU.

## 16. Estrategia de entrega

| Campo | Valor |
|---|---|
| Despliegue | El instalador lleva la herramienta a cada proyecto (análisis 2, punto 8) |
| Migración de datos | `pendientes/` queda como historia (análisis 1, punto 21) |
| Plan de reversión | Las reglas derogadas no se borran (`20·M11`), así que se pueden volver a poner en vigor |
| Capacitación y gestión del cambio | El CHANGELOG dice lo que cada proyecto tiene que hacer, citando `20·M10` y `02·F22` (análisis 1, punto 30) |
| Soporte post-despliegue | N/A |

## 17. Definition of Ready (épica)

- [x] Problema y objetivo validados: análisis 1 y 2 aprobados el 2026-10-01
- [x] Alcance delimitado: los 41 puntos, cada uno con su HU
- [x] Métricas de éxito definidas
- [ ] Historias de usuario identificadas y estimadas: identificadas, sin estimar
- [x] Dependencias y riesgos registrados
- [ ] Viabilidad técnica evaluada
- [ ] Presupuesto y capacidad confirmados: N/A

## 18. Definition of Done (épica)

- [ ] Las siete HU completadas y aceptadas
- [ ] Criterios de aceptación de la épica verificados
- [ ] Versión 40.0.0 publicada
- [ ] Aceptación formal del usuario

## 19. Referencias

| Campo | Valor |
|---|---|
| Pendiente | [Lo que se construye se aparta de lo aprobado](pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/pendiente.md) |
| Análisis | [análisis 1](pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-1.md), [análisis 2](pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-2.md), [análisis 3](pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-3.md), [análisis 4](pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-4.md) y [análisis 5](pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-5.md) |

## 20. Bitácora de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-01 | Claude, por pedido de Ing. José Dúmar Jiménez Ruíz | Creación de la épica desde la propuesta final de los análisis 1 y 2, corregida según el análisis 3 |
| 2026-10-01 | Claude, por pedido de Ing. José Dúmar Jiménez Ruíz | Suma los dos puntos del análisis 4: uno a la HU-001 y otro a la HU-002 |
| 2026-10-01 | Ing. José Dúmar Jiménez Ruíz | Aprobadas las siete HU |
