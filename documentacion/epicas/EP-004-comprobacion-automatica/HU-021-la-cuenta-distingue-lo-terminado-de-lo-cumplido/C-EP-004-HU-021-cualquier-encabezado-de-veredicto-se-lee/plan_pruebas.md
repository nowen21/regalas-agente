# Plan de Pruebas — Fase `C-EP-004-HU-021-cualquier-encabezado-de-veredicto-se-lee`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** el criterio de esta fase, con qué datos y cuándo se da por aprobado. Lo que se pide vive en la [HU-021](../HU-021-la-cuenta-distingue-lo-terminado-de-lo-cumplido.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que el lector reconoce el encabezado `## N. Veredicto`, **y que sigue sin reconocer los seis títulos que se le parecen**.

### 1.2 Alcance

**Entra:** `veredicto_de` en `validadores/fases.py` y sus pruebas.

**No entra:** uniformar los 130 resultados, las cinco fases que de verdad no lo dicen, ni resolver los tres «No cumple» que van a aparecer.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Los seis títulos enumerados, y por qué solo uno sirve |
| La fase [`B`](../B-EP-004-HU-021-el-veredicto-se-lee-en-sus-tres-formas/funcionalidad_implementada.md) | El defecto que se corrige, y cómo se cometió |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| `veredicto_de` | Que lea `## N. Veredicto`, y que **no** lea los otros cinco títulos |
| `por_veredicto` | Que las diez historias salgan de «no dicen», **incluidas las tres que no cumplen** |
| Las 22 pruebas de `A` y `B` | Que sigan pasando **sin tocarlas** |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

**Unitario** sobre árboles de mentira, uno por título. **De sistema** sobre el árbol real, para el número.

| Tipo | Por qué |
|---|---|
| **De partición por título** | Hay seis títulos distintos y solo uno sirve |
| **De que no pase** | Es el riesgo real: 70 encabezados empiezan por «Veredicto» y no son el veredicto de la fase |
| De no regresión | Las 22 de `A` y `B` |
| De sabotaje | Que las pruebas cacen lo que dicen cazar |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-002 | Tomar un «por criterio» haría que el lector mintiera en la dirección optimista: **peor que el defecto que se corrige** |
| Alta | CP-001, CP-003 | El título que sirve, y que lo de antes no se rompa |
| Media | CP-004 | El número, y adónde va cada una de las diez |

### 3.3 Alcance de la ejecución automatizada  ·  `02·F5`

`python validadores/pruebas.py` **entera**, con el conteo a la vista.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- Los dos planes, aprobados.
- Los seis títulos enumerados y contado qué sigue a cada uno, que está en el plan §2.0.

### 4.2 Criterios de salida

- Los cuatro casos ejecutados.
- **Las 22 pruebas de `A` y `B`, pasando sin haberlas tocado.**
- Las diez recuperadas, **nombradas una por una** con adónde fueron.
- La suite completa en verde, con conteo distinto de cero.

### 4.3 Criterios de suspensión y reanudación

Se suspende si al medir **no se recuperan exactamente diez**, o si **las tres que dicen «No cumple» no aparecen entre ellas**.

**La segunda mitad es la que vale.** Si se recuperaran solo las siete que cumplen, el número quedaría **mejor y más falso** — y eso se vería como un éxito.

**Y hay una trampa conocida de antemano:** abrir esta fase con su carpeta ya movió la línea. La `HU-021` salió de «terminadas» al existir una carpeta sin sus cinco documentos, y `56 cumplen` es la base **con esta fase ya abierta**. Es `S-053` por cuarta vez, y el [pendiente 88](../../../../../pendientes/88-el-andamio-crea-una-fase-que-ya-cuenta-como-terminada.md) lo recoge.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| CA-03 — se lee lo que se puede leer | CP-001 | Partición por título |
| CA-03 — y **solo** lo que se puede leer | CP-002 | Que **no** pase |
| Transversal · no regresión | CP-003 | No regresión |
| El efecto sobre el número | CP-004 | De sistema |

---

## 6. Casos de prueba

### CP-001 — El título que sirve se lee

| Campo | Valor |
|---|---|
| **HU / CA** | HU-021 / CA-03 |
| **Tipo** | Partición por título |
| **Prioridad** | Alta |
| **Precondiciones** | Un árbol de mentira por título |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `## 5. Veredicto` y debajo `**Cumple.**` | Se lee `Cumple` |
| 2 | Lo mismo con `**No cumple.**` | Se lee `No cumple` |
| 3 | `## 2. Veredicto de la fase`, que ya servía | Se sigue leyendo |
| 4 | El número del encabezado cambiado, y con y sin punto | Se lee igual |

---

### CP-002 — Los cinco títulos que se le parecen no se leen

