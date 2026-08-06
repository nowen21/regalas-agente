# Pendientes del estándar

Backlog de mejoras del estándar del agente que aún no se implementan. Un archivo por ítem, **numerado en el orden en que conviene ejecutarlos**. Al cerrar un pendiente, se implementa en la base/plantillas/skills y se borra su archivo de aquí (o se marca como hecho con la fecha).

Lo ya cerrado se registra en la carpeta **[hecho/](hecho/)** — un archivo por tema, nombrado por lo que resuelve. Es la contraparte de este backlog: allí se ve lo hecho, aquí lo que falta.

**El número es el orden, no la prioridad.** Los pendientes se ejecutan de menor a mayor porque cada uno se apoya en los anteriores. Al cerrar uno, el número no se reutiliza ni se renumeran los demás: los huecos son historia.

## Abiertos

### Garantía y sostenimiento del estándar (01–06, en orden)

| # | Pendiente | Qué resuelve | Por qué va aquí |
|---|---|---|---|
| 01 | [Validadores de código de proyecto](01-validadores-de-codigo-de-proyecto.md) | Los validadores que faltan: los que leen el código/config del proyecto o corren una herramienta (linter, pruebas, audit), más las puertas de flujo. | Primero: cierra la brecha entre "el estándar dice" y "el estándar se cumple", y produce los datos que necesita el 06. La **base ya está hecha** ([hecho/validadores-y-hooks.md](hecho/validadores-y-hooks.md)): hooks + validadores de documentación y estructura. Aquí queda la mitad que necesita un proyecto real. |
| ~~02~~ | **hecho** → [Vigencia y poda de la memoria](hecho/vigencia-y-poda-de-memoria.md) | Vigencia (`revisada`), marca de sin-verificar, recencia en `search`, comandos `revisar`/`archivar`. | Evitaba que la memoria se degrade sola de activo a ruido. Cerrado 2026-08-06 (la detección de contradicciones se movió al 05). |
| ~~03~~ | **hecho** → [Ciclo de vida de pendientes y deuda](hecho/ciclo-de-vida-de-pendientes.md) | Estado `cerrada` + `cerrada_en`/`cierra_ref`; comandos `pendientes` / `cerrar`. | Cierra lo que el agente difiere (deuda, preguntas). Cerrado 2026-08-06, sobre el gancho de migración del 02. |
| ~~04~~ | **hecho** → [Versión del estándar](hecho/version-del-estandar.md) | `VERSION` + `CHANGELOG`, fijación por proyecto, retroactividad y validador de desfase. | "El proyecto cumple el estándar" pasa a tener fecha. Cerrado 2026-08-06. |
| 05 | [Memoria semántica](05-memoria-semantica.md) | Búsqueda por significado sobre `senales.db` (híbrida con FTS5), con `sqlite-vec` para no perder el modo offline. | El 02 (vigencia) ya está; este hereda además la **detección de contradicciones**, que es semántica. |
| ~~06~~ | **hecho** → [Métricas del proceso](hecho/metricas-del-proceso.md) | Lee `senales.db` y reporta deuda abierta/cerrada, vigencia y pulso de señales. | Para decidir qué reglas cambiar, no para calificar. Cerrado 2026-08-06 (falta lo que necesita instrumentación nueva). |

### Patrones opt-in de dominio (07–08, fuera de la fila)

| # | Pendiente | Qué resuelve |
|---|---|---|
| 07 | [Patrones DevOps 18 y 19](07-patrones-devops.md) | Patrones opt-in de despliegue/infraestructura y observabilidad/operación. |
| 08 | [Patrón RPA](08-patrones-rpa.md) | Patrón opt-in para desarrollar soluciones RPA (bots): diseño, orquestación, resiliencia, credenciales, pruebas y gobernanza. |

Estos dos **no dependen de 01–06 ni entre sí**. Van numerados al final porque agregan *cobertura*, mientras que 01–06 agregan *garantía* sobre la cobertura existente. Si un proyecto real necesita DevOps o RPA, se adelantan sin esperar la fila.

## Dependencias duras

Todo lo demás es preferencia y se puede reordenar:

- **02 → 05.** ✅ resuelta: el 02 (vigencia) ya está, así que la memoria semántica arranca sin recuperar más ruido del necesario.
- **02 → 03.** El 02 dejó el gancho de migración (`memoria.py · migrar()`) y `estado` abierto; el 03 suma `'cerrada'` sin migrar de nuevo.
