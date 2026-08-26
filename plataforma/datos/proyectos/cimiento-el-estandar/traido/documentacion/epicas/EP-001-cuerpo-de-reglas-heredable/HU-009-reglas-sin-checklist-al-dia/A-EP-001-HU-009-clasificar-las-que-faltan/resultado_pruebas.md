# Resultado de Pruebas — Fase «A-EP-001-HU-009-clasificar-las-que-faltan»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. El diseño de los casos vive en el [`plan_pruebas.md`](plan_pruebas.md), que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-001-HU-009-clasificar-las-que-faltan` |
| **HU** | [HU-009 — Poner al día las reglas que no pasan su propio checklist](../HU-009-reglas-sin-checklist-al-dia.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-16 |
| **Ejecutado por** | El agente |
| **Ambiente y versión** | Windows 11 · Python 3.11 · estándar 23.1.0 → 23.1.1 |

---

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

---

## 2. Ejecución caso por caso

### CA-02 · CP-001 — ninguna regla queda fuera del registro

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Contar los hallazgos de «no aparece en el registro» antes | 33 | **33** |
| 2 | Clasificar las 33 | — | Hecho |
| 3 | Volver a contar | Cero | **Cero** |
| 4 | Comprobar que el total bajó exactamente 33 | 269 → 236 | **269 → 236** |

**Veredicto:** ✅ Cumple. El paso 4 es el que descarta que algo se haya roto o que una fila quedara mal escrita.

---

### CA-02 · CP-002 — la clasificación aguanta el criterio escrito

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Tres «no validables» contra el criterio | Un script no podría decidirlas | `C3` (quédate en tu tarea), `OB5` (postmortem sin culpa) y `DP8` (autoriza el humano): las tres se juzgan leyendo, no contando |
| 2 | Leer qué le falta a cada 🟡 | Cada una lo dice, y es concreto | Las diez lo dicen: ocho necesitan proyecto real, `F4` necesita que la aprobación quede escrita en algún archivo, `G9` necesita decidir dónde va el identificador |
| 3 | Buscar el programa de cada ✅ nueva | Existe y se puede nombrar | `M15` → `enlaces.py` · `F12` → `fases.py` |

**Veredicto:** ✅ Cumple. El riesgo `B-01` —clasificar de más como «no validable» para bajar el número— no se materializó: la lista de 🟡 **creció** de ~12 a ~22.

---

### CA-02 · CP-003 — los capítulos opcionales también cuentan

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Buscar una regla del `18` | Está | Las ocho |
| 2 | Buscar una del `19` | Está | Las seis |

**Veredicto:** ✅ Cumple.

---

## 3. Defectos encontrados

Ninguno.

---

## 4. Lo que se descubrió fuera del criterio

**Quince de las 33 ya estaban clasificadas, y el problema era cómo estaban escritas.** El registro decía `C1–C17`, un rango, y el programa que comprueba `20·M9` busca cada identificador literal. Quince reglas de conducta figuraban como «sin clasificar» estando clasificadas desde el 2026-08-05.

**Cambia el diagnóstico del pendiente 19.** Su tercera deuda no era «33 reglas que nadie clasificó»: eran **18 de verdad** —los capítulos `18` y `19` completos, más `G9`, `M15`, `F4` y `F12`— y **15 escritas de una forma que el validador no puede leer**.

Vale como aprendizaje del propio registro: **un documento que alimenta a un programa se escribe como el programa lee**, no como es cómodo para quien lo escribe. Un rango ahorra cuatro líneas y cuesta quince falsos hallazgos que nadie sabe si son reales.

**Lo que sí faltaba de verdad y era grave:** los capítulos `18` y `19` no aparecían **ni una sola vez**, ni siquiera para decir que no se validan. Ser opcional no exime de aparecer, y no aparecer es lo que los volvió invisibles.

---

## 5. Cobertura contra el plan de pruebas

| Exigencia | Caso | Estado |
|---|---|---|
| CA-02 — toda regla aparece clasificada | CP-001 | ✅ |
| CA-02 · calidad de la clasificación | CP-002 | ✅ |
| CA-02 · límites, los capítulos opt-in | CP-003 | ✅ |

**Cobertura:** 1 de 1 CA del alcance = 100%. **La HU tiene tres CA y esta fase cubre uno**, declarado así desde el plan.

---

## 6. Veredicto de la fase

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 1 de 1 del alcance de la fase |
| **CA en "No"** | ninguno |
| **Defectos abiertos aceptados** | ninguno |

> **La HU-009 sigue abierta**, y el pendiente 19 también. Esta fase cerró su parte mecánica; faltan las siete publicadas en «no cumple» y las 121 sin bloque de checklist.

---

## 7. Métricas contra la meta del plan

| Métrica | Meta | Dio |
|---|---|---|
| Reglas sin clasificar | 0 | **0**, desde 33 |
| Cada 🟡 dice qué le falta | 100% | 100% |
| Reglas cuyo texto se tocó | 0 | **0** |
| Hallazgos totales del validador de meta-reglas | — | 269 → 236 |
