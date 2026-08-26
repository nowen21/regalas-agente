# Estado de fase - F-EP-010-HU-002: lo que no se reconoce se reporta   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Módulo** | Importación |
| **Épica / HU** | [EP-010](../../epica.md) · [HU-002](../HU-002-reportar-lo-no-reconocido.md) |
| **Versión del producto** | 1, fase F de ocho. **La última** |
| **Última actualización** | 2026-08-25 |
| **Veredicto de las pruebas** | Cumple. 8 de 8 casos aprobados en el ciclo 2, en [resultado_pruebas.md](resultado_pruebas.md) |

---

## 1. En qué estación va

**Estación actual:** cerrada. **Última puerta pasada:** 9, el commit `4573a15`.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | 👤 La HU-002 aprobada el 2026-08-25 | ☑ |
| 2 | Disparo / autorización de inicio | 👤 El usuario pidió seguir, el 2026-08-25 | ☑ |
| 3 | Diseño del plan detallado | Los dos planes escritos | ☑ |
| 4 | Pausa y presentación | Presentados y leídos | ☑ |
| 5 | Aprobación del plan detallado | 👤 «si», el 2026-08-25 | ☑ |
| 6 | Ejecución continua | El reporte guardado, enlazado y visible | ☑ |
| 7 | Pruebas | Los ocho casos con veredicto: 8 de 8 en el ciclo 2 | ☑ |
| 8 | Cierre de la fase | [funcionalidad_implementada.md](funcionalidad_implementada.md), y la versión 1 cerrada | ☑ |
| 9 | Commit único | 👤 «si», el 2026-08-25. Commit `4573a15` | ☑ |

---

## 2. Qué falta para avanzar

**Nada: la fase cerró**, en el commit `4573a15`. Las seis tareas hechas, los ocho casos en verde con su evidencia, y el cierre escrito. **Con esto terminó la versión 1 del producto.**

**El reporte real de este repositorio:**

```
Documentos que entraron    | 1000
Que NO entraron            |    1     →  cvds/cumplimiento.md
Carpetas que no se miraron |    8     →  base/, plantillas/, historico-chat/, …
```

Y el registro de auditoría pasó de decir «1 sin reconocer» a enlazar el detalle.

**El defecto del ciclo 1 era el peor posible para esta fase.** Cuando **no entraba ningún** documento reconocido, no se escribía ni el reporte ni el registro de auditoría: justo el caso donde más falta hacen. Alguien trae un proyecto, no entra nada, y no queda constancia de que se intentó ni de por qué. Lo encontró el caso de «que NO pase», y quedó corregido con su porqué en el código.

## 3. Lo que ya se decidió

| Qué | Decisión |
|---|---|
| Dónde vive el reporte | Un documento en la carpeta del proyecto dentro de la plataforma, con su fecha |
| Qué hace el registro de auditoría | Lo **enlaza**, no repite la lista: dos copias de lo mismo se separan |
| Cuándo se escribe | **Siempre**, también cuando no quedó nada afuera. Su ausencia no distinguiría entre «salió limpio» y «no se corrió» |
| Cuántos reportes quedan | Uno por traída. Poder comparar dos es la mitad del valor |
| Qué dice además | Qué carpetas no se miraron, y por qué. Es la otra mitad de lo que no entró |
| Qué pasa con las traídas anteriores | No se inventa un reporte hacia atrás: sería afirmar sobre algo que no se observó |
| Qué se prueba | Los **cuatro** criterios, no solo el que falta. El caso más duro borra la carpeta del proyecto y pide el reporte igual |
