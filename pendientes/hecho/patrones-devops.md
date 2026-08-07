# Hecho · Patrones DevOps (18 y 19)

Origen: pendiente 07. El agente ya trae **conocimiento DevOps** como dos capítulos opt-in: deja el código listo para desplegarse de forma reproducible y el sistema observable — sin operar en vivo.

Cerrado el 2026-08-06 (estándar `v1.1.0`).

---

## Qué se hizo

- **`base/18-despliegue-e-infraestructura.md`** (opt-in, prefijo `DP`): despliegue como artefacto versionado (nada de click-ops), IaC, build-una-vez y promover el mismo artefacto, config/secretos por entorno fuera del build, release reversible con plan de vuelta, checklist de despliegue, health/readiness, y **correr contra producción gateado por el usuario** (`00·N2`/`N4`). Extiende `09·G6`.
- **`base/19-observabilidad-y-operacion.md`** (opt-in, prefijo `OB`): logs estructurados y correlacionables (sin secretos, `05·E5`), señales doradas + trazas, SLO/alertas como código sobre **síntomas del usuario**, runbooks, postmortem **sin culpa**. Extiende `05`.
- **Plantillas:** `checklist-despliegue.md` (DP6) y `postmortem.md` (OB5).
- **Cableado:** toggles en `CLAUDE.md.plantilla §5.1` (rango a `01–19`), lista de capítulos y plantillas en el README, y `VERSION` a `1.1.0` con su entrada en el CHANGELOG (cambio MENOR, aditivo).

## Alcance, por diseño

El agente **produce artefactos** (pipeline, IaC, scripts, runbooks, postmortem). **No** ejecuta el deploy en producción, **no** opera el sistema vivo, **no** vigila dashboards ni responde incidentes en caliente — eso es del humano. La identidad es *desarrollador senior*, no SRE. Ambos capítulos lo dicen explícito (`DP8`, `OB6`).
