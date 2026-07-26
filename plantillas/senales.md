# Señales del proyecto «NOMBRE»  ·  `[CAPA 3 · memoria por señales]`

> **Qué es.** El registro de **señales**: conocimiento de alto valor que **no se puede recuperar del código**. Se guardan señales, **no la conversación**. Vive en `documentacion/senales.md` y **se versiona** (es conocimiento del proyecto).
>
> **Cómo se usa.** Cada vez que aparece una señal (una decisión, un error resuelto, un patrón, un aprendizaje…), se agrega una entrada abajo con el formato estándar. No se borran las señales revertidas: se marcan `reemplazada` y se enlaza la nueva. Antes de confiar en una señal vieja, verificar que sigue vigente (regla `01`·C2).

## Tipos de señal

`decisión` · `error-resuelto` · `patrón` · `aprendizaje` · `alternativa-descartada` · `supuesto` · `restricción` · `pregunta-abierta` · `gotcha` · `deuda-técnica`

## Formato de cada entrada

```
## S-000 · «título corto»  ·  tipo · estado
- **What:** qué se decidió / hizo / encontró.
- **Why:** por qué (la razón que no está en el código).
- **Where:** [archivo:línea](ruta)  ·  o el módulo/área.
- **Learned:** la lección para la próxima vez (si aplica).
- **When/Who:** «fecha» · «quién o qué rol».
- **Scope:** módulo «X» / proyecto / organización.
- **Rel:** reemplaza a S-00 / relacionada con S-00 / —.
```

- **estado:** `activa` · `reemplazada` · `revertida`.
- **id:** `S-001`, `S-002`… correlativo, para poder referenciar y enlazar.

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
