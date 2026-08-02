# Stack del proyecto  ·  `[CAPA 3]`

> Plantilla. Declara el stack concreto que la base deja abierto. Reemplaza los `«…»` y borra esta caja.

## Lenguajes y frameworks

- **Lenguaje(s):** «…» · versión «…»
- **Framework(s):** «…» · versión «…»
- **Base de datos:** «motor» · versión «…»
- **Frontend / UI:** «…»

## Cómo se corre

| Acción | Comando |
|---|---|
| Instalar dependencias | `«…»` |
| Levantar en desarrollo | `«…»` |
| Compilar / build | `«…»` |
| Correr las pruebas | `«…»` |
| Lint / formateo | `«…»` |

## Entorno de pruebas (concreta `08` · T4 y `00` · N4)

- **Dónde corren las pruebas:** «BD en memoria / dedicada efímera / …» — **nunca datos reales**.
- **Qué NO reproduce el entorno de pruebas** (requiere verificación manual): «…»

## Estructura del proyecto

- Punto de entrada: `«…»`
- Organización del código: «cómo se agrupan los módulos» (concreta `14` · EST1)
- Dónde vive la configuración de entorno: `«…»` (base `11`)

## Integración continua / despliegue

- **CI:** «hay / no hay» · «qué corre»
- **Despliegue:** «manual / pipeline» · «pasos»

## Tecnologías de apoyo

- Caché: «…» · Colas / segundo plano: «…» · Almacenamiento de archivos: «…»

## Herramientas del proyecto

> Por cada herramienta o comando **propio del proyecto** (motor de pruebas, CLI de memoria, scripts, importadores, pasarelas, generadores…). NO las genéricas del agente (Read, Edit, Bash, Grep…) — esas son del entorno. Aquí se gana o se pierde la confiabilidad: sin esto, el agente adivina cómo usar cada tool.

### «nombre-de-la-herramienta»

- **Propósito:** «para qué sirve, en una frase».
- **Cuándo usarla:** «la situación en que corresponde».
- **Cuándo NO:** «cuándo evitarla o usar otra».
- **Parámetros clave:** «flags/argumentos importantes y sus valores válidos».
- **Costo / latencia:** «rápida / lenta / cara (tokens, tiempo, red) — para no abusarla».
- **Si falla:** «qué hacer — reintentar, fallback, o pausar y reportar al usuario (`00`·N3: no rodear el obstáculo)».

_(Repetir el bloque por cada herramienta. Si el proyecto no tiene herramientas propias, dejar "Ninguna — solo las genéricas del agente".)_
