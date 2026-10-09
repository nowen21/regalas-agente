# Análisis 2: el plan de la EP-029·HU-001 no declara la migración que piden los ajustes nuevos

> **Aprobado** por el usuario el 2026-10-08, en el turno 30, con la versión 56.8.0. Desde ese momento este análisis no se reescribe.

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
| R-1 | «Dónde más puede pasar» revisa las otras cuatro HU de la EP-029 y cualquier plan que cambie los ajustes |
| R-2 | Se revisó cómo se resolvió la `0006` de la EP-028·HU-001: estaba declarada en su plan |
| R-6 | Se leyó completo el análisis 1: su punto 2 manda los ajustes y no dice nada de migraciones |
| R-15 | La ejecución se detuvo antes de escribir la migración |
| Las demás | No aplican: no se cambia ninguna regla (R-3, R-4) y no hay piloto (R-16) |

---

## Hallazgo

### H-2 · El plan de la EP-029·HU-001 no declara la migración que piden los ajustes nuevos

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-08, al ejecutar la fase `A-EP-029-HU-001-ajustes-y-estado-de-la-revision`, Django pidió `proyectos/cimiento/core/proyectos/migrations/0007_…py`: las claves de los ajustes son opciones de un campo de la base, y dos claves nuevas cambian esas opciones. El plan declaró solo la migración de la app nueva. La `0006` de la EP-028·HU-001 sí estaba declarada en su plan |
| Por qué importa | Lo que el plan no declara no se escribe: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). Sin esa migración, los modelos y la base quedan desfasados |
| Pendiente | El mismo pendiente 141: se trata en su análisis 2 |

## Pendiente

**De dónde sale:** hallazgo V2 de H-1 · Cimiento no sabe qué parte del programa de cada proyecto queda sin pruebas, ni lo exige, según el análisis 1.

**El problema.** Ningún proyecto mide qué parte de su programa queda sin pruebas; la configuración de cada proyecto no lo exige ni guarda el estado; ninguna prueba usa un navegador real; y cada proyecto tiene una copia de su configuración, `.agente/configuracion.md`, que ningún programa lee.

**Por qué importa.** Un hueco sin medir no se ve, una exigencia que no está en la configuración no se cumple, y una copia que nadie lee termina con datos viejos que alguien puede creer ciertos.

---

## Conversación

> La escribe el enganche en tiempo real, turno por turno, desde la transcripción de la sesión. No se escribe a mano.

### 24 · Usuario, 2026-10-08 15:28:46
> Analicemos: el pendiente 141

**Agente**, 2026-10-08 15:30:39
<!-- agente: 74fb8c3d-d83d-494d-b086-a857a1760dfa -->

El análisis 2 quedó abierto y ya tiene lo que encontré: [analisis-2.md](../../../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-2.md).

Una explicación corta del problema. Cuando cambia lo que se guarda en la base de datos, Django pide un archivo nuevo que describe ese cambio, llamado migración. El plan de la HU-001 nombró la migración de la parte nueva, pero no la de las opciones de configuración, que también cambiaron.

Necesito dos respuestas:

1. **¿Se agrega al plan de la HU-001 el archivo que falta?** Así la fase puede seguir donde quedó. Recomiendo que sí.
2. **¿Cómo evitar que vuelva a pasar?** Antes de escribir el plan de una fase que cambie la base de datos, preguntarle a Django qué archivos va a pedir y ponerlos todos en el plan. Esto serviría para las HU-002 a HU-005 y para cualquier fase futura de cualquier proyecto. Recomiendo que sí, y que quede como una recomendación nueva para todos los análisis.

### 25 · Usuario, 2026-10-08 20:07:44
> 
> explique: aplicando 00 id7 y 00 id9

**Agente**, 2026-10-08 20:07:58
<!-- agente: 532206dc-55ed-4011-81f7-037da97f1f42 -->

Lo explico con un ejemplo de la casa.

Cimiento guarda sus datos en una base de datos, que funciona como un archivador con cajones. Cada vez que cambia la forma de un cajón, hay que dejar una nota que diga «a este cajón se le agregaron dos divisiones». Django, el programa sobre el que está hecho Cimiento, exige esa nota. Sin ella, el archivador y lo que el programa cree que tiene dejan de coincidir.

Antes de trabajar, se escribe un plan con la lista de archivos que se van a tocar, y Cimiento no deja tocar ninguno que no esté en esa lista. Al agregar las dos opciones nuevas (qué tan estricto ser y cada cuántos días revisar), cambió un cajón, y su nota no estaba en la lista. Por eso el trabajo se detuvo.

