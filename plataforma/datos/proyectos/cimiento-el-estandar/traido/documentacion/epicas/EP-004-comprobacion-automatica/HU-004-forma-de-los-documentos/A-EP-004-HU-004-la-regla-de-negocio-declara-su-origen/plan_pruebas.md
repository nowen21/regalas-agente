# Plan de Pruebas — «Fase A-EP-004-HU-004: la regla de negocio declara su origen»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de la misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-004-HU-004 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-004-HU-004-la-regla-de-negocio-declara-su-origen` |
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
| Unitario | La comprobación sobre el texto de una especificación | En memoria y carpeta temporal | Sí |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | El `CA-04` |
| Falsos positivos | ☑ | El riesgo `B-02`: una regla con fuente que además nombra códigos |
| No regresión | ☑ | Que las tres comprobaciones que ya existen sigan igual |

### 3.3 Técnicas de diseño de casos

- **El caso real** — las dos reglas de `shopnest-mesa`, la que baja de `RF-13` y la que no baja de nada. Se ven casi iguales y solo una tiene fuente.
- **Prueba de la prueba** — se revierte la comprobación y los casos tienen que ponerse rojos.
- **Caso trampa** — una regla con fuente cuyo texto menciona además un código, para ver que no se cuenta dos veces ni se confunde.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/tests/` entera.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-004 | CA-04 | [CP-001](#cp-001--la-regla-sin-origen-se-reporta-y-la-que-lo-tiene-no) | Funcional | Alta | Sí | ☐ |
| HU-004 | CA-04 · límites | [CP-002](#cp-002--lo-que-no-hay-que-reportar) | Falsos positivos | Alta | Sí | ☐ |
| HU-004 | CA-04 · el documento se reconoce | [CP-003](#cp-003--una-especificación-se-compara-contra-su-plantilla) | Funcional | Alta | Sí | ☐ |
| HU-004 | CA-04 · prueba de la prueba | [CP-004](#cp-004--los-casos-se-ponen-rojos-si-se-revierte-la-comprobación) | Verificación | Alta | No — a mano, una vez | ☐ |

**Cobertura:** 1 de 1 CA = 100%.

---

## 6. Casos de prueba

### CP-001 — La regla sin origen se reporta, y la que lo tiene no

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / CA-04 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | Un §4 con las dos reglas reales de `shopnest-mesa` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Comprobar la especificación de mentira | Sale exactamente **una** falla de este tipo |
| 2 | Leer de qué línea habla | De la regla que no baja de ninguna parte |
| 3 | Leer el texto de la falla | Dice que falta la procedencia y qué hacer con esa regla |
| 4 | Ponerle un origen a esa regla y volver a comprobar | Ninguna falla de este tipo |

**Resultado esperado final:** lo que antes solo se veía preguntando, ahora se reporta.

---

### CP-002 — Lo que no hay que reportar

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / CA-04 · falsos positivos |
| **Tipo** | Límites |
| **Prioridad** | Alta |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | Tres §4 distintos |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Un §4 que sigue siendo el molde de la plantilla, sin llenar | Ninguna falla de este tipo: de eso ya se queja otra comprobación |
| 2 | Un §4 vacío, sin ninguna regla | Ninguna falla |
| 3 | Una regla con origen que además nombra un código en su texto | Ninguna falla |
| 4 | Un documento que **no** es una especificación pero tiene una sección con ese nombre | Ninguna falla |

**Resultado esperado final:** la comprobación habla solo cuando tiene algo que decir.

---

### CP-003 — Una especificación se compara contra su plantilla

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / CA-04 · el documento se reconoce |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | Un archivo llamado `spec.md` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Preguntar qué plantilla le corresponde | La de especificación de módulo |
| 2 | Comprobar que esa plantilla existe en disco | Existe |

**Resultado esperado final:** el documento que se quiere comprobar deja de ser invisible.

> **Sin este caso, todo lo demás pasa y nada se comprueba.** Hoy un `spec.md` no se compara contra ninguna plantilla: el programa no lo reconoce, así que la comprobación nueva no se dispararía nunca.

---

### CP-004 — Los casos se ponen rojos si se revierte la comprobación

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / CA-04 · verificación del propio caso |
| **Tipo** | Verificación manual, una sola vez |
| **Prioridad** | Alta |
| **Precondiciones** | El CP-001 pasó |
| **Datos de entrada** | Ninguno |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Desactivar la comprobación nueva | Queda revertida |
| 2 | Correr la suite de la fase | El CP-001 se pone rojo |
| 3 | Volver a activarla y correr todo | Verde otra vez |

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Alta** | Reportar una regla que sí tiene fuente | Inmediato — un validador que se equivoca se deja de leer |
| **Alta** | Que el caso pase con la comprobación revertida | Inmediato |
| **Media** | Que reconocer `spec` levante una avalancha de hallazgos de forma | Se cuenta y se deja escrito; no se calla la comprobación |

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de CA | 100% — el 1 con caso |
| Casos ejecutados | 4 de 4 |
| Pruebas del repositorio en verde | Las 26 de hoy, más las nuevas |
| Falsos positivos en los casos límite | **0** |

El veredicto va en el `resultado_pruebas.md` de esta fase.
