# Análisis 3: el plan de la EP-029·HU-002 no declara la sección del manual que pide toda pantalla nueva

> **Aprobado** por el usuario el 2026-10-08, en el turno 33, con la versión 56.8.0. Desde ese momento este análisis no se reescribe.

> Plantilla del análisis. Al llenarla se reemplazan los `«…»` y se borran las notas como esta, menos la tabla de reglas.
>
> Solo entra lo que ayuda a entender qué pasa y a tomar una decisión. Lo que no aporta a decidir no se escribe.
>
> Todo título y todo enlace dicen de qué se trata, nunca solo un número: «Pendiente: lo que se construye se aparta de lo aprobado», no «pendiente 103».
>
> Este análisis se redacta aplicando estas reglas.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../../../../../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](../../../../../base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Un análisis aprobado no se reescribe. Si al ejecutar el plan aparece un hallazgo que obliga a tocar algo que el plan no declara, se abre `analisis-«N+1»`.md, que trata solo lo que falló y sus implicaciones sobre lo ya hecho. El hallazgo que no obliga a eso no abre análisis: se anota con su pendiente donde pertenece y el plan continúa.

---

## Recomendaciones

| Recomendación | Cómo se aplica en este análisis |
|---|---|
| R-1 | «Dónde más puede pasar» revisa las HU-003 a HU-005 y toda fase que cree una pantalla |
| R-2 | Se corrieron las suites de las demás apps de Cimiento para encontrar de una vez todo lo que piden las pantallas nuevas |
| R-15 | La ejecución se detuvo antes de escribir el manual |
| R-19 | Se aplicó a las migraciones; este análisis la amplía porque no cubrió el manual |
| Las demás | No aplican: no se cambia ninguna regla (R-3, R-4) y no hay piloto (R-16) |

---

## Hallazgo

### H-3 · El plan de la EP-029·HU-002 no declara la sección del manual que pide toda pantalla nueva

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-08, en la fase `A-EP-029-HU-002-revisar-y-su-pagina`, la prueba `test_ninguna_pantalla_queda_sin_seccion` (`core/ayuda/tests.py`) falló: toda pantalla nueva necesita su sección del manual en `core/ayuda/secciones.py` y su texto en `core/ayuda/templates/ayuda/secciones/`, y las rutas que no son pantalla van en `NO_SON_PANTALLAS`. El plan declaró el menú, las tablas y la ayuda de pantalla, pero no el manual |
| Por qué importa | Lo que el plan no declara no se escribe y la fase se detiene. La R-19 del análisis 2 solo pide preguntar por las migraciones; no cubre las pruebas que exigen piezas a toda pantalla nueva |
| Pendiente | El mismo pendiente 141: se trata en su análisis 3 |

## Pendiente

La V3, según el análisis 2: Cimiento revisa qué parte de cada proyecto queda sin pruebas y lo exige desde su configuración. Además de lo de la V2, el plan de la HU-001 tiene que declarar la migración de `core/proyectos/`, y los planes que cambian la base tienen que listar antes todo lo que el marco va a pedir.

---

## Conversación

> La escribe el enganche en tiempo real, turno por turno, desde la transcripción de la sesión. No se escribe a mano.

### 31 · Usuario, 2026-10-08 21:03:35
> Analicemos: el pendiente 141

**Agente**, 2026-10-08 21:05:24
<!-- agente: 483fcad6-50fb-4a4d-b33f-58d236f4a381 -->

El análisis 3 está abierto: [analisis-3.md](../../../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-3.md).

Cimiento tiene pruebas que revisan que toda pantalla nueva tenga cuatro cosas: un lugar en el menú, tablas que se puedan ordenar, su ayuda y un capítulo en el manual. El plan de la HU-002 olvidó el capítulo del manual, y por eso el trabajo se detuvo.

Necesito dos respuestas, cada una con SÍ o NO:

1. ¿Se agregan al plan de la HU-002 los dos archivos del manual, para que el trabajo siga? Recomiendo SÍ.
2. ¿Se amplía la R-19? Hoy solo pide revisar los archivos de la base de datos. La propuesta es que también pida revisar estas cuatro cosas cada vez que un plan cree una pantalla, en cualquier proyecto. Recomiendo SÍ.

### 32 · Usuario, 2026-10-08 21:05:53
> respondo: SI

**Agente**, 2026-10-08 21:07:43
<!-- agente: 0ce387a3-4a5c-4c47-8e45-c3995acc1ff2 -->

Hago ya lo que se manda «de una»: el pendiente pasa a su V4, el hallazgo H-3 a su V2 y la R-19 se amplía.

Quedaron anotados los dos acuerdos. El pendiente pasó a su V4, el hallazgo H-3 a su V2 y la R-19 ya incluye también las piezas que toda pantalla nueva necesita. El análisis 3 no tiene preguntas abiertas.

Para aprobarlo, escriba:

```
Apruebo el análisis
```

### 33 · Usuario, 2026-10-08 21:10:22
> Apruebo el análisis

**Agente**, 2026-10-08 22:15:23
<!-- agente: 5e74d6eb-3ecb-4bbf-b486-3ac1c9e4cabe -->

El análisis 3 quedó aprobado. Sigo con la HU-002: primero sumo los dos archivos del manual al plan, y después escribo la sección.

Las 120 pruebas de las suites de la fase pasan. Cierro los documentos de la fase A de la HU-002.

Sigo revisando qué piezas pide un subcomando nuevo de validación, para declararlas todas en el plan de la HU-003.

Primero agrego al modelo el dato que necesita el desinstalador y compruebo qué migración pide Django, antes de escribir el plan (R-19).

Ya tengo la lista completa de lo que pide la HU-003. Escribo la HU y abro su fase.

El aviso de enlace roto es del pendiente 142, que escribió otra sesión. No lo toco, porque es trabajo de otra sesión; lo menciono al final. Sigo con el plan de la HU-003.

Ahora el código. Primero la migración declarada y el aviso, que lee la base sin arrancar Django.

La base guarda las fechas en UTC, así que el aviso tiene que compararlas con la hora UTC y no con la local.

Conecto el aviso al arranque de la sesión.

Ahora el subcomando `pruebas` de `validar.py` y su línea en el `pre-commit`.

Ahora `parte.py`, la que pone y quita la herramienta según el lenguaje sin depender de Django, y la orden `marcar_pruebas`.

Agrego el paso al instalador y su contrario al desinstalador.

Escribo las pruebas de la HU-003. Antes reviso cómo se arma `ArranqueDeSesion`.

Las 41 pruebas de la app pasan. Corro la regresión de las suites que toca la HU-003: enganches y herramientas.

Hay 5 problemas. Uno ya se conocía (pendiente 140). Reviso los otros cuatro para saber si los causa este cambio.

Dos fallas son de `validar.py`: el subcomando `estandar` ahora sale con código 1. Lo corro para ver qué reporta.

Esta sí la causa mi cambio: mis pruebas sin Django vacían la base al terminar, y eso choca con lo que prepara `tests_reglas_del_proyecto`. Reviso cómo resolvió esto el resto del código.

The convention in Cimiento is `serialized_rollback = True`, so the database is restored after each test. I'll add it to my test classes.

Ya pasan. Las fallas que quedan en la regresión son ajenas a esta HU: la del pendiente 140 y las dos que causa el enlace roto del pendiente 142, de otra sesión. Cierro los documentos de la HU-003.

La orden falló por cómo la consola leyó el texto largo; no alcanzó a cambiar nada. Escribo los dos documentos con el editor y hago aparte los reemplazos cortos.

Cimiento tiene la orden `cerrar_fase`. Reviso qué hace antes de seguir marcando los documentos a mano.

Solo tocaría el estado de la fase, el plan de pruebas, la HU y la épica; no reescribe lo que ya escribí. La aplico.

La HU-003 quedó cerrada. Sigo con la HU-004, que quita la copia de la configuración. Según la R-19, primero busco todo lo que la nombra, para declararlo en el plan.

Ahora el código de la HU-004. Reviso las cuatro llamadas en las vistas.

Ahora la ayuda, que deja de nombrar la copia, y el paso del instalador que borra la copia vieja.

La HU-004 pasa: 299 pruebas en verde y ningún archivo sigue usando la copia. Escribo su cierre.

Para fijar versiones exactas sin instalar nada, le pido a pip que resuelva Playwright 1.63.0 en modo de prueba.

Pip resolvió las versiones exactas: playwright 1.63.0, greenlet 3.5.6, pyee 13.0.1 y typing_extensions 4.16.0. Con eso cumplo `10·DEP2`. Escribo la HU-005.

Esos enlaces rotos son de la EP-026·HU-011, en la que otra sesión está trabajando ahora mismo. No los toco. Escribo el plan de la HU-005.

Ahora el código de la HU-005: el módulo que encuentra y corre las pruebas de navegador.

Escribo las pruebas de la HU-005.

La HU-005 pasa: 313 pruebas en verde. Cierro su fase.

Cerré las cinco HU. Dejo la épica con un estado uniforme y reviso si quedaron marcadores sin llenar en sus archivos.

Pongo al día el índice de épicas. Después reviso cómo registró su versión la épica anterior, porque la regla `20·M10` exige versionar todo cambio.

Las cuatro migraciones quedaron aplicadas. Hago una prueba real, con un proyecto registrado, para ver el mensaje que recibe quien usa Cimiento cuando a un proyecto le falta la herramienta.

Ahora registro la versión del estándar en la base. Es MAYOR porque obliga a volver a instalar Cimiento en cada proyecto.

La versión quedó registrada: el estándar pasa a la 59.0.0, MAYOR. Reviso si hay una herramienta para cerrar el pendiente 141, ahora que sus tres análisis están construidos.

El pendiente 141 no se cierra a mano: su estado sale solo de los enlaces, y su épica ya está terminada. Lleno la sección de cierre del resumen de la sesión.

Reúno la lista de lo que cambió esta sesión, para separarlo del trabajo de las otras antes de preguntar por el commit.

La EP-029 quedó construida completa: las cinco HU, cada una con su plan, sus pruebas y su cierre.

**Qué quedó funcionando:**
- En la página de cada proyecto se elige qué tan estricto ser con la revisión de pruebas y cada cuántos días hacerla.
- La página «Revisión de pruebas» muestra todos los proyectos. El botón «Revisar» revisa con la herramienta del lenguaje de cada uno e incluye las pruebas de navegador.
- Al empezar a trabajar, Cimiento avisa si la revisión falta o está vencida. Con la opción «no dejar guardar», además no deja guardar los cambios.
- El instalador pone la herramienta que revisa, y el desinstalador la quita.
- La copia de la configuración que nadie usaba ya no existe.
- La base de Cimiento ya tiene las tablas nuevas. El estándar pasó a la versión 59.0.0, que es MAYOR.

**Lo que no salió perfecto:**
- La ejecución se detuvo dos veces por archivos que el plan no nombraba. Se resolvió con los análisis 2 y 3, y la recomendación R-19 quedó para que no se repita.
- Al cerrar encontré y corregí un defecto mío: la revisión dejaba un archivo suelto dentro del proyecto revisado.
- La herramienta `cerrar_fase` deja sin marcar los criterios que tienen dos casos (pendiente 139). Los marqué a mano.

**Lo que es de otras sesiones y no toqué:**
- Hay enlaces rotos en el pendiente 142 y en la EP-026·HU-011, y fallan pruebas por ellos y por el pendiente 140.
- `tests_freno.py` lo cambió otra sesión.
- El análisis principal mezcla líneas mías y de otras sesiones.

Falta, en orden:
1. Su aprobación del commit.
2. Volver a instalar Cimiento en cada proyecto, porque es una versión MAYOR.
3. Dar clic en «Revisar» en cada proyecto.

¿Hago el commit, SÍ o NO? Sería uno solo para toda la épica, como en la EP-028, y solo con los archivos de esta sesión.

> acá termina la conversación

---

## Lo acordado

1. La HU-002: se agregan a su plan `core/ayuda/secciones.py` y `core/ayuda/templates/ayuda/secciones/pruebas.html`, la sección del manual de las pantallas nuevas, y la fase sigue donde quedó (turno 32).
2. La R-19 se amplía: antes de escribir el plan, además de las migraciones, se buscan las pruebas que exigen piezas a toda pantalla nueva (menú, tablas, ayuda y manual) y se declara lo que cada una pide. Vale para cualquier proyecto (turno 32).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `02·F8`, `02·F17` y `02·F14` Q9, como en el análisis 2, y `17·I7` (toda pantalla se alcanza y orienta sola), que es lo que exigen las pruebas del menú, la ayuda y el manual. No choca ninguna.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| Lo que las pruebas exigen a toda pantalla nueva | Estar en el menú (`core/inicio/tests_menu.py`), usar el patrón de tablas (`core/inicio/tests_tablas.py`), traer su ayuda de pantalla (`core/ayuda/tests_formularios.py`) y tener su sección del manual (`core/ayuda/tests.py`, con `core/ayuda/secciones.py`) |
| La fase A de la HU-002 | T-01 a T-04 hechas; 25 pruebas propias en verde; falta la sección del manual |
| Las demás suites | `core.cuentas`, `core.historia`, `core.estandar`, `core.niveles` y `core.consumo` no piden nada más a las pantallas nuevas; su única falla es ajena (H-4, pendiente 143) |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| Análisis 2 del pendiente 141, lección 1 (S-353) y R-19 | Muestra que la R-19 se quedó corta: preguntó por las migraciones y no por las demás piezas que pide un cambio |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | Ninguno: cambia el plan de una fase de Cimiento y una recomendación de los análisis |
| Normas y leyes | Ninguna |
| Herramientas | Las pruebas de Cimiento que recorren todas sus pantallas |

### Dónde más puede pasar

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| La HU-002 | Su fase A | Se queda detenida | Acuerdo 1 |
| Las HU-003 a HU-005 | Sus planes, por escribir | Se detienen igual si crean una pantalla | Acuerdo 2 |
| Toda fase que cree una pantalla, en cualquier proyecto | Las fases futuras | El mismo hallazgo en otra épica | Acuerdo 2: la R-19 ampliada |

---

## Propuesta final: hallazgo y pendiente V4, épica y HU

### Hallazgo V2. El plan de la EP-029·HU-002 no declara la sección del manual que pide toda pantalla nueva

| Campo | Valor |
|---|---|
| Qué pasó | Al ejecutar la fase A de la EP-029·HU-002, la prueba del manual pidió la sección de las pantallas nuevas en `core/ayuda/secciones.py` y su texto. El plan no buscó qué pruebas le exigen piezas a toda pantalla nueva |
| Por qué importa | Lo que el plan no declara no se escribe, y la fase se detiene. Le puede pasar a cualquier plan que cree una pantalla en cualquier proyecto |

### Pendiente V4. Cimiento revisa qué parte de cada proyecto queda sin pruebas y lo exige desde su configuración

| Campo | Valor |
|---|---|
| De dónde sale | Los hallazgos V2 de H-1 y H-2, según los análisis 1 y 2, y el hallazgo V2 de H-3: el plan de la EP-029·HU-002 no declara la sección del manual que pide toda pantalla nueva |
| El problema | El de la V3. Además, el plan de la HU-002 tiene que declarar la sección del manual, y los planes que crean pantallas tienen que buscar antes qué piezas les exigen las pruebas |
| Por qué importa | El de la V3, y que una fase no se detenga por una pieza que se podía prever |

### Épica y HU que salen del análisis

Las mismas de la EP-029: este análisis no crea HU, cambia el plan de la HU-002 y amplía la R-19 para las demás.

| Orden | HU | Título | Parte del problema que resuelve | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|---|---|
| 1 | EP-029·HU-002 | El botón «Revisar» muestra qué parte de cada proyecto queda sin pruebas | El plan no declara la sección del manual | EP-029·HU-001 | Es la que quedó detenida | 2 |

## Lecciones aprendidas

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | Antes de planear una pantalla nueva, se buscan las pruebas que exigen piezas a toda pantalla | Falló | S-354 | Complementa R-19 |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Pasar el pendiente a su versión siguiente y el hallazgo H-3 a su V2 | `13·DOC26` | Este análisis, de una y sin fase: `historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/pendiente.md` y `historico-chat/resumenes/2026-10-07/instalar-desde-cimiento-y-pruebas-en-django.md`, hecho el 2026-10-08 |
| 2 | Agregar al plan de la fase A de la HU-002 `core/ayuda/secciones.py` y `core/ayuda/templates/ayuda/secciones/pruebas.html`, y seguir la fase desde T-05 | 1 | EP-029·HU-002 |
| 3 | Ampliar la R-19 con las pruebas que exigen piezas a toda pantalla nueva, y sumarle el origen de la lección 1 | 2 | Este análisis, de una y sin fase: `plantillas/recomendaciones-del-analisis.md`, hecho el 2026-10-08 |

## Lo que aporta al análisis principal

**Resultado:** aclara.

**Lo que suma al análisis principal:** antes de escribir el plan de una fase, se buscan también las pruebas que exigen piezas a toda pantalla nueva, y el plan declara lo que cada una pide.
