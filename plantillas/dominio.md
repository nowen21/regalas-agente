# Dominio del proyecto  ·  `[CAPA 3]`

> Plantilla. Explica qué hace el sistema y las reglas del negocio que el agente no puede adivinar leyendo el código. Reemplaza los `«…»` y borra esta caja.

## Qué es el sistema

«Una o dos frases: qué resuelve, para quién.»

## Contexto operativo

- **Dominio:** «rubro / sector — ej. contable, salud, logística».
- **Usuario típico:** «quién lo usa a diario y para qué — ej. contador, operario de campo, administrador».
- **Sistemas con los que convive:** «integraciones y dependencias externas — APIs, pasarelas de pago, otros módulos/servicios, base compartida».
- **Supuestos:** «lo que se da por cierto del entorno (volúmenes esperados, disponibilidad, versiones) — cada supuesto es un riesgo si resulta falso».

## Entidades del negocio

Las cosas centrales del dominio y qué representan. Las cuatro primeras columnas también las lee un programa, así que se escriben con cuidado; la última es para quien lee.

| Entidad | Tabla | Clave natural | Inmutable | Qué representa |
|---|---|---|---|---|
| «…» | `«tabla»` | `«columna, columna»` | no | «…» |

- **Tabla** — el nombre real en la base de datos. Vacío o `—` si la entidad no se persiste; entonces el validador la salta.
- **Clave natural** — las columnas que no pueden repetirse juntas en dos filas (`03`·D1 pide su `UNIQUE`). `—` si la entidad no tiene una.
- **Inmutable** — `sí` para lo que ya surtió efecto y solo se anula, nunca se edita ni se borra (`15`). Con `sí`, se comprueban los estados y los campos de anulación que declara `mapeo-nombres.md`.

Solo se listan las tablas **de dominio**: las que trae el framework (sesiones, colas, migraciones, caché) no van, y por eso no se les exige auditoría.

## Módulos

Las grandes áreas funcionales del sistema. La carpeta y la especificación también las lee un programa: con ellas se comprueba que ningún módulo tenga código sin especificación (`02`·F2) y que cada uno viva donde la convención dice (`14`·EST1).

| Módulo | Carpeta | Especificación | Qué hace |
|---|---|---|---|
| `«modulo»` | `«ruta/desde/la/raiz»` | `«documentacion/«modulo»/spec.md»` | «…» |

## Reglas de negocio clave

Invariantes que el código debe garantizar y que no se ven leyendo un archivo suelto (base `13` · DOC2):

1. «Regla — por qué existe.»
2. «…»

## Glosario

Las palabras de este negocio, cada una en una línea que entienda quien no lo conoce. Lo exige [`13·DOC23`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC23-escribe-el-glosario-de-los-terminos-del-proyecto.md); el modelo es [`base/glosario.md`](«RUTA-ESTANDAR»/base/glosario.md).

Entra la palabra que el negocio ya trae y la base no nombra. La que sí nombra la base va en `mapeo-nombres.md`, que es otra cosa: ahí se dice cómo se llama acá un concepto del estándar.

Se actualiza en el mismo cambio que introduce el término, no después.

- **«Término»** — «qué es, en una línea».

## Decisiones ya tomadas

> Decisiones de diseño cerradas, para que no se reabran en cada sesión (fecha, motivo).

- «…»
