# Resultado de Pruebas — Fase `A-EP-004-HU-023-la-fase-declara-que-veredicto-deja-atras`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, caso por caso, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-004-HU-023-la-fase-declara-que-veredicto-deja-atras` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-27 |
| **Ciclo** | 2. **El primero dejó tres sabotajes en verde** |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** con cero declaraciones la línea quedó **idéntica a la base**, y al declarar en los dos cierres que sí verificaron se movieron **exactamente dos**. Las otras catorce siguen contando, incluidas las seis que tienen fase posterior y **no resolvieron su rojo**.

| Métrica | Meta | Real |
|---|---|---|
| Casos ejecutados | 7 de 7 | 7 de 7 |
| **Historias que se mueven con cero declaraciones** | 0 | **0** |
| **Historias que se mueven al declarar** | exactamente 2, con nombre | **2, nombradas** |
| Pruebas de `por_veredicto` que hubo que tocar | 0 | **0** |
| Sabotajes cazados | Todos | **5 de 5**, tras reescribir tres pruebas |
| Fallas en la suite completa | 0 | 0, sobre **484 pruebas** |

---

## 3. Resultado por caso

### CP-000 — El molde admite un campo más

**Corrido antes de tocar código.**

| Qué se miró | Resultado |
|---|---|
| Pruebas que exigen la lista de campos del molde `11` | **Ninguna** |
| Cómo decide el validador de completitud | Compara **encabezados** y **líneas copiadas tal cual** |
| Efecto de una fila de tabla opcional | **Ninguno**: no es encabezado, y las 130 fases que no la tienen no la copian |

### CP-001 — Declarar cierra el rojo

| Paso | Resultado |
|---|---|
| Roja + verde, **sin el campo** | La historia **no cumple** |
| Con el campo nombrando a la roja | La historia **cumple** |
| Quitando el campo otra vez | Vuelve a **no cumplir** |

**El tercero importa:** comprueba que el cambio lo produce el campo, y no otra cosa que se movió de paso.

### CP-002 — Un rojo no cierra otro rojo

| Qué se le puso delante | Conjunto de reemplazos | Cuenta |
|---|---|---|
| Roja + roja que declara | **Vacío** | No cumple |
| Roja + **sin veredicto** que declara | **Vacío** | No dice |

**Se comprueba sobre el conjunto, no sobre la cuenta**, y el §4.2 dice por qué.

### CP-003 — El reemplazo no se deduce del orden

| Qué se le puso delante | Qué hizo |
|---|---|
| Roja + verde, sin campo | **No cumple** |
| Roja + verde + verde, sin campo | **No cumple** |
| **El árbol real:** las historias con rojo que no declaran nada | **Todas siguen contadas** |

**El tercero es el que decide.** Se comprueba contando las historias con un rojo cuya lista de reemplazos está vacía, y exigiendo que ese número **sea igual** al de «no cumplen». Si alguna hubiera salido sin declararlo, los números no cuadrarían.

### CP-004 — Un nombre que no resuelve avisa, y no reemplaza

| Qué se declaró | Conjunto | Aviso |
|---|---|---|
| Una fase **inventada** | Vacío | Sí, **con el nombre escrito** |
| Una fase de **otra historia** | Vacío | Sí |
| **Sí misma**, estando en verde | Vacío | Sí, «se nombra a sí misma» |
| El campo **vacío** | Vacío | No avisa, no revienta |
| Quien declara **está en rojo** | Vacío | Sí, «un rojo no cierra otro rojo» |

### CP-005 — El veredicto reemplazado no se borra

El documento de la fase reemplazada queda **idéntico**, y `veredicto_de` **sigue leyendo «No cumple»** en ella. La cuenta lo deja atrás; el dato no desaparece.

### CP-006 — El número, antes y después

| Momento | La línea |
|---|---|
| Línea base | `66 cumplen, 16 no cumplen, 5 no dicen` |
| **Con el código puesto y cero declaraciones** | **`66 cumplen, 16 no cumplen, 5 no dicen`** |
| Tras declarar en los dos que verificaron | `68 cumplen, 14 no cumplen, 5 no dicen` |

**Las dos que se movieron:** `EP-003·HU-002` y `EP-005·HU-001`.

**Y al cerrar esta misma fase la línea quedó en `69 cumplen, 14 no cumplen, 5 no dicen`:** la `HU-023` pasó a terminada y cumple. Es el mismo efecto de siempre, ahora previsto.

