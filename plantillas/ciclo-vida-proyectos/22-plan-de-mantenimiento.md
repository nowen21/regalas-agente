# Plan de mantenimiento   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se sostiene el sistema después de entregado: con qué cadencia se revisa, cómo se mantienen al día las dependencias, cuándo se prueba la restauración y qué pasa con la deuda declarada. Un sistema sin plan de mantenimiento no está terminado: está abandonado con retraso.

> Plantilla. Se escribe al preparar la primera entrega y se revisa en cada acta de entrega. Mientras no haya nada entregado, existe y dice: «No aplica todavía porque «el porqué»». Reemplaza los `«…»` y borra esta caja.

## 1. Las rutinas, con su cadencia

> Cada rutina con su disparador: una fecha, un evento o un umbral. «Cuando se pueda» no es una cadencia.

| Rutina | Cadencia | Qué se hace | Dónde queda constancia |
|---|---|---|---|
| Revisión de dependencias | «mensual / al aviso de seguridad» | «actualizar según [`10`](../../base/10-dependencias.md), correr la suite, anotar» | [Bitácora](21-bitacora-de-operacion.md) |
| Prueba de restauración | «…» | «restaurar el último respaldo en limpio y verificar» | Bitácora y [manual de operación](18-manual-tecnico-y-de-operacion.md) §2 |
| Revisión de la deuda declarada | «por entrega» | «releer los pendientes aceptados de las [actas](20-acta-de-entrega.md) y decidir cuáles suben» | «el backlog del proyecto» |
| Depuración de datos y registros | «…» | «qué se archiva o borra, según [`12`](../../base/12-privacidad-datos.md)» | Bitácora |

## 2. Cómo entra un cambio después de entregado

«El mismo ciclo, no un atajo: la corrección o mejora entra por el paso 1 (necesidad), toca el [inventario](02-inventario-funcionalidades.md) si cambia el alcance, y baja por sus fases. El mantenimiento no suspende las reglas: las repite en chico.»

## 3. Quién responde

| Frente | Quién | Hasta cuándo se compromete |
|---|---|---|
| Correcciones | «…» | «…» |
| Operación (respaldos, monitoreo) | «…» | «…» |

## 4. El fin de vida

«Qué pasa el día que el sistema se apague: qué datos se entregan o archivan, a quién, y qué se destruye. Decidirlo al final, con el sistema lleno de datos, es decidirlo tarde.»
