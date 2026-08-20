# Especificación del módulo Automatismos

- **Slug del módulo:** `automatismos`
- **Estado:** en implementación

> El módulo son los programas que corren solos al trabajar: los enganches de la sesión. Esta especificación crece con cada fase. Lo que cubre hoy:
>
> | Incremento | Fase | Estado |
> |---|---|---|
> | El enganche que sostiene el resumen de sesión | [`A-EP-005-HU-008-enganche-del-resumen`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/A-EP-005-HU-008-enganche-del-resumen/README.md) | Cerrada el 2026-08-14 |
> | El enganche del checkpoint de la fase | [`A-EP-005-HU-013-el-enganche-del-checkpoint`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-013-el-checkpoint-se-reclama-solo/A-EP-005-HU-013-el-enganche-del-checkpoint/README.md) | Cerrada el 2026-08-20 |
> | El aviso de consumo por tramo | [`A-EP-005-HU-014-el-aviso-por-tramo`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-014-el-consumo-se-ve-a-tiempo/A-EP-005-HU-014-el-aviso-por-tramo/README.md) | Cerrada el 2026-08-20 |
> | El veredicto se copia solo | [`C-EP-005-HU-003-el-veredicto-se-copia-solo`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-003-disparo-al-escribir-un-archivo/C-EP-005-HU-003-el-veredicto-se-copia-solo/README.md) | Cerrada el 2026-08-20 |
> | Las reglas llegan también al propio estándar | [`B-EP-005-HU-009-las-reglas-llegan-tambien-al-propio-estandar`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-009-lo-que-rige-cada-frase-llega-puesto/B-EP-005-HU-009-las-reglas-llegan-tambien-al-propio-estandar/README.md) | Cerrada el 2026-08-20 |
>
> Los siete enganches que ya existen (transcripción, memoria, enlaces, instalación) se construyeron antes de que hubiera especificación de módulo. Retro-documentarlos es trabajo aparte, y lo pide [`13·DOC6`](../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md).

---

## 1. Propósito y alcance

Lo que depende de que alguien se acuerde, no pasa. El módulo existe para que las cosas que el estándar exige en cada sesión las haga un programa, no la memoria de quien esté trabajando.

- **Dentro de alcance:**
  - El enganche del resumen de sesión, con sus tres comportamientos: crear el archivo, avisar qué le falta cuando la sesión ya produjo algo, y mostrar lo que sigue abierto del propósito que la sesión declara.
  - **El reparto de las reglas al abrir la sesión** ([EP-005 · HU-009](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-009-lo-que-rige-cada-frase-llega-puesto/HU-009-lo-que-rige-cada-frase-llega-puesto.md)): qué capítulos del cuerpo de reglas llegan con su texto y cuáles llegan como índice. El programa existe desde la 5.0.0; lo que faltaba era esta parte, la que dice qué se le exige.
- **Fuera de alcance:**
  - **Escribir los hallazgos.** Reconocer un hallazgo y redactarlo es criterio, y el criterio no lo tiene un programa. El enganche crea, avisa y arrastra.
  - **Decidir qué es un hallazgo.** Eso lo decide quien trabaja.
  - **El modelo del resumen**, que es de EP-003 · HU-009 y ya está cerrado.
  - **Los otros enganches** que ya existen. Esta fase no los toca.

## 2. Contexto — qué hay hoy

Verificado el 2026-08-14.

**Siete enganches ya corriendo**, conectados en `.claude/settings.json` por [`validadores/instalar.py`](../../validadores/instalar.py), que es quien los instala en cada proyecto:

| Evento | Programa | Qué hace |
|---|---|---|
| `SessionStart` | `hook_sesion.py` | Carga las reglas, la memoria y el índice del histórico |
| `SessionStart` | `hook_recuerdos.py` | Recoge la memoria que quedó en el almacén de la herramienta |
| `UserPromptSubmit` | `hook_historico.py` | Anota el mensaje del usuario en la transcripción |
| `Stop` | `hook_historico.py` | Anota la respuesta del agente |
| `UserPromptSubmit` | `hook_checklist.py` | Revisa que el agente esté bien instalado |
| `PostToolUse` | `hook_md.py` | Revisa los enlaces al escribir un archivo |
| `PostToolUse` | `hook_recuerdos.py` | Recoge la memoria al escribir un archivo |

