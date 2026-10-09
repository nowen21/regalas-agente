# Análisis 1: la consulta de las reglas falla porque `manage.py` se abre con un Python que no tiene el conector de MySQL

> **Aprobado** por el usuario el 2026-10-08, en el turno 35, con la versión 56.8.0. Desde ese momento este análisis no se reescribe.

> Este análisis se redacta aplicando estas reglas.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../../../../../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](../../../../../base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Un análisis aprobado no se reescribe. Si al ejecutar el plan aparece un hallazgo que obliga a tocar algo que el plan no declara, se abre `analisis-2.md`, que trata solo lo que falló y sus implicaciones sobre lo ya hecho. El hallazgo que no obliga a eso no abre análisis: se anota con su pendiente donde pertenece y el plan continúa.

---

## Recomendaciones

Se leyeron las [recomendaciones de Cimiento](../../../../../plantillas/recomendaciones-del-analisis.md); el proyecto no tiene `analisis/recomendaciones.md` propio.

| Recomendación | Cómo se aplica en este análisis |
|---|---|
| R-1 | «Dónde más puede pasar» revisa todo lo que llama a `manage.py`: el aviso de cada sesión, `recuperar.py`, la pantalla de pruebas, quien lo escribe a mano y los proyectos que heredan |
| R-2 | Ya hay dos funciones que buscan el Python de Cimiento: `python_de_cimiento` (`core/herramientas/instalar.py:1081`) y `python_de_la_plataforma` (`core/herramientas/corredor.py:200`). La solución hace lo mismo en `manage.py` |
| R-10 | La solución se explicó con el ejemplo de la caja de herramientas (turno 28) |
| R-19 | El plan declara todo lo que pide el cambio: `manage.py` y su prueba. No hay migraciones |
| Las demás | No aplican: no se cambia ninguna regla (R-3, R-4) y no hay piloto (R-16) |

---

## Hallazgo

### H-4 · La consulta de las reglas falla porque el aviso manda a usar el Python que no tiene el conector de MySQL

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-08, `python manage.py ver_estandar base/01-conducta/palabras-clave.md` terminó con `ModuleNotFoundError: No module named 'MySQLdb'`. El `python` del sistema (3.11, y también 3.13 y 3.14) no tiene el conector; el de Cimiento, `proyectos/cimiento/.venv/Scripts/python.exe`, sí lo tiene y con él la consulta funciona. El aviso de cada sesión manda a usar `python` (`proyectos/cimiento/core/enganches/cargador.py:68`). Además, con el Python de Cimiento las tildes salen dañadas en la consola de Windows |
| Por qué importa | Toda sesión, en cualquier proyecto, recibe la orden de leer las reglas con un comando que falla; sin leerlas, trabaja sin las reglas completas |
| Pendiente | [Pendiente 145: `manage.py` se abre siempre con el Python de Cimiento y escribe bien las tildes](pendiente.md) |

## Pendiente

**De dónde sale:** H-4 · La consulta de las reglas falla porque el aviso manda a usar el Python que no tiene el conector de MySQL.

**El problema.** El aviso de cada sesión manda a leer las reglas con `python "…/proyectos/cimiento/manage.py" ver_estandar <ruta>` (`cargador.py:68`; también `recuperar.py:319`). Ese `python` es el del computador, que no tiene el conector de MySQL, y la consulta falla. Cimiento usa su propio Python 3.11.9, en `proyectos/cimiento/.venv/`, y con ese funciona. Con el Python de Cimiento, las tildes salen dañadas en la consola de Windows. El usuario aprobó la solución el 2026-10-08.

**Por qué importa.** Toda sesión, en cualquier proyecto, recibe la orden de leer las reglas con un comando que falla; sin leerlas, trabaja sin las reglas completas.

---

## Conversación

> La escribe el enganche en tiempo real, turno por turno, desde la transcripción de la sesión. No se escribe a mano.

### 25 · Usuario, 2026-10-08 21:25:09
> respondo: 1 revise

**Agente**, 2026-10-08 21:29:12
<!-- agente: 2a6a594b-cb02-4b6f-9368-ebcfcc812156 -->

Encontré la causa probable: el Python del sistema no tiene el conector de MySQL; el del entorno propio de Cimiento (`.venv`) sí. Lo compruebo.

**La consulta falla porque el aviso manda a usar el Python equivocado.** En este computador hay instalados tres Python (3.11, 3.13 y 3.14), y ninguno tiene la pieza que conecta con la base de datos MySQL. Cimiento tiene su propio Python, `proyectos/cimiento/.venv/Scripts/python.exe`, que sí la tiene, y con ese la consulta funciona.

El aviso que llega al abrir cada sesión dice que se use `python` a secas ([cargador.py:68](../../../../../proyectos/cimiento/core/enganches/cargador.py#L68)), y con eso se termina usando uno de los del sistema. Por eso, en cualquier proyecto, la orden de leer las reglas desde la base falla.

Hay un segundo detalle: con el Python de Cimiento, las tildes salen dañadas en la consola de Windows.

Lo anoté como H-4 en el [resumen de la sesión](../../../../../historico-chat/resumenes/2026-10-08/los-documentos-de-cimiento-pasan-a-su-base.md). Mientras revisaba, volví a escribir un archivo temporal fuera del proyecto y el freno me lo bloqueó. Eso quedó como H-3: no necesita pendiente, porque repetí la consulta sin ese archivo.

**¿Abro un pendiente para corregir el aviso?** Le recomiendo que sí. El arreglo sería que el aviso indique el Python de Cimiento y que las tildes salgan bien.

### 26 · Usuario, 2026-10-08 21:30:19
> pregunta pero cuál es el que se está utilizando en este proyecto no importa revisar cuántas versiones hay instaladas

**Agente**, 2026-10-08 21:30:46
<!-- agente: 456cb513-0e9c-492a-a0f8-7f6ccfbd5145 -->

Cimiento usa **Python 3.11.9**, desde su propio entorno en [proyectos/cimiento/.venv/](../../../../../proyectos/cimiento/.venv/). Ese entorno se armó a partir del Python 3.11 del computador y tiene sus propias librerías, entre ellas el conector de MySQL.

El problema es este:
- El aviso dice que se escriba `python`, y eso abre el Python 3.11 del computador. Es la misma versión, pero no tiene esas librerías, y por eso la consulta falla.
- Con `proyectos/cimiento/.venv/Scripts/python.exe`, la misma consulta funciona.

### 27 · Usuario, 2026-10-08 21:31:40
> pregunta: cuál es la solución ?

**Agente**, 2026-10-08 21:31:56
<!-- agente: 73651dcc-389c-4e65-96d8-40d2e7d1c836 -->

La solución que recomiendo tiene dos partes.

1. **Que `manage.py` busque su propio Python.** Si alguien lo abre con el Python del computador, `manage.py` se vuelve a lanzar solo con el de `proyectos/cimiento/.venv/`. Así el comando del aviso funciona tal como está escrito, y también funciona cualquier otro que llame a `manage.py`, en cualquier proyecto. Es mejor que cambiar el texto del aviso: el aviso no es el único lugar desde donde se llama a `manage.py` (también está [recuperar.py:319](../../../../../proyectos/cimiento/core/herramientas/recuperar.py#L319)), y si se cambia solo el aviso, los demás siguen fallando.
2. **Que la salida se escriba siempre con tildes bien.** `manage.py` le indica a la consola de Windows el formato que conserva las tildes, para que el texto no salga dañado.

Son pocas líneas en un solo archivo, [manage.py](../../../../../proyectos/cimiento/manage.py), más una prueba que lo abre con el Python del computador y verifica que la consulta funcione.

Hoy no lo cubre ningún plan aprobado. Por eso tendría que entrar como pendiente y seguir el camino de siempre.

### 28 · Usuario, 2026-10-08 21:33:20
> respondo: no entiendo la solución 00 id7

**Agente**, 2026-10-08 21:33:32
<!-- agente: 1e809666-699f-4e3f-b298-7b36cfded698 -->

Una comparación: Cimiento es como una cocina que solo funciona con su propia caja de herramientas.

- **El problema:** el aviso dice «use `python`», y eso agarra la caja de herramientas general del computador. A esa caja le falta la herramienta para abrir la base de datos, y por eso la consulta falla.
- **La solución:** que el programa de entrada de Cimiento (`manage.py`) revise con qué caja lo abrieron. Si es la general, se cambia solo a la de Cimiento, que sí tiene esa herramienta. Así funciona siempre, lo llame quien lo llame, y nadie tiene que acordarse de cuál caja usar.
- **Las tildes:** de paso, `manage.py` le dice a la pantalla que escriba las letras con tilde como son, para que no salgan símbolos raros.

Es un cambio pequeño, en un solo archivo, y lleva una prueba que confirma que ya no falla.

### 29 · Usuario, 2026-10-08 21:36:28
> apruebo

**Agente**, 2026-10-08 21:37:58
<!-- agente: ee22d9b4-2b76-4a9c-af55-bc7cfd2dff9a -->

Lo aprobado es la solución. La cadena (`02·F0`) pide que el cambio de código pase primero por un pendiente y su análisis, así que abro el pendiente.

Quedó abierto el [pendiente 145](../../../../../historico-chat/resumenes/2026-10-08/pendientes/145-manage-py-usa-el-python-de-cimiento/pendiente.md), con la solución que aprobó: que `manage.py` se abra siempre con el Python de Cimiento y que las tildes salgan bien. También quedó enlazado desde el hallazgo H-4.

De paso arreglé un enlace del pendiente 142 que se había roto al cambiarle el nombre a la sesión.

Para hacer el cambio en el código, la cadena del estándar pide primero el análisis del pendiente. Ese análisis solo se puede abrir si usted escribe el mensaje que lo prende; yo no puedo prenderlo por mi cuenta. **Escriba «Analicemos: el pendiente 145».** En el análisis queda la solución que ya aprobó, y desde ahí sigo hasta dejarlo funcionando sin volver a pedirle aprobación.

### 30 · Usuario, 2026-10-08 21:39:30
> Analicemos: el pendiente 145

**Agente**, 2026-10-08 21:49:13
<!-- agente: 9dfb94f0-47ec-4c81-bb0d-dc3a191f7ab9 -->

Estoy llenando el análisis con lo encontrado. Antes reviso a qué épica le toca.

Sigo llenando el análisis; lo hago con ediciones directas en el archivo, sin guion.

El análisis quedó escrito en [analisis-1.md](../../../../../historico-chat/resumenes/2026-10-08/pendientes/145-manage-py-usa-el-python-de-cimiento/analisis-1.md).

**Antes de aprobarlo hay que corregir desde dónde copia la conversación.** Se prendió en el turno 30, y la explicación y el «apruebo» de la solución quedaron antes, entre los turnos 25 y 29. Para que entren, hay que escribir «Analicemos: el pendiente 145 desde el turno 25».

**Lo que encontré:**
- Hay dos programas de Cimiento que ya buscan su propio Python: el que lo instala y el que corre las pruebas. `manage.py` es el que no lo hace, y el arreglo consiste en que haga lo mismo que esos dos.
- El arreglo cubre a todos los que llaman a `manage.py`: el aviso de cada sesión, la pantalla de pruebas y quien lo escriba a mano. Si Cimiento todavía no tiene su propio Python, `manage.py` sigue con el que lo abrió.
- Para los proyectos que heredan es un cambio menor: no les pide nada nuevo.

**Queda una decisión: ¿la HU nueva entra en la EP-026?** Esa es la épica de leer el estándar desde la base, y le recomiendo esa.

### 31 · Usuario, 2026-10-08 21:49:36
> apruebo

**Agente**, 2026-10-08 21:51:11
<!-- agente: 5c5e9f41-b78f-4bcf-8aae-a90ce9de3a0a -->

Quedó anotado en el análisis que la HU nueva entra en la EP-026. Con eso ya no queda ninguna decisión abierta.

Faltan dos pasos y los dos dependen de usted:

1. **Escriba «Analicemos: el pendiente 145 desde el turno 25».** Hoy la conversación del análisis empieza en el turno 30. El «apruebo» de la solución fue en el turno 29, así que todavía no quedó copiado en el análisis.
2. **Después, apruebe el análisis completo.** Su «apruebo» de ahora lo tomé como la respuesta sobre la épica, no como aprobación del análisis entero. Cuando lo apruebe, yo hago el resto sin volver a preguntarle: la HU, el plan, el cambio en `manage.py`, la prueba, y el aviso de que ya funciona.

### 32 · Usuario, 2026-10-08 21:52:07
> Analicemos: el pendiente 145 desde el turno 25

**Agente**, 2026-10-08 21:52:42
<!-- agente: aac7dd45-c04b-403f-a8d6-4f0d9e7397ba -->

El análisis ya está prendido desde el turno 25. Por ahora la conversación copiada sigue empezando en el turno 30; lo normal es que el enganche agregue los turnos 25 a 29 cuando termine esta respuesta. En el próximo mensaje reviso que hayan quedado.

**Solo falta que se apruebe el análisis completo:** [analisis-1.md](../../../../../historico-chat/resumenes/2026-10-08/pendientes/145-manage-py-usa-el-python-de-cimiento/analisis-1.md). Con esa aprobación hago la HU en la EP-026, el plan, el cambio en `manage.py` y su prueba, y aviso cuando funcione.

### 33 · Usuario, 2026-10-08 21:53:36
> pregunta: osea que no hay necesidad de analizar nada

**Agente**, 2026-10-08 21:54:35
<!-- agente: 1e102a22-1016-4fd8-8685-0acbb3c7a29b -->

Así es: **no queda nada por analizar.** El análisis ya se hizo entre los turnos 25 y 31:
- se encontró la causa;
- se revisó dónde más puede fallar lo mismo;
- se decidieron la solución y la épica.

Ahora la conversación ya incluye los turnos 25 a 29, donde se aprobó la solución.

Lo único que falta es aprobar el documento del análisis. Esa aprobación es la que deja empezar a construir: la cadena del estándar no permite tocar el código mientras el análisis siga sin aprobar.

### 34 · Usuario, 2026-10-08 21:56:57
> apruebo análisis

**Agente**, 2026-10-08 21:59:31
<!-- agente: bf04731c-f4e0-41ae-88ae-3d5b8dd605ba -->

**El análisis todavía no quedó aprobado.** El programa que pone la marca de aprobado solo reconoce la frase exacta «Apruebo el análisis», y el mensaje decía «apruebo análisis», sin el «el».

Ya revisé que al análisis no le falta nada para aprobarse. **Escriba «Apruebo el análisis».** Con eso hago la HU, el plan, el cambio y la prueba sin volver a preguntarle nada.

### 35 · Usuario, 2026-10-08 22:00:03
> Apruebo el análisis

**Agente**, 2026-10-08 22:07:50
<!-- agente: d12b5d74-744a-4d85-b3d8-17b7c3f87fdd -->

Quedó aprobado. Arranco la cadena: HU en la EP-026, plan, fase, cambio y prueba.

Escribo la HU-011, siguiendo el estilo de la HU-010.

Los enlaces que el validador marcó como rotos ya existen: el andamio acaba de crear la fase. Reviso los documentos de la fase.

Ahora el cambio en `manage.py`.

Estoy revisando por qué el freno no me dejó editar `manage.py`.

**El cambio en `manage.py` no se hizo todavía: el freno lo detuvo, y con razón.** El error fue mío, al escribir el análisis:

- En «Lo que se tiene que hacer» puse «la HU de EP-026 que salga de este análisis», en vez del nombre exacto de la HU, **EP-026·HU-011**. El freno solo deja editar el código cuando el análisis aprobado nombra esa HU.
- Además, al plan le faltaba la versión del estándar en la aprobación. Eso ya lo corregí.

Lo que ya está hecho:
- la HU-011 en la EP-026;
- la fase con su plan de trabajo y su plan de pruebas.

Un análisis aprobado no se vuelve a escribir. Por eso la corrección va en un **análisis 2 del pendiente 145**, que solo cambia ese nombre por **EP-026·HU-011**. Quedó anotado como H-5 en el [resumen de la sesión](../../../../../historico-chat/resumenes/2026-10-08/los-documentos-de-cimiento-pasan-a-su-base.md).

**Escriba «Analicemos: el pendiente 145».** Lo dejo listo para que lo apruebe con «Apruebo el análisis», y después sigo con el cambio y la prueba hasta que funcione.

> acá termina la conversación

---

## Lo acordado

1. La solución: `manage.py` revisa con qué Python lo abrieron y, si no es el de `proyectos/cimiento/.venv/`, se vuelve a abrir solo con ese; y escribe la salida de forma que las tildes salgan bien en la consola de Windows. Lleva una prueba que lo abre con el Python del computador y confirma que la consulta funciona (turno 29).

2. La épica: la HU se suma a la EP-026, porque `ver_estandar` es como se lee el estándar desde la base (turno 31).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `02·F0` (el cambio de código recorre la cadena), `02·F8` (solo se edita lo que el plan declara), `08·T1` (el cambio lleva su prueba) y `00·M13` (lo que viaja a los proyectos que heredan). No choca ninguna.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| `manage.py` | Carga el `.env` y pone el puerto; no revisa con qué Python lo abrieron (`proyectos/cimiento/manage.py`) |
| El Python del computador | 3.11, con Django y PyMySQL pero sin `MySQLdb`: Django falla al cargar el conector de MySQL |
| El Python de Cimiento | `proyectos/cimiento/.venv/`, 3.11.9, con el conector: la consulta funciona |
| Quién lo busca ya | `instalar.py:1081` y `corredor.py:200` buscan el Python de `.venv`; `manage.py` no |
| Pruebas de `manage.py` | Ninguna: nada prueba hoy el arranque ni el puerto |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| `corredor.py:200` (`python_de_la_plataforma`) | Confirma: ya se resolvió lo mismo para correr las pruebas de Cimiento, «el que trae el conector de su base». El acuerdo 1 lo lleva a `manage.py` |
| `instalar.py:1265` | Muestra el otro camino: instalar PyMySQL en el Python que corre los enganches. No alcanza, porque Django busca `MySQLdb` y nada le dice que use PyMySQL |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | PARCHE (`20·M10`): corrige un comando que ya se les exige; no les pide nada nuevo |
| Normas y leyes | Ninguna |
| Herramientas | En Windows, la consola daña las tildes si el programa no le dice que escriba en UTF-8. El `.venv` puede tener su Python en `Scripts/` (Windows) o en `bin/` (Linux y Mac) |

### Dónde más puede pasar

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| El aviso de cada sesión | `cargador.py:68`, en todo proyecto | Ninguna sesión puede leer las reglas | Punto 1: el comando del aviso funciona sin cambiarlo |
| La pista de las reglas que no cupieron | `recuperar.py:319` | La misma falla | Punto 1 |
| La pantalla de pruebas | `core/pruebas/views.py:32` abre `manage.py` con `sys.executable` | Si el servidor corre con otro Python, falla igual | Punto 1 |
| Quien escribe `python manage.py` a mano | La consola de cualquiera | Falla igual | Punto 1 |
| Cimiento sin `.venv` | Una instalación nueva, antes de crear el ambiente | Buscar un Python que no existe | Punto 1: sin `.venv`, sigue con el Python que lo abrió |
| Ya abierto con el Python de Cimiento | El servidor y el vigilante | Volver a abrirse sin necesidad | Punto 1: si ya es ese, no hace nada |

---

## Propuesta final: hallazgo y pendiente, épica y HU

El hallazgo H-4 y el pendiente 145 quedan como están: el análisis no los cambia.

### Épica y HU que salen del análisis

Se suma a la [EP-026: el estándar vive en la base de Cimiento y cada cambio queda versionado](../../../../../documentacion/epicas/EP-026-el-estandar-vive-en-la-base-de-cimiento-y-cada-cambio-queda-versionado/epica.md), porque `ver_estandar` es como se lee el estándar desde la base.

| Orden | HU | Título | Parte del problema que resuelve | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|---|---|
| 1 | La siguiente libre de EP-026 | `manage.py` se abre siempre con el Python de Cimiento y escribe bien las tildes | El aviso manda a leer las reglas con un comando que falla | Ninguna | Es la única | 1 (acuerdos 1 y 2) |

## Lecciones aprendidas

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | Antes de poner un comando en un aviso, correrlo como lo va a correr quien lo lee | Falló | Se escribe al aprobar | Complementa R-12 |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | `manage.py` revisa con qué Python lo abrieron; si no es el de `.venv` y ese existe, se vuelve a abrir con él y con los mismos argumentos; escribe la salida en UTF-8; y una prueba lo abre con el Python del computador y confirma que `ver_estandar` responde sin error y con las tildes bien | 1 | La HU de EP-026 que salga de este análisis |

## Lo que aporta al análisis principal

**Resultado:** aclara.

**Lo que suma al análisis principal:** Todo comando de Cimiento se abre con el Python de Cimiento, lo llame quien lo llame, para que la lectura del estándar desde la base no dependa de qué Python tenga el computador.
