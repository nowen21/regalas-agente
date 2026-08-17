# Plan de Pruebas — Fase A-EP-004-HU-012-contar-las-marcas-de-generacion-automatica   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-004-HU-012 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-004-HU-012-contar-las-marcas-de-generacion-automatica` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/planes/pruebas.md)).

**El CA-03 se prueba primero.** Es el que decide si el programa sirve: el estándar usa a propósito el punto medio, las comillas angulares y las casillas. Un programa que las cuente reporta el estándar entero y nadie lo vuelve a correr.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Positiva | Que las marcas de tipografía y las invisibles se cuenten | Carpetas temporales | Sí |
| Negativa | Que la notación propia del estándar **no** se cuente | Corrida sobre `base/` | Sí |
| Medición | Cuántas marcas tiene hoy el propio estándar | Este repositorio | Parcial |

**De dónde sale la lista de marcas.** De [`marcadores-de-ia.md`](../../../../../base/00-identidad-y-rol/marcadores-de-ia.md), leída por el programa. **No** de una copia dentro del código: dos listas de lo mismo se separan solas, y la del capítulo es la que manda.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los tres CA |
| Negativa | ☑ | El CA-03, que es el que decide si el reporte se puede creer |
| Límites | ☑ | Un símbolo que es notación propia en un contexto y marca en otro |
| Medición | ☑ | La cuenta del propio estándar, para el pendiente [11](../../../../../pendientes/11-limpiar-marcadores-de-ia-del-texto-del-estandar.md) |

### 3.3 Técnicas de diseño de casos