**La lección ya está probada.** La transcripción de la sesión solo empezó a escribirse siempre cuando la escribió un programa. Antes era una obligación escrita, y se incumplía.

**El resumen está en ese punto.** Desde la 14.0.0 [`13·DOC22`](../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md) lo exige, el modelo existe y el índice lo enlaza. Lo que no existe es el programa: hoy el resumen se escribe porque el agente se acuerda, que es exactamente la forma en que se pierde.

**Un detalle que condiciona el diseño.** La transcripción nace como `AAAA-MM-DD-sesion.md` y se renombra cuando el tema está claro. El resumen se llama igual, sin la fecha, así que **los dos nombres tienen que moverse juntos**: si solo se renombra uno, el enlace del índice apunta a un archivo que no existe.

## 3. Supuestos, dependencias y preguntas abiertas

- **Supuestos:**
  - "La sesión ya produjo algo" se puede detectar sin criterio: hubo un commit, o cambió un archivo de `base/` o de `plantillas/`.
  - Lo que un enganche imprime le llega al agente en ese turno. Es como funciona hoy el recordatorio de ponerle nombre a la sesión.
- **Dependencias / prerequisitos:**
  - EP-003 · HU-009, el modelo del resumen. **Cerrada** el 2026-08-14.
  - EP-005 · HU-001, la transcripción de la sesión. Ya corriendo: comparte el momento y el nombre del archivo.
- **Preguntas abiertas:** cuál es la señal de que el tema ya cerró. Viene arrastrada del hallazgo H-4 y sigue sin decidir. No bloquea: lo que el enganche mira es si la sección de cierre está llena, no si el tema cerró de verdad.

## 4. Reglas de negocio

1. **El archivo del resumen se crea solo, en el primer mensaje de la sesión**, con el modelo puesto y sin hallazgos. No al abrir: en ese momento la transcripción todavía no existe, y de su nombre sale el nombre del resumen. Si la sesión se retoma y ya tiene transcripción, el archivo está desde el arranque. Baja de [`EP-005 · HU-008`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/HU-008-enganche-del-resumen.md).
2. **El resumen se renombra con la transcripción.** Los dos nombres se mueven en la misma operación, o el índice queda apuntando a un archivo que no existe. Baja de [`EP-005 · HU-008`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/HU-008-enganche-del-resumen.md).
3. **Cuando la sesión ya produjo algo y al resumen le falta algo, se avisa una vez por cada cosa que falte.** Son dos como máximo: que no haya ningún hallazgo escrito, y que no se haya dicho si la sesión se puede cerrar. Un aviso repetido se vuelve ruido y se deja de leer. Baja de [`EP-005 · HU-008`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/HU-008-enganche-del-resumen.md).
4. **El aviso dice qué falta**, con la lista. Un aviso genérico obliga a preguntar, y preguntar es justo lo que se quiere evitar. Baja de [`EP-005 · HU-008`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/HU-008-enganche-del-resumen.md).
5. **Para cerrar una sesión cuentan los hallazgos de su propósito.** Cada sesión se abre para resolver algo; lo que aparece y es de otro tema nace acá y se cierra en otra sesión, y basta con que quede anotado. Baja de [`EP-005 · HU-008`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/HU-008-enganche-del-resumen.md).
6. **Se muestra lo que sigue abierto del propósito de la sesión, y nada más.** El propósito lo declara el usuario al abrir; el programa no lo adivina. Mostrar todos los hallazgos abiertos del repositorio es ruido: una sesión abierta para una cosa no tiene por qué ver las de otro tema. Baja de [`EP-005 · HU-008`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/HU-008-enganche-del-resumen.md).
7. **El enganche no escribe hallazgos ni los interpreta.** Crea, avisa y arrastra. Baja de [`EP-005 · HU-008`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/HU-008-enganche-del-resumen.md).
8. **El enganche no detiene el trabajo.** Si no puede escribir, avisa y la sesión sigue. Baja de [`EP-005 · HU-008`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/HU-008-enganche-del-resumen.md).
9. **El enganche no modifica un hallazgo ya escrito.** Baja de [`EP-005 · HU-008`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/HU-008-enganche-del-resumen.md).

