# Plan de Pruebas — Fase A-EP-004-HU-016-el-pendiente-cerrado-declara-su-fase   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-004-HU-016 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-004-HU-016-el-pendiente-cerrado-declara-su-fase` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/planes/pruebas.md)).

**Los tres CA de excepción pesan tanto como el primero.** Sin ellos el programa reporta de más el primer día y nadie lo vuelve a correr.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Positiva | Que el pendiente cerrado sin fase se reporte | Carpetas temporales | Sí |
| Resolución | Que la fase declarada exista de verdad en el árbol | Este repositorio y temporales | Sí |
| Excepción | Que el pendiente que no fue desarrollo, y lo cerrado antes del corte, no se reporten | Carpetas temporales | Sí |
| Medición | Cuáles de los pendientes ya cerrados quedan de cada lado del corte | Este repositorio | Parcial |

**Por qué la fase declarada se resuelve contra el árbol.** Es la mitad del valor: una fase que no existe es una promesa de trazabilidad que nadie puede seguir.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los cuatro CA |
| Negativa | ☑ | Los CA-03 y CA-04: lo que **no** debe reportarse |
| Límites | ☑ | La fecha de corte, justo antes y justo después |
| Medición | ☑ | El reparto de los pendientes ya cerrados |

### 3.3 Técnicas de diseño de casos

