# Plan de Pruebas — Fase `B-EP-004-HU-021-el-veredicto-se-lee-en-sus-tres-formas`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** el criterio de esta fase, con qué datos y cuándo se da por aprobado. Lo que se pide vive en la [HU-021](../HU-021-la-cuenta-distingue-lo-terminado-de-lo-cumplido.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que el lector del veredicto reconoce las **tres** formas que existen en el repositorio, y **ninguna más**.

### 1.2 Alcance

**Entra:** `veredicto_de` en `validadores/fases.py` y sus pruebas.

**No entra:** uniformar cómo se escribe el veredicto en las 129 fases, ni las 39 que no lo declaran.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las tres formas contadas, y por qué es fase `B` |
| La fase [`A`](../A-EP-004-HU-021-la-cuenta-mira-el-veredicto/funcionalidad_implementada.md) | Lo que dejó, y el defecto que se corrige |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| `veredicto_de` | Que lea las tres formas, y que **no** lea de más |
| `por_veredicto` | Que las siete historias salgan de «no dicen» |
| Las 14 pruebas de la fase `A` | Que sigan pasando **sin tocarlas** |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

**Unitario** sobre árboles de mentira, uno por forma. **De sistema** sobre el árbol real, para el número.

| Tipo | Por qué |
|---|---|
| **De partición por forma** | Es exactamente lo que falló: una forma sin cubrir |
| **De que no pase** | Que ampliar el lector no lo vuelva laxo |
| De no regresión | Las 14 de la fase `A` |
| De sabotaje | Que las pruebas cacen lo que dicen cazar |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-002 | Un lector laxo daría por cumplidas fases que no lo dicen: es peor que el defecto que se corrige |
| Alta | CP-001, CP-003 | Las tres formas, y que lo de antes no se rompa |
| Media | CP-004 | El número |

### 3.3 Alcance de la ejecución automatizada  ·  `02·F5`

`python validadores/pruebas.py` **entera**, con el conteo a la vista.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- Los dos planes, aprobados.
- Las tres formas contadas una por una, que está en el plan §2.

### 4.2 Criterios de salida

- Los cuatro casos ejecutados.
- **Las 14 pruebas de la fase `A`, pasando sin haberlas tocado.**
- El número medido antes y después.
- La suite completa en verde, con conteo distinto de cero.

### 4.3 Criterios de suspensión y reanudación

Se suspende si al medir el número **las «no dicen» no bajan en siete exactamente**: significaría que el lector cambió de comportamiento en algo más, y hay que entenderlo antes de seguir.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| CA-03 — se lee lo que se puede leer | CP-001 | Partición por forma |
| CA-03 — y **solo** lo que se puede leer | CP-002 | Que **no** pase |
| Transversal · no regresión | CP-003 | No regresión |
| El efecto sobre el número | CP-004 | De sistema |

---

## 6. Casos de prueba

### CP-001 — Las tres formas se leen

| Campo | Valor |
|---|---|
| **HU / CA** | HU-021 / CA-03 |
| **Tipo** | Partición por forma |
| **Prioridad** | Alta |
| **Precondiciones** | Un árbol de mentira por forma |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Un resultado con `**Concepto:** Cumple` bajo su encabezado | Se lee `Cumple` |
| 2 | Un resultado con la tabla `\| **Concepto** \| Cumple \|` | Se lee `Cumple` |
| 3 | Un resultado con `**Cumple.**` directo bajo el encabezado | Se lee `Cumple` |
| 4 | Los tres, pero diciendo `No cumple` | Se lee `No cumple` en los tres |

**El paso 3 es el que hoy falla.** Los otros dos están para que arreglarlo no rompa lo que ya servía.

---

### CP-002 — El lector no lee de más

| Campo | Valor |
|---|---|
| **HU / CA** | HU-021 / CA-03 |
| **Tipo** | Que **no** pase |
| **Prioridad** | Crítica |
| **Precondiciones** | Árboles de mentira con la palabra en sitios que no son el veredicto |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Un resultado **sin encabezado de veredicto**, con una tabla de criterios que dice `Cumple` en cada fila | **No se lee**: devuelve nada |
| 2 | Un resultado con encabezado de veredicto y **nada debajo** | **No se lee** |
| 3 | Un resultado donde la palabra aparece en prosa, lejos del encabezado | **No se lee** |
| 4 | Un resultado vacío | **No se lee**, y no revienta |

**Por qué es el caso crítico:** en un resultado la palabra «Cumple» aparece en cada fila de criterio. Un lector que la busque sin exigir su encabezado leería **el primer criterio en vez del veredicto** — y daría por cumplida una fase que no lo está. **Eso es peor que el defecto que esta fase corrige**, porque miente en la dirección optimista.

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
| 1 | Correr las **14 pruebas** de la fase `A`, **sin tocarlas** | Todas en verde |
| 2 | Comprobar que `veredicto_de` y `por_veredicto` conservan su firma | Sin cambios |
| 3 | Correr la suite completa | Verde, con conteo distinto de cero |

---

### CP-004 — El número baja en siete, ni más ni menos

| Campo | Valor |
|---|---|
| **HU / CA** | HU-021 / CA-03 |
| **Tipo** | De sistema |
| **Prioridad** | Media |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Anotar la línea **antes** del cambio | `22 no dicen si cumplen` |
| 2 | Aplicar y volver a correr | Las «no dicen» bajan a **15** |
| 3 | Comprobar adónde fueron las siete | Al reparto que les corresponda por su veredicto |
| 4 | Comprobar que el total y las terminadas **no se movieron** | Los mismos números |

**El paso 4 es el que separa lo que se arregló de lo que se pudo romper.** Esta fase cambia **quién sabe leer**, no cuánto trabajo hay.

---

## 7. Datos y ambientes de prueba

Árboles de mentira en carpeta temporal, creados y borrados por la prueba. **Ninguna prueba usa credenciales** (`00·N6`), y ningún documento real se edita (`08·T4`).

**Qué no reproduce el entorno:** los árboles tienen una fase. **Por eso `CP-004` corre contra el árbol real**, que es el único con las tres formas de verdad.

---

## 8. Herramientas

`unittest` de la biblioteca estándar, y un guion de sabotaje que **se restaura con copia**, limpia sus rastros tras cada sabotaje, y **se cae si su corrida final reporta cero pruebas**.

---

## 9. Gestión de defectos

| Severidad | Qué la define |
|---|---|
| Crítica | El lector lee un veredicto donde no lo hay |
| Alta | Alguna de las 14 pruebas de la fase `A` hubo que tocarla |
| Media | Una de las tres formas sigue sin leerse |
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
| Formas leídas | 3 de 3 |
| **Veredictos leídos donde no los hay** | **0** |
| Pruebas de la fase `A` que hubo que tocar | **0** |
| Bajada de las «no dicen» | **exactamente 7** |
| Sabotajes cazados | Todos |
| Fallas en la suite completa | 0, con conteo distinto de cero |

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Que se pruebe solo la forma que faltaba | `CP-001` prueba las tres, y la que fallaba es una |
| Que ampliar el lector lo vuelva laxo sin que se note | `CP-002`, con cuatro casos de lo que **no** debe leer |
| Que un sabotaje pase en verde | Se corre el escenario y se mira el estado final |

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
