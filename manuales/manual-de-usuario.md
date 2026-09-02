# Manual de uso — Cimiento

---

## 1. Información general del documento

| Campo | Valor |
|---|---|
| Nombre del sistema | Cimiento |
| Código o identificador | `cimiento` |
| Versión del sistema | 5 |
| Versión del cuerpo de reglas | 37.2.2 |
| Versión del manual | 1 |
| Fecha de elaboración | 2026-09-02 |
| Fecha de actualización | 2026-09-02 |
| Responsable | Ing. José Dúmar Jiménez Ruíz |
| Estado del documento | BORRADOR |
| Dirigido a | Quien use la plataforma. Este manual no supone conocimiento previo |

---

## 2. Introducción

**¿Qué es el sistema?**

Cimiento son dos cosas que trabajan juntas:

1. **Un cuerpo de reglas** escritas en archivos de texto: 257 reglas que dicen cómo se documenta y se construye un proyecto.
2. **Una plataforma** que se abre en el navegador y administra esas reglas y los proyectos que las usan.

**¿Para qué sirve?**

Para que el estado de un proyecto no dependa de que alguien lo recuerde. Todo lo que Cimiento muestra sale de los documentos del propio proyecto: si el documento cambia, la pantalla cambia.

**¿Qué necesidad resuelve?**

Un proyecto documentado tiene cientos de archivos. Nadie los lee todos. Preguntas como *«¿en qué va esa fase?»*, *«¿esto ya se comprobó?»* o *«¿quién aprobó este documento y sobre qué texto?»* se responden hoy abriendo archivos uno por uno. Cimiento las responde de una.

**¿Quiénes lo utilizan?**

Quien escribe o revisa la documentación de un proyecto. También el agente de inteligencia artificial que trabaja sobre él, que recibe de la plataforma las reglas que debe seguir.

**¿Qué procesos pueden realizarse?**

- Conectar un proyecto y traer lo que ya tenga escrito.
- Ver en qué estación va cada fase de trabajo y qué le falta.
- Ver qué funcionalidades están comprobadas y cuáles no.
- Registrar quién aprobó un documento, y enterarse cuando ese documento cambie.
- Ver lo que el agente recuerda del proyecto.
- Armar el expediente completo del proyecto y generar su entregable.
- Escribir, numerar y derogar reglas del estándar.

---

## 3. Objetivo del manual

**Objetivo:** explicar cómo se pone a andar Cimiento y cómo se usa cada una de sus pantallas y órdenes, sin suponer conocimiento previo.

**Al terminar de leerlo se puede:**

- Poner a andar la plataforma en una máquina.
- Conectar un proyecto y traer sus documentos.
- Leer las cinco pantallas de consulta y entender qué dice cada número.
- Ejecutar las órdenes que cambian algo: abrir una fase, llenar un espacio, aprobar un documento.
- Reconocer las fallas más frecuentes y saber qué hacer con cada una.

---

## 4. Alcance

**Lo que este manual cubre:** el uso de la plataforma y de sus órdenes de consola.

**Lo que no cubre:**

- **Cómo instalar Python o Git.** Se supone que ya están en la máquina.
- **El contenido de las 257 reglas.** Esas viven en la carpeta `base/` del repositorio y se leen ahí.
- **Cómo se programó la plataforma.** Eso está en el [manual técnico y de operación](../cvds/despliegue/manual-tecnico-y-de-operacion.md).

---

## 5. Conceptos básicos

Estos términos aparecen en todas las pantallas. Se explican una vez acá.

