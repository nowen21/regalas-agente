# Señales del proyecto «NOMBRE»  ·  `[CAPA 3 · memoria por señales]`

> **Qué es.** El registro de **señales**: conocimiento de alto valor que **no se puede recuperar del código**. Se guardan señales, **no la conversación**. Vive en `documentacion/senales.md` y **se versiona** (es conocimiento del proyecto).
>
> **Cómo se usa.** Cada vez que aparece una señal (una decisión, un error resuelto, un patrón, un aprendizaje...), se agrega una entrada abajo con el formato estándar. No se borran las señales revertidas: se marcan `reemplazada` y se enlaza la nueva. Antes de confiar en una señal vieja, verificar que sigue vigente (regla `01`·C2).

## Lo que se aprendió va acá; lo que falta hacer, a `pendientes/`

Los dos salen del mismo momento y por eso se confunden. La pregunta que los separa:

| Si la frase dice... | Es | Va a |
|---|---|---|
| ...**qué pasó y qué se decidió** | Señal | Este archivo |
| ...**qué falta hacer** | Pendiente | `pendientes/`, con su historia de usuario |

Una misma conversación suele dejar las dos. Escribir solo una de ellas es lo que hace que el aprendizaje se pierda o que el trabajo pendiente se olvide.

## Tipos de señal

`decisión` · `error-resuelto` · `patrón` · `aprendizaje` · `alternativa-descartada` · `supuesto` · `restricción` · `pregunta-abierta` · `gotcha` · `deuda-técnica`

## Formato de cada entrada

```
## S-000 · «título corto»  ·  tipo · estado
- **Qué pasó:** qué se decidió, se hizo o se encontró.
- **Por qué importa:** la razón que no está en el código.
- **Qué se decidió:** la lección para la próxima vez.
- **Dónde queda:** [archivo:línea](ruta) · o el módulo/área.
```

**Cuatro campos, no siete.** El molde tenía además `When/Who`, `Scope` y `Rel`, y **siete campos se llenan las dos primeras veces**: a la tercera la señal no se escribe, que es peor que escribirla incompleta. La fecha y quién la escribió ya los guarda el control de versiones; el alcance y las relaciones se dicen en el texto cuando hacen falta.

Si una señal necesita decir a cuál reemplaza, se escribe en **Qué se decidió** — es parte de la decisión, no un campo aparte.

- **estado:** `activa` · `reemplazada` · `revertida`.
- **id:** `S-001`, `S-002`... correlativo, para poder referenciar y enlazar.

---

## Señales

## S-001 · Ejemplo — modalidad de pago por defecto  ·  decisión · activa
- **What:** el pago por defecto es "efectivo" cuando no se especifica.
- **Why:** el 90% de los registros históricos eran efectivo; evita fricción en la carga.
- **Where:** [PagoService.php:42](app/PagoService.php)
- **Learned:** documentar el default en la UI para que el usuario no lo pase por alto.
- **When/Who:** 2026-07-23 · agente + usuario.
- **Scope:** módulo pagos.
- **Rel:** —

[[Borrar esta señal de ejemplo al empezar a usar el log.]]
