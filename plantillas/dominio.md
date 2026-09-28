# Dominio del proyecto  ·  `[CAPA 3]`

> Todo documento creado con esta plantilla se redacta aplicando estas reglas. Esta nota se borra al llenarla.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |

> Plantilla. Explica qué hace el sistema y las reglas del negocio que el agente no puede adivinar leyendo el código. Reemplaza los `«…»` y borra esta caja.

## Qué es el sistema

> Es la presentación del sistema para quien no lo conoce.

«Una o dos frases: qué resuelve, para quién.»

## Contexto operativo

> Describe el entorno en que opera el sistema: el negocio, quién lo usa, con qué convive y qué se da por cierto.

- **Dominio:** «rubro / sector, ej. contable, salud, logística».
- **Usuario típico:** «quién lo usa a diario y para qué, ej. contador, operario de campo, administrador».
- **Sistemas con los que convive:** «integraciones y dependencias externas: APIs, pasarelas de pago, otros módulos/servicios, base compartida».
- **Supuestos:** «lo que se da por cierto del entorno (volúmenes esperados, disponibilidad, versiones); cada supuesto es un riesgo si resulta falso».

## Entidades del negocio

> Lista las cosas centrales del dominio y qué representa cada una.

Las cuatro primeras columnas también las lee un programa, así que se escriben con cuidado; la última es para quien lee.

| Entidad | Tabla | Clave natural | Inmutable | Qué representa |
|---|---|---|---|---|
| «…» | `«tabla»` | `«columna, columna»` | no | «…» |

- *Tabla*: el nombre real en la base de datos. Vacío o `—` si la entidad no se persiste, y entonces el validador la salta.
- *Clave natural*: las columnas que no pueden repetirse juntas en dos filas (`03·D1` pide su `UNIQUE`). `—` si la entidad no tiene una.
- *Inmutable*: `sí` para lo que ya surtió efecto y solo se anula, nunca se edita ni se borra (`15`). Con `sí`, se comprueban los estados y los campos de anulación que declara `mapeo-nombres.md`.

Solo se listan las tablas **de dominio**: las que trae el framework (sesiones, colas, migraciones, caché) no van, y por eso no se les exige auditoría.

## Módulos

> Lista las grandes áreas funcionales del sistema, con su carpeta y su especificación.

La carpeta y la especificación también las lee un programa: con ellas se comprueba que ningún módulo tenga código sin especificación (`02·F2`) y que cada uno viva donde la convención dice (`14·EST1`).

| Módulo | Carpeta | Especificación | Qué hace |
|---|---|---|---|
| `«modulo»` | `«ruta/desde/la/raiz»` | `«documentacion/«modulo»/spec.md»` | «…» |

## Reglas de negocio clave

> Son las invariantes que el código debe garantizar y que no se ven leyendo un archivo suelto (`13·DOC2`), cada una con el motivo por el que existe.

1. «Regla, y por qué existe.»
2. «…»

## Glosario

> Son las palabras de este negocio, cada una en una línea que entienda quien no lo conoce. Se actualiza en el mismo cambio que introduce el término, no después.

Lo exige [`13·DOC23`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC23-escribe-el-glosario-de-los-terminos-del-proyecto.md); el modelo es [`base/glosario.md`](«RUTA-ESTANDAR»/base/glosario.md).

Entra la palabra que el negocio ya trae y la base no nombra. La que sí nombra la base va en `mapeo-nombres.md`, que es otra cosa: ahí se dice cómo se llama acá un concepto del estándar.

- **«Término»**: «qué es, en una línea».

## Decisiones ya tomadas

> Registra las decisiones de diseño ya cerradas, con su fecha y su motivo, para que no se reabran en cada sesión. Si no hay ninguna, se escribe «Ninguna».

- «…»
