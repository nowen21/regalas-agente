# Resultado de pruebas — Fase A-EP-005-HU-008-enganche-del-resumen

**Para qué sirve este documento.** Dice **qué se ejecutó y cuánto dio**. El plan de pruebas no se toca al correrlo: la línea base aprobada se queda como está y lo que pasó se escribe acá. Sin este documento, una exigencia no se puede dar por cumplida.

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-005-HU-008-enganche-del-resumen` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md) · PP-A-EP-005-HU-008 v1.0 |
| **Fecha de ejecución** | 2026-08-14 |
| **Ejecutado por** | Cimiento, con el usuario aprobando el plan |

> ## ⚠ Corrida 1 anulada · la fase se reabrió el 2026-08-14
>
> **Seis de los nueve casos no probaron lo que decían.** CP-001, CP-002, CP-004, CP-005, CP-006 y CP-007 se corrieron llamando por dentro a `resumen.crear()`, con la transcripción y la carpeta puestas a mano, en vez de disparar el enganche. Ese estado no ocurre nunca: al abrir la sesión la transcripción todavía no existe, así que el archivo del resumen **no nacía**, y todo lo que esos casos daban por cierto partía de un archivo que nadie creaba.
>
> Con eso, [CA-01](../HU-008-enganche-del-resumen.md#ca-01--el-archivo-nace-solo), [CA-02](../HU-008-enganche-del-resumen.md#ca-02--avisa-cuando-la-sesión-ya-produjo-algo-y-el-resumen-sigue-vacío) y [CA-03](../HU-008-enganche-del-resumen.md#ca-03--del-propósito-se-muestra-lo-que-sigue-abierto-y-nada-más) quedaron **sin probar**, y CA-01 además **no cumplía**.
>
> **Siguen en pie de la corrida 1** CP-003, CP-008 y CP-009: el renombrado se corrió con su orden real, y los otros dos no dependen del archivo.
>
> **No se abrió una fase nueva: se reabrió esta.** El veredicto bueno es el de la corrida 2, más abajo, con el enganche disparado como orden del sistema. Lo de la corrida 1 se conserva tal cual, sin corregirle los números: es la evidencia de cómo pasó.

---

## 1. Línea base antes de ejecutar

| Medida | Valor de partida |
|---|---|
| Enganches conectados | 7 |
| Enganches que sostienen el resumen | 0 |
| Resúmenes escritos hasta hoy | 2, los dos a mano |
| Qué mueve `renombrar()` | Solo la transcripción |
| Sesiones en el histórico | 35 |

---

## 2. Casos ejecutados

| Caso | Exigencia | Con qué se probó | Veredicto | Evidencia |
|---|---|---|---|---|
| [CP-001](plan_pruebas.md#cp-001--el-archivo-nace-al-abrir-la-sesión) | CA-01 | `2026-08-14-maracuya.md` en un proyecto temporal con `plantillas/sesion.md` de tres líneas | **Anulado** | 2 casos de la suite |
| [CP-002](plan_pruebas.md#cp-002--dos-sesiones-el-mismo-día-no-se-pisan) | CA-01 | `2026-08-14-maracuya.md` y `2026-08-14-pepito.md`, el mismo día | **Anulado** | 1 caso de la suite |
| [CP-003](plan_pruebas.md#cp-003--el-renombrado-mueve-los-dos-archivos) | CA-01 | `historico.py --renombrar 2026-08-14-sesion.md --tema "maracuya"`, con su resumen `sesion.md` ya creado. Y el caso contrario: la misma orden sobre una sesión sin resumen | Cumple | 2 casos de la suite y una corrida a mano |
| [CP-004](plan_pruebas.md#cp-004--avisa-qué-falta-cuando-la-sesión-produjo-algo) | CA-02 · RNF-01 | Un resumen con `# lo que quedó` y nada más; después el mismo con un `### H-1` y la casilla de cierre en `☐`. La detección de "produjo algo", contra este repositorio y contra una carpeta sin git | **Anulado** | 2 casos de la suite y 2 corridas de `_produjo_algo()` |
| [CP-005](plan_pruebas.md#cp-005--calla-cuando-no-hay-nada-que-avisar) | CA-02 | Un resumen con `### H-1 · algo`, estado `resuelto acá` y la casilla de cierre en `☑` | **Anulado** | 1 caso de la suite |
| [CP-006](plan_pruebas.md#cp-006--se-muestra-lo-abierto-del-propósito-y-nada-de-otros-temas) | CA-03 | `**Viene de:** 2026-08-14 · maracuya · H-4`, con `maracuya.md` abierto y `otro-tema.md` con un `H-9` abierto que no debe salir. Y el caso real de esta sesión: el `H-4` de `hu-de-la-comprobacion-automatica` | **Anulado** | 3 casos de la suite y la corrida real |
| [CP-007](plan_pruebas.md#cp-007--el-aviso-no-se-repite) | RNF-02 | El mismo resumen vacío, consultado dos veces seguidas, con `marcar_avisado()` entre medio | **Anulado** | 2 casos de la suite |
| [CP-008](plan_pruebas.md#cp-008--no-demora-el-arranque) | RNF-03 | Este repositorio, con 35 sesiones en el histórico: 0,13 s el de arranque y 0,23 s el del aviso, contra 0,26 s de `hook_sesion.py` | Cumple | Medición a mano |
| [CP-009](plan_pruebas.md#cp-009--no-toca-lo-escrito-no-se-mete-donde-no-lo-llaman-y-no-detiene) | Transversales | Una carpeta temporal sin `historico-chat/`; y la revisión de `main()`, que sale con 0 pase lo que pase | Cumple | 1 caso de la suite y lectura del código |

**Detalle de CP-001**

**El problema que resuelven [CA-01](../HU-008-enganche-del-resumen.md#ca-01--el-archivo-nace-solo) y [CP-001](plan_pruebas.md#cp-001--el-archivo-nace-al-abrir-la-sesión) es:** que el archivo del resumen nunca falte. Nace solo, vacío y con el modelo puesto.

**La precondición:** una carpeta nueva y vacía, con Cimiento instalado y sin ningún resumen de hoy.

**Qué había que ver para darlo por cumplido:**

| # | Qué hacer | Qué tiene que pasar |
|---|---|---|
| 1 | Abrir una sesión y escribir el primer mensaje | En la carpeta de los resúmenes aparece el archivo de esa sesión, con el mismo nombre con que quedó guardada la conversación |
| 2 | Abrir ese archivo | Trae el formulario en blanco: los espacios por llenar y ningún hallazgo escrito |
| 3 | Abrir una segunda sesión el mismo día | Aparece su propio archivo, y el de la primera sigue igual |
| 4 | Escribir algo adentro y seguir trabajando | Lo escrito sigue ahí, y en la lista del día cada sesión aparece una sola vez |

**Y para darlo por reprobado**, basta una de estas cuatro:

| # | Qué hacer | Con qué queda reprobado |
|---|---|---|
| 1 | Abrir una sesión y escribir el primer mensaje | En la carpeta de los resúmenes no hay ningún archivo |
| 2 | Abrir el archivo recién creado | Trae un hallazgo escrito que nadie escribió |
| 3 | Abrir una segunda sesión el mismo día | No aparece su archivo, o el de la primera quedó pisado |
| 4 | Escribir algo adentro y seguir trabajando | Lo escrito se borró, o la sesión quedó dos veces en la lista del día |

**Los pasos que se siguieron para comprobar esa solución son los siguientes:**

1. En vez de abrir una sesión, se le pidió al programa que hiciera el archivo, dándole ya escrito el nombre de una conversación inventada. **Salió:** apareció el archivo.
2. Se abrió ese archivo y se contaron los hallazgos escritos adentro. **Salió:** ninguno, con el formulario en blanco.
3. Se le volvió a pedir lo mismo, sobre un archivo que ya tenía algo escrito. **Salió:** no lo tocó.
4. No se abrió ninguna segunda sesión del mismo día: ese paso se dejó para otro caso.

**Anulado.** Nunca se abrió una sesión, que es el paso 1 del caso: se le pidió el archivo directamente al programa y se le dio hecho el dato que él no tiene al abrir, el nombre de la conversación. Con una sesión de verdad, el archivo no aparecía. Es el paso 1 de la tabla de reprobados, y así estuvo desde que la fase cerró. Lo prueba bien [CP-010](plan_pruebas.md#cp-010--el-resumen-aparece-solo-en-una-sesión-nueva).

**Detalle de CP-002**

1. Se crearon los resúmenes de dos sesiones del mismo día, `maracuya` y `pepito`. Quedaron los dos archivos en la carpeta del día.
2. Se releyó el primero: sin cambios.

**Cumple** porque dos sesiones del mismo día quedan en dos archivos y ninguna pisa a la otra.

**Anulado.** Los dos archivos se pidieron por dentro al programa, sin abrir ninguna sesión. Lo prueba [CP-012](plan_pruebas.md#cp-012--dos-sesiones-el-mismo-día-no-se-pisan).

**Detalle de CP-003**

1. Se renombró una sesión que ya tenía su resumen, con el comando `historico.py --renombrar … --tema "maracuya"`. Quedaron con el nombre nuevo **los dos** archivos, la transcripción y el resumen.
2. Se miró el índice del día: apunta al nombre nuevo.
3. Se miró el índice del histórico: la línea trae los dos enlaces y ninguno está roto.
4. Se repitió con una sesión **sin** resumen: renombró la transcripción, no falló y no inventó el enlace.

**Cumple** porque los dos archivos se mueven juntos y los dos índices quedan al día, que era lo que podía dejar todo a medias.

**Detalle de CP-004**

1. Con un resumen vacío y la sesión ya con cambios sin guardar, el enganche avisó que no hay ningún hallazgo y dijo cuál es el archivo.
2. Se escribió un hallazgo y se volvió a correr: no repitió el primer aviso, y avisó lo otro, que falta decir si la sesión se puede cerrar.
3. Se llenó la sección de cierre: dejó de avisar.
4. Se comprobó cuándo sale: durante la sesión, en el turno, no al cerrarla.
5. Se probó el otro camino de "la sesión produjo algo", sobre una carpeta sin git: no hay señal, y el enganche calla.

**Cumple** porque avisa lo que falta, una vez por cada cosa, y deja de avisar cuando ya no falta.

**Anulado.** El aviso se probó sobre un resumen puesto a mano, y ese archivo no existía nunca en una sesión de verdad. Lo prueba [CP-014](plan_pruebas.md#cp-014--avisa-qué-falta-cuando-la-sesión-produjo-algo).

> El paso 5 salió distinto de lo que decía el plan, que pedía que el segundo camino avisara igual que el primero. Sin git no existe ninguno de los dos caminos, y callar es lo que la propia HU pide en su límite: un proyecto que no lleva git no se ve afectado. Lo que estaba mal era el resultado esperado del plan, no el comportamiento.

**Detalle de CP-005**

1. Sesión que no produjo nada y resumen vacío: no avisó.
2. Resumen con su hallazgo escrito y la sección de cierre llena: no avisó.

**Cumple** porque calla cuando no hay nada que avisar, que es lo que lo separa del ruido.

**Anulado** por lo mismo que CP-004: el resumen del que parte lo puso el que probaba.

**Detalle de CP-006**

1. Una sesión que declara como propósito el `H-4` de otra: el enganche lo encontró y trajo su pregunta viva.
2. En el mismo día había otro hallazgo abierto, de otro tema: no apareció.
3. Se marcó ese `H-4` como resuelto: dejó de aparecer.
4. Se corrió contra esta sesión real: encontró `H-4 · No había dónde escribir lo aprendido` en el resumen de la sesión donde nació.

**Cumple** porque muestra lo que sigue abierto del propósito y nada de otros temas.

**Anulado.** Se leyó de resúmenes puestos a mano. Lo prueba [CP-015](plan_pruebas.md#cp-015--del-propósito-se-muestra-lo-abierto-y-nada-de-otros-temas).

**Detalle de CP-007**

1. Se consultó dos veces seguidas un resumen vacío, con el aviso marcado en medio: salió una sola vez.
2. Se provocaron las dos cosas que pueden faltar a lo largo de la sesión: salieron dos avisos, no más.
3. Se miró dónde quedó la marca: dentro del propio resumen.

**Cumple** porque cada aviso sale una vez y la marca vive donde vive el dato.

**Anulado.** Mismo motivo. Lo prueba [CP-016](plan_pruebas.md#cp-016--correr-los-dos-modos-no-pisa-ni-duplica).

**Detalle de CP-008**

1. Se midió el arranque con el enganche que ya existía: 0,26 segundos.
2. Se midieron los dos nuevos: 0,13 y 0,23 segundos.

**Cumple** porque lo nuevo suma menos que lo que ya había, así que no se nota.

**Detalle de CP-009**

1. Se corrieron los enganches sobre un resumen con hallazgos escritos: ni una línea cambió.
2. Se corrieron en una carpeta sin histórico: no hicieron nada y no fallaron.
3. Se revisó el camino del error: cualquier fallo se avisa y la sesión sigue.

**Cumple** porque no toca lo escrito, no se mete donde no lo llaman y no detiene el trabajo.

---

## 2.1 Corrida 2 — el enganche disparado de verdad · 2026-08-14

**Qué cambió respecto de la corrida 1.** Ningún caso llama a `resumen.crear()`. Cada uno corre el enganche como orden del sistema operativo, con el JSON que le manda Claude Code por la entrada estándar, sobre una carpeta temporal que pasó por `instalar.py --aplicar`. La transcripción no se escribe a mano: la escribe `hook_historico.py`.

| Caso | Exigencia | Veredicto | Evidencia |
|---|---|---|---|
| [CP-010](plan_pruebas.md#cp-010--el-resumen-aparece-solo-en-una-sesión-nueva) | CA-01 | Cumple | 3 casos de la suite |
| [CP-011](plan_pruebas.md#cp-011--el-instalador-deja-el-proyecto-listo) | CA-01 | Cumple | 2 casos de la suite |
| [CP-012](plan_pruebas.md#cp-012--dos-sesiones-el-mismo-día-no-se-pisan) | CA-01 | Cumple | 1 caso de la suite |
| [CP-013](plan_pruebas.md#cp-013--el-encabezado-no-enlaza-a-nada-que-no-exista) | CA-01 | Cumple | 1 caso de la suite |
| [CP-014](plan_pruebas.md#cp-014--avisa-qué-falta-cuando-la-sesión-produjo-algo) | CA-02 | Cumple | 1 caso de la suite |
| [CP-015](plan_pruebas.md#cp-015--del-propósito-se-muestra-lo-abierto-y-nada-de-otros-temas) | CA-03 | Cumple | 1 caso de la suite |
| [CP-016](plan_pruebas.md#cp-016--correr-los-dos-modos-no-pisa-ni-duplica) | RNF-02 | Cumple | 1 caso de la suite |
| [CP-017](plan_pruebas.md#cp-017--un-proyecto-sin-instalar-no-se-ve-afectado) | Transversales | Cumple | 1 caso de la suite |
| [CP-018](plan_pruebas.md#cp-018--el-archivo-aparece-solo-en-una-sesión-real) | CA-01 | **Sin correr** | Necesita una sesión nueva de verdad |

**Detalle de CP-010**

**El problema que resuelve:** que el archivo del resumen nunca falte. Nace solo, vacío y con el modelo puesto.

**La precondición:** una carpeta nueva y vacía, con Cimiento instalado y sin ningún resumen de hoy.

**Para que cumpla:**

1. Abrir una sesión y escribir el primer mensaje. Aparece el archivo del resumen en la carpeta del día, con el mismo nombre con que quedó guardada la conversación.
2. Abrir ese archivo. Trae el formulario en blanco y ningún hallazgo escrito.
3. Mirar la lista del día. La sesión aparece ahí, una sola vez.

**Reprueba si:** después de escribir el primer mensaje no hay archivo; o el archivo nace con un hallazgo que nadie escribió; o la sesión no queda en la lista del día.

**Los pasos que se siguieron:**

1. Instalar Cimiento en una carpeta temporal recién creada. **Salió:** quedó la carpeta donde viven los resúmenes.
2. Avisarle que se abre la sesión. **Salió:** no dijo nada y no hizo nada, porque todavía no hay conversación guardada.
3. Escribir el primer mensaje de la sesión. **Salió:** apareció el archivo de la conversación. La carpeta de los resúmenes seguía vacía: **acá se quedaba antes**.
4. Dejar que corra lo que corre en cada mensaje. **Salió:** apareció el archivo del resumen, con el mismo nombre, y Cimiento dijo dónde había quedado.

**Cumple.** El paso 3 es la prueba del defecto viejo: la sesión llegaba hasta ahí y el archivo no existía nunca.

**Detalle de CP-011**

**El problema que resuelve:** que un proyecto que hereda a Cimiento tenga dónde guardar el resumen, sin que nadie cree carpetas a mano.

**La precondición:** una carpeta nueva, sin nada instalado.

**Para que cumpla:** instalar Cimiento y que quede creada la carpeta de los resúmenes con su índice. Instalar otra vez y que no pise lo que haya adentro.

**Reprueba si:** después de instalar no está la carpeta, o si al reinstalar se borra lo que ya había.

**Los pasos que se siguieron:**

1. Instalar Cimiento en una carpeta temporal. **Salió:** entre lo que hizo, creó la carpeta de los resúmenes y su índice.
2. Instalar una segunda vez. **Salió:** no volvió a escribir el índice que ya estaba.

**Cumple.**

**Detalle de CP-012**

**El problema que resuelve:** que dos sesiones del mismo día no se pisen, porque el resumen se guarda por día.

**La precondición:** la misma de CP-010, y una sesión ya con su resumen.

**Para que cumpla:** abrir una segunda sesión el mismo día y que aparezca su propio archivo, con el de la primera intacto.

**Reprueba si:** la segunda escribe encima de la primera, o si no aparece.

**Los pasos que se siguieron:**

1. Hacer lo de CP-010 con una sesión, y después con otra distinta el mismo día. **Salió:** dos archivos, cada uno con el nombre de su conversación, y el primero sin tocar.

**Cumple.**

**Detalle de CP-013**

**El problema que resuelve:** que los enlaces del resumen lleven a algún lado en cualquier proyecto, no solo en este repositorio.

**La precondición:** un resumen recién nacido en un proyecto que hereda a Cimiento.

**Para que cumpla:** seguir cada enlace del encabezado y llegar a un archivo que existe.

**Reprueba si:** algún enlace apunta a una carpeta que solo existe en el repositorio del estándar.

**Los pasos que se siguieron:**

1. Buscar en el archivo la mención al modelo que antes iba enlazado. **Salió:** ya no está.
2. Seguir los dos enlaces del encabezado desde la carpeta donde vive el archivo. **Salió:** los dos llegan a un archivo que existe.

**Cumple.**

**Detalle de CP-014**

**El problema que resuelve:** que el hueco se avise mientras se trabaja, y no al cerrar, que es cuando ya nadie escribe.

**La precondición:** una sesión con su resumen recién nacido, todavía vacío.

**Para que cumpla:** hacer un cambio de verdad en el proyecto y que en el mensaje siguiente Cimiento avise que el resumen sigue sin un solo hallazgo.

**Reprueba si:** no avisa, o si avisa sin decir qué falta.

**Los pasos que se siguieron:**

1. Escribir un archivo en el proyecto y dejarlo listo para guardar. **Salió:** el proyecto quedó con un cambio pendiente.
2. Mandar otro mensaje en la sesión. **Salió:** avisó que el resumen de esa sesión sigue vacío, y dijo dónde está el archivo.

**Cumple.**

**Detalle de CP-015**

**El problema que resuelve:** que quien retoma un tema vea lo que quedó abierto de **ese** tema, sin que le aparezcan los de otros.

**La precondición:** dos resúmenes con hallazgos abiertos, de temas distintos, y una sesión que declara cuál viene a resolver.

**Para que cumpla:** al abrir, Cimiento muestra el hallazgo declarado y su pregunta viva, y no nombra el del otro tema.

**Reprueba si:** no muestra el declarado, o si muestra el ajeno.

**Los pasos que se siguieron:**

1. Dejar un resumen con un hallazgo abierto y otro, de tema distinto, también abierto. Escribir en la sesión de cuál viene. **Salió:** los tres archivos en la carpeta del día.
2. Avisarle que se abre la sesión. **Salió:** mostró el hallazgo declarado y su pregunta viva.
3. Leer lo que mostró. **Salió:** el hallazgo del otro tema no aparece.

**Cumple.**

**Detalle de CP-016**

**El problema que resuelve:** que lo escrito a mano en el resumen no lo borre ni lo duplique el programa que corre en cada mensaje.

**La precondición:** un resumen con un hallazgo escrito a mano.

**Para que cumpla:** correr otra vez lo de la apertura y lo de cada mensaje, y que el texto siga igual y la lista del día no gane una línea repetida.

**Reprueba si:** el texto se pierde, o la sesión queda dos veces en la lista.

**Los pasos que se siguieron:**

1. Escribir un hallazgo a mano y volver a correr las dos cosas. **Salió:** el texto sigue ahí y la lista del día nombra el archivo una sola vez.

**Cumple.**

**Detalle de CP-017**

**El problema que resuelve:** que Cimiento no se meta donde no lo llamaron: un proyecto que no lo instaló no debe verse afectado.

**La precondición:** una carpeta vacía, sin instalar nada.

**Para que cumpla:** correr las dos cosas y que no escriba nada ni diga nada, y que la sesión siga.

**Reprueba si:** crea carpetas, o imprime un aviso, o corta el trabajo.

**Los pasos que se siguieron:**

1. Correr lo de la apertura y lo de cada mensaje sobre la carpeta vacía. **Salió:** no escribió nada, no dijo nada y terminó bien.

**Cumple.**

**Detalle de la medición del arranque** (RNF-03, con el histórico real de 37 sesiones): `--modo inicio` 0,12 s y `--modo aviso` 0,12 s, contra 0,14 s de `hook_sesion.py`, que ya corría.

**Corrida de la suite:** `python validadores/pruebas.py EngancheDelResumenPorElCaminoReal` → 10 casos, `OK`. La suite completa queda en 236 casos con una falla ajena, la de las citas de `base/09-git.md` y `base/glosario.md`, que está escribiendo otra sesión. `validar.py estandar`: 0 fallas, 4 avisos, los cuatro de esos mismos archivos ajenos.

---

## 3. Defectos encontrados

| ID | Título | Caso | Severidad | Estado |
|---|---|---|---|---|
| DEF-01 | El primer intento copiaba al resumen nuevo los hallazgos de ejemplo del modelo, así que el archivo nacía con un `H-1` que nadie escribió | [CP-001](plan_pruebas.md#cp-001--el-archivo-nace-al-abrir-la-sesión) | Alta | Corregido en la misma fase: el archivo nuevo copia la sección de cierre y no los ejemplos |
| DEF-02 | La búsqueda del propósito no reconocía el hallazgo cuando venía escrito como enlace, que es como lo escribe el modelo | [CP-006](plan_pruebas.md#cp-006--se-muestra-lo-abierto-del-propósito-y-nada-de-otros-temas) | Alta | Corregido |
| DEF-03 | **El resumen no nacía nunca.** Al abrir la sesión la transcripción todavía no existe, y de su nombre sale el del resumen: `inicio()` se salía sin crear, y `aviso()` también, porque el archivo no estaba | [CP-010](plan_pruebas.md#cp-010--el-resumen-aparece-solo-en-una-sesión-nueva) | Crítica | Corregido al reabrir la fase: los dos modos aseguran el archivo |
| DEF-04 | En un proyecto que hereda el estándar no había dónde crearlo: el instalador nunca dejaba `historico-chat/resumenes/` | [CP-011](plan_pruebas.md#cp-011--el-instalador-deja-el-proyecto-listo) | Alta | Corregido: lo deja el instalador |
| DEF-05 | El encabezado del resumen enlazaba `plantillas/sesion.md`, ruta que solo existe en el estándar: en todo proyecto heredero nacía roto | [CP-013](plan_pruebas.md#cp-013--el-encabezado-no-enlaza-a-nada-que-no-exista) | Media | Corregido: enlaza el índice del histórico del proyecto |

DEF-01 y DEF-02 los encontró la propia suite. **DEF-03 no lo encontró nadie hasta la sesión siguiente**, y esa es la parte que importa: la suite de la corrida 1 no podía encontrarlo, porque probaba la pieza y no el camino. Lo destapó el usuario preguntando si lo hecho se podía replicar a otro proyecto.

---

## 4. Métricas

| Métrica | Meta | Obtenido |
|---|---|---|
| Cobertura de exigencias | 100% | 100%: 7 de 7 con caso ejecutado en la corrida 2 |
| Casos automatizados | ≥ 85% | 89%: 8 de 9 de la corrida 2 en la suite; CP-018 solo se puede correr en una sesión real |
| Avisos por sesión cuando falta el resumen | 2 como máximo | 2 como máximo, uno por hueco |
| Enlaces rotos en el índice tras renombrar | 0 | 0 |
| Enlaces rotos en el resumen que nace en un proyecto heredero | 0 | 0, después de DEF-05 |
| Lo que suma al arranque | Que no se note | 0,12 s cada modo, contra 0,14 s del enganche que ya corría |
| Casos nuevos en la suite | — | 14 en la corrida 1, 10 más en la corrida 2 |

---

## 5. Verificación por exigencia

| Exigencia | Veredicto | De dónde sale |
|---|---|---|
| [CA-01](../HU-008-enganche-del-resumen.md#ca-01--el-archivo-nace-solo) · el archivo nace solo | **Cumple en lo automatizado; falta CP-018** | CP-010 a CP-013 y CP-003 |
| [CA-02](../HU-008-enganche-del-resumen.md#ca-02--avisa-cuando-la-sesión-ya-produjo-algo-y-el-resumen-sigue-vacío) · avisa qué falta | **Cumple** | CP-014 y CP-005 |
| [CA-03](../HU-008-enganche-del-resumen.md#ca-03--del-propósito-se-muestra-lo-que-sigue-abierto-y-nada-más) · lo abierto del propósito | **Cumple** | CP-015 |
| [RNF-01](../HU-008-enganche-del-resumen.md#5-requisitos-no-funcionales) · avisa durante la sesión | **Cumple** | CP-014 |
| [RNF-02](../HU-008-enganche-del-resumen.md#5-requisitos-no-funcionales) · una vez por cada cosa | **Cumple** | CP-016 |
| [RNF-03](../HU-008-enganche-del-resumen.md#5-requisitos-no-funcionales) · no demora el arranque | **Cumple** | La medición de la corrida 2 |
| Transversales · no toca, no estorba, no detiene | **Cumple** | CP-016 y CP-017 |

> Los veredictos de arriba son los de la **corrida 2**. Los de la corrida 1 quedaron anulados y no se cuentan.

---

## 6. Concepto final

**Todavía no cumple: falta [CP-018](plan_pruebas.md#cp-018--el-archivo-aparece-solo-en-una-sesión-real).** Todo lo que se puede automatizar está en verde, y la cadena real se corrió a mano paso por paso sobre un proyecto instalado. Lo que falta es lo único que no se puede simular: que en una sesión nueva de este repositorio el archivo aparezca solo.

**No se declara cumplida antes de eso**, y esa es la lección de la corrida 1: la fase se cerró sin haber abierto una sola sesión de verdad. La fase se cierra cuando CP-018 pase, en la próxima sesión.

**Un aparte sobre la suite completa.** `validadores/pruebas.py` termina con 236 casos y **una** falla, que no es de esta fase: otra sesión está escribiendo `base/09-git.md` y `base/glosario.md`, y de ahí salen las citas que la comprobación reporta. Se deja anotado sin tocar: esos archivos son de esa sesión.
