# Plan de Pruebas — Fase A-EP-004-HU-009-el-conteo-de-hallazgos-por-regla   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-004-HU-009 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-004-HU-009-el-conteo-de-hallazgos-por-regla` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/planes/pruebas.md)).

**El caso del CA-02 va antes de dar la fase por buena.** Un registro de hallazgos que arrastre el contenido revisado sería una filtración por la puerta de atrás ([`00·N6`](../../../../../base/00-nucleo-blindado.md#n6--secretos-y-datos-sensibles-nunca-se-exponen-blindada)).

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Unitario | Que cada hallazgo diga a qué regla pertenece de forma agrupable | En memoria | Sí |
| Privacidad | Que el registro no contenga el texto de lo revisado | Carpeta temporal con una clave armada | Sí |
| Comparación | Que dos corridas con un arreglo en medio muestren la baja | Carpeta temporal | Sí |
| No regresión | Que el campo nuevo no rompa ninguna prueba existente | Este repositorio | Sí |

**Por qué el campo entra con valor por omisión.** Así nada se rompe de golpe y los validadores lo van llenando de a uno (riesgo `R-03`).

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los tres CA |
| Privacidad | ☑ | El CA-02, que es el delicado |
| No regresión | ☑ | La suite completa, antes y después del campo nuevo |
| Legibilidad | ☑ | El RNF: que el número sirva para decidir |

### 3.3 Técnicas de diseño de casos

- **La prueba de privacidad usa una clave armada** — la única forma de comprobar que el registro no arrastra contenido es correrlo sobre algo que **no debería aparecer nunca**, y buscar esa cadena en el registro. La cadena se arma para la prueba y se borra.
- **Baja medida, no supuesta** — el CA-03 se prueba con dos corridas y un arreglo real en medio. Que el conteo exista no prueba que sirva para comparar; que baje en la regla arreglada y **no en las otras**, sí.
- **Suite completa antes y después** — el campo nuevo toca [`comun.py`](../../../../../validadores/comun.py), que usan los 24 subcomandos. La suite se corre entera en los dos momentos.
- **El número decide, no puntúa** — el riesgo `R-01`: la advertencia se escribe en la documentación del conteo, donde la va a leer quien lo use, no solo en `metricas/`.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/pruebas.py` **entera**, porque se toca `comun.py`, que es de todos.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-009 | [CA-01](../HU-009-conteo-por-regla.md#ca-01--la-corrida-deja-el-conteo-por-regla) | [CP-001](#cp-001--la-corrida-deja-el-conteo-agrupado-por-regla) | Funcional | Alta | Sí | ☐ |
| HU-009 | [CA-02](../HU-009-conteo-por-regla.md#ca-02--el-registro-no-guarda-lo-revisado) | [CP-002](#cp-002--el-registro-no-contiene-la-clave-del-archivo-revisado) | Privacidad | Crítica | Sí | ☐ |
| HU-009 | [CA-03](../HU-009-conteo-por-regla.md#ca-03--dos-corridas-se-pueden-comparar) | [CP-003](#cp-003--dos-corridas-con-un-arreglo-en-medio-muestran-la-baja) | Funcional | Alta | Sí | ☐ |
| HU-009 | RNF — que el número sirva para decidir y no para puntuar | [CP-004](#cp-004--el-campo-nuevo-no-rompe-nada-y-la-advertencia-está-donde-se-lee) | No regresión | Media | Sí | ☐ |

**Cobertura:** 3 de 3 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — La corrida deja el conteo agrupado por regla

| Campo | Valor |
|---|---|
| **HU / CA** | HU-009 / CA-01 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Dudas 1 y 2 resueltas: dónde vive el registro y si se espera a la corrida completa |
| **Datos de entrada** | Una corrida sobre este repositorio |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr y leer el conteo | Está agrupado por identificador de regla |
| 2 | Comprobar que la suma de los conteos por regla es el total de hallazgos | Coincide |
| 3 | Comprobar que un hallazgo sin regla asignada aparece en su propio grupo | Aparece, no se pierde |
| 4 | Comprobar que el registro trae fecha y versión del estándar | Los dos |

**Resultado esperado final:** se sabe **qué regla** se incumple, no solo cuántos hallazgos hubo.

> **El paso 3 evita el conteo mentiroso.** Un hallazgo sin regla que desaparece del agrupado haría que la suma no cuadre y nadie lo notaría.

---

### CP-002 — El registro no contiene la clave del archivo revisado

| Campo | Valor |
|---|---|
| **HU / CA** | HU-009 / CA-02 |
| **Tipo** | Privacidad |
| **Prioridad** | Crítica |
| **Precondiciones** | Carpeta temporal |
| **Datos de entrada** | Un archivo con una cadena con forma de credencial, **armada para la prueba** |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir la cadena armada en un archivo de la carpeta temporal | Queda escrita |
| 2 | Correr la comprobación sobre esa carpeta | Sale el hallazgo, como debe |
| 3 | Buscar la cadena en el registro de conteos | **No está** |
| 4 | Buscar en el registro cualquier fragmento del archivo revisado | No hay ninguno |
| 5 | Comprobar que el registro trae solo identificador, número y fecha | Solo eso |
| 6 | Borrar la carpeta temporal y comprobar la limpieza | No queda rastro |

**Resultado esperado final:** el registro cuenta sin copiar, que es lo que el CA-02 exige.

> **Este caso corre antes de dar la fase por buena.** Un registro que arrastra contenido revisado es una filtración por la puerta de atrás.

---

### CP-003 — Dos corridas con un arreglo en medio muestran la baja

| Campo | Valor |
|---|---|
| **HU / CA** | HU-009 / CA-03 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | El CP-001 corrido |
| **Datos de entrada** | Una carpeta temporal con incumplimientos de dos reglas distintas |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr y guardar el conteo | Queda la primera corrida, con su fecha |
| 2 | Arreglar los incumplimientos de **una sola** de las dos reglas | Quedan arreglados |
| 3 | Correr otra vez y guardar el conteo | Queda la segunda corrida |
| 4 | Comparar los dos conteos | La regla arreglada baja |
| 5 | Comprobar que la otra regla **no** cambió | No cambió |
| 6 | Comprobar que la comparación se puede hacer con lo que el registro guarda | Se puede, sin datos extra |

**Resultado esperado final:** el conteo sirve para saber si algo mejoró, y qué exactamente.

> **El paso 5 es el que da valor al 4.** Una baja general no dice qué se arregló; la baja en una sola regla, sí.

---

### CP-004 — El campo nuevo no rompe nada, y la advertencia está donde se lee

| Campo | Valor |
|---|---|
| **HU / CA** | HU-009 / RNF |
| **Tipo** | No regresión |
| **Prioridad** | Media |
| **Precondiciones** | El número de pruebas de la suite anotado **antes** de tocar `comun.py` |
| **Datos de entrada** | La suite completa y la documentación del conteo |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Anotar cuántas pruebas hay y cuántas pasan, antes de tocar `comun.py` | Queda la línea base |
| 2 | Aplicar el campo con valor por omisión y correr la suite entera | Ninguna prueba que pasaba, falla |
| 3 | Correr cada subcomando por separado | Ninguno cambió de comportamiento |
| 4 | Comprobar que la advertencia de «no es para puntuar trabajo» está en la documentación del conteo | Está donde la lee quien usa el número |

**Resultado esperado final:** el campo entra sin romper, y el número nace con su advertencia puesta.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que el registro contenga cualquier fragmento del archivo revisado (riesgo `R-02`) | Inmediato. La fase se detiene: es una filtración |
| **Alta** | Que el campo nuevo rompa pruebas existentes (riesgo `R-03`) | Inmediato — entra con valor por omisión justamente para que no pase |
| **Media** | Que la suma de conteos por regla no dé el total | Antes de cerrar |
| **Media** | Que el conteo se pueda usar para calificar trabajo (riesgo `R-01`) | La advertencia va en la documentación del conteo, no solo en `metricas/` |
| **Baja** | Hallazgos sin regla asignada | Aparecen en su propio grupo; llenarlos es de cada validador |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 3 CA y los RNF con caso |
| Casos ejecutados | 4 de 4 |
| Fragmentos de contenido revisado en el registro | **0** |
| Claves reales usadas | **0** |
| Pruebas de la suite que dejan de pasar | **0** |
| Diferencia entre la suma por regla y el total | **0** |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
