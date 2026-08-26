# Estado de fase — Fase B-EP-002-HU-003-la-version-declarada-se-comprueba (módulo Programas de comprobación)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-002-HU-003-la-version-declarada-se-comprueba` |
| **Módulo** | Programas de comprobación |
| **Épica / HU** | `EP-002` · `HU-003` |
| **Última actualización** | 2026-08-22 |

---

## 1. En qué estación va

**Estación actual:** 11 — cierre documental. **Ejecutada y cerrada el 2026-08-22.**

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ |
| 8 | Implementador | implementado + pruebas verdes | ☑ |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ☐ |

**Sobre la puerta 7:** el usuario ordenó resolver los pendientes del 81 al 84, y esa orden se tomó como la aprobación de los planes.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | El que la fase A dejó en rojo |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno propio |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) §5 |

---

## 2. Decisiones y señales generadas

| Decisión | Por qué |
|---|---|
| Las versiones se leen del registro de cambios, no de `VERSION` | `VERSION` dice cuál es la última; la pregunta es si el número declarado existió alguna vez |
| Primero que exista, después que coincida | Mientras un número falso apague el aviso, cualquier proyecto puede quedar en silencio sin que se note |
| Cuando difieren, el mensaje nombra las dos | No se sabe cuál sin mirar, y un validador no opina |
| Sin registro legible no se acusa a nadie | Es la lección del pendiente 81: una comprobación que no pudo leer su archivo no debe afirmar nada |

---

## 3. Pendiente / preguntas abiertas

- Falta la autorización del usuario para el commit.
- Lo que la fase no cubre: no se decide qué hacer cuando las dos difieren: eso es del usuario, y lo que se pedía es que se vea. Y queda sin averiguar si el instalador escribe el registro sin actualizar la declaración, que explicaría el caso de shopnest-mesa.

---

## 4. Si se bloqueó

No se bloqueó.