| Campo | Valor |
|---|---|
| **HU / CA** | HU-021 / CA-03 |
| **Tipo** | Que **no** pase |
| **Prioridad** | Crítica |
| **Precondiciones** | Árboles de mentira con cada título parecido |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `## 4. Veredicto por criterio de aceptación`, **con `Cumple` en la primera fila de su tabla** | **No se lee**: devuelve nada |
| 2 | `## 4. Veredicto por criterio de aceptación y requisito no funcional` | **No se lee** |
| 3 | `## 6. Veredicto final` | **No se lee** |
| 4 | `## 3. Veredicto por exigencia` y `## 3. Veredicto por criterio de la historia` | **No se leen** |
| 5 | `## 5. Veredicto` con **nada** debajo | **No se lee** |

**Por qué es el caso crítico:** hay **70 encabezados** que empiezan por «Veredicto» y son la tabla criterio por criterio. Si el patrón los toma, el lector devuelve **el primer criterio** como si fuera el veredicto de la fase. Eso miente en la dirección optimista — **peor que el defecto que esta fase corrige**, que miente en la pesimista.

**El paso 1 es el que lo demuestra**, porque le pone delante justo la tabla que lo tentaría.

---

### CP-003 — Lo de antes no se rompió

| Campo | Valor |
|---|---|
| **HU / CA** | HU-021 / transversal |
| **Tipo** | No regresión |
| **Prioridad** | Alta |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr las **22 pruebas** de las fases `A` y `B`, **sin tocarlas** | Todas en verde |
| 2 | Comprobar que `veredicto_de` y `por_veredicto` conservan su firma | Sin cambios |
| 3 | Comprobar que **ninguna historia que ya tenía veredicto lo cambia** | Cero cambios |
| 4 | Correr la suite completa | Verde, con conteo distinto de cero |

**El paso 3 ya se midió antes de escribir esto**, y dio cero. Se repite en la corrida final porque medir una vez no es una prueba.

---

### CP-004 — Las diez, una por una

| Campo | Valor |
|---|---|
| **HU / CA** | HU-021 / CA-03 |
| **Tipo** | De sistema |
| **Prioridad** | Media |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Anotar la línea **antes** | `56 cumplen, 13 no cumplen, 15 no dicen` |
| 2 | Aplicar y volver a correr | `63 cumplen, 16 no cumplen, 5 no dicen` |
| 3 | **Nombrar las diez** y adónde fue cada una | Siete a «cumplen», **tres a «no cumplen»** |
| 4 | Nombrar las cinco que siguen mudas | Son las que de verdad no lo dicen |
| 5 | Comprobar que el total no se movió | El mismo número |

**El paso 3 es el que separa un arreglo de un maquillaje.** Un cambio que solo recuperara las que cumplen daría un número mejor **y más falso**.

---

## 7. Datos y ambientes de prueba

Árboles de mentira en carpeta temporal, creados y borrados por la prueba. **Ninguna prueba usa credenciales** (`00·N6`), y ningún documento real se edita (`08·T4`).

**Qué no reproduce el entorno:** los árboles tienen una fase. **Por eso `CP-004` corre contra el árbol real**, que es el único que tiene los seis títulos de verdad.

---

## 8. Herramientas

`unittest` de la biblioteca estándar, y un guion de sabotaje que **se restaura con copia**, limpia sus rastros tras cada sabotaje, y **se cae si su corrida final reporta cero pruebas**. Va en [historico-chat/scripts/2026-08-27/](../../../../../historico-chat/scripts/2026-08-27/), que es donde van los guiones (`S-057`).

---

## 9. Gestión de defectos

| Severidad | Qué la define |
|---|---|
| Crítica | El lector toma un encabezado «por criterio» |
| Alta | Alguna de las 22 pruebas de `A` o `B` hubo que tocarla |
| Media | El título `Veredicto` sigue sin leerse |
| Baja | Redacción |

Se anota en el `resultado_pruebas.md`, se arregla, y **se vuelve a correr el caso completo**.

---

## 10. Cronograma

Un solo tramo. La suite completa al final.

---

## 11. Roles y responsabilidades

Una sola persona cumple los roles. El agente construye y corre; el usuario aprueba.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Casos ejecutados | 4 de 4 |
| Títulos que se leen | 2 de 2 |
| **Títulos parecidos leídos por error** | **0 de 5** |
| Pruebas de `A` y `B` que hubo que tocar | **0** |
| Historias recuperadas | **exactamente 10** |
| **De ellas, con «No cumple»** | **exactamente 3** |
| Sabotajes cazados | Todos |
| Fallas en la suite completa | 0, con conteo distinto de cero |

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Que se pruebe solo el título que faltaba | `CP-002` prueba los cinco que **no** deben leerse |
| Que el arreglo se juzgue por si el número mejora | La meta incluye **tres «No cumple»**: el número tiene que empeorar en esa mitad |
| Que un sabotaje pase en verde | Se corre el escenario y se mira el estado final |
| Que vuelva a haber formas sin mirar | Se enumeraron todas, y el guion que lo hizo quedó guardado para repetirlo |

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
