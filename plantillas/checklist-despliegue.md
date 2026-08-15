# Checklist de despliegue — «servicio / versión»   ·   `[CAPA 3]`

Parte del entregable de cada despliegue no trivial ([`18·DP6`](../base/18-despliegue-e-infraestructura.md#dp6--checklist-de-despliegue)). Se llena y se versiona junto al release. **Ejecutar contra producción lo autoriza el usuario** ([`00·N2`](../base/00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada)).

- **Artefacto:** «imagen/paquete + tag» · **commit:** «hash» · **entorno destino:** «staging / producción»
- **Responsable (humano que ejecuta):** «nombre» · **fecha/hora:** «…»

## Antes

- [ ] El artefacto es el **mismo** que pasó pruebas y staging ([`18·DP3`](../base/18-despliegue-e-infraestructura.md#dp3--build-una-vez-promover-el-mismo-artefacto)) — no se recompila.
- [ ] Config y secretos del entorno destino listos y **fuera del artefacto** ([`18·DP4`](../base/18-despliegue-e-infraestructura.md#dp4--config-por-entorno-fuera-del-artefacto), [`04·S4`](../base/04-seguridad.md#s4--gestión-de-secretos)).
- [ ] Migraciones **reversibles** ([`03·D2`](../base/03-datos.md#d2--cada-cambio-de-esquema-es-una-migración-reversible)) y retrocompatibles con los datos ([`03·D3`](../base/03-datos.md#d3--migraciones-retrocompatibles-con-los-datos-existentes)).
- [ ] **Respaldo** tomado (BD y lo que no se pueda reconstruir), y restauración probada.
- [ ] Plan de **reversión** escrito y a mano ([`18·DP5`](../base/18-despliegue-e-infraestructura.md#dp5--release-reversible-con-plan-de-vuelta)): «cómo volver».
- [ ] Ventana / aviso a quien corresponda, si aplica.

## Durante

- [ ] Aplicar en el **orden** definido (p. ej. migración → despliegue → activación).
- [ ] Verificar `health/readiness` en verde ([`18·DP7`](../base/18-despliegue-e-infraestructura.md#dp7--la-app-expone-su-salud)) antes de enviar tráfico.

## Después

- [ ] **Smoke test** de los caminos críticos (login, la operación principal, un flujo con datos).
- [ ] Métricas y errores sin anomalías en los primeros minutos ([`19·OB2`](../base/19-observabilidad-y-operacion.md#ob2--se-mide-lo-que-le-duele-al-usuario)).
- [ ] Registrar el resultado (y cualquier señal/aprendizaje: [`13·DOC5`](../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)).

## Si algo sale mal

- [ ] Ejecutar el **rollback** del plan (artefacto anterior + reversión de migración).
- [ ] Confirmar que el sistema volvió a estado sano.
- [ ] Postmortem si el impacto lo amerita ([`19·OB5`](../base/19-observabilidad-y-operacion.md#ob5--postmortem-sin-culpa)).
