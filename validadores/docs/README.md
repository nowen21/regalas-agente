# Cómo funciona por dentro cada archivo de `validadores/`

Hay **un documento por cada archivo** de `validadores/`. Cada uno cuenta qué hace ese archivo, qué guarda adentro, qué se le entrega y qué retorna cada una de sus funciones, a quién necesita y quién lo necesita a él.

Todo salió de leer el código, no de suponerlo.

Antes de empezar, dos palabras que aparecen todo el tiempo:

- **Validador:** un programa chico que revisa una cosa y avisa si está mal. Acá hay uno por tema.
- **Hallazgo:** cada cosa que un validador encontró mal, con el archivo y la línea donde está.

## Cómo encontrar lo que busca

El nombre del documento es el nombre del archivo. Para entender `secretos.py`, abra [secretos.md](secretos.md).

### Piezas base

Las usan casi todos los demás.

| Archivo | Documentación | Qué hace |
|---|---|---|
| `comun.py` | [comun.md](comun.md) | Guarda lo que todos comparten: cómo se anota un hallazgo, qué tan grave es y cómo se leen los archivos de texto. |
| `codigo.py` | [codigo.md](codigo.md) | Abre los archivos de código del proyecto y los va pasando de a uno, con su nombre y su contenido. |
| `versionado.py` | [versionado.md](versionado.md) | Le pregunta a git qué archivos está guardando y marca los que no deberían estar ahí. |

Git es el programa que guarda la historia del proyecto: qué archivo cambió, cuándo y quién lo cambió.

### Instalación y versiones

| Archivo | Documentación | Qué hace |
|---|---|---|
| `instalar.py` | [instalar.md](instalar.md) | Deja el agente instalado y funcionando en un proyecto con una sola línea. |
| `checklist.py` | [checklist.md](checklist.md) | Revisa qué le falta al proyecto para estar completo. |
| `versiones.py` | [versiones.md](versiones.md) | Le pone una marca a cada documento copiado del estándar y avisa cuando quedó viejo. |
| `version.py` | [version.md](version.md) | Compara la versión del estándar con la que dice usar el proyecto. |
| `sesion.py` | [sesion.md](sesion.md) | Al empezar a trabajar, revisa si el estándar quedó bien puesto. |
| `cargador.py` | [cargador.md](cargador.md) | Arma el texto de las reglas que se le entrega al agente cuando arranca. |

### Memoria e histórico

| Archivo | Documentación | Qué hace |
|---|---|---|
| `historico.py` | [historico.md](historico.md) | Escribe la conversación en `historico-chat/`, para que no se pierda cuando el chat se borre. |
| `recuerdos.py` | [recuerdos.md](recuerdos.md) | Trae al repositorio lo que el agente tiene que recordar de una sesión a otra. |

### Revisan este repositorio (el estándar)

| Archivo | Documentación | Qué revisa |
|---|---|---|
| `enlaces.py` | [enlaces.md](enlaces.md) | Enlaces que no llevan a ninguna parte e índices a los que les falta algo. |
| `citas.py` | [citas.md](citas.md) | Que cada regla nombrada traiga su enlace. También se los pone. |
| `plantillas.py` | [plantillas.md](plantillas.md) | Un documento contra el molde del que salió, para ver si quedó algo sin llenar. |
| `commits.py` | [commits.md](commits.md) | El mensaje con que se guarda un cambio en git. |

### Revisan la documentación de un proyecto

Antes de escribir código, el trabajo se planea por escrito. Lo grande es una **épica**; adentro van las **historias de usuario** (una necesidad concreta de quien va a usar el sistema, se abrevia **HU**); y adentro de cada una, las **fases**, que son los pedazos en que se hace.

| Archivo | Documentación | Qué revisa |
|---|---|---|
| `fases.py` | [fases.md](fases.md) | Que las carpetas de épica, historia y fase estén bien nombradas y en orden. |
| `flujo.py` | [flujo.md](flujo.md) | Que el plan de trabajo esté completo y sin dudas sin resolver. |
| `trazabilidad.py` | [trazabilidad.md](trazabilidad.md) | Que la épica y la historia se nombren entre sí, y que al cerrar quede la tabla de qué se hizo. |

### Revisan el código de un proyecto