### 4.1 El reparto de las reglas al abrir la sesión

10. **Llegan con su texto completo los capítulos que gobiernan todos los turnos**, sin importar el tema: los que empiezan por `00-` y por `01-`, con sus anexos. Son la identidad, el núcleo blindado y la conducta. Baja de [`EP-005 · HU-009`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-009-lo-que-rige-cada-frase-llega-puesto/HU-009-lo-que-rige-cada-frase-llega-puesto.md).
11. **Del resto llega el índice:** una línea por archivo, con su ruta, su peso y su título sacado del propio archivo. El índice dice de qué trata cada uno, no qué manda. Baja de [`EP-005 · HU-009`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-009-lo-que-rige-cada-frase-llega-puesto/HU-009-lo-que-rige-cada-frase-llega-puesto.md).
12. **El reparto se decide por el primer tramo de la ruta, no por el nombre del archivo.** Un capítulo puede vivir en un archivo suelto o en su carpeta; mirando el nombre, el que vive en carpeta caería al índice y la sesión arrancaría sin identidad. Baja de [`EP-005 · HU-009`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-009-lo-que-rige-cada-frase-llega-puesto/HU-009-lo-que-rige-cada-frase-llega-puesto.md).
13. **Se dice cuál es cuál.** Lo cargado se entrega diciendo que rige la sesión y es obligatorio; el índice se entrega diciendo que hay que abrir el archivo antes de tocar su tema. Baja de [`EP-005 · HU-009`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-009-lo-que-rige-cada-frase-llega-puesto/HU-009-lo-que-rige-cada-frase-llega-puesto.md).
14. **Un capítulo nuevo entra solo.** El reparto mira el prefijo, así que agregar un `01-` al estándar no obliga a tocar el programa. Baja de [`EP-005 · HU-009`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-009-lo-que-rige-cada-frase-llega-puesto/HU-009-lo-que-rige-cada-frase-llega-puesto.md).
15. **Si el arranque no pasa el gate [`02·F13`](../../base/02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md), llega esa regla y nada más.** Cargar las reglas de trabajo ahí invitaría a trabajar sobre una estructura que el propio estándar manda detener. Baja de [`EP-005 · HU-009`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-009-lo-que-rige-cada-frase-llega-puesto/HU-009-lo-que-rige-cada-frase-llega-puesto.md).
16. **Cargarlo todo no es una opción, y el motivo se escribe:** el cuerpo entero pesa mucho más que la ventana de contexto que se le puede dedicar, y llenarla adelanta el resumen automático, que borra justo lo que se inyectó al arrancar. Se pagaría el precio completo por una garantía que caduca. Baja de [`EP-005 · HU-009`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-009-lo-que-rige-cada-frase-llega-puesto/HU-009-lo-que-rige-cada-frase-llega-puesto.md).

> **Agregado el 2026-08-20 en la fase B de HU-009.** Las reglas de arriba se midieron en proyectos herederos. En la carpeta del propio estándar el enganche salía antes de cargarlas, desde su primera versión: 30 de 30 aperturas sin el bloque de reglas.

31. **Al propio estándar le llegan las reglas igual que a cualquier proyecto**, junto con su memoria y su histórico, y sin la revisión de instalación, que ahí no tiene qué revisar. El gate `F13` no se le aplica: no es un proyecto, es donde viven las reglas. Baja de [`EP-005 · HU-009`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-009-lo-que-rige-cada-frase-llega-puesto/HU-009-lo-que-rige-cada-frase-llega-puesto.md).

> **Que la regla llegue es necesario y no es suficiente.** El 2026-08-14 se incumplió [`00·ID8`](../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) durante una sesión entera, y esa regla llegaba completa. Lo que falta después es comprobar lo entregado, y eso es de EP-004.

### 4.2 La transcripción de la sesión

