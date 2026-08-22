# Plan de Pruebas — Fase B-EP-004-HU-004, el encuadre de la plantilla sobrevive al llenado   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó al correrlas va en el `resultado_pruebas.md` de la misma fase, para no perder la línea base aprobada. La lista de tareas vive en el `plan_trabajo` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-B-EP-004-HU-004 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase B de HU-004, épica EP-004 |
| **Fecha** | 2026-08-22 |
| **Elaborado por** | El agente |
| **Aprobado por** | El usuario |
| **Estado** | Borrador |

**Proporcionalidad.** Una sola fase, así que van las secciones 3, 5, 6, 9 y 12.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

Unidad sobre `plantillas.validar()`, con documentos escritos en carpeta temporal. Más una corrida de sistema contra los documentos reales del repositorio, que es la que mide el riesgo R-01.

### 3.2 Tipos de prueba

| Tipo | Para qué |
|---|---|
| Funcional negativa | Que repruebe el encuadre borrado y el encuadre reemplazado |
| Funcional positiva | Que no repruebe el documento que lo conserva |
| No regresión | Que las cuatro comprobaciones que ya existían sigan igual, y que ningún documento real quede reprobado por esto |

### 3.3 Técnicas de diseño de casos

**La mitad de los casos son de lo que NO tiene que reprobar.** Es la prueba que falta siempre en este repositorio, y está dicho en el [pendiente 11](../../../../../pendientes/hecho/limpiar-marcadores-de-ia-del-texto-del-estandar.md) al describir el trinquete. Un validador que reprueba de más enseña a ignorar todos los veredictos.

### 3.4 Priorización