**El segundo renglón es el que hace creíble el tercero.** Si con cero declaraciones la línea hubiera cambiado en un solo número, el reemplazo se estaría deduciendo de algo, y el plan decía parar ahí.

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Los sabotajes

Cinco, restaurados **con copia** y en `try/finally`.

| # | Qué se rompió | Ciclo 1 | Ciclo 2 |
|---|---|---|---|
| 1 | El reemplazo se deduce del orden | Cazado (5) | Cazado (6) |
| 2 | Un rojo puede cerrar otro rojo | **Verde** | **Cazado (2)** |
| 3 | Una fase se puede cerrar a sí misma | **Verde** | **Cazado (1)** |
| 4 | Se acepta el nombre de otra historia | **Verde** | **Cazado (2)** |
| 5 | El aviso no dice qué nombre se escribió | Cazado (2) | Cazado |

### 4.2 Los tres que pasaron en verde, y la causa única

**Las tres pruebas miraban la cuenta, y las guardias no actúan ahí.** Actúan sobre el **conjunto de reemplazos**. Se comprobó en vez de deducirlo:

| Guardia | Sobre la cuenta | Sobre el conjunto |
|---|---|---|
| Quien declara tiene que cumplir | **El resultado coincide**: el rojo de quien declara ya ensucia la cuenta | Ahí sí cambia |
| No nombrarse a sí misma | Con la fase en rojo, la guardia anterior ya la bloquea | Ahí sí |
| La fase nombrada es de esta historia | Un nombre que no está en la lista **no filtra nada** | Ahí sí |

**Así que las tres pruebas no podían fallar.** Es la tercera forma de `S-062` — *una prueba que no toca la rama que dice tocar* — **y ocurrió otra vez el mismo día, sabiéndolo**.

Reescritas sobre `veredictos_reemplazados`, y con los dos avisos que faltaban. **De 15 pruebas a 18.**

**Un matiz que se aprendió acá:** la guardia de «no nombrarse a sí misma» **solo importa en verde**. La prueba la ponía en rojo, donde la bloquea la otra guardia — pasaba sin tocar lo que decía probar.

### 4.3 Rastros

**Uno, declarado.** La copia de restauración del guion vive en la carpeta temporal del sistema, **y el enganche de la `HU-018` la va a avisar** — que es para lo que se construyó.

### 4.4 Ninguna prueba usa credenciales

Ni reales ni inventadas (`00·N6`).

---

## 5. Defectos encontrados

| # | Qué | Severidad | Estado |
|---|---|---|---|
| DEF-01 | Tres pruebas de las guardias miraban la cuenta, donde el resultado coincide: **no podían fallar** | **Crítica** — tres sabotajes en verde | **Corregido.** Reescritas sobre el conjunto |
| DEF-02 | La guardia de «no nombrarse a sí misma» se probaba en rojo, donde otra guardia la tapa | Alta | **Corregido.** Se prueba en verde |
| DEF-03 | Faltaban los avisos de «se nombra a sí misma» y «quien declara está en rojo» | Media | **Corregido** |
| DEF-04 | La guardia del guion de sabotaje **dio falsa alarma con la corrida limpia** | Alta — **de la herramienta que juzga** | **Corregido** en los tres guiones del día |

**Ninguno en el código.** Los cuatro son de las pruebas y del guion que las corre — y el `DEF-01` es la segunda vez en la jornada que el mismo defecto de prueba aparece **después** de haberlo escrito como señal.

**El `DEF-04` cierra la tercera falla del día en la herramienta que juzga**, y las tres son de la misma familia: un guion que dijo «suite OK» sin correr nada, otro que leyó «OK: sin incumplimientos» como aprobación, y este — que pedía la línea `OK` **sola** y no reconocía `OK (expected failures=4)`, que es lo que `unittest` escribe cuando la suite trae fallos esperados. **Gritaba con la corrida limpia.**

**Y el arreglo tuvo que evitar volver al defecto anterior:** aceptar cualquier línea que empiece por `OK` habría vuelto a tragarse `OK: sin incumplimientos.`. Se acepta `OK` exacto o `OK (`.

---

## 6. Evidencias

- `veredictos_reemplazados` y `reemplazos_que_no_resuelven` en `validadores/fases.py`
- **18 pruebas**, de las cuales **once comprueban que NO cierre**
- La `T-06`: con cero declaraciones, los cinco números iguales a la base
- El guion de sabotaje, en [historico-chat/scripts/2026-08-27/](../../../../../historico-chat/scripts/2026-08-27/)
