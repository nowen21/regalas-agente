# Plan de Trabajo — Fase `A-EP-005-HU-021-el-corredor-que-si-las-corre`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. Lo que se pide vive en la [HU-021](../HU-021-las-pruebas-que-existen-se-corren.md); con qué casos se comprueba, en el [plan_pruebas.md](plan_pruebas.md).

---

## 1. Qué se va a hacer

**Que las 650 pruebas de `validadores/tests/` se puedan correr, se corran, y que cero pruebas no pase por verde.**

- 📝 **Sale de un daño medido.** La lista de exentos del detector de secretos quedó vieja y `validar.py todo` estuvo **seis días en rojo** diciendo «posible secreto en el código». La prueba que lo cazaba estaba escrita hacía diez días y nunca se corrió (`S-075`, [pendiente 90](../../../../../pendientes/90-las-pruebas-de-validadores-tests-no-las-corre-nada.md)).

### 1.1 Fuera de alcance

- **Arreglar los seis rojos.** Se declaran; se arreglan aparte. Son seis defectos de fases distintas.
- **Fundir las dos suites.** `02·F5` pide correr lo que la fase toca, no todo.
- **Cambiar `02·F5`.**

---

## 2. Análisis previo  ·  `02·F17`

### 2.1 La línea base, medida

| Qué | Cuánto | Con qué se midió |
|---|---|---|
| Archivos de prueba en `validadores/tests/` | **67** | `ls` |
| Pruebas que contienen | **650** | `todos-en-un-proceso.py` |
| Archivos en verde corridos **uno por uno** | **61** | `corren-las-pruebas-de-tests.py` |
| Archivos en rojo | **6**, con 8 fallas | el mismo |
| Los 650 **juntos en un proceso** | **los mismos 6 archivos**, 8 fallas, **0 errores** | `todos-en-un-proceso.py` |
| Lo que tarda la carpeta entera | **~3 min** | el mismo |
| Lo que tarda `pruebas.py` | **~3 min**, 515 pruebas | `salida-suite.txt` |

**La quinta fila es la que decide el diseño.** Como cargarlas juntas da exactamente el mismo resultado que una por una, **no se estorban**: el corredor puede cargarlas en un solo proceso y no hace falta darle a cada archivo el suyo, que costaría 67 arranques de Python.

### 2.2 Lo que ya existe y no se rehace

| Pieza | Estado | Qué hace |
|---|---|---|
| Las 650 pruebas | **Existen y corren** | No se tocan. Lo que falta es quién las llama |
| `validar.py` | **Existe** | Ya tiene 43 subcomandos y el molde de `reportar` |
| `pruebas.py` | **Existe** | Sus 515 siguen corriéndose igual que hoy |

### 2.3 Qué se va a tocar

| Archivo | Qué se le hace |
|---|---|
| `validadores/tests/__init__.py` | **Nuevo, vacío.** Es lo que hace cargar el descubrimiento |
| `validadores/corredor.py` | **Nuevo.** Carga la carpeta, acepta un subconjunto, reporta el conteo y **falla si corrió cero** |
| `validadores/validar.py` | Un subcomando que lo llama |
| `validadores/pruebas.py` | Las pruebas de la fase |
| `.githooks/pre-push` o el instalador | De dónde cuelga la corrida completa — **se decide en la `T-04`, midiendo** |
| `CHANGELOG.md` · `VERSION` | `20·M10` |
| El `README` de `validadores/` | La orden correcta, donde alguien la busca |

### 2.4 Matriz de dependencias

| Archivo | Cambio de contrato | Quién depende | Dónde rompe |
|---|---|---|---|
| `validadores/tests/` | **Pasa a ser paquete** | Los 67 archivos, que hoy se corren sueltos | **Riesgo real:** un `__init__.py` cambia cómo resuelven sus importaciones. Se mide en la `T-01` antes de seguir |
| `validar.py` | Se agrega un subcomando; ninguno cambia | El enganche de `pre-commit`, el instalador | No rompen: agregar no quita |

### 2.5 Punto de entrada

Una orden. Y la corrida completa, colgada.

### 2.6 Permisos / roles a sembrar

**Ninguno.** No se toca la configuración global de git (`00·N1`).

### 2.7 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **Un corredor propio**, no `discover` pelado | Solo crear el `__init__.py` | `discover` con cero pruebas **termina en 0**. Eso es exactamente el defecto que estamos arreglando: el silencio leído como éxito |
| **Se crea igual el `__init__.py`** | Cargar solo por ruta desde el corredor | La orden documentada desde la primera prueba del repositorio debe funcionar. Que la documentación mienta es la mitad del problema |
| **Un solo proceso** | Un proceso por archivo | Medido: mismo resultado, y 67 arranques costarían minutos |
| **Las dos suites siguen separadas** | Fundirlas | `02·F5`; y juntarlas empujaría a correr 1165 pruebas en cada fase |
| **Lo colgado no puede ser un peaje de cada commit** | Correrlas en `pre-commit` | 3 minutos por commit se desinstala en una tarde. **Dónde cuelga se decide midiendo**, no de entrada |
| **Los seis rojos se declaran, no se arreglan acá** | Arreglarlos de paso | Seis defectos de fases distintas dentro de una fase la vuelven irrevisable |

### 2.8 Dudas por resolver antes de codificar