> Escrito el 2026-08-17 en la fase [`A-EP-005-HU-001`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-001-transcripcion-de-la-sesion/A-EP-005-HU-001-retrodocumentar-la-transcripcion-de-la-sesion/resultado_pruebas.md).

17. **La escribe el programa, no el agente.** `hook_historico.py` anota cada mensaje del usuario apenas se envía y cada respuesta apenas termina. El agente escribiéndola a mano la duplica y le inventa horas: ya pasó seis veces. Baja de [`EP-005 · HU-001`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-001-transcripcion-de-la-sesion/HU-001-transcripcion-de-la-sesion.md).
18. **La hora sale del reloj de la máquina**, nunca del texto del mensaje. Si se copiara lo que dice el texto, bastaría con escribir «03:33» en un mensaje para falsear el histórico. Baja de [`EP-005 · HU-001`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-001-transcripcion-de-la-sesion/HU-001-transcripcion-de-la-sesion.md).
19. **El archivo nace con el primer mensaje**, aunque sea un «hola», y crece de a un intercambio. Nada se escribe al cerrar: un chat no tiene final. Baja de [`EP-005 · HU-001`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-001-transcripcion-de-la-sesion/HU-001-transcripcion-de-la-sesion.md).
20. **Cada intercambio queda una sola vez.** Si el enganche se dispara dos veces por el mismo mensaje, no se duplica. Baja de [`EP-005 · HU-001`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-001-transcripcion-de-la-sesion/HU-001-transcripcion-de-la-sesion.md).
21. **La sesión entra al índice al nacer**, y al renombrarla se corrigen las dos cosas —el archivo y su línea—, o el índice apunta a un archivo que ya no está. Baja de [`EP-005 · HU-001`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-001-transcripcion-de-la-sesion/HU-001-transcripcion-de-la-sesion.md).
22. **Un proyecto sin la carpeta del histórico no se ve afectado:** el enganche no la crea ni escribe nada. Instalar el estándar es lo que la pone. Baja de [`EP-005 · HU-001`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-001-transcripcion-de-la-sesion/HU-001-transcripcion-de-la-sesion.md).

> **Lo que todavía no hace: enmascarar.** La HU pide que lo enmascarado no quede en claro, y **nada enmascara**: el texto del mensaje se guarda tal cual. Una clave pegada en el chat queda escrita en la transcripción, que se versiona. Es [EP-005 · HU-002](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-002-enmascarar-claves/HU-002-enmascarar-claves.md), sin construir.

### 4.3 El disparo al escribir un archivo

> Escrito el 2026-08-17 en la fase [`A-EP-005-HU-003`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-003-disparo-al-escribir-un-archivo/A-EP-005-HU-003-retrodocumentar-el-disparo-al-escribir/resultado_pruebas.md).

23. **Al escribir un documento corre su comprobación**, en el momento, no al cerrar la sesión. Un enlace roto avisado tres horas después ya se copió a otros documentos. Baja de [`EP-005 · HU-003`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-003-disparo-al-escribir-un-archivo/HU-003-disparo-al-escribir-un-archivo.md).
24. **Lo que no le toca se ignora en silencio**, y el enganche **corre igual**. Que calle no puede confundirse con que no se ejecutó: son dos estados distintos con la misma apariencia. Baja de [`EP-005 · HU-003`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-003-disparo-al-escribir-un-archivo/HU-003-disparo-al-escribir-un-archivo.md).
25. **El archivo que ya no está cuando el enganche llega no lo revienta.** Entre escribir y disparar puede pasar cualquier cosa. Baja de [`EP-005 · HU-003`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-003-disparo-al-escribir-un-archivo/HU-003-disparo-al-escribir-un-archivo.md).
26. **El disparo no se nota:** se mide, no se supone. Baja de [`EP-005 · HU-003`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-003-disparo-al-escribir-un-archivo/HU-003-disparo-al-escribir-un-archivo.md).

> **Lo que todavía no hace: detener.** El CA-03 de la HU pide que el hallazgo grave detenga y el resto avise. Hoy **todo avisa**: el enganche informa y el trabajo sigue en los dos casos.

### 4.4 El recogido de lo guardado por fuera

