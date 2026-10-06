# Resultado de Pruebas · Fase «A-EP01-HU03-Descripción»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra qué se ejecutó de verdad y con qué resultado, y de ahí sale el **veredicto** de la fase: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el `estado-fase.md` para pasar la puerta de verificación, y la fuente de la sección *Qué se probó* del `funcionalidad_implementada.md`. El diseño de los casos vive en el `plan_pruebas.md` de esta misma fase, que no se modifica al ejecutar: se aprobó antes y así se queda.

> Todo documento creado con esta plantilla se redacta aplicando estas reglas. Esta nota se borra al llenarla.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](../../base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Plantilla del `resultado_pruebas` de una fase. Se guarda en la carpeta de la fase (ruta `02·F12.13`) como `resultado_pruebas.md`, y se crea junto con los dos planes aunque todavía no se haya ejecutado nada: el formato puesto desde el principio se ve, se revisa y no se olvida. Lo que no se ha corrido se escribe «no ejecutado», nunca en blanco ni como aprobado, y el veredicto arranca en «todavía no se ejecutó».
>
> Va en un documento aparte del plan porque el plan se aprueba antes de ejecutar: si los resultados se escriben encima, se pierde la línea base aprobada y ya no se puede comparar lo que se acordó probar contra lo que se probó. Es la misma separación que hace ISO/IEC/IEEE 29119-3, la norma en que se apoya el plan de pruebas, entre el plan y el registro de ejecución.
>
> Al llenarla se reemplazan los `«…»`, se borran las secciones que no apliquen y se borran todas las notas como esta. El párrafo «Para qué sirve este documento» se queda.

## 0. Identificación

> Dice qué se está probando: de qué fase y de qué historia salen los casos, contra qué plan, y en qué ciclo, cuándo, quién y sobre qué versión corrieron.

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `«A-EP01-HU03-Descripción»` |
| **HU** | «HU-NNN» |
| **Plan de pruebas de origen** | «`plan_pruebas.md`» |
| **Ciclo** | «1» (se agrega un bloque por cada reprueba, no se pisa el anterior) |
| **Fecha de ejecución** | AAAA-MM-DD |
| **Ejecutado por** | «quién» |
| **Ambiente y versión** | «dónde corrió y sobre qué build» |

## 1. Resumen de la ejecución

> Cuenta los casos del plan y los que se ejecutaron, repartidos por resultado, y nombra los que quedaron sin ejecutar con su motivo.
>
> Una ejecución es correr las pruebas de principio a fin. Si se corrige algo y se vuelve a correr, es otra ejecución, y el ciclo las numera.

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | | | | | | |

**Casos no ejecutados y por qué:** «cuáles y el motivo. Un caso sin ejecutar no se cuenta como aprobado».

## 2. Ejecución caso por caso

> Documenta cómo se corrió cada pareja CA-CP y qué problema resuelve. Por cada pareja va un bloque con tres partes, siempre las mismas y en este orden; después de los bloques va la tabla que resume los casos.

| Parte | Qué se escribe |
|---|---|
| **El problema que resuelve** | Una frase: qué se rompe si esto no funciona. Es lo que el criterio y el caso vienen a asegurar, no lo que hace la HU entera |
| **Cómo se hizo la prueba, paso a paso** | Una fila por paso, con tres columnas: **qué hacer** (en infinitivo y en palabras sencillas), **qué tiene que pasar** y **qué salió** |
| **Cómo se verificó que la pareja cumple** | Cuál paso decide y por qué, y cuál no alcanzaba solo. Si algo quedó sin hacer o se hizo distinto, se dice acá |

**Las cuatro reglas del paso a paso.** Ningún paso se da por supuesto:

| Regla | Qué exige |
|---|---|
| **Un paso por cada fila del plan** | Se copian del `plan_pruebas`, en su mismo orden. No se agrupan, no se saltan, no se inventan |
| **Se arranca desde cero** | El primer paso deja el ambiente y los datos listos. Si para llegar al punto de partida hay que **hacer** algo, ese algo es un paso, no una precondición |
| **Ningún paso queda vacío** | «Qué salió» se llena siempre: con lo que salió, con `no se hizo` o con `no quedó registrado`. En blanco se lee como aprobado |
| **Detallado es repetible** | Está suficientemente detallado cuando alguien que no estuvo puede repetir la prueba leyendo solo esto, sin preguntar nada. Comandos, rutas y datos van literales |

Un caso cumple cuando lo que salió es lo que decía la columna del medio. Si se hizo otra cosa, aunque haya salido bien, el caso **no cumple**: se probó otra cosa. El veredicto no se repite en el bloque: vive en la tabla de casos ejecutados.

Si un paso sale distinto de lo esperado, la fila lo dice. Un paso que no coincide y que nadie explica convierte el *cumple* en una afirmación sin respaldo.

> Por qué tanto detalle: con el paso a paso a medias («se creó el archivo y apareció») un caso puede pasar habiendo probado otra cosa. Pasó: un caso decía «correr el enganche» y lo que se corrió fue la función que ese enganche usa, con el dato que el enganche no tiene. Los tres criterios de esa fase quedaron en «cumple» sin estar probados, y el defecto salió a la sesión siguiente. Con las tres columnas al lado, el desvío se ve en la fila.

**Ejemplo:**

```
**CA-02 · CP-002 — que una regla nueva no entre sin su ejemplo INCORRECTO/CORRECTO**

**El problema que resuelve:** una regla sin ejemplo se lee de dos maneras y cada
proyecto la cumple a su modo. El ejemplo es lo que fija cuál es la correcta.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Situarse en el repositorio del estándar, en la rama `fase-a-q9` | `git status` no muestra cambios pendientes | Sin cambios pendientes, sobre el commit `6391e79` |
| 2 | Contar los archivos de `base/07-calidad-de-codigo/reglas/` | Queda el número de partida | 8 archivos |
| 3 | Correr `python validadores/validar.py metareglas` antes de tocar nada | Pasa sin hallazgos, así lo que falle después lo causó la regla nueva | `0 hallazgos · 8 reglas revisadas` |
| 4 | Crear `base/07-calidad-de-codigo/reglas/Q9-una-prueba-por-comportamiento.md` con su exigencia y **sin** el bloque de ejemplo | El archivo queda escrito | Quedó, 14 líneas |
| 5 | Correr el mismo comando del paso 3 | Falla, nombra el archivo y cita `20·M5` | `Q9 · falta el ejemplo INCORRECTO/CORRECTO (20·M5)` |
| 6 | Agregar a `Q9` un caso INCORRECTO y uno CORRECTO | El archivo queda con los dos casos | Quedó, 22 líneas |
| 7 | Correr el mismo comando por tercera vez | Pasa y ya no nombra a `Q9` | `0 hallazgos · 9 reglas revisadas` |

**Cómo se verificó que la pareja cumple:** el paso 5 es el que prueba el
criterio, pero solo no alcanza: un validador que fallara siempre habría fallado
igual ahí. Por eso el 3 lo deja en verde antes y el 7 lo deja en verde después,
con la regla ya corregida; y el conteo de reglas revisadas sube de 8 a 9, así
que `Q9` sí entró en la revisión y no la saltó. Los pasos 1 y 2 dejan el punto
de partida por escrito: sin ellos nadie puede repetir esto. La salida de las
tres ejecuciones quedó en EV-02.
```

| Caso | CA | Prioridad (del plan) | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Crítica | AAAA-MM-DD | «el dato, el archivo o el comando concretos» | Aprobado / Fallido / Bloqueado / No ejecutado | EV-01 | — |

La columna **Con qué se probó** lleva lo que se hizo y lo que salió, no un puntero. El plan dice qué tipo de dato usar; este documento dice qué se ejecutó exactamente y qué se obtuvo. Sin eso, *aprobado* es una afirmación sin respaldo: nadie puede repetir la prueba ni ver por qué el caso quedó en cumple.

```
INCORRECTO: | CP-002 | CA-02 | Crítica | 2026-01-05 | un usuario sin permiso | Aprobado | EV-02 | — |
            — no dice qué usuario, sobre qué, ni qué pasó
INCORRECTO: | CP-002 | CA-02 | Crítica | 2026-01-05 | ver la suite | Aprobado | EV-02 | — |
            — manda a buscarlo a otra parte
CORRECTO:   | CP-002 | CA-02 | Crítica | 2026-01-05 | `qa.consulta` pidió `POST /facturas/42/anular`
            y recibió 403; la factura siguió en estado `emitida` | Aprobado | EV-02 | — |
```

**Correspondencia con el plan:** «N casos en el plan, N acá. Ninguno de más, ninguno de menos». Si no cuadra, se dice cuáles bailan y por qué.

**Qué salió distinto de lo esperado:** «para los fallidos, qué se esperaba y qué pasó. Sin esto, "fallido" no sirve para corregir».

## 3. Verificaciones manuales  ·  [`08·T4`](../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

> Es lo que el entorno automático no reproduce y hubo que comprobar a mano. Se lista aunque haya salido bien: lo que no está aquí se lee como no probado. Si no hubo ninguna, se escribe «Ninguna».

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | | | |

## 4. Defectos encontrados

> Registra cada defecto que destapó la ejecución, con su severidad, su estado y dónde quedó registrado. Si no hubo, se escribe «Ninguno».

| ID | Título | Caso que lo destapó | Severidad | Estado | Dónde quedó registrado |
|---|---|---|---|---|---|
| DEF-01 | | CP-001 | Crítica / Alta / Media / Baja | Abierto / Corregido / Verificado / Aceptado | |

**Defectos abiertos que se aceptan y por qué:** «los que se dejan pasar, con quién lo autorizó. Un defecto abierto sin decisión escrita bloquea el cierre».

## 5. Veredicto por criterio de aceptación y requisito no funcional

> Es la tabla que decide: una fila por cada `CA-0N` y cada `RNF-0N` de la HU, con los casos que la cubren. Una exigencia sin caso ejecutado no se marca cumplida, aunque se haya visto funcionar. Los requisitos no funcionales llevan su fila igual que los criterios: sueltos en un renglón de prosa, nadie los verifica.

| Exigencia de la HU (`CA-0N` · `RNF-0N`) | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001, CP-002 | | Sí / No |

**Los que no cumplen:** «qué falta exactamente y a qué tarea o fase se traslada».

## 5.1 Lo que el plan exigía

> Contrasta cada meta que fijó el `plan_pruebas` con lo que se logró, una fila por meta. Las metas se copian del plan, no se inventan aquí: si el plan pedía cubrir el 100% de los casos críticos, esta tabla dice cuánto se cubrió de verdad.

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de criterios y requisitos no funcionales | Plan §5 | 100% | | Sí / No |
| Casos críticos y altos ejecutados | Plan §3.4 | 100% | | Sí / No |
| «Métrica propia del plan» | Plan §12.1 | «meta» | | Sí / No |
| Criterios de salida | Plan §4.2 | Todos | | Sí / No |

**Lo que no se cumplió:** «qué meta del plan quedó corta y qué se decidió al respecto. Una meta incumplida sin decisión escrita bloquea el cierre».

## 6. Veredicto de la fase

> Es el concepto final de la fase, el que se copia al `estado-fase.md` y al `funcionalidad_implementada.md`. Una fase con un CA en «No» no pasa la puerta de verificación, pero sí cierra, declarándolo: el cierre deja escrito qué salió, qué falta y a dónde se pasó. Dejarla abierta esconde su deuda, porque una deuda en una fase sin cerrar no la lee nadie.

**Concepto:** «Cumple / No cumple». No hay estado intermedio: si algo de lo pedido falta, es **No cumple**. Los defectos van en §4 con su severidad, y ahí se ve qué se aceptó y quién lo aceptó.

**Justificación:** «en dos o tres líneas, apoyada en §5».

**Qué falta para que cumpla** (si no cumple): «lista concreta».

## 7. Evidencias

> Lista cada evidencia que citan las secciones anteriores y dónde está.

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Salida de la ejecución / captura / archivo resultante | `«ruta o enlace»` |

## 8. Ciclos anteriores

> Guarda la historia de las repruebas. Cuando hay una, el ciclo nuevo se agrega encima y el anterior queda tal cual, porque saber que algo falló y después pasó vale más que ver solo el resultado final. Con un solo ciclo queda la fila de la primera ejecución.

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | | | | Primera ejecución |
