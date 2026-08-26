# Resultado de Pruebas — Fase «A-EP-004-HU-004-la-regla-de-negocio-declara-su-origen»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. El diseño de los casos vive en el [`plan_pruebas.md`](plan_pruebas.md), que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-004-HU-004-la-regla-de-negocio-declara-su-origen` |
| **HU** | [HU-004 — Forma de los documentos](../HU-004-forma-de-los-documentos.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-16 |
| **Ejecutado por** | El agente |
| **Ambiente y versión** | Windows 11 · Python 3.11 · estándar 22.0.0 → 22.1.0 |

---

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

---

## 2. Ejecución caso por caso

### CA-04 · CP-001 — la regla sin origen se reporta, y la que lo tiene no

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Comprobar un §4 con las dos reglas reales | Sale exactamente una falla | Una |
| 2 | Ver de cuál habla | De la que no baja de ninguna parte | «Un problema **no se cierra** sin causa raíz…» |
| 3 | Leer el texto de la falla | Dice qué falta y qué hacer | Nombra el identificador que falta y manda subir la regla a su historia |
| 4 | Ponerle `D-22` y volver a comprobar | Ninguna falla | Ninguna |

**Veredicto:** ✅ Cumple.

---

### CA-04 · CP-002 — lo que no hay que reportar

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | El §4 con el molde sin llenar | Ninguna falla de este tipo | Ninguna — de eso se queja la comprobación 1 |
| 2 | Un §4 sin ninguna regla | Ninguna falla | Ninguna |
| 3 | Una regla con origen que nombra un catálogo en su texto | Ninguna falla | Ninguna |
| 4 | Un documento que no es especificación, con la misma sección | Ninguna falla | Ninguna |

**Veredicto:** ✅ Cumple. El riesgo `B-02` —falsos positivos— no se materializó.

---

### CA-04 · CP-003 — una especificación se compara contra su plantilla

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Preguntar qué plantilla le toca a un `spec.md` | La de especificación de módulo | La correcta |
| 2 | Comprobar que existe en disco | Existe | Existe |

**Veredicto:** ✅ Cumple.

**Sin este caso, todo lo demás pasaba y nada se comprobaba.** Antes de esta fase un `spec.md` no se comparaba contra ninguna plantilla: el programa no lo reconocía, así que la comprobación nueva no se habría disparado nunca. Fue el hallazgo del análisis previo, no de la corrida.

---

### CA-04 · CP-004 — los casos se ponen rojos si se revierte la comprobación

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Desactivar la comprobación nueva | Revertida | Revertida |
| 2 | Correr la suite de la fase | El CP-001 se pone rojo | Rojo: `0 != 1 : se esperaba una sola falla: []` |
| 3 | Volver a activarla y correr todo | Verde | 29 de 29 |

**Veredicto:** ✅ Cumple.

---

## 3. Defectos encontrados

Ninguno.

---

## 4. Lo que se descubrió fuera del criterio

**El riesgo `B-01` se materializó, y hay que decirlo con número.** Al reconocer `spec.md`, las dos especificaciones de este repositorio empezaron a compararse contra la plantilla:

| Especificación | Hallazgos totales | De ellos, reglas sin origen |
|---|---:|---:|
| `documentacion/automatismos/spec.md` | 18 | **16** |
| `documentacion/documentos-modelo/spec.md` | 17 | **15** |

**31 reglas de negocio del propio estándar no dicen de dónde bajan.** Es exactamente lo que la exigencia 3 del pendiente 43 pedía averiguar, y la respuesta es que el estándar no cumple la regla que acaba de escribir.

**No se corrigió acá, y no es pereza:** el plan lo declaraba fuera de alcance, y arreglarlas es decidir de dónde baja cada una — trabajo de criterio, no mecánico. Queda como pendiente propio, que es lo que `20·M11` hace con lo que aparece después de cerrar algo.

**No se calló la comprobación para que el número diera cero.** Un validador que se apaga cuando molesta no sirve para nada.

---

## 5. Cobertura contra el plan de pruebas

| Exigencia | Caso | Estado |
|---|---|---|
| CA-04 — la regla sin origen se reporta | CP-001 | ✅ |
| CA-04 — no reportar lo que no toca | CP-002 | ✅ |
| CA-04 — el documento se reconoce | CP-003 | ✅ |
| CA-04 — prueba de la prueba | CP-004 | ✅ |

**Cobertura:** 1 de 1 CA = 100%.

---

## 6. Veredicto de la fase

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 1 de 1 |
| **CA en "No"** | ninguno |
| **Defectos abiertos aceptados** | ninguno. Las 31 reglas sin origen no son un defecto de esta fase: son lo que esta fase vino a hacer visible |

---

## 7. Métricas contra la meta del plan

| Métrica | Meta | Dio |
|---|---|---|
| Cobertura de CA | 100% | 100% |
| Casos ejecutados | 4 de 4 | 4 de 4 |
| Pruebas del repositorio en verde | 26 + las nuevas | 29 de 29 |
| Falsos positivos en los casos límite | 0 | 0 |
| Reglas sin origen en las especificaciones de este repositorio | — | **31**, en 2 archivos |
