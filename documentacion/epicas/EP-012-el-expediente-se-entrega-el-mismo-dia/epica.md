# EP-012 — El expediente se entrega el mismo día

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | EP-012 |
| **Producto** | Cimiento, plataforma de gestión de proyectos |
| **Módulo** | Expediente |
| **Versión del producto** | 2, según [cvds/implementacion/README.md](../../../cvds/implementacion/README.md) |
| **Funcionalidades que cubre** | `F-025`, `F-026` |
| **Estado** | Aprobada el 2026-08-31 |
| **Fecha de apertura** | 2026-08-31 |

---

## 2. Resumen ejecutivo

Que juntar toda la documentación de un proyecto y entregarla en el formato que el cliente espera deje de costar un día de trabajo, y deje de depender de que alguien se acuerde de cuáles documentos hay.

## 3. Problema y oportunidad

**Situación actual.** Los documentos de un proyecto existen y están completos, pero **repartidos**: las siete etapas del ciclo en una carpeta, las épicas y sus historias en otra, y las fases con sus cinco documentos cada una. Armar el conjunto para entregarlo es abrir carpeta por carpeta, decidir qué entra y en qué orden, y copiarlo a mano al formato del cliente.

**Impacto de no hacerlo.** Es lo que hoy cuesta un día entero, y ese día se paga **cada vez** que hay que entregar. Peor que el tiempo: lo armado a mano se arma distinto cada vez, así que dos entregas del mismo proyecto no se parecen.

**Evidencia.** El propio repositorio ya tiene **1 054 documentos reconocidos** por el módulo Importación, repartidos en 19 tipos. Nadie puede juntarlos a ojo sin dejar algo afuera.

**Y hay un daño más silencioso:** lo que falta no se ve. Un expediente armado a mano no distingue entre «este documento no existe» y «se me pasó», así que se entrega incompleto sin que nadie lo note.

## 4. Objetivo y propuesta de valor

Que el expediente se arme solo, **diga qué le falta**, y se convierta en el archivo que el cliente espera sin escribir una línea a mano.

**Beneficios esperados:**

- Entregar el mismo día, no el día siguiente.
- Entregar siempre lo mismo, armado igual.
- **Saber qué falta antes de entregar**, en vez de después.

## 5. Alcance

**Dentro:**

- Juntar los documentos de un proyecto en el orden del ciclo, con el alcance que se pida.
- Señalar lo que falta y lo que está a medio llenar, sin inventarlo.
- Generar el archivo de ofimática desde el texto, cuantas veces haga falta.

**Fuera:**

- **La auditoría y la memoria.** Decidido con el usuario el 2026-08-31, cerrando la duda 5 del análisis: *«solo los entregables; el resto es memoria para Cimiento»*. Sirven para saber cómo se llegó, no para entregar.
- **Recibir cambios hechos encima del entregable.** Lo dice `DA-09`: la fuente es el texto y la salida se rehace. Está declarado como lo que se pierde.
- Llenar los documentos desde la plataforma, que es `F-014` y va en su propia épica.

**Alcance funcional, ítem por ítem**

| Funcionalidad | Qué entrega | Versión |
|---|---|---|
| `F-025` Armar el expediente de un proyecto | El expediente armado, con lo que falta señalado | 2 |
| `F-026` Generar el entregable de ofimática | El archivo generado, nunca escrito a mano | 2 |

## 6. Usuarios y actores

| Actor | Qué hace acá |
|---|---|
| El usuario | Pide el expediente, mira lo que falta y decide si entrega |
| Quien recibe el proyecto | Lee el entregable. **No lo edita**: si necesita cambios, los pide |
| El módulo Importación | Es quien reconoce qué documento es cada archivo |

## 7. Criterios de aceptación de la épica

- El expediente completo de un proyecto se arma cuando se pide, en el orden del ciclo.
- Lo que falta se lista y **no se inventa**.
- Lo que está a medio llenar se marca antes de entregar.
- El archivo de ofimática sale del texto, y generarlo dos veces da lo mismo.
- **La auditoría y la memoria no entran.**

