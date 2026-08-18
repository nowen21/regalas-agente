# Estado de fase — A-EP-001-HU-011: la regla de buscar antes de preguntar

## 0. Identificación

| Campo | Valor |
|---|---|
| **Módulo** | Cuerpo de reglas — capítulo `01` |
| **Épica / HU / Pendiente** | [EP-001](../../epica.md) · [HU-011](../HU-011-buscar-antes-de-preguntar.md) · [pendiente 24](../../../../../pendientes/24-buscar-en-el-repositorio-antes-de-preguntar.md) |
| **Última actualización** | 2026-08-18 |

---

## 1. En qué estación va

**Estación actual:** 9 — commit único. **Última puerta pasada:** 8.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 «siga», con el pendiente 24 abierto en el editor | ☑ |
| 3 | Diseño del plan detallado | los dos planes escritos | ☑ |
| 4 | Pausa y presentación | presentados | ☑ |
| 5 | Aprobación del plan detallado | 👤 tomada del «siga» sostenido de la sesión | ☑ |
| 6 | Ejecución continua | la regla escrita | ☑ |
| 7 | Pruebas | veredicto **Cumple**, ciclo 1 | ☑ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☑ |
| 9 | Commit único | 👤 **acá está detenida** | ☐ |
| 10 | Reporte al usuario | | ☐ |
| 11 | Publicación / despliegue | 👤 | ☐ |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 3 de 3 |
| **CA en "No"** | ninguno |
| **Defectos abiertos aceptados** | uno: la comprobación de la cita, fuera del alcance declarado |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §5 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Hecha | El mayor del capítulo era `C22` |
| T-02 | Hecha | `C23`, con el molde de `M5` |
| T-03 | Hecha | 20 filas: 19 ✅ · 0 ❌ · 1 N/A |
| T-04 | Hecha | 368 → 271 → 311 de 320 |
| T-05 | Hecha | Clasificada con su motivo |
| T-06 | Hecha | Ninguna corrida cambió |
| T-07 | Hecha | 23.5.0, **MENOR** |

**Hechas:** 7 de 7.

---

## 2. Decisiones y señales generadas

| Decisión / aprendizaje | Dónde queda |
|---|---|
| El orden de búsqueda sale de dónde el estándar ya manda escribir cada cosa, no de una preferencia | Plan §2.7 y el cierre |
| Extiende `C7` en vez de repetirla: aquella da por hecho que el dato no está | Bloque de checklist, fila 2 |
| **El plan de pruebas encontró el CA sin cubrir que la lectura daba por cubierto** | [resultado_pruebas.md](resultado_pruebas.md) §2 |
| El porqué del orden no cabía en la regla y se fue a la historia | Bloque de checklist, fila 10 |

---

## 3. Pendiente / preguntas abiertas

- **El commit.** Lo autoriza el usuario aparte, y es lo único que detiene la fase.
- **La mitad comprobable de `C23` no tiene programa.** Es su propia fase, y sin ella la regla depende de que el agente se acuerde.

---

## 4. Si se bloqueó

No se bloqueó. Las dos correcciones —el CA sin cubrir y el cuerpo que no cabía— las destaparon los propios casos de prueba antes de cerrar.
