# EP-016 — El cuerpo de reglas se administra desde la plataforma

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | EP-016 |
| **Producto** | Cimiento, plataforma de gestión de proyectos |
| **Módulo** | Reglas |
| **Versión del producto** | 3, según [cvds/implementacion/README.md](../../../cvds/implementacion/README.md) |
| **Funcionalidades que cubre** | `F-005`, `F-006`, `F-007`, `F-008`, `F-009`, `F-010` |
| **Estado** | Terminada el 2026-09-01: sus seis historias cumplen |
| **Fecha de apertura** | 2026-09-01 |

---

## 2. Resumen ejecutivo

Que el cuerpo de reglas se escriba, se numere, se derogue y se publique desde la plataforma, sin editar archivos a mano y sin que dos reglas terminen con el mismo número.

## 3. Problema y oportunidad

**Situación actual, medida el 2026-09-01.** El cuerpo de reglas tiene **257 reglas repartidas en 24 capítulos**, de las cuales **248 rigen y 9 están derogadas**. Todas se escriben editando archivos a mano.

**Qué cuesta.** Tres cosas distintas, y las tres pasan en silencio:

| Qué pasa | Por qué no se ve |
|---|---|
| Dos reglas terminan con el mismo número | La cita sigue viéndose bien; apunta a otra cosa |
| Una regla nueva repite lo que otra ya decía | Con 248 vigentes, nadie las tiene todas en la cabeza |
| Una regla se borra en vez de derogarse | Se pierde el porqué, y su número queda libre para otra |

**Lo más caro es el número.** Una especificación escrita hace un año, un commit, una fase cerrada: todos citan reglas por su identificador. Reasignar uno hace que todas esas citas empiecen a apuntar a algo que dice otra cosa, **y no hay forma de notarlo leyendo**.

## 4. Objetivo y propuesta de valor

Que administrar una regla sea pedirlo, y que lo que no se puede deshacer esté impedido por construcción.

**Beneficios esperados:**

- Ningún identificador se reutiliza, ni el de una regla derogada.
- Antes de escribir se ven las reglas que hablan de lo mismo.
- Derogar deja la regla legible, marcada y con su número ocupado.
- Publicar una versión pasa por la puerta que ya existe.

## 5. Alcance

**Dentro:**

- Dar el identificador y comprobar que esté libre (`F-006`).
- Escribir, corregir y derogar una regla (`F-005`).
- Aplicar la lista de comprobación y guardar el sello (`F-007`).
- Publicar una versión, con qué cambió (`F-008`).
- Entregarle las reglas al agente al abrir sesión (`F-009`).
- Avisarle a un proyecto que quedó atrás (`F-010`).

**Fuera:**

- **Decidir si una regla es buena.** La plataforma acompaña; el criterio es de una persona.
- **Detectar contradicciones.** Se muestran las reglas que hablan de lo mismo, que es distinto y hay que decirlo.
- Hacer cumplir las reglas, que es `F-020` y ya está construido.

**Alcance funcional, ítem por ítem**

| Funcionalidad | Qué entrega | Versión |
|---|---|---|
| `F-006` Asignar el identificador sin reutilizar ninguno | El identificador asignado | 3 |
| `F-005` Escribir, cambiar y derogar reglas | La regla guardada, con su identificador | 3 |
| `F-007` Aplicar el checklist y guardar su sello | El sello, y contra qué versión | 3 |
| `F-008` Publicar una versión del cuerpo de reglas | La versión publicada, con qué cambió | 3 |
| `F-009` Entregarle las reglas al agente al abrir sesión | Las reglas vigentes de ese proyecto | 3 |
| `F-010` Avisar a un proyecto que quedó atrás | El aviso, y qué cambió desde entonces | 3 |

## 6. Usuarios y actores

| Actor | Qué hace acá |
|---|---|
| El usuario | Escribe las reglas y decide qué se deroga y qué se publica |
| El agente | Recibe las reglas al abrir sesión, y las obedece |
| El estándar | **Sabe leer su propio cuerpo de reglas.** La plataforma no lo duplica |

## 7. Criterios de aceptación de la épica

- Ningún identificador se reutiliza, **ni el de una regla derogada**.
- Antes de guardar, se ven las reglas vigentes que hablan de lo mismo.
- Derogar deja la regla **legible y marcada**, nunca borrada.
- Una regla editada pierde su sello, y lo dice.
- Sin registro de qué cambió, no se publica.
- La fuente sigue siendo el texto: todo se lee sin la plataforma.

## 8. Métricas de éxito

