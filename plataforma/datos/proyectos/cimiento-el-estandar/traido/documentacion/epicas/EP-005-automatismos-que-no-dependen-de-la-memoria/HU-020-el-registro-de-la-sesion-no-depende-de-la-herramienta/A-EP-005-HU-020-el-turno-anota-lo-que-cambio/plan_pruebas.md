# Plan de Pruebas — Fase `A-EP-005-HU-020-el-turno-anota-lo-que-cambio`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** el criterio de esta fase, con qué datos y cuándo se da por aprobado. Lo que se pide vive en la [HU-020](../HU-020-el-registro-de-la-sesion-no-depende-de-la-herramienta.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que el registro anota **lo que cambió en el turno**, y **solo eso**.

### 1.2 Alcance

**Entra:** qué se considera cambiado en la ventana, cómo se anota, el enganche, y el efecto sobre la comprobación que ya existe.

**No entra:** tocar `validar_preparados`, ni identificar quién escribió cada archivo.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Los doce commits medidos, y por qué no se afina la comprobación |
| `S-071` | Un archivo que nadie registró parece de nadie |
| `S-072` | El hueco por el que entró lo ajeno es el mismo por el que pasa lo propio |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| «Qué cambió en la ventana» | Que incluya lo escrito con guiones, y **excluya lo de antes** |
| El registro | Que no duplique lo que ya estaba |
| El enganche | Que **nunca** rompa el turno |
| `validar_preparados` | Que **empiece a ver** la colisión, y que **no pase a hablar siempre** |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

**Con repositorios de git de verdad y fechas controladas.** Sin fechas controladas no se puede distinguir «dentro del turno» de «antes», que es la mitad del criterio.

| Tipo | Por qué |
|---|---|
| **De que no pase** | Reclamar lo viejo convierte el silencio inútil en ruido inútil |
| **De efecto sobre lo existente** | El arreglo se mide por lo que le hace a la comprobación, no por sí mismo |
| De partición | Escrito con herramienta, con guion, y no escrito |
| De borde | Ignorados, borrados, sin git, sin registro previo |
| **De conexión** | Que esté colgado, no solo escrito |
| De sabotaje | Que las pruebas cacen lo que dicen cazar |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-002 | Reclamar lo viejo hace que la comprobación hable siempre |
| Crítica | CP-006 | **Si con el registro nuevo avisa en la mayoría de los commits, la fase no sirve** |
| Alta | CP-001, CP-003 | Que anote lo del guion, y que la colisión se vea |
| Media | CP-004, CP-005, CP-007 | No duplicar, no romper, y estar colgado |

### 3.3 Alcance de la ejecución automatizada  ·  `02·F5`

`python validadores/pruebas.py` **entera**, con el conteo a la vista.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- Los dos planes, aprobados.
- **La `T-00` corrida:** saber si alguna prueba fija el contenido del registro.
- **La `T-01` resuelta:** qué entrega git para ignorados y borrados.
- La línea base y los doce commits medidos, en el plan §2.

### 4.2 Criterios de salida

- Los siete casos ejecutados.
- **El número de la `T-06`:** cuántos commits avisarían con el registro nuevo.
- El enganche probado **escribiendo con un guion**.
- La suite completa en verde, con conteo distinto de cero.

### 4.3 Criterios de suspensión y reanudación

Se suspende si:

- **Se anota un archivo modificado antes del turno.** Cero es cero.
- **Con el registro nuevo, `validar_preparados` avisaría en más de la mitad de los commits recientes.** Ahí el arreglo cambió un silencio por un ruido, y hay que replantearlo — no seguir de largo.
- **Un turno se rompe** por el enganche.

**El segundo es el que decide si esta fase tiene sentido**, y por eso se mide antes de cerrarla. Está escrito para que la fase pueda fracasar.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| Previo · las pruebas del registro | CP-000 | De impacto |
| CA-01 — lo escrito con guion queda registrado | CP-001 | De partición |
| CA-02 — no se reclama lo de antes | CP-002 | Que **no** pase |
| CA-03 — dos sesiones producen colisión | CP-003 | De sistema |
| CA-04 — no se duplica lo que ya estaba | CP-004 | De no regresión |
| CA-05 — un fallo no rompe el turno | CP-005 | De no destruir |
| Transversal — cuánto hablaría | CP-006 | **De ruido** |
| CA-01 · conexión | CP-007 | De sistema |

---

## 6. Casos de prueba

### CP-000 — Las pruebas del registro admiten más contenido

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar las pruebas que miran `historico-chat/.tocado/` | Se listan |
| 2 | Ver si alguna fija **exactamente** qué contiene el registro | **Ninguna debería** |
| 3 | Si alguna lo hace, **parar y decidir** | — |

---

### CP-001 — Lo escrito con un guion queda registrado

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir un archivo **sin las herramientas de escritura** | — |
| 2 | Correr el enganche de fin de turno | — |
| 3 | Leer el registro de la sesión | **El archivo está** |
| 4 | Un archivo nuevo, sin seguimiento todavía | También está |

**El paso 4 importa:** los dos moldes que causaron el daño eran archivos nuevos.

---

