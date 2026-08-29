# Plan de Pruebas — Fase `A-EP-005-HU-021-el-corredor-que-si-las-corre`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** el criterio de esta fase, con qué datos y cuándo se da por aprobado. Lo que se pide vive en la [HU-021](../HU-021-las-pruebas-que-existen-se-corren.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que las 650 pruebas **se corren**, que **cero no pasa por verde**, y que la corrida completa **no depende de que alguien se acuerde**.

### 1.2 Alcance

**Entra:** el corredor, su conteo, el subconjunto, la orden documentada, de dónde cuelga, y la declaración de los seis rojos.

**No entra:** arreglar los seis rojos, ni tocar `02·F5`, ni fundir las dos suites.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | La línea base 61/6 y las dos dudas que se miden |
| `S-075` | Tres registros tenían comprobador y estuvieron rotos días igual |
| [pendiente 90](../../../../../pendientes/90-las-pruebas-de-validadores-tests-no-las-corre-nada.md) | Los cuatro comandos que podrían correrlas y no lo hacen |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| El corredor | Que corra las 650 y **diga cuántas** |
| El conteo | Que **cero sea rojo**, no verde |
| El subconjunto | Que se pueda pedir menos, para que `02·F5` se cumpla |
| La orden documentada | Que la escrita y la que funciona sean **la misma** |
| Lo colgado | Que **exista donde se cuelga**, y que no sea un peaje |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

**Con carpetas de verdad**, creadas y borradas por la prueba.

| Tipo | Por qué |
|---|---|
| **De que no pase** | Cero pruebas leído como verde es el defecto que se arregla |
| **De partición** | Carpeta llena, vacía, con un archivo, con un nombre que no existe |
| **De ruido** | Lo colgado se mide antes de colgarlo |
| **De conexión** | Que esté colgado, no solo escrito |
| **De no regresión** | Que las 515 de `pruebas.py` sigan igual, y que el `__init__.py` no rompa los 61 |
| De sabotaje | Que las pruebas cacen lo que dicen cazar |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-002 | **Cero pruebas en verde es el defecto que originó todo** |
| Crítica | CP-001 | **Si el `__init__.py` rompe alguno de los 61, el diseño se cae** |
| Crítica | CP-006 | **Si lo colgado cuesta más de lo que evita, se apaga y quedamos peor** |
| Alta | CP-003, CP-004 | Que corra las 650 y que la orden documentada sea la que funciona |
| Media | CP-005, CP-007, CP-008 | Subconjunto, conexión, y los seis declarados |

### 3.3 Alcance de la ejecución automatizada  ·  `02·F5`

`python validadores/pruebas.py` **entera**, con el conteo a la vista. **Y la carpeta nueva, entera**, que es lo que esta fase viene a hacer posible — es la primera fase que puede correr las dos.

**Las 650 no entran dentro de `pruebas.py`.** Meterlas ahí la volvería de seis minutos y empujaría contra `02·F5`.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- Los dos planes, aprobados.
- **La `T-00` corrida:** el 61/6 de hoy, escrito archivo por archivo.
- **La `T-01` resuelta:** si el `__init__.py` rompe algo.

### 4.2 Criterios de salida

- Los ocho casos ejecutados.
- **El número de la `T-04`:** cuánto costaría lo colgado.
- La orden documentada probada **desde cero**, no desde la sesión que la escribió.
- Las dos suites en verde, con conteo distinto de cero.

### 4.3 Criterios de suspensión y reanudación

Se suspende si:

- **El `__init__.py` pone en rojo alguno de los 61 que hoy están en verde.** Uno es uno.
- **El corredor devuelve verde con cero pruebas.** Es el defecto original, reconstruido.
- **Lo colgado agrega más de un minuto a algo que se hace en cada commit.** Ahí el arreglo se apaga solo, y hay que colgarlo en otro sitio.

