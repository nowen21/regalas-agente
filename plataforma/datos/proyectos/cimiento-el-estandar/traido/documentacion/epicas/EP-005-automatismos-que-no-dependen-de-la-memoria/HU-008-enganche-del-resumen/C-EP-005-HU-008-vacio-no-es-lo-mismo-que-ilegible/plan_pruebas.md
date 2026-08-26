# Plan de Pruebas — Fase C-EP-005-HU-008: vacío no es lo mismo que ilegible

**Para qué sirve este documento.** Dice **con qué casos se comprueba** lo construido. Se aprueba antes de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el [resultado_pruebas.md](resultado_pruebas.md).

| Campo | Valor |
|---|---|
| **Código** | PP-C-EP-005-HU-008 |
| **Versión** | 1.0 |
| **Fecha** | 2026-08-18 |
| **Aprobado por** | Pendiente — el usuario |

---

## 3. Estrategia de pruebas

### 3.1 Niveles

| Nivel | Objetivo | Ambiente |
|---|---|---|
| Unitarias | Que los dos casos se distingan y no se pisen | Resúmenes de mentira en carpetas temporales |
| Sobre el histórico real | Que ninguno de los 47 quede ilegible | El repositorio |
| Regresión | Que el aviso de vacío siga funcionando igual | Las dos suites |

**Lo que hay que probar son los dos silencios, no el aviso.** El aviso se ve; lo que no se ve es el resumen que se cuenta como vacío teniendo quince hallazgos, y el cierre que nunca se mira porque no encontró ninguno. **Los dos callan, y callar no deja rastro.**

### 3.2 Técnicas

- **El mismo archivo con y sin `H-`**, para aislar que la única diferencia es el molde.
- **Marcar un aviso y comprobar el otro**, porque con una sola marca avisar de uno apagaría el otro para siempre.
- **Los 47 resúmenes de verdad**, que es la prueba que envejece con el repositorio.

### 3.5 Alcance de la corrida

`validadores/tests/` entera, `validadores/pruebas.py` entera —se toca `resumen.py`, que ya tiene sus casos— y `validar.py estandar`.

---

## 5. Matriz de trazabilidad

| CA / exigencia | Caso | Estado |
|---|---|---|
| CA-02 · el vacío sigue diciendo vacío | [CP-001](#cp-001--el-que-no-tiene-nada-sigue-diciendo-vacío) | ☐ |
| CA-02 · el ilegible dice otra cosa | [CP-002](#cp-002--el-escrito-sin-la-h-no-se-cuenta-como-vacío) | ☐ |
| CA-02 · el aviso sirve para actuar | [CP-003](#cp-003--dice-cuántos-hay-escritos) | ☐ |
| Ruido · el resumen correcto no se toca | [CP-004](#cp-004--el-que-ya-sigue-el-molde-no-se-reporta) | ☐ |
| CA-02 · el aviso no se repite | [CP-005](#cp-005--el-aviso-no-se-repite) | ☐ |
| Límite · las dos marcas no se pisan | [CP-006](#cp-006--marcar-un-aviso-no-apaga-el-otro) | ☐ |
| Lo que el defecto tapaba | [CP-007](#cp-007--el-cierre-no-se-miraba-y-ahora-sí) | ☐ |
| CA-02 · el histórico real | [CP-008](#cp-008--ningún-resumen-del-repositorio-queda-ilegible) | ☐ |
| No regresión | [CP-009](#cp-009--nada-de-lo-que-ya-estaba-deja-de-pasar) | ☐ |

**Cobertura:** 9 de 9 exigencias con caso = 100%.

---

## 6. Casos de prueba

### CP-001 — El que no tiene nada sigue diciendo vacío

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Un resumen sin hallazgos y sin secciones numeradas | Falta `vacio` |

> Es el `CA-02` como estaba. Si esto se rompe, la fase arregló un caso y estropeó el que ya funcionaba.

---

### CP-002 — El escrito sin la `H` no se cuenta como vacío

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Un resumen con `### 1 ·` y `### 2 ·` | Falta `molde`, **no** `vacio` |

> **Los dos piden trabajo distinto:** uno, escribir el resumen; el otro, renumerar el que ya está escrito. Un aviso que confunde los dos manda a hacer lo que no es.

---

### CP-003 — Dice cuántos hay escritos

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Tres hallazgos fuera del molde | Devuelve los tres títulos |

> Es lo que permite decir «renumerá los tres que ya están» en vez de «escribí el resumen». **El número es lo que hace creíble el aviso** ante quien tiene el archivo lleno delante.

---

### CP-004 — El que ya sigue el molde no se reporta

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Un resumen con `### H-1 ·` y además un `### 2 ·` que es otra sección | No se reporta el molde |

> Un resumen correcto puede tener secciones numeradas que no son hallazgos. La comprobación solo mira **cuando no hay ni un `H-`**: si los hay, el molde se está siguiendo.

---

### CP-005 — El aviso no se repite

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Avisar, marcar, volver a preguntar | La segunda vez no falta nada |

---

### CP-006 — Marcar un aviso no apaga el otro

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Sobre un resumen vacío, marcar el aviso **del molde** | Sigue faltando `vacio` |

> **Con una sola marca compartida, avisar de uno apagaría el otro para siempre.** Y el aviso se da una vez: apagarlo por error no se recupera.

---

### CP-007 — El cierre no se miraba, y ahora sí

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Un resumen con `### 1 ·` y la sección de cierre con casillas sin marcar | Falta `molde` |
| 2 | El mismo archivo con `### H-1 ·` | Falta `cierre` |

> **Es el caso que mide el daño real.** La comprobación del cierre necesita encontrar un hallazgo antes de mirar, así que en los tres resúmenes mal numerados **nunca corrió**. Los dos pasos son el mismo archivo con una letra de diferencia.

---

### CP-008 — Ningún resumen del repositorio queda ilegible

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Recorrer los 47 resúmenes | Ninguno con hallazgos fuera del molde |

> Es la que se cae cuando alguien escriba el próximo a mano sin la `H-`.

---

### CP-009 — Nada de lo que ya estaba deja de pasar

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `validadores/tests/` entera | Pasa, con los casos nuevos |
| 2 | `validadores/pruebas.py` entera | Igual que antes |
| 3 | `validar.py estandar` | Sin incumplimientos |

---

## 9. Gestión de defectos

| Severidad | Qué sería acá | Atención |
|---|---|---|
| **Crítica** | Que marcar un aviso apague el otro | Inmediato |
| **Alta** | Que el aviso salte en resúmenes correctos | Antes de cerrar |
| **Media** | La redacción del aviso | Se reporta |

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Resúmenes del repositorio ilegibles para el programa | **0** |
| Hallazgos invisibles | **0** — eran 29 |
| Resúmenes correctos reportados por error | **0** |
| Pruebas del repositorio que dejan de pasar | **0** |
| Cobertura de exigencias | 100% — 9 de 9 |

Un solo concepto: **Cumple** o **No cumple**.