| Archivo | Documentación | Qué revisa |
|---|---|---|
| `secretos.py` | [secretos.md](secretos.md) | Contraseñas y claves escritas dentro del código, donde las ve cualquiera. |
| `seguridad.py` | [seguridad.md](seguridad.md) | Consultas y comandos armados pegando texto: así un dato del usuario puede colarse como orden. |
| `errores.py` | [errores.md](errores.md) | Errores que se atrapan y se tiran a la basura, y contraseñas que quedan escritas en los registros. |
| `rendimiento.py` | [rendimiento.md](rendimiento.md) | Consultas que traen todas las columnas cuando se necesitan dos, y consultas metidas adentro de algo que se repite miles de veces. |
| `calidad.py` | [calidad.md](calidad.md) | Funciones demasiado largas. |
| `esquema.py` | [esquema.md](esquema.md) | En la base de datos: columnas que apuntan a otra tabla sin decir qué pasa si se borra lo apuntado, y columnas nuevas obligatorias que dejarían inválido lo ya guardado. |
| `migraciones.py` | [migraciones.md](migraciones.md) | Que cada cambio a la base de datos diga cómo se deshace. |
| `dependencias.py` | [dependencias.md](dependencias.md) | Que esté guardado el archivo que fija qué versión exacta se usa de cada programa de afuera. |
| `aislamiento.py` | [aislamiento.md](aislamiento.md) | Que las pruebas no toquen los datos de verdad ni dependan del azar. |
| `ci.py` | [ci.md](ci.md) | Que exista algo que corra solo las pruebas y el revisor de estilo cada vez que llega un cambio. |
| `rama.py` | [rama.md](rama.md) | Que se trabaje en una copia aparte del proyecto y que esté al día. |
| `herramientas.py` | [herramientas.md](herramientas.md) | Corre las herramientas del propio proyecto: el revisor de estilo, las pruebas y la búsqueda de programas de afuera con fallas conocidas. |

### Se ejecutan solos

Un **enganche** (*hook*) es un programa que arranca solo cuando pasa algo, sin que nadie lo llame.

| Archivo | Documentación | Cuándo corre |
|---|---|---|
| `validar.py` | [validar.md](validar.md) | Cuando alguien lo escribe en la consola. |
| `hook_sesion.py` | [hook_sesion.md](hook_sesion.md) | Al empezar a trabajar. |
| `hook_historico.py` | [hook_historico.md](hook_historico.md) | Al enviar un mensaje y al terminar la respuesta. |
| `hook_checklist.py` | [hook_checklist.md](hook_checklist.md) | Al enviar un mensaje. |
| `hook_recuerdos.py` | [hook_recuerdos.md](hook_recuerdos.md) | Al empezar a trabajar y cada vez que se escribe un archivo. |
| `hook_md.py` | [hook_md.md](hook_md.md) | Al escribir o cambiar un archivo. |
| `pruebas.py` | [pruebas.md](pruebas.md) | A mano, con `python validadores/pruebas.py`. |

### Documentos de la carpeta

| Archivo | Documentación | Qué es |
|---|---|---|
| `README.md` | [readme-fuente.md](readme-fuente.md) | El manual de uso de los validadores. |
| `reglas-validables.md` | [reglas-validables.md](reglas-validables.md) | La lista de qué reglas puede revisar un programa y cuáles no. |
| `__pycache__/` | — | Archivos que arma Python solo para arrancar más rápido. Nadie los escribió. |

## Cómo se relacionan entre sí

Un archivo **depende** de otro cuando lo trae para usar algo suyo.

### Los archivos están en cinco niveles

Cada nivel usa solo archivos de los niveles de arriba. Así ninguno se queda esperando a otro que a su vez lo espera a él.

```
NIVEL 1 — no usan a nadie
    comun.py        recuerdos.py        historico.py

NIVEL 2 — usan el nivel 1
    instalar.py     versionado.py   versiones.py   version.py
    cargador.py     enlaces.py      citas.py       plantillas.py
    commits.py      fases.py

NIVEL 3 — usan instalar.py, versionado.py o fases.py
    codigo.py       sesion.py       rama.py         ci.py
    dependencias.py secretos.py     migraciones.py  herramientas.py
    flujo.py        trazabilidad.py

NIVEL 4 — usan codigo.py, migraciones.py o sesion.py
    calidad.py      errores.py      rendimiento.py  seguridad.py
    aislamiento.py  esquema.py      checklist.py

NIVEL 5 — se ejecutan solos y nadie los usa
    validar.py      pruebas.py      hook_md.py      hook_sesion.py
    hook_historico.py    hook_checklist.py    hook_recuerdos.py
```

### Tabla completa