| Término | Qué quiere decir |
|---|---|
| **Proyecto** | Una carpeta con código y documentos, que Cimiento observa. Cimiento **nunca modifica el código**; solo lee y escribe documentos |
| **Conectar un proyecto** | Decirle a la plataforma dónde vive esa carpeta. No copia ni mueve nada: anota la ruta |
| **Traer** | Copiar los documentos del proyecto a la plataforma para poder consultarlos. La copia se rehace cuando se quiera |
| **Épica** | Un bloque grande de trabajo. Se identifica `EP-001`, `EP-002`... |
| **Historia de usuario** | Una parte de una épica, escrita como lo que alguien necesita. Se identifica `HU-001`, `HU-002`... |
| **Fase** | El trabajo concreto que construye una historia. Se llama, por ejemplo, `A-EP-009-HU-001-la-constancia-va-antes-que-el-efecto`: la letra dice el orden, y el resto dice de qué historia cuelga |
| **Estación** | Cada uno de los trece pasos por los que pasa una fase, del análisis al despliegue |
| **Puerta** | Lo que hay que cumplir para pasar de una estación a la siguiente |
| **Veredicto** | Lo que la fase declara al terminar sus pruebas: *Cumple* o *No cumple* |
| **Funcionalidad** | Algo que el sistema hace. Se identifica `F-001`, `F-002`... |
| **Espacio por llenar** | Una marca `«…»` dentro de un documento. Señala algo que falta escribir |
| **Señal** | Algo que se aprendió y no se puede deducir leyendo el código. Se guardan en `documentacion/senales.md` |
| **Deuda** | Trabajo declarado que todavía no se hizo. Cimiento la muestra en vez de esconderla |

---

## 6. Requisitos para utilizar el sistema

| Requisito | Detalle | Cómo se comprueba |
|---|---|---|
| Python 3.11 o superior | El lenguaje en que está escrita la plataforma | Escribir `python --version` en la consola |
| Django | La biblioteca web que usa | Se instala con los pasos del punto 7 |
| Un navegador | Cualquiera | — |
| Internet | **Solo una vez**, para traer los archivos de apariencia | Después funciona sin conexión |

**No hace falta** ninguna base de datos aparte, ningún servidor, ninguna cuenta y ninguna contraseña.

---

## 7. Acceso al sistema

### 7.1 La primera vez

Se abre una consola, se entra a la carpeta `plataforma` del repositorio y se escriben estas órdenes, una por una:

```
cd plataforma
pip install -r requirements/base.txt
cp .env.example .env
python descargar_estaticos.py
python manage.py migrate
```

Qué hace cada una:

| Orden | Qué hace | Qué se ve si sale bien |
|---|---|---|
| `cd plataforma` | Entra a la carpeta de la plataforma | La consola cambia de carpeta |
| `pip install -r requirements/base.txt` | Instala Django | Varias líneas y al final `Successfully installed` |
| `cp .env.example .env` | Crea el archivo de ajustes de esta máquina | Nada. Se puede comprobar con `dir .env` |
| `python descargar_estaticos.py` | **Lo único que sale a internet.** Trae los archivos de apariencia | Ocho líneas que dicen `traído`, y al final `Listo: 8 descargado(s)` |
| `python manage.py migrate` | Crea el archivo donde la plataforma guarda su índice | Varias líneas terminadas en `OK` |

**Si `descargar_estaticos.py` falla diciendo `HUELLA DISTINTA`:** el archivo que llegó no es el esperado. No se escribió nada. Se vuelve a intentar; si sigue fallando, hay que revisar la conexión.

### 7.2 Elegir el puerto

El **puerto** es el número por el que se llega a la plataforma en el navegador. Se escribe en el archivo `.env`, que se creó en el paso anterior. Se abre con cualquier editor de texto y se deja así:

```
PUERTO=8015
```

**Por qué importa.** En una máquina pueden estar corriendo varias aplicaciones, y cada una necesita su propio número. Si el número ya está tomado por otra, la plataforma no arranca. El 8000 es el número de fábrica; si está ocupado, se cambia por otro, por ejemplo 8015.

### 7.3 Ponerla a andar

Cada vez que se quiera usar:

```
cd plataforma
python manage.py runserver
```

Se ve algo así:

