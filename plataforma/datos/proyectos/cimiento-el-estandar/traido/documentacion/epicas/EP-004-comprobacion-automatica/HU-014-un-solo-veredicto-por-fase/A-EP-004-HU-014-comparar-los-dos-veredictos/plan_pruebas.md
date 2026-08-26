# Plan de Pruebas — «Fase A-EP-004-HU-014: comparar los dos veredictos»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de la misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-004-HU-014 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-004-HU-014-comparar-los-dos-veredictos` |
| **Fecha** | 2026-08-16 |
| **Elaborado por** | El agente |
| **Aprobado por** | El usuario, en la orden de resolver los ocho pendientes `P1` |
| **Estado** | Aprobado |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12**.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Integración | Correr el recorrido de fases sobre árboles de mentira y leer los hallazgos | Carpeta temporal | Sí |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los tres CA |
| Falsos positivos | ☑ | El riesgo `B-01`: una fase que cumple **con salvedad** |
| Límites | ☑ | Los transversales: falta un documento, o no se puede leer |

### 3.3 Técnicas de diseño de casos

- **El caso real, reconstruido** — la contradicción que destapó el pendiente: resultado en «No cumple» y estado-fase en «aprobada». Se reconstruye de mentira, porque el original ya se corrigió.
- **Caso trampa** — una fase que dice «Cumple, con una salvedad» en un documento y «Cumple» en el otro: **no** es una contradicción.
- **Prueba de la prueba** — se revierte la comprobación y los casos tienen que ponerse rojos.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/tests/` entera.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-014 | CA-01 | [CP-001](#cp-001--dos-veredictos-distintos-se-reportan) | Funcional | Alta | Sí | ☐ |
| HU-014 | CA-02 | [CP-002](#cp-002--un-criterio-en-no-con-la-fase-dada-por-cumplida) | Funcional | Alta | Sí | ☐ |
| HU-014 | CA-03 | [CP-003](#cp-003--el-conteo-que-no-cuadra) | Funcional | Alta | Sí | ☐ |
| HU-014 | Transversales y `B-01` | [CP-004](#cp-004--lo-que-no-hay-que-reportar) | Límites | Alta | Sí | ☐ |

**Cobertura:** 3 de 3 CA = 100%.

---

## 6. Casos de prueba

### CP-001 — Dos veredictos distintos se reportan

| Campo | Valor |
|---|---|
| **HU / CA** | HU-014 / CA-01 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Fase de mentira con los dos documentos |
| **Datos de entrada** | Resultado en «No cumple», estado-fase en «Cumple» |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Dejar el mismo veredicto en los dos y correr | Ningún hallazgo de este tipo |
| 2 | Cambiar el del resultado a «No cumple» y correr | Un hallazgo |
| 3 | Leer el hallazgo | Nombra los dos documentos y los dos valores |
| 4 | Copiar el veredicto al estado-fase y correr | Ya no sale |

**Resultado esperado final:** un `estado-fase` desactualizado no pasa por veredicto.

---

### CP-002 — Un criterio en «No» con la fase dada por cumplida

| Campo | Valor |
|---|---|
| **HU / CA** | HU-014 / CA-02 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Fase de mentira con los dos documentos |
| **Datos de entrada** | Un requisito no funcional en «No» en el §5 del resultado |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Marcar el requisito en «No» y dejar el estado-fase en cumplida | — |
| 2 | Correr | Sale un hallazgo que nombra ese requisito |
| 3 | Poner el requisito en «Sí» y correr | Ya no sale |

**Resultado esperado final:** la puerta no se pasa con una exigencia en «No».

---

### CP-003 — El conteo que no cuadra

| Campo | Valor |
|---|---|
| **HU / CA** | HU-014 / CA-03 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Fase de mentira con los dos documentos |
| **Datos de entrada** | «3 de 3» en el resultado y «2 de 3» en el estado-fase |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Dejar los conteos distintos y correr | Sale un hallazgo con los dos números |
| 2 | Igualarlos y correr | Ninguno |

**Resultado esperado final:** los dos documentos no pueden contar cosas distintas.

---

### CP-004 — Lo que no hay que reportar

| Campo | Valor |
|---|---|
| **HU / CA** | HU-014 / transversales y riesgo `B-01` |
| **Tipo** | Límites |
| **Prioridad** | Alta |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | Cuatro fases distintas |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Una fase que dice «Cumple, con una salvedad» y «Cumple» | Ningún hallazgo: no es una contradicción |
| 2 | Una fase sin `resultado_pruebas` | Ninguno de este tipo |
| 3 | Una fase sin `estado-fase` | Ninguno de este tipo |
| 4 | Una fase cuyo resultado usa la forma vieja de escribir el concepto | Se reconoce igual, sin reportar |
| 5 | Comprobar que ningún documento quedó modificado | Iguales |

**Resultado esperado final:** el validador habla solo cuando hay una contradicción de verdad.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Alta** | Reportar una fase que no se contradice | Inmediato — un validador que se equivoca se deja de leer |
| **Alta** | No reportar la contradicción del caso real | Inmediato |
| **Media** | Que no reconozca la forma vieja de escribir el concepto | Antes de cerrar |

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de CA | 100% — los 3 con caso |
| Casos ejecutados | 4 de 4 |
| Pruebas del repositorio en verde | Las 32 de hoy, más las nuevas |
| Falsos positivos en los casos límite | **0** |

El veredicto va en el `resultado_pruebas.md` de esta fase.