| Archivo | Usa a | Lo usan |
|---|---|---|
| `comun.py` | — | todos menos `recuerdos.py` e `historico.py` |
| `recuerdos.py` | — | `checklist`, `instalar`, `hook_recuerdos`, `hook_sesion`, `pruebas` |
| `historico.py` | — | `hook_historico`, `hook_sesion`, `pruebas` |
| `instalar.py` | `comun` | `codigo`, `sesion`, `rama`, `ci`, `secretos`, `dependencias`, `migraciones`, `esquema`, `aislamiento`, `herramientas`, `checklist`, `validar`, `hook_sesion`, `pruebas` |
| `versionado.py` | `comun` | `codigo`, `secretos`, `dependencias`, `migraciones`, `esquema`, `aislamiento`, `ci`, `herramientas`, `validar`, `pruebas` |
| `versiones.py` | `comun` | `checklist`, `instalar`, `validar`, `pruebas` |
| `version.py` | `comun` | `checklist`, `instalar`, `validar`, `pruebas` |
| `cargador.py` | `comun` | `hook_sesion` |
| `enlaces.py` | `comun` | `hook_md`, `validar`, `pruebas` |
| `citas.py` | `comun` | `validar`, `pruebas` |
| `plantillas.py` | `comun` | `validar`, `pruebas` |
| `commits.py` | `comun` | `validar`, `pruebas` |
| `fases.py` | `comun` | `flujo`, `trazabilidad`, `validar`, `pruebas` |
| `codigo.py` | `instalar`, `versionado`, `comun` | `calidad`, `errores`, `rendimiento`, `seguridad`, `aislamiento`, `esquema` |
| `sesion.py` | `instalar`, `comun` | `checklist`, `hook_sesion` |
| `rama.py` | `instalar`, `comun` | `validar`, `pruebas` |
| `ci.py` | `instalar`, `versionado`, `comun` | `validar`, `pruebas` |
| `dependencias.py` | `instalar`, `versionado`, `comun` | `validar`, `pruebas` |
| `secretos.py` | `instalar`, `versionado`, `comun` | `validar`, `pruebas` |
| `migraciones.py` | `instalar`, `versionado`, `comun` | `esquema`, `validar`, `pruebas` |
| `herramientas.py` | `instalar`, `versionado`, `comun` | `validar`, `pruebas` |
| `flujo.py` | `fases`, `comun` | `validar`, `pruebas` |
| `trazabilidad.py` | `fases`, `comun` | `validar`, `pruebas` |
| `calidad.py` | `codigo`, `comun` | `validar`, `pruebas` |
| `errores.py` | `codigo`, `comun` | `validar`, `pruebas` |
| `rendimiento.py` | `codigo`, `comun` | `validar`, `pruebas` |
| `seguridad.py` | `codigo`, `comun` | `validar`, `pruebas` |
| `aislamiento.py` | `codigo`, `instalar`, `versionado`, `comun` | `validar`, `pruebas` |
| `esquema.py` | `codigo`, `instalar`, `migraciones`, `versionado`, `comun` | `validar`, `pruebas` |
| `checklist.py` | `instalar`, `recuerdos`, `sesion`, `version`, `versiones`, `comun` | `validar`, `hook_checklist`, `instalar`, `pruebas` |
| `validar.py` | los 24 validadores y `comun` | — |
| `pruebas.py` | 27 archivos | — |
| `hook_md.py` | `enlaces`, `comun` | — |
| `hook_sesion.py` | `cargador`, `historico`, `instalar`, `recuerdos`, `sesion`, `comun` | — |
| `hook_historico.py` | `historico`, `comun` | — |
| `hook_checklist.py` | `checklist`, `comun` | — |
| `hook_recuerdos.py` | `recuerdos`, `comun` | — |

### Un caso especial: `instalar.py`

`instalar.py` necesita a `checklist.py`, `versiones.py`, `version.py` y `recuerdos.py`, pero tres de ellos lo necesitan a él. Si cada uno esperara al otro, ninguno arrancaría. Por eso `instalar.py` los trae **adentro de la función** que los usa, en el momento justo, y no al comienzo del archivo.

## Qué retornan los validadores

Todos retornan una lista de hallazgos. Cada hallazgo trae una de dos etiquetas:

| Etiqueta | Qué significa | ¿Detiene el trabajo? |
|---|---|---|
| `FALLA` | Está mal, sin discusión. | Sí. |
| `AVISO` | Algo que conviene que mire una persona. | No. |
