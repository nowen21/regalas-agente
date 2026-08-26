# Plan de Pruebas — Fase A-EP-007-HU-003-retrodocumentar-la-estructura-de-carpetas   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-007-HU-003 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-007-HU-003-retrodocumentar-la-estructura-de-carpetas` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/ciclo-vida-proyectos/08-plan-pruebas.md)).

**Condición de arranque, no negociable.** Todas las corridas van sobre proyectos de prueba en carpetas temporales. No se instala ni se actualiza ningún proyecto vivo.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Instalación limpia | Que la estructura quede completa en una carpeta vacía | Carpeta temporal | Sí |
| No destrucción | Que lo que ya existe conserve su **contenido** | Carpeta temporal con archivos previos | Sí |
| Idempotencia | Que instalar dos veces dé el mismo resultado | Carpeta temporal | Sí |
| Revisión | Que la estructura que falta se reporte | Carpeta temporal y este repositorio | Sí |

**Por qué la prueba de no destrucción usa archivos con contenido.** Pisar es **perder contenido**. Una carpeta que sigue ahí con un archivo vacío se ve igual de bien que una intacta.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los tres CA |
| Integridad | ☑ | El CA-02: instalar no borra |
| Idempotencia | ☑ | La segunda corrida, que es la que borra de verdad |
| Interpretación | ☑ | Cómo se lee la revisión en esta casa, que no se instala a sí misma |

### 3.3 Técnicas de diseño de casos

