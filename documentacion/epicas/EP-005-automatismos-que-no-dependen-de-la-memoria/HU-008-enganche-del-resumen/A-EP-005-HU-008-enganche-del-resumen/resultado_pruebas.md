# Resultado de pruebas — Fase A-EP-005-HU-008-enganche-del-resumen

**Para qué sirve este documento.** Dice **qué se ejecutó y cuánto dio**. El plan de pruebas no se toca al correrlo: la línea base aprobada se queda como está y lo que pasó se escribe acá. Sin este documento, una exigencia no se puede dar por cumplida.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-005-HU-008-enganche-del-resumen` |
| **HU** | [HU-008](../HU-008-enganche-del-resumen.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) · PP-A-EP-005-HU-008 v1.1 |
| **Ciclo** | 2. El 1 quedó anulado y se conserva en §8 |
| **Fecha de ejecución** | Ciclo 1: 2026-08-14. Ciclo 2: 2026-08-14, con la fase reabierta |
| **Ejecutado por** | Cimiento, con el usuario aprobando el plan |
| **Ambiente y versión** | Carpetas temporales instaladas con el instalador, y este repositorio para las mediciones. Estándar 15.4.1 |

---

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 9 | 9 | 3 | 0 | 0 | 0 |
| 2 | 9 | 8 | 8 | 0 | 0 | 1 |

**Casos no ejecutados y por qué:** [CP-018](plan_pruebas.md#cp-018--el-archivo-aparece-solo-en-una-sesión-real), el único que no se puede automatizar: hay que abrir una sesión nueva de verdad en este repositorio y mirar si el archivo aparece solo. Queda para la próxima sesión, y hasta entonces no se cuenta como aprobado.

**Del ciclo 1, seis de sus nueve aprobados quedaron anulados**, no fallidos: no probaron lo que decían. El detalle está en §8.

---

## 2. Ejecución caso por caso

> Los casos de esta sección son los de la [corrida 2](plan_pruebas.md#61-corrida-2--los-mismos-criterios-disparados-de-verdad): cada uno dispara el enganche como orden del sistema, con el mismo JSON que le manda Claude Code, sobre un proyecto que arma el instalador. Ninguna precondición se monta a mano.

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

**Los pasos, qué tenía que pasar en cada uno y qué salió:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Abrir la sesión | Todavía no hay resumen: la conversación no está guardada | No dijo nada y no escribió nada |
| 2 | Escribir el primer mensaje | Aparece el archivo de la conversación | Apareció. La carpeta de los resúmenes seguía vacía: **acá se quedaba antes** |
| 3 | Dejar que corra lo que corre en cada mensaje | Aparece el resumen, con el mismo nombre | Apareció, y dijo dónde había quedado |
| 4 | Abrir ese archivo | Trae el formulario en blanco y ningún hallazgo escrito | Así llegó |
| 5 | Mirar la lista del día | La sesión aparece ahí, una sola vez | Una sola vez |

**Detalle de CP-011**

**El problema que resuelve:** que un proyecto que hereda a Cimiento tenga dónde guardar el resumen, sin que nadie cree carpetas a mano.

**La precondición:** una carpeta nueva, sin nada instalado.

**Los pasos, qué tenía que pasar en cada uno y qué salió:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Instalar Cimiento en esa carpeta | Queda creada la carpeta de los resúmenes, con su índice | Quedó creada, con su índice |
| 2 | Instalar otra vez | No pisa lo que haya adentro | No volvió a escribir el índice que ya estaba |

**Detalle de CP-012**

**El problema que resuelve:** que dos sesiones del mismo día no se pisen.

**La precondición:** la misma de CP-010, con una sesión que ya tiene su resumen.

**Los pasos, qué tenía que pasar en cada uno y qué salió:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Abrir una segunda sesión el mismo día y escribir su primer mensaje | Aparece su propio archivo | Apareció, con el nombre de su conversación |
| 2 | Mirar el de la primera | Sigue igual | Siguió igual |

**Detalle de CP-013**

**El problema que resuelve:** que los enlaces del resumen lleven a algún lado en cualquier proyecto, no solo en este repositorio.

**La precondición:** el resumen que nació en CP-010, dentro de un proyecto que hereda a Cimiento.

**Los pasos, qué tenía que pasar en cada uno y qué salió:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Buscar en el archivo la mención al modelo, que antes iba enlazada | Ya no está | Ya no está |
| 2 | Seguir cada enlace del encabezado | Todos llegan a un archivo que existe | Los dos llegaron |

**Detalle de CP-014**

**El problema que resuelve:** que el hueco se avise mientras se trabaja, y no al cerrar, que es cuando ya nadie escribe.

**La precondición:** la sesión de CP-010, con su resumen recién nacido y todavía vacío.

**Los pasos, qué tenía que pasar en cada uno y qué salió:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Escribir un archivo en el proyecto y dejarlo listo para guardar | El proyecto queda con algo producido | Quedó con un cambio pendiente |
| 2 | Mandar otro mensaje en la sesión | Avisa que el resumen sigue sin un solo hallazgo, y dice cuál es el archivo | Avisó, con el archivo |

**Detalle de CP-015**

**El problema que resuelve:** que quien retoma un tema vea lo que quedó abierto de ese tema, y no los de otros.

**La precondición:** dos resúmenes con hallazgos abiertos, de temas distintos, y una sesión que declara cuál viene a resolver.

**Los pasos, qué tenía que pasar en cada uno y qué salió:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Escribir en el resumen de la sesión de cuál hallazgo viene | Queda declarado el propósito | Quedó declarado |
| 2 | Abrir la sesión | Muestra ese hallazgo y su pregunta viva | Los mostró |
| 3 | Leer lo que mostró | El hallazgo del otro tema no aparece | No apareció |

**Detalle de CP-016**

**El problema que resuelve:** que lo escrito a mano en el resumen no lo borre ni lo duplique el programa que corre en cada mensaje.

**La precondición:** un resumen con un hallazgo escrito a mano.

**Los pasos, qué tenía que pasar en cada uno y qué salió:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Abrir otra vez la sesión y mandar otro mensaje | El texto sigue igual | Siguió igual |
| 2 | Mirar la lista del día | La sesión aparece una sola vez | Una sola vez |

**Detalle de CP-017**

**El problema que resuelve:** que Cimiento no se meta donde no lo llamaron: un proyecto que no lo instaló no debe verse afectado.

**La precondición:** una carpeta vacía, sin nada instalado.

**Los pasos, qué tenía que pasar en cada uno y qué salió:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Abrir una sesión ahí y mandar un mensaje | No escribe nada, no dice nada y el trabajo sigue | No escribió ni dijo nada, y terminó bien |
| 2 | Mirar la carpeta | Sigue vacía | Siguió vacía |

**Detalle de la medición del arranque** (RNF-03, con el histórico real de 37 sesiones): `--modo inicio` 0,12 s y `--modo aviso` 0,12 s, contra 0,14 s de `hook_sesion.py`, que ya corría.

**Corrida de la suite:** `python validadores/pruebas.py EngancheDelResumenPorElCaminoReal` → 10 casos, `OK`. La suite completa queda en 236 casos con una falla ajena, la de las citas de `base/09-git.md` y `base/glosario.md`, que está escribiendo otra sesión. `validar.py estandar`: 0 fallas, 4 avisos, los cuatro de esos mismos archivos ajenos.

---

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | La cadena completa de [CP-010](plan_pruebas.md#cp-010--el-resumen-aparece-solo-en-una-sesión-nueva), paso por paso | A mano, sobre una carpeta temporal instalada, corriendo cada enganche como orden del sistema | El archivo apareció en el paso 4, y no antes |
| 2 | Lo que suma al arranque | Midiendo los dos modos contra este repositorio, con sus 37 sesiones | 0,12 s cada uno, contra 0,14 s del enganche que ya corría |
| 3 | [CP-018](plan_pruebas.md#cp-018--el-archivo-aparece-solo-en-una-sesión-real): que en una sesión real el archivo aparezca solo | Abriendo una sesión nueva en este repositorio | **Sin verificar todavía.** Se ve en la próxima sesión |

---

## 4. Defectos encontrados

| ID | Título | Caso | Severidad | Estado |
|---|---|---|---|---|
| DEF-01 | El primer intento copiaba al resumen nuevo los hallazgos de ejemplo del modelo, así que el archivo nacía con un `H-1` que nadie escribió | [CP-001](plan_pruebas.md#cp-001--el-archivo-nace-al-abrir-la-sesión) | Alta | Corregido en la misma fase: el archivo nuevo copia la sección de cierre y no los ejemplos |
| DEF-02 | La búsqueda del propósito no reconocía el hallazgo cuando venía escrito como enlace, que es como lo escribe el modelo | [CP-006](plan_pruebas.md#cp-006--se-muestra-lo-abierto-del-propósito-y-nada-de-otros-temas) | Alta | Corregido |
| DEF-03 | **El resumen no nacía nunca.** Al abrir la sesión la transcripción todavía no existe, y de su nombre sale el del resumen: `inicio()` se salía sin crear, y `aviso()` también, porque el archivo no estaba | [CP-010](plan_pruebas.md#cp-010--el-resumen-aparece-solo-en-una-sesión-nueva) | Crítica | Corregido al reabrir la fase: los dos modos aseguran el archivo |
| DEF-04 | En un proyecto que hereda el estándar no había dónde crearlo: el instalador nunca dejaba `historico-chat/resumenes/` | [CP-011](plan_pruebas.md#cp-011--el-instalador-deja-el-proyecto-listo) | Alta | Corregido: lo deja el instalador |
| DEF-05 | El encabezado del resumen enlazaba `plantillas/sesion.md`, ruta que solo existe en el estándar: en todo proyecto heredero nacía roto | [CP-013](plan_pruebas.md#cp-013--el-encabezado-no-enlaza-a-nada-que-no-exista) | Media | Corregido: enlaza el índice del histórico del proyecto |

DEF-01 y DEF-02 los encontró la propia suite. **DEF-03 no lo encontró nadie hasta la sesión siguiente**, y esa es la parte que importa: la suite de la corrida 1 no podía encontrarlo, porque probaba la pieza y no el camino. Lo destapó el usuario preguntando si lo hecho se podía replicar a otro proyecto.

**Defectos abiertos que se aceptan y por qué:** ninguno. Los cinco están corregidos.

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| [CA-01](../HU-008-enganche-del-resumen.md#ca-01--el-archivo-nace-solo) · el archivo nace solo | CP-010, CP-011, CP-012, CP-013, CP-003 y CP-018 | Todo en verde salvo CP-018, que no se ha corrido | **No** |
| [CA-02](../HU-008-enganche-del-resumen.md#ca-02--avisa-cuando-la-sesión-ya-produjo-algo-y-el-resumen-sigue-vacío) · avisa qué falta | CP-014 y CP-005 | Avisa lo que falta y calla cuando no falta nada | Sí |
| [CA-03](../HU-008-enganche-del-resumen.md#ca-03--del-propósito-se-muestra-lo-que-sigue-abierto-y-nada-más) · lo abierto del propósito | CP-015 | Muestra el del propósito y no el de otro tema | Sí |
| [RNF-01](../HU-008-enganche-del-resumen.md#5-requisitos-no-funcionales) · avisa durante la sesión | CP-014 | El aviso sale en un turno intermedio | Sí |
| [RNF-02](../HU-008-enganche-del-resumen.md#5-requisitos-no-funcionales) · una vez por cada cosa | CP-016 | No repite ni duplica | Sí |
| [RNF-03](../HU-008-enganche-del-resumen.md#5-requisitos-no-funcionales) · no demora el arranque | La medición de §3 | Suma menos que el enganche que ya corría | Sí |
| Transversales · no toca, no estorba, no detiene | CP-016 y CP-017 | No pisa lo escrito y no se mete donde no lo llaman | Sí |

**Los que no cumplen:** CA-01. Le falta [CP-018](plan_pruebas.md#cp-018--el-archivo-aparece-solo-en-una-sesión-real), y no se traslada a otra fase: se corre al abrir la próxima sesión de este repositorio.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias con caso | Plan §5 | 100% | 100%: 7 de 7 | Sí |
| Casos automatizados | Plan §12 | 85% o más | 89%: 8 de 9 de la corrida 2 | Sí |
| Avisos por sesión cuando falta el resumen | Plan §12 | 2 como máximo | 2, uno por hueco | Sí |
| Enlaces rotos en el índice tras renombrar | Plan §12 | 0 | 0 | Sí |
| Lo que suma al arranque | Plan §12 | Que no se note | 0,12 s cada modo | Sí |
| Criterios de salida | Plan §9 | Todos | Falta la corrida manual en una sesión real | **No** |

**Lo que no se cumplió:** el criterio de salida que pide la comprobación en una sesión de verdad. No se acepta como está: la fase espera.

---

## 6. Veredicto de la fase

**Concepto:** **No cumple**, todavía.

**Justificación:** todo lo que se puede automatizar está en verde, y la cadena real se corrió a mano paso por paso sobre un proyecto instalado. Pero CA-01 tiene un caso sin correr, y ese caso es justo el que el ciclo 1 dio por hecho sin hacerlo nunca.

**Qué falta para que cumpla:** abrir una sesión nueva en este repositorio y ver que el archivo del resumen aparece solo.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Casos automatizados del ciclo 2 | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `EngancheDelResumenPorElCaminoReal` |
| EV-02 | Corrida de la suite | 10 casos de esa clase en verde; la suite completa en 236 casos con una falla ajena, de `base/09-git.md` y `base/glosario.md`, que escribe otra sesión |
| EV-03 | Comprobación del estándar | `validar.py estandar`: 0 fallas, 4 avisos, los cuatro de esos mismos archivos ajenos |
| EV-04 | Corrida a mano de la cadena completa | §3, verificación 1 |
| EV-05 | Casos del ciclo 1 | Los mismos programas, antes de la corrección |

---

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-08-14 | 3 de 9; los otros 6, anulados | 0 | Se corrigieron tres defectos, y las pruebas pasaron a disparar el enganche en vez de llamar la función |

> ### Por qué se anuló el ciclo 1
>
> **Seis de los nueve casos no probaron lo que decían.** CP-001, CP-002, CP-004, CP-005, CP-006 y CP-007 se corrieron llamando por dentro a la función que el enganche usa, con la transcripción y la carpeta puestas a mano. Ese estado no ocurre nunca: al abrir la sesión la transcripción todavía no existe, así que el archivo del resumen **no nacía**.
>
> **Siguen en pie** CP-003, CP-008 y CP-009: el renombrado se corrió con su orden real, y los otros dos no dependen del archivo.
>
> **No se abrió una fase nueva: se reabrió esta.** Lo del ciclo 1 se conserva tal cual, sin corregirle los números: es la evidencia de cómo pasó.

**Casos del ciclo 1**

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

**Los pasos, qué tenía que pasar en cada uno y qué salió:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Abrir una sesión y escribir el primer mensaje | En la carpeta de los resúmenes aparece el archivo de esa sesión, con el mismo nombre con que quedó guardada la conversación | **No se abrió ninguna sesión.** Se le pidió el archivo al programa, dándole ya escrito el nombre de una conversación inventada. Apareció |
| 2 | Abrir ese archivo | Trae el formulario en blanco: los espacios por llenar y ningún hallazgo escrito | Así llegó: en blanco y sin ningún hallazgo |
| 3 | Abrir una segunda sesión el mismo día | Aparece su propio archivo, y el de la primera sigue igual | No se hizo: ese paso se dejó para otro caso |
| 4 | Escribir algo adentro y seguir trabajando | Lo escrito sigue ahí, y en la lista del día cada sesión aparece una sola vez | Se le volvió a pedir el archivo, sobre uno que ya tenía algo escrito. No lo tocó |

**Detalle de CP-002**

**El problema que resuelve:** que dos sesiones del mismo día no se pisen, porque el resumen se guarda por día.

**La precondición:** una carpeta con Cimiento instalado y una sesión que ya tiene su resumen del día.

**Los pasos, qué tenía que pasar en cada uno y qué salió:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Abrir dos sesiones el mismo día, con nombres distintos | Aparecen dos archivos en la carpeta del día | **No se abrió ninguna sesión.** Se le pidieron los dos archivos al programa, con nombres de conversaciones inventadas. Aparecieron los dos |
| 2 | Mirar el primero | Sigue como estaba, sin tocar | Siguió igual |

**Detalle de CP-003**

**El problema que resuelve:** que al ponerle nombre a la sesión no quede un índice apuntando a un archivo que ya no está.

**La precondición:** una sesión sin tema todavía, con su conversación guardada y su resumen ya creado.

**Los pasos, qué tenía que pasar en cada uno y qué salió:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Ponerle tema a la sesión con la orden de renombrar | La conversación y el resumen quedan con el nombre nuevo | Los dos quedaron con el nombre nuevo |
| 2 | Mirar el índice del histórico | La línea apunta a los dos archivos nuevos, y ninguno de los enlaces está roto | Apunta a los dos, sin enlaces rotos |
| 3 | Repetirlo con una sesión que no tiene resumen | No falla: renombra la conversación y no inventa el enlace | Renombró la conversación y no inventó nada |

**Detalle de CP-004**

**El problema que resuelve:** que el hueco se avise mientras se trabaja, cuando la sesión ya produjo algo, y no al cerrar, que es cuando ya nadie escribe.

**La precondición:** una sesión con su resumen vacío y un cambio hecho en el proyecto.

**Los pasos, qué tenía que pasar en cada uno y qué salió:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Dejar un cambio guardado en el proyecto, con el resumen vacío | El proyecto queda con algo producido | **El resumen se puso a mano:** en una sesión de verdad ese archivo no existía |
| 2 | Mandar otro mensaje en la sesión | Avisa que no hay ningún hallazgo y dice cuál es el archivo | Avisó, y dijo cuál es el archivo |
| 3 | Escribir un hallazgo y mandar otro mensaje | No repite el primer aviso; avisa que falta decir si la sesión se puede cerrar | No lo repitió, y avisó lo otro |
| 4 | Llenar la parte del cierre y seguir | No avisa nada | No avisó |
| 5 | Repetirlo por el otro camino: cambiar una regla sin guardar | El aviso sale igual | Sin control de versiones no hay ninguno de los dos caminos, y calló. Es lo que la HU pide en su límite; lo que estaba mal era el resultado que esperaba el plan |
| 6 | Mirar cuándo salió el aviso | Durante la sesión, no al cerrarla | Durante la sesión |

**Detalle de CP-005**

**El problema que resuelve:** que el aviso no se vuelva ruido: si no falta nada, no dice nada.

**La precondición:** resúmenes en los tres estados que no deben avisar.

**Los pasos, qué tenía que pasar en cada uno y qué salió:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Una sesión que no produjo nada, con el resumen vacío | No avisa | **Los resúmenes se pusieron a mano.** No avisó |
| 2 | Una sesión con sus hallazgos escritos y la parte del cierre llena | No avisa | No avisó |
| 3 | Una sesión con un hallazgo abierto que no es de su propósito, y el cierre lleno | No avisa: ese se cierra en otra sesión | No avisó |

**Detalle de CP-006**

**El problema que resuelve:** que quien retoma un tema vea lo que quedó abierto de ese tema, y no los de otros.

**La precondición:** dos temas con hallazgos abiertos, en días distintos, y una sesión que declara cuál viene a resolver.

**Los pasos, qué tenía que pasar en cada uno y qué salió:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Abrir la sesión con su propósito declarado | Se muestra el hallazgo del propósito, con su archivo y su pregunta viva | **Los resúmenes se pusieron a mano.** Lo mostró, con su pregunta viva |
| 2 | Mirar el hallazgo abierto del otro tema | No aparece | No apareció |
| 3 | Poner el propósito en un hallazgo de hace una semana | Aparece igual: lo que acota es el tema, no la fecha | Apareció igual |
| 4 | Cerrarlo y abrir otra sesión con el mismo propósito | Ya no aparece | Dejó de aparecer |

**Detalle de CP-007**

**El problema que resuelve:** que el mismo aviso no salga en cada mensaje, porque un aviso repetido se deja de leer.

**La precondición:** una sesión con su resumen vacío.

**Los pasos, qué tenía que pasar en cada uno y qué salió:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Mandar dos mensajes seguidos con lo mismo faltando | El aviso sale una sola vez | **El resumen se puso a mano.** Salió una sola vez |
| 2 | Provocar las dos cosas que pueden faltar a lo largo de la sesión | Salen dos avisos en total, no más | Salieron dos |
| 3 | Mirar dónde quedó la marca de que ya se avisó | Dentro del propio resumen, no en un archivo aparte | Dentro del propio resumen |

**Detalle de CP-008**

**El problema que resuelve:** que abrir una sesión no se vuelva más lento por esto.

**La precondición:** este repositorio, con su histórico real.

**Los pasos, qué tenía que pasar en cada uno y qué salió:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Medir el arranque con el enganche que ya existía | Un número de partida | 0,26 segundos |
| 2 | Medir los dos nuevos | La diferencia no se nota al abrir la sesión | 0,13 y 0,23 segundos: menos que lo que ya había |

**Detalle de CP-009**

**El problema que resuelve:** que Cimiento no borre lo escrito, no se meta donde no lo llamaron y no corte el trabajo.

**La precondición:** un resumen con hallazgos escritos, una carpeta sin histórico y una carpeta donde no se puede escribir.

**Los pasos, qué tenía que pasar en cada uno y qué salió:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correrlo sobre un resumen con hallazgos escritos | Ni una línea cambia | No cambió ninguna |
| 2 | Correrlo en un proyecto sin carpeta de resúmenes | No hace nada y no falla | No hizo nada y no falló |
| 3 | Correrlo donde no se puede escribir | Avisa el motivo y la sesión sigue | Avisa y sigue |
