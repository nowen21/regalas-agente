# Resultado de Pruebas — Fase `C-EP-004-HU-021-cualquier-encabezado-de-veredicto-se-lee`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, caso por caso, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `C-EP-004-HU-021-cualquier-encabezado-de-veredicto-se-lee` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-27 |
| **Ciclo** | 2. **El primero dejó un sabotaje en verde**, y eso costó una prueba nueva |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los dos títulos que sirven se leen, los cinco que se les parecen no, y las diez historias se recuperaron **con las tres que dicen «No cumple» entre ellas**, que era la mitad exigida.

| Métrica | Meta | Real |
|---|---|---|
| Casos ejecutados | 4 de 4 | 4 de 4 |
| Títulos que se leen | 2 de 2 | 2 de 2 |
| Títulos parecidos leídos por error | 0 de 5 | **0 de 5** |
| Pruebas de `A` y `B` que hubo que tocar | 0 | **0** |
| Historias recuperadas | exactamente 10 | **10** |
| **De ellas, con «No cumple»** | exactamente 3 | **3** |
| Sabotajes cazados | Todos | **4 de 4** — el cuarto, tras agregar la prueba que faltaba |
| Fallas en la suite completa | 0 | 0, sobre **434 pruebas** |

---

## 3. Resultado por caso

### CP-001 — El título que sirve se lee

| Paso | Resultado |
|---|---|
| `## 5. Veredicto` + `**Cumple.**` | Se lee `Cumple` |
| Lo mismo con `**No cumple.**` | Se lee `No cumple` |
| `## 2. Veredicto de la fase`, que ya servía | Se sigue leyendo |
| Números de encabezado distintos, con y sin punto | Se lee igual en los tres |

### CP-002 — Los cinco títulos parecidos no se leen

| Título que se le puso delante | Qué hizo |
|---|---|
| **`Veredicto por criterio de aceptación`, con `Cumple` en la primera fila** | **No lo leyó** |
| `Veredicto por criterio de aceptación y requisito no funcional` | No lo leyó |
| `Veredicto final` | No lo leyó |
| `Veredicto por exigencia` y `Veredicto por criterio de la historia` | No los leyó |
| `Veredicto` con nada debajo | No lo leyó |

**El primero es el que decide si esta fase sirve.** Cuarenta fases escriben ese título, y su tabla dice `Cumple` en la primera fila. Un patrón que lo tomara devolvería **el primer criterio** como veredicto de la fase — y mentiría en la dirección optimista, que es peor que el defecto corregido.

### CP-003 — Lo de antes no se rompió

Las **22 pruebas** de las fases `A` y `B` pasan **sin haberlas tocado**, y `veredicto_de` y `por_veredicto` conservan su firma.

**Y ninguna historia que ya tenía veredicto lo cambió.** Se midió antes de escribir el código y se repitió después: cero cambios. La cuenta lo confirma sola — `56 + 13 = 69` antes, `63 + 16 = 79` después: **exactamente las diez que salieron de «no dicen»**, sin trasvase entre las otras dos.

### CP-004 — Las diez, una por una

| Historia | Adónde fue |
|---|---|
| `EP-001 · HU-009` reglas sin checklist al día | Cumple |
| `EP-002 · HU-005` sellar el trabajo cerrado | Cumple |
| `EP-004 · HU-009` conteo por regla | Cumple |
| `EP-004 · HU-013` comparar el plan con lo hecho | Cumple |
| `EP-004 · HU-016` el pendiente cerrado nombra su fase | Cumple |
| `EP-005 · HU-011` dónde termina el estándar | Cumple |
| `EP-007 · HU-005` no pisar lo escrito | Cumple |
| **`EP-001 · HU-007` la regla de las reglas** | **No cumple** |
| **`EP-003 · HU-002` modelos del encargo** | **No cumple** |
| **`EP-005 · HU-001` transcripción de la sesión** | **No cumple** |

**Las cinco que de verdad no lo dicen:** `EP-003 · HU-001` marca de espacio por llenar · `EP-003 · HU-009` modelo del resumen de sesión · `EP-003 · HU-010` glosario de la terminología · `EP-005 · HU-015` lo que llega de afuera llega marcado · `EP-005 · HU-016` la traza de la sesión paso a paso.

**La línea, antes y después:**

| Antes | Ahora |
|---|---|
| `56 cumplen, 13 no cumplen, 15 no dicen` | `63 cumplen, 16 no cumplen, 5 no dicen` |

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Los sabotajes