- **Instalar dos veces es un caso propio** — es la forma en que esto se rompe de verdad: la primera corrida crea, la segunda es la que puede borrar. Confiar en la prueba de la primera dejaría el defecto sin ver.
- **Contenido comparado, no presencia** — arriba.
- **El caso de esta casa se explica en el resultado** — el riesgo `R-03`: la revisión reprueba acá con razón —falta el planteamiento, pendiente [56](../../../../../pendientes/hecho/el-estandar-tiene-su-planteamiento.md)— y varios puntos no le aplican, porque el estándar no se instala a sí mismo. Quien lea el resultado tiene que entenderlo sin reconstruirlo.
- **La falla del CA-02 detiene la fase** — el riesgo `R-01`: si el instalador borra trabajo, se para y se reporta de inmediato. Corregirlo es una fase con su propio plan.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/pruebas.py` entera, el instalador y `validar.py estructura` sobre carpetas temporales.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-003 | [CA-01](../HU-003-estructura-de-carpetas.md#ca-01--la-estructura-se-crea-sola) | [CP-001](#cp-001--la-instalación-en-carpeta-vacía-deja-la-estructura-completa) | Funcional | Alta | Sí | ☐ |
| HU-003 | [CA-02](../HU-003-estructura-de-carpetas.md#ca-02--lo-que-ya-existe-no-se-pisa) | [CP-002](#cp-002--los-archivos-con-contenido-no-cambian), [CP-003](#cp-003--instalar-dos-veces-deja-el-mismo-resultado) | Integridad | Crítica | Sí | ☐ |
| HU-003 | [CA-03](../HU-003-estructura-de-carpetas.md#ca-03--la-estructura-que-falta-se-reporta) | [CP-004](#cp-004--la-carpeta-quitada-se-reporta), [CP-005](#cp-005--cómo-se-lee-la-revisión-en-esta-casa) | Funcional | Alta | Sí | ☐ |
| HU-003 | RNF — que instalar no borre nada | [CP-002](#cp-002--los-archivos-con-contenido-no-cambian), [CP-003](#cp-003--instalar-dos-veces-deja-el-mismo-resultado) | Integridad | Crítica | Sí | ☐ |

**Cobertura:** 3 de 3 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — La instalación en carpeta vacía deja la estructura completa

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-01 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Carpeta temporal vacía |
| **Datos de entrada** | La estructura declarada en [`estructura-base.md`](../../../../../base/02-flujo-de-trabajo/estructura-base.md) |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Tomar la lista de lo que la estructura declara | Queda la referencia |
| 2 | Correr el instalador sobre la carpeta vacía | Crea la estructura |
| 3 | Comparar contra la lista del paso 1 | No falta nada |
| 4 | Correr `validar.py estructura` sobre la carpeta | Sin hallazgos |
| 5 | Comprobar que no escribió fuera de la carpeta | Nada afuera |

**Resultado esperado final:** un proyecto nuevo arranca con la estructura que [`02·F13`](../../../../../base/02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md) exige, sin que nadie la arme a mano.

---

### CP-002 — Los archivos con contenido no cambian

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-02 y RNF |
| **Tipo** | Integridad |
| **Prioridad** | Crítica |
| **Precondiciones** | Carpeta temporal con carpetas y archivos **con contenido reconocible** |
| **Datos de entrada** | Un proyecto que ya trabajó: documentos escritos dentro de las carpetas de la estructura |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Anotar el contenido de cada archivo previo | Queda la línea base, con su contenido |
| 2 | Correr el instalador | Termina |
| 3 | Comparar el **contenido** de cada archivo previo contra la línea base | Idéntico, byte por byte |
| 4 | Comprobar que ninguno quedó vacío | Ninguno |
| 5 | Comprobar que lo que faltaba de la estructura sí se creó | Se creó |

**Resultado esperado final:** instalar sobre un proyecto que ya trabajó agrega lo que falta y no toca lo que hay.

> **El paso 3 compara contenido, no presencia.** Un archivo vaciado sigue estando, y ese es exactamente el defecto que hay que detectar.

---

### CP-003 — Instalar dos veces deja el mismo resultado

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-02 y RNF |
| **Tipo** | Idempotencia |
| **Prioridad** | Crítica |
| **Precondiciones** | El CP-002 corrido |
| **Datos de entrada** | El mismo proyecto de prueba, con contenido |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Anotar el árbol y el contenido después de la primera instalación | Queda la línea base |
| 2 | Correr el instalador **otra vez** | Termina |
| 3 | Comparar árbol y contenido contra la línea base | Idénticos |
| 4 | Repetir una tercera vez | Idénticos |
| 5 | Anotar qué archivo cambie, si alguno | Es hallazgo grave del CA-02 |

**Resultado esperado final:** la segunda corrida no destruye lo que dejó la primera.

> **Este es el caso que rompe de verdad.** La primera instalación crea; la segunda es la que puede pisar.

---

### CP-004 — La carpeta quitada se reporta

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-03 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Un proyecto de prueba con la estructura completa |
| **Datos de entrada** | El proyecto al que se le quita una carpeta |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr la revisión sobre el proyecto completo | Sin hallazgos |
| 2 | Quitar una carpeta de la estructura | Queda faltando |
| 3 | Correr la revisión | Reporta, y **dice cuál** falta |
| 4 | Repetir quitando otra distinta | También la nombra |
| 5 | Devolver las carpetas y correr | Sin hallazgos otra vez |

**Resultado esperado final:** lo que falta se ve, y se ve qué es.

---

### CP-005 — Cómo se lee la revisión en esta casa

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-03 |
| **Tipo** | Interpretación |
| **Prioridad** | Alta |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | La revisión corrida sobre este repositorio |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr la revisión sobre este repositorio | Sale su resultado |
| 2 | Separar los puntos que **no le aplican**, porque el estándar no se instala a sí mismo | Cada uno con su motivo |
| 3 | Separar los que reprueban **con razón** | Al menos el planteamiento faltante, pendiente [56](../../../../../pendientes/hecho/el-estandar-tiene-su-planteamiento.md) |
| 4 | Escribir la lectura completa en el resultado | Queda para quien lea después |
| 5 | Comprobar que la corrida no escribió nada | Ningún archivo modificado |

**Resultado esperado final:** el resultado de la revisión sobre esta casa se entiende sin reconstruirlo cada vez (riesgo `R-03`).

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que el instalador pise contenido existente (riesgo `R-01`) | **Se para y se reporta de inmediato.** Corregirlo es una fase con su propio plan |
| **Crítica** | Que la corrida de prueba escriba fuera de su carpeta (riesgo `R-02`) | Inmediato. Se detiene y se restaura |
| **Alta** | Que la segunda instalación cambie algo | Inmediato: el CA-02 queda en «No» |
| **Media** | Que la revisión no diga **cuál** carpeta falta | Antes de cerrar |
| **Media** | Que el resultado de esta casa se lea como que el estándar está mal instalado (riesgo `R-03`) | El resultado explica cada punto que no le aplica |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 3 CA y los RNF con caso |
| Casos ejecutados | 5 de 5 |
| Proyectos vivos instalados | **0** |
| Archivos con contenido alterados por instalar | **0** |
| Diferencias entre la primera y la segunda instalación | **0** |
| Puntos de la revisión de esta casa sin explicar | **0** |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
