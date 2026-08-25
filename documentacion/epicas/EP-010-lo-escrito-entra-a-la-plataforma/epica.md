# EP-010 — Lo que ya está escrito entra a la plataforma

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | EP-010 |
| **Producto** | Cimiento, plataforma de gestión de proyectos |
| **Módulo** | Importación |
| **Versión del producto** | 1, según [cvds/implementacion/README.md](../../../cvds/implementacion/README.md) |
| **Funcionalidades que cubre** | `F-027`, `F-028` |
| **Estado** | Aprobada el 2026-08-25 por Ing. José Dúmar Jiménez Ruíz |
| **Fecha de apertura** | 2026-08-25 |

---

## 2. Resumen ejecutivo

Traer a la plataforma la documentación que un proyecto ya tiene escrita, sin tocar el proyecto de origen y sin transformar lo que no se reconoce.

## 3. Problema y oportunidad

**Situación actual.** Los proyectos del usuario ya tienen documentación escrita, y la plataforma arrancaría vacía. Rehacer esa historia a mano no es viable: solo este repositorio tiene más de cien fases documentadas.

**Impacto de no hacerlo.** La plataforma serviría únicamente para lo que se empiece de cero, y todo lo anterior seguiría disperso.

**Evidencia.** Este mismo repositorio: siete épicas, más de cien historias, más de cien fases con sus planes y resultados.

## 4. Objetivo y propuesta de valor

Que conectar un proyecto y traerlo alcance para empezar a gobernarlo desde el primer día.

**Beneficios esperados:** la plataforma arranca con contenido real · nada se rehace a mano · lo que no encaje queda listado en vez de perderse.

## 5. Alcance

**Dentro:** traer lo que siga un molde conocido · reportar lo que no se reconoció, con su ruta.

**Fuera:** transformar lo que no tiene forma conocida · corregir lo traído · tocar el proyecto de origen.

**Diferido:** nada. Las dos funcionalidades entran en la versión 1.

**Alcance funcional, ítem por ítem**

| Funcionalidad | Qué entrega | Versión |
|---|---|---|
| `F-027` Traer un proyecto | Lo reconocido, adentro de la plataforma | 1 |
| `F-028` Reportar lo no reconocido | La lista, con la ruta de cada archivo | 1 |

## 6. Usuarios y actores

| Actor | Qué hace acá |
|---|---|
| El usuario | Pide traer, revisa qué se va a traer y confirma |
| El proyecto de origen | Aporta sus archivos, y queda intacto |

## 7. Criterios de aceptación de la épica

- Los documentos que siguen un molde conocido quedan adentro, con su tipo.
- El proyecto de origen queda intacto.
- Traer dos veces no duplica.
- Lo no reconocido queda listado con su ruta, y no se transforma.

## 8. Métricas de éxito

| Qué se mide | Meta |
|---|---|
| Documentos reconocidos al traer este repositorio | Lo más alto posible, y el resto listado |
| Archivos modificados en el proyecto de origen | Cero |
| Duplicados al traer dos veces | Cero |

## 9. Historias de usuario

| HU | Título | Funcionalidad | Estado |
|---|---|---|---|
| [HU-001](HU-001-traer-un-proyecto/HU-001-traer-un-proyecto.md) | Traer un proyecto con lo que tenga escrito | `F-027` | Aprobada |
| [HU-002](HU-002-reportar-lo-no-reconocido/HU-002-reportar-lo-no-reconocido.md) | Reportar lo que no sigue ningún molde | `F-028` | Aprobada |

## 10. Consideraciones técnicas

**Componentes afectados:** el módulo Importación, especificado en [documentacion/importacion/spec.md](../../importacion/spec.md).

**Decisiones que la gobiernan:** [`DA-10`](../../../cvds/diseno/decisiones-de-arquitectura.md) traer no modifica el proyecto de origen · [`DA-02`](../../../cvds/diseno/decisiones-de-arquitectura.md) lo traído vive en el repositorio de la plataforma.

## 11. Dependencias

Depende de [EP-008](../EP-008-los-proyectos-se-administran-desde-un-solo-lugar/epica.md): solo se trae a un proyecto ya conectado. Y de [EP-009](../EP-009-todo-lo-que-se-hace-queda-registrado/epica.md), porque traer queda registrado.

## 12. Riesgos

| Riesgo | Qué se hace |
|---|---|
| Que se reconozca mucho menos de lo esperado | Es la mayor incertidumbre de la versión 1, y por eso la fase va temprano |
| Que la traída falle a mitad | Se descarta lo traído en esa pasada, y el origen queda intacto |
| Que lo traído traiga información de un cliente | Todo queda en la máquina del usuario; se rehace la sección si la plataforma corre en un servidor |

## 13. Supuestos y restricciones

**Supuestos:** que buena parte de lo escrito sigue un molde conocido, y que lo demás es minoría.
**Restricciones:** se copia, no se mueve; nada se transforma sin que el usuario lo diga.

## 14. Hoja de ruta

Fases E y F de la versión 1. La E va antes que la G de EP-008, porque ver el estado sin haber traído nada sería mostrar pantallas vacías.

## 15. Definition of Ready

- ☑ El módulo tiene especificación aprobada.
- ☑ Hay un proyecto real para probar: este repositorio.
- ☑ Está decidido qué se hace con lo que no se reconoce.

## 16. Definition of Done

- ☐ Las dos historias cerradas, con veredicto por criterio.
- ☐ Comprobado sobre este repositorio, y con cuántos documentos entraron y cuántos no.
- ☐ Comprobado que el proyecto de origen quedó intacto.

## 17. Bitácora de cambios

| Fecha | Qué pasó |
|---|---|
| 2026-08-25 | Nace al aprobarse el inventario. Se declara este repositorio como su caso real de prueba |
