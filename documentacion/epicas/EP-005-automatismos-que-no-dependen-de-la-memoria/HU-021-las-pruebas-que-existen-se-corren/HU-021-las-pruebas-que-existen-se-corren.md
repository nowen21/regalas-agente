# HU-021 — Que las pruebas que ya existen se corran

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-021 |
| **Épica / Feature** | [EP-005 Automatismos que no dependen de la memoria](../epica.md) |
| **Módulo / Componente** | Pruebas |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien confía en que lo comprobado sigue comprobado
- **Quiero** que las pruebas escritas se puedan correr con una orden, y que alguien las corra
- **Para** que «tiene pruebas» signifique algo

---

## 3. Contexto y descripción

**`validadores/tests/` tiene 67 archivos y 650 pruebas, y ningún comando del repositorio las ejecuta.**

| Quién podría correrlas | Qué hace en realidad |
|---|---|
| `python validadores/pruebas.py` | Corre sus **515 propias**. No descubre la carpeta |
| `python -m unittest discover -s validadores/tests` | **Se cae antes de correr nada** — falta el `__init__.py`. Es la orden que el registro de cambios documenta desde la primera prueba del repositorio |
| `validar.py suite` | Busca `pytest`, `phpunit` o `npm test`. Ninguno aplica acá |
| El enganche de `pre-commit` | Corre comprobadores, no pruebas |

**Hay dos suites y el repositorio conoce una.** Cada fase cierra diciendo «la suite completa, en verde»: es cierto de las 515, y de las otras 650 nadie afirmó nada.

### Lo que aparece al correrlas

**61 archivos en verde, 6 en rojo.** Uno de ellos cuenta **98 enlaces entre carpetas mal escritos** donde su criterio exige cero; otro dice que `hook_estacion.py` se quedó del lado equivocado de la frontera del adaptador. Varias son de trabajo de estos días.

**El daño ya se pagó una vez.** La lista de exentos del detector de secretos quedó vieja el 2026-08-22 y `validar.py todo` estuvo **seis días en rojo** diciendo «posible secreto en el código» — el mismo mensaje que daría una fuga real. La prueba que lo cazaba estaba escrita hacía diez días. Es `S-075`.

### Por qué no basta con crear el archivo que falta

Poner el `__init__.py` hace que la orden cargue. **No hace que alguien la corra**, y eso es lo que faltó durante semanas. Un arreglo que deja la orden disponible y nada colgado de ella **vuelve al mismo sitio la próxima semana ocupada** — es la lección de `EP-002·HU-004`, construido, probado, en verde y sin que nadie lo llamara.

### Y por qué no se meten dentro de `pruebas.py`

`02·F5` dice que una fase corre **las suites que toca**, no la suite completa del proyecto, y por buenas razones: cientos de pruebas, minutos de espera y rojos que ya existían antes. Fundir las dos suites empujaría exactamente a lo que esa regla prohíbe.

**Lo que falta no es correr más en cada fase.** Es que la orden exista, que se pueda pedir un subconjunto, y que la corrida completa esté colgada de algo que no sea la memoria.

### 3.1 Reglas de negocio

| ID | Regla | De dónde baja |
|---|---|---|
| RN-01 | Las pruebas de `validadores/tests/` se corren **con una sola orden**, y es la que está documentada | Hoy la documentada se cae |
| RN-02 | La corrida **dice cuántas corrió**. Cero pruebas no es verde | `08·T5`; y es el defecto que dejó la carpeta invisible |
| RN-03 | Se puede pedir **un subconjunto**, para que `02·F5` se pueda cumplir sobre esta carpeta | Sin esto, la única opción es todo o nada |
| RN-04 | La corrida completa **queda colgada de algo**, no de que alguien se acuerde | El pendiente 90, punto 2 |
| RN-05 | **Los seis rojos se declaran**, con lo que dice cada uno | Un rojo arrastrado sin decisión escrita apaga el semáforo otra vez |
| RN-06 | **No se juntan las dos suites** | `02·F5` |

### 3.2 Supuestos

- **Las pruebas no se estorban entre ellas.** Comprobado: los 650 casos cargados en un solo proceso dan **las mismas 8 fallas en los mismos 6 archivos** que uno por uno. Así que el corredor puede cargarlas juntas sin darle a cada archivo su propio proceso.

### 3.3 Fuera de alcance

- **Arreglar los seis rojos.** Se declaran acá y se arreglan en su propio trabajo: son seis defectos distintos, de fases distintas, y meterlos en esta historia la vuelve otra cosa.
- **Cambiar `02·F5`.** La regla está bien; lo que falta es poder cumplirla sobre esta carpeta.
- **Fundir las dos suites.**

---

## 4. Criterios de aceptación

### CA-01 — La carpeta se corre con una orden, y es la documentada

```gherkin
Dado el repositorio del estándar recién clonado
Cuando se corre la orden que la documentación nombra
Entonces las 650 pruebas se ejecutan y se reporta el conteo
```

**Cómo validarlo:**
1. Correr la orden documentada.
2. Resultado esperado: **corre**, y dice cuántas pruebas y cuántas fallaron.
- **Aprobado cuando:** la orden escrita y la orden que funciona son la misma.

### CA-02 — Cero pruebas no pasa por verde

```gherkin
Dado que la carpeta quedara vacía, o el descubrimiento se rompiera
Cuando se corre la orden
Entonces termina en rojo, no en verde
```

