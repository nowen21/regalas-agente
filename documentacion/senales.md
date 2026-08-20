# Señales del estándar del agente  ·  `[CAPA 3 · memoria por señales]`

Conocimiento de alto valor que **no se recupera leyendo el código ni las reglas**: decisiones, errores resueltos, patrones y aprendizajes. Se guardan señales, no la conversación (`13·DOC5`). La conversación entera vive en [historico-chat/README.md/](../historico-chat/README.md).

Una señal revertida no se borra: se marca `reemplazada` y se enlaza la nueva. Antes de confiar en una vieja, comprobar que sigue vigente.

## Tipos

`decisión` · `error-resuelto` · `patrón` · `aprendizaje` · `alternativa-descartada` · `supuesto` · `restricción` · `pregunta-abierta` · `gotcha` · `deuda-técnica`

**Estado:** `activa` · `reemplazada` · `revertida`.

---

## Señales

## S-001 · El estándar escribía en inglés lo que exige escribir en español  ·  aprendizaje · activa
- **What:** el estándar usaba "spec" en 53 archivos, y su propia regla `01·C8` manda escribir en el idioma del proyecto.
- **Why:** nadie lo notó porque el término se leía como jerga técnica normal. Salió a la luz cuando el usuario preguntó qué significaba.
- **Where:** [base/01-conducta.md](../base/01-conducta.md) · regla `C20`.
- **Learned:** el estándar no se audita a sí mismo con sus propias reglas. Lo que se exige por escrito hay que comprobarlo también sobre el propio texto.
- **When/Who:** 2026-08-14 · usuario + agente.
- **Scope:** estándar.
- **Rel:** —

## S-002 · Escribir código sin haber recorrido la cadena  ·  error-resuelto · activa
- **What:** se escribieron cinco validadores nuevos desde el pendiente 01, sin épica, sin historia de usuario y sin plan aprobado.
- **Why:** el pendiente describía el trabajo con tanto detalle que pareció suficiente para arrancar. Un pendiente no es una historia de usuario: dice qué falta, no qué se acepta como cumplido.
- **Where:** [documentacion/epicas/EP-004-comprobacion-automatica/README.md/](epicas/EP-004-comprobacion-automatica/README.md).
- **Learned:** el pendiente es el origen, no el permiso. Lo escrito quedó como línea base verificada, no como trabajo hecho.
- **When/Who:** 2026-08-14 · usuario.
- **Scope:** estándar.
- **Rel:** —

## S-003 · `F2` está escrita para construir software, no para escribir reglas  ·  pregunta-abierta · activa
- **What:** dos fases seguidas se abrieron declarando que no tienen especificación aparte, porque su entregable es texto normativo o programas cortos.
- **Why:** `F2` da por hecho que lo que se construye es código de un módulo. Cuando el entregable es el propio texto, una especificación aparte diría lo mismo dos veces.
- **Where:** [base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md](../base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md).
- **Learned:** una regla que se incumple dos veces seguidas con buenos motivos necesita decir cuándo no aplica, o se vuelve costumbre incumplirla.
- **When/Who:** 2026-08-14 · agente.
- **Scope:** estándar.
- **Rel:** pendiente 21.

## S-004 · Lo que un validador encuentra sobre el propio estándar no es ruido  ·  aprendizaje · activa
- **What:** al escribir los validadores nuevos aparecieron 354 enlaces que incumplen `DOC14`, 129 reglas sin bloque de checklist, 7 publicadas en "no cumple" y 33 sin clasificar.
- **Why:** son incumplimientos reales del propio estándar, no falsos positivos del validador. Se descubrieron porque nadie los había comprobado nunca.
- **Where:** [validadores/reglas-validables.md](../validadores/reglas-validables.md).
- **Learned:** escribir el validador es la única forma de saber cuánto se incumplía. Antes de tenerlo, el número era cero por falta de medición, no por cumplimiento.
- **When/Who:** 2026-08-14 · agente.
- **Scope:** estándar.
- **Rel:** pendientes 18 y 19.

## S-005 · Dos sesiones versionando el mismo archivo a la vez  ·  gotcha · activa
- **What:** mientras esta sesión escribía la versión 10.0.0, otra subió la 9.0.0, la 9.1.0 y dejó escrita la 9.2.0 sin guardar. Al final quedaron dos numeraciones vivas.
- **Why:** `VERSION` y el `CHANGELOG` son un archivo único y ninguna sesión sabe qué está haciendo la otra.
- **Where:** [CHANGELOG.md](../CHANGELOG.md) · [VERSION](../VERSION).
- **Learned:** la regla de que cada sesión sube lo suyo se rompe en los archivos que las dos tocan. Hace falta decidir quién manda sobre la versión.
- **When/Who:** 2026-08-14 · agente.
- **Scope:** estándar.
- **Rel:** pendiente 22.

