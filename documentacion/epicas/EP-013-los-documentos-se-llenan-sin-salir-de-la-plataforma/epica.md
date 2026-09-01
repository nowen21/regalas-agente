# EP-013 — Los documentos se llenan sin salir de la plataforma

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | EP-013 |
| **Producto** | Cimiento, plataforma de gestión de proyectos |
| **Módulo** | Ciclo de vida |
| **Versión del producto** | 2, según [cvds/implementacion/README.md](../../../cvds/implementacion/README.md) |
| **Funcionalidades que cubre** | `F-014` |
| **Estado** | En curso desde el 2026-09-01 |
| **Fecha de apertura** | 2026-09-01 |

---

## 2. Resumen ejecutivo

Que llenar un documento del ciclo deje de ser copiar un molde a mano y acordarse de qué hueco falta. La plataforma sabe qué molde sigue cada documento; el trabajo es que lo use para pedir lo que falta, uno por uno.

## 3. Problema y oportunidad

**Situación actual.** Los documentos entran a la plataforma **solo por importación**: un proyecto trae lo que ya escribió y ahí se queda. Para llenar un hueco hay que salir a un editor, buscar el archivo, encontrar la marca y escribir encima. La plataforma mira, no escribe.

**Qué cuesta.** Cada documento del ciclo sigue un molde de `plantillas/`, y esos moldes tienen decenas de huecos. Quien los llena a mano no tiene cómo saber cuántos le faltan sin releer el archivo entero, así que **se entrega con huecos sin llenar y nadie lo nota hasta que el documento sale**.

**Evidencia, medida sobre este repositorio.** El expediente del 2026-08-31 contó **31 documentos con espacios sin llenar** y 22 que el ciclo espera y no existen. Los 31 no salieron de revisar: salieron de contar la marca `«…»`, que es justo lo que una persona no hace releyendo.

**Y hay algo que el editor no puede dar.** Un editor de texto no sabe qué molde sigue el archivo abierto, así que no puede decir qué falta ni por qué ese hueco existe. La plataforma sí: el módulo Importación ya reconoce **19 tipos de documento por su nombre y su ubicación**.

## 4. Objetivo y propuesta de valor

Que la plataforma **muestre los huecos que le faltan a un documento y los pida uno por uno**, y que lo escrito quede en el archivo de texto, legible sin ella.

**Beneficios esperados:**

- Saber cuántos huecos faltan sin releer nada.
- Llenar sin salir de la plataforma, con el molde a la vista.
- Que lo escrito siga siendo texto: se lee, se versiona y se entrega igual.

## 5. Alcance

**Dentro:**

- Decir qué molde sigue un documento y qué huecos le faltan.
- Pedir cada hueco con el contexto que trae el molde, y guardar lo escrito en el archivo.
- Dejar registro de quién escribió qué y cuándo.

**Fuera:**

- **Redactar libre.** Se decidió con el usuario el 2026-09-01: la plataforma llena huecos, no reemplaza al editor. Un cuadro de texto compite con el editor del usuario y pierde, y es lo que la propia ficha de `F-014` advierte.
- **Crear épicas, historias y fases nuevas**, que es `F-011` y va en la versión 5. Acá se llenan documentos que ya existen porque la importación los trajo.
- Las puertas y los estados de una fase, que son `F-012` y `F-013`.

**Alcance funcional, ítem por ítem**

| Funcionalidad | Qué entrega | Versión |
|---|---|---|
| `F-014` Llenar los documentos del ciclo desde la plataforma | El documento guardado, con lo que le falta por llenar | 2 |

## 6. Usuarios y actores

| Actor | Qué hace acá |
|---|---|
| El usuario | Ve qué falta, lo llena y decide cuándo el documento está listo |
| El agente | Llena lo que le corresponde, por el mismo camino y con el mismo registro |
| El módulo Importación | Dice qué tipo de documento es cada archivo |
| El módulo Auditoría | Guarda quién escribió qué y cuándo |

## 7. Criterios de aceptación de la épica

- Un documento del ciclo se llena sin salir de la plataforma.
- Se ve **cuántos huecos** le faltan, y cuáles.
- Lo guardado queda como texto legible **sin la plataforma**, con el mismo formato que tenía.
- Escribir queda registrado en la auditoría.
- **Lo que no es un hueco no se toca:** llenar uno no reescribe el resto del documento.

## 8. Métricas de éxito

