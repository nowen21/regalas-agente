# Plan de Pruebas — Fase A-EP-006-HU-004-retrodocumentar-la-busqueda-por-significado   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-006-HU-004 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-006-HU-004-retrodocumentar-la-busqueda-por-significado` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/planes/pruebas.md)).

**Nada del contenido de las señales sale de la máquina.** Es [`00·N6`](../../../../../base/00-nucleo-blindado.md#n6--secretos-y-datos-sensibles-nunca-se-exponen-blindada), y se **comprueba**, no se supone.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Con modelo | Que encuentre lo escrito con otras palabras | Base temporal, entorno aislado con las dependencias | Sí |
| Sin modelo | Que la búsqueda siga funcionando y lo diga | Base temporal, sin las dependencias | Sí |
| Aislamiento | Que ningún dato salga a la red | Entorno aislado | Sí |
| Comparación | Que lo combinado no pierda lo que la búsqueda por palabra encontraba | Base temporal | Sí |

**Cómo se monta el escenario sin modelo.** Simulando la falta de dependencias, **no desinstalándolas**: desinstalar rompe el entorno de trabajo de quien corre la prueba (riesgo `R-03`).

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los dos CA |
| Degradación | ☑ | El CA-02, que es el que sostiene que la parte sea opcional |
| Seguridad | ☑ | Que nada salga de la máquina |
| No regresión | ☑ | Que lo combinado no pierda resultados de la búsqueda por palabra |

### 3.3 Técnicas de diseño de casos

- **La mejora se mide con búsquedas reales** — lo que importa es si encuentra lo que alguien buscaría, no cuánto puntúa el modelo. Un puntaje alto con resultados inútiles no sirve.
- **Lo combinado no puede perder** — el caso de no regresión compara los resultados con y sin significado: si lo combinado devuelve **menos** que la búsqueda por palabra, la mejora es un retroceso.
- **El aislamiento se comprueba por el programa, no por la red** — el riesgo `R-02`: se comprueba que el programa **no abra ninguna conexión**, no que la red esté caída. Una prueba con la red desconectada pasaría igual con un programa que sí manda datos.
- **La mejora chica también es resultado** — el riesgo `R-01`: si no vale instalar el modelo, se escribe la medida y se decide con el dato.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `memoria/pruebas.py` entera, sobre bases temporales y en entorno aislado.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-004 | [CA-01](../HU-004-busqueda-por-significado.md#ca-01--encuentra-lo-que-se-escribió-con-otras-palabras) | [CP-001](#cp-001--encuentra-la-señal-buscándola-con-otras-palabras), [CP-002](#cp-002--lo-combinado-no-pierde-lo-que-la-búsqueda-por-palabra-encontraba) | Funcional | Alta | Sí | ☐ |
| HU-004 | [CA-02](../HU-004-busqueda-por-significado.md#ca-02--sin-el-modelo-la-búsqueda-sigue-funcionando) | [CP-003](#cp-003--sin-las-dependencias-la-búsqueda-responde-igual-y-lo-dice) | Degradación | Crítica | Sí | ☐ |
| HU-004 | RNF — que la memoria sirva aunque el modelo no esté | [CP-004](#cp-004--nada-sale-de-la-máquina) | Seguridad | Crítica | Sí | ☐ |

**Cobertura:** 2 de 2 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — Encuentra la señal buscándola con otras palabras

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / CA-01 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Entorno aislado con las dependencias, y base temporal con señales de prueba |
| **Datos de entrada** | Una señal, y una consulta que dice lo mismo con **otras palabras** |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar con las palabras exactas de la señal | La encuentra |
| 2 | Buscar con la consulta que no comparte ninguna palabra | La encuentra igual |
| 3 | Comprobar que sin el modelo el paso 2 **no** la encontraría | No la encuentra: eso es lo que aporta |
| 4 | Repetir con tres consultas reales, de las que alguien haría | Se anota cuántas mejoraron |
| 5 | Anotar la medida de la mejora | Queda el dato para decidir si vale instalarlo |

**Resultado esperado final:** se sabe cuánto aporta el significado, con búsquedas que alguien haría de verdad.

> **El paso 3 es el que aísla el aporte.** Sin él, no se distingue lo que agrega el modelo de lo que la búsqueda por palabra ya hacía.

---

### CP-002 — Lo combinado no pierde lo que la búsqueda por palabra encontraba

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / CA-01 |
| **Tipo** | No regresión |
| **Prioridad** | Alta |
| **Precondiciones** | El CP-001 corrido |
| **Datos de entrada** | Un conjunto de consultas que la búsqueda por palabra resuelve bien |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr las consultas **sin** significado y guardar los resultados | Queda la línea base |
| 2 | Correr las mismas **con** significado | Salen resultados |
| 3 | Comprobar que todo lo de la línea base sigue apareciendo | Nada se perdió |
| 4 | Anotar lo que aparece de más | Es la ganancia |
| 5 | Anotar lo que aparece de más y **no** sirve | Es el ruido: también se mide |

**Resultado esperado final:** la mejora suma sin restar, y se sabe cuánto ruido trae.

---

### CP-003 — Sin las dependencias, la búsqueda responde igual y lo dice

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / CA-02 |
| **Tipo** | Degradación |
| **Prioridad** | Crítica |
| **Precondiciones** | Escenario con las dependencias **simuladas como ausentes** |
| **Datos de entrada** | Las mismas consultas del CP-002 |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr una búsqueda sin las dependencias | Responde, con la búsqueda por palabra |
| 2 | Comprobar que **no falla** ni pide instalar nada para funcionar | No falla |
| 3 | Comprobar que **dice** que el significado no está disponible | Lo dice: el usuario sabe qué le falta |
| 4 | Comprobar que los resultados son los mismos que sin significado en el CP-002 | Los mismos |
| 5 | Comprobar que el entorno de trabajo no se modificó | Sin cambios |

**Resultado esperado final:** la parte opcional es opcional de verdad, que es lo que hace usable la memoria sin instalar nada.

> **El paso 3 importa tanto como el 1.** Degradarse en silencio deja al usuario creyendo que busca por significado cuando no.

---

### CP-004 — Nada sale de la máquina

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / RNF |
| **Tipo** | Seguridad |
| **Prioridad** | Crítica |
| **Precondiciones** | Entorno aislado con las dependencias |
| **Datos de entrada** | Una señal con contenido reconocible |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Calcular los vectores de la señal | Se calculan |
| 2 | Comprobar que el programa **no abrió ninguna conexión** | Ninguna |
| 3 | Comprobar que el modelo se leyó del disco local | Del disco |
| 4 | Buscar por significado y repetir la comprobación | Ninguna conexión |
| 5 | Comprobar que la comprobación no depende de que la red esté caída | No depende |

**Resultado esperado final:** [`00·N6`](../../../../../base/00-nucleo-blindado.md#n6--secretos-y-datos-sensibles-nunca-se-exponen-blindada) queda comprobado, no supuesto.

> **El paso 5 es el que hace válida la prueba.** Con la red desconectada, un programa que manda datos pasaría igual.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que el contenido de una señal salga de la máquina | Inmediato. Es una regla `[BLINDADA]` |
| **Crítica** | Que sin las dependencias la búsqueda falle | Inmediato. El CA-02 queda en «No» y la parte deja de ser opcional |
| **Alta** | Que lo combinado pierda resultados de la búsqueda por palabra | Inmediato — la mejora sería un retroceso |
| **Media** | Que la mejora sea chica (riesgo `R-01`) | Es un resultado útil: se escribe la medida y se decide con el dato |
| **Media** | Que la prueba de la red dependa del entorno (riesgo `R-02`) | Se corrige el caso: se comprueba el programa, no la red |
| **Baja** | Que instalar las dependencias cambie el entorno (riesgo `R-03`) | Entorno aislado y temporal |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 2 CA y los RNF con caso |
| Casos ejecutados | 4 de 4 |
| Conexiones de red abiertas por el programa | **0** |
| Resultados perdidos por la búsqueda combinada | **0** |
| Consultas que mejoran con significado | Medidas, con las que no también |
| Cambios en el entorno de trabajo | **0** |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