Cuatro, restaurados **con copia**. **Tres cazados al primer intento; el cuarto pasó en verde.**

| # | Qué se rompió | Ciclo 1 | Ciclo 2 |
|---|---|---|---|
| 1 | El patrón nuevo se cae de la cadena | Cazado (3) | Cazado (3) |
| 2 | El título se afloja y admite «por criterio» | Cazado (3) | Cazado (3) |
| 3 | Se reemplaza en vez de sumar | Cazado (9) | Cazado (9) |
| 4 | La palabra ya no tiene que ir pegada al encabezado | **Verde** | **Cazado (1)** |

### 4.2 El sabotaje en verde tenía dos diagnósticos, y se corrió el escenario para elegir

Un sabotaje que no rompe nada significa **o que falta una prueba, o que la exigencia sobra**. Los dos se ven igual en el reporte.

Se miró el caso concreto: aflojar el patrón para que la palabra pueda estar **en cualquier parte** después del encabezado. Las pruebas que había ponían `Cumple` **justo debajo**, o no lo ponían en ninguna parte. **Faltaba el caso de en medio**, y es el que ocurre de verdad: un encabezado de veredicto seguido de prosa, con la palabra más abajo dentro de una tabla de criterios.

Escrita la prueba, el sabotaje 4 **la rompe**. Era hueco de cobertura, no exigencia sobrante.

### 4.3 Un defecto del propio guion de sabotaje

Su guardia final decía `if "OK" not in final`. **La salida de los validadores trae «OK: sin incumplimientos.»**, así que el guion habría dado por buena una corrida con fallas — y de hecho **la dio**: el ciclo 1 terminó con `FAILED (failures=3)` y el guion salió con código 0.

Es `S-044` otra vez, en forma nueva: allá el guion no corría nada y decía OK; acá corre y no sabe leer el resultado. Corregido: se exige la línea que `unittest` escribe sola, exactamente `OK`, y que haya una línea `Ran ` distinta de cero.

### 4.4 Las tres fallas del ciclo 1, y por qué no eran defectos

`Enlaces`, `FormatoDelHallazgo` y `NumeracionDePendientes` fallaron. **Una sola causa:** este documento y el de cierre todavía no estaban escritos, y el `estado-fase` y el plan ya los enlazaban. Dos enlaces rotos hacían que `validar.py estandar` saliera con código 1, y las tres pruebas dependen de eso.

**Se comprueba escribiéndolos**, que es lo que cierra la fase. Escritos, `validar.py estandar` vuelve a `OK` y la corrida final da **434 pruebas en verde**, que es lo que dice la tabla del §2.

### 4.5 Rastros

**Uno, y se declara.** El guion de sabotaje guarda su copia de restauración en la carpeta temporal del sistema, igual que los guiones anteriores del repositorio. Se borró al terminar. **Es un resto de lo mismo que destapó `S-057`**, y queda anotado en el [pendiente 89](../../../../../pendientes/89-nada-hace-cumplir-que-los-guiones-queden-en-el-repositorio.md): la regla dice «nada se escribe por fuera», y una copia de respaldo también es escribir.

### 4.6 Ninguna prueba usa credenciales

Ni reales ni inventadas (`00·N6`).

---

## 5. Defectos encontrados

| # | Qué | Severidad | Estado |
|---|---|---|---|
| DEF-01 | Faltaba la prueba del caso de en medio: el sabotaje 4 pasaba en verde | Media — cobertura, no código | **Corregido.** Prueba escrita, sabotaje cazado |
| DEF-02 | La guardia del guion de sabotaje aceptaba «OK: sin incumplimientos.» como corrida limpia | Alta — **reporta bien un resultado malo** | **Corregido.** Se exige la línea `OK` sola |

**El DEF-02 es el que más vale**, porque es de la herramienta que juzga: un guion que aprueba corridas rojas invalida todo lo que dijo antes.

---

## 6. Evidencias

- `_VEREDICTO_TITULO_SOLO` en `validadores/fases.py`, con los seis títulos y su cuenta escritos al lado
- Nueve pruebas nuevas: tres de lo que se lee, seis de lo que **no**
- Los guiones que enumeraron y midieron, en [historico-chat/scripts/2026-08-27/](../../../../../historico-chat/scripts/2026-08-27/)
- La línea del inventario, antes y después, y las diez nombradas una por una
