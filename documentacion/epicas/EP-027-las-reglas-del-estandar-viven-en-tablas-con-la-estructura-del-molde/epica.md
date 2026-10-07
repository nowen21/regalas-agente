# EP-027 · Las reglas del estándar viven en tablas con la estructura del molde

> El alcance, los criterios y las HU salen de la propuesta final y de «Lo que se tiene que hacer» del [análisis 1 del pendiente 136](../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/analisis-1.md), aprobado el 2026-10-07. Los campos que no son alcance (tipo, prioridad, estimación, riesgos, supuestos) son propuesta del agente.

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | EP-027 |
| **Planteamiento de origen** | El [pendiente 136](../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/pendiente.md), V2: las reglas del estándar viven en tablas con la estructura del molde |
| **Iniciativa / Objetivo estratégico** | Que cada regla se guarde, se muestre y se relacione por lo que es, y no como un texto entero |
| **Producto / Sistema** | Cimiento, la aplicación Django de `proyectos/cimiento/` |
| **Tipo** | Técnica (habilitadora) |
| **Prioridad** | Must |
| **Estimación** | XL: siete HU |
| **Horizonte** | N/A |
| **Product Owner** | Ing. José Dúmar Jiménez Ruíz |
| **Tech Lead / Arquitecto** | N/A |
| **Estado** | En curso |

## 2. Resumen ejecutivo

Cada regla del estándar deja de guardarse como un texto entero y pasa a una tabla, con una casilla por cada parte de su molde: código, título, marca, exigencia, dependencias, excepción, ejemplo, quién la hace cumplir, si es validable, a qué tareas aplica, qué deja escribir y sello. Las reglas de cada proyecto van en la misma tabla.

La pantalla lista las reglas por capítulo, con su nombre, y cada regla muestra sus relaciones con las demás y enlaces que abren. El agente sigue recibiendo el mismo texto, armado desde las tablas.

## 3. Problema y oportunidad

### 3.1 Situación actual

Las 269 reglas están en 152 documentos de texto, en `estandar_documento`, con solo `ruta` y `contenido`. La pantalla las lista por ruta, sus 2.697 enlaces no abren, las propuestas, la historia y la memoria muestran rutas o números, y las reglas de cada proyecto siguen en archivos.

### 3.2 Impacto de no hacerlo

Quien administra el estándar no reconoce las reglas ni sigue sus relaciones, y cada pantalla o programa que necesita una parte de la regla la busca dentro del texto.

### 3.3 Evidencia

| Fuente | Hallazgo |
|---|---|
| [H-12 de la sesión del 2026-10-06](../../../historico-chat/resumenes/2026-10-06/sesion.md) | La pantalla del estándar lista rutas de archivo y no nombres de reglas |

## 4. Objetivo y propuesta de valor

**Objetivo:** que cada regla viva en casillas que siguen su molde, y que la pantalla la muestre por su nombre y con sus relaciones.

**Hipótesis de valor:**
> Creemos que guardar las reglas en casillas, para quien mantiene el estándar, logrará que una regla se encuentre y se entienda sin leer archivos. Lo sabremos cuando la pantalla muestre las 269 reglas por su nombre y el agente reciba el mismo texto que hoy.

### 4.1 Beneficios esperados

| Beneficiario | Beneficio | Tipo |
|---|---|---|
| Quien mantiene el estándar | Encuentra y relaciona las reglas por su nombre | Cualitativo |
| Los proyectos que heredan | Sus reglas propias se administran como las del estándar | Cualitativo |

## 5. Alcance

### 5.1 Dentro del alcance

- Tablas de capítulo, regla, dependencia, tarea y sello, con las casillas del molde.
- El paso de las 269 reglas y del mapa de tareas a las tablas, sin perder nada.
- El texto del agente, del freno y de `ver_estandar` armado desde las tablas.
- La pantalla por capítulo, la página de cada regla con sus relaciones y enlaces que abren.
- Nombres legibles en las propuestas, la historia y la memoria.
- Las reglas de cada proyecto en la misma tabla.
- `20·M5` y `20·M9` hablan de casillas y no de archivos.

### 5.2 Fuera del alcance

- La librería `markdown` (acuerdo 3).
- Las plantillas: siguen en archivos.

### 5.3 Diferido a fases posteriores

Ninguno.

