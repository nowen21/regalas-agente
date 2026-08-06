# Hecho · Métricas del proceso

Origen: pendiente 06. Ya hay con qué medir si el estándar sirve: un lector que agrega desde `senales.db` lo que el 02 y el 03 empezaron a registrar.

Cerrado el 2026-08-06.

---

## Qué se hizo

- **`metricas/metricas.py`** — lee `memoria/senales.db` (no instrumenta nada nuevo) y reporta: **deuda abierta vs cerrada** (03), **vigencia** (activas sin verificar >N meses, del 02), y el pulso por **estado** y por **tipo**. `--scope`/`--meses` filtran.
- Núcleo `resumen()` puro (agrega filas sintéticas), **4 pruebas** en `metricas/pruebas.py`. Sobre la base real: 198 señales, 11 de deuda (0 cerradas aún), 0 sin verificar.
- **`metricas/README.md`** deja escrita la advertencia de diseño: **para decidir qué reglas cambiar, no para calificar**. Una métrica visible se vuelve objetivo y deja de medir.

## Lo que falta (necesita instrumentación nueva)

Anotado en `metricas/README.md`: fases reabiertas (falta marcar una fase como reabierta), puertas que fallan (aproximable corriendo los validadores y contando por regla), decisiones escaladas (sin registro por fase), uso real de la memoria (registrar las búsquedas), retrabajo por spec incompleta (correlacionar `git log` con la fase). El [visor](../../interfaz/) es el lugar natural para exponerlas sin terminal.