**Cómo validarlo:**
1. Apuntar el corredor a una carpeta sin pruebas.
2. Resultado esperado: **falla**, y dice que no encontró ninguna.
- **Aprobado cuando:** el silencio no se puede leer como éxito.

**Este es el criterio que decide si sirve.** El defecto que se está arreglando es exactamente ese: una orden que no corría nada y nadie lo notó.

### CA-03 — Se puede pedir un subconjunto

```gherkin
Dado que una fase toca dos archivos de prueba
Cuando se pide correr solo esos
Entonces corren solo esos, y el conteo lo dice
```

**Cómo validarlo:**
1. Pedir uno o dos archivos por su nombre.
2. Resultado esperado: corren esos, y el conteo es menor que el total.
- **Aprobado cuando:** `02·F5` se puede cumplir sobre esta carpeta.

### CA-04 — La corrida completa está colgada de algo

```gherkin
Dado que nadie se acuerde de correrla
Cuando llega el momento en que importa
Entonces la corrida ocurre, o se reclama
```

**Cómo validarlo:**
1. Comprobar que existe el enganche o la puerta, y que nombra al corredor.
2. Una prueba que lo busque **donde se cuelga**, no en el disco.
- **Aprobado cuando:** no depende de la memoria de nadie.

**Es la lección de `EP-002·HU-004`:** construido, probado, en verde, y nadie lo llamaba.

### CA-05 — Los seis rojos quedan declarados

```gherkin
Dado que hoy seis archivos fallan
Cuando se cierra esta historia
Entonces está escrito cuáles son, qué dice cada uno y adónde va
```

**Cómo validarlo:**
1. Leer el documento de cierre. Resultado esperado: los seis, con su destino.
- **Aprobado cuando:** ningún rojo queda sin decisión escrita.

### Criterios de aceptación transversales

- [x] **Errores** — apuntar el corredor a algo que no existe da mensaje claro y termina en rojo, no en silencio (`05`).
- [x] **Límites** — carpeta vacía, un solo archivo, y un nombre que no existe tienen comportamiento definido (`08`).
- [x] **No regresión** — las 515 de `pruebas.py` siguen verdes y **se siguen corriendo como hasta ahora** (`08`, `02·F5`).

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | Las 650 tardan cerca de 3 minutos. El corredor no las hace más lentas, y **poder pedir un subconjunto es lo que las vuelve usables en una fase** |
| RNF-02 | **No estorbar** | Lo que se cuelgue de la corrida completa no puede volverse un peaje en cada commit: eso se desinstala en una tarde |

---

## 6. Diseño y referencias

- **De dónde sale:** el [pendiente 90](../../../../pendientes/hecho/las-pruebas-que-existen-se-corren.md).
- **La señal:** `S-075` — cuatro registros llevados a mano se quedaron atrás, y tres tenían comprobador que nadie corría.
- **Las mediciones:** [historico-chat/scripts/2026-08-28/](../../../../historico-chat/scripts/2026-08-28/) — `corren-las-pruebas-de-tests.py` y `todos-en-un-proceso.py`.
- **La regla que hoy no se puede cumplir acá:** `02·F5`.

---

## 7. Tareas técnicas derivadas

- [x] «Backend» Un corredor que cargue la carpeta y reporte el conteo.
- [x] «Backend» Que acepte un subconjunto por nombre.
- [x] «Backend» Que cero pruebas sea rojo.
- [x] «Adaptador» Colgar la corrida completa de algo.
- [x] «Documentación» Corregir la orden que el `CHANGELOG` documenta y no funciona.
- [x] «Documentación» Declarar los seis rojos, con su destino.
- [x] «Pruebas» Los cinco criterios, con el de la carpeta vacía.
- [x] «Documentación» Entrada en el `CHANGELOG` y subir `VERSION`.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| [A-EP-005-HU-021-el-corredor-que-si-las-corre](A-EP-005-HU-021-el-corredor-que-si-las-corre/) | CA-01 a CA-05 | (vacío) | [plan_trabajo](A-EP-005-HU-021-el-corredor-que-si-las-corre/plan_trabajo.md) | [plan_pruebas](A-EP-005-HU-021-el-corredor-que-si-las-corre/plan_pruebas.md) | [resultado](A-EP-005-HU-021-el-corredor-que-si-las-corre/resultado_pruebas.md) — **Cumple** | Terminada |

**La línea base, medida antes de abrir la carpeta:** `122 en total · 32 sin terminar · 90 terminadas, de las cuales 72 cumplen, 13 no cumplen y 5 no dicen si cumplen`.

---

## 9. Dependencias y riesgos

| # | Riesgo | Qué pasa si ocurre | Qué lo controla |
|---|---|---|---|
| R-01 | Que el corredor exista y nadie lo corra | Se vuelve al mismo sitio, con una orden más | `CA-04`, que exige que esté colgado |
| R-02 | Que lo colgado moleste tanto que se apague | Peor que no tenerlo: figura como cubierto | `RNF-02`; se mide antes de cerrar cuánto tarda y cuántas veces hablaría |
| R-03 | Que los seis rojos se arrastren | El semáforo se apaga otra vez | `CA-05` |
| R-04 | Que aparezcan más rojos al correrlas seguido | Es el resultado buscado, no un riesgo | Se declaran y se enrutan |