| Qué se mide | Meta |
|---|---|
| Documentos que se entregan con huecos sin que nadie lo note | Cero: la cuenta está a la vista antes de entregar |
| Saber cuántos huecos le faltan a un documento | De releerlo entero a un número |
| Documentos que la plataforma cambia de formato al guardar | Cero |

## 9. Historias de usuario

| HU | Título | Funcionalidad | Estado |
|---|---|---|---|
| [HU-001](HU-001-ver-que-le-falta-a-un-documento/HU-001-ver-que-le-falta-a-un-documento.md) | Ver qué le falta a un documento | `F-014` | **Terminada el 2026-09-01** |
| [HU-002](HU-002-llenar-un-hueco-desde-la-plataforma/HU-002-llenar-un-hueco-desde-la-plataforma.md) | Llenar un hueco desde la plataforma | `F-014` | Lista el 2026-09-01 |

## 10. Consideraciones técnicas

**Módulo nuevo:** Ciclo de vida, con [especificación aprobada](../../ciclo-de-vida/spec.md) el 2026-09-01, antes de tocar código ([`02·F2`](../../../base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md)).

**La marca del hueco ya es una convención del estándar:** `«…»`, fijada por [`13·DOC19`](../../../base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md). El módulo Expediente ya la cuenta, así que hay de dónde partir.

**Decisión que la gobierna:** [`DA-12`](../../../cvds/diseno/decisiones-de-arquitectura.md), que nombra a `RF-14` por su nombre. La pantalla administra, y lo que la hace segura no es prohibir el cambio sino registrarlo.

**Y la que manda sobre el guardado:** el texto es la verdad. Lo escrito va al archivo, no a una copia dentro de la base.

## 11. Dependencias

Depende de [EP-010](../EP-010-lo-escrito-entra-a-la-plataforma/epica.md): sin documentos traídos no hay qué llenar.

**La ficha de `F-014` dice depender de `F-011`, que es de la versión 5, y no la bloquea.** Esa columna dice qué tiene que existir, no qué construir antes; lo que `F-014` necesita es que haya documentos en la plataforma, y la importación los trae. Comprobado el 2026-09-01 recorriendo las 35 fichas, y escrito en el [inventario](../../../cvds/analisis-requisitos/inventario-funcionalidades.md).

## 12. Riesgos

| Riesgo | Qué se hace |
|---|---|
| **Que llenar ahí sea más incómodo que en un editor.** Es la advertencia de la propia ficha | Por eso se llena por huecos y no con un cuadro de texto: hace algo que el editor no puede, en vez de competir con él |
| Que guardar cambie el formato del documento | Se toca solo el hueco. Se comprueba comparando el archivo entero antes y después |
| Que un molde cambie y los huecos ya no cuadren | El molde se lee cuando se pide, no se copia. Lo que no cuadre se dice |
| Que se pierda lo escrito si el archivo cambió por fuera | Se detecta antes de guardar y se avisa, en vez de escribir encima |

## 13. Supuestos y restricciones

**Supuestos:** que los moldes de `plantillas/` marcan sus huecos con `«…»`, que es lo que `13·DOC19` exige.

**Restricciones:** la fuente es el texto; nada se guarda solo dentro de la base; todo cambio queda registrado.

## 14. Hoja de ruta

Versión 2. Es la última funcionalidad obligatoria de esa versión sin construir.

## 15. Definition of Ready

- ☑ La funcionalidad está en el inventario, con su ficha.
- ☑ El camino quedó decidido el 2026-09-01: se llena por huecos.
- ☑ Comprobado que no está bloqueada por `F-011`.
- ☑ El módulo Ciclo de vida, con [especificación aprobada](../../ciclo-de-vida/spec.md) el 2026-09-01.
- ☑ Las dos historias, aprobadas el 2026-09-01.

## 16. Definition of Done

- ☐ Las dos historias cerradas, con veredicto por criterio.
- ☐ Un documento real de este repositorio llenado desde la plataforma.
- ☐ Comprobado que el archivo no cambia fuera del hueco.
- ☐ La cuenta de documentos con huecos, medida antes y después.

## 17. Bitácora de cambios

| Fecha | Qué pasó |
|---|---|
| 2026-09-01 | **Aprobada** por Ing. José Dúmar Jiménez Ruíz, y sus dos historias escritas |
| 2026-09-01 | Nace del inventario aprobado, para cubrir `F-014`, la última funcionalidad obligatoria de la versión 2 sin historia escrita. El mismo día se decidió que se llena por huecos y se comprobó que `F-011` no la bloquea |
