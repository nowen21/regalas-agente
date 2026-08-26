# Estado de fase - E-EP-010-HU-001: se trae un proyecto con lo que tenga escrito   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Módulo** | Importación |
| **Épica / HU** | [EP-010](../../epica.md) · [HU-001](../HU-001-traer-un-proyecto.md) |
| **Versión del producto** | 1, fase E de ocho |
| **Última actualización** | 2026-08-25 |
| **Veredicto de las pruebas** | Cumple. 9 de 9 casos aprobados en el ciclo 2, en [resultado_pruebas.md](resultado_pruebas.md) |

---

## 1. En qué estación va

**Estación actual:** 9, commit. **Última puerta pasada:** 8.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | 👤 La HU-001 aprobada el 2026-08-25 | ☑ |
| 2 | Disparo / autorización de inicio | 👤 El usuario pidió seguir, el 2026-08-25 | ☑ |
| 3 | Diseño del plan detallado | Los dos planes escritos | ☑ |
| 4 | Pausa y presentación | Presentados y leídos | ☑ |
| 5 | Aprobación del plan detallado | 👤 «si», el 2026-08-25 | ☑ |
| 6 | Ejecución continua | Reconocer, mostrar, traer, no duplicar | ☑ |
| 7 | Pruebas | Los nueve casos con veredicto: 9 de 9 en el ciclo 2 | ☑ |
| 8 | Cierre de la fase | [funcionalidad_implementada.md](funcionalidad_implementada.md), con cuatro deudas declaradas | ☑ |
| 9 | Commit único | 👤 Aprobación aparte para guardar | ☐ |

---

## 2. Qué falta para avanzar

**El visto bueno para guardar.** Las siete tareas hechas, los nueve casos en verde con su evidencia, y el cierre escrito.

**El caso real:** este repositorio entró con **973 documentos, ninguno sin reconocer, en 13,6 segundos**. La segunda pasada no duplicó nada, y el repositorio quedó con sus mismos 1924 archivos.

**Dos defectos en el ciclo 1, los dos encontrados por pruebas escritas de la forma incómoda:**

| Defecto | Qué era | Cómo se cazó |
|---|---|---|
| `DEF-01` | Traer transformaba los saltos de línea de Windows. **El texto se ve idéntico** | Una prueba que compara **bytes**, no texto. Comparando como texto habría pasado en verde |
| `DEF-02` | Al fallar a mitad se borraban los archivos pero no las filas del índice | Una prueba que mira **las dos** formas en que puede quedar media importación |

Los dos corregidos, con su porqué escrito en el código.

**Y un hallazgo que no era de la fase.** Uno de los sabotajes hacía que traer escribiera dentro del repositorio. La prueba lo cazó y el código se restauró, pero **el archivo que ese sabotaje escribió se quedó ahí**: 973 líneas en la raíz. Se descubrió porque la corrida real preguntaba si había rastros. Restaurar con copia protege el código, no el mundo.

## 3. Lo que ya se decidió

| Qué | Decisión |
|---|---|
| Qué se recorre | Solo la documentación del ciclo de vida. Lo demás no se mira, **y se dice cuál es** |
| Cómo se reconoce un documento | Por su nombre y su ubicación, que es lo que el estándar fija. No por su contenido |
| Qué entra a la plataforma | Una copia del contenido, no un enlace: si el proyecto se mueve, lo traído sigue sirviendo |
| Qué identifica un documento traído | Su ruta dentro del proyecto. Por eso traer dos veces no duplica, y un documento editado se actualiza sin crear otro |
| Qué se muestra antes de confirmar | El **recuento por tipo**, no la lista entera. Mil líneas se confirman sin mirar |
| Qué pasa si falla a mitad | No queda nada de esa pasada. Media importación es peor que ninguna |
| Qué se prueba | Nueve casos, incluido el caso real de traer este repositorio, y uno de lo que NO debe pasar |
