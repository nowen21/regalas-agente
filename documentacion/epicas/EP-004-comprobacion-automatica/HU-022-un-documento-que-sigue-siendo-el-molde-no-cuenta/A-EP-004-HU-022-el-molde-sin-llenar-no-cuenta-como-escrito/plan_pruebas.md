# Plan de Pruebas — Fase `A-EP-004-HU-022-el-molde-sin-llenar-no-cuenta-como-escrito`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** el criterio de esta fase, con qué datos y cuándo se da por aprobado. Lo que se pide vive en la [HU-022](../HU-022-un-documento-que-sigue-siendo-el-molde-no-cuenta.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que un documento que **sigue siendo su plantilla** no cuenta como escrito, y que **ningún documento escrito se señala**.

### 1.2 Alcance

**Entra:** `inventario` en `validadores/fases.py`, la lectura de plantillas, el aviso, y sus pruebas.

**No entra:** llenar los siete documentos, cambiar el andamio, ni los documentos que no son de fase.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | La línea base, el reparto de los 664 y por qué el corte es tres |
| `S-059` | La medida que falló, y por qué |
| [pendiente 88](../../../../../pendientes/hecho/el-molde-sin-llenar-no-cuenta-como-escrito.md) | Las tres salidas, y cuál quedó fuera |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| La lectura de plantillas | Que salga del repositorio, y que sin plantilla no afirme nada |
| La comparación | Que señale el molde y **no** la prosa con comillas |
| `inventario` | Que una fase con un documento sin llenar no cuente completa |
| El aviso | Que diga fase, documento y un ejemplo |
| Las 43 pruebas de `inventario` y `por_veredicto` | Que sigan pasando |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

**Unitario** sobre árboles de mentira con sus propias plantillas. **De sistema** sobre el árbol real, para el número y los siete nombres.

| Tipo | Por qué |
|---|---|
| **De que no pase** | Es el riesgo central: la medida anterior señaló documentos escritos |
| De partición | Cero marcadores del molde, uno o dos, tres o más |
| De borde | Sin plantilla, plantilla vacía, documento vacío |
| De no regresión | Las 43 que dependen de las dos cuentas |
| De sabotaje | Que las pruebas cacen lo que dicen cazar |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-002 | Señalar un documento escrito repite el defecto que se corrige |
| Crítica | CP-000 | Si los árboles de prueba existentes quedan señalados, el plan cambia |
| Alta | CP-001, CP-003 | Que cuente bien, y que diga cuáles |
| Media | CP-004, CP-005 | Las plantillas del repositorio, y que no corrija |

### 3.3 Alcance de la ejecución automatizada  ·  `02·F5`

`python validadores/pruebas.py` **entera**, con el conteo a la vista.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- Los dos planes, aprobados.
- **La línea base medida antes de crear la carpeta de la fase**, que está en el plan §2.0.
- El reparto de los 664 documentos, contado.

### 4.2 Criterios de salida

- Los seis casos ejecutados.
- **Las 43 pruebas de `inventario` y `por_veredicto`, pasando.**
- Los siete documentos nombrados uno por uno.
- La suite completa en verde, con conteo distinto de cero.

### 4.3 Criterios de suspensión y reanudación

Se suspende si:

- **Se señala aunque sea un documento escrito.** Cero es cero: es el defecto que se corrige.
- **Los señalados no son exactamente los siete medidos.** Ni más ni menos.
- **La `T-00` encuentra que un árbol de prueba existente quedaría señalado.** Ahí se para y se replantea, porque significaría que el corte toca datos de mentira legítimos.

**El segundo criterio es el que vale.** «Que señale menos de 38» sería cierto con cualquier arreglo a medias. **Siete exactos**, con nombre, no.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| Previo · los árboles de prueba de hoy | CP-000 | De impacto |
| CA-01 — la fase no cuenta terminada | CP-001 | Partición |
| CA-02 — se compara contra la plantilla | CP-002 | Que **no** pase |
| CA-03 — el aviso dice cuáles | CP-003 | De sistema |
| CA-04 — las plantillas se leen del repositorio | CP-004 | De configuración |
| CA-05 — avisa y no corrige | CP-005 | De efecto |

---

## 6. Casos de prueba

### CP-000 — Los árboles de prueba de hoy no quedan señalados

| Campo | Valor |
|---|---|
| **HU / CA** | Previo a todo |
| **Tipo** | De impacto |
| **Prioridad** | Crítica |
| **Precondiciones** | Ninguna: se mide antes de tocar código |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar en `pruebas.py` los cuerpos con que se arman los documentos de mentira | Se listan |
| 2 | Comprobar cuántos marcadores de plantilla tiene cada uno | **Cero** |
| 3 | Si alguno tuviera tres o más, **parar y replantear** | No debería |

**Por qué va primero:** once pruebas arman árboles con los cinco documentos. Si sus cuerpos falsos se parecen a una plantilla, la comprobación nueva los señalaría y romperían once pruebas **por algo que no es un defecto**. Descubrirlo al final costaría el doble.

---

### CP-001 — Una fase con un documento sin llenar no cuenta terminada

| Campo | Valor |
|---|---|
| **HU / CA** | HU-022 / CA-01 |
| **Tipo** | Partición |
| **Prioridad** | Alta |
| **Precondiciones** | Un árbol con una historia de una fase y sus cinco documentos |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Los cinco escritos | La historia cuenta terminada |
| 2 | Reemplazar uno por su plantilla sin llenar | **Sale de terminadas** |
| 3 | Volver a escribirlo | Vuelve a contar terminada |
| 4 | Con dos fases, una escrita y una con el molde | La historia **no** cuenta terminada |
| 5 | Comprobar que tampoco entra al reparto de veredictos | No aparece en ninguna de las tres cuentas |