**El tercero es el que decide si el enganche tiene sentido**, y por eso se mide antes de colgarlo. Está escrito para que la fase pueda fracasar.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| Previo · la línea base | CP-000 | De impacto |
| Previo · el `__init__.py` no rompe nada | CP-001 | De no regresión |
| CA-02 — cero pruebas es rojo | CP-002 | Que **no** pase |
| CA-01 — las 650 corren y se cuentan | CP-003 | De partición |
| CA-01 — la orden documentada es la que funciona | CP-004 | De sistema |
| CA-03 — subconjunto | CP-005 | De partición |
| CA-04 — cuánto cuesta lo colgado | CP-006 | **De ruido** |
| CA-04 — está colgado | CP-007 | De sistema |
| CA-05 — los seis rojos declarados | CP-008 | De registro |

---

## 6. Casos de prueba

### CP-000 — La línea base, archivo por archivo

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr los 67 uno por uno y guardar el resultado de cada uno | Queda la lista |
| 2 | Contar verdes y rojos | **61 y 6** |
| 3 | Guardar la salida como evidencia | Queda |

**Sin esto, la `T-01` no se puede juzgar:** un rojo después no se distingue de un rojo de antes.

---

### CP-001 — El `__init__.py` no rompe ninguno

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Crear el `__init__.py` vacío | — |
| 2 | Correr los 67 uno por uno otra vez | — |
| 3 | Comparar contra `CP-000` | **Los mismos 61 y los mismos 6** |
| 4 | Si aparece un rojo nuevo, **parar y replantear** | — |

**Es crítico y va antes de escribir el corredor.** Un `__init__.py` cambia cómo un módulo resuelve sus importaciones, y estos 67 hoy se corren sueltos.

---

### CP-002 — Cero pruebas no pasa por verde   ·   **el crítico**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Apuntar el corredor a una carpeta **vacía** | **Termina en rojo**, y dice que no encontró ninguna |
| 2 | Apuntarlo a una carpeta **que no existe** | Rojo, con mensaje claro |
| 3 | Apuntarlo a una carpeta con archivos **sin ninguna prueba dentro** | Rojo |
| 4 | Comprobar que `unittest discover` **solo**, en el mismo caso, da 0 | Da 0 — **y por eso hace falta el corredor** |

**Es el defecto original, reconstruido.** Durante semanas hubo una orden documentada que no corría nada, y su silencio se leyó como que estaba todo bien. El paso 4 no prueba el corredor: **prueba que el corredor hace falta**.

---

### CP-003 — Las 650 corren y se cuentan

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr el corredor sobre la carpeta real | Corre |
| 2 | Leer el conteo | **650**, o el número que haya ese día, **nunca 0** |
| 3 | Leer las fallas | **6 archivos**, los de `CP-000` |
| 4 | Medir lo que tarda | Se anota el número |

---

### CP-004 — La orden documentada es la que funciona

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar en el repositorio qué orden se documenta para correr esta carpeta | Se encuentra |
| 2 | Correrla **tal cual está escrita**, desde la raíz | **Corre** |
| 3 | Comprobar que el `README` de `validadores/` la nombra | La nombra |

**El paso 2 es el que se ganó su fila:** hoy la orden documentada existe desde la primera prueba del repositorio y **se cae antes de correr nada**. Que la documentación mienta es la mitad del defecto.

---

### CP-005 — Se puede pedir un subconjunto

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir **un** archivo por su nombre | Corre solo ese, y el conteo lo dice |
| 2 | Pedir **dos** | Corren los dos |
| 3 | Pedir un nombre **que no existe** | **Rojo**, no verde silencioso |
| 4 | Comprobar que el conteo es menor que el total | Lo es |

**El paso 3 importa tanto como el 1:** pedir un archivo mal escrito y recibir verde es `CP-002` otra vez, por la puerta de al lado.

---