- **El par reportado / no reportado en cada CA** — con solo el caso positivo, un programa que reporta todo pasaría los cuatro.
- **La excepción se declara, no se adivina** — el pendiente que no fue desarrollo lo dice él mismo. Adivinar por prosa produce falsos positivos, y un falso positivo apaga el programa.
- **Fecha de corte escrita, no deducida** — deducirla del historial la vuelve frágil: un archivo movido cambiaría la fecha. Va escrita en la documentación del programa.
- **Los dos lados del corte** — el caso prueba un pendiente cerrado justo antes y otro justo después: es donde la separación se rompe si está mal hecha.
- **La cita rota es aviso, no falla** — el riesgo `R-02`: si una fase se renombró después, el pendiente que la nombra queda mal por un cambio legítimo. Eso ya está planteado en el pendiente [54](../../../../../pendientes/hecho/cerrar-un-pendiente-arrastra-sus-citas.md).

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/pruebas.py` entera y el subcomando nuevo sobre este repositorio y sobre las carpetas temporales.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-016 | [CA-01](../HU-016-el-pendiente-cerrado-nombra-su-fase.md#ca-01--un-pendiente-cerrado-sin-fase-se-reporta) | [CP-001](#cp-001--el-pendiente-cerrado-sin-fase-se-reporta-y-el-que-la-nombra-no) | Funcional | Alta | Sí | ☐ |
| HU-016 | [CA-02](../HU-016-el-pendiente-cerrado-nombra-su-fase.md#ca-02--una-fase-que-no-existe-se-reporta) | [CP-002](#cp-002--la-fase-inventada-se-reporta-y-la-que-existe-no) | Funcional | Crítica | Sí | ☐ |
| HU-016 | [CA-03](../HU-016-el-pendiente-cerrado-nombra-su-fase.md#ca-03--el-pendiente-que-no-era-desarrollo-no-se-reporta) | [CP-003](#cp-003--el-pendiente-cerrado-por-decisión-no-se-reporta) | Negativa | Crítica | Sí | ☐ |
| HU-016 | [CA-04](../HU-016-el-pendiente-cerrado-nombra-su-fase.md#ca-04--lo-cerrado-antes-de-la-regla-se-separa) | [CP-004](#cp-004--lo-cerrado-antes-del-corte-queda-de-su-lado) | Límites | Crítica | Sí | ☐ |
| HU-016 | RNF — que el programa no reporte de más | [CP-003](#cp-003--el-pendiente-cerrado-por-decisión-no-se-reporta), [CP-004](#cp-004--lo-cerrado-antes-del-corte-queda-de-su-lado) | Negativa | Alta | Sí | ☐ |

**Cobertura:** 4 de 4 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — El pendiente cerrado sin fase se reporta, y el que la nombra no

| Campo | Valor |
|---|---|
| **HU / CA** | HU-016 / CA-01 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Dudas 1 y 2 resueltas: fecha de corte y dónde se declara la fase |
| **Datos de entrada** | Dos pendientes cerrados en carpeta temporal, uno con fase declarada y otro sin ella, los dos posteriores al corte |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr sobre el pendiente sin fase | Se reporta, y nombra el archivo |
| 2 | Correr sobre el que la declara | No se reporta |
| 3 | Comprobar que la declaración se busca donde decidió la duda 2 | Ahí, y no en cualquier parte del texto |
| 4 | Comprobar que ninguna corrida escribió | Ningún archivo modificado |

**Resultado esperado final:** un pendiente cerrado dice en qué fase se hizo, o se nota que no lo dice.

---

### CP-002 — La fase inventada se reporta, y la que existe no

| Campo | Valor |
|---|---|
| **HU / CA** | HU-016 / CA-02 |
| **Tipo** | Funcional |
| **Prioridad** | Crítica |
| **Precondiciones** | El CP-001 corrido |
| **Datos de entrada** | Un pendiente que nombra una fase inexistente, y otro que nombra una del árbol real |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr sobre el que nombra una fase inventada | Se reporta, y dice qué fase no encontró |
| 2 | Correr sobre el que nombra una fase real | No se reporta |
| 3 | Renombrar la fase real y volver a correr | Se reporta como **aviso**, no como falla (riesgo `R-02`) |
| 4 | Comprobar que el nombre se resolvió contra el árbol de épicas | Se resolvió ahí |

**Resultado esperado final:** declarar la fase deja de ser un trámite que se llena de cualquier manera.

> **El paso 3 separa el error del cambio legítimo.** Renombrar una fase es válido; lo que hay que arreglar es la cita, y eso ya está planteado en el pendiente [54](../../../../../pendientes/hecho/cerrar-un-pendiente-arrastra-sus-citas.md).

---

### CP-003 — El pendiente cerrado por decisión no se reporta

| Campo | Valor |
|---|---|
| **HU / CA** | HU-016 / CA-03 y RNF |
| **Tipo** | Negativa |
| **Prioridad** | Crítica |
| **Precondiciones** | Carpeta temporal |
| **Datos de entrada** | Un pendiente cerrado porque se decidió no hacerlo, con su motivo declarado, y otro cerrado por construcción |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr sobre el pendiente cerrado por decisión, con su declaración | No se reporta |
| 2 | Quitarle la declaración y volver a correr | Se reporta: la exención se declara, no se supone |
| 3 | Correr sobre el cerrado por construcción sin fase | Se reporta |
| 4 | Comprobar que el programa no intentó adivinar por el texto | No lo intentó |

**Resultado esperado final:** no todo pendiente cerrado fue una fase, y eso lo dice el pendiente, no el programa.

---

### CP-004 — Lo cerrado antes del corte queda de su lado

| Campo | Valor |
|---|---|
| **HU / CA** | HU-016 / CA-04 y RNF |
| **Tipo** | Límites |
| **Prioridad** | Crítica |
| **Precondiciones** | Duda 1 resuelta: la fecha de corte |
| **Datos de entrada** | Un pendiente cerrado justo antes del corte y otro justo después, los dos sin fase declarada |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr sobre el anterior al corte | **No** se reporta como incumplimiento |
| 2 | Correr sobre el posterior | Se reporta |
| 3 | Comprobar que los anteriores se cuentan **aparte** | Salen en su propio grupo, no mezclados |
| 4 | Correr sobre los pendientes ya cerrados del repositorio | Se anota cuáles quedan de cada lado |
| 5 | Comprobar que la fecha de corte salió de la documentación y no del historial | De la documentación |

**Resultado esperado final:** la regla no se aplica hacia atrás, y lo viejo queda contado sin quedar en falta.

> **Sin este caso, el primer día el programa reportaría todos los pendientes ya cerrados** (riesgo `R-01`) y nadie lo miraría.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que el programa reporte los pendientes cerrados antes del corte | Inmediato. El CA-04 queda en «No» y el programa nace ignorado |
| **Crítica** | Que reporte un pendiente que no fue desarrollo | Inmediato — es el falso positivo que apaga el programa |
| **Alta** | Que una fase inventada pase sin reporte | El CA-02 queda en «No»: la trazabilidad sería de adorno |
| **Media** | Que una fase renombrada produzca falso positivo (riesgo `R-02`) | Sale como aviso; arreglar la cita es del pendiente 54 |
| **Baja** | Que la declaración se llene de cualquier manera (riesgo `R-03`) | El CP-002 lo detecta: el nombre se resuelve contra el árbol |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 4 CA y los RNF con caso |
| Casos ejecutados | 4 de 4 |
| Pendientes anteriores al corte reportados como incumplimiento | **0** |
| Pendientes no-desarrollo reportados | **0** |
| Fases declaradas que no existen | Todas reportadas |
| Reparto de los pendientes ya cerrados a cada lado del corte | Anotado, con su fecha |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