**El paso 5 importa:** `por_veredicto` solo mira las terminadas. Si la fase deja de estarlo, su historia tiene que salir del reparto, no quedarse en «no dice si cumple».

---

### CP-002 — No se señala un documento escrito

| Campo | Valor |
|---|---|
| **HU / CA** | HU-022 / CA-02 |
| **Tipo** | Que **no** pase |
| **Prioridad** | Crítica |
| **Precondiciones** | Documentos reales del repositorio |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | El `plan_trabajo.md` de `C-EP-004-HU-021`, que tiene **13 marcadores de prosa** | **No se señala** |
| 2 | El `plan_pruebas.md` de la misma fase, con 12 | **No se señala** |
| 3 | Un documento inventado con veinte `«Cumple»` y `«No cumple»` | **No se señala** |
| 4 | El `plan_pruebas.md` de `B-EP-004-HU-011`, que es la plantilla | **Se señala** |
| 5 | Correr contra los 664 y contar los señalados | **Exactamente 7** |

**Por qué es el caso crítico:** los pasos 1 y 2 son los tres documentos que la medida anterior señaló **el mismo día en que se escribieron**. Si vuelven a salir, la fase no sirve.

---

### CP-003 — El aviso dice cuáles

| Campo | Valor |
|---|---|
| **HU / CA** | HU-022 / CA-03 |
| **Tipo** | De sistema |
| **Prioridad** | Alta |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `validar.py fases` | Siete avisos nuevos |
| 2 | Leer uno | Dice la fase, el documento y **un marcador de ejemplo** |
| 3 | Ir a ese archivo y mirarlo | Es el molde, sin interpretar |
| 4 | Contar los avisos contra los siete medidos | Coinciden, uno a uno |

---

### CP-004 — Las plantillas se leen del repositorio

| Campo | Valor |
|---|---|
| **HU / CA** | HU-022 / CA-04 |
| **Tipo** | De configuración |
| **Prioridad** | Media |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar en `validadores/` una lista de marcadores escrita a mano | **No hay** |
| 2 | En un árbol de prueba, agregar un marcador nuevo a una plantilla | — |
| 3 | Comprobar un documento que lo tenga tres veces | **Se señala** |
| 4 | Quitar la plantilla del árbol | **No se señala nada** de ese tipo, y no revienta |

**El paso 4 es `04·R4`:** sin plantilla no hay con qué comparar, así que no se afirma nada.

---

### CP-005 — Avisa y no corrige

| Campo | Valor |
|---|---|
| **HU / CA** | HU-022 / CA-05 |
| **Tipo** | De efecto |
| **Prioridad** | Media |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Anotar el contenido y la fecha de un documento sin llenar | — |
| 2 | Correr la comprobación | — |
| 3 | Comparar | Idéntico, y la fecha sin cambiar |

---

## 7. Datos y ambientes de prueba

Árboles de mentira en carpeta temporal, **cada uno con sus propias plantillas**, para poder probar `CA-04` sin tocar las de verdad. **Ninguna prueba usa credenciales** (`00·N6`), y ningún documento real se edita (`08·T4`).

**Qué no reproduce el entorno:** un árbol de mentira tiene una o dos fases. **Por eso `CP-002` paso 5 y `CP-003` corren contra el árbol real**, que es el único con 664 documentos y prosa de verdad.

---

## 8. Herramientas

`unittest` de la biblioteca estándar, y un guion de sabotaje que **se restaura con copia**, limpia sus rastros tras cada sabotaje, y **se cae si su corrida final no trae la línea `OK` sola**. Va en [historico-chat/scripts/2026-08-27/](../../../../../historico-chat/scripts/2026-08-27/).

> **La guardia se corrigió hoy** (`DEF-02` de la fase `C` de la `HU-021`): buscaba «OK» en un texto que trae «OK: sin incumplimientos.», y dio por buena una corrida con tres fallas.

---

## 9. Gestión de defectos

| Severidad | Qué la define |
|---|---|
| Crítica | Se señala un documento escrito |
| Alta | Los señalados no son los siete medidos |
| Media | El aviso no dice cuál documento es |
| Baja | Redacción |

Se anota en el `resultado_pruebas.md`, se arregla, y **se vuelve a correr el caso completo**.

---

## 10. Cronograma

Un solo tramo, con la `T-00` antes de tocar código. La suite completa al final.

---

## 11. Roles y responsabilidades

Una sola persona cumple los roles. El agente construye y corre; el usuario aprueba.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Casos ejecutados | 6 de 6 |
| **Documentos escritos señalados** | **0** |
| **Documentos señalados** | **exactamente 7, con nombre** |
| Pruebas de `inventario` y `por_veredicto` que hubo que tocar | 0 |
| Sabotajes cazados | Todos |
| Fallas en la suite completa | 0, con conteo distinto de cero |

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Que se pruebe solo con moldes y no con prosa | `CP-002` usa **los tres documentos reales que la medida anterior señaló mal** |
| Que el umbral se ajuste hasta que dé siete | El corte se eligió mirando el reparto **antes** de escribir código: no hay ningún documento entre 3 y 15 marcadores |
| Que un sabotaje pase en verde | Se corre el escenario y se mira el estado final, como en la fase `C` |
| Que abrir esta fase mueva el número | La línea base quedó anotada antes de crear la carpeta |

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
