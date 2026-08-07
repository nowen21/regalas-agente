# 18 · Despliegue e infraestructura  ·  `[CAPA 2 · opt-in]`

**Opt-in.** Reglas agnósticas para que lo que el agente entrega quede **listo para desplegarse de forma reproducible**. Aplican a proyectos que se despliegan (servicio, web, app); una librería o un script suelto las omiten. El agente **produce los artefactos** (pipeline, manifiestos, scripts, checklist); **no ejecuta** el despliegue en producción — eso lo autoriza y lo corre el humano (`00·N2`, `00·N4`). La herramienta concreta (CI, orquestador, nube, IaC) la declara la capa 3 (`.agente/stack.md`). Extiende `09·G6`.

---

## DP1 · El despliegue es un artefacto versionado, no una serie de clics

Todo lo que lleva el código a un entorno vive en el repo como **texto revisable**: pipeline de CI/CD, manifiestos de infraestructura, scripts. Nada de configurar a mano en una consola (click-ops) sin dejar rastro: lo que no está versionado no es reproducible ni auditable, y se pierde cuando cambia la persona.

## DP2 · Infraestructura como código

La infraestructura (contenedor, red, servicios, recursos de nube) se declara en archivos versionados y se aplica desde ahí, no se crea a mano. Un entorno nuevo se levanta corriendo la declaración, no siguiendo un instructivo. El **estado real** debe poder reconstruirse del código.

## DP3 · Build una vez, promover el mismo artefacto

Se compila/empaqueta **una sola vez** y ese mismo artefacto inmutable (imagen, paquete) pasa por los entornos (pruebas → staging → producción). No se recompila por entorno: lo que se probó es exactamente lo que se despliega. La versión del artefacto es rastreable al commit.

## DP4 · Config por entorno, fuera del artefacto

El artefacto es **agnóstico del entorno**; la configuración y los secretos se inyectan al desplegar, no se hornean adentro (`11`, `04·S4`). Así la misma imagen corre en cualquier entorno cambiando solo su config, y un secreto no viaja dentro del build.

## DP5 · Release reversible, con plan de vuelta

Toda estrategia de release define **cómo se revierte** antes de aplicarse: volver a la versión anterior del artefacto, revertir la migración (`03·D2`), restaurar datos. Preferir releases graduales (canario/azul-verde) cuando el riesgo lo amerite. Un release sin rollback pensado no está listo.

## DP6 · Checklist de despliegue

Cada despliegue no trivial lleva su checklist, del [plantillas/checklist-despliegue.md](../plantillas/checklist-despliegue.md): respaldo previo, migraciones reversibles, orden de pasos, verificación (smoke test) después, y el plan de reversión a mano. El checklist es parte del entregable, no memoria de quien despliega.

## DP7 · La app expone su salud

El servicio ofrece un punto de **readiness/health** (¿está vivo?, ¿listo para recibir tráfico?) para que el pipeline y el orquestador decidan sin adivinar si el release quedó bien. Migraciones y arranque no dejan el servicio a medias: o queda sano, o el release falla y se revierte.

## DP8 · Correr contra producción lo autoriza el humano

El agente **prepara** el despliegue; **ejecutarlo contra producción** (o contra datos reales) requiere autorización explícita del usuario (`00·N2`, `00·N4`), nunca por iniciativa propia ni "para probar". **Fuera de alcance por diseño:** operar el sistema vivo, vigilar dashboards, responder incidentes en caliente — eso es del humano (la observabilidad la cubre `19`). La identidad del agente es *desarrollador senior*, no SRE.
