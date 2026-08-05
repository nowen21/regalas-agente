# Pendiente · Patrones DevOps (18 y 19)

**Estado:** abierto · anotado 2026-08-02.

Extender la cobertura DevOps del agente con dos **patrones opt-in** (estilo `15` registros inmutables, `16` cumplimiento, `17` interfaz — con toggle en `CLAUDE.md.plantilla §5.1`).

## Qué implementar

### `18 · Despliegue e infraestructura` *(opt-in)*

- CI/CD como código, IaC (contenedor/manifiestos), estrategia de release, checklist de despliegue.
- Ejecución contra producción **siempre gateada por el usuario** (`00·N2`).
- Extiende `G6` (integración continua).
- **Mayor retorno:** convierte "el agente entrega código" en "código listo para desplegarse de forma reproducible".

### `19 · Observabilidad y operación` *(opt-in)*

- Métricas/trazas/logs estructurados con SLO y alertas **como código**.
- Runbooks (backup/restore, recuperación).
- Plantilla de postmortem.
- Extiende `05` (errores y logging).

## Principio que lo justifica

El agente **produce artefactos** (código, config, scripts, docs) → todo lo expresable como artefacto es implementable.

**Fuera de alcance por diseño** (no es que falte cubrir): **ejecutar** el deploy en producción, **operar** el sistema vivo, **vigilar** dashboards en tiempo real, **responder** incidentes en caliente. Eso lo autoriza/hace el humano — la identidad del agente es *desarrollador senior*, no SRE.

## Orden sugerido

Primero `18` (CI/CD + IaC), luego `19` (observabilidad).
