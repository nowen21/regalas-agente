# EP-028 · Las pantallas orientan al usuario sin que conozca cómo está armado el sistema

> El alcance, los criterios y las HU salen de la propuesta final y de «Lo que se tiene que hacer» del [análisis 1 del pendiente 137](../../../historico-chat/resumenes/2026-10-07/pendientes/137-las-pantallas-de-cimiento-no-orientan-al-usuario/analisis-1.md), aprobado el 2026-10-07. Los campos que no son alcance (tipo, prioridad, estimación, riesgos, supuestos) son propuesta del agente.

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | EP-028 |
| **Planteamiento de origen** | El [pendiente 137](../../../historico-chat/resumenes/2026-10-07/pendientes/137-las-pantallas-de-cimiento-no-orientan-al-usuario/pendiente.md), V2: las pantallas orientan al usuario sin que tenga que conocer cómo está armado el sistema |
| **Iniciativa / Objetivo estratégico** | Que Cimiento, como línea base, dé el ejemplo de pantallas que orientan solas |
| **Producto / Sistema** | El estándar (capítulo `17` y su guía) y Cimiento |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | XL: seis HU |
| **Horizonte** | N/A |
| **Product Owner** | Ing. José Dúmar Jiménez Ruíz |
| **Tech Lead / Arquitecto** | N/A |
| **Estado** | Terminada |

## 2. Resumen ejecutivo

El capítulo `17 · Interfaz` deja de ser opt-in y rige para todo proyecto con pantallas, con una regla nueva: la pantalla orienta sola. El estándar gana una guía de diseño de pantallas, única para todos, que pide aprovechar a fondo la plantilla que cada proyecto ya tiene instalada. Cimiento es el primero que la cumple: su menú, su inicio, «Propuestas», sus formularios y sus tablas se arreglan con los recursos de Tabler.

## 3. Problema y oportunidad

### 3.1 Situación actual

Pantallas fuera del menú, «Propuestas» sin mostrar qué cambió, preguntas de versión que no se entienden, formularios sin ayuda y tablas que no se ordenan ni se filtran; y un estándar sin guía ni regla obligatoria que lo exija.

### 3.2 Impacto de no hacerlo

Lo que no se encuentra no se usa, y la línea base no puede exigir lo que ella misma no cumple.

### 3.3 Evidencia

| Fuente | Hallazgo |
|---|---|
| [H-14 de la sesión del 2026-10-06](../../../historico-chat/resumenes/2026-10-06/sesion.md) | El usuario no encontró cómo aprobar las propuestas de la EP-027·HU-007 |

## 4. Objetivo y propuesta de valor

**Objetivo:** que toda pantalla oriente a su usuario, empezando por las de Cimiento.

**Hipótesis de valor:**
> Creemos que una guía única y una regla obligatoria, cumplidas primero por Cimiento con los recursos de su plantilla, lograrán que quien usa un proyecto encuentre cada función sin conocer cómo está armado. Lo sabremos cuando se pueda aprobar una propuesta en Cimiento sin que nadie explique el camino.

### 4.1 Beneficios esperados

| Beneficiario | Beneficio | Tipo |
|---|---|---|
| Quien usa Cimiento | Encuentra y usa cada función sin preguntar | Cualitativo |
| Los proyectos que heredan | Tienen una guía y una regla con qué diseñar sus pantallas | Cualitativo |

## 5. Alcance

### 5.1 Dentro del alcance

- El capítulo `17` obligatorio para todo proyecto con pantallas, su regla nueva y el ajuste de `17·I5`.
- La guía de diseño de pantallas, con las 14 secciones del encargo `prompts/prompt-guia-estilo.md`.
- El menú, el inicio, «Propuestas», las preguntas de versión, los formularios y las tablas de Cimiento, con los recursos de Tabler.

### 5.2 Fuera del alcance

- Diseñar una plantilla propia para cada proyecto (acuerdo 3).

