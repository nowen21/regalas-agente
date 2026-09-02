# EP-009 — Todo lo que se hace queda registrado

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | EP-009 |
| **Producto** | Cimiento, plataforma de gestión de proyectos |
| **Módulo** | Auditoría |
| **Versión del producto** | 1, según [cvds/implementacion/README.md](../../../cvds/implementacion/README.md) |
| **Funcionalidades que cubre** | `F-018`, `F-019` |
| **Estado** | Terminada el 2026-09-01: sus dos historias cumplen |
| **Fecha de apertura** | 2026-08-25 |

---

## 2. Resumen ejecutivo

Que quede constancia de qué se hizo en la plataforma: quién, cuándo, sobre qué y qué cambió. Y que esa constancia se pueda enlazar con lo que la sesión dejó escrito, para saber también por qué.

## 3. Problema y oportunidad

**Situación actual.** Lo que se aprueba y lo que se decide vive en conversaciones que se borran. Meses después nadie puede demostrar qué se autorizó, ni por qué se cambió algo.

**Impacto de no hacerlo.** Sin registro, la plataforma administra pero no responde. Y agregarlo tarde deja un tramo sin historia que ya no se puede reconstruir.

**Evidencia.** Pasó en este mismo proyecto: tres documentos aprobados un día quedaron sin efecto al día siguiente, y lo único que lo dice es la sección de cambios que se escribió a mano.

## 4. Objetivo y propuesta de valor

Que cualquier cambio se pueda rastrear hasta quién lo hizo, cuándo, y con qué razón escrita.

**Beneficios esperados:** poder demostrar lo autorizado · encontrar cuándo entró un cambio · saber qué sesión lo produjo y qué dejó escrito.

## 5. Alcance

**Dentro:** registrar cada acción que cambia algo · enlazar el registro con lo que la sesión dejó escrito · consultar lo registrado con filtros.

**Fuera:** guardar la conversación completa de las sesiones, que se sigue guardando aparte · interpretar por qué se hizo algo, que es del documento y de la memoria.

**Diferido:** la consulta con filtros (`F-019`) queda para la versión 4. Registrar temprano es barato; consultar puede esperar a que haya qué consultar.

**Alcance funcional, ítem por ítem**

| Funcionalidad | Qué entrega | Versión |
|---|---|---|
| `F-018` Registrar cada acción | La constancia, con su enlace a la sesión | 1 |
| `F-019` Consultar lo registrado | La búsqueda por proyecto, fecha y tipo | 4 |

## 6. Usuarios y actores

| Actor | Qué hace acá |
|---|---|
| El usuario | Consulta lo registrado, y no puede editarlo |
| El agente | Sus acciones quedan registradas igual que las del usuario |
| Los demás módulos | Le entregan cada acción que ejecutan |

## 7. Criterios de aceptación de la épica

- Toda acción que cambia algo queda registrada, con quién, cuándo y sobre qué.
- Lo registrado no se puede editar ni borrar.
- Si el registro no se puede escribir, la acción no se ejecuta.
- Ninguna credencial queda en el registro.

## 8. Métricas de éxito

| Qué se mide | Meta |
|---|---|
| Acciones que cambian algo sin quedar registradas | Cero |
| Registros con credenciales | Cero |
| Acciones de sesión con su enlace a lo que dejó escrito | Todas las que la sesión haya escrito |

## 9. Historias de usuario

| HU | Título | Funcionalidad | Estado |
|---|---|---|---|
| [HU-001](HU-001-registrar-cada-accion/HU-001-registrar-cada-accion.md) | Registrar cada acción que se hace | `F-018` | **Terminada el 2026-09-01** |
| [HU-002](HU-002-buscar-en-la-auditoria/HU-002-buscar-en-la-auditoria.md) | Buscar en la auditoría | `F-019` | **Terminada el 2026-09-01** |

## 10. Consideraciones técnicas

**Componentes afectados:** el módulo Auditoría, especificado en [documentacion/auditoria/spec.md](../../auditoria/spec.md).

**Decisiones que la gobiernan:** [`DA-08`](../../../cvds/diseno/decisiones-de-arquitectura.md) se registran acciones, no conversación, y el registro no se edita.

## 11. Dependencias

Depende de [EP-008](../EP-008-los-proyectos-se-administran-desde-un-solo-lugar/epica.md), para saber en qué proyecto ocurrió cada acción.

## 12. Riesgos

| Riesgo | Qué se hace |
|---|---|
| Que el registro crezca hasta no poder consultarse | Se indexa por proyecto y por fecha desde el principio |
| Que registrar antes de ejecutar haga lento el trabajo | Se mide: si estorba, se revisa el orden, no la exigencia |
| Que un registro que no se borra choque con el derecho de un cliente a que borren lo suyo | Declarado en la sección 9 de la especificación; se rehace si la plataforma guarda datos de clientes |

## 13. Supuestos y restricciones

**Supuestos:** que registrar la acción alcanza, y que el porqué queda cubierto por lo que la sesión escribe.
**Restricciones:** el registro solo se agrega, nunca se modifica.

## 14. Hoja de ruta

Fase D de la versión 1, que va temprano a propósito: registrar desde el primer día evita tener un tramo sin historia.

## 15. Definition of Ready

- ☑ El módulo tiene especificación aprobada.
- ☑ Está resuelto qué se audita de una sesión.
- ☑ El modelo de datos define el registro y su campo de sesión.

## 16. Definition of Done

- ☐ La historia cerrada, con veredicto por criterio.
- ☐ Comprobado que una acción no puede cambiar algo sin quedar registrada.
- ☐ Comprobado que el registro no se puede editar.

## 17. Bitácora de cambios

| Fecha | Qué pasó |
|---|---|
| 2026-08-25 | Nace con el inventario aprobado. Ese mismo día se resuelve qué se audita de una sesión: las acciones, más lo que dejó escrito |