### CP-006 — Cuánto cuesta lo colgado   ·   **el que puede tumbar el enganche**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Medir lo que tardan las 650 | Se anota |
| 2 | Contar cuántas veces se dispararía en los últimos doce commits | Se anota |
| 3 | Multiplicar: cuánto tiempo habría costado | **Menos de un minuto por commit**, o se cuelga en otro sitio |
| 4 | Si no pasa, elegir otro sitio **y decirlo con el número** | — |

**Este caso puede tumbar el enganche**, y está escrito para eso. Tres minutos por commit **se desinstalan en una tarde**, y entonces quedamos peor: con un control que figura como puesto.

---

### CP-007 — Está colgado

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar el corredor **donde se cuelga** —la lista del instalador o el enganche— | Está |
| 2 | Una prueba que lo busque ahí, no en el disco | Está |

**Es la lección de `EP-002·HU-004`:** construido, probado, en verde, y nadie lo llamaba.

---

### CP-008 — Los seis rojos quedan declarados

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer el `funcionalidad_implementada.md` de la fase | Los seis, por su nombre |
| 2 | Comprobar que cada uno dice **qué falla y adónde va** | Lo dice |
| 3 | Comprobar que ninguno queda como «se verá» | Ninguno |

---

## 7. Datos y ambientes de prueba

**Carpetas temporales**, creadas y borradas por la prueba, para vacío, inexistente y subconjunto. **Ninguna prueba usa credenciales** (`00·N6`). **Las 650 no se corren dentro de `pruebas.py`**: eso la volvería de seis minutos y empujaría contra `02·F5`.

---

## 8. Herramientas

`unittest`, y un guion de sabotaje que **se restaura con copia**, **restaura en `try/finally`**, limpia sus rastros, **no se corre por una tubería**, y cuya guardia acepta `OK` y `OK (…)` pero no `OK:` (`S-060`, `S-068`).

---

## 9. Gestión de defectos

| Severidad | Qué la define |
|---|---|
| Crítica | Cero pruebas da verde, o el `__init__.py` rompe uno de los 61 |
| Alta | Lo colgado cuesta más de un minuto por commit |
| Media | El subconjunto acepta un nombre inexistente sin quejarse |
| Baja | Redacción |

Se anota en el `resultado_pruebas.md`, se arregla, y **se vuelve a correr el caso completo**.

---

## 10. Cronograma

Un solo tramo, con la `T-00` y la `T-01` antes de escribir código, y la `T-04` **antes de colgar nada**.

---

## 11. Roles y responsabilidades

Una sola persona cumple los roles. El agente construye y corre; el usuario aprueba.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Casos ejecutados | 8 de 8 |
| **Archivos que el `__init__.py` pone en rojo** | **0** |
| **Casos donde cero pruebas da verde** | **0** |
| **Lo que agrega lo colgado, por commit** | **menos de 1 min**, y dicho con el número |
| Rojos declarados de los 6 | 6 |
| Sabotajes cazados | Todos |
| Fallas en `pruebas.py` | 0, con conteo distinto de cero |
| Fallas nuevas en la carpeta de 650 | 0 sobre la línea base |

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Probar el corredor y no la orden documentada | `CP-004` la corre tal como está escrita |
| Probar que cuenta y no que **no** miente contando cero | `CP-002`, que es el crítico |
| Colgar sin medir el costo | `CP-006`, con su umbral escrito |
| Que un sabotaje pase en verde | Se corre el escenario y se mira el estado final — **pasó cinco veces en dos días** |
| **Dar por bueno un rojo de antes como si fuera nuevo, o al revés** | `CP-000` deja la línea base escrita antes de tocar nada |

---

## 14. Control de versiones

| Versión | Fecha | Cambio |
|---|---|---|
| 1 | 2026-08-28 | Redacción inicial, junto con el plan de trabajo |

---

## 15. Aprobación

| Rol | Estado |
|---|---|
| Usuario | **Aprobado** el 2026-08-28 |