### 5.3 Diferido a fases posteriores

- Que Scilit y los demás proyectos apliquen la guía: lo hace cada uno en su propio trabajo.

## 6. Usuarios y actores

| Actor | Rol en el proceso | Necesidad principal |
|---|---|---|
| Quien usa Cimiento | Administra el estándar y los proyectos | Encontrar y usar cada función |
| Quien construye pantallas | Diseña la pantalla de un proyecto | Saber qué componente usar y cómo |

## 7. Criterios de aceptación de la épica

- [ ] **CAE-01** — El capítulo `17` rige para todo proyecto con pantallas y trae la regla de que la pantalla orienta sola.
- [ ] **CAE-02** — La guía cubre las 14 secciones del encargo.
- [ ] **CAE-03** — Toda pantalla de Cimiento se alcanza desde el menú o desde lo que la pide, y usa los recursos de Tabler.

## 8. Métricas de éxito

| Métrica | Línea base | Meta | Plazo de medición | Instrumento |
|---|---|---|---|---|
| Pantallas de Cimiento fuera del menú | 5 | 0 | Al cerrar la HU-003 | Revisión del menú |
| Formularios de Cimiento con ayuda | 2 de 15 | 15 de 15 | Al cerrar la HU-005 | Prueba de la ayuda |

## 9. Historias de usuario

| ID | Título | Prioridad | Estimación | Sprint | Estado |
|---|---|---|---|---|---|
| [HU-001](HU-001-el-capitulo-17-rige-para-todo-proyecto-con-pantallas-y-exige-que-la-pantalla-oriente-sola/HU-001-el-capitulo-17-rige-para-todo-proyecto-con-pantallas-y-exige-que-la-pantalla-oriente-sola.md) | «Título» | «Prioridad» | «Estimación» | «…» | Terminada |
| [HU-002](HU-002-el-estandar-tiene-su-guia-de-diseno-de-pantallas/HU-002-el-estandar-tiene-su-guia-de-diseno-de-pantallas.md) | «Título» | «Prioridad» | «Estimación» | «…» | Terminada |
| [HU-003](HU-003-el-menu-y-el-inicio-de-cimiento-llevan-a-cada-funcion/HU-003-el-menu-y-el-inicio-de-cimiento-llevan-a-cada-funcion.md) | «Título» | «Prioridad» | «Estimación» | «…» | Terminada |
| [HU-004](HU-004-la-pantalla-de-propuestas-y-las-preguntas-de-version-se-entienden/HU-004-la-pantalla-de-propuestas-y-las-preguntas-de-version-se-entienden.md) | «Título» | «Prioridad» | «Estimación» | «…» | Terminada |
| [HU-005](HU-005-cada-formulario-de-cimiento-trae-su-ayuda/HU-005-cada-formulario-de-cimiento-trae-su-ayuda.md) | «Título» | «Prioridad» | «Estimación» | «…» | Terminada |
| [HU-006](HU-006-las-tablas-de-cimiento-usan-los-recursos-de-tablas-de-la-plantilla/HU-006-las-tablas-de-cimiento-usan-los-recursos-de-tablas-de-la-plantilla.md) | «Título» | «Prioridad» | «Estimación» | «…» | Terminada |
| [HU-007](HU-007-cimiento-usa-adminlte-4/HU-007-cimiento-usa-adminlte-4.md) | «Título» | «Prioridad» | «Estimación» | «…» | Terminada |

## 10. Consideraciones técnicas

### 10.1 Arquitectura y componentes afectados

| Componente | Impacto | Observaciones |
|---|---|---|
| Capítulo `17` del estándar, en la base | Modificado | Se propone y se aprueba en la pantalla |
| `proyectos/cimiento/templates/` y las plantillas de cada app | Modificado | Con los componentes de Tabler |
| `core/proyectos/ajustes.py` | Modificado | Sale el ajuste `opt_in_17` |

