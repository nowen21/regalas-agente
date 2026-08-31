# Estado de fase — Fase `A-EP-005-HU-012-que-cada-regla-del-nucleo-diga-quien-la-hace-cumplir` (módulo Automatismos — enganches)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-005-HU-012-que-cada-regla-del-nucleo-diga-quien-la-hace-cumplir` |
| **Módulo** | Automatismos — enganches |
| **Planteamiento / Épica / HU** | [EP-005](../../epica.md) · [HU-012](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md) |
| **Última actualización** | 2026-08-31 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ La medición abrió la fase: 18 reglas, 14 sin quién las ejecute |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ 2026-08-31 — *«no las deje como pendiente de una solución»* |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-005 ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ HU-012, del 2026-08-17 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ (la redacción de los CA es la especificación funcional, `02·F19`) |
| 6 | Diseñador | diseño coherente | ☑ La declaración va en la regla, no en un catálogo aparte |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-08-31, **después de construir**: así quedó y así se anota |
| 8 | Implementador | implementado + pruebas verdes | ☑ 51 pruebas nuevas, todas en verde |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ Tres defectos aparecieron y se cerraron en la fase |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ✅ `8946e8c` |
| 13 | Publicación / despliegue | 👤 autorizado | N/A — el estándar no se despliega |

> **La estación 7 se firmó después de construir, y esta fase lo dice de frente.** La pieza de redacción (`redaccion.py` y su enganche) se construyó **antes** de que existieran estos cinco documentos, dentro de la misma jornada y bajo la aprobación que el usuario dio en el chat: *«una sola pieza», y la respuesta fue «si»*. El resto —la comprobación, las dieciocho declaraciones, el molde— sí salió del plan escrito. `02·F4` pide la aprobación explícita **antes**, y acá llegó al final: queda anotado para que la fase no se lea como si el orden se hubiera cumplido.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 4 de 4, más los 2 requisitos no funcionales |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno. Los tres que aparecieron se cerraron acá |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Terminada | Sección 6 de `estructura-regla.md`, con las dos aperturas y su tabla |
| T-02 | Terminada | `validadores/ejecutable.py` |
| T-03 | Terminada | `validar.py ejecutable`, y **detiene el `pre-push`** |
| T-04 | Terminada | 8 pruebas del CA-01 |
| T-05 | Terminada | El motivo se exige con un largo mínimo, escrito con su porqué |
| T-06 | Terminada | 4 pruebas del CA-02 |
| T-07 | Terminada | La pieza se resuelve contra el disco por su ruta desde la raíz |
| T-08 | Terminada | 5 pruebas del CA-03 |
| T-09 | Terminada | `validadores/redaccion.py`, con el umbral tomado de `brevedad.HOLGADO` |
| T-10 | Terminada | `adaptadores/claude-code/hook_redaccion.py` |
| T-11 | Terminada | Declarado en el instalador; el enganche corriendo en esta misma sesión |
| T-12 | Terminada | **18 de 18**, con un guion para que las dieciocho quedaran iguales |
| T-13 | Terminada | El catálogo dice que `ID8`, `ID9` e `ID10` ya tienen quien las mida |
| T-14 | Terminada | 27 pruebas de la pieza de redacción y su enganche |
| T-15 | Terminada | El mensaje nombra la regla, dice qué falta y dónde se escribe |
| T-16 | Terminada | Dos corridas dan la misma lista |
| T-17 | Terminada | Versión y entrada del registro de cambios |

**Hechas:** 17 de 17. **Bloqueadas:** ninguna.

**Un archivo apareció que el plan no declaraba** (`02·F8`): `validadores/metareglas.py`. La línea nueva le caía dentro del cuerpo de la regla, así que ocho reglas del capítulo `00` empezaron a reprobar el largo del molde y catorce sellos se dieron por vencidos, sin que ninguna hubiera cambiado lo que exige. Se reportó, se agregó al §2.1 del plan y se arregló ahí mismo.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Una regla escrita **informa** y un programa **ejecuta**, y el estándar no distinguía las dos: catorce de dieciocho reglas del núcleo no tenían quién las ejecutara, y ninguna lo decía | [`S-093`](../../../../senales.md) |
| Una línea nueva dentro de un archivo de reglas la miran cuatro comprobaciones distintas, y ninguna sabía que existía | [`S-094`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- Nada. **El aviso a `shopnest-mesa` lo autorizó el usuario el 2026-08-31** y se escribió en el pendiente 22 de ese proyecto, que es donde el caso se reportó.

---

## 4. Si se bloqueó

No se bloqueó.