```
Starting development server at http://127.0.0.1:8015/
Quit the server with CTRL-BREAK.
```

Se abre el navegador en esa dirección: **`http://127.0.0.1:8015/`**.

**Para cerrarla:** se oprime `Ctrl` y `C` a la vez en la consola donde quedó corriendo.

### 7.4 Si algo sale mal al arrancar

| Qué se ve | Qué está pasando | Qué se hace |
|---|---|---|
| `That port is already in use` | Otra aplicación tiene ese número | Cambiar `PUERTO` en el `.env` por otro |
| **La página abre pero no muestra los cambios** | **Quedó corriendo una versión anterior con ese mismo número** | Cerrar todas las consolas donde esté corriendo y volver a arrancar |
| Las letras y los colores no se ven | No se corrió `descargar_estaticos.py` | Correrlo |
| `ModuleNotFoundError: No module named 'django'` | Falta instalar Django | Correr `pip install -r requirements/base.txt` |

---

## 8. Interfaz principal

Todas las pantallas tienen la misma forma:

- **Menú lateral, a la izquierda.** Arriba las opciones que valen para todos los proyectos: *Proyectos* y *Tablero*. Debajo, al entrar a un proyecto, aparecen sus seis pantallas. La que se está viendo queda resaltada.
- **Barra de arriba.** A la izquierda, el botón de tres rayas esconde o muestra el menú. A la derecha, el círculo mitad claro mitad oscuro cambia entre modo claro y modo oscuro; la elección se recuerda.
- **Título de la pantalla**, y debajo el contenido.
- **Tarjetas de cifra** en varias pantallas: cuadros de color con un número grande, para ver de un vistazo.

**Lo que hay que saber leer:** los cuadros de color con borde no son errores.

| Color | Qué quiere decir |
|---|---|
| Verde | Está bien |
| Amarillo | Hay algo que mirar, sin urgencia |
| Gris | **No se sabe.** No es lo mismo que cero |
| Rojo | Algo no cumple |
| Recuadro con borde punteado | No hay nada que mostrar, y debajo dice por qué |

**Una pantalla vacía no es una falla.** Cimiento nunca deja una pantalla en blanco: siempre explica por qué no hay nada.

---

## 9. Roles y permisos

**No hay.** Cimiento no tiene usuarios, ni contraseñas, ni permisos. Corre en la máquina de quien lo usa y confía en quien lo abre.

Esto tiene una consecuencia que conviene saber: cuando una orden pide `--quien "Nombre"`, ese nombre **se escribe y no se comprueba**. Sirve para dejar constancia, no para autenticar a nadie.

---

## 10. Módulos del sistema

### 10.1 Proyectos — la pantalla de entrada

**Dónde:** `http://127.0.0.1:8015/`, o *Proyectos* en el menú.

**Qué muestra:** una tabla con los proyectos conectados. De cada uno: cómo se llama, dónde vive su código, qué versión de reglas declaró y en qué estado está.

**Qué se puede hacer:**

**Conectar un proyecto.** Debajo de la tabla hay un formulario con dos casillas:

1. En *Cómo se llama* se escribe un nombre, por ejemplo `Tienda en línea`.
2. En *Dónde vive su código* se escribe la ruta de la carpeta, por ejemplo `c:\proyectos\tienda`.
3. Se oprime **Conectar**.

Si la carpeta no existe, la plataforma lo dice y no conecta nada. Conectar **no toca nada dentro de la carpeta**: solo anota dónde está.

**Entrar a un proyecto.** Se hace clic en su nombre.

### 10.2 Tablero — cómo van todos

**Dónde:** *Tablero* en el menú.

**Qué muestra, en dos partes.**

Arriba, **cómo va cada proyecto**, con cuatro columnas:

| Columna | Qué mide |
|---|---|
| **Avance** | Fases con las trece estaciones pasadas, sobre el total de fases. **No mide funcionalidad entregada: mide fases cerradas** |
| **Deuda** | Avisos vivos: fases detenidas, historias sin fase y funcionalidades construidas sin verificar |
| **Vencida** | De esa deuda, la parte que lleva más de 30 días sin moverse |
| **Sin fecha** | Fases sin cerrar que no dicen desde cuándo llevan quietas |

Esa misma tabla sale impresa debajo, en la pantalla. **No se toma de este manual: viaja con los datos**, para que nadie tenga que buscar qué significa una columna.

**Si un proyecto dice «sin datos» en avance**, no es que vaya mal: es que no tiene ninguna fase escrita y no hay con qué calcular.

**Sobre «vencida»:** los 30 días son un número puesto en la plataforma. **El estándar nunca le puso fecha a una deuda**, así que no es un vencimiento acordado con nadie.

Abajo, **lo que se salió de lo acordado**: una fila por aviso, con qué lo disparó y en qué archivo mirar. Hay tres clases:

| Clase | Cuándo aparece |
|---|---|
| **fase detenida** | Una fase sin cerrar que lleva más de 30 días sin tocarse |
| **historia sin fase** | Una historia escrita sin ninguna fase que la construya |
| **terminado sin comprobar** | Una funcionalidad construida que sigue sin verificarse |

**Son tres y no más, a propósito.** Demasiados avisos se vuelven ruido, y el ruido se ignora completo.

Si no hay ninguno, sale un cuadro verde: *Nada se salió de lo acordado*.

### 10.3 En qué va cada fase

**Dónde:** dentro de un proyecto, *En qué va cada fase*.

**Qué muestra:** todas las fases del proyecto, **de la menos avanzada a la más avanzada**. Se ordenan así porque lo primero que hay que mirar es lo que lleva más tiempo sin moverse.

De cada fase: su nombre, en qué estación va, qué le falta para pasar a la siguiente, y cuántos días lleva sin tocarse.

**Los avisos de arriba explican tres cosas que suelen confundir:**

1. **«Usan una tabla que no es la de trece estaciones».** Las fases viejas se escribieron con otro modelo, de once estaciones o menos. **No se reescriben**, y su número de estación no se compara con el de las demás.
2. **«Tienen alguna estación sin marcar».** El documento cuenta con palabras qué pasó con esa estación en vez de marcarla. **Eso no es lo mismo que estar pendiente**: es que no se sabe.
3. **«Dicen ir en una estación distinta de la que marca su tabla».** El documento se contradice a sí mismo. **Manda la tabla**, porque es la que se marca al hacer el trabajo.

**Botón *Ver solo las abiertas*:** esconde las fases que ya pasaron las trece estaciones.

### 10.4 Qué está comprobado

**Dónde:** dentro de un proyecto, *Qué está comprobado*.

**Qué muestra:** cada funcionalidad del proyecto con uno de tres estados, y de dónde sale ese estado.

| Estado | Qué quiere decir |
|---|---|
| **verificado** | La fase que la construyó cerró con veredicto *Cumple* |
| **no cumple** | Se comprobó y salió mal |
| **sin verificar** | **Nadie comprobó.** No es lo mismo que «no cumple» |

**Una advertencia que la pantalla repite, y conviene tomar en serio:** *verificada* quiere decir que la fase que la construyó declaró sus pruebas en verde. **No quiere decir que alguien de afuera la haya auditado.**

### 10.5 Qué está aprobado

**Dónde:** dentro de un proyecto, *Qué está aprobado*.

**Qué muestra:** los documentos que tienen alguna aprobación registrada, con tres estados posibles:

| Estado | Qué quiere decir |
|---|---|
| **Aprobado** | El documento sigue siendo exactamente el que se aprobó |
| **La aprobación caducó** | **El texto cambió después de aprobarse.** Se dice cuántos caracteres |
| **Sin aprobación** | Nadie lo ha aprobado |