### 5.4 Alcance funcional completo

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Finalidad | Guardar, mostrar y relacionar cada regla por sus partes |
| 2 | Actores | Administrador (cambia), consulta (mira) y el agente (lee) |
| 3 | Información | Capítulo, regla, dependencia, tarea, sello |
| 4 | Campos | Los del molde de la regla; se especifican en la HU-001 |
| 5 | Validaciones | El código no se repite ni cambia (`20·M4`); solo tres tipos de dependencia (`20·M7`); solo tres marcas (`20·M5`) |
| 6 | Reglas de negocio | Todo cambio sube versión y queda en la historia (`20·M10`) |
| 7 | Estados | Vigente o derogada, por la marca |
| 8 | Operaciones | Crear, cambiar, derogar, ver, relacionar |
| 9 | Restricciones | Nada se borra (`20·M11`) |
| 10 | Relaciones | Una regla pertenece a un capítulo, o a un proyecto; se relaciona con otras y con tareas |
| 11 | Consultas | Lista por capítulo; página de cada regla con sus relaciones |
| 12 | Mensajes | Los de siempre al agente, con la misma forma |
| 13 | Errores | Una regla que no pasa a las tablas detiene el paso y se informa |
| 14 | Permisos | Por grupo de Django: administrador y consulta |
| 15 | Auditoría | La historia de cambios de la EP-026 |
| 16 | Resultado final | Las reglas viven en tablas y se ven por su nombre |
| 17 a 26 | Ciclo de vida y demás | Migración: las 269 reglas pasan a las tablas (HU-002); el resto no aplica porque Cimiento corre en una máquina para una persona |

## 6. Usuarios y actores

| Actor | Rol en el proceso | Necesidad principal |
|---|---|---|
| Administrador | Cambia las reglas | Encontrarlas por su nombre |
| Consulta | Mira las reglas | Entender qué exige cada una y con cuáles se relaciona |
| El agente | Lee las reglas | Recibir el mismo texto que hoy |

**Volumetría estimada:** una persona; 269 reglas; decenas de proyectos.

## 7. Criterios de aceptación de la épica

- [ ] **CAE-01** — Las 269 reglas están en las tablas, y armadas desde ellas dan el mismo texto que hoy.
- [ ] **CAE-02** — La pantalla lista las reglas por capítulo y por su nombre, sin rutas.
- [ ] **CAE-03** — Cada regla muestra sus dependencias y las reglas que nombra, y sus enlaces abren.
- [ ] **CAE-04** — Las reglas de cada proyecto viven en la misma tabla.

## 8. Métricas de éxito

| Métrica | Línea base | Meta | Plazo de medición | Instrumento |
|---|---|---|---|---|
| Reglas en las tablas | 0 de 269 | 269 de 269 | Al cerrar la HU-002 | Prueba de paso |
| Enlaces que abren | 0 de 2.697 | Todos los que apuntan a una regla | Al cerrar la HU-004 | Prueba de la pantalla |

## 9. Historias de usuario

| ID | Título | Prioridad | Estimación | Sprint | Estado |
|---|---|---|---|---|---|
| [HU-001](HU-001-las-reglas-tienen-sus-tablas-con-las-casillas-del-molde/HU-001-las-reglas-tienen-sus-tablas-con-las-casillas-del-molde.md) | «Título» | «Prioridad» | «Estimación» | «…» | «…» |
| [HU-002](HU-002-las-269-reglas-pasan-a-las-tablas-sin-perder-nada/HU-002-las-269-reglas-pasan-a-las-tablas-sin-perder-nada.md) | «Título» | «Prioridad» | «Estimación» | «…» | «…» |
| [HU-003](HU-003-el-texto-que-recibe-el-agente-se-arma-desde-las-tablas/HU-003-el-texto-que-recibe-el-agente-se-arma-desde-las-tablas.md) | «Título» | «Prioridad» | «Estimación» | «…» | «…» |
| [HU-004](HU-004-la-pantalla-lista-las-reglas-por-capitulo-con-sus-relaciones-y-enlaces-que-abren/HU-004-la-pantalla-lista-las-reglas-por-capitulo-con-sus-relaciones-y-enlaces-que-abren.md) | «Título» | «Prioridad» | «Estimación» | «…» | «…» |
| [HU-005](HU-005-las-propuestas-la-historia-y-la-memoria-muestran-nombres-legibles/HU-005-las-propuestas-la-historia-y-la-memoria-muestran-nombres-legibles.md) | «Título» | «Prioridad» | «Estimación» | «…» | «…» |
| [HU-006](HU-006-las-reglas-de-cada-proyecto-viven-en-la-misma-tabla/HU-006-las-reglas-de-cada-proyecto-viven-en-la-misma-tabla.md) | «Título» | «Prioridad» | «Estimación» | «…» | «…» |
| [HU-007](HU-007-las-reglas-m5-y-m9-dicen-que-la-regla-vive-en-casillas/HU-007-las-reglas-m5-y-m9-dicen-que-la-regla-vive-en-casillas.md) | «Título» | «Prioridad» | «Estimación» | «…» | Terminada |

