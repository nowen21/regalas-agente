# Métricas del proceso

Mide si el estándar **está sirviendo**: un lector que agrega y reporta desde lo que **ya se registra**, no un sistema de telemetría. Backend opcional del estándar (pendiente 06).

```
python metricas/metricas.py [--db <ruta>] [--scope proyecto:x] [--meses 6]
```

## La advertencia que no se negocia

> **Para decidir qué reglas cambiar, no para calificar el trabajo.**

Una métrica visible se convierte en objetivo y deja de medir: "cero fases reabiertas" se consigue **no reabriendo** ninguna, no haciéndolas bien. Estos números orientan qué parte del flujo ayuda, cuál estorba y cuál se salta siempre — para ajustar la norma, nunca para puntuar a nadie.

## Qué reporta hoy (derivado de `senales.db`)

- **Deuda diferida** — abierta vs cerrada (`03`): si la abierta solo crece, `§Fuera-de-scope` se volvió un basurero.
- **Vigencia** — señales activas sin verificar hace más de N meses (`02`).
- **Señales por estado y por tipo** — el pulso de la memoria.

## Qué falta (necesita un marcador que hoy no existe)

Estas no se derivan sin instrumentar algo nuevo; quedan anotadas para cuando haya de dónde sacarlas:

- **Fases reabiertas** — hace falta marcar una fase como reabierta (hoy no se distingue de una nueva).
- **Puertas que fallan** — se puede aproximar corriendo los validadores y contando hallazgos por regla; falta agregarlo.
- **Decisiones escaladas al usuario** — sin registro por fase; `pregunta-abierta` es solo un proxy grueso.
- **Uso real de la memoria** — cuántas búsquedas encuentran algo útil: necesita registrar las búsquedas.
- **Retrabajo por spec incompleta** — cambios de spec tras empezar a implementar: necesita correlacionar `git log` con la fase.

El [visor](../interfaz/) ya lee la base y los archivos reales; exponer estas métricas ahí es la extensión natural cuando se quiera verlas sin la terminal.
