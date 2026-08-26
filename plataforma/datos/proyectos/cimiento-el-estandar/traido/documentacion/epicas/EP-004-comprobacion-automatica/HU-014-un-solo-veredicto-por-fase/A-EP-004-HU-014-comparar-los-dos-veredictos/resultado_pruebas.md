# Resultado de Pruebas — Fase «A-EP-004-HU-014-comparar-los-dos-veredictos»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. El diseño de los casos vive en el [`plan_pruebas.md`](plan_pruebas.md), que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-004-HU-014-comparar-los-dos-veredictos` |
| **HU** | [HU-014 — Un solo veredicto por fase](../HU-014-un-solo-veredicto-por-fase.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-16 |
| **Ejecutado por** | El agente |
| **Ambiente y versión** | Windows 11 · Python 3.11 · estándar 23.0.0 → 23.1.0 |

---

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

---

## 2. Ejecución caso por caso

### CA-01 · CP-001 — dos veredictos distintos se reportan

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Los dos iguales | Ningún hallazgo | Ninguno |
| 2 | El resultado en «No cumple» | Un hallazgo | Uno |
| 3 | Leer el hallazgo | Nombra los dos documentos y los dos valores | Los nombra, y dice cuál mira la puerta |
| 4 | Copiar el veredicto al estado-fase | Ya no sale | No sale |

**Veredicto:** ✅ Cumple.

---

### CA-02 · CP-002 — un criterio en «No» con la fase dada por cumplida

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | `RNF-01` en «No», estado-fase en cumplida | — | — |
| 2 | Correr | Un hallazgo que nombra el requisito | `RNF-01` nombrado |
| 3 | Ponerlo en «Sí» | Ya no sale | No sale |

**Veredicto:** ✅ Cumple.

---

### CA-03 · CP-003 — el conteo que no cuadra

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | «3 de 3» contra «2 de 3» | Un hallazgo con los dos números | Los dos |
| 2 | Igualarlos | Ninguno | Ninguno |

**Veredicto:** ✅ Cumple.

---

### Transversales · CP-004 — lo que no hay que reportar

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | «Cumple, con una salvedad» contra «Cumple» | Ningún hallazgo | Ninguno |
| 2 | Sin `resultado_pruebas` | Ninguno de este tipo | Ninguno |
| 3 | Sin `estado-fase` | Ninguno de este tipo | Ninguno |
| 4 | La forma vieja de escribir el concepto | Se reconoce, sin reportar | Se reconoce |
| 5 | Comparar el tamaño de los documentos antes y después | Iguales | Iguales |

**Veredicto:** ✅ Cumple. El riesgo `B-01` —falsos positivos por las salvedades— no se materializó.

---

## 3. Defectos encontrados

Ninguno.

---

## 4. Lo que se descubrió fuera del criterio

**No queda ninguna contradicción viva en este repositorio.** El riesgo `B-02` no se materializó, y hay un motivo: el único caso conocido —la fase `A-EP-003-HU-010`— se corrigió unas horas antes, al cerrar el pendiente 27.

Vale decirlo así de claro: **esta comprobación no encontró nada porque llegó tarde a su propio caso**. Su valor no es lo que encuentra hoy, es que la próxima vez no dependa de que alguien reescriba un resultado de pruebas y note la diferencia.

---

## 5. Cobertura contra el plan de pruebas

| Exigencia | Caso | Estado |
|---|---|---|
| CA-01 — avisa cuando los dos veredictos difieren | CP-001 | ✅ |
| CA-02 — criterio en «No» con la fase cumplida | CP-002 | ✅ |
| CA-03 — el conteo que no cuadra | CP-003 | ✅ |
| Transversales y falsos positivos | CP-004 | ✅ |

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
| Pruebas del repositorio en verde | 32 + las nuevas | 36 de 36 |
| Falsos positivos en los casos límite | 0 | 0 |