CP-001 a CP-003 son críticos. CP-004 a CP-006 son los que impiden el falso positivo, y sin ellos la fase no cierra aunque los tres primeros pasen.

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`python -m pytest validadores/tests/test_encuadre_de_la_plantilla.py` para lo nuevo, y `python -m pytest validadores/tests` entera para la no regresión. Fuera de eso, `validar.py estandar`.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-004 | [CA-05](../HU-004-forma-de-los-documentos.md#ca-05--el-texto-fijo-de-la-plantilla-sobrevive-al-llenado) | CP-001, CP-002, CP-003 | Funcional | Crítica | Sí | ☐ |
| HU-004 | RN-07 | CP-001, CP-004 | Funcional | Crítica | Sí | ☐ |
| HU-004 | RN-08 | CP-003, CP-005 | Funcional | Alta | Sí | ☐ |
| HU-004 | Transversal, no regresión | CP-006, CP-007 | No funcional | Alta | Sí | ☐ |

**Cobertura:** 4 de 4 exigencias cubiertas = 100%.

---

## 6. Casos de prueba

### CP-001 — El encuadre borrado se reprueba

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / CA-05, RN-07 |
| **Tipo** | Funcional, caso negativo |
| **Prioridad** | Crítica |
| **Precondiciones** | Una plantilla con texto fijo antes del primer separador |
| **Datos de entrada** | Un documento igual pero sin ese texto |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir la plantilla con su recuadro de instrucciones y su línea fija | Queda el archivo, con las dos cosas |
| 2 | Escribir el documento sin la línea fija | Queda el archivo |
| 3 | Correr `validar()` del documento contra la plantilla | Devuelve una falla que nombra el archivo |
| 4 | Leer el mensaje de la falla | Dice qué texto tenía la plantilla en ese lugar |

**Resultado esperado final:** borrar el encuadre deja de pasar en silencio.

---

### CP-002 — El encuadre conservado no se reprueba

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / CA-05 |
| **Tipo** | Funcional, camino feliz |
| **Prioridad** | Crítica |
| **Precondiciones** | La misma plantilla del CP-001 |
| **Datos de entrada** | Un documento que conserva el encuadre, adaptado en su redacción y con sus citas |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir el documento con el encuadre reescrito, más corto, citando una de las reglas de la plantilla | Queda el archivo |
| 2 | Correr `validar()` | Ninguna falla de encuadre |

**Resultado esperado final:** adaptar la redacción del encuadre sigue siendo legal. Es lo que el molde permite.

---

### CP-003 — El encuadre reemplazado por otra cosa se reprueba

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / CA-05, RN-08 |
| **Tipo** | Funcional, caso negativo |
| **Prioridad** | Crítica |
| **Precondiciones** | La misma plantilla |
| **Datos de entrada** | El caso real: una nota de procedencia con fecha, fuentes y el número de un pendiente, sin una sola cita de regla |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir el documento con la nota de procedencia en el lugar del encuadre | Queda el archivo |
| 2 | Correr `validar()` | Devuelve una falla |
| 3 | Leer el mensaje | Dice que ese lugar es instrucción de uso y que la plantilla cita reglas ahí |

**Resultado esperado final:** el caso que ya ocurrió en `prompts/cimiento-planteamiento.md` queda cubierto.

---

### CP-004 — Una plantilla sin texto fijo no exige nada

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / RN-07 |
| **Tipo** | Funcional, no reprobar de más |
| **Prioridad** | Alta |
| **Precondiciones** | Una plantilla cuyo primer separador viene enseguida del H1 |
| **Datos de entrada** | Un documento cualquiera de esa plantilla |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `validar()` | Ninguna falla de encuadre, porque no hay encuadre que conservar |

---

### CP-005 — Una plantilla que no cita reglas no le exige citas al documento

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / RN-08 |
| **Tipo** | Funcional, no reprobar de más |
| **Prioridad** | Alta |
| **Precondiciones** | Una plantilla con texto fijo que no cita ninguna regla, como el plan de trabajo |
| **Datos de entrada** | Un documento con su texto fijo, tampoco con citas |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `validar()` | Ninguna falla: la exigencia de citar sale de la plantilla, y esa plantilla no la impone |

---

### CP-006 — Las cuatro comprobaciones anteriores siguen igual

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / no regresión |
| **Tipo** | No funcional |
| **Prioridad** | Alta |
| **Precondiciones** | La fase construida |
| **Datos de entrada** | La batería completa de `validadores/tests` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `python -m pytest validadores/tests` | Todo en verde, sin una prueba que antes pasara y ahora falle |
| 2 | Correr `python validadores/validar.py estandar` | Sin incumplimientos |

---

### CP-007 — Ningún documento real queda reprobado estando bien

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / no regresión |
| **Tipo** | No funcional, es el que mide el riesgo R-01 |
| **Prioridad** | Alta |
| **Precondiciones** | La fase construida |
| **Datos de entrada** | Los documentos del repositorio que `deducir_plantilla()` sabe resolver |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Recorrer esos documentos y correr `validar()` de cada uno | Sale una lista de fallas de encuadre |
| 2 | Abrir cada uno de los reprobados y leer su encabezado | O le falta el encuadre de verdad, o el validador se equivocó |
| 3 | Contar los que se equivocó | Cero. Con uno solo, se corrige el validador antes de cerrar la fase |

**Resultado esperado final:** la comprobación entra sin dejar ruido detrás.

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| Crítica | Reprueba un documento que está bien, o deja pasar el caso del CP-003 |
| Alta | El mensaje de la falla no dice qué hay que hacer |
| Media | Funciona pero se cae con un documento de forma rara |
| Baja | Redacción del mensaje |

### 9.2 Flujo del defecto

Se anota en el `resultado_pruebas.md` con su caso de origen. Crítico abierto, la fase no cierra.

### 9.3 Contenido mínimo de un reporte

El caso, el documento de entrada, qué se esperaba, qué salió.

### 9.4 Registro

En el `resultado_pruebas.md` de la fase.

---

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Meta |
|---|---|
| Exigencias con al menos un caso | 4 de 4 |
| Casos en verde | 7 de 7 |
| Documentos reales reprobados estando bien | 0 |
| Pruebas que antes pasaban y ahora fallan | 0 |

### 12.2 Dónde se miden

En el `resultado_pruebas.md` de esta fase.
