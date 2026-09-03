# Épicas

Contenido inmediato de esta carpeta. Todas nacen de [planteamiento.md](../../planteamiento.md).

| Épica | De qué se trata | Estado |
|---|---|---|
| [EP-001](EP-001-cuerpo-de-reglas-heredable/) | El cuerpo de reglas en capas que los proyectos heredan | Propuesta |
| [EP-002](EP-002-versionado-y-adopcion/) | Poner número a las reglas y saber en cuál quedó cada proyecto | Propuesta |
| [EP-003](EP-003-documentos-modelo-y-procedimientos/) | Los modelos de documento y el paso a paso de cada rol | Propuesta |
| [EP-004](EP-004-comprobacion-automatica/) | Los programas que comprueban lo que se responde con sí o no | Propuesta |
| [EP-005](EP-005-automatismos-que-no-dependen-de-la-memoria/) | Que eso se dispare solo, y que cada sesión quede escrita | Propuesta |
| [EP-006](EP-006-memoria-de-lo-aprendido/) | Dónde queda lo aprendido y cómo se busca | Propuesta |
| [EP-007](EP-007-instalacion-y-actualizacion/) | Que todo llegue a un proyecto con una línea | Propuesta |

**Las nueve de la plataforma** nacen del giro de producto del 2026-08-24, y salen del inventario aprobado, no del planteamiento:

| Épica | De qué se trata | Versión | Estado |
|---|---|---|---|
| [EP-008](EP-008-los-proyectos-se-administran-desde-un-solo-lugar/) | Conectar proyectos y verlos sin entrar a ellos | 1 | Abierta. Fase A cerrada |
| [EP-009](EP-009-todo-lo-que-se-hace-queda-registrado/) | Que quede constancia de qué se hizo | 1 | Terminada el 2026-09-01: registrar y consultar, las dos mitades |
| [EP-010](EP-010-lo-escrito-entra-a-la-plataforma/) | Traer un proyecto con lo que ya tenga escrito | 1 | Abierta |
| [EP-011](EP-011-lo-que-se-repite-sale-a-la-luz/) | Ver qué correcciones se repiten, para escribir la regla que falta | 2 | Abierta |
| [EP-012](EP-012-el-expediente-se-entrega-el-mismo-dia/) | Armar el expediente de un proyecto y entregarlo el mismo día | 2 | Aprobada el 2026-08-31 |
| [EP-013](EP-013-los-documentos-se-llenan-sin-salir-de-la-plataforma/) | Llenar los huecos de un documento del ciclo sin salir de la plataforma | 2 | Terminada el 2026-09-01 |
| [EP-014](EP-014-ninguna-clave-queda-escrita/) | Que ninguna clave quede escrita: se tapa lo que se teclea, no lo que se copia | 3 | Terminada el 2026-09-01 |
| [EP-015](EP-015-lo-exigido-se-comprueba-solo/) | Que la plataforma diga si un proyecto cumple, sin entrar a él | 3 | Terminada el 2026-09-01: sus tres historias cumplen |
| [EP-016](EP-016-el-cuerpo-de-reglas-se-administra-desde-la-plataforma/) | Escribir, numerar y derogar reglas sin reutilizar ningún identificador | 3 | Terminada el 2026-09-01: sus seis historias cumplen |
| [EP-017](EP-017-una-aprobacion-dice-sobre-que-texto/) | Que una aprobación diga sobre qué texto se dio, y caduque cuando ese texto cambia | 4 | Terminada el 2026-09-01: sus tres historias cumplen |
| [EP-018](EP-018-lo-aprendido-no-se-pierde-entre-sesiones/) | Que lo aprendido en una sesión llegue a la siguiente, y el usuario lo pueda corregir | 4 | Terminada el 2026-09-01: sus dos historias cumplen |
| [EP-019](EP-019-el-ciclo-se-opera-desde-la-plataforma/) | Abrir una fase, ver en cuál estación va, y no dejar pasar la puerta que falta | 5 | Terminada el 2026-09-01: sus tres historias cumplen |
| [EP-020](EP-020-lo-que-se-desvia-se-avisa/) | Que lo que se salió de lo acordado salga solo, y que comparar proyectos no engañe | 5 | Terminada el 2026-09-01: sus dos historias cumplen |
| [EP-021](EP-021-la-plataforma-se-mira-sin-consola/) | Que lo que la plataforma sabe se pueda mirar sin abrir una consola | 5 | Terminada el 2026-09-02: su historia cumple |
| [EP-022](EP-022-quien-entra-y-que-puede-hacer/) | Que la plataforma sepa quién entró, y que no todos puedan hacer lo mismo | 5 | Terminada el 2026-09-02: sus dos historias cumplen |

Las siete primeras tienen sus historias de usuario escritas: **60 en total**. Ninguna se ha descompuesto en fases todavía, salvo EP-001 y EP-004, que tienen una cada una.

El número es el orden en que se ejecutan, y las dependencias lo confirman: EP-004 no arranca sin EP-001 y EP-003.

**En las de la plataforma el número no es el orden.** El orden lo fija la versión, en [cvds/implementacion/README.md](../../cvds/implementacion/README.md): la auditoría de `EP-009` va antes que conectar proyectos de `EP-008`, para no dejar un tramo sin registrar.