## 10. Consideraciones técnicas

### 10.1 Arquitectura y componentes afectados

| Componente | Impacto | Observaciones |
|---|---|---|
| `proyectos/cimiento/core/estandar/` | Nuevo y modificado | Tablas de reglas, paso, pantalla |
| `core/herramientas/recuperar.py`, `mapa_tareas.py`, `core/enganches/` | Modificado | Leen de las tablas |
| `core/validadores/metareglas.py` | Modificado | Lee las reglas de las tablas |

### 10.2 Decisiones de arquitectura (ADR)

Ninguna aparte: las decisiones están en «Lo acordado» del análisis 1 del pendiente 136.

### 10.3 Integraciones

Ninguna.

### 10.4 Requisitos no funcionales transversales

| Categoría | Requisito |
|---|---|
| **Rendimiento** | Los enganches arman el texto desde las tablas sin arrancar Django |
| **Seguridad** | N/A |
| **Disponibilidad** | Sin base, el freno no deja trabajar, como hoy |
| **Auditoría y trazabilidad** | Todo cambio de una regla queda en la historia |
| **Escalabilidad** | N/A: una máquina |
| **Accesibilidad** | N/A |

### 10.5 Deuda técnica generada o pagada

- Se paga: las reglas dejan de leerse buscando dentro del texto.

## 11. Cumplimiento y normativa

N/A.

## 12. Dependencias

| ID | Dependencia | Tipo | Responsable | Fecha requerida | Estado |
|---|---|---|---|---|---|
| DEP-01 | EP-026: el estándar vive en la base | Interna | Agente | Antes de HU-001 | Resuelta |

## 13. Riesgos

| ID | Riesgo | Probabilidad | Impacto | Mitigación | Responsable |
|---|---|:--:|:--:|---|---|
| R-01 | Una regla que no sigue el molde no cabe en las casillas | Media | Medio | El paso compara el texto armado con el de hoy y se detiene si no son iguales (HU-002) | Agente |
| R-02 | El texto armado cambia lo que recibe el agente | Media | Alto | Prueba que compara el texto de cada mensaje antes y después (HU-003) | Agente |

## 14. Supuestos y restricciones

**Supuestos**
- Una sola máquina y una sola persona.

**Restricciones**
- Sin la librería `markdown`.

## 15. Hoja de ruta

| Orden | HU | Depende de | Por qué en ese orden | Estado |
|---|---|---|---|---|
| 1 | HU-007 | Ninguna | La regla tiene que permitirlo antes de construir lo que la usa | Terminada |
| 2 | HU-001 | HU-007 | Es donde se guarda todo lo demás | Pendiente |
| 3 | HU-002 | HU-001 | Sin las reglas en las tablas no hay qué leer ni mostrar | Pendiente |
| 4 | HU-003 | HU-002 | Necesita las reglas en las tablas | Pendiente |
| 5 | HU-004 | HU-002 | Necesita las reglas en las tablas | Pendiente |
| 6 | HU-005 | HU-002 | Necesita el título de cada regla | Pendiente |
| 7 | HU-006 | HU-003 | Se leen igual que las del estándar | Pendiente |

## 16. Estrategia de entrega

| Tema | Cómo |
|---|---|
| Despliegue | En la máquina del usuario, HU por HU |
| Migración de datos | Las 269 reglas pasan de los documentos a las tablas (HU-002) |
| Plan de reversión | Revertir el commit de la HU; los documentos siguen en `estandar_documento` hasta que la HU-003 deje de leerlos |
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

- [Análisis 1 del pendiente 136](../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/analisis-1.md)

## 20. Bitácora de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-07 | Agente | Creación de la épica desde el análisis aprobado |