**Pregunta 1.** ¿Se agrega esa nota a la lista del plan? Así el trabajo sigue donde quedó. Recomiendo que sí.

**Pregunta 2.** ¿Cómo evitar que se repita? Antes de escribir un plan, se le pregunta a Django qué notas va a pedir y se ponen todas en la lista desde el principio. Recomiendo hacerlo así siempre, en este proyecto y en los demás.

### 26 · Usuario, 2026-10-08 20:10:35
> apruebo

**Agente**, 2026-10-08 20:15:33
<!-- agente: 161e8acf-2055-49e1-be90-824db4be0a6b -->

Anoto los dos acuerdos. Primero tomo el número de turno de la conversación del análisis, sin contarlo a ojo.

Hago ya lo que el análisis manda «de una»: el pendiente pasa a su V3, el hallazgo H-2 a su V2, y se agrega la recomendación R-19.

El análisis 2 está completo y listo para aprobar: [analisis-2.md](../../../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-2.md).

Queda así:
- La HU-001 suma a su plan el archivo que faltaba y sigue donde quedó.
- La recomendación nueva, la R-19, ya está escrita: antes de hacer un plan que cambie la base de datos, se le pregunta al programa qué archivos va a pedir.
- El pendiente y el hallazgo ya quedaron actualizados.

Encontré otra falla mía, del análisis 1. Sus tres lecciones dicen que «complementan» las recomendaciones R-2, R-10 y R-18, pero no agregué esas lecciones al origen de cada una, como pide el archivo de recomendaciones. Recomiendo corregirlo dentro de este análisis. ¿Lo agrego?

Si lo aprueba todo, escriba:

```
Apruebo el análisis
```

### 27 · Usuario, 2026-10-08 20:16:00
> pregunta ya quedó claro todo el análisis?

**Agente**, 2026-10-08 20:16:11
<!-- agente: dcbeccb1-9725-4de7-a269-7ae310f00f09 -->

Casi todo. Los dos puntos que usted aprobó ya están escritos en el análisis, y lo que había que hacer de inmediato ya se hizo.

Queda una sola pregunta abierta: corregir una falla del análisis 1. Sus tres lecciones debían quedar anotadas como origen de las recomendaciones que complementan (R-2, R-10 y R-18), y no lo hice. Corregirlo es agregar esa referencia en el archivo de recomendaciones. Recomiendo hacerlo dentro de este análisis.

Si responde que sí, lo anoto y el análisis queda listo para aprobar. Si responde que no, el análisis ya está listo como está.

### 28 · Usuario, 2026-10-08 20:17:33
> respondo: necesito respuestas claras casi todo no me sirve. La respuesta debe ser SI o NO y si es no por qué?

**Agente**, 2026-10-08 20:17:41
<!-- agente: d7560663-1dc0-4cd8-ae11-08a42dba9889 -->

NO. Falta una decisión: si se corrige o no una falla del análisis 1.

La falla es esta: el análisis 1 sacó tres lecciones que completan las recomendaciones R-2, R-10 y R-18, pero esas lecciones no quedaron anotadas en el archivo de recomendaciones como origen de cada una.

Si la respuesta es «sí», se corrige en este análisis y queda listo para aprobar. Si es «no», el análisis ya está listo para aprobar como está.

### 29 · Usuario, 2026-10-08 20:22:24
> hágalo: si

**Agente**, 2026-10-08 20:23:19
<!-- agente: 326ebb4b-0a36-4849-a404-62e23401d2ce -->

La corrección quedó hecha. Las tres lecciones del análisis 1 aparecen ahora como origen de las recomendaciones R-2, R-10 y R-18, y el análisis 2 la registra como acuerdo 3.

El análisis 2 ya no tiene preguntas abiertas. Para aprobarlo, escriba:

```
Apruebo el análisis
```

### 30 · Usuario, 2026-10-08 20:24:28
> Apruebo el análisis

**Agente**, 2026-10-08 20:54:47
<!-- agente: fd4f8dd6-2347-44d9-bc48-bc25b9cf80dd -->

El análisis 2 quedó aprobado, así que retomo la HU-001 donde quedó. Primero sumo al plan la migración que faltaba, comprobada con Django.

Las dos migraciones están creadas y Django no pide ninguna más. Ahora escribo las pruebas de la HU-001.

