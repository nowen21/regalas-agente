# EP-008 — Los proyectos se administran desde un solo lugar

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | EP-008 |
| **Producto** | Cimiento, plataforma de gestión de proyectos |
| **Módulo** | Proyectos |
| **Versión del producto** | 1, según [cvds/implementacion/README.md](../../../cvds/implementacion/README.md) |
| **Funcionalidades que cubre** | `F-001`, `F-002`, `F-003`, `F-004`, `F-035` |
| **Estado** | Abierta |
| **Fecha de apertura** | 2026-08-25 |

---

## 2. Resumen ejecutivo

El usuario trabaja en varios proyectos y no tiene desde dónde verlos juntos. Esta épica hace que la plataforma sepa qué proyectos existen, dónde vive el código de cada uno, y en qué va cada uno sin abrir su carpeta.

## 3. Problema y oportunidad

**Situación actual.** Para saber cómo va un proyecto hay que entrar a él y leer sus archivos. Para compararlos, no hay forma. Cuando un proyecto se mueve de carpeta, nadie se entera hasta que algo falla.

**Impacto de no hacerlo.** Sin esto no hay plataforma: las otras once épicas necesitan saber a qué proyecto pertenece cada cosa. Es la base de todo lo demás.

**Evidencia.** El problema declarado en la [planificación](../../../cvds/planificacion/README.md): entrar proyecto por proyecto es hoy la única forma de saber cómo van.

## 4. Objetivo y propuesta de valor

Que el usuario abra la plataforma y vea todos sus proyectos, con su estado, sin entrar a ninguno.

**Beneficios esperados:** saber en qué va cada proyecto en segundos · enterarse cuando una ruta se pierde, en vez de descubrirlo tarde · tener dónde colgar la documentación, las reglas y la auditoría de cada uno.

## 5. Alcance

**Dentro:** registrar un proyecto con su nombre y su ruta · detectar y avisar la ruta perdida · mostrar el estado de un proyecto · configurar qué reglas y moldes rigen en él.

**Fuera:** tocar el código del proyecto · traer su documentación, que es de [EP-010](../EP-010-lo-escrito-entra-a-la-plataforma/epica.md) · registrar lo que se hace, que es de [EP-009](../EP-009-todo-lo-que-se-hace-queda-registrado/epica.md).

**Diferido:** la configuración por proyecto (`F-004`) queda para la versión 5. Sin reglas administradas todavía, no hay qué configurar.

**Alcance funcional, ítem por ítem**

| Funcionalidad | Qué entrega | Versión |
|---|---|---|
| `F-001` Conectar un proyecto | El proyecto registrado y visible | 1 |
| `F-035` Administrar un proyecto conectado | Desconectarlo, renombrarlo o corregir su versión, sin borrar nada | 1 |
| `F-002` Avisar la ruta perdida | El aviso, sin perder su documentación | 1 |
| `F-003` Ver el estado sin entrar | El estado en pantalla | 1 |
| `F-004` Configurar qué rige | Reglas y moldes por proyecto | 5 |

## 6. Usuarios y actores

| Actor | Qué hace acá |
|---|---|
| El usuario | Conecta, consulta y desconecta proyectos |
| El agente | Consulta a qué proyecto pertenece la sesión en la que trabaja |

## 7. Criterios de aceptación de la épica

- Un proyecto queda conectado, y aparece en la lista con su estado.
- Una ruta que deja de existir se avisa, y la documentación de ese proyecto se sigue viendo.
- El estado de cualquier proyecto se ve sin abrir su carpeta.
- Nada de lo que hace esta épica modifica el código de un proyecto.

## 8. Métricas de éxito

| Qué se mide | Meta |
|---|---|
| Tiempo en saber cómo va un proyecto | Menos de un minuto, contra los varios que toma hoy entrar y leer |
| Listar cincuenta proyectos | Menos de un segundo (`RNF-02`) |
| Rutas perdidas detectadas | Todas, y avisadas antes de que el usuario las busque |

## 9. Historias de usuario

| HU | Título | Funcionalidad | Estado |
|---|---|---|---|
| [HU-001](HU-001-conectar-un-proyecto/HU-001-conectar-un-proyecto.md) | Conectar un proyecto | `F-001` | Cerrada el 2026-08-25 |
| [HU-002](HU-002-avisar-la-ruta-perdida/HU-002-avisar-la-ruta-perdida.md) | Avisar cuando la ruta se pierde | `F-002` | Aprobada |
| [HU-003](HU-003-ver-el-estado-de-un-proyecto/HU-003-ver-el-estado-de-un-proyecto.md) | Ver el estado de un proyecto | `F-003` | Aprobada |
| [HU-004](HU-004-administrar-un-proyecto-conectado/HU-004-administrar-un-proyecto-conectado.md) | Administrar un proyecto conectado | `F-035` | Escrita, sin aprobar |

## 10. Consideraciones técnicas

**Componentes afectados:** el módulo Proyectos, especificado en [documentacion/proyectos/spec.md](../../proyectos/spec.md).

**Decisiones de arquitectura que la gobiernan:** [`DA-01`](../../../cvds/diseno/decisiones-de-arquitectura.md) la fuente es texto y la base es índice · [`DA-02`](../../../cvds/diseno/decisiones-de-arquitectura.md) la documentación vive en el repositorio de la plataforma.

## 11. Dependencias

Ninguna hacia afuera. De ella dependen EP-009 y EP-010.

## 12. Riesgos

| Riesgo | Qué se hace |
|---|---|
| Que el estado calculado sea lento con muchos proyectos | Se guarda como índice, reconstruible desde el texto |
| Que un proyecto se mueva seguido y el aviso canse | Se mide en el uso; si estorba, se decide si la ruta se corrige sola |

## 13. Supuestos y restricciones

**Supuestos:** que basta la ruta del código para ubicar un proyecto.
**Restricciones:** la plataforma corre en la máquina del usuario, y nada de esta épica toca el código de los proyectos.

## 14. Hoja de ruta

Fases A, B, C y G de la versión 1, en ese orden. La C depende de la B, y la G de que haya algo traído para mostrar.

## 15. Definition of Ready

- ☑ El módulo tiene especificación aprobada.
- ☑ Las tres historias de la versión 1 tienen criterios verificables.
- ☑ El modelo de datos define la entidad Proyecto.

## 16. Definition of Done

- ☐ Las tres historias cerradas, con veredicto por criterio.
- ☐ Ningún criterio sin prueba corrida.
- ☐ Notas de la versión escritas.

## 17. Bitácora de cambios

| Fecha | Qué pasó |
|---|---|
| 2026-08-25 | Nace al aprobarse el inventario de Cimiento, que abre la puerta de las épicas |
