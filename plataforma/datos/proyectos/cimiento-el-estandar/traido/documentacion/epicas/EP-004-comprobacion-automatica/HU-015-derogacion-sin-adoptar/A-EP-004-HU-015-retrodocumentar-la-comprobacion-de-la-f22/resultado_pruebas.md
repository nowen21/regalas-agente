# Resultado de Pruebas — Fase «A-EP-004-HU-015-retrodocumentar-la-comprobacion-de-la-f22»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. El diseño de los casos vive en el [`plan_pruebas.md`](plan_pruebas.md), que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-004-HU-015-retrodocumentar-la-comprobacion-de-la-f22` |
| **HU** | [HU-015 — Derogación sin adoptar](../HU-015-derogacion-sin-adoptar.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-16 |
| **Ejecutado por** | El agente |
| **Ambiente y versión** | Windows 11 · Python 3.11 · estándar 21.3.0 → 21.3.1 |

---

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Lo que se retrodocumenta funciona.** El código llevaba desde el 2026-08-16 corriendo en todos los proyectos con una sola evidencia: el relato de la sesión que lo escribió. Ahora tiene cuatro casos que corren.

---

## 2. Ejecución caso por caso

### CA-01 · CP-001 — el proyecto atrasado con fases falla, y la falla nombra las reglas

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Pedir las derogaciones del estándar | Hay al menos una | **8**, la primera `F4.1` (3.1.0 → `F14`) |
| 2 | Correr sobre el proyecto que declara `3.0.0` y tiene una fase | Sale exactamente una falla | Una |
| 3 | Leer el texto | Nombra la regla, la versión y el reemplazo | Los tres |
| 4 | Declarar la versión vigente y correr | Ningún hallazgo | Ninguno |

**Veredicto:** ✅ Cumple.

---

### CA-02 · CP-002 — lo ya adoptado no se cuenta

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Filtrar desde antes de las tres derogaciones | Salen las tres | Tres |
| 2 | Filtrar desde una intermedia | Solo las posteriores | `X2` y `X3` |
| 3 | Filtrar desde la vigente | Ninguna | Ninguna |
| 4 | Filtrar sin versión declarada | Vacío, no error | Vacío |

**Veredicto:** ✅ Cumple.

---

### CA-03 · CP-003 — sin fases no se cobra

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr el recorrido de flujo con la fase puesta | Sale la falla | Una |
| 2 | Borrar la fase y correr otra vez | Ninguna falla de este tipo | Ninguna |

**Veredicto:** ✅ Cumple. El paso 1 es el que le da valor al 2: sin él, el caso también pasaría con la comprobación rota.

---

### Transversales · CP-004 — los límites callan en vez de romper

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Quitar el `CLAUDE.md` y correr | Lista vacía, sin excepción | Vacía |
| 2 | Dejar un `CLAUDE.md` sin versión declarada | Lista vacía, sin excepción | Vacía |
| 3 | Comparar el contenido del proyecto | Igual que antes | Igual |

**Veredicto:** ✅ Cumple.

---

## 3. Defectos encontrados

Ninguno. El riesgo `B-01` del plan —que la prueba destapara que el código no hace lo que la HU dice— no se materializó.

---

## 4. Lo que se descubrió fuera del criterio

**El módulo ya estaba documentado, y bien.** `validadores/docs/version.md` describía las tres funciones con ejemplos de lo que retornan. Lo que faltaba no era la explicación: era la prueba. Vale anotarlo porque cambia el diagnóstico del pendiente 38 — el trabajo sin cadena no había quedado sin documentar, había quedado **sin comprobar**.

---

## 5. Cobertura contra el plan de pruebas

| Exigencia | Caso | Estado |
|---|---|---|
| CA-01 — falla el proyecto con una derogación sin adoptar | CP-001 | ✅ |
| CA-02 — no cuenta lo que ya está adoptado | CP-002 | ✅ |
| CA-03 — sin fases no se cobra | CP-003 | ✅ |
| Transversales — inocuidad, límites y errores | CP-004 | ✅ |

**Cobertura:** 3 de 3 CA = 100%.

---

## 6. Veredicto de la fase

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 3 de 3 |
| **CA en "No"** | ninguno |
| **Defectos abiertos aceptados** | ninguno |

---

## 7. Métricas contra la meta del plan

| Métrica | Meta | Dio |
|---|---|---|
| Cobertura de CA | 100% | 100% |
| Casos ejecutados | 4 de 4 | 4 de 4 |
| Pruebas del repositorio en verde | 22 + las nuevas | 26 de 26 |
| Archivos del proyecto de prueba modificados por comprobar | 0 | 0 |