## S-006 · Mover un archivo que los proyectos llaman por ruta rompe el propio aviso de rotura  ·  error-resuelto · activa
- **What:** la 26.0.0 movió los ocho `hook_*.py` de `validadores/` a `adaptadores/claude-code/` sin dejar nada en la ruta vieja. Los proyectos instalados seguían llamando la ruta vieja: Python salía con código 2, que en el enganche del mensaje **bloquea el mensaje del usuario**, y todos los proyectos quedaron mudos.
- **Why:** el plan de recuperación —«hook_checklist.py lo reclama en el primer mensaje»— corría por el mismo enganche roto. El aviso de desfase viaja por el canal que la mudanza rompe: no puede avisar de su propia caída.
- **Where:** [CHANGELOG.md](../CHANGELOG.md) (26.0.1) · puentes en `validadores/hook_*.py` · [validadores/instalar.py](../validadores/instalar.py).
- **Learned:** lo que otros llaman por ruta absoluta no se muda sin puente en la ruta vieja, y el puente se prueba con el código de salida: para la herramienta, salir con 2 no es fallar — es bloquear al usuario.
- **When/Who:** 2026-08-19 · usuario (reportó el bloqueo) + agente.
- **Scope:** estándar y todos los proyectos instalados.
- **Rel:** S-001 (el estándar no se audita a sí mismo con sus propias reglas).

## S-007 · El enganche de apertura nunca le cargó las reglas al propio estándar  ·  error-resuelto · activa
- **What:** `hook_sesion.py` salía antes de llamar al cargador cuando la carpeta era la del estándar, desde su primera versión (2026-08-05). 30 de 30 aperturas de sesión de este repositorio sin el bloque de reglas; los proyectos herederos sí lo recibían.
- **Why:** la excepción «el propio estándar no se revisa a sí mismo» se escribió para la revisión de instalación y se llevó las reglas por delante. Y nadie lo midió porque las reglas viajan por el canal que no se dibuja: en pantalla se ven los mensajes de estado de los enganches, no lo que llega.
- **Where:** [adaptadores/claude-code/hook_sesion.py](../adaptadores/claude-code/hook_sesion.py) · fase `B-EP-005-HU-009` · caso `arranque-reglas-en-el-estandar` en `evals/`.
- **Learned:** lo que llega por un canal invisible necesita una medición que lo mire, o falta sin que nadie se entere. Y el `CLAUDE.md` §0 de este repositorio lo mandaba por escrito: mandarlo no lo hizo pasar, igual que con el histórico.
- **When/Who:** 2026-08-20 · usuario (preguntó por qué el agente hacía cosas que las reglas no dicen) + agente.
- **Scope:** estándar.
- **Rel:** S-001 · S-006.

## S-008 · El checkpoint se reclama comparando fechas, no leyendo el estado  ·  decisión · activa
- **What:** el enganche del checkpoint decide «falta» o «atrasado» con la fecha de escritura del `estado-fase.md` contra la del documento de puerta recién escrito. No lee ninguno de los dos.
- **Why:** leer el checkpoint y buscar la estación es opinar sobre el texto, y decir en qué estación va la fase es criterio del agente. Dos fechas del sistema de archivos no cuestan nada y no dependen de la redacción.
- **Where:** [validadores/checkpoint.py](../validadores/checkpoint.py) · fase `A-EP-005-HU-013`.
- **Learned:** el aviso se repite mientras el checkpoint siga atrás, a propósito: la marca de «ya avisé» exigiría escribir en un archivo del agente, que es justo lo que este enganche no hace. Solo tres documentos disparan, así que no es ruido.
- **When/Who:** 2026-08-20 · agente, aprobado por el usuario en el plan.
- **Scope:** estándar y proyectos instalados.
- **Rel:** S-007.

## S-009 · El tramo de consumo es un millón y se decide sin estado  ·  decisión · activa
- **What:** el aviso de consumo a mitad de sesión sale una vez por cada millón de fichas (entrada más salida, sin caché) cruzado, y el cruce se decide comparando el total con el último turno contra el total sin él.
- **Why:** ocho sesiones reales medidas el 2026-08-20 fueron de 144 mil a 12,7 millones: con 200 mil (el tope de la nota de arquitectura) avisaría en todas, y un aviso que sale siempre se deja de leer. Sin estado compartido porque el enganche no tiene archivo propio en el proyecto donde marcar, y crear uno para esto es más estado del que la información vale.
- **Where:** [validadores/presupuesto.py](../validadores/presupuesto.py) · fase `A-EP-005-HU-014`.
- **Learned:** el comando de cierre instalado no se tocó: el modo nuevo entra por un argumento y el viejo es el que corre sin ninguno. Vencer un comando instalado es lo que la 26.0.1 pagó.
- **When/Who:** 2026-08-20 · agente, aprobado por el usuario en el plan.
- **Scope:** estándar y proyectos instalados.
- **Rel:** S-006.