| # | Duda | Estado |
|---|---|---|
| 1 | **¿El `__init__.py` rompe alguno de los 67?** Cambia cómo resuelven sus importaciones | **`T-01`, midiendo**: se crea, se corren los 67, se compara contra los 61/6 de hoy. Si aparece un rojo nuevo, **para y se replantea** |
| 2 | **¿De dónde cuelga la corrida completa sin volverse peaje?** | **`T-04`, midiendo**: se cuenta cuánto tardaría y cuántas veces se dispararía en los últimos commits, igual que la `T-06` de la `HU-020` |

**Las dos se resuelven midiendo, no decidiendo.** Es lo que salvó la historia anterior: el arreglo obvio se descartó porque el número lo desmintió.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|:--:|---|---|---|
| T-00 | **Antes de tocar nada:** dejar por escrito el 61/6 de hoy, archivo por archivo | Test | 0,5 h | — | EV-00 |
| T-01 | **Resolver la duda 1**: crear el `__init__.py` y comparar contra la línea base | Backend | 0,5 h | T-00 | EV-01 |
| T-02 | El corredor: carga la carpeta y reporta el conteo | Backend | 1,5 h | T-01 | EV-02 |
| T-03 | Que **cero pruebas sea rojo**, y que acepte un subconjunto | Backend | 1 h | T-02 | EV-02 |
| T-04 | **Resolver la duda 2**: dónde cuelga, con el número de cuánto costaría | Calidad | 1 h | T-03 | EV-03 |
| T-05 | Colgarlo donde diga la `T-04` | Adaptador | 1 h | T-04 | EV-03 |
| T-06 | Corregir la orden documentada en el `README` de `validadores/` | Documentación | 0,5 h | T-02 | EV-04 |
| T-07 | **Declarar los seis rojos**, con lo que dice cada uno y adónde va | Documentación | 1 h | T-00 | EV-05 |
| T-08 | Los cinco CA, con el de la carpeta vacía | Test | 2,5 h | T-03 | EV-01 a EV-05 |
| T-09 | **Correrlo de verdad**: la orden documentada, desde cero | Calidad | 0,5 h | T-05 | EV-06 |
| T-10 | `CHANGELOG` y `VERSION` | Documentación | 0,5 h | T-04 | EV-07 |
| T-11 | Sabotear | Calidad | 1 h | T-08 | EV-08 |

**Total estimado:** 11,5 h

**Versión: MENOR.** Aditivo: un subcomando y un corredor. **Nadie tiene que cambiar nada de lo que ya tiene.** Sube a `35.9.0`.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-00 → T-01 → T-02 → T-03 → T-04 → T-05 → T-09

**La `T-01` puede tumbar el diseño**, y va antes de escribir el corredor: si el `__init__.py` pone en rojo alguno de los 61 que hoy están en verde, el camino de «que la orden documentada funcione» se cae y hay que replantear.

**La `T-04` puede tumbar el enganche.** Si colgarlo cuesta más de lo que evita, se cuelga en otro sitio o no se cuelga — y se dice con el número.

**Y la `T-09` no es opcional:** es la lección de `EP-002·HU-004`, construido y no colgado.

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Evidencia | Resultado | Estado |
|---|---|---|---|---|
| CA-01 · la orden documentada corre | Correrla desde cero | EV-04 | | ☐ |
| CA-02 · cero pruebas es rojo | Apuntarlo a una carpeta vacía | EV-02 | | ☐ |
| CA-03 · subconjunto | Pedir dos archivos por su nombre | EV-02 | | ☐ |
| CA-04 · está colgado | Buscarlo donde se cuelga, no en el disco | EV-03 | | ☐ |
| CA-05 · los seis rojos declarados | Leer el cierre | EV-05 | | ☐ |

---

## 6. Datos y ambiente de prueba

**Carpetas temporales**, creadas y borradas por la prueba, para los casos de vacío y de subconjunto. **Ninguna prueba usa credenciales** (`00·N6`), y **ninguna corre las 650 dentro de la suite** — eso las volvería de tres minutos.

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit y bajando `VERSION`. **Lo colgado se quita volviendo a correr el instalador.** El `__init__.py` se borra y todo vuelve a como está hoy.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**Quien ya tenga el estándar** no ve cambiar nada hasta que corra el instalador. **Ningún archivo suyo se toca.**

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `02·F8` — solo los archivos declarados.
- `02·F17` — la línea base medida antes de planear, no citada.
- `02·F5` — las dos suites siguen separadas.
- `08·T5` — ejecuta **y reporta el conteo**.
- `00·N1` — no se toca la configuración global de git.
- `20·M10` — versión y registro de cambios.
- `13·DOC5` — lo decidido se registra como señal: `S-075`.

---

## 10. Riesgos

| # | Riesgo | Qué pasa si ocurre | Qué lo controla |
|---|---|---|---|
| R-01 | El `__init__.py` rompe importaciones | El camino documentado se cae | **`T-01`, antes de codificar** |
| R-02 | Lo colgado se vuelve peaje y se apaga | Peor que no tenerlo: figura como cubierto | **`T-04`, con su número** |
| R-03 | Que el corredor exista y nadie lo corra | Se vuelve al mismo sitio | `CA-04` |
| R-04 | Que aparezcan más rojos | Es el resultado buscado | Se declaran y se enrutan |

---

## 11. Aprobación

| Rol | Estado |
|---|---|
| Usuario | **Aprobado** el 2026-08-28 |
