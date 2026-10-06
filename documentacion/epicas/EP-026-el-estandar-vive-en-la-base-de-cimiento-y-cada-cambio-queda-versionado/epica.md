# EP-026 · El estándar vive en la base de Cimiento y cada cambio queda versionado

> El alcance, los criterios y las HU salen de la propuesta final y de «Lo que se tiene que hacer» del [análisis 1 del pendiente 132](../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md), aprobado el 2026-10-06. Los campos que no son alcance (tipo, prioridad, estimación, riesgos, supuestos) son propuesta del agente.

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | EP-026 |
| **Planteamiento de origen** | El [pendiente 132](../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/pendiente.md), V2: el estándar vive en la base de Cimiento y cada cambio queda versionado |
| **Iniciativa / Objetivo estratégico** | Que el estándar se administre desde la pantalla de Cimiento y que todo lo que cambia en él tenga historia |
| **Producto / Sistema** | Cimiento, la aplicación Django de `proyectos/cimiento/` |
| **Tipo** | Técnica (habilitadora) |
| **Prioridad** | Must |
| **Estimación** | XL: diez HU, más la HU-041 de EP-001 |
| **Horizonte** | N/A |
| **Product Owner** | Ing. José Dúmar Jiménez Ruíz |
| **Tech Lead / Arquitecto** | N/A |
| **Estado** | En curso |

## 2. Resumen ejecutivo

El estándar deja de escribirse en archivos. Las reglas, las palabras clave, el mapa de tareas y todo lo que se pueda administrar pasan a la base de Cimiento, y se manejan y se aprueban desde su pantalla. Los archivos de `base/` se quedan quietos en la versión 55.1.0, para que git conserve la historia anterior.

Todo lo que cambia en Cimiento queda en su historia: quién, cuándo, cómo estaba, cómo quedó y por qué. Cada cambio sube una versión: la del estándar o la del proyecto al que pertenece. La base se copia sola cada día.

## 3. Problema y oportunidad

### 3.1 Situación actual

El estándar vive en archivos de `base/` y la configuración de cada proyecto en la base. La base guarda los cambios de tres maneras distintas: los niveles de las reglas sin versión, las suspensiones sin rastro al editarlas y los ajustes sin ningún rastro.

### 3.2 Impacto de no hacerlo

Lo que no tiene historia no se puede revisar ni deshacer. Y mientras el estándar viva en dos sitios, uno de los dos se desactualiza.

### 3.3 Evidencia

| Fuente | Hallazgo |
|---|---|
| [H-1 de la sesión del 2026-10-06](../../../historico-chat/resumenes/2026-10-06/sesion.md) | Los ajustes de capa 1 y 2 reemplazan el valor viejo sin dejar rastro |

## 4. Objetivo y propuesta de valor

**Objetivo:** que el estándar se administre desde la pantalla de Cimiento y que todo cambio quede con su historia y su versión.

**Hipótesis de valor:**
> Creemos que un estándar guardado en la base, con un solo registro de cambios, para quien mantiene Cimiento y sus proyectos, logrará que ningún cambio se pierda y que cada proyecto sepa qué cambió. Lo sabremos cuando todo cambio hecho en la pantalla aparezca en la historia con su versión.

### 4.1 Beneficios esperados

| Beneficiario | Beneficio | Tipo |
|---|---|---|
| Quien mantiene Cimiento | Ve y deshace cualquier cambio | Cualitativo |
| Los proyectos que heredan | Saben qué cambió en el estándar y en su propia configuración | Cualitativo |

## 5. Alcance

### 5.1 Dentro del alcance

- Un solo registro de cambios para todo lo que cambia en Cimiento, también usuarios, grupos, gasto, señales y estado del análisis.
- Versión del estándar y versión de cada proyecto.
- El estándar 55.1.0 entra a la base; los enganches lo leen de ahí.
- La pantalla administra y autoriza todo, también lo que propone el agente.
- Un botón sube a git lo que cambió en Cimiento.
- Lo que reporta un proyecto llega como pendiente del estándar.
- Vista previa de las reglas de un mensaje y capítulos opt-in desde la pantalla.
- Copia diaria de la base.

### 5.2 Fuera del alcance

- Guardar lo que solo se mira (acuerdo 21).
- Las plantillas: siguen en archivos (acuerdo 5).

### 5.3 Diferido a fases posteriores

Ninguno.

