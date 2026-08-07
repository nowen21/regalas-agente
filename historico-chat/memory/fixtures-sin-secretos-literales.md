# Fixtures sin secretos literales

En tests y ejemplos, un token de secreto de mentira (AWS `AKIA…`, Slack `xoxb-…`, `ghp_…`, `sk_live_…`) **no** debe quedar como literal completo en el archivo: se arma en runtime (`"xoxb-" + "1234…"` · `f"{prefijo}{cuerpo}"`).

**Por qué:** el *push protection* de GitHub escanea el contenido y **bloquea el push** si ve un token con forma real, aunque sea de prueba. Pasó con el fixture de `validadores/secretos.py` (en `pruebas.py`): un `xoxb-…` de ejemplo frenó el push y hubo que reescribir el commit para sacarlo de la historia — no basta con editarlo después.

**Cómo se aplica:** al escribir fixtures o ejemplos de secretos, partir el literal en prefijo + cuerpo y concatenar en runtime. Mantiene la cobertura del test y no dispara el escaneo. Es coherente con lo que valida el propio `secretos.py` (`04·S4`, `00·N6`): ni los secretos falsos se versionan enteros.

Relacionado: [todo multiproyecto](todo-multiproyecto.md).