### 10.2 Decisiones de arquitectura (ADR)

Ninguna aparte: están en «Lo acordado» del análisis 1 del pendiente 137.

### 10.3 Integraciones

Ninguna.

### 10.4 Requisitos no funcionales transversales

| Categoría | Requisito |
|---|---|
| **Accesibilidad** | La de `17·I3` y la guía |
| **Rendimiento** | Sin dependencias nuevas: Tabler ya está instalado |
| **Seguridad** | N/A |
| **Disponibilidad** | N/A |
| **Auditoría y trazabilidad** | Los cambios del estándar quedan en la historia |
| **Escalabilidad** | N/A |

### 10.5 Deuda técnica generada o pagada

- Se paga: los formularios nacidos después de la EP-025·HU-018 reciben su ayuda.

## 11. Cumplimiento y normativa

N/A.

## 12. Dependencias

| ID | Dependencia | Tipo | Responsable | Fecha requerida | Estado |
|---|---|---|---|---|---|
| DEP-01 | La aprobación en «Propuestas» de los cambios del capítulo `17` | Interna | Usuario | Antes de cerrar la HU-001 | Resuelta |

## 13. Riesgos

| ID | Riesgo | Probabilidad | Impacto | Mitigación | Responsable |
|---|---|:--:|:--:|---|---|
| R-01 | La HU-001 se aprueba en la misma pantalla de «Propuestas» que arregla la HU-004 | Alta | Medio | Se acompaña paso a paso desde el menú (S-348) | Agente |

## 14. Supuestos y restricciones

**Supuestos**
- Cimiento sigue usando Tabler.

**Restricciones**
- Sin dependencias nuevas.

## 15. Hoja de ruta

| Orden | HU | Depende de | Por qué en ese orden | Estado |
|---|---|---|---|---|
| 1 | HU-001 | Ninguna | La regla tiene que existir antes de lo que la cumple | Terminada |
| 2 | HU-002 | HU-001 | Las pantallas se arreglan siguiendo la guía | Terminada |
| 3 | HU-003 | HU-002 | Sigue la guía | Terminada |
| 4 | HU-004 | HU-002 | Sigue la guía | Terminada |
| 5 | HU-005 | HU-002 | Sigue la guía | Terminada |
| 6 | HU-006 | HU-002 | Sigue la guía | Terminada |

## 16. Estrategia de entrega

| Tema | Cómo |
|---|---|
| Despliegue | En la máquina del usuario, HU por HU |
| Migración de datos | Sale el ajuste `opt_in_17` de la base |
| Plan de reversión | Revertir el commit de la HU; los cambios del estándar se deshacen desde «Historia» |
| Capacitación y gestión del cambio | N/A |
| Soporte post-despliegue | N/A |

## 17. Definition of Ready (épica)

- [x] Problema y objetivo validados con el negocio
- [x] Alcance delimitado (dentro y fuera)
- [x] Métricas de éxito definidas y medibles
- [x] Historias de usuario identificadas
- [x] Dependencias y riesgos registrados
- [x] Viabilidad técnica evaluada
- [x] Capacidad confirmada

## 18. Definition of Done (épica)

- [ ] Todas las HU obligatorias completadas y aceptadas
- [ ] Criterios de aceptación de la épica verificados
- [ ] Requisitos no funcionales validados
- [ ] Documentación técnica entregada
- [ ] Métricas midiendo

## 19. Referencias

- [Análisis 1 del pendiente 137](../../../historico-chat/resumenes/2026-10-07/pendientes/137-las-pantallas-de-cimiento-no-orientan-al-usuario/analisis-1.md)
- [El encargo de la guía](../../../prompts/prompt-guia-estilo.md)

## 20. Bitácora de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-07 | Agente | Creación de la épica desde el análisis aprobado |
| 2026-10-07 | Agente | Terminadas las seis HU: la épica queda terminada |
