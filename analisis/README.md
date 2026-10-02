# `analisis/` — auditorías del estándar

Análisis persistidos sobre el propio estándar: qué se revisó, qué se encontró y qué queda por corregir. No son norma (`20·M13`): la norma vive en `base/`. Son evidencia y plan de trabajo.

**Nomenclatura:** `<ámbito>-AAAA-MM-DD-<tema>.md` — el mismo patrón que `13·DOC6` fija para los análisis dentro de un proyecto.

El **análisis principal** dice lo que se va a construir hoy: se reescribe cuando un análisis individual cambia algo, y suma ese cambio a su lista con la fecha y el enlace (`13·DOC25`). Los análisis individuales viven en la carpeta de su pendiente, cierran al final de su mismo archivo y, aprobados, no se reescriben (`13·DOC24`).

## Índice

| Análisis | Fecha | Versión auditada | Qué cubre |
|---|---|---|---|
| [proyecto-2026-10-02-analisis-principal.md](proyecto-2026-10-02-analisis-principal.md) | 2026-10-02 | 40.1.0 | El análisis principal de Cimiento: qué se construye hoy y la lista de cambios que lo trajo hasta ahí. |
| [base-2026-08-07-cumplimiento-meta-reglas.md](base-2026-08-07-cumplimiento-meta-reglas.md) | 2026-08-07 | 1.3.0 | Las 170 reglas de `base/` contra las 13 meta-reglas del capítulo 20. Estado de cumplimiento regla por regla, 22 hallazgos transversales, 15 inconsistencias entre reglas y plan de corrección en 5 olas. |
