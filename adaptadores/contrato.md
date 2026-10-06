# Qué necesita el estándar de un agente

**Este documento existe para que soportar otro agente sea llenar un formulario, no empezar de cero.**

Las reglas de [`base/`](../base/) son texto y sirven en cualquier parte. Lo que las hace cumplir solas, no: son doce programas que existen **porque esta herramienta los llama**, y viven en [`claude-code/`](claude-code/).

Acá está lo que hay que poder hacer, sin nombrar ninguna herramienta. Quien vaya a soportar otra, responde las cinco filas y sabe si se puede.

---

## Las cinco capacidades

| # | Capacidad | Sin ella se pierde |
|---|---|---|
| **1** | **Inyectar texto al arrancar la sesión** | El agente trabaja sin haber leído las reglas |
| **2** | **Correr un programa después de que una herramienta devuelve** (el agente escribe un archivo, o trae algo de afuera) | Los enlaces rotos y los índices desactualizados se descubren días después; y lo que llega de afuera entra sin la marca de que es dato, no orden (`01·C27`) |
| **3** | **Correr un programa cuando el usuario manda un mensaje** | No hay transcripción, ni aviso de instalación, ni recuerdos recogidos |
| **4** | **Correr un programa cuando el agente termina de responder** | La transcripción queda a medias: se anota lo que se pidió y no lo que se hizo |
| **5** | **Cortar un `commit` desde fuera del agente** | Las claves, los artefactos y las marcas entran al repositorio |

**La quinta no es del agente.** La da el control de versiones, y por eso es la única que ya funciona con cualquier herramienta: son los `.githooks/`. Se lista igual, porque quien evalúe un agente nuevo tiene que saber que esa parte **no depende de él**.

## Las capas del freno que cubre cada adaptador

`EP-023·HU-007·CA-02`: nada se escribe fuera del plan aprobado, por ningún canal. El freno tiene cuatro capas; cada adaptador dice cuáles cubre en su herramienta y por qué no las demás.

| Capa | Qué detiene | `claude-code` | Por qué |
|---|---|---|---|
| **1 · Antes de actuar** | La escritura, el borrado o la publicación fuera del plan, antes de que pase | Sí: `hook_antes.py`, sobre toda herramienta (`PreToolUse` sin filtro) | La herramienta deja cortar la acción antes de correrla |
| **2 · Después de actuar** | Lo que un programa escribió por dentro, que la capa 1 no ve | Sí: `hook_despues.py`, sobre la consola (`PostToolUse` de `Bash` y `PowerShell`), comparando git con la foto de antes | Solo la consola corre programas; las demás herramientas ya las vio la capa 1. Lo que se escribe fuera del proyecto no está en git y no se ve |
| **3 · Al guardar el commit** | El archivo que entra al commit sin estar en el plan | No depende del adaptador: el `pre-commit` de `.githooks/` | La da el control de versiones, como la capacidad 5 |
| **4 · En la integración continua** | Lo que llega al repositorio compartido sin pasar por las otras tres | No depende del adaptador: `validar.py plan --rango`, que la instalación agrega a la integración continua del proyecto que la tiene | Corre fuera de la máquina, con Cimiento descargado del sitio que el proyecto anota |

Un adaptador nuevo llena la columna de su herramienta: las capas 3 y 4 ya las tiene.

## Qué recibe y qué devuelve cada programa

**Reciben lo que pasó, por la entrada estándar, y responden por su código de salida.** Nada más. No hay estado compartido, ni base de datos, ni orden garantizado entre ellos.

| Necesita | Detalle |
|---|---|
| **Ejecutar un comando** | Con argumentos, y con la carpeta del proyecto como uno de ellos |
| **Pasarle qué ocurrió** | Qué archivo se escribió, qué escribió el usuario, en qué carpeta |
| **Leer su código de salida** | `0` sigue · distinto de `0` significa que el programa tiene algo que decir |
| **Mostrar lo que imprime** | Al usuario, o al agente como contexto |

**Lo que el estándar NO necesita**, y decirlo importa tanto como lo otro: no necesita modificar la respuesta del agente, ni cancelarla, ni leer su razonamiento, ni acceso a la red, ni que la herramienta guarde nada por él. Todo lo que se guarda son archivos del repositorio.

## Cuánto costaría el cambio

**Medido el 2026-08-19**, con el amarre ya reunido en una carpeta.

| Qué | Cuánto |
|---|---|
| Programas que habría que reescribir | **12**, los de [`claude-code/`](claude-code/) |
| Programas que se quedan como están | **51**, todo [`validadores/`](../validadores/) |
| Lo que enchufa el adaptador | Una función de [`instalar.py`](../validadores/instalar.py) y su lista de eventos |
| Reglas de `base/` que habría que tocar | Ninguna — salvo diez menciones a un **nombre de archivo** |

**El amarre es de forma, no de fondo.** Los doce programas hacen trabajo agnóstico: lo que es de la herramienta es cómo se enteran de que pasó algo. Reescribirlos es traducir la entrada, no rehacer la lógica.

## Lo que este documento no hace

**No soporta un segundo agente, y no debe.** Construir la abstracción antes de tener el segundo caso produce una capa diseñada contra uno solo, que es la peor clase de capa. Lo que sí hacía falta era **saber cuánto costaría**, y hasta hoy ni eso se sabía.

## La frontera, en una línea

> **`validadores/` es lo que sirve con cualquier agente. `adaptadores/` es lo que existe porque una herramienta concreta lo llama.**

Un programa nuevo que nombre la herramienta y viva en `validadores/` es un error, y [`validar.py amarre`](../proyectos/cimiento/core/validadores/amarre.py) lo reporta.
