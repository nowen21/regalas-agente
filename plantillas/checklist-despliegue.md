# Checklist de despliegue — «servicio / versión»   ·   `[CAPA 3]`

Parte del entregable de cada despliegue no trivial (`18·DP6`). Se llena y se versiona junto al release. **Ejecutar contra producción lo autoriza el usuario** (`00·N2`).

- **Artefacto:** «imagen/paquete + tag» · **commit:** «hash» · **entorno destino:** «staging / producción»
- **Responsable (humano que ejecuta):** «nombre» · **fecha/hora:** «…»

## Antes

- [ ] El artefacto es el **mismo** que pasó pruebas y staging (`18·DP3`) — no se recompila.
- [ ] Config y secretos del entorno destino listos y **fuera del artefacto** (`18·DP4`, `04·S4`).
- [ ] Migraciones **reversibles** (`03·D2`) y retrocompatibles con los datos (`03·D3`).
- [ ] **Respaldo** tomado (BD y lo que no se pueda reconstruir), y restauración probada.
- [ ] Plan de **reversión** escrito y a mano (`18·DP5`): «cómo volver».
- [ ] Ventana / aviso a quien corresponda, si aplica.

## Durante

- [ ] Aplicar en el **orden** definido (p. ej. migración → despliegue → activación).
- [ ] Verificar `health/readiness` en verde (`18·DP7`) antes de enviar tráfico.

## Después

- [ ] **Smoke test** de los caminos críticos (login, la operación principal, un flujo con datos).
- [ ] Métricas y errores sin anomalías en los primeros minutos (`19·OB2`).
- [ ] Registrar el resultado (y cualquier señal/aprendizaje: `13·DOC5`).

## Si algo sale mal

- [ ] Ejecutar el **rollback** del plan (artefacto anterior + reversión de migración).
- [ ] Confirmar que el sistema volvió a estado sano.
- [ ] Postmortem si el impacto lo amerita (`19·OB5`).
