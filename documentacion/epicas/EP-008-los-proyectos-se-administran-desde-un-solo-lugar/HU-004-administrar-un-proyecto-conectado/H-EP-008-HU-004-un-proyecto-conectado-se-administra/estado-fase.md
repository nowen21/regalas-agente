# Estado de fase - H-EP-008-HU-004: un proyecto conectado se administra   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Módulo** | Proyectos |
| **Épica / HU** | [EP-008](../../epica.md) · [HU-004](../HU-004-administrar-un-proyecto-conectado.md) |
| **Versión del producto** | 1, fase H de ocho |
| **Última actualización** | 2026-08-25 |
| **Veredicto de las pruebas** | Cumple. 8 de 8 casos aprobados, en [resultado_pruebas.md](resultado_pruebas.md) |

---

## 1. En qué estación va

**Estación actual:** 9, commit. **Última puerta pasada:** 8.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | 👤 La HU-004 aprobada el 2026-08-25 | ☑ |
| 2 | Disparo / autorización de inicio | 👤 El usuario pidió seguir, el 2026-08-25 | ☑ |
| 3 | Diseño del plan detallado | Los dos planes escritos | ☑ |
| 4 | Pausa y presentación | Presentados y leídos | ☑ |
| 5 | Aprobación del plan detallado | 👤 «aprobado», el 2026-08-25 | ☑ |
| 6 | Ejecución continua | Los tres cambios, su confirmación, y reconectar | ☑ |
| 7 | Pruebas | Los ocho casos con veredicto: 8 de 8 aprobados | ☑ |
| 8 | Cierre de la fase | [funcionalidad_implementada.md](funcionalidad_implementada.md), con cuatro deudas declaradas | ☑ |
| 9 | Commit único | 👤 Aprobación aparte para guardar | ☐ |

**La historia y los planes quedaron aprobados el 2026-08-25**, en la misma respuesta. La historia había nacido ese mismo día, de lo que destapó la fase B.

---

## 2. Qué falta para avanzar

**El visto bueno para guardar.** Las siete tareas hechas, los ocho casos de prueba en verde con su evidencia, y el documento de cierre escrito. Con esto **la HU-004 queda cerrada**.

**Lo que salió al validar las pruebas.** Uno de los seis sabotajes pasó en verde, y la lectura fácil habría sido «falta una prueba». No era eso: **el sabotaje no saboteaba**, porque borraba la ficha y la reescribía enseguida, sin cambiar nada observable. Se cambió por uno que sí toca lo que la fase promete, y ahí fallaron las dos pruebas correctas.

## 3. Lo que ya se decidió

| Qué | Decisión |
|---|---|
| Qué construye esta fase | Desconectar, renombrar, corregir la versión, y la confirmación de los cuatro |
| Cómo se marca un desconectado | Con una fecha en su ficha, no solo en la base: si no, rehacer el índice lo resucita |
| Qué pasa con su documentación | Se queda donde está. Desconectar no borra, y eso ya estaba decidido en la especificación |
| Qué pasa con su carpeta al renombrar | No se mueve. El identificador se guardó aparte del nombre desde la fase B, hecho para esto |
| Dónde se ven los desconectados | En la pantalla, en una sección aparte. Si desaparecen, nadie sabe que su documentación sigue ahí |
| Qué se prueba | Ocho casos, incluido uno de lo que NO debe pasar: que desconectar toque la carpeta del proyecto |
| Qué pasa al reconectar una ruta liberada | Reactiva el proyecto desconectado, con su documentación, avisando antes |
| Qué pasa con las fichas de la fase B | Una ficha sin el campo nuevo se lee como conectada. No hay que migrar nada |