- **El falso positivo se prueba antes que el acierto** — arriba. Un detector que reporta el estándar entero no llega a usarse nunca.
- **Las invisibles se reportan por posición** — no se pueden citar copiando el carácter, porque no se ve. El hallazgo tiene que decir archivo, línea y **columna**, o no sirve para arreglar.
- **La corrida sobre `base/` como caso negativo mayor** — es el texto que más notación propia usa. Si el programa calla ahí y habla en un texto con marcas reales, discrimina.
- **La cuenta del estándar se separa de la del entregable nuevo** — el riesgo `R-01`: el propio estándar tiene marcas (por eso existe el pendiente 11). El resultado presenta las dos cuentas aparte, o la primera hace parecer inservible al programa.
- **Lista cerrada** — el riesgo `R-03`: lo que no está en `marcadores-de-ia.md` no se cuenta. Si no, el programa se vuelve un corrector de estilo y sus reportes dejan de aceptarse.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/pruebas.py` entera y el subcomando nuevo sobre `base/` y sobre las carpetas temporales.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-012 | [CA-01](../HU-012-marcas-de-generacion-automatica.md#ca-01--las-marcas-de-tipografía-se-cuentan) | [CP-002](#cp-002--el-texto-con-marcas-de-tipografía-se-reporta-y-el-limpio-no) | Funcional | Alta | Sí | ☐ |
| HU-012 | [CA-02](../HU-012-marcas-de-generacion-automatica.md#ca-02--las-marcas-invisibles-se-encuentran) | [CP-003](#cp-003--las-marcas-invisibles-se-reportan-por-su-posición) | Funcional | Alta | Sí | ☐ |
| HU-012 | [CA-03](../HU-012-marcas-de-generacion-automatica.md#ca-03--la-notación-del-estándar-no-se-cuenta-como-marca) | [CP-001](#cp-001--la-notación-propia-del-estándar-no-se-reporta), [CP-004](#cp-004--el-símbolo-que-es-notación-en-un-contexto-y-marca-en-otro) | Negativa | Crítica | Sí | ☐ |
| HU-012 | RNF — que el reporte se pueda creer | [CP-001](#cp-001--la-notación-propia-del-estándar-no-se-reporta) | Negativa | Crítica | Sí | ☐ |

**Cobertura:** 3 de 3 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — La notación propia del estándar no se reporta

| Campo | Valor |
|---|---|
| **HU / CA** | HU-012 / CA-03 y RNF |
| **Tipo** | Negativa |
| **Prioridad** | Crítica |
| **Precondiciones** | La lista de notación propia escrita (T-05) |
| **Datos de entrada** | `base/` entero |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Tomar la lista de lo que es notación del estándar | Está escrita en el capítulo, no dentro del programa |
| 2 | Correr sobre `base/` | El punto medio, las comillas angulares y las casillas **no** aparecen en el reporte |
| 3 | Contar cuántos hallazgos salen | Sale un número, anotado con su fecha |
| 4 | Separar esa cuenta de la de un entregable nuevo | Dos cuentas, presentadas aparte |
| 5 | Comprobar que lo que sí sale son marcas de la lista, no notación | Se revisa hallazgo por hallazgo |

**Resultado esperado final:** el reporte se puede creer, y la cuenta del propio estándar queda para el pendiente [11](../../../../../pendientes/11-limpiar-marcadores-de-ia-del-texto-del-estandar.md).

> **Este caso va primero.** Si el programa reporta la notación propia, no hace falta probar nada más: nadie lo va a correr dos veces.

---

### CP-002 — El texto con marcas de tipografía se reporta, y el limpio no

| Campo | Valor |
|---|---|
| **HU / CA** | HU-012 / CA-01 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | El CP-001 corrido |
| **Datos de entrada** | Un texto con varias marcas de la lista, y el mismo texto sin ellas |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr sobre el texto con marcas | Se reportan, con archivo y línea |
| 2 | Comprobar que se reportan **todas** las que trae | Ninguna se pasa |
| 3 | Correr sobre el texto limpio | No sale ninguna |
| 4 | Agregar una marca nueva a `marcadores-de-ia.md` y volver a correr | El programa la detecta sin tocar código: lee la lista |

**Resultado esperado final:** las marcas se cuentan, y la lista del capítulo es la que manda.

> **El paso 4 es el que evita la lista duplicada.** Si el programa trajera su propia copia, agregar una marca al capítulo no cambiaría nada.

---

### CP-003 — Las marcas invisibles se reportan por su posición

| Campo | Valor |
|---|---|
| **HU / CA** | HU-012 / CA-02 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Carpeta temporal |
| **Datos de entrada** | Un texto con un espacio que no se ve y un separador invisible |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir el texto con los caracteres invisibles | Queda escrito, y a la vista no se nota |
| 2 | Revisarlo a ojo | No se detecta nada: por eso hace falta el programa |
| 3 | Correr el programa | Los reporta |
| 4 | Comprobar que el hallazgo dice archivo, línea **y columna** | Los tres |
| 5 | Borrar el carácter y volver a correr | Deja de reportarse |

**Resultado esperado final:** lo que sobrevive a una revisión a ojo se puede encontrar y ubicar.

> **La columna no es un detalle.** Un carácter invisible no se puede citar copiándolo: sin la posición, el hallazgo no sirve para arreglar.

---

### CP-004 — El símbolo que es notación en un contexto y marca en otro

| Campo | Valor |
|---|---|
| **HU / CA** | HU-012 / CA-03 |
| **Tipo** | Límites |
| **Prioridad** | Crítica |
| **Precondiciones** | El CP-001 corrido |
| **Datos de entrada** | Un símbolo que la notación del estándar usa, puesto también donde sería marca |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir el símbolo como notación del estándar | No se reporta |
| 2 | Escribirlo donde sería marca de generación automática | Se anota qué hace el programa |
| 3 | Si no puede distinguirlos, declarar esa marca como no comprobable | Queda registrado, no simulado |
| 4 | Comprobar que la decisión quedó escrita en el capítulo | Quien reciba un hallazgo puede leer por qué su símbolo cuenta y otro no |

**Resultado esperado final:** el límite del programa queda escrito, en vez de producir un falso positivo imposible de arreglar (riesgo `R-02`).

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que la notación propia del estándar se reporte como marca | Inmediato. El programa quedaría inservible |
| **Alta** | Que una marca invisible se reporte sin posición | Inmediato — el hallazgo no sirve para arreglar |
| **Media** | Que el programa reporte cientos de marcas en el propio estándar (riesgo `R-01`) | Es el dato que el pendiente 11 necesita: se presenta aparte de la cuenta de un entregable nuevo |
| **Media** | Que un símbolo no se pueda clasificar por contexto (riesgo `R-02`) | Se declara no comprobable y se escribe por qué |
| **Baja** | Que se pida contar algo que no está en la lista (riesgo `R-03`) | La lista es cerrada: lo que no está, no se cuenta |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 3 CA y los RNF con caso |
| Casos ejecutados | 4 de 4 |
| Notación propia reportada como marca | **0** |
| Marcas invisibles reportadas sin columna | **0** |
| Listas de marcas dentro del programa | **0** — se lee la del capítulo |
| Cuenta de marcas del propio estándar | Anotada aparte, con su fecha |
| Marcas del texto de prueba que se pasaron | **0** |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
