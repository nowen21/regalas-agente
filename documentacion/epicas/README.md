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

**Las cuatro de la plataforma** nacen del giro de producto del 2026-08-24, y salen del inventario aprobado, no del planteamiento:

| Épica | De qué se trata | Versión | Estado |
|---|---|---|---|
| [EP-008](EP-008-los-proyectos-se-administran-desde-un-solo-lugar/) | Conectar proyectos y verlos sin entrar a ellos | 1 | Abierta. Fase A cerrada |
| [EP-009](EP-009-todo-lo-que-se-hace-queda-registrado/) | Que quede constancia de qué se hizo | 1 | Abierta. Fase D en curso |
| [EP-010](EP-010-lo-escrito-entra-a-la-plataforma/) | Traer un proyecto con lo que ya tenga escrito | 1 | Abierta |
| [EP-011](EP-011-lo-que-se-repite-sale-a-la-luz/) | Ver qué correcciones se repiten, para escribir la regla que falta | 2 | Abierta |
| [EP-012](EP-012-el-expediente-se-entrega-el-mismo-dia/) | Armar el expediente de un proyecto y entregarlo el mismo día | 2 | Aprobada el 2026-08-31 |

Las siete primeras tienen sus historias de usuario escritas: **60 en total**. Ninguna se ha descompuesto en fases todavía, salvo EP-001 y EP-004, que tienen una cada una.

El número es el orden en que se ejecutan, y las dependencias lo confirman: EP-004 no arranca sin EP-001 y EP-003.

**En las de la plataforma el número no es el orden.** El orden lo fija la versión, en [cvds/implementacion/README.md](../../cvds/implementacion/README.md): la auditoría de `EP-009` va antes que conectar proyectos de `EP-008`, para no dejar un tramo sin registrar.
