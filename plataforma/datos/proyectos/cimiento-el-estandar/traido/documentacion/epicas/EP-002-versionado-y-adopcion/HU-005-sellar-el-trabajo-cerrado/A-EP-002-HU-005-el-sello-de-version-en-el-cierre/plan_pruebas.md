# Plan de Pruebas — Fase A-EP-002-HU-005-el-sello-de-version-en-el-cierre   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-002-HU-005 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-002-HU-005-el-sello-de-version-en-el-cierre` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/ciclo-vida-proyectos/08-plan-pruebas.md)).

**El campo se exige hacia adelante.** Ninguna de las fases ya cerradas se vuelve incumplidora por este cambio: lo prohíbe la RN-02 de la HU y la regla de retroactividad de la cabecera del [`CHANGELOG`](../../../../../CHANGELOG.md).

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Modelo | Que el campo del sello esté en los modelos y que el validador lo vea | Este repositorio | Sí |
| Negativa | Que un cierre sin sello se detecte y uno con sello pase | Documentos de mentira en carpeta temporal | Sí |
| Retroactividad | Que una fase cerrada bajo una versión anterior no se reporte por reglas posteriores | Las fases reales de este repositorio | Sí |

**Cuál es el material de prueba.** Las fases que ya existen en el repositorio: son el único conjunto real de cierres, y sobre ellas se mide la retroactividad.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los dos CA |
| Negativa | ☑ | El cierre sin sello tiene que salir reportado |
| No regresión | ☑ | Las fases cerradas no cambian de veredicto |
| Documento | ☑ | El campo del sello en los modelos |

### 3.3 Técnicas de diseño de casos

