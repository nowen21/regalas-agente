# Trabajar en este repo

Este repo **es el estándar**: las reglas que otros proyectos heredan (`base/`, `plantillas/`, `skills/`, `validadores/`).

Este archivo manda sobre el trabajo **dentro de este repo** — mantener el estándar. No viaja a los proyectos que lo heredan; lo que sí les llega es `base/` (`00·M13`).

## 1 · Toda sesión se escribe en `historico-chat/` — sin que haya que pedirlo

Es obligatorio, no una cortesía. El chat se borra; el repo no.

- **Cuándo crear el archivo:** apenas la sesión produce su primera decisión o su primer cambio. No al cerrar: un chat rara vez tiene cierre explícito, y esperarlo es la forma segura de no escribirlo nunca.
- **Cuándo actualizarlo:** después de **cada** intercambio. No se acumula para el final.
- **Qué va:** la transcripción literal — cada mensaje del usuario tal como lo escribió y cada respuesta del agente tal como la dio, con sus tablas, código y ejemplos. No se condensa ni se parafrasea. Solo se omite la salida cruda de herramientas.
- **Marca de tiempo:** cada interacción, la del usuario y la del agente, lleva `AAAA-MM-DD HH:MM:SS` **leída del reloj del sistema** (`date "+%Y-%m-%d %H:%M:%S"`). Se toma una lectura al recibir el mensaje y otra al escribir la respuesta. Una hora que no se registró se escribe `hora no registrada`; **no se estima ni se reconstruye de memoria**.
- **Formato y plantilla:** [`historico-chat/README.md`](historico-chat/README.md). Al crear un archivo, agregar su línea al índice de ese README.

El nombre del archivo es `AAAA-MM-DD-tema.md`; si hay más de una sesión el mismo día, se sufija `-2`, `-3`.

## 2 · Agregar o cambiar una regla del estándar

El procedimiento completo está en las meta-reglas del preámbulo — se sigue tal cual, sin atajos. En corto: buscar antes de crear (`M12`), enrutar (`M13`, `M1`, `M2`), verificar que sea agnóstica de stack (`M3`), ID libre del prefijo del capítulo (`M4`), formato canónico con una sola exigencia y ejemplo INCORRECTO/CORRECTO (`M5`), declarar dependencias y excepciones (`M7`, `M8`), decidir si es validable (`M9`), versionar (`M10`).

**Versionar no es opcional** (`M10`): todo cambio de `base/` o `plantillas/` suma entrada en [`CHANGELOG.md`](CHANGELOG.md) y sube [`VERSION`](VERSION).

- **MAYOR** — obliga a un proyecto al día a hacer algo nuevo.
- **MENOR** — aditivo: regla opt-in, plantilla, validador, capítulo.
- **PARCHE** — redacción, ejemplos, correcciones que no cambian qué se exige.

Nada se renumera ni se borra: las reglas se derogan (`M11`), porque specs, commits y fases cerradas citan por ID.

## 3 · Dónde va cada cosa

| Si es… | Va en… |
|---|---|
| Regla que aplica a **cualquier** proyecto | `base/` |
| Instructivo para mantener el estándar | este `CLAUDE.md` |
| **Por qué** se diseñó algo así (razonamiento, alternativas) | `notas/` |
| Mejora acordada pero aún no hecha | `pendientes/` |
| Qué pasó en una sesión | `historico-chat/` |
| Preferencia del usuario sobre cómo trabajar | memoria del agente |

Regla que solo sirve a un stack o a un cliente: no va en `base/` (`M3`, `M13`).

## 4 · Antes de commitear

No hacer `commit` ni `push` hasta que el usuario haya leído el cambio y lo apruebe. Que apruebe el cambio no es que apruebe el commit: se pregunta aparte.

En el cuerpo del commit va primero la idea del usuario y después lo que hizo el agente. Nunca `Co-Authored-By`.