Pasan 594 de 595 pruebas. Falla una del freno sobre capítulos opt-in. Reviso si la causa es mi cambio o si ya fallaba antes.

No hay un catálogo de módulos de Cimiento que nombre sus apps, así que no hay índice que actualizar. Escribo el resultado y la funcionalidad de la fase.

Pongo al día el estado de la fase, el plan, la HU y la épica.

La HU-001 quedó terminada y probada. Ahora diseño la HU-002: el botón «Revisar», la revisión según el lenguaje de cada proyecto y la página con todos los proyectos.

Escribo la HU-002 y abro su fase.

Ahora el código de la HU-002. Primero el campo nuevo, y compruebo que Django pida solo la migración que el plan declara.

Escribo el reconocimiento del lenguaje y la revisión.

Escribo las vistas, las rutas y las dos pantallas.

Agrego la ayuda de las dos pantallas y el enlace «Pruebas» en la lista de proyectos.

Ahora agrego las pantallas nuevas a las pruebas que ya existen (menú, tablas y ayuda) y escribo las pruebas de la HU-002.

Las 25 pruebas de la app pasan. Corro la regresión de las suites que toca la fase.

Apareció otro archivo que el plan no nombra. Antes de detenerme, reviso exactamente qué exige.

Me detuve otra vez por un hallazgo. Ya está anotado como H-3 en el resumen de la sesión y en el estado de la fase.

**Qué pasó.** Cada pantalla nueva de Cimiento tiene que tener su capítulo en el manual de ayuda. El plan de la HU-002 incluyó el menú, las tablas y la ayuda de la pantalla, pero no el manual. Faltan dos archivos: `core/ayuda/secciones.py` y el texto de la sección. La recomendación R-19 del análisis 2 solo cubría los archivos de la base de datos, así que no lo previno.

**Qué quedó hecho en la HU-002:**
- El reconocimiento del lenguaje de cada proyecto.
- La revisión con la herramienta de cada lenguaje.
- La orden de consola.
- La página con todos los proyectos y la página de cada uno.
- El enlace en el menú y en la lista de proyectos.

Sus 25 pruebas pasan.

**Otra falla, ajena a esta épica.** Una prueba de la guía de pantallas falla desde la EP-028. No la toqué. La anoté como H-4, con su pendiente 143 en la EP-028.

**Qué propongo para el análisis 3:**
1. Agregar al plan de la HU-002 los dos archivos del manual.
2. Ampliar la R-19. Antes de escribir un plan, se pregunta qué archivos pide el cambio. Eso incluye las migraciones y también las piezas que las pruebas le exigen a toda pantalla nueva: menú, tablas, ayuda y manual.

Para abrirlo, escriba:

```
Analicemos: el pendiente 141
```

> acá termina la conversación

---

## Lo acordado

1. La HU-001: se agrega a su plan la migración `core/proyectos/migrations/0007_…py` que piden los ajustes nuevos, y la fase sigue donde quedó (turno 26).
2. Que no se repita: antes de escribir el plan de una fase que cambie la base de datos, se le pregunta al marco del proyecto qué archivos va a pedir (en Django, `manage.py makemigrations --dry-run`) y se ponen todos en el plan. Vale para las HU-002 a HU-005 y para toda fase de cualquier proyecto, como recomendación nueva de los análisis (turno 26).

3. Lo que faltó del análisis 1: sus lecciones 1, 2 y 3 (S-350, S-351, S-352) se suman al origen de las recomendaciones R-10, R-2 y R-18, que complementan (turno 29).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `02·F8` (solo se edita lo que el plan declara), `02·F17` (lo que el plan afirma se verifica contra el proyecto real) y `02·F14` Q9 (el plan lista los archivos que crea o modifica). No choca ninguna.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| Los ajustes | `AjusteBase.clave` y `AjusteDelProyecto.clave` (`core/proyectos/models.py`) toman sus opciones del catálogo `AJUSTES`; cambiar el catálogo cambia el campo y pide migración |
| La fase A de la HU-001 | T-01 y T-02 hechas; la app `core/pruebas/` creada sin migraciones; nada corrido |
| Lo que pide Django | `manage.py makemigrations --dry-run` lista dos: `pruebas/0001_inicial.py` (declarada) y `proyectos/0007_…py` (sin declarar) |
| Las HU-002 a HU-005 | Sin plan todavía: sus archivos se declaran al escribirlo |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| Plan de la EP-028·HU-001 | Confirma: el cambio igual declaró su `0006`. Se omitió aquí por no revisar qué pide Django antes de escribir el plan |
| S-274 · Al planear un cambio de reglas no se buscó qué pruebas las leen | El mismo patrón: el plan no buscó qué más cambia con lo que toca |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | Ninguno: el cambio queda en el plan de una fase de Cimiento |
| Normas y leyes | Ninguna |
| Herramientas | Django pide una migración cada vez que cambian las opciones de un campo |