### CP-002 — No se reclama lo que no se tocó en el turno

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Un archivo sucio con fecha **anterior** a la ventana | **No entra** al registro |
| 2 | Un archivo sucio **modificado durante** la ventana | Entra |
| 3 | Con el registro vacío —primera corrida— | **No se reclama el árbol entero** |
| 4 | Contar cuántos entran sobre el árbol real | Un puñado, no decenas |

**Es el crítico.** Sin él, la primera sesión del día se atribuye todo lo que estuviera sucio, y la comprobación pasa de callar siempre a hablar siempre.

**El paso 3 es el que se cuela:** en la primera corrida no hay fecha anterior contra la cual comparar, y ahí es donde un programa ingenuo se lo lleva todo.

---

### CP-003 — Dos sesiones que tocan lo mismo producen colisión

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Dos registros de sesión distintos con el mismo archivo | — |
| 2 | Preparar ese archivo para el commit | — |
| 3 | Correr `validar_preparados` | **Avisa**, y nombra el archivo |
| 4 | **Reproducir el caso real:** una sesión escribe dos archivos, otra commitea con ellos dentro | Avisa |

**El paso 4 es la prueba de que esta fase sirve para lo que se hizo.**

---

### CP-004 — No se duplica lo que ya estaba

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Anotar un archivo con la función de siempre | — |
| 2 | Correr el enganche de fin de turno con ese archivo cambiado | — |
| 3 | Leer el registro | El archivo, **una sola vez** |
| 4 | Comprobar que no se perdió nada de lo anterior | Todo sigue |

---

### CP-005 — Un fallo del enganche no rompe el turno

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correrlo **sin git en el camino** | Termina en 0, y calla |
| 2 | Entrada sin identificador de sesión | Termina en 0 |
| 3 | Entrada que no es JSON | Termina en 0 |
| 4 | Una carpeta que no es un repositorio | Termina en 0 |

**El paso 1 es un caso real**, no una hipótesis: una máquina sin git instalado.

---

### CP-006 — Cuánto hablaría la comprobación con el registro nuevo

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Simular el registro nuevo sobre los últimos doce commits | — |
| 2 | Contar en cuántos avisaría `validar_preparados` | **Menos de la mitad** |
| 3 | Comparar con el diseño descartado, que avisaba en 7 de 12 | Mejor, y dicho con el número |

**Este caso puede tumbar la fase**, y está escrito para eso. Un arreglo que cambia un silencio inútil por un ruido inútil **es peor que no hacerlo**: el ruido apaga también lo que servía.

---

### CP-007 — El enganche está colgado

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr el instalador sobre un proyecto de prueba | El enganche aparece en la configuración |
| 2 | Una prueba que lo busque **en la lista del instalador** | Está |

**Es la lección de `EP-002·HU-004`:** construido, probado, en verde, y nadie lo llamaba.

---

## 7. Datos y ambientes de prueba

**Repositorios de git de verdad**, creados y borrados por la prueba, con `user.name` y `user.email` **locales** (`00·N1`), y **fechas de modificación puestas a mano** para poder distinguir dentro y fuera de la ventana.

**Ninguna prueba usa credenciales** (`00·N6`), y **ninguna escribe en el registro real** del repositorio.

---

## 8. Herramientas

`unittest`, `git` de verdad, y un guion de sabotaje que **se restaura con copia**, **restaura en `try/finally`**, limpia sus rastros, **no se corre por una tubería**, y cuya guardia acepta `OK` y `OK (…)` pero no `OK:` (`S-060`, `S-068`).

---

## 9. Gestión de defectos

| Severidad | Qué la define |
|---|---|
| Crítica | Se reclama un archivo de antes del turno, o se rompe un turno |
| Alta | La comprobación pasa a avisar en la mayoría de los commits |
| Media | Se duplica una entrada del registro |
| Baja | Redacción |

Se anota en el `resultado_pruebas.md`, se arregla, y **se vuelve a correr el caso completo**.

---

## 10. Cronograma

Un solo tramo, con la `T-00` y la `T-01` antes de escribir código, y la `T-06` **antes de dar la fase por buena**.

---

## 11. Roles y responsabilidades

Una sola persona cumple los roles. El agente construye y corre; el usuario aprueba.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Casos ejecutados | 7 de 7 |
| **Archivos de antes del turno que se reclaman** | **0** |
| **Commits en que avisaría, de los últimos doce** | **menos de 6**, y dicho con el número |
| Turnos rotos por el enganche | 0 de 4 |
| Entradas duplicadas en el registro | 0 |
| Sabotajes cazados | Todos |
| Fallas en la suite completa | 0, con conteo distinto de cero |

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Probar la función y no el enganche | `CP-007` y `CP-001` usan repositorios y guiones de verdad |
| Probar que anota y no que **no** anota de más | `CP-002`, que es el crítico |
| Dar la fase por buena sin medir el ruido | `CP-006`, con su número y su umbral escrito |
| Que un sabotaje pase en verde | Se corre el escenario y se mira el estado final — **pasó cinco veces en dos días** |

---

## 14. Control de versiones

| Versión | Fecha | Cambio |
|---|---|---|
| 1 | 2026-08-28 | Redacción inicial, junto con el plan de trabajo |

---

## 15. Aprobación

| Rol | Estado |
|---|---|
| Usuario | Pendiente. **No se toca nada hasta que este plan y el de trabajo estén aprobados** (`02·F4`) |
