# Plan de Pruebas — Fase D-EP-001-HU-009: enlazar en vez de repetir

**Para qué sirve este documento.** Dice **con qué casos se comprueba** lo construido. Se aprueba antes de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el [resultado_pruebas.md](resultado_pruebas.md).

| Campo | Valor |
|---|---|
| **Código** | PP-D-EP-001-HU-009 |
| **Versión** | 1.0 |
| **Fecha** | 2026-08-18 |
| **Aprobado por** | Pendiente — el usuario |

---

## 3. Estrategia de pruebas

### 3.1 Niveles

| Nivel | Objetivo | Ambiente |
|---|---|---|
| Documental | Que lo que cada regla exigía siga exigido, por ella o por su vecina | El cuerpo de reglas |
| Sobre el cuerpo real | Que las dos queden en CUMPLE y ninguna otra se mueva | El repositorio |
| Regresión | Que nada del repositorio deje de pasar | Las dos suites |

**Acá se prueba leyendo, y hay que decirlo.** No hay programa que compruebe si una frase que se quitó seguía haciendo falta: eso lo decide quien lee las dos reglas juntas. Lo que sí se puede medir —y es lo que se mide— es que **el conteo baje exactamente dos**: ni uno menos, que sería no haber cerrado; ni uno más, que sería haber tocado algo que no era.

### 3.2 Técnicas

- **Lectura frase por frase**, comparando antes y después con la regla prestada delante.
- **Conteo exacto**, como red contra el cambio que no se declaró.
- **Comparación con el modelo**: `Q7` contra `14·EST3`, que ya cumplía la misma fila sobre la misma regla prestada.

### 3.5 Alcance de la corrida

`validadores/tests/` entera, `validadores/pruebas.py` entera, `validar.py estandar` y `validar.py metareglas`.

---

## 5. Matriz de trazabilidad

| CA / exigencia | Caso | Estado |
|---|---|---|
| CA-01 · `Q7` deja de repetir a `C3` | [CP-001](#cp-001--q7-se-queda-con-lo-suyo) | ☐ |
| CA-01 · `PR4` deja de repetir a `E5` | [CP-002](#cp-002--pr4-se-queda-con-lo-suyo) | ☐ |
| `20·M7` · la dependencia queda declarada | [CP-003](#cp-003--pr4-declara-su-dependencia) | ☐ |
| Coherencia · el ejemplo dice lo que la regla dice | [CP-004](#cp-004--el-ejemplo-de-pr4-corresponde-a-lo-que-dice-hoy) | ☐ |
| No regresión · nada se pierde | [CP-005](#cp-005--lo-que-se-quitó-sigue-rigiendo) | ☐ |
| No regresión · el conteo | [CP-006](#cp-006--el-conteo-baja-exactamente-dos) | ☐ |
| No regresión · las suites | [CP-007](#cp-007--nada-de-lo-que-ya-estaba-deja-de-pasar) | ☐ |

**Cobertura:** 7 de 7 exigencias con caso = 100%.

---

## 6. Casos de prueba

### CP-001 — `Q7` se queda con lo suyo

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer `Q7` y `01·C3` juntas | `Q7` nombra a `C3` como motivo y no repite su criterio |
| 2 | Comparar con `14·EST3` | La misma forma: la vecina entre paréntesis, lo propio en el cuerpo |
| 3 | `validar.py metareglas` | `Q7` en CUMPLE |

> **El modelo estaba en el propio cuerpo.** `EST3` toma de `C3` el mismo criterio y cumplía; `Q7` no. La diferencia entre las dos era la prueba, y estaba escrita.

---

### CP-002 — `PR4` se queda con lo suyo

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer `PR4` y `05·E5` juntas | Lo de logs lo dice `E5`; lo de pantallas y reportes, `PR4` |
| 2 | Buscar en `E5` algo sobre pantallas | **No hay** — es lo que salva a `PR4` de derogarse |
| 3 | `validar.py metareglas` | `PR4` en CUMPLE |

> Eran **tres capas del mismo criterio**: `00·N6` blindada, `05·E5` y `PR4`. La única que aporta algo propio es la mitad de pantallas.

---

### CP-003 — `PR4` declara su dependencia

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar la forma `depende de` en su cuerpo | Está, y apunta a `05·E5` |
| 2 | La comprobación de dependencias | No reporta forma inválida ni ciclo |

> La relación ya existía; lo que faltaba era **decirla** en una de las tres formas de `M7`.

---

### CP-004 — El ejemplo de `PR4` corresponde a lo que dice hoy

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer el ejemplo | Es de pantalla, no de logs |

> **Un ejemplo que ilustra lo que la regla dejó de decir es peor que ninguno**: manda a buscar la exigencia donde ya no está.

---

### CP-005 — Lo que se quitó sigue rigiendo

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Tomar cada frase eliminada y buscarla en la regla vecina | Está, dicha por su dueña |

> Es el caso que separa «dejar de repetir» de «dejar de exigir». Sin él, esta fase no se distingue de haber aflojado el estándar.

---

### CP-006 — El conteo baja exactamente dos

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Contar las reglas en NO CUMPLE antes y después | **72 → 70** |

> Ni una menos —sería no haber cerrado— ni una más —sería haber tocado algo que no era—. Es la red contra el cambio no declarado.

---

### CP-007 — Nada de lo que ya estaba deja de pasar

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `validadores/tests/` entera | Pasa |
| 2 | `validadores/pruebas.py` entera | Igual que antes |
| 3 | `validar.py estandar` | Sin incumplimientos |

---

## 9. Gestión de defectos

| Severidad | Qué sería acá | Atención |
|---|---|---|
| **Crítica** | Que una exigencia desaparezca del cuerpo entero | Inmediato |
| **Alta** | Que el conteo se mueva más o menos de dos | Antes de cerrar |
| **Media** | La redacción de la regla nueva | Se reporta |

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Exigencias que desaparecen del cuerpo | **0** |
| Reglas que cambian de veredicto | **2**, las dos de NO CUMPLE a CUMPLE |
| Otras reglas que se mueven | **0** |
| Pruebas del repositorio que dejan de pasar | **0** |
| Cobertura de exigencias | 100% — 7 de 7 |

Un solo concepto: **Cumple** o **No cumple**.