**Por qué esto importa.** Una marca de aprobación escrita a mano dice quién y cuándo, pero no **sobre qué texto**. El documento puede cambiar tres veces y la marca sigue igual. Cimiento guarda una huella del texto aprobado, y cuando el texto cambia, lo dice.

**La pantalla dice qué deja por fuera:** solo salen los documentos con alguna aprobación registrada. **No son todos los del proyecto.**

**Aprobar no se hace desde la pantalla**, sino con una orden de consola (punto 11.3). Es a propósito: aprobar es un cambio de estado y va con su confirmación.

### 10.6 Qué recuerda el agente

**Dónde:** dentro de un proyecto, *Qué recuerda el agente*.

**Qué muestra:** los recuerdos guardados del proyecto. Un **recuerdo** es algo que se decidió o se aprendió y que conviene que el agente sepa la próxima vez. Viven como archivos de texto en `historico-chat/memory/` y viajan con el proyecto.

De cada uno: su título, si vale hoy, y en qué archivo está.

**Lo dado de baja también sale**, en gris. No se borra: sigue siendo la respuesta a por qué algo se hizo como se hizo; lo que cambia es que deja de entregársele al agente.

**Casilla de búsqueda:** escribe una palabra y muestra los recuerdos que la traen.

### 10.7 Traer lo escrito

**Dónde:** dentro de un proyecto, *Traer lo escrito*.

**Qué hace:** copia los documentos del proyecto a la plataforma, para poder consultarlos.

**Cuándo se hace:** la primera vez, y **cada vez que el proyecto cambie**. Si no se hace, las pantallas responden sobre una copia vieja.

**Cómo se nota que hace falta:** el expediente reporta documentos faltantes que sí existen. Si eso pasa, se trae de nuevo.

Después de traer, la plataforma escribe un reporte con lo que no reconoció. Se ve en *Ver qué no entró en cada traída*, dentro de la ficha del proyecto.

---

## 11. Órdenes de consola

Todo lo que **cambia algo** se hace por consola, no desde la pantalla. Es a propósito: un cambio de estado va con su confirmación, y una pantalla con botones sería media confirmación.

Todas se escriben desde la carpeta `plataforma`, con la plataforma corriendo o no.

### 11.1 Abrir una fase

```
python manage.py abrir_fase <proyecto> S EP-019 HU-001 "de qué trata"
```

Crea la carpeta de la fase con sus cinco documentos, tomados del molde del estándar.

- `<proyecto>` es el identificador del proyecto, el que sale en la dirección del navegador.
- `S` es la letra de la fase: A la primera, B la segunda, y así.
- `EP-019` y `HU-001` son la épica y la historia de las que cuelga.
- Lo último, entre comillas, describe de qué trata.

**El nombre lo arma la plataforma.** No se escribe a mano.

**Si la historia no existe, no se abre nada** y se dice por qué. **Si la fase ya existe, no se toca**: puede tener trabajo escrito.

Para ver dónde quedaría sin crear nada, se agrega `--donde-iria` al final.

### 11.2 Llenar un espacio de un documento

Primero se mira qué le falta:

```
python manage.py que_le_falta <proyecto> --documento documentacion/x/spec.md
```

Muestra la lista de espacios `«…»` con el número de línea y su contexto.

Después se llena uno:

```
python manage.py llenar_hueco <proyecto> documentacion/x/spec.md --numero 1 --texto "lo que va"
```

`--numero 1` es siempre **el primero de los que quedan**: al llenar uno, el siguiente pasa a ser el 1.

**Se escribe en el archivo del proyecto**, no en la copia. Nada más del documento se toca.

### 11.3 Aprobar un documento

```
python manage.py aprobar <proyecto> documentacion/x/spec.md --quien "Nombre Apellido"
```

Guarda quién aprobó, cuándo, y **una huella del texto exacto**. Desde ese momento, si el documento cambia, la aprobación caduca.

Para ver el estado de todos:

```
python manage.py aprobaciones <proyecto>
```