### 5.4 Alcance funcional completo

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Finalidad | Administrar el estándar desde la pantalla y guardar la historia de todo lo que cambia |
| 2 | Actores | Administrador (cambia y aprueba), consulta (solo ve) y el agente (propone y lee) |
| 3 | Información | Regla, palabra clave, tarea, capítulo, ajuste, cambio registrado, versión del estándar, versión de cada proyecto, copia de la base |
| 4 | Campos | Cada entidad tiene campos de identificación, texto, estado y fechas; se especifican en cada HU |
| 5 | Validaciones | Ningún identificador se reutiliza; un cambio sin motivo no se guarda; la ruta de la copia está autorizada |
| 6 | Reglas de negocio | Todo cambio sube una versión; el reporte de un proyecto sube la del estándar cuando se corrige |
| 7 | Estados | Propuesta, aprobada; vigente, derogada; cambio «sin subir» o subido |
| 8 | Operaciones | Crear, cambiar, derogar, aprobar, deshacer, subir a git, ver la historia |
| 9 | Restricciones | Nada se borra; nadie edita a mano los archivos de `base/`; sin base no se trabaja |
| 10 | Relaciones | Un cambio pertenece a una versión, y la versión al estándar o a un proyecto |
| 11 | Consultas | Historia de cambios con filtros; versiones; vista previa de las reglas de un mensaje |
| 12 | Mensajes | Aviso de versión atrasada a los proyectos; aviso de base caída |
| 13 | Errores | Base sin conexión, git que falla, copia que no se puede restaurar: se informan y no se guarda nada a medias |
| 14 | Permisos | Por grupo de Django: administrador y consulta |
| 15 | Auditoría | Todo lo que cambia: quién, cuándo, antes, después, por qué y versión |
| 16 | Resultado final | El estándar se lee y se cambia solo en la base, con su historia completa |
| 17 a 26 | Ciclo de vida y demás | Migración: el estándar 55.1.0 pasa a la base (HU-003); la copia diaria protege la historia (HU-010); el resto no aplica porque Cimiento corre en una máquina para una persona |

## 6. Usuarios y actores

| Actor | Rol en el proceso | Necesidad principal |
|---|---|---|
| Administrador | Cambia y aprueba el estándar y la configuración | Que todo cambio quede con su historia |
| Consulta | Mira la historia y las versiones | Saber qué cambió |
| El agente | Lee el estándar de la base y propone cambios | Recibir las reglas vigentes |

**Volumetría estimada:** una persona; unas 260 reglas; decenas de proyectos.

## 7. Criterios de aceptación de la épica

- [ ] **CAE-01** — Todo cambio guardado en Cimiento aparece en su historia con quién, cuándo, antes, después, por qué y versión.
- [ ] **CAE-02** — El agente recibe las reglas leídas de la base, y sin base el freno no deja trabajar.
- [ ] **CAE-03** — El estándar se cambia y se aprueba solo desde la pantalla; los archivos de `base/` no cambian después de 55.1.0.
- [ ] **CAE-04** — La base tiene una copia de cada uno de los últimos 7 días, y una de ellas se restauró en una prueba.

## 8. Métricas de éxito

| Métrica | Línea base | Meta | Plazo de medición | Instrumento |
|---|---|---|---|---|
| Cambios sin historia | Los ajustes de capa 1 y 2 | Ninguno | 30 días | La historia de cambios |
| Archivos de `base/` cambiados después de 55.1.0 | N/A | Ninguno | 30 días | git |

## 9. Historias de usuario

| ID | Título | Prioridad | Estimación | Sprint | Estado |
|---|---|---|---|---|---|
| [HU-001](HU-001-todo-cambio-guardado-en-la-base-deja-quien-cuando-antes-despues-y-por-que/HU-001-todo-cambio-guardado-en-la-base-deja-quien-cuando-antes-despues-y-por-que.md) | «Título» | «Prioridad» | «Estimación» | «…» | «…» |
| [HU-002](HU-002-cada-proyecto-tiene-su-version-y-el-estandar-la-suya/HU-002-cada-proyecto-tiene-su-version-y-el-estandar-la-suya.md) | «Título» | «Prioridad» | «Estimación» | «…» | «…» |
| [HU-003](HU-003-el-estandar-55-1-0-entra-a-la-base/HU-003-el-estandar-55-1-0-entra-a-la-base.md) | «Título» | «Prioridad» | «Estimación» | «…» | «…» |
| [HU-004](HU-004-los-enganches-leen-el-estandar-de-la-base/HU-004-los-enganches-leen-el-estandar-de-la-base.md) | «Título» | «Prioridad» | «Estimación» | «…» | «…» |
| [HU-005](HU-005-el-estandar-se-administra-y-se-autoriza-desde-la-pantalla/HU-005-el-estandar-se-administra-y-se-autoriza-desde-la-pantalla.md) | «Título» | «Prioridad» | «Estimación» | «…» | «…» |
| [HU-006](HU-006-los-archivos-de-base-quedan-quietos-en-la-version-55-1-0/HU-006-los-archivos-de-base-quedan-quietos-en-la-version-55-1-0.md) | «Título» | «Prioridad» | «Estimación» | «…» | «…» |
| [HU-007](HU-007-un-boton-de-la-pantalla-guarda-en-git-lo-que-cambio-en-cimiento/HU-007-un-boton-de-la-pantalla-guarda-en-git-lo-que-cambio-en-cimiento.md) | «Título» | «Prioridad» | «Estimación» | «…» | «…» |
| [HU-008](HU-008-lo-que-un-proyecto-reporta-llega-al-estandar-como-pendiente/HU-008-lo-que-un-proyecto-reporta-llega-al-estandar-como-pendiente.md) | «Título» | «Prioridad» | «Estimación» | «…» | «…» |
| [HU-009](HU-009-la-pantalla-muestra-que-reglas-llegarian-con-un-mensaje-y-prende-los-capitulos-opt-in/HU-009-la-pantalla-muestra-que-reglas-llegarian-con-un-mensaje-y-prende-los-capitulos-opt-in.md) | «Título» | «Prioridad» | «Estimación» | «…» | «…» |
| [HU-010](HU-010-la-base-se-copia-sola-en-una-carpeta-hermana-de-agente/HU-010-la-base-se-copia-sola-en-una-carpeta-hermana-de-agente.md) | «Título» | «Prioridad» | «Estimación» | «…» | «…» |

