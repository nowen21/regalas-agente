# Plan de Pruebas — Fase `A-EP-004-HU-021-la-cuenta-mira-el-veredicto`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba cada criterio de aceptación**, con qué datos y en qué ambiente, y cuándo se da por aprobado. Lo que se pide vive en la [HU-021](../HU-021-la-cuenta-distingue-lo-terminado-de-lo-cumplido.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que el número que responde «cuánto falta» deja de contar como hecha una fase que no cumplió, sin repartir entre las cuentas lo que no se puede leer.

### 1.2 Alcance

**Entra:** la cuenta en `validadores/fases.py`, sus pruebas, y los tres moldes que hablan del veredicto.

**No entra:** arreglar las 19 fases que no cumplen, rellenar los 25 resultados sin veredicto, ni los veredictos de épicas o planes.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [HU-021](../HU-021-la-cuenta-distingue-lo-terminado-de-lo-cumplido.md) | Los cinco criterios y sus pasos |
| [plan_trabajo.md](plan_trabajo.md) | Lo medido, y por qué la cuenta nueva va aparte |
| `S-054` | El hallazgo que la originó |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| La cuenta nueva | Que distinga terminada de cumplida, y que aparte lo ilegible |
| `linea_inventario` | Que diga las tres y se entienda sin documentación |
| Los tres moldes | Que usen un solo vocabulario y no prohíban lo que se hace con razón |
| `inventario`, el de siempre | Que **no** haya cambiado: sus 10 pruebas pasan sin tocarlas |

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

**Unitario** sobre árboles de mentira, para las tres cuentas y los bordes. **De sistema** sobre el árbol real, para la línea y el número.

### 3.2 Tipos de prueba

| Tipo | Por qué |
|---|---|
| Funcional | Las tres cuentas y sus combinaciones |
| **De partición** | Terminada-y-cumple, terminada-y-no-cumple, y sin veredicto legible |
| De no regresión | Las 10 pruebas de `inventario`, **sin tocarlas** |
| De sabotaje | Que las pruebas cacen lo que dicen cazar |

### 3.3 Técnicas de diseño de casos

**Partición** por veredicto. **Bordes**: una historia con dos fases donde solo una cumple, una fase sin resultado, y un veredicto escrito en otra caja o con texto detrás.

### 3.4 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-002, CP-003 | Son la razón de la fase: no contar como hecho lo que no cumple, y no repartir lo ilegible |
| Alta | CP-001, CP-006 | Que la línea se entienda, y que lo de antes no se rompa |
| Media | CP-004, CP-005, CP-007 | Moldes, bordes y versionado |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

`python validadores/pruebas.py` **entera**, y **con el conteo a la vista**.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- Los dos planes, aprobados.
- **T-01 hecha:** el vocabulario fijado en el molde, porque es contra lo que lee el programa.

### 4.2 Criterios de salida

- Los siete casos ejecutados.
- Los cinco criterios en verde.
- **Las 10 pruebas de `inventario`, pasando sin haberlas tocado.**
- La suite completa en verde, con conteo distinto de cero.

### 4.3 Criterios de suspensión y reanudación

Se suspende si al medir el número resulta que **no baja**: eso significaría que la cuenta nueva no está leyendo el veredicto, y hay que entender por qué antes de seguir.

---

## 5. Matriz de trazabilidad

| CA / RNF | Caso | Tipo |
|---|---|---|
| CA-01 — la línea dice las dos cosas | CP-001 | Camino feliz |
| CA-02 — una fase que no cumple no cuenta cumplida | CP-002 | Partición |
| CA-03 — lo ilegible se cuenta aparte | CP-003 | Que **no** pase |
| CA-04 — el molde puede decir «No cumple» | CP-004 | Documentación |
| CA-05 — la versión sube y avisa | CP-007 | Funcional |
| Transversal · límites | CP-005 | Bordes |
| Transversal · no regresión | CP-006 | No regresión |

---

## 6. Casos de prueba

### CP-001 — La línea dice las dos cosas y los números cuadran