### 11.4 Escribir y consultar recuerdos

```
python manage.py memoria <proyecto>
python manage.py memoria <proyecto> --buscar palabra
python manage.py memoria <proyecto> --corregir nombre-del-recuerdo --texto "lo nuevo"
python manage.py memoria <proyecto> --dar-de-baja nombre-del-recuerdo
```

**Corregir conserva lo que decía antes**, escrito debajo. **Dar de baja no borra**: marca el recuerdo.

### 11.5 Elegir qué reglas rigen

```
python manage.py que_rige <proyecto>
python manage.py que_rige <proyecto> --encender DOC5 --cuando 2026-09-02
python manage.py que_rige <proyecto> --apagar DOC5 --cuando 2026-09-02
```

De las 257 reglas del estándar, **49 son opcionales** y se pueden encender o apagar por proyecto. Las demás rigen siempre.

**Intentar apagar una obligatoria no se hace, y se dice por qué:** apagarla volvería el estándar una sugerencia.

### 11.6 Armar el expediente

```
python manage.py armar_expediente <proyecto>
python manage.py generar_entregable <proyecto>
```

El primero agrupa todos los documentos y dice qué falta y qué está a medio llenar. El segundo produce el archivo para entregar.

### 11.7 Comprobar

```
python manage.py comprobar <proyecto>
python manage.py estado_funcionalidades <proyecto>
python manage.py puerta_de_publicacion <proyecto>
```

`comprobar` corre los validadores del estándar sobre el proyecto. `estado_funcionalidades` dice cuáles están verificadas. `puerta_de_publicacion` responde si se puede publicar.

### 11.8 Consultar lo registrado

```
python manage.py buscar_en_la_auditoria <proyecto>
python manage.py buscar_en_la_auditoria <proyecto> --desde 2026-08-01 --hasta 2026-09-02
python manage.py buscar_en_lo_conversado "una frase"
python manage.py correcciones_que_se_repiten
python manage.py cuanto_se_revisa --por-mes
```

La última mide cuánto tiempo se gasta revisando, sacado de las horas que ya quedan escritas. **Nadie tiene que anotar nada.**

### 11.9 Rehacer lo que se borre

```
python manage.py reconstruir_traido
python manage.py reconstruir_proyectos
python manage.py indexar_conversaciones
```

**Casi todo lo que la plataforma guarda es un índice que se rehace.** La única excepción son las aprobaciones: quién aprobó y sobre qué texto no está escrito en ningún documento, y por eso no se puede reconstruir.

---

## 12. Búsquedas y filtros

| Dónde | Qué se filtra | Cómo |
|---|---|---|
| Fases | Solo las abiertas | Botón *Ver solo las abiertas* |
| Memoria | Por palabra | Casilla *Buscar una palabra* |
| Auditoría | Por proyecto, fechas y tipo de acción | Orden `buscar_en_la_auditoria` |
| Conversaciones | Por frase | Orden `buscar_en_lo_conversado` |

**Cuando una búsqueda no encuentra nada, lo dice con palabras.** No devuelve una lista vacía, porque un vacío se ve igual que una falla.

---

## 13. Reportes

| Reporte | Dónde | Qué responde |
|---|---|---|
| Tablero | Pantalla | Cómo va cada proyecto y qué se desvió |
| Estado de funcionalidades | Pantalla y consola | Qué está comprobado |
| Expediente | Consola | Qué documentos hay, cuáles faltan y cuáles están a medio llenar |
| Correcciones repetidas | Consola | Qué se ha tenido que corregir más de una vez |
| Tiempo de revisión | Consola | Cuánto se gasta revisando, mes a mes |

**Sobre el tiempo de revisión, una advertencia que sale impresa cada vez:** la comparación usa como punto de partida el tramo más viejo que quedó grabado. **No es un «antes» de verdad** — la medición inicial debió tomarse antes de empezar el proyecto y no se tomó.

---

## 14. Exportación de información

