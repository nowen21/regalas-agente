# Plan de Pruebas — Fase C-EP-001-HU-009: las tres reglas con nombre propio

**Para qué sirve este documento.** Dice **con qué casos se comprueba** lo construido. Se aprueba antes de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el [resultado_pruebas.md](resultado_pruebas.md).

| Campo | Valor |
|---|---|
| **Código** | PP-C-EP-001-HU-009 |
| **Versión** | 1.0 |
| **Fecha** | 2026-08-18 |
| **Aprobado por** | Pendiente — el usuario |

---

## 3. Estrategia de pruebas

### 3.1 Niveles

| Nivel | Objetivo | Ambiente |
|---|---|---|
| Unitarias | Que el detector encuentre lo que se le escapaba **y calle lo que se conserva** | Textos de mentira |
| Sobre el cuerpo real | Que solo quede el caso declarado | El repositorio |
| Documental | Que ninguna de las cuatro cambie de norma | Comparación exigencia por exigencia |
| Regresión | Que el conteo de NO CUMPLE no se mueva | Las dos suites |

**Lo que hay que probar no es sobre todo qué se quitó: es qué se conserva y por qué.** Tres nombres se quedan a propósito, y sin un caso que lo escriba **la próxima pasada los borra creyendo que mejora**. Un plan de pruebas que solo comprueba lo que se sacó deja el criterio en la cabeza de quien lo tomó.

### 3.2 Técnicas

- **Un caso por nombre que se conserva**, con el motivo en el propio caso.
- **Casos de borde de palabra**, porque `react` dentro de «reaccionar» y `node` dentro de «nodo» son falsos positivos que el detector tiene que evitar en español.
- **Una prueba contra `base/` que no exige cero**, sino exactamente la lista declarada.

### 3.5 Alcance de la corrida

`validadores/tests/` entera, `validadores/pruebas.py` entera, `validar.py estandar` y `validar.py metareglas`.

---

## 5. Matriz de trazabilidad

| CA / exigencia | Caso | Estado |
|---|---|---|
| CA-01 · lo que ya se detectaba sigue detectándose | [CP-001](#cp-001--los-nombres-que-ya-estaban-en-la-lista) | ☐ |
| CA-01 · `node` no estaba | [CP-002](#cp-002--node-no-estaba-en-la-lista) | ☐ |
| CA-01 · `SoftDeletes` tampoco | [CP-003](#cp-003--softdeletes-tampoco-estaba) | ☐ |
| Criterio · los nombres del oficio se quedan | [CP-004](#cp-004--los-nombres-del-oficio-no-se-reportan) | ☐ |
| Criterio · el vocabulario del estándar no es stack | [CP-005](#cp-005--las-palabras-de-esta-casa-no-se-reportan) | ☐ |
| Ruido · bordes de palabra en español | [CP-006](#cp-006--no-se-reporta-una-palabra-dentro-de-otra) | ☐ |
| CA-01 · el cuerpo real | [CP-007](#cp-007--en-base-solo-queda-el-declarado) | ☐ |
| No regresión · ninguna norma cambia | [CP-008](#cp-008--ninguna-de-las-cuatro-cambia-de-norma) | ☐ |
| No regresión · las suites | [CP-009](#cp-009--nada-de-lo-que-ya-estaba-deja-de-pasar) | ☐ |

**Cobertura:** 9 de 9 exigencias con caso = 100%.

---

## 6. Casos de prueba

### CP-001 — Los nombres que ya estaban en la lista

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Un cuerpo que diga `Django`, `SQLite`, `MariaDB`, `React`, `php` | Uno reportado por cada uno |

---

### CP-002 — `node` no estaba en la lista

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Un cuerpo que diga «todos los `node`» | Se reporta |

> Es lo que `04·S10` decía, junto con `php`. **Solo se reportaba el segundo**, y por eso el sello pudo dar la fila por buena: el programa callaba la mitad.

---

### CP-003 — `SoftDeletes` tampoco estaba

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Un cuerpo que diga `` `destroy()`, `SoftDeletes` `` | Se reporta |

> `04·S11` lo nombra y su sello ya lo tenía anotado como pendiente. Lo que cambia es que **ahora el programa dice lo mismo que el sello**, en vez de callar.

---

### CP-004 — Los nombres del oficio no se reportan

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `killall`, `pkill -f`, `taskkill /IM` | **Ninguno se reporta** |

> **Es el caso que más importa de los nueve.** No son producto ni framework: son cómo se llama la misma acción en cada sistema, y quitarlos deja a `04·S10` sin decir qué prohíbe. Sin este caso, la próxima pasada los borra creyendo que mejora.

---

### CP-005 — Las palabras de esta casa no se reportan

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | «La fase declara su historia, y la migración documenta por qué» | No se reporta |

> Fase, historia, épica, catálogo, migración son el vocabulario del estándar, no de un stack.

---

### CP-006 — No se reporta una palabra dentro de otra

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | «el usuario puede **reaccionar** al aviso» | No se reporta |
| 2 | «el **nodo** del árbol» | No se reporta |

> Los dos son español corriente que contiene el nombre de una tecnología. Sin bordes de palabra, agregar `node` a la lista habría empezado a reportar «nodo» en todo el capítulo `03`.

---

### CP-007 — En `base/` solo queda el declarado

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr el detector sobre las 200 reglas | Exactamente `{S11}` |

> **No se exige cero, a propósito.** `S11` queda vivo y su sello dice por qué: ahí el nombre del método **es el argumento**. Exigir cero obligaría a arreglarlo a medias para que la prueba pase — justo lo que su sello decidió no hacer.

---

### CP-008 — Ninguna de las cuatro cambia de norma

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer las cuatro antes y después, exigencia por exigencia | La misma exigencia, dicha sin nombre propio |
| 2 | Contar las reglas en NO CUMPLE | **El mismo número** |

> El paso 2 es el que fija el alcance. Si bajara, esta fase habría arreglado otra fila sin decirlo; si subiera, habría roto algo.

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
| **Crítica** | Que una de las cuatro cambie lo que exige | Inmediato |
| **Alta** | Que el detector reporte español corriente | Antes de cerrar |
| **Media** | Que el texto en concepto quede peor de leer | Se reporta |

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Reglas de `base/` que nombran stack sin declararlo | **0** |
| Reglas que cambian de norma | **0** |
| Falsos positivos en español corriente | **0** |
| Reglas en NO CUMPLE, antes y después | **igual** |
| Cobertura de exigencias | 100% — 9 de 9 |

Un solo concepto: **Cumple** o **No cumple**.
