# B-EP-004-HU-008-ningun-validador-termina-en-silencio

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se hizo, en qué orden y sobre qué archivos |
| [plan_pruebas.md](plan_pruebas.md) | Con qué casos se comprobó |
| [resultado_pruebas.md](resultado_pruebas.md) | Qué dieron · **Cumple**, ciclo 1 |
| [funcionalidad_implementada.md](funcionalidad_implementada.md) | Qué quedó hecho |
| [estado-fase.md](estado-fase.md) | En qué estación va |

**Qué cerró.** El [pendientes/hecho/ningun-validador-termina-en-silencio.md](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md), sus dos puntos: ningún módulo de `validadores/` sale ya con código 0 en silencio —eran **33 de 45**— y `metareglas.py` tiene su subcomando.

**Por qué importaba.** Un validador que no existe se nota. Uno que calla **afirma**: sale con 0 y sin salida, que es lo mismo que imprime cuando ha mirado todo y está en orden. Una fase se lo creyó el 2026-08-16 y escribió «cero enlaces rotos» sobre veinte.

**Lo que se supo.** No era un descuido de `enlaces.py`: era el comportamiento por omisión de todo el módulo. Y el reparador es peor que el validador — `citas.py --aplicar` **escribiría** en `base/` los cuatro falsos positivos que el pendiente 55 solo denunciaba como reporte de más.

**Estado:** estación 9. Detenida esperando el commit.