`python manage.py generar_entregable <proyecto>` produce el expediente en un archivo que se puede abrir fuera de la plataforma. Queda en `plataforma/datos/proyectos/<proyecto>/entregable/`.

---

## 15. Notificaciones y mensajes del sistema

Cimiento **no envía correos ni notificaciones**. Todo lo que tiene que decir lo dice en la pantalla o en la consola.

Cómo se leen sus mensajes:

| Forma | Qué quiere decir |
|---|---|
| Cuadro verde | Todo bien |
| Cuadro amarillo | Algo que mirar |
| Cuadro gris | Una aclaración sobre lo que se está viendo |
| Recuadro punteado | No hay nada que mostrar, y dice por qué |
| `No se hizo: ...` en consola | La orden se rechazó, y a continuación dice el motivo |

**Ningún mensaje dice solo que algo falló.** Todos dicen qué falló y qué se hace.

---

## 16. Validaciones y errores frecuentes

| Mensaje | Qué pasó | Qué se hace |
|---|---|---|
| `No se abrió: no existe la historia HU-00X` | Se intentó abrir una fase de una historia que no está escrita | Escribir primero la historia |
| `No se abrió: la fase ... ya existe` | Ya hay una fase con ese nombre | Revisar la que está; no se pisa porque puede tener trabajo |
| `No se hizo: F0 no es opcional` | Se intentó apagar una regla obligatoria | No se puede. Solo las 49 marcadas como opcionales |
| `Ese documento no está traído` | La copia no tiene ese archivo | Traer el proyecto de nuevo |
| `El proyecto X no está conectado` | El identificador está mal escrito | Mirar el que sale en la dirección del navegador |
| `Esa carpeta ya no está` | La carpeta del proyecto se movió o se borró | Corregir la ruta desde la ficha del proyecto |
| Caracteres raros en la consola | La consola de Windows no muestra tildes | No es una falla: el texto está bien, solo se ve mal |

---

## 17. Flujos completos de operación

### 17.1 Empezar con un proyecto nuevo

1. Abrir `http://127.0.0.1:8015/`.
2. Llenar el formulario *Conectar un proyecto* con el nombre y la ruta. Oprimir **Conectar**.
3. Entrar al proyecto haciendo clic en su nombre.
4. Ir a *Traer lo escrito* y traerlo.
5. Volver al menú y mirar *En qué va cada fase* y *Qué está comprobado*.

**Al principio casi todo va a estar vacío, y cada pantalla lo explica.** Eso es normal en un proyecto recién conectado.

### 17.2 Trabajar una fase de principio a fin

1. Abrirla: `python manage.py abrir_fase <proyecto> A EP-001 HU-001 "de qué trata"`.
2. Llenar sus documentos, con `que_le_falta` y `llenar_hueco`.
3. Marcar a mano las estaciones en el archivo `estado-fase.md` a medida que se cumplen.
4. Consultar la puerta: `python manage.py puerta_de_fase <proyecto> --fase <nombre>`.
5. Al cerrar, mirarla en *En qué va cada fase*.

### 17.3 Aprobar un documento y enterarse cuando cambie

1. Aprobar: `python manage.py aprobar <proyecto> <documento> --quien "Nombre"`.
2. Mirar *Qué está aprobado*: aparece en verde.
3. Editar el documento, aunque sea una coma.
4. Volver a mirar: **la aprobación aparece caducada**, y dice cuántos caracteres cambiaron.

### 17.4 Revisar cómo va todo, una vez por semana

1. Abrir el *Tablero*.
2. Leer los avisos, de arriba hacia abajo: están ordenados por lo que más duele.
3. De cada uno, abrir el archivo que dice la columna *Dónde mirar*.

---

## 18. Casos de uso frecuentes