> Escrito el 2026-08-17 en la fase [`A-EP-005-HU-007`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-007-recoger-lo-guardado-por-fuera/A-EP-005-HU-007-retrodocumentar-el-recogido-de-lo-guardado-por-fuera/resultado_pruebas.md).

27. **Al abrir la sesión y al escribir un archivo, lo que quedó en el almacén de la herramienta se mueve al repositorio.** El almacén tiene que quedar vacío: dos copias del mismo recuerdo terminan diciendo cosas distintas, y manda la que nadie puede leer. Baja de [`EP-005 · HU-007`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-007-recoger-lo-guardado-por-fuera/HU-007-recoger-lo-guardado-por-fuera.md).
28. **Nunca se borra: se mueve.** Si el nombre ya está ocupado en el repositorio, entra como `<nombre>-local.md` y decide el usuario cuál manda. Una versión anterior borraba el idéntico «porque no se pierde nada» y destruyó memoria real. Baja de [`EP-005 · HU-007`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-007-recoger-lo-guardado-por-fuera/HU-007-recoger-lo-guardado-por-fuera.md).
29. **Los nombres que solo difieren en mayúsculas son el mismo archivo.** En Windows lo son de verdad, y mover uno sobre otro se llevaría el índice sin decir nada. Baja de [`EP-005 · HU-007`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-007-recoger-lo-guardado-por-fuera/HU-007-recoger-lo-guardado-por-fuera.md).
30. **Con el almacén enlazado a la carpeta del repositorio, no hay nada que mover:** son el mismo archivo, y compararlos daría idéntico siempre. Baja de [`EP-005 · HU-007`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-007-recoger-lo-guardado-por-fuera/HU-007-recoger-lo-guardado-por-fuera.md).

### 4.5 El checkpoint de la fase se reclama solo

> Escrito el 2026-08-20 en la fase [`A-EP-005-HU-013`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-013-el-checkpoint-se-reclama-solo/A-EP-005-HU-013-el-enganche-del-checkpoint/README.md).

32. **Tres documentos marcan una puerta:** `plan_trabajo.md`, `resultado_pruebas.md` y `funcionalidad_implementada.md`. Escribir cualquier otro archivo no dispara nada. Baja de [`EP-005 · HU-013`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-013-el-checkpoint-se-reclama-solo/HU-013-el-checkpoint-se-reclama-solo.md).
33. **Al escribir uno de esos tres dentro de una fase se mira su `estado-fase.md`:** si falta, o si su última escritura es anterior a la del documento, se avisa nombrando la fase y el documento. Baja de [`EP-005 · HU-013`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-013-el-checkpoint-se-reclama-solo/HU-013-el-checkpoint-se-reclama-solo.md).
34. **Se comparan fechas, no contenido.** Decir en qué estación va la fase es criterio; el programa no escribe ni lee el checkpoint. Baja de [`EP-005 · HU-013`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-013-el-checkpoint-se-reclama-solo/HU-013-el-checkpoint-se-reclama-solo.md).
35. **No detiene el trabajo:** sale siempre con código 0. Baja de [`EP-005 · HU-013`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-013-el-checkpoint-se-reclama-solo/HU-013-el-checkpoint-se-reclama-solo.md).

### 4.6 El consumo de la sesión se ve mientras se puede actuar

> Escrito el 2026-08-20 en la fase [`A-EP-005-HU-014`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-014-el-consumo-se-ve-a-tiempo/A-EP-005-HU-014-el-aviso-por-tramo/README.md), que además le da historia al reporte de cierre que la 27.0.0 construyó sin cadena.

