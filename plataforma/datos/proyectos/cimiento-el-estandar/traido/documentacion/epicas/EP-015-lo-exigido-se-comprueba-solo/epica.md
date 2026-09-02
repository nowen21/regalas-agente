# EP-015 — Lo exigido se comprueba solo

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | EP-015 |
| **Producto** | Cimiento, plataforma de gestión de proyectos |
| **Módulo** | Comprobaciones |
| **Versión del producto** | 3, según [cvds/implementacion/README.md](../../../cvds/implementacion/README.md) |
| **Funcionalidades que cubre** | `F-020`, `F-021`, `F-022` |
| **Estado** | Terminada el 2026-09-01: sus tres historias cumplen |
| **Fecha de apertura** | 2026-09-01 |

---

## 2. Resumen ejecutivo

Que la plataforma diga si un proyecto cumple lo que las reglas exigen, sin que nadie tenga que entrar a la carpeta y correr nada a mano.

## 3. Problema y oportunidad

**Situación actual.** El estándar tiene **32 comprobaciones** y **733 pruebas** que dicen si lo escrito cumple. Están todas, funcionan, y **la plataforma no las usa**: para saber si un proyecto cumple hay que abrir su carpeta y correrlas ahí.

**Qué cuesta.** La plataforma administra proyectos y muestra su estado, pero ese estado sale de leer documentos, no de comprobar nada. Un proyecto puede verse al día en la pantalla y estar rojo en su carpeta.

**Y hay un dato que hoy nadie fija.** El inventario tiene 35 funcionalidades y **las 35 dicen «Sin verificar»**. No porque estén mal, sino porque nada convierte una prueba corrida en un estado escrito.

**El ciclo que apareció al planificar.** La columna de dependencias tiene una vuelta entre estas tres y `F-008`: publicar necesita comprobar que no rompió, comprobar que no rompió necesita comprobar, y comprobar necesita una versión publicada. Leída como orden de construcción, ninguna arranca. Se resuelve solo: **lo que hay que comprobar ya existe escrito en `base/`**, y no hace falta que la plataforma lo publique.

## 4. Objetivo y propuesta de valor

Que se pida «¿este proyecto cumple?» desde la plataforma y salga la respuesta **con el archivo y la línea de lo que no cumple**.

**Beneficios esperados:**

- Saber si un proyecto cumple sin entrar a él.
- Que el estado de una funcionalidad lo fije **la prueba corrida**, no la lectura.
- Que nada se publique rompiendo lo que ya servía.

## 5. Alcance

**Dentro:**

- Correr las comprobaciones del estándar contra un proyecto conectado, y decir qué falla y dónde.
- Fijar el estado de una funcionalidad desde la evidencia, y **no dejar cerrar sin ella**.
- Volver a correr lo que ya funcionaba antes de publicar.

**Fuera:**

- **Corregir lo que encuentra.** Las comprobaciones leen y dicen; no tocan.
- **Escribir comprobaciones nuevas.** Eso es del estándar, y allá viven con sus pruebas.
- La pantalla.

**Alcance funcional, ítem por ítem**

| Funcionalidad | Qué entrega | Versión |
|---|---|---|
| `F-020` Comprobar sola lo que las reglas exigen | El veredicto, con archivo y línea | 3 |
| `F-021` Declarar sin verificar lo que no tiene prueba | El estado, fijado por la evidencia | 3 |
| `F-022` Comprobar que lo nuevo no rompió lo anterior | La puerta antes de publicar | 3 |

## 6. Usuarios y actores

| Actor | Qué hace acá |
|---|---|
| El usuario | Pide el veredicto y decide qué hacer con él |
| El agente | Recibe lo mismo, y no puede cerrar una fase sin evidencia |
| El estándar | Aporta las comprobaciones. La plataforma **no las duplica** |

## 7. Criterios de aceptación de la épica

- Un proyecto que cumple pasa; uno que no, es rechazado **con el archivo y la línea**.
- Apuntada a algo que no le corresponde, **lo dice en vez de dar veredicto**.
- Una funcionalidad sin prueba queda «sin verificar», y no se puede cerrar.
- Una versión que rompe algo que servía **no se publica**.
- Las comprobaciones **no corrigen nada**.

