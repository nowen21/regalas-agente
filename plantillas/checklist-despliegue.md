# Checklist de despliegue · «servicio / versión»   ·   `[CAPA 3]`

> Todo documento creado con esta plantilla se redacta aplicando estas reglas. Esta nota se borra al llenarla.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |

Parte del entregable de cada despliegue no trivial ([`18·DP6`](«RUTA-ESTANDAR»/base/18-despliegue-e-infraestructura.md#dp6--checklist-de-despliegue)). Se llena y se versiona junto al release. Ejecutar contra producción lo autoriza el usuario ([`00·N2`](«RUTA-ESTANDAR»/base/00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada)).

- Artefacto: «imagen/paquete + tag». Commit: «hash». Entorno destino: «staging / producción».
- Responsable (humano que ejecuta): «nombre». Fecha y hora: «…».

## Antes

> Es lo que tiene que estar listo antes de tocar el entorno destino.

- [ ] El artefacto es el **mismo** que pasó pruebas y staging ([`18·DP3`](«RUTA-ESTANDAR»/base/18-despliegue-e-infraestructura.md#dp3--build-una-vez-promover-el-mismo-artefacto)), sin recompilarlo.
- [ ] Config y secretos del entorno destino listos y fuera del artefacto ([`18·DP4`](«RUTA-ESTANDAR»/base/18-despliegue-e-infraestructura.md#dp4--config-por-entorno-fuera-del-artefacto), [`04·S4`](«RUTA-ESTANDAR»/base/04-seguridad.md#s4--gestión-de-secretos)).
- [ ] Migraciones **reversibles** ([`03·D2`](«RUTA-ESTANDAR»/base/03-datos.md#d2--cada-cambio-de-esquema-es-una-migración-reversible)) y retrocompatibles con los datos ([`03·D3`](«RUTA-ESTANDAR»/base/03-datos.md#d3--migraciones-retrocompatibles-con-los-datos-existentes)).
- [ ] **Respaldo** tomado (BD y lo que no se pueda reconstruir), y restauración probada.
- [ ] Plan de **reversión** escrito y a mano ([`18·DP5`](«RUTA-ESTANDAR»/base/18-despliegue-e-infraestructura.md#dp5--release-reversible-con-plan-de-vuelta)): «cómo volver».
- [ ] Ventana / aviso a quien corresponda, si aplica.

## Durante

> Es lo que se comprueba mientras se aplica el despliegue.

- [ ] Aplicar en el **orden** definido (por ejemplo: migración, despliegue y activación).
- [ ] Verificar `health/readiness` en verde ([`18·DP7`](«RUTA-ESTANDAR»/base/18-despliegue-e-infraestructura.md#dp7--la-app-expone-su-salud)) antes de enviar tráfico.

## Después

> Es lo que confirma que el despliegue quedó sano y deja registrado el resultado.

- [ ] **Smoke test** de los caminos críticos (login, la operación principal, un flujo con datos).
- [ ] Métricas y errores sin anomalías en los primeros minutos ([`19·OB2`](«RUTA-ESTANDAR»/base/19-observabilidad-y-operacion.md#ob2--se-mide-lo-que-le-duele-al-usuario)).
- [ ] Registrar el resultado (y cualquier señal/aprendizaje: [`13·DOC5`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)).

## Si algo sale mal

> Es lo que se hace para volver al estado anterior. Si el despliegue salió bien, se escribe «No aplica».

- [ ] Ejecutar el **rollback** del plan (artefacto anterior y reversión de la migración).
- [ ] Confirmar que el sistema volvió a estado sano.
- [ ] Postmortem si el impacto lo amerita ([`19·OB5`](«RUTA-ESTANDAR»/base/19-observabilidad-y-operacion.md#ob5--postmortem-sin-culpa)).
