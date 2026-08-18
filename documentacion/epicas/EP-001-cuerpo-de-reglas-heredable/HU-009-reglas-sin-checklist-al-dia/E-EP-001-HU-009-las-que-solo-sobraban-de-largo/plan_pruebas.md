# Plan de Pruebas — Fase E-EP-001-HU-009: las que solo sobraban de largo

**Para qué sirve este documento.** Dice **con qué casos se comprueba** lo construido. Se aprueba antes de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el [resultado_pruebas.md](resultado_pruebas.md).

| Campo | Valor |
|---|---|
| **Código** | PP-E-EP-001-HU-009 |
| **Versión** | 1.0 |
| **Fecha** | 2026-08-18 |
| **Aprobado por** | Pendiente — el usuario |

---

## 3. Estrategia de pruebas

### 3.1 Niveles

| Nivel | Objetivo | Ambiente |
|---|---|---|
| Medición | Que las diez quepan de verdad, no de estimación | El cuerpo de reglas, por programa |
| Documental | Que ninguna exigencia se haya ido con el texto | Lectura punto por punto |
| Sobre el cuerpo real | Que el conteo baje exactamente diez | El repositorio |
| Regresión | Que nada del repositorio deje de pasar | Las dos suites |

**Acortar es el cambio que más fácil se hace mal sin que se note.** Un texto más corto se lee mejor, así que el resultado *parece* mejor aunque falte una exigencia. Por eso la comprobación central no es que quepa —eso lo dice un programa— sino **que lo que se fue fuera explicación**, y eso se lee.

### 3.2 Técnicas

- **Punto por punto, antes y después.** Cada viñeta y cada frase imperativa del texto viejo tiene que estar en el nuevo o ser reconociblemente un porqué.
- **Medición por programa después de cada corte**, no estimación. Ya costó un sello en esta misma historia.
- **Conteo exacto** del cuerpo, como red contra el cambio no declarado.

### 3.5 Alcance de la corrida

`validadores/tests/` entera, `validadores/pruebas.py` entera, `validar.py estandar` y `validar.py metareglas`.

---

## 5. Matriz de trazabilidad

| CA / exigencia | Caso | Estado |
|---|---|---|
| CA-01 · las diez caben | [CP-001](#cp-001--las-diez-caben-medidas-no-estimadas) | ☐ |
| CA-01 · las diez en CUMPLE | [CP-002](#cp-002--las-diez-pasan-a-cumple) | ☐ |
| Ninguna exigencia se pierde | [CP-003](#cp-003--cada-exigencia-del-texto-viejo-sigue-en-el-nuevo) | ☐ |
| `20·M8` · las excepciones intactas | [CP-004](#cp-004--las-excepciones-no-se-tocaron) | ☐ |
| Trazabilidad · el sello dice qué se fue | [CP-005](#cp-005--cada-sello-dice-qué-se-fue) | ☐ |
| No regresión · el conteo | [CP-006](#cp-006--el-conteo-baja-exactamente-diez) | ☐ |
| No regresión · las suites | [CP-007](#cp-007--nada-de-lo-que-ya-estaba-deja-de-pasar) | ☐ |

**Cobertura:** 7 de 7 exigencias con caso = 100%.

---

## 6. Casos de prueba

### CP-001 — Las diez caben, medidas y no estimadas

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Medir el cuerpo de las diez por programa | Las diez ≤ 320 |

> **La medición es el caso, no el trámite.** La primera reescritura dejó cinco todavía pasadas y una necesitó tres pasadas. Un sello firmado sobre un largo estimado hereda el error de quien estimó — ya pasó en esta historia.

---

### CP-002 — Las diez pasan a CUMPLE

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `validar.py metareglas` | Ninguna de las diez aparece en NO CUMPLE |

---

### CP-003 — Cada exigencia del texto viejo sigue en el nuevo

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `03·D3`: los tres puntos de migración | Los tres, incluido documentar cuando la reversión no recupera |
| 2 | `04·S1`: punto de entrada, alcance, permiso propio | Los tres |
| 3 | `04·S2`: validar, escapar, lista blanca, archivos | Los cuatro |
| 4 | `17·I1`: vacío, cargando, error | Los tres |
| 5 | `01·C13`: chat abierto, cuándo sí el formulario, en duda abierto | Los tres |
| 6 | El resto | Cada frase imperativa del viejo está en el nuevo |

> **Es el caso que separa acortar de aflojar.** Un texto más corto se lee mejor y por eso parece mejor aunque falte algo: sin este paso, la fase no se distingue de haber recortado el estándar.

---

### CP-004 — Las excepciones no se tocaron

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | La excepción de `09·G9` | Conserva **condición y límite** |
| 2 | La de `01·C11` —verificar ante duda real— | Entera |

> Una excepción es lo único de una regla que no se puede resumir sin cambiar qué permite.

---

### CP-005 — Cada sello dice qué se fue

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer los diez bloques nuevos | Cada uno dice de cuánto a cuánto **y qué texto salió** |

> Quien lea dentro de un año necesita saber si lo que falta **se perdió o se movió**. Un sello que solo dice «se acortó» obliga a ir al historial.

---

### CP-006 — El conteo baja exactamente diez

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Reglas en NO CUMPLE antes y después | **70 → 60** |

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
| **Crítica** | Que una exigencia desaparezca al acortar | Inmediato |
| **Alta** | Que una excepción cambie qué permite | Inmediato |
| **Media** | Un sello con el largo mal medido | Antes de cerrar |

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Exigencias perdidas | **0** |
| Excepciones alteradas | **0** |
| Reglas que siguen pasadas del molde | **0** de las diez |
| Sellos con el largo sin remedir | **0** |
| Cobertura de exigencias | 100% — 7 de 7 |

Un solo concepto: **Cumple** o **No cumple**.
