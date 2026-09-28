# Stack del proyecto  ·  `[CAPA 3]`

> Todo documento creado con esta plantilla se redacta aplicando estas reglas. Esta nota se borra al llenarla.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |

> Plantilla. Declara el stack concreto que la base deja abierto. Al llenarla se reemplazan los `«…»` y se borran esta caja y las notas de cada sección.

## Lenguajes y frameworks

> Nombra cada pieza del stack con la versión que usa el proyecto. Si una no existe, se escribe «No aplica».

- **Lenguaje(s):** «…», versión «…»
- **Framework(s):** «…», versión «…»
- **Base de datos:** «motor», versión «…»
- **Frontend / UI:** «…»

## Cómo se corre

> Da el comando exacto de cada acción, tal como se escribe en la terminal.

| Acción | Comando |
|---|---|
| Instalar dependencias | `«…»` |
| Levantar en desarrollo | `«…»` |
| Compilar / build | `«…»` |
| Correr las pruebas | `«…»` |
| Lint / formateo | `«…»` |
| **Respaldo de datos** | `«…»` |
| **Restaurar un respaldo** | `«…»` |

## Entorno de pruebas (concreta `08` · T4 y `00` · N4)

> Dice dónde corren las pruebas y qué no alcanzan a reproducir.

- **Dónde corren las pruebas:** «BD en memoria / dedicada efímera / ...», nunca con datos reales.
- **Qué no reproduce el entorno de pruebas** (requiere verificación manual): «…»

## Estructura del proyecto

> Dice dónde arranca el código, cómo se agrupa y dónde vive su configuración.

- Punto de entrada: `«…»`
- Organización del código: «cómo se agrupan los módulos» (concreta `14·EST1`)
- Dónde vive la configuración de entorno: `«…»` (base `11`)

## Integración continua / despliegue

> Dice qué se comprueba solo en cada cambio y cómo llega el código a producción.

- **CI:** «hay / no hay», «qué corre»
- **Despliegue:** «manual / pipeline», «pasos»

## Tecnologías de apoyo

> Nombra los servicios auxiliares que usa el proyecto. El que no usa se escribe «Ninguno».

- Caché: «…»
- Colas / segundo plano: «…»
- Almacenamiento de archivos: «…»

## Herramientas del proyecto

> Un bloque por cada herramienta o comando propio del proyecto (motor de pruebas, CLI de memoria, scripts, importadores, pasarelas, generadores...), sin las genéricas del agente (Read, Edit, Bash, Grep...), que son del entorno. Sin esta sección el agente adivina cómo usar cada una. Si el proyecto no tiene herramientas propias, se escribe «Ninguna, solo las genéricas del agente».

### «nombre-de-la-herramienta»

> Ejemplo del bloque de una herramienta, que se repite por cada una.

- **Propósito:** «para qué sirve, en una frase».
- **Cuándo usarla:** «la situación en que corresponde».
- **Cuándo no:** «cuándo evitarla o usar otra».
- **Parámetros clave:** «flags/argumentos importantes y sus valores válidos».
- **Costo / latencia:** «rápida / lenta / cara (tokens, tiempo, red), para no abusarla».
- **Si falla:** «qué hacer: reintentar, fallback, o pausar y reportar al usuario (`00·N3`: no rodear el obstáculo)».

## Respaldo · para qué se declara

> Explica para qué sirven las filas de respaldo y de restaurar de «Cómo se corre».

Lo usa [`validadores/respaldo.py`](../validadores/respaldo.py) antes de correr una operación que no se puede deshacer, que es lo que exige [`00·N7`](../base/00-nucleo-blindado.md).

Si no está declarado, el envoltorio no corre nada y lo dice. No adivina el comando: adivinar cómo se respalda una base ajena es la clase de error que este repositorio no puede permitirse.

El comando de restaurar no se usa solo nunca. Se declara para que esté a mano el día que haga falta, escrito antes del susto y no durante.