36. **Al terminar cada respuesta se reporta el total de la sesión:** turnos, fichas de entrada, de salida y leídas de caché. Baja de [`EP-005 · HU-014`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-014-el-consumo-se-ve-a-tiempo/HU-014-el-consumo-se-ve-a-tiempo.md).
37. **En cada mensaje se mira si el último turno cruzó un tramo**, y si lo cruzó se avisa una vez, diciendo cuánto va y qué tramo se pasó. El cruce se decide comparando el total con y sin el último turno: sin estado compartido. Baja de [`EP-005 · HU-014`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-014-el-consumo-se-ve-a-tiempo/HU-014-el-consumo-se-ve-a-tiempo.md).
38. **El tramo por defecto es un millón de fichas de entrada más salida, sin caché.** Salió de medir ocho sesiones reales (de 144 mil a 12,7 millones): avisa de cero a doce veces según el tamaño, y ninguna sesión corta lo cruza. Se cambia con un argumento. Baja de [`EP-005 · HU-014`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-014-el-consumo-se-ve-a-tiempo/HU-014-el-consumo-se-ve-a-tiempo.md).
39. **Mide, no detiene.** Sin transcripción, o con una ilegible, calla y sale con 0. Baja de [`EP-005 · HU-014`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-014-el-consumo-se-ve-a-tiempo/HU-014-el-consumo-se-ve-a-tiempo.md).

### 4.7 El veredicto se copia solo

> Escrito el 2026-08-20 en la fase [`C-EP-005-HU-003`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-003-disparo-al-escribir-un-archivo/C-EP-005-HU-003-el-veredicto-se-copia-solo/README.md).

40. **Al escribir el `resultado_pruebas.md` de una fase con concepto en su §6, el veredicto se copia a la fila de la fase en el §8 de su historia y a los README de la fase y de la historia.** Se copia lo que el §6 dice, con las mismas expresiones con que `fases.py` lo lee para pasar la puerta. Baja de [`EP-005 · HU-003`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-003-disparo-al-escribir-un-archivo/HU-003-disparo-al-escribir-un-archivo.md).
41. **Un resultado sin concepto no se propaga.** Un borrador no es un veredicto; copiarlo pondría «no ejecutado» en la historia a cada guardado. Baja de [`EP-005 · HU-003`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-003-disparo-al-escribir-un-archivo/HU-003-disparo-al-escribir-un-archivo.md).
42. **El `estado-fase.md` no se toca:** es el checkpoint y lo escribe el agente. Baja de [`EP-005 · HU-003`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-003-disparo-al-escribir-un-archivo/HU-003-disparo-al-escribir-un-archivo.md).
43. **Si no hay dónde copiarlo, se dice.** Callar se leería como hecho. Baja de [`EP-005 · HU-003`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-003-disparo-al-escribir-un-archivo/HU-003-disparo-al-escribir-un-archivo.md).

## 5. Modelo de datos

No aplica porque el entregable son programas de línea de comandos sobre archivos de texto: no hay entidades, tablas ni catálogos.

## 6. Comportamiento y flujos

**Al abrir la sesión, qué reglas llegan.** El enganche de apertura recorre `base/` en orden de precedencia, y de cada archivo decide por el primer tramo de su ruta: si empieza por `00-` o `01-`, entrega el texto completo; si no, una línea de índice con la ruta, el peso y el título. Después entrega las dos partes con su encabezado, para que se sepa cuál rige ya y cuál hay que abrir. Medido el 2026-08-15 sobre este repositorio: 73 KB completos de 369 KB que existen.

**Al abrir la sesión y en cada mensaje del usuario.** El enganche mira si existe el resumen del día para esa sesión. Si no está y la transcripción ya nació, lo crea con el modelo y sin hallazgos. Los dos momentos hacen lo mismo a propósito: al abrir, la transcripción de una sesión nueva todavía no existe, así que ahí no hay de dónde sacarle el nombre. El turno en que el archivo nace muestra dónde quedó; los avisos empiezan en el siguiente.

**La carpeta la deja el instalador.** `historico-chat/resumenes/` llega puesta con su índice, como el histórico y la memoria. Sin ella el enganche calla, y eso sigue siendo lo correcto para un proyecto que no instaló el estándar.

**Al declararse el propósito.** Cuando la sesión dice qué hallazgo viene a resolver —en su «viene de»—, el enganche va a buscarlo, y muestra ese hallazgo y lo que siga abierto de él. Nada de otros temas: una sesión abierta para una cosa no tiene por qué ver las demás.

**Durante la sesión.** Cada vez que el usuario manda un mensaje, el enganche pregunta si la sesión ya produjo algo. Si sí, mira qué le falta al resumen y avisa lo que encuentre, una vez cada cosa:

| Qué falta | Qué imprime |
|---|---|
| Ningún hallazgo escrito | Que el resumen está vacío, y dónde está el archivo |
| Hay hallazgos, pero no dice si la sesión se puede cerrar | Cuáles son los hallazgos del propósito que siguen sin resolver |

Cada aviso deja su marca en el propio resumen, así que no se repite. Dos avisos como máximo en toda la sesión.

**Al ponerle nombre a la sesión.** El renombrado mueve los dos archivos, la transcripción y el resumen, y corrige la línea del índice con el enlace nuevo.

**Camino de error.** Si el enganche no puede escribir —carpeta sin permisos, disco lleno—, imprime el motivo y sale con código 0. La sesión sigue. Un enganche que detiene el trabajo es peor que el problema que resuelve.

## 7. Interfaz / UI

No aplica: se ve como un mensaje en la sesión, no como pantalla.

## 8. Permisos y autorización

No aplica porque no hay servicio ni autenticación.

| Permiso | Quién lo tiene | Qué habilita |
|---|---|---|
| Ninguno | — | — |

## 9. Marco normativo

No aplica: el módulo no toca datos personales ni ninguna norma externa.

## 10. Plan de pruebas

El detalle vive en el [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/A-EP-005-HU-008-enganche-del-resumen/plan_pruebas.md](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/A-EP-005-HU-008-enganche-del-resumen/plan_pruebas.md) de la fase. En resumen:

