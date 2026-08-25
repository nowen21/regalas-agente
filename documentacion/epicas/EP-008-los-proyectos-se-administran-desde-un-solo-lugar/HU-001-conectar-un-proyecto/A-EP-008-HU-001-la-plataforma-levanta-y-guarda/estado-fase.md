# Estado de fase — A-EP-008-HU-001: la plataforma levanta y guarda   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Módulo** | Proyectos |
| **Épica / HU** | [EP-008](../../epica.md) · [HU-001](../HU-001-conectar-un-proyecto.md) |
| **Versión del producto** | 1, fase A de siete |
| **Última actualización** | 2026-08-25 |
| **Veredicto de las pruebas** | Cumple. 6 de 6 casos aprobados, en [resultado_pruebas.md](resultado_pruebas.md) |

---

## 1. En qué estación va

**Estación actual:** 9 - commit. **Última puerta pasada:** 8.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | La historia aprobada y la fase abierta | ☑ |
| 2 | Disparo / autorización de inicio | 👤 El usuario pidió continuar | ☑ |
| 3 | Diseño del plan detallado | Los dos planes escritos | ☑ |
| 4 | Pausa y presentación | Presentados, esperando lectura | ☑ |
| 5 | Aprobación del plan detallado | 👤 «aprobado», el 2026-08-25 | ☑ |
| 6 | Ejecución continua | La plataforma levanta y guarda | ☑ |
| 7 | Pruebas | Los seis casos con veredicto: 6 de 6 aprobados | ☑ |
| 8 | Cierre de la fase | [funcionalidad_implementada.md](funcionalidad_implementada.md), con cuatro deudas declaradas | ☑ |
| 9 | Commit único | 👤 Aprobación aparte para guardar | ☐ |

---

## 2. Qué falta para avanzar

**El visto bueno para guardar.** Todo lo demás está hecho: las cinco tareas del plan, los seis casos de prueba en verde con su evidencia, y el documento de cierre escrito. Falta que el usuario apruebe el commit, que se pide aparte de haber aprobado el trabajo.

---

## 3. Lo que ya se decidió

| Qué | Decisión |
|---|---|
| Qué construye esta fase | Levantar, guardar y reconstruir el índice. Registrar un proyecto es la fase B |
| Dónde vive lo guardado | Texto en el repositorio de la plataforma; el índice se rehace |
| Qué se prueba | Seis casos, incluido uno de lo que NO debe pasar: escribir fuera de la plataforma |
| Cómo se revierte | Se descarta la rama de la fase; nada de afuera se tocó |
