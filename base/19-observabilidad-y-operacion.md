# 19 · Observabilidad y operación  ·  `[CAPA 2 · opt-in]`

**Opt-in.** Reglas agnósticas para que un sistema desplegado se pueda **entender desde afuera** cuando algo va mal, sin adivinar. Aplican a proyectos que corren en producción; complementan `18` (despliegue). El agente **construye** la instrumentación y los documentos de operación (logs, métricas, alertas, runbooks, postmortem); **no opera** el sistema vivo. La herramienta concreta (stack de logs, métricas, tracing) la declara la capa 3. Extiende `05` (errores y logging).

---

## OB1 · Logs estructurados y correlacionables

Los logs se emiten como **datos** (clave-valor / JSON), no como texto libre para leer con el ojo: nivel, marca de tiempo, y un **identificador de correlación** que permita seguir una operación de punta a punta. Nunca llevan secretos ni datos sensibles ([`05·E5`](05-errores-y-logging.md#e5--nunca-registres-secretos-ni-datos-sensibles), [`00·N6`](00-nucleo-blindado.md#n6--secretos-y-datos-sensibles-nunca-se-exponen-blindada)). Sin estructura, un log a escala no se puede buscar ni agregar.

## OB2 · Se mide lo que le duele al usuario

La instrumentación cubre las **señales doradas** del servicio: latencia, tráfico, errores y saturación. Las trazas permiten seguir una petición por los componentes que atraviesa. Se mide el **síntoma que sufre el usuario** (una página que no carga), no solo recursos internos (CPU) que no dicen si el sistema sirve.

## OB3 · SLO y alertas como código, sobre síntomas

Los objetivos de servicio (SLO) y las alertas se declaran **versionados**, no se configuran a mano en un dashboard. Una alerta se dispara por un **síntoma que exige acción humana** (el error del usuario supera el umbral), no por ruido que nadie atiende: una alerta que se ignora siempre es peor que ninguna. Cada alerta apunta a su runbook.

## OB4 · Runbooks para lo que se opera

Las operaciones recurrentes y las de emergencia se documentan como **runbook** versionado: respaldo y restauración, recuperación ante fallo, rotación de un secreto expuesto ([`04·S4`](04-seguridad.md#s4--gestión-de-secretos)), reversión de un release ([`18·DP5`](18-despliegue-e-infraestructura.md#dp5--release-reversible-con-plan-de-vuelta)). Un procedimiento crítico que solo vive en la cabeza de alguien no existe cuando esa persona no está.

## OB5 · Postmortem sin culpa

Tras un incidente relevante se escribe un **postmortem** (del [plantillas/postmortem.md](../plantillas/postmortem.md)): qué pasó, impacto, causa raíz, línea de tiempo y **acciones para que no vuelva** — centrado en el sistema y el proceso, **no en culpar a una persona**. El aprendizaje se registra como señal ([`13·DOC5`](13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md), tipo `error-resuelto`/`aprendizaje`) para que la memoria lo tenga.

## OB6 · Operar en vivo lo hace el humano

**Fuera de alcance por diseño:** ejecutar la operación, vigilar dashboards en tiempo real y responder incidentes en caliente son del humano. El agente **deja el sistema observable y los procedimientos escritos** para que esa operación sea posible y barata — no la reemplaza. Igual que en [`18·DP8`](18-despliegue-e-infraestructura.md#dp8--correr-contra-producción-lo-autoriza-el-humano), la identidad es *desarrollador senior*, no SRE de guardia.