- **Caso feliz:** se abre una sesión y el archivo aparece, con el modelo y sin hallazgos.
- **Casos límite:** dos sesiones el mismo día, una sesión que no produce nada, un resumen que ya tiene hallazgos.
- **Errores:** carpeta sin permiso de escritura; el aviso no se repite; el enganche no toca lo ya escrito.
- **Triangulación:** que la sesión "produjo algo" se comprueba por dos caminos independientes, el commit y el cambio en `base/`.
- **Verificación manual ([`08·T4`](../../base\08-pruebas.md#t4--protege-los-datos-reales-al-probar)):** que el aviso se lea como ayuda y no como ruido. Eso no lo mide ningún programa.

## 11. Criterios de aceptación (Definition of Done)

- [x] El archivo del resumen se crea solo al abrir la sesión.
- [x] Se renombra junto con la transcripción, y el índice queda al día.
- [x] Avisa qué falta, una vez por cada cosa, cuando la sesión produjo algo.
- [x] Lo que sigue abierto del propósito se muestra al abrir la sesión.
- [x] No escribe hallazgos, no modifica los escritos y no detiene la sesión.
- [x] Pruebas verdes, incluida la triangulación de "produjo algo".
- [ ] Trazabilidad especificación → implementación sin faltantes ([`13·DOC3`](../../base/13-documentacion/reglas/DOC3-verifica-la-trazabilidad-especificacion-implementacion-antes-de-cerrar.md)).
- [ ] Entrada en `CHANGELOG.md` y subida de `VERSION` ([`20·M10`](../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)).

## 12. Decisiones tomadas

- **`2026-08-14` — el enganche crea, avisa y arrastra; no escribe hallazgos.** Reconocer un hallazgo es criterio. Lo que un programa sí puede hacer es que el hueco se vea.
- **`2026-08-14` — el resumen se crea al abrir la sesión, no al cerrarla.** Un chat no tiene final: lo que se deja para el cierre no se escribe. Es la misma lección de la transcripción.
- **`2026-08-14` — el aviso sale una vez por cada cosa que falta, no una por sesión.** Se descartó el aviso único porque dejaba pasar el caso real: escribir un hallazgo y no decir nunca si la sesión se puede cerrar. Son dos como máximo.
- **`2026-08-14` — el aviso dice qué falta, con la lista.** Un aviso genérico obliga a preguntar qué falta, y preguntar es lo que se quiere evitar.
- **`2026-08-14` — para cerrar cuentan los hallazgos del propósito de la sesión.** Cada sesión se abre para resolver algo. Lo que aparece y no es de ese propósito se cierra en otra, y acá basta con dejarlo anotado.
- **`2026-08-14` — se muestra solo lo abierto del propósito de la sesión.** Se descartó mostrar todo lo abierto del repositorio: una sesión que trabaja un tema no tiene por qué ver los hallazgos de otro, y ese ruido es lo que hace que los avisos se dejen de leer. Sin límite de días: el hallazgo del propósito se busca donde esté.
- **`2026-08-14` — el enganche nunca detiene el trabajo.** Sale con código 0 pase lo que pase, igual que los siete que ya existen.

## 13. Trazabilidad (se completa al implementar)

| Ítem de la especificación | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| RN-01 · el archivo se crea en el primer mensaje | programa | `validadores/resumen.py` | ✅ | CP-010 |
| RN-02 · se renombra con la transcripción | programa | `validadores/historico.py` | ✅ | CP-003 |
| RN-03 · avisa qué falta, una vez por hueco | programa | `validadores/hook_resumen.py` | ✅ | CP-004 y CP-007 |
| RN-04 a RN-06 · qué falta, qué cuenta para cerrar, y lo abierto del propósito | programa | `validadores/resumen.py` | ✅ | CP-006 |
| RN-07 a RN-09 · límites del enganche | programa | `validadores/hook_resumen.py` | ✅ | CP-009 |
| Instalación en cada proyecto | programa | `validadores/instalar.py` | ✅ | Los dos enganches en `.claude/settings.json` |
| RN-10 a RN-12 · qué llega completo y qué llega en índice | programa | `validadores/cargador.py` | ✅ | CP-001 de la fase A de HU-009 |
| RN-13 · se dice cuál rige ya y cuál hay que abrir | programa | `validadores/cargador.py` | ✅ | CP-002 de esa fase |
| RN-14 · un capítulo nuevo entra solo | programa | `validadores/cargador.py` | ✅ | CP-001, paso 4 |
| RN-15 · con el gate sin pasar llega solo esa regla | programa | `validadores/cargador.py` | ✅ | CP-005 de esa fase |
| RN-16 · el motivo de no cargarlo todo queda escrito | documentación | Esta especificación, §4.1 | ✅ | — |
| RN-31 · al propio estándar le llegan las reglas | programa | `adaptadores/claude-code/hook_sesion.py` | ✅ | CP-001 a CP-003 de la fase B de HU-009, y el caso `arranque-reglas-en-el-estandar` de `evals/` |
| RN-32 y RN-33 · qué dispara y qué se mira | programa | `validadores/checkpoint.py` | ✅ | CP-001 a CP-004 de la fase A de HU-013 |
| RN-34 · fechas, no contenido; no escribe | programa | `validadores/checkpoint.py` | ✅ | CP-005 y CP-007 de esa fase |
| RN-35 · no detiene | programa | `adaptadores/claude-code/hook_checkpoint.py` | ✅ | CP-006 de esa fase |
| RN-36 · el reporte de cierre | programa | `adaptadores/claude-code/hook_presupuesto.py` | ✅ | CP-001 de la fase A de HU-014 |
| RN-37 y RN-38 · el aviso por tramo y el tramo por defecto | programa | `validadores/presupuesto.py` | ✅ | CP-002 a CP-004 y CP-006 de esa fase |
| RN-39 · mide, no detiene | programa | `adaptadores/claude-code/hook_presupuesto.py` | ✅ | CP-005 de esa fase |
| RN-40 a RN-42 · el veredicto se copia, el borrador no, el checkpoint no se toca | programa | `validadores/veredicto.py` | ✅ | CP-001 a CP-004 de la fase C de HU-003 |
| RN-43 · si no hay dónde, se dice | programa | `adaptadores/claude-code/hook_veredicto.py` | ✅ | CP-006 de esa fase |

## 14. Cruces con otros módulos

**Qué consume este módulo de otros:**

| Módulo | Qué consume | Por qué |
|---|---|---|
| `documentos-modelo` | El modelo `plantillas/sesion.md` | Es lo que copia al crear el archivo |
| `instalador` | `validadores/instalar.py` | Es quien conecta el enganche en cada proyecto |

**Historial cruzado — quién consume de este módulo:**

| Fecha | Módulo que consume | Qué cambió acá por eso |
|---|---|---|
| Ninguno | — | — |