| Campo | Valor |
|---|---|
| **HU / CA** | HU-021 / CA-01 |
| **Tipo** | Funcional — camino feliz |
| **Prioridad** | Alta |
| **Precondiciones** | El árbol real del estándar |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `validar.py fases` | Termina con su línea de inventario |
| 2 | Leer la línea | Dice el total, **cuántas cumplen**, cuántas terminaron sin cumplir y cuántas no se pudieron leer |
| 3 | Sumar los números | Cuadran con el total, sin sobrar ni faltar |
| 4 | Leerla sin conocer el proyecto | Se entiende qué es cada número, sin ir a la documentación |

---

### CP-002 — Una fase que no cumple no cuenta cumplida

| Campo | Valor |
|---|---|
| **HU / CA** | HU-021 / CA-02 |
| **Tipo** | Partición |
| **Prioridad** | Crítica |
| **Precondiciones** | Árbol de mentira con una historia de **dos** fases, las dos con sus cinco documentos |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Poner en las dos fases `Concepto: Cumple` | La historia cuenta terminada **y** cumplida |
| 2 | Cambiar una a `Concepto: No cumple` | Cuenta terminada, **no** cumplida |
| 3 | Cambiar las dos a `No cumple` | Igual: terminada, no cumplida |
| 4 | Devolverlas a `Cumple` | Vuelve a contar en las dos |

**Basta una fase que no cumpla.** Es la misma regla que ya usa `inventario` para «completa», y por el mismo motivo: cerrar la primera no cierra la historia.

---

### CP-003 — Lo que no se puede leer se cuenta aparte

| Campo | Valor |
|---|---|
| **HU / CA** | HU-021 / CA-03 |
| **Tipo** | Que **no** pase |
| **Prioridad** | Crítica |
| **Precondiciones** | Árbol con una historia cuya fase tiene los cinco documentos y **ningún** veredicto |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Contar | La línea trae una tercera cuenta, con esa historia dentro |
| 2 | Buscarla entre las que cumplen | **No está** |
| 3 | Buscarla entre las que terminaron sin cumplir | **No está** |
| 4 | Ponerle `Concepto: Cumple` y contar | Sale de la tercera y entra en las que cumplen |

**Repartirla habría hecho que el número mintiera de una forma nueva**, que es exactamente lo que esta fase viene a terminar.

---

### CP-004 — Los moldes usan un solo vocabulario

| Campo | Valor |
|---|---|
| **HU / CA** | HU-021 / CA-04 |
| **Tipo** | Documentación |
| **Prioridad** | Media |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir el molde del cierre y buscar el campo del veredicto | Existe, **como campo con su rótulo**, no en prosa |
| 2 | Leer qué valores ofrece | `Cumple` o `No cumple`, y **ninguna tercera opción** |
| 3 | Comparar con el molde del resultado | Es el mismo vocabulario, palabra por palabra |
| 4 | Buscar en los tres moldes la frase que prohíbe cerrar con un rojo | Ya no está, o dice que cierra **declarándolo** |

**El paso 1 importa tanto como el 2:** el veredicto en prosa es lo que hoy hace que 70 cierres no se puedan leer.

---

### CP-005 — Los bordes

| Campo | Valor |
|---|---|
| **HU / CA** | HU-021 / transversal de límites |
| **Tipo** | Bordes |
| **Prioridad** | Media |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Una historia **sin ninguna fase** | Cuenta incompleta, y no entra en las cuentas de veredicto |
| 2 | Una fase **sin `resultado_pruebas.md`** | Cuenta como sin veredicto legible, y no revienta |
| 3 | Un veredicto **con texto detrás**: `Cumple, con los tres criterios` | Se lee como `Cumple` |
| 4 | Un veredicto en **otra caja**: `cumple` | Se decide y se declara qué pasa |
| 5 | Un árbol **vacío** | Devuelve ceros y no imprime línea |

---

### CP-006 — Lo de antes no se rompió

| Campo | Valor |
|---|---|
| **HU / CA** | HU-021 / transversal |
| **Tipo** | No regresión |
| **Prioridad** | Alta |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr las **10 pruebas** que usan `fases.inventario`, **sin tocarlas** | Todas en verde |
| 2 | Comprobar que `inventario` sigue devolviendo **tres** valores | Su firma no cambió |
| 3 | Comparar el total y las incompletas con lo de antes del cambio | Los mismos números |
| 4 | Correr la suite completa | En verde, y con conteo distinto de cero |

