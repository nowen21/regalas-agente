# Estado de fase - B-EP-008-HU-001: se conecta un proyecto   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Módulo** | Proyectos |
| **Épica / HU** | [EP-008](../../epica.md) · [HU-001](../HU-001-conectar-un-proyecto.md) |
| **Versión del producto** | 1, fase B de siete |
| **Última actualización** | 2026-08-25 |
| **Veredicto de las pruebas** | Cumple. 9 de 9 casos aprobados, en [resultado_pruebas.md](resultado_pruebas.md) |

---

## 1. En qué estación va

**Estación actual:** 9, commit. **Última puerta pasada:** 8.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | La historia aprobada y la fase abierta | ☑ |
| 2 | Disparo / autorización de inicio | 👤 El usuario pidió seguir, el 2026-08-25 | ☑ |
| 3 | Diseño del plan detallado | Los dos planes escritos | ☑ |
| 4 | Pausa y presentación | Presentados y leídos | ☑ |
| 5 | Aprobación del plan detallado | 👤 «si», el 2026-08-25 | ☑ |
| 6 | Ejecución continua | El proyecto se conecta y se ve | ☑ |
| 7 | Pruebas | Los nueve casos con veredicto: 9 de 9 aprobados | ☑ |
| 8 | Cierre de la fase | [funcionalidad_implementada.md](funcionalidad_implementada.md), con cinco deudas declaradas | ☑ |
| 9 | Commit único | 👤 Aprobación aparte para guardar | ☐ |

---

## 2. Qué falta para avanzar

**El visto bueno para guardar.** Las siete tareas hechas, los nueve casos de prueba en verde con su evidencia, y el documento de cierre escrito. Con esto **la HU-001 queda cerrada**: sus cuatro criterios tienen veredicto.

**Lo que la fase destapó, y no era del alcance.** Al ver la primera pantalla funcionando salió que **conectar no tiene reversa**: no se puede desconectar, renombrar ni corregir la versión declarada. Peor: la especificación del módulo ya decidía cómo se comporta desconectar, y ninguna funcionalidad lo pedía. Se pidió por la cadena completa el mismo día, y es la fase H.

## 3. Lo que ya se decidió

| Qué | Decisión |
|---|---|
| Qué construye esta fase | Conectar un proyecto, y la primera pantalla. Avisar la ruta perdida es la fase C |
| Cómo se escribe | Con el comprobante de la auditoría. Es la primera fase que usa de verdad lo que la D construyó |
| Cómo se nombra la carpeta del proyecto | Con un identificador derivado del nombre, que se guarda: renombrar el proyecto no mueve su carpeta |
| Qué se prueba | Nueve casos, incluido uno de lo que NO debe pasar: que conectar toque la carpeta del proyecto |
| Con qué se prueba | Proyectos de mentira. Ninguna carpeta real del usuario como conejillo |
| Qué se hace con un proyecto sin estándar | Se conecta igual, con el campo vacío y su aviso |