| Qué se mide | Meta |
|---|---|
| Identificadores reutilizados | **Cero** |
| Reglas borradas en vez de derogadas | **Cero** |
| Versiones publicadas sin decir qué cambió | **Cero** |

## 9. Historias de usuario

| HU | Título | Funcionalidad | Estado |
|---|---|---|---|
| [HU-001](HU-001-dar-el-identificador-sin-reutilizar-ninguno/HU-001-dar-el-identificador-sin-reutilizar-ninguno.md) | Dar el identificador sin reutilizar ninguno | `F-006` | **Terminada el 2026-09-01** |
| [HU-002](HU-002-escribir-corregir-y-derogar-una-regla/HU-002-escribir-corregir-y-derogar-una-regla.md) | Escribir, corregir y derogar una regla | `F-005` | **Terminada el 2026-09-01** |
| [HU-003](HU-003-aplicar-el-checklist-y-guardar-su-sello/HU-003-aplicar-el-checklist-y-guardar-su-sello.md) | Aplicar el checklist y guardar su sello | `F-007` | **Terminada el 2026-09-01** |
| [HU-004](HU-004-publicar-una-version-del-cuerpo-de-reglas/HU-004-publicar-una-version-del-cuerpo-de-reglas.md) | Publicar una versión del cuerpo de reglas | `F-008` | **Terminada el 2026-09-01** |
| [HU-005](HU-005-entregarle-las-reglas-al-agente/HU-005-entregarle-las-reglas-al-agente.md) | Entregarle las reglas al agente al abrir sesión | `F-009` | **Terminada el 2026-09-01** |
| [HU-006](HU-006-avisar-al-proyecto-que-quedo-atras/HU-006-avisar-al-proyecto-que-quedo-atras.md) | Avisar a un proyecto que quedó atrás | `F-010` | **Terminada el 2026-09-01** |

## 10. Consideraciones técnicas

**Módulo nuevo:** Reglas, con su especificación escrita en esta épica.

**Es el cuarto puente hacia el estándar**, después del que tapa credenciales, el que parte una conversación en turnos y el que corre las comprobaciones. **Ya no es una excepción: es la forma.** El estándar sabe leer su propio cuerpo de reglas, y duplicar ese lector dejaría dos que se separan.

**La fuente es el texto.** Las reglas se escriben en archivos, no en la base. Guardarlas en la base y generar el texto haría del texto una copia, y la copia se queda vieja el día que alguien edite el archivo a mano, que es como se ha trabajado siempre.

## 11. Dependencias

Depende de `EP-015`: publicar una versión necesita la puerta que `F-022` construyó.

**La vuelta de la columna quedó cerrada** el mismo día: `F-020` se pudo construir porque lo que hay que comprobar ya existía escrito en `base/`.

## 12. Riesgos

| Riesgo | Qué se hace |
|---|---|
| **Que se reutilice un identificador** | Se comprueba antes de guardar, contando también las derogadas |
| Que alguien crea que la plataforma detecta contradicciones | El aviso dice, cada vez, que solo muestra las que se parecen |
| Que escribir desde la plataforma y a mano se separen | La fuente es el archivo, y las dos formas escriben el mismo |

## 13. Supuestos y restricciones

**Supuestos:** que el proyecto tiene el estándar instalado, con su lector de reglas.

**Restricciones:** la fuente es el texto; ningún identificador se reutiliza; nada se borra.

## 14. Hoja de ruta

Versión 3. Va al final: necesita la puerta de publicación que `EP-015` construyó.

## 15. Definition of Ready

- ☑ Las seis funcionalidades están en el inventario, con su ficha.
- ☑ Medido el cuerpo de reglas: 257, 248 vigentes, 9 derogadas, 24 capítulos.
- ☑ El módulo Reglas, con [especificación](../../reglas/spec.md) aprobada el 2026-09-01.
- ☑ `EP-015` cerrada, con la puerta de publicación.

## 16. Definition of Done

- ☑ Las seis historias cerradas, con veredicto por criterio.
- ☑ Comprobado que el identificador de una derogada no se reasigna.
- ☑ Comprobado que derogar deja la regla legible.
- ☑ La puerta de publicación enchufada: sin decir qué cambió no se publica.

## 17. Bitácora de cambios

| Fecha | Qué pasó |
|---|---|
| 2026-09-01 | **Terminada**: las seis historias construidas y probadas el mismo día. Con ella cierra el módulo Reglas y la versión 3 |
| 2026-09-01 | Nace del inventario aprobado, para cubrir las seis funcionalidades de Reglas. Sus dos primeras historias se construyeron el mismo día |
