# Estado de fase — Fase `A-EP-005-HU-018-el-enganche-avisa-al-escribir-afuera` (módulo Enganches)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-005-HU-018-el-enganche-avisa-al-escribir-afuera` |
| **Módulo** | Enganches |
| **Planteamiento / Épica / HU** | [EP-005](../../epica.md) · [HU-018](../HU-018-los-guiones-de-apoyo-quedan-en-el-repositorio.md) |
| **Última actualización** | 2026-08-27 |

---

## 1. En qué estación va

**Estación actual:** 13 · Publicación. **Última puerta pasada:** 12, en `ef22e79`.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ✅ |
| 2 | Proponente · alcance | 👤 alcance aprobado | ✅ Salidas 1 y 3 del pendiente 89 |
| 3 | Escritor de épica | 👤 épica aprobada | ✅ Ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ✅ 2026-08-27 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ✅ `02·F19`: la redacción del CA |
| 6 | Diseñador | diseño coherente | ✅ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ✅ 2026-08-27 |
| 8 | Implementador | implementado + pruebas verdes | ✅ 466 de 466 |
| 9 | Verificador | trazabilidad sin faltantes | ✅ 9 tareas, 9 con resultado |
| 10 | Crítico | sin hallazgos graves | ✅ Cinco sabotajes, seis defectos encontrados |
| 11 | Cierre documental + señales | docs y señales al día | ✅ `S-062` |
| 12 | Commit | 👤 autorizado | ✅ `ef22e79` |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 5 de 5 |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno. `DEF-01` a `DEF-06` corregidos |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §2 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-00 · impacto sobre las pruebas del instalador | Terminada | Ninguna compara la lista completa: se pudo seguir |
| T-01 · decir si la ruta está dentro | Terminada | Por tramos, no por prefijo |
| T-02 · el enganche | Terminada | Cualquier fallo termina en silencio y código 0 |
| T-03 · que el instalador lo cuelgue | Terminada | Con prueba que lo comprueba |
| T-04 · la regla en `base/` | Terminada | `04·S18`, tras enumerar los 18 identificadores |
| T-05 · los cinco CA | Terminada | 16 pruebas, **9 de que NO avise** |
| T-06 · correrlo de verdad | Terminada | Avisa afuera, calla adentro, no borra |
| T-07 · `CHANGELOG` y `VERSION` | Terminada | `35.4.0`, MENOR |
| T-08 · sabotear | Terminada | Cinco; dos pasaron en verde y obligaron a un segundo ciclo |

**Hechas:** 9 de 9. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Hay tres formas de que una prueba mienta en verde, y ninguna se ve leyéndola | [`S-062`](../../../../senales.md) |
| Ante la duda no se acusa: un aviso falso apaga el enganche entero | `04·R4`, y el §5 del cierre |
| Una regla que solo vive en un recuerdo se deja de cumplir al día siguiente | [`S-057`](../../../../senales.md), que originó esta historia |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del `push`**, que se pide aparte del commit.
- **Lo que se escribe por `Bash` no se ve.** Declarado, no descubierto: la herramienta no entrega esa ruta.

---

## 4. Si se bloqueó

No se bloqueó.

**Un archivo de más, declarado:** `validadores/reglas-validables.md`, que el plan no nombraba. Lo exigió `M9` al agregar la regla — toda regla declara si es validable — y lo cobró `validar.py metareglas`. Se dice acá y en el §2.2 del cierre en vez de callarlo (`02·F8`).