- **El par sin sello / con sello** — el CA-01 no se cierra viendo que el campo existe en el modelo: se cierra comprobando que **falta cuando falta**. Sin el caso negativo, un validador que no mira nada pasaría igual.
- **Fecha de corte escrita** — el riesgo `R-01`: el validador exige el campo desde una fecha, y esa fecha va escrita. Sin ella, las fases existentes quedarían en falta en cada corrida y el aviso se volvería ruido.
- **La versión se copia, no se recuerda** — el riesgo `R-02`: el modelo pide de dónde salió el número, que es [`VERSION`](../../../../../VERSION). Un sello puesto de memoria es peor que ninguno, porque parece dato.
- **La excepción del desfase con derogación** — con desfase simple la fase cerrada no se reabre; con una derogación sin adoptar, la fase **en curso** sí se detiene ([`02·F22`](../../../../../base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md)). Son dos cosas distintas y el caso las separa.
- **Lo que quedó sin sello se lista, no se rellena** — completar el sello de una fase cerrada sería inventar el dato.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validar.py plantilla`, `fases` y `flujo` sobre este repositorio, más `validadores/pruebas.py` entera, porque se toca `validadores/plantillas.py`.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-005 | [CA-01](../HU-005-sellar-el-trabajo-cerrado.md#ca-01--lo-cerrado-queda-sellado) | [CP-001](#cp-001--el-cierre-sin-sello-se-detecta-y-el-que-lo-tiene-pasa), [CP-002](#cp-002--el-campo-pide-de-dónde-salió-el-número) | Negativa | Crítica | Sí | ☐ |
| HU-005 | [CA-02](../HU-005-sellar-el-trabajo-cerrado.md#ca-02--un-cambio-de-reglas-no-reabre-lo-cerrado) | [CP-003](#cp-003--la-fase-cerrada-bajo-una-versión-anterior-no-se-reporta-por-reglas-posteriores), [CP-004](#cp-004--la-derogación-sin-adoptar-detiene-la-fase-en-curso-no-la-cerrada) | No regresión | Crítica | Sí | ☐ |
| HU-005 | RNF — que el sello se escriba al cerrar y no después | [CP-005](#cp-005--el-sello-está-desde-el-estado-de-la-fase) | Documento | Media | Parcial | ☐ |

**Cobertura:** 2 de 2 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — El cierre sin sello se detecta, y el que lo tiene pasa

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-01 |
| **Tipo** | Negativa |
| **Prioridad** | Crítica |
| **Precondiciones** | Dudas 1 y 2 resueltas: en qué modelos entra el campo y si el validador lo exige o lo avisa |
| **Datos de entrada** | Dos documentos de cierre de mentira, uno con sello y otro sin él, en carpeta temporal |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr el validador de modelos sobre el documento **sin** sello | Sale el hallazgo, con el alcance que decidió la duda 2 |
| 2 | Correr sobre el documento **con** sello | Pasa |
| 3 | Comprobar que la diferencia entre los dos es solo el campo | Lo es |
| 4 | Correr sobre una fase cerrada antes de la fecha de corte | **No** sale hallazgo: el campo se exige hacia adelante |

**Resultado esperado final:** el sello se exige donde toca y no ensucia lo ya cerrado.

> **El paso 2 es el que da valor al 1.** Sin él, el caso pasaría con un validador que reporta todo.

---

### CP-002 — El campo pide de dónde salió el número

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-01 |
| **Tipo** | Documento |
| **Prioridad** | Alta |
| **Precondiciones** | El campo ya escrito en el modelo |
| **Datos de entrada** | El modelo del cierre, y el del estado de la fase si la duda 1 lo resuelve así |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer el campo en el modelo | Dice que el número se copia de `VERSION` |
| 2 | Llenar un cierre de mentira con un número inventado | Queda escrito |
| 3 | Comparar el número contra `VERSION` | No coinciden, y eso se puede ver sin preguntarle a nadie |

**Resultado esperado final:** un sello falso se puede descubrir, porque el modelo dice de dónde tenía que salir.

---

### CP-003 — La fase cerrada bajo una versión anterior no se reporta por reglas posteriores

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-02 |
| **Tipo** | No regresión |
| **Prioridad** | Crítica |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | Las fases cerradas de este repositorio, con su fecha |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `validar.py fases` y `flujo` antes del cambio | Queda la línea base con su número de hallazgos |
| 2 | Aplicar el cambio de modelos y volver a correr | Ningún hallazgo nuevo sobre una fase cerrada |
| 3 | Elegir una fase cerrada bajo una versión anterior y revisarla contra las reglas de hoy | No se reporta como incumplida |
| 4 | Comparar las dos corridas fase por fase | Lo que cambió, cambió hacia adelante |

**Resultado esperado final:** cambiar la norma no reabre lo cerrado.

---

### CP-004 — La derogación sin adoptar detiene la fase en curso, no la cerrada

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-02 — excepción |
| **Tipo** | Límites |
| **Prioridad** | Crítica |
| **Precondiciones** | El estándar tiene derogaciones; un proyecto de prueba con una fase abierta y otra cerrada |
| **Datos de entrada** | El proyecto declarando una versión anterior a la derogación |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Comprobar que hay derogaciones en el tramo | Las hay; si no, el caso falla acá y lo dice |
| 2 | Correr el recorrido de flujo | La fase **en curso** se detiene ([`02·F22`](../../../../../base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md)) |
| 3 | Comprobar qué pasa con la fase cerrada | No se reabre ni se reporta |
| 4 | Anotar la diferencia entre los dos comportamientos | Queda escrita |

**Resultado esperado final:** detener lo que está en curso no es lo mismo que reabrir lo cerrado.

---

### CP-005 — El sello está desde el estado de la fase

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / RNF |
| **Tipo** | Documento |
| **Prioridad** | Media |
| **Precondiciones** | La duda 1 resuelta a favor de los dos modelos |
| **Datos de entrada** | Una fase nueva, abierta después del cambio |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir la fase y escribir su estado | El campo del sello ya está pedido ahí |
| 2 | Cerrarla y escribir el cierre | El número se copia del estado, no se reconstruye de memoria |
| 3 | Comparar los dos números | Coinciden, y los dos salieron de `VERSION` |

**Resultado esperado final:** el sello se escribe cuando se sabe, no cuando hay que acordarse.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que el cambio vuelva incumplidoras a las fases cerradas (riesgo `R-01`) | Inmediato. Se pone la fecha de corte antes de seguir |
| **Alta** | Que un cierre sin sello pase sin hallazgo | Inmediato — el CA-01 queda en «No» |
| **Media** | Que el sello se pueda escribir sin decir de dónde salió (riesgo `R-02`) | Antes de cerrar: el modelo tiene que pedirlo |
| **Media** | Que otra sesión esté tocando `plantillas/` o `VERSION` (riesgo `R-03`) | Se comprueba `VERSION` justo antes de subirla, por el pendiente [22](../../../../../pendientes/hecho/dos-sesiones-versionando-a-la-vez.md) |
| **Baja** | Fases cerradas sin sello | Se listan, no se rellenan: completarlas sería inventar el dato |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 2 CA y los RNF con caso |
| Casos ejecutados | 5 de 5 |
| Hallazgos nuevos sobre fases cerradas | **0** |
| Fases cerradas modificadas | **0** |
| Fases cerradas sin sello | Las que salgan, todas listadas y ninguna rellenada |
| Pruebas de la suite | Las de la línea base, más las nuevas, todas en verde |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
