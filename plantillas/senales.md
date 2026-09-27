# Señales del proyecto «NOMBRE»  ·  `[CAPA 3 · memoria por señales]`

> Todo documento creado con esta plantilla se redacta aplicando estas reglas. Esta nota se borra al llenarla.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |

> **Qué es.** El registro de señales: conocimiento de alto valor que no se puede recuperar del código. Se guardan señales, no la conversación. Vive en `documentacion/senales.md` y se versiona, porque es conocimiento del proyecto.
>
> **Cómo se usa.** Cada vez que aparece una señal (una decisión, un error resuelto, un patrón, un aprendizaje...), se agrega una entrada abajo con el formato estándar. No se borran las señales revertidas: se marcan `reemplazada` y se enlaza la nueva. Antes de confiar en una señal vieja, se verifica que siga vigente (regla `01·C2`).

## Lo que se aprendió va acá; lo que falta hacer, a `pendientes/`

> Separa la señal del pendiente, que salen del mismo momento y por eso se confunden.

La pregunta que los separa:

| Si la frase dice... | Es | Va a |
|---|---|---|
| ...**qué pasó y qué se decidió** | Señal | Este archivo |
| ...**qué falta hacer** | Pendiente | `pendientes/`, con su historia de usuario |

Una misma conversación suele dejar las dos. Escribir solo una de ellas es lo que hace que el aprendizaje se pierda o que el trabajo pendiente se olvide.

## Tipos de señal

> Son los tipos que puede llevar una entrada, en el encabezado, después del título.

`decisión`, `error-resuelto`, `patrón`, `aprendizaje`, `alternativa-descartada`, `supuesto`, `restricción`, `pregunta-abierta`, `gotcha`, `deuda-técnica`.

## Formato de cada entrada

> Es el molde de una entrada: un encabezado con id, título, tipo y estado, y cuatro campos debajo.

```
## S-000 · «título corto»  ·  tipo · estado
- **Qué pasó:** qué se decidió, se hizo o se encontró.
- **Por qué importa:** la razón que no está en el código.
- **Qué se decidió:** la lección para la próxima vez.
- **Dónde queda:** [archivo:línea](ruta) · o el módulo/área.
```

Son cuatro campos y no siete. El molde tenía además `When/Who`, `Scope` y `Rel`, y siete campos se llenan las dos primeras veces: a la tercera la señal no se escribe, que es peor que escribirla incompleta. La fecha y quién la escribió ya los guarda el control de versiones; el alcance y las relaciones se dicen en el texto cuando hacen falta.

Si una señal necesita decir a cuál reemplaza, se escribe en el campo *Qué se decidió*: es parte de la decisión y no un campo aparte.

- El estado es `activa`, `reemplazada` o `revertida`.
- El id es `S-001`, `S-002`... correlativo, para poder referenciar y enlazar.

## Señales

> Aquí van las entradas, una por señal, en orden de id.

## S-001 · Ejemplo — modalidad de pago por defecto  ·  decisión · activa
- **What:** el pago por defecto es "efectivo" cuando no se especifica.
- **Why:** el 90% de los registros históricos eran efectivo; evita fricción en la carga.
- **Where:** [PagoService.php:42](app/PagoService.php)
- **Learned:** documentar el default en la UI para que el usuario no lo pase por alto.
- **When/Who:** 2026-07-23 · agente + usuario.
- **Scope:** módulo pagos.
- **Rel:** —

[[Borrar esta señal de ejemplo al empezar a usar el log.]]
