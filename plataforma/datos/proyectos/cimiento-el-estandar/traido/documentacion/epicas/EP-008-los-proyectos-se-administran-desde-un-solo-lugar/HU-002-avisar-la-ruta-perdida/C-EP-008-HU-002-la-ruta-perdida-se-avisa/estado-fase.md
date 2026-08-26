# Estado de fase - C-EP-008-HU-002: la ruta perdida se avisa   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Módulo** | Proyectos |
| **Épica / HU** | [EP-008](../../epica.md) · [HU-002](../HU-002-avisar-la-ruta-perdida.md) |
| **Versión del producto** | 1, fase C de ocho |
| **Última actualización** | 2026-08-25 |
| **Veredicto de las pruebas** | Cumple. 7 de 7 casos aprobados, en [resultado_pruebas.md](resultado_pruebas.md) |

---

## 1. En qué estación va

**Estación actual:** cerrada. **Última puerta pasada:** 9, el commit `ff2248e`.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | 👤 La HU-002 aprobada el 2026-08-25 | ☑ |
| 2 | Disparo / autorización de inicio | 👤 El usuario pidió seguir, el 2026-08-25 | ☑ |
| 3 | Diseño del plan detallado | Los dos planes escritos | ☑ |
| 4 | Pausa y presentación | Presentados y leídos | ☑ |
| 5 | Aprobación del plan detallado | 👤 «aprobado», el 2026-08-25 | ☑ |
| 6 | Ejecución continua | El aviso, la corrección y la medición | ☑ |
| 7 | Pruebas | Los siete casos con veredicto: 7 de 7 aprobados | ☑ |
| 8 | Cierre de la fase | [funcionalidad_implementada.md](funcionalidad_implementada.md), con tres deudas declaradas | ☑ |
| 9 | Commit único | 👤 «si», el 2026-08-25. Commit `ff2248e` | ☑ |

---

## 2. Qué falta para avanzar

**Nada: la fase cerró**, en el commit `ff2248e`. Las cinco tareas hechas, los siete casos en verde con su evidencia, y el cierre escrito. Con esto **la HU-002 queda cerrada**.

**La medición de `RNF-02`:** listar cincuenta proyectos tardó **0.010 s**, contra un límite de un segundo. El número queda escrito para poder compararlo cuando haya doscientos.

**Lo que encontró el sabotaje.** Uno de los seis pasó en verde. A diferencia del caso de la fase H, este **sí saboteaba**: hacía que corregir la ruta guardara la versión nueva en el índice y dejara la vieja en la ficha, así que al rehacer el índice volvía la vieja. Era **una prueba floja**, no un sabotaje inofensivo: miraba el objeto que devuelve la función en vez del texto. Se reforzó para borrar el índice, rehacerlo desde el texto y comprobar ahí.

## 3. Lo que ya se decidió

| Qué | Decisión |
|---|---|
| Cuándo se comprueba la ruta | Al listar. Es el supuesto declarado en la historia; no se vigila todo el tiempo |
| Qué pasa con la documentación de un proyecto con ruta perdida | Se sigue viendo. La documentación vive en la plataforma, no en el proyecto |
| Si corregir la ruta puede saltarse las comprobaciones de conectar | No. La ruta nueva se comprueba igual: que exista y que no la tenga otro |
| Qué pasa con la versión de reglas al corregir la ruta | Se relee de la carpeta nueva. Dejar la vieja sería afirmar sobre lo que no se leyó |
| Qué se prueba | Siete casos, incluido uno de lo que NO debe pasar: que corregir toque **alguna de las dos** carpetas |
| Qué se hace con la medición | El número se escribe aunque cumpla, para poder compararlo cuando haya doscientos proyectos |
