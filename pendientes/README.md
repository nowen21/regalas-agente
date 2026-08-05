# Pendientes del estándar

Backlog de mejoras del estándar del agente que aún no se implementan. Un archivo por ítem, **numerado en el orden en que conviene ejecutarlos**. Al cerrar un pendiente, se implementa en la base/plantillas/skills y se borra su archivo de aquí (o se marca como hecho con la fecha).

Lo ya cerrado se registra en la carpeta **[hecho/](hecho/)** — un archivo por tema, nombrado por lo que resuelve. Es la contraparte de este backlog: allí se ve lo hecho, aquí lo que falta.

**El número es el orden, no la prioridad.** Los pendientes se ejecutan de menor a mayor porque cada uno se apoya en los anteriores. Al cerrar uno, el número no se reutiliza ni se renumeran los demás: los huecos son historia.

## Abiertos

### Garantía y sostenimiento del estándar (01–06, en orden)

| # | Pendiente | Qué resuelve | Por qué va aquí |
|---|---|---|---|
| 01 | [Validadores de código de proyecto](01-validadores-de-codigo-de-proyecto.md) | Los validadores que faltan: los que leen el código/config del proyecto o corren una herramienta (linter, pruebas, audit), más las puertas de flujo. | Primero: cierra la brecha entre "el estándar dice" y "el estándar se cumple", y produce los datos que necesita el 06. La **base ya está hecha** ([hecho/validadores-y-hooks.md](hecho/validadores-y-hooks.md)): hooks + validadores de documentación y estructura. Aquí queda la mitad que necesita un proyecto real. |
| 02 | [Vigencia y poda de la memoria](02-vigencia-y-poda-de-memoria.md) | Caducidad, revisión y ranking por recencia en `senales.db`. | Evita que la pieza más valiosa construida hasta hoy se degrade sola de activo a ruido. Bloquea al 05. |
| 03 | [Ciclo de vida de pendientes y deuda](03-ciclo-de-vida-de-pendientes.md) | Cerrar lo que el agente difiere: estado `cerrada` en las señales + comandos `pendientes` / `cerrar`. | Toca el **mismo esquema** que el 02: van seguidos para diseñar los cambios de `estado` en una sola migración. |
| 04 | [Versión del estándar](04-version-del-estandar.md) | Versionar `base/` y que cada proyecto fije la versión que sigue, con regla de retroactividad. | Independiente, pero su comprobación automática se apoya en el 01. |
| 05 | [Memoria semántica](05-memoria-semantica.md) | Búsqueda por significado sobre `senales.db` (híbrida con FTS5), con `sqlite-vec` para no perder el modo offline. | **Después del 02, obligatorio**: la búsqueda semántica encuentra más señales obsoletas que la léxica, así que sin vigencia empeora el problema. |
| 06 | [Métricas del proceso](06-metricas-del-proceso.md) | Medir si el estándar sirve: fases reabiertas, puertas que fallan, decisiones escaladas, deuda abierta vs cerrada. | Último: **no tiene qué medir** hasta que 01 y 03 estén hechos. |

### Patrones opt-in de dominio (07–08, fuera de la fila)

| # | Pendiente | Qué resuelve |
|---|---|---|
| 07 | [Patrones DevOps 18 y 19](07-patrones-devops.md) | Patrones opt-in de despliegue/infraestructura y observabilidad/operación. |
| 08 | [Patrón RPA](08-patrones-rpa.md) | Patrón opt-in para desarrollar soluciones RPA (bots): diseño, orquestación, resiliencia, credenciales, pruebas y gobernanza. |

Estos dos **no dependen de 01–06 ni entre sí**. Van numerados al final porque agregan *cobertura*, mientras que 01–06 agregan *garantía* sobre la cobertura existente. Si un proyecto real necesita DevOps o RPA, se adelantan sin esperar la fila.

## Las dos únicas dependencias duras

Todo lo demás es preferencia y se puede reordenar:

- **02 → 05.** La memoria semántica sin política de vigencia recupera más ruido, no menos.
- **02 ↔ 03.** Mismo cambio de esquema en `senales`. Diseñar los estados juntos; hacerlos por separado obliga a migrar dos veces.