## 8. Métricas de éxito

| Qué se mide | Meta |
|---|---|
| Saber si un proyecto cumple | De entrar a su carpeta a pedirlo desde la plataforma |
| Funcionalidades con estado fijado por lectura | **Cero** |
| Versiones publicadas que rompieron algo | **Cero** |

## 9. Historias de usuario

| HU | Título | Funcionalidad | Estado |
|---|---|---|---|
| [HU-001](HU-001-comprobar-un-proyecto-desde-la-plataforma/HU-001-comprobar-un-proyecto-desde-la-plataforma.md) | Comprobar un proyecto desde la plataforma | `F-020` | **Terminada el 2026-09-01** |
| [HU-002](HU-002-fijar-el-estado-desde-la-evidencia/HU-002-fijar-el-estado-desde-la-evidencia.md) | Fijar el estado desde la evidencia | `F-021` | **Terminada el 2026-09-01** |
| [HU-003](HU-003-no-publicar-lo-que-rompe-lo-anterior/HU-003-no-publicar-lo-que-rompe-lo-anterior.md) | No publicar lo que rompe lo anterior | `F-022` | **Terminada el 2026-09-01** |

## 10. Consideraciones técnicas

**Módulo nuevo:** Comprobaciones, sin especificación previa.

**Se corren por su punto de entrada**, en un proceso aparte, que es como se corren de verdad. Cargar sus archivos a mano daría un número que nadie más obtiene. Es lo mismo que ya se hace para correr la batería de la plataforma desde el estándar.

**Decisión que la gobierna:** las comprobaciones viven en el estándar y la plataforma las usa. Duplicarlas dejaría dos versiones que se separan, igual que pasaría con el reconocedor de credenciales.

## 11. Dependencias

Depende de `EP-008`, que registra los proyectos y sabe dónde viven.

**La columna de dependencias tiene una vuelta** entre `F-020`, `F-022` y `F-008`. No bloquea: lo que hay que comprobar ya existe escrito en `base/`. Queda explicado en el [inventario](../../../cvds/analisis-requisitos/inventario-funcionalidades.md).

## 12. Riesgos

| Riesgo | Qué se hace |
|---|---|
| Que correr las comprobaciones tarde tanto que nadie las pida | Se mide cuánto tardan sobre este repositorio, y el número queda escrito |
| Que un proyecto sin el estándar instalado dé un veredicto falso | Se detecta antes de correr, y se dice en vez de concluir |
| Que la plataforma duplique las comprobaciones | Se corren las del estándar, por su punto de entrada |

## 13. Supuestos y restricciones

**Supuestos:** que el proyecto conectado tiene el estándar instalado. Si no, se dice.

**Restricciones:** las comprobaciones no corrigen; no se duplican; el veredicto sale con archivo y línea.

## 14. Hoja de ruta

Versión 3. Va después de `EP-014` y antes de las reglas: **desbloquea la vuelta de la columna**, porque publicar una versión necesita esta puerta.

## 15. Definition of Ready

- ☑ Las tres funcionalidades están en el inventario, con su ficha.
- ☑ Comprobado que la plataforma no corre hoy ninguna comprobación.
- ☑ La vuelta de la columna, explicada y resuelta.
- ☑ El módulo Comprobaciones, con [especificación](../../comprobaciones/spec.md) aprobada el 2026-09-01.

## 16. Definition of Done

- ☑ Las tres historias cerradas, con veredicto por criterio.
- ☑ Un proyecto real comprobado desde la plataforma: **32 comprobaciones en 116,9 s**.
- ☑ Una funcionalidad que no se puede cerrar sin evidencia: **21 de 35 sin verificar**.
- ☑ Una publicación detenida por romper algo, probada con cada rojo por separado.

## 17. Bitácora de cambios

| Fecha | Qué pasó |
|---|---|
| 2026-09-01 | **Terminada**: las tres historias construidas y probadas el mismo día. Con ella cierra la vuelta de la columna: `F-008` ya tiene su puerta |
| 2026-09-01 | Nace del inventario aprobado, para cubrir las tres funcionalidades de Comprobaciones. El mismo día apareció la vuelta de la columna, que se resolvió antes de abrirla |