| Pregunta | Dónde se responde |
|---|---|
| ¿En qué va esa fase? | *En qué va cada fase* |
| ¿Esto ya se comprobó? | *Qué está comprobado* |
| ¿Quién aprobó este documento? | *Qué está aprobado* |
| ¿Qué se decidió sobre esto? | *Qué recuerda el agente* |
| ¿Qué está atrasado? | *Tablero* |
| ¿Qué le falta a este documento? | `que_le_falta` |
| ¿Ya se puede entregar? | `armar_expediente` |
| ¿Qué he tenido que corregir varias veces? | `correcciones_que_se_repiten` |

---

## 19. Preguntas frecuentes

**¿Cimiento modifica el código de mis proyectos?**
No. Lee documentos y escribe documentos. El código no se toca nunca.

**¿Qué pasa si borro la carpeta `datos` o el archivo `indice.sqlite3`?**
Casi nada: son índices y se rehacen con las órdenes del punto 11.9. **Lo único que no se recupera son las aprobaciones**, porque quién aprobó no está escrito en ningún documento.

**¿Puedo usarla sin internet?**
Sí, después de correr `descargar_estaticos.py` la primera vez.

**¿Por qué no puedo aprobar desde la pantalla?**
Porque aprobar es un cambio de estado, y esos van con su confirmación. Poner un botón sería media confirmación.

**¿Por qué dice «sin datos» en vez de cero?**
Porque no es lo mismo. Cero dice «va mal»; sin datos dice «no se sabe».

**¿Por qué hay fases que dicen usar otra tabla?**
Porque se escribieron con un modelo anterior. No se reescriben: una fase cerrada se lee como quedó.

**¿La plataforma se puede poner en un servidor para que la usen varias personas?**
No hoy. Corre en una máquina, sin usuarios ni permisos.

---

## 20. Buenas prácticas de uso

- **Traer el proyecto antes de mirar sus pantallas.** Si no, se responde sobre una copia vieja.
- **Mirar el tablero antes de planear.** Suele haber trabajo empezado que nadie retomó.
- **Aprobar un documento apenas se acuerde**, no después. La huella se toma del texto de ese momento.
- **No dejar la plataforma corriendo en varias consolas.** La vieja responde por la nueva y no hay ningún error que lo diga.
- **Leer las frases en gris.** Ahí está lo que la pantalla no muestra.

---

## 21. Soporte y atención de incidentes

**No hay soporte, y decirlo es parte del manual.** Cimiento lo mantiene una sola persona; no hay turnos, ni guardia, ni nadie a quien escribirle.

Lo que sí hay:

| Si pasa esto | Dónde mirar |
|---|---|
| Una falla al arrancar | El punto 7.4 de este manual |
| Un mensaje que no se entiende | El punto 16 |
| Un comportamiento raro | La [bitácora de operación](../cvds/mantenimiento/bitacora-de-operacion.md) |
| Una duda de cómo está hecho | El [manual técnico](../cvds/despliegue/manual-tecnico-y-de-operacion.md) |

---

## 22. Glosario

Los términos están explicados en el punto 5 de este manual.

---

## 23. Historial de cambios del manual

| Versión | Fecha | Qué cambió |
|---|---|---|
| 1 | 2026-09-02 | Primera versión. Escrita sobre la plataforma andando, comprobando cada orden y cada pantalla |

---

## 24. Anexos

**Lo que este manual no promete.** Cimiento está construido y probado, pero **casi no se ha usado**: un solo proyecto conectado —su propio repositorio—, ninguna aprobación registrada y diez acciones en la auditoría. Que todo lo de acá funcione está comprobado; que sirva en el día a día de un proyecto ajeno, todavía no.

**Documentos relacionados:**

- [Manual técnico y de operación](../cvds/despliegue/manual-tecnico-y-de-operacion.md)
- [Notas de versión](../cvds/despliegue/notas-de-version.md)
- [Acta de entrega](../cvds/despliegue/acta-de-entrega.md)
- [Plan de mantenimiento](../cvds/mantenimiento/plan-de-mantenimiento.md)