## 8. Métricas de éxito

| Qué se mide | Meta |
|---|---|
| Lo que cuesta armar y entregar un expediente | De un día a minutos |
| Documentos que se quedan afuera sin que nadie lo note | Cero: lo que falta se dice |
| Entregables escritos a mano | Cero |

## 9. Historias de usuario

| HU | Título | Funcionalidad | Estado |
|---|---|---|---|
| [HU-001](HU-001-armar-el-expediente-de-un-proyecto/HU-001-armar-el-expediente-de-un-proyecto.md) | Armar el expediente de un proyecto | `F-025` | Aprobada el 2026-08-31 |
| [HU-002](HU-002-generar-el-entregable-de-ofimatica/HU-002-generar-el-entregable-de-ofimatica.md) | Generar el entregable de ofimática | `F-026` | Aprobada el 2026-08-31 |

## 10. Consideraciones técnicas

**Componentes afectados:** el módulo Expediente, con su especificación [escrita y aprobada el 2026-08-31](../../expediente/spec.md).

**De dónde salen los documentos:** de lo que el módulo Importación ya trajo y reconoció. No se vuelve a recorrer el proyecto de origen.

**Decisión que la gobierna:** [`DA-09`](../../../cvds/diseno/decisiones-de-arquitectura.md). El entregable **se genera** desde el texto y nunca al contrario; un segundo original habría que mantenerlo para siempre.

**Lo que ya está advertido en la ficha de `F-026`:** las listas dentro de una celda tienen que salir como listas, no con la etiqueta a la vista. Es el detalle donde este tipo de generadores se cae.

## 11. Dependencias

Depende de [EP-010](../EP-010-lo-escrito-entra-a-la-plataforma/epica.md): sin los documentos traídos y reconocidos no hay qué juntar.

Depende también de `F-014` —llenar los documentos desde la plataforma— según la ficha de `F-025`. **Se puede empezar sin ella**: hoy los documentos entran por importación, y armar el expediente con lo que hay ya sirve.

## 12. Riesgos

| Riesgo | Qué se hace |
|---|---|
| Que el generador de ofimática rompa el formato en listas y tablas | Es el riesgo de peso, y ya está advertido en la ficha. Se prueba con un documento real del repositorio, no con uno de mentiras |
| Que armar el expediente esconda lo que falta | Lo que falta se lista con nombre; un expediente que no dice qué le falta es peor que no tenerlo |
| Que el orden del ciclo no esté definido para todos los tipos | Se declara el orden en la especificación del módulo, y lo que no encaje se dice |

## 13. Supuestos y restricciones

**Supuestos:** que lo que Importación reconoció alcanza para armar el expediente.
**Restricciones:** la fuente es el texto; nada se escribe a mano en el entregable; la auditoría y la memoria quedan fuera.

## 14. Hoja de ruta

Versión 2. Es lo que esa versión promete como valor —*entregar el expediente el mismo día*— y por eso va antes que el resto de lo que queda de la versión.

## 15. Definition of Ready

- ☑ Las dos funcionalidades están en el inventario, con su ficha.
- ☑ La duda 5 del análisis, resuelta el 2026-08-31.
- ☑ El módulo Expediente tiene especificación aprobada, el 2026-08-31.
- ☑ Las dos historias escritas y aprobadas, el 2026-08-31.

## 16. Definition of Done

- ☐ Las dos historias cerradas, con veredicto por criterio.
- ☐ Un expediente real armado, con lo que le falta dicho.
- ☐ Un entregable generado dos veces con el mismo resultado.
- ☐ Comprobado que la auditoría y la memoria no entraron.

## 17. Bitácora de cambios

| Fecha | Qué pasó |
|---|---|
| 2026-08-31 | **Aprobada** por Ing. José Dúmar Jiménez Ruíz |
| 2026-08-31 | Nace del inventario aprobado, para cubrir `F-025` y `F-026`, que eran las dos funcionalidades obligatorias de la versión 2 sin historia escrita. El mismo día se resolvió la duda 5, que fijaba su alcance |
