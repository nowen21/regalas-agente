# EP-011 — Lo que se repite sale a la luz

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | EP-011 |
| **Producto** | Cimiento, plataforma de gestión de proyectos |
| **Módulo** | Medición |
| **Versión del producto** | 2, según [cvds/implementacion/README.md](../../../cvds/implementacion/README.md) |
| **Funcionalidades que cubre** | `F-033`, `F-034` |
| **Estado** | Abierta |
| **Fecha de apertura** | 2026-08-25 |

---

## 2. Resumen ejecutivo

Que las conversaciones que ya se guardan se puedan buscar y contar, para ver qué correcciones el usuario tuvo que repetir.

## 3. Problema y oportunidad

**Situación actual.** Cada mensaje del usuario y cada respuesta del agente quedan escritos en `historico-chat/`, con las claves ya tapadas. Nadie puede contar nada sobre eso: para saber qué se repitió hay que releer las transcripciones una por una, que es lo que el histórico vino a evitar.

**Impacto de no hacerlo.** El daño es lento y no se ve. Se corrige el caso y se pierde el patrón, así que la misma corrección vuelve en la sesión siguiente.

**Evidencia.** En la sesión del 2026-08-25, dos correcciones se repitieron: *español colombiano* se pidió tres veces antes de quedar escrita como recuerdo, y `00·ID9` se citó cuatro veces sobre respuestas distintas. Las dos terminaron en algo escrito porque el usuario insistió, no porque el sistema lo detectara.

## 4. Objetivo y propuesta de valor

Que una corrección repetida se vea como lo que es: **una regla que falta**.

**Beneficios esperados:**

- Descubrir lo que el estándar no contempla.
- Dejar de gastar tiempo repitiendo lo mismo.
- Darle a `F-032` la fuente que hoy no tiene.

## 5. Alcance

**Dentro:**

- Indexar las conversaciones que el enganche del histórico ya escribe.
- Contar qué se repite y mostrarlo ordenado.

**Fuera:**

- La auditoría, que registra qué se hizo y no qué se conversó. Su `RN-4` queda intacta.
- Decidir sola la regla que resuelve el patrón: eso lo sigue decidiendo el usuario, por la cadena.
- Traer conversaciones de otras herramientas.

**Alcance funcional, ítem por ítem**

| Funcionalidad | Qué entrega | Versión |
|---|---|---|
| `F-033` Guardar las conversaciones donde se pueda buscar | La conversación indexada, con su fecha y su sesión | 2 |
| `F-034` Decir qué correcciones se repiten | Las más repetidas, con cuántas veces y en qué sesiones | 2 |

## 6. Usuarios y actores

| Actor | Qué hace acá |
|---|---|
| El usuario | Pide el reporte y decide qué regla escribir con lo que vea |
| El agente | Sus respuestas entran al conteo igual que los mensajes del usuario |
| El enganche del histórico | Es quien escribe lo que después se indexa |

## 7. Criterios de aceptación de la épica

- Lo que una sesión conversó se encuentra buscando una palabra suya.
- Las correcciones más repetidas salen con cuántas veces y en qué sesiones.
- Dos formas distintas de decir lo mismo cuentan como una.
- Ninguna credencial aparece en lo indexado.

## 8. Métricas de éxito

| Qué se mide | Meta |
|---|---|
| Reglas nuevas que nacieron de un patrón que nadie había visto | Al menos una |
| Credenciales en lo indexado | Cero |
| Correcciones que se repiten después de quedar escritas como regla | Que bajen |

## 9. Historias de usuario

| HU | Título | Funcionalidad | Estado |
|---|---|---|---|
| [HU-001](HU-001-buscar-en-lo-conversado/HU-001-buscar-en-lo-conversado.md) | Buscar en lo conversado | `F-033` | Escrita, sin aprobar |
| [HU-002](HU-002-ver-que-correccion-se-repite/HU-002-ver-que-correccion-se-repite.md) | Ver qué corrección se repite | `F-034` | Escrita, sin aprobar |

## 10. Consideraciones técnicas

**Componentes afectados:** el módulo Medición, que todavía no tiene especificación escrita. Se escribe antes de la primera fase (`02·F2`).

**De dónde sale el texto:** [validadores/historico.py](../../../validadores/historico.py), que ya escribe cada mensaje y cada respuesta con las claves tapadas por [validadores/enmascarar.py](../../../validadores/enmascarar.py).

**Decisión que la gobierna:** `DA-01`. El texto sigue siendo la fuente y el índice se puede borrar y rehacer, igual que todo lo demás.

## 11. Dependencias

Depende de [EP-008](../EP-008-los-proyectos-se-administran-desde-un-solo-lugar/epica.md), porque la plataforma tiene que existir para indexar algo.

**No depende de [EP-009](../EP-009-todo-lo-que-se-hace-queda-registrado/epica.md)**, y conviene decirlo porque se parecen: la auditoría guarda qué se hizo, esta épica guarda qué se conversó. Son dos preguntas distintas y dos almacenamientos distintos.

## 12. Riesgos

| Riesgo | Qué se hace |
|---|---|
| Que agrupar frases parecidas no salga sin depender de algo instalado aparte | Es el riesgo de peso. Se prueba temprano, y si no sale, se entrega el conteo exacto y se declara la deuda |
| Que el conteo diga lo obvio y no sirva para nada | La métrica de éxito no es que el reporte exista: es que de él salga al menos una regla nueva |
| Que indexar todas las conversaciones pese | Se mide con lo que ya hay acumulado, que es volumen real y no de mentira |

## 13. Supuestos y restricciones

**Supuestos:** que lo que el usuario repite queda escrito en la conversación, y no solo en su cabeza.
**Restricciones:** no se instala nada que salga a la red; el texto sigue siendo la fuente.

## 14. Hoja de ruta

Versión 2, después de entregar el expediente. Postergarla no pierde nada: las conversaciones ya están escritas y versionadas, así que se pueden indexar hacia atrás el día que se construya.

## 15. Definition of Ready

- ☑ Las dos funcionalidades están en el inventario, con su cambio anotado.
- ☑ El texto de origen existe y ya viene sin credenciales.
- ☐ El módulo Medición tiene especificación aprobada.

## 16. Definition of Done

- ☐ Las dos historias cerradas, con veredicto por criterio.
- ☐ Comprobado que ninguna credencial quedó en lo indexado.
- ☐ Al menos una regla nueva nacida de lo que el reporte mostró.

## 17. Bitácora de cambios

| Fecha | Qué pasó |
|---|---|
| 2026-08-25 | Nace de [pendientes/85](../../../pendientes/85-las-conversaciones-completas-no-se-pueden-analizar.md), aprobado ese día. El usuario lo pidió al abrir la fase de auditoría, y quedó separado de ella a propósito |