## S-010 · El andamio traslada solo el enlace que llega exactamente a la raíz  ·  decisión · activa
- **What:** al copiar una plantilla, el andamio reescribe el prefijo `../…/` que desde la carpeta de la plantilla llega a la raíz del repositorio, y el marcador `«RUTA-ESTANDAR»`, con la ruta desde la carpeta de la fase. Un `../` que se queda en `plantillas/`, o que pasa de la raíz, no se toca.
- **Why:** siete fases nacieron hoy con el mismo enlace roto, corregido siete veces con `sed`. Reescribir cualquier `../` habría roto los que no iban a la raíz; las plantillas usan dos formas (`../../` y el marcador) y el andamio atiende las dos para no tocar las plantillas.
- **Where:** [validadores/andamio.py](../validadores/andamio.py) `_reenlazar` · fase `C-EP-004-HU-005`.
- **Learned:** lo que un programa copia de una plantilla hereda la perspectiva de la plantilla, no la del destino. El prefijo se calcula con `relpath`, nunca se escribe fijo.
- **When/Who:** 2026-08-20 · agente, aprobado por el usuario.
- **Scope:** estándar.
- **Rel:** S-012.

## S-011 · Un índice que escribe un programa se corrige en el programa, no en el índice  ·  error-resuelto · activa
- **What:** `historico.py` y `resumen.py` escribían el texto del enlace igual al destino (`[2026-08-20/](2026-08-20/)`), y `13·DOC14` pide la ruta desde la raíz. La suite reprobaba cuatro enlaces, dos de ellos nuevos cada sesión.
- **Why:** corregir solo los cuatro habría dejado que la próxima sesión agregara el quinto. La forma del enlace la decide el programa que lo escribe.
- **Where:** [validadores/historico.py](../validadores/historico.py) `_enlace_al_resumen` · [validadores/resumen.py](../validadores/resumen.py) `_indexar_dias` · fase `C-EP-004-HU-008`.
- **Learned:** una suite en rojo por causas viejas esconde la falla nueva; hoy hubo que leer siete fallas para separar tres. El vecino de la misma carpeta sigue por su nombre, que es la excepción que la regla escribe.
- **When/Who:** 2026-08-20 · agente.
- **Scope:** estándar y proyectos instalados (sus índices nuevos nacen bien).
- **Rel:** S-010.

## S-012 · La historia toma el número siguiente al mayor; la fase, el primer hueco  ·  decisión · activa
- **What:** `andamio.py hu` numera la historia con el siguiente al mayor que exista en la épica, como los pendientes; `andamio.py` para la fase sigue tomando la primera letra libre.
- **Why:** la historia se cita por número desde fases, pendientes, commits y el mapa del backlog; un hueco puede ser una historia que se movió, y reutilizarlo haría que «HU-002» apuntara a dos cosas según cuándo se lea. La letra de la fase vive solo dentro de su historia. Un caso lo atrapó: la primera versión tomaba el hueco.
- **Where:** [validadores/andamio.py](../validadores/andamio.py) `siguiente_hu` · fase `B-EP-007-HU-003`.
- **Learned:** los enlaces de la plantilla se trasladan **antes** de poner los propios; al revés, el `../epica.md` recién puesto se trasladaba también. Y la fila del backlog va a «Sin agrupar todavía»: agrupar es criterio y el andamio no lo tiene.
- **When/Who:** 2026-08-20 · agente, aprobado por el usuario.
- **Scope:** estándar.
- **Rel:** S-010.

## S-013 · El veredicto se copia solo con concepto escrito, y nunca al checkpoint  ·  decisión · activa
- **What:** `veredicto.py` copia el §6 del resultado a la fila de la historia y a los dos README únicamente cuando el concepto es «cumple» o «no cumple», y no toca el `estado-fase.md`.
- **Why:** un resultado a medio escribir no es un veredicto: propagarlo pondría «no ejecutado» en la historia a cada guardado. El checkpoint es criterio del agente (HU-013). Se reutilizan las expresiones de `fases.py` porque es la que decide la puerta, y dos lecturas del mismo texto se desincronizan.
- **Where:** [validadores/veredicto.py](../validadores/veredicto.py) · [validadores/cerrar.py](../validadores/cerrar.py) `_fila_hecha` · fase `C-EP-005-HU-003`.
- **Learned:** doce copias a mano en un día, y el programa que ya sabía el veredicto solo lo comprobaba después. Se estrenó cerrando sus propias cuatro fases.
- **When/Who:** 2026-08-20 · agente, aprobado por el usuario.
- **Scope:** estándar y proyectos instalados.
- **Rel:** S-008.
