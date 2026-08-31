# Estado de fase — Fase `B-EP-006-HU-001-la-regla-de-privacidad-de-la-memoria` (módulo Memoria)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-006-HU-001-la-regla-de-privacidad-de-la-memoria` |
| **Módulo** | Memoria |
| **Planteamiento / Épica / HU** | [EP-006](../../epica.md) · [HU-001](../HU-001-que-se-guarda-tipos-y-alcances.md) |
| **Última actualización** | 2026-08-30 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ✅ Se buscó la regla que faltaba y se comprobó que no existía |
| 2 | Proponente · alcance | 👤 alcance aprobado | ✅ 2026-08-30 |
| 3 | Escritor de épica | 👤 épica aprobada | ✅ Ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ✅ Ya existía |
| 5 | Escritor de especificación | 👤 especificación aprobada | ✅ El usuario decidió que la regla se escriba, y dónde |
| 6 | Diseñador | diseño coherente | ✅ Va en `04`, no en `13` |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ✅ |
| 8 | Implementador | implementado + pruebas verdes | ✅ `validar.py metareglas` sin incumplimientos |
| 9 | Verificador | trazabilidad sin faltantes | ✅ 4 tareas, 4 con resultado |
| 10 | Crítico | sin hallazgos graves | ✅ |
| 11 | Cierre documental + señales | docs y señales al día | ✅ |
| 12 | Commit | 👤 autorizado | ✅ `c6068ff` |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 1 de 1, el transversal de privacidad |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | La mitad de la regla no es comprobable por programa, y queda declarado |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §2 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 · comprobar que la regla no existe | Terminada | `13·DOC5` no dice nada de datos personales ni claves |
| T-02 · escribir `04·S19` | Terminada | 303 caracteres de cuerpo, para un molde de 320 |
| T-03 · clasificarla en el registro de validables | Terminada | Mitad validable, mitad criterio humano, con el porqué |
| T-04 · versionar y declarar el veredicto | Terminada | `36.0.0`, MAYOR |

**Hechas:** 4 de 4. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  `13·DOC5`

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Un dato en la memoria no envejece: se vuelve a leer en cada sesión | El cuerpo de `04·S19` |
| La regla va en seguridad, no en documentación | §5 del cierre |

---

## 3. Pendiente / preguntas abiertas

- **La autorización del commit**, que se pide aparte.
- Apuntar `enmascarar.py` también a la memoria, que es la mitad comprobable.

---

## 4. Si se bloqueó

No se bloqueó.
