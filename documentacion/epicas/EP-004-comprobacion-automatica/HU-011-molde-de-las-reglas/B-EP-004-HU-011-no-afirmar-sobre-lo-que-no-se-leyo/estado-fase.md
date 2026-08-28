# Estado de fase — Fase B-EP-004-HU-011-no-afirmar-sobre-lo-que-no-se-leyo (módulo Programas de comprobación)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-004-HU-011-no-afirmar-sobre-lo-que-no-se-leyo` |
| **Módulo** | Programas de comprobación |
| **Épica / HU** | `EP-004` · `HU-011` |
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
| 12 | Commit | 👤 autorizado | ✅ `da94174` |
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
| `--raiz` rechaza lo que no es el estándar | Cambiar lo que significa la bandera obliga a revisar quién la llama hoy; rechazar es barato y quita el veredicto falso |
| El aviso nombra la bandera correcta | Sin decirla, el aviso deja a quien lo lee igual de perdido |
| Sin el dato no se afirma | La lectura devuelve vacío cuando el archivo no está, así que atrapar el error de disco no bastaba |

---

## 3. Pendiente / preguntas abiertas

- Falta la autorización del usuario para el commit.
- Lo que la fase no cubre: no se revisaron los demás subcomandos. `--raiz` significa «el proyecto» en casi todos, y si el mismo problema aparece en otro sale como pendiente aparte.

---

## 4. Si se bloqueó

No se bloqueó.