**El paso 3 es el que separa lo que esta fase agrega de lo que podría haber roto.** El total y las incompletas no tienen por qué moverse: lo que aparece es una cuenta nueva.

---

### CP-007 — La versión sube y avisa del cambio de significado

| Campo | Valor |
|---|---|
| **HU / CA** | HU-021 / CA-05 |
| **Tipo** | Funcional |
| **Prioridad** | Media |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Anotar el número de completas **antes** del cambio | Queda la referencia |
| 2 | Aplicar y volver a medir | Se sabe **cuánto** bajó, sin inventarlo |
| 3 | Leer la entrada del `CHANGELOG` | Dice que el número **cambia de significado**, y trae los dos valores |
| 4 | Comprobar que no se lee como retroceso | Dice que no se perdió trabajo: **antes contaba de más** |
| 5 | Correr `validar.py versionado` | Sin incumplimientos |

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes

La máquina de quien trabaja, con la biblioteca estándar.

### 7.2 Datos de prueba

Árboles de mentira en carpeta temporal. **Ningún documento real se edita para probar.**

### 7.3 Usuarios de prueba

No aplica. **Ninguna prueba usa credenciales** (`00·N6`).

### 7.4 Qué NO reproduce el entorno de pruebas  ·  `08·T4`

Los árboles de mentira tienen una o dos historias. **Por eso `CP-001` y `CP-006` corren contra el árbol real**: son los únicos que ven las 128 fases y la variedad de redacciones de verdad.

---

## 8. Herramientas

| Herramienta | Para qué |
|---|---|
| `unittest`, de la biblioteca estándar | La suite |
| Un guion de sabotaje | Romper cada pieza a propósito |

**El guion se restaura con copia**, limpia sus rastros **tras cada sabotaje** y no al final, y **se cae si su corrida final reporta cero pruebas**.

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué la define |
|---|---|
| Crítica | Lo ilegible se reparte, o una fase que no cumple cuenta cumplida |
| Alta | Alguna de las 10 pruebas de `inventario` hubo que tocarla |
| Media | Un borde revienta, o la línea no se entiende sola |
| Baja | Redacción de la línea o de la entrada |

### 9.2 Flujo del defecto

Se anota en el `resultado_pruebas.md`, se arregla, y **se vuelve a correr el caso completo**.

### 9.3 Contenido mínimo de un reporte

Qué se esperaba, qué pasó, con qué datos, y en qué archivo y línea.

### 9.4 Registro

En el `resultado_pruebas.md` de esta fase.

---

## 10. Cronograma

Un solo tramo. La suite completa al final.

---

## 11. Roles y responsabilidades

Una sola persona cumple los roles. El agente construye y corre; el usuario aprueba.

---

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Meta |
|---|---|
| Casos ejecutados | 7 de 7 |
| Criterios en verde | 5 de 5 |
| **Pruebas de `inventario` que hubo que tocar** | **0** |
| Historias sin veredicto repartidas entre las otras cuentas | **0** |
| Sabotajes cazados | Todos |
| Fallas en la suite completa | 0, con conteo distinto de cero |

### 12.2 Dónde se miden

En el `resultado_pruebas.md`, con la salida pegada.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Que se ajuste una prueba de `inventario` «de paso» y no se note | Se cuenta cuántas se tocaron, y la meta es cero |
| Que un sabotaje pase en verde | Se corre el escenario y se mira el estado final |
| Que la prueba de la línea se escriba copiando el texto que produce el código | Se escribe **desde lo que la historia pide**, no desde lo que salió |

---

## 14. Control de versiones

| Versión | Fecha | Cambio |
|---|---|---|
| 1 | 2026-08-27 | Redacción inicial, junto con el plan de trabajo |

---

## 15. Aprobación

| Rol | Estado |
|---|---|
| Usuario | Pendiente. **No se toca nada hasta que este plan y el de trabajo estén aprobados** (`02·F4`) |
