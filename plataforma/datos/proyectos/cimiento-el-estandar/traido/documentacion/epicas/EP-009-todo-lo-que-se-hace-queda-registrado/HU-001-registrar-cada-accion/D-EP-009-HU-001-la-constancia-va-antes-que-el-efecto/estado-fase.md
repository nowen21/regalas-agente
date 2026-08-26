# Estado de fase - D-EP-009-HU-001: la constancia va antes que el efecto   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Módulo** | Auditoría |
| **Épica / HU** | [EP-009](../../epica.md) · [HU-001](../HU-001-registrar-cada-accion.md) |
| **Versión del producto** | 1, fase D de siete |
| **Última actualización** | 2026-08-25 |
| **Veredicto de las pruebas** | Cumple. 7 de 7 casos aprobados en el ciclo 2, en [resultado_pruebas.md](resultado_pruebas.md) |

---

## 1. En qué estación va

**Estación actual:** cerrada. **Última puerta pasada:** 9, el commit `5231022`.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | La historia aprobada y la fase abierta | ☑ |
| 2 | Disparo / autorización de inicio | 👤 El usuario pidió seguir, el 2026-08-25 | ☑ |
| 3 | Diseño del plan detallado | Los dos planes escritos | ☑ |
| 4 | Pausa y presentación | Presentados y leídos | ☑ |
| 5 | Aprobación del plan detallado | 👤 «si», el 2026-08-25 | ☑ |
| 6 | Ejecución continua | El registro escribe, tapa y enlaza. Siete tareas, con la 7 agregada por autorización | ☑ |
| 7 | Pruebas | Los siete casos con veredicto. Dos ciclos: el 1 destapó un defecto crítico | ☑ |
| 8 | Cierre de la fase | [funcionalidad_implementada.md](funcionalidad_implementada.md), con cuatro deudas declaradas | ☑ |
| 9 | Commit único | 👤 «aprobado», el 2026-08-25. Commit `5231022` | ☑ |

---

## 2. Qué falta para avanzar

**Nada: la fase cerró.** Las siete tareas hechas, los siete casos de prueba en verde con su evidencia, el documento de cierre escrito y todo guardado en el commit `5231022`. Lo que sigue es la fase B, conectar un proyecto.

**Lo que pasó en el camino, y conviene no olvidar.** `CP-007` falló en el primer ciclo: se podía escribir sin dejar constancia, y con eso `CA-01` no se cumplía. Corregirlo obligaba a tocar el almacén, que el plan no declaraba, así que **la fase se detuvo y se pidió autorización** en vez de ampliar el plan por iniciativa (`02·F8`). El usuario la dio el 2026-08-25 sobre dos opciones escritas con su costo, y el ciclo se corrió completo otra vez.

## 3. Lo que ya se decidió

| Qué | Decisión |
|---|---|
| Por qué esta fase va antes que la B | El orden aprobado en la etapa 4: registrar desde el primer día evita un tramo sin historia |
| Cómo se rompe la dependencia con Proyectos | Una acción sin proyecto se registra igual, con el campo vacío |
| Cómo se guarda | Texto que solo se agrega, con lo que la fase A ya construyó |
| Qué se prueba | Siete casos, incluido uno de lo que NO debe pasar: que algo cambie sin quedar registrado |
| De dónde sale el tapado de claves | De `validadores/enmascarar.py`, importado. No se copia ni se mueve |
| Qué guarda el campo de sesión | El identificador del histórico, que aguanta el renombre del archivo |