## 10. Consideraciones técnicas

### 10.1 Arquitectura y componentes afectados

| Componente | Impacto | Observaciones |
|---|---|---|
| `proyectos/cimiento/core/` | Nuevo y modificado | Registro de cambios, versiones, estándar en la base, pantallas |
| `core/herramientas/recuperar.py`, `mapa_tareas.py`, `core/enganches/` | Modificado | Leen de la base |
| `base/` | Sin cambio desde 55.1.0 | Queda quieta |

### 10.2 Decisiones de arquitectura (ADR)

Ninguna aparte: las decisiones están en «Lo acordado» del análisis 1 del pendiente 132.

### 10.3 Integraciones

Ninguna.

### 10.4 Requisitos no funcionales transversales

| Categoría | Requisito |
|---|---|
| **Rendimiento** | Los enganches leen las reglas de la base en cada mensaje sin arrancar Django |
| **Seguridad** | La copia de la base va sin claves (`00·N6`) |
| **Disponibilidad** | Sin base, el freno no deja trabajar |
| **Auditoría y trazabilidad** | Todo lo que cambia queda en la historia |
| **Escalabilidad** | N/A: una máquina |
| **Accesibilidad** | N/A |

### 10.5 Deuda técnica generada o pagada

- Se paga: los ajustes y las suspensiones dejan de cambiar sin rastro.

## 11. Cumplimiento y normativa

N/A.

## 12. Dependencias

| ID | Dependencia | Tipo | Responsable | Fecha requerida | Estado |
|---|---|---|---|---|---|
| DEP-01 | EP-001·HU-041: las reglas reconocen la base como fuente del estándar | Interna | Agente | Antes de HU-003 | Bloqueante |

## 13. Riesgos

| ID | Riesgo | Probabilidad | Impacto | Mitigación | Responsable |
|---|---|:--:|:--:|---|---|
| R-01 | Perder la base es perder toda la historia | Baja | Alto | Copia diaria y prueba de restauración (HU-010) | Agente |
| R-02 | Leer la base en cada mensaje vuelve lentos los enganches | Media | Medio | Se mide en HU-004 | Agente |

## 14. Supuestos y restricciones

**Supuestos**
- Una sola máquina y una sola persona.

**Restricciones**
- Django con plantillas propias; lo nuevo va como clases en `proyectos/cimiento/core/`.

## 15. Hoja de ruta

| Orden | HU | Depende de | Por qué en ese orden | Estado |
|---|---|---|---|---|
| 1 | EP-001·HU-041 | Ninguna | La regla tiene que permitirlo antes de construir lo que la usa | Propuesta |
| 2 | HU-001 | Ninguna | Es el registro que usan todas las demás | Propuesta |
| 3 | HU-002 | HU-001 | La versión sube con cada cambio registrado | Propuesta |
| 4 | HU-010 | HU-001 | Protege la historia apenas empieza a guardarse | Propuesta |
| 5 | HU-003 | EP-001·HU-041, HU-002 | Sin el estándar en la base no hay qué administrar ni qué leer | Propuesta |
| 6 | HU-004 | HU-003 | Necesita el estándar en la base | Propuesta |
| 7 | HU-005 | HU-003 | Necesita el estándar en la base y el registro | Propuesta |
| 8 | HU-006 | HU-003 | Se congelan cuando el estándar ya está en la base | Propuesta |
| 9 | HU-007 | HU-005 | Se aprueba desde la pantalla | Propuesta |
| 10 | HU-008 | HU-002, HU-005 | Necesita las dos versiones y la pantalla | Propuesta |
| 11 | HU-009 | HU-004 | Usa la lectura desde la base | Propuesta |

## 16. Estrategia de entrega

| Tema | Cómo |
|---|---|
| Despliegue | En la máquina del usuario, HU por HU |
| Migración de datos | El estándar 55.1.0 pasa de `base/` a la base (HU-003) |
| Plan de reversión | Revertir el commit de la HU; los archivos de `base/` siguen en 55.1.0 |
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

- [Análisis 1 del pendiente 132](../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md)

## 20. Bitácora de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | Agente | Creación de la épica desde el análisis aprobado |
