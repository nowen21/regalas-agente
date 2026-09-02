# Resultado de Pruebas — Fase `X-EP-020-HU-002-sin-datos-no-es-cero`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**. Lo que se iba a probar está en el [plan_pruebas.md](plan_pruebas.md).

---

## 1. Identificación de la ejecución

| Campo | Valor |
|---|---|
| **Fase** | `X-EP-020-HU-002-sin-datos-no-es-cero` |
| **Fecha de ejecución** | 2026-09-01 |
| **Ejecutor** | Ing. José Dúmar Jiménez Ruíz |
| **Ambiente** | La máquina del usuario · Windows · carpetas temporales |
| **Versión del estándar** | 37.2.1 |

---

## 2. Resumen ejecutivo

**El reporte usa la misma medida para todos y dice cuál es, y un proyecto sin datos aparece así.** Los tres criterios cumplen.

Lo que la fase resolvió no fue calcular: fue **no mentir al comparar**. La definición de cada columna sale impresa con la tabla —incluida la advertencia de que «vencida» es un número puesto acá y no un vencimiento acordado—, y un proyecto sin fases dice «sin datos» en vez de cero por cien.

---

## 3. Casos ejecutados

| Caso | Qué comprobó | Resultado |
|---|---|---|
| CP-004 | La misma medida · la definición impresa · la deuda y la vencida separadas | ✅ |
| CP-005 | **Sin datos no es cero** · se nombra aparte · va al final · la tabla vacía se dice | ✅ |

**7 pruebas nuevas.** Ninguna quedó en rojo al cerrar.

---

## 4. Defectos encontrados

**Ninguno en esta fase.**

---

## 5. Cobertura de los criterios de aceptación

| CA | Caso | Concepto |
|---|---|---|
| CA-01 · La misma medida, y escrita | CP-004 | ✅ Cumple |
| CA-02 · La deuda y la vencida | CP-004 | ✅ Cumple |
| CA-03 · Sin datos no es cero | CP-005 | ✅ Cumple |

**3 de 3.**

---

## 6. Concepto

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 3 de 3 |
| **Defectos abiertos aceptados** | Ninguno |

---

## 7. Las dos baterías completas

| Batería | Pruebas | Resultado |
|---|---|---|
| La plataforma | 552 | ✅ En verde |
| El estándar | 733 | ✅ En verde |
| Los validadores | 32 | ✅ Sin fallas |

---

## 8. Lo que esta ejecución NO comprueba

- **Si la misma medida es justa entre proyectos muy distintos.** Un proyecto de 209 fases y uno de tres se miden igual, y eso puede engañar; por eso la definición va impresa.
- **Si el avance quiere decir algo.** Mide fases cerradas, no funcionalidad entregada, y así está declarado.