### Dónde más puede pasar

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| La HU-001 | Su fase A | Se queda detenida | Acuerdo 1 |
| Las HU-002 a HU-005 | Sus planes, por escribir | Se detienen igual si cambian un modelo y el plan no lista su migración | Acuerdo 2 |
| Cualquier plan de cualquier proyecto que cambie su base de datos | Las fases futuras, con Django, Laravel o cualquier marco que genere archivos al cambiar la base | El mismo hallazgo en otra épica | Acuerdo 2: la recomendación nueva |

---

## Propuesta final: hallazgo y pendiente V3, épica y HU

### Hallazgo V2. El plan de la EP-029·HU-001 no declara la migración que piden los ajustes nuevos

| Campo | Valor |
|---|---|
| Qué pasó | Al ejecutar la fase A de la EP-029·HU-001, Django pidió una migración de `core/proyectos/` que el plan no declaraba: cambiar el catálogo de ajustes cambia las opciones de un campo de la base. El plan no preguntó qué archivos pedía el cambio antes de escribirse |
| Por qué importa | Lo que el plan no declara no se escribe, y la fase se detiene. Le puede pasar a cualquier plan que cambie la base de datos de cualquier proyecto |

### Pendiente V3. Cimiento revisa qué parte de cada proyecto queda sin pruebas y lo exige desde su configuración

| Campo | Valor |
|---|---|
| De dónde sale | Hallazgo V2 de H-1, según el análisis 1, y hallazgo V2 de H-2: el plan de la EP-029·HU-001 no declara la migración que piden los ajustes nuevos |
| El problema | El mismo de la V2. Además, el plan de la HU-001 tiene que declarar la migración de `core/proyectos/`, y los planes que cambian la base tienen que listar antes todo lo que el marco va a pedir |
| Por qué importa | El de la V2, y que una fase no se detenga por un archivo que se podía prever |

### Épica y HU que salen del análisis

Las mismas de la EP-029: este análisis no crea HU, cambia el plan de la HU-001 y deja una recomendación para las demás.

| Orden | HU | Título | Parte del problema que resuelve | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|---|---|
| 1 | EP-029·HU-001 | La configuración de cada proyecto dice qué tan estricta es la revisión de pruebas y cada cuántos días toca | El plan no declara la migración | Ninguna | Es la que quedó detenida | 2 |

## Lecciones aprendidas

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | Antes de escribir un plan que cambia la base, se le pregunta al marco qué migraciones va a pedir | Falló | S-353 | Nueva R-19 |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Pasar el pendiente a su versión siguiente y el hallazgo H-2 a su V2 | `13·DOC26` | Este análisis, de una y sin fase: `historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/pendiente.md` y `historico-chat/resumenes/2026-10-07/instalar-desde-cimiento-y-pruebas-en-django.md`, hecho el 2026-10-08 |
| 2 | Agregar al plan de la fase A de la HU-001 la migración `core/proyectos/migrations/0007_…py`, verificada con `manage.py makemigrations --dry-run`, y seguir la fase desde T-03 | 1 | EP-029·HU-001 |
| 3 | Agregar la recomendación R-19: antes de escribir el plan de una fase que cambie la base de datos, preguntarle al marco del proyecto qué archivos va a pedir y ponerlos todos en el plan | 2 | Este análisis, de una y sin fase: `plantillas/recomendaciones-del-analisis.md`, hecho el 2026-10-08 |
| 4 | Sumar las lecciones 1, 2 y 3 del análisis 1 al origen de R-10, R-2 y R-18 | 3 | Este análisis, de una y sin fase: `plantillas/recomendaciones-del-analisis.md`, hecho el 2026-10-08 |

## Lo que aporta al análisis principal

**Resultado:** aclara.

**Lo que suma al análisis principal:** antes de escribir el plan de una fase que cambie la base de datos, se le pregunta al marco del proyecto qué archivos va a pedir, y el plan los declara todos.
