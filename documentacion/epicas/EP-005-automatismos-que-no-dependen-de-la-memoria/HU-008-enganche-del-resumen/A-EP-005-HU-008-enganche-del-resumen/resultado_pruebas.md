# Resultado de pruebas — Fase A-EP-005-HU-008-enganche-del-resumen

**Para qué sirve este documento.** Dice **qué se ejecutó y cuánto dio**. El plan de pruebas no se toca al correrlo: la línea base aprobada se queda como está y lo que pasó se escribe acá. Sin este documento, una exigencia no se puede dar por cumplida.

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-005-HU-008-enganche-del-resumen` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md) · PP-A-EP-005-HU-008 v1.0 |
| **Fecha de ejecución** | 2026-08-14 |
| **Ejecutado por** | Cimiento, con el usuario aprobando el plan |

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
| [CP-001](plan_pruebas.md#cp-001--el-archivo-nace-al-abrir-la-sesión) | CA-01 | `2026-08-14-maracuya.md` en un proyecto temporal con `plantillas/sesion.md` de tres líneas | Cumple | 2 casos de la suite |
| [CP-002](plan_pruebas.md#cp-002--dos-sesiones-el-mismo-día-no-se-pisan) | CA-01 | `2026-08-14-maracuya.md` y `2026-08-14-pepito.md`, el mismo día | Cumple | 1 caso de la suite |
| [CP-003](plan_pruebas.md#cp-003--el-renombrado-mueve-los-dos-archivos) | CA-01 | `historico.py --renombrar 2026-08-14-sesion.md --tema "maracuya"`, con su resumen `sesion.md` ya creado. Y el caso contrario: la misma orden sobre una sesión sin resumen | Cumple | 2 casos de la suite y una corrida a mano |
| [CP-004](plan_pruebas.md#cp-004--avisa-qué-falta-cuando-la-sesión-produjo-algo) | CA-02 · RNF-01 | Un resumen con `# lo que quedó` y nada más; después el mismo con un `### H-1` y la casilla de cierre en `☐`. La detección de "produjo algo", contra este repositorio y contra una carpeta sin git | Cumple | 2 casos de la suite y 2 corridas de `_produjo_algo()` |
| [CP-005](plan_pruebas.md#cp-005--calla-cuando-no-hay-nada-que-avisar) | CA-02 | Un resumen con `### H-1 · algo`, estado `resuelto acá` y la casilla de cierre en `☑` | Cumple | 1 caso de la suite |
| [CP-006](plan_pruebas.md#cp-006--se-muestra-lo-abierto-del-propósito-y-nada-de-otros-temas) | CA-03 | `**Viene de:** 2026-08-14 · maracuya · H-4`, con `maracuya.md` abierto y `otro-tema.md` con un `H-9` abierto que no debe salir. Y el caso real de esta sesión: el `H-4` de `hu-de-la-comprobacion-automatica` | Cumple | 3 casos de la suite y la corrida real |
| [CP-007](plan_pruebas.md#cp-007--el-aviso-no-se-repite) | RNF-02 | El mismo resumen vacío, consultado dos veces seguidas, con `marcar_avisado()` entre medio | Cumple | 2 casos de la suite |
| [CP-008](plan_pruebas.md#cp-008--no-demora-el-arranque) | RNF-03 | Este repositorio, con 35 sesiones en el histórico: 0,13 s el de arranque y 0,23 s el del aviso, contra 0,26 s de `hook_sesion.py` | Cumple | Medición a mano |
| [CP-009](plan_pruebas.md#cp-009--no-toca-lo-escrito-no-se-mete-donde-no-lo-llaman-y-no-detiene) | Transversales | Una carpeta temporal sin `historico-chat/`; y la revisión de `main()`, que sale con 0 pase lo que pase | Cumple | 1 caso de la suite y lectura del código |

**Detalle de CP-001**

1. Se pidió crear el resumen de una sesión llamada `2026-08-14-maracuya.md`, en un proyecto de prueba. Apareció el archivo `resumenes/2026-08-14/maracuya.md`, que es donde el plan decía que tenía que estar.
2. Se abrió: trae los campos del modelo y ningún hallazgo, como pedía el plan.
3. Se pidió crearlo otra vez, sobre un resumen que ya tenía escrito un hallazgo. No lo tocó.

**Cumple** porque los tres pasos dieron lo que el plan esperaba: el archivo nace solo, nace vacío y no pisa lo que ya está.

**Detalle de CP-002**

1. Se crearon los resúmenes de dos sesiones del mismo día, `maracuya` y `pepito`. Quedaron los dos archivos en la carpeta del día.
2. Se releyó el primero: sin cambios.

**Cumple** porque dos sesiones del mismo día quedan en dos archivos y ninguna pisa a la otra.

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

> El paso 5 salió distinto de lo que decía el plan, que pedía que el segundo camino avisara igual que el primero. Sin git no existe ninguno de los dos caminos, y callar es lo que la propia HU pide en su límite: un proyecto que no lleva git no se ve afectado. Lo que estaba mal era el resultado esperado del plan, no el comportamiento.

**Detalle de CP-005**

1. Sesión que no produjo nada y resumen vacío: no avisó.
2. Resumen con su hallazgo escrito y la sección de cierre llena: no avisó.

**Cumple** porque calla cuando no hay nada que avisar, que es lo que lo separa del ruido.

**Detalle de CP-006**

1. Una sesión que declara como propósito el `H-4` de otra: el enganche lo encontró y trajo su pregunta viva.
2. En el mismo día había otro hallazgo abierto, de otro tema: no apareció.
3. Se marcó ese `H-4` como resuelto: dejó de aparecer.
4. Se corrió contra esta sesión real: encontró `H-4 · No había dónde escribir lo aprendido` en el resumen de la sesión donde nació.

**Cumple** porque muestra lo que sigue abierto del propósito y nada de otros temas.

**Detalle de CP-007**

1. Se consultó dos veces seguidas un resumen vacío, con el aviso marcado en medio: salió una sola vez.
2. Se provocaron las dos cosas que pueden faltar a lo largo de la sesión: salieron dos avisos, no más.
3. Se miró dónde quedó la marca: dentro del propio resumen.

**Cumple** porque cada aviso sale una vez y la marca vive donde vive el dato.

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

## 3. Defectos encontrados

| ID | Título | Caso | Severidad | Estado |
|---|---|---|---|---|
| DEF-01 | El primer intento copiaba al resumen nuevo los hallazgos de ejemplo del modelo, así que el archivo nacía con un `H-1` que nadie escribió | [CP-001](plan_pruebas.md#cp-001--el-archivo-nace-al-abrir-la-sesión) | Alta | Corregido en la misma fase: el archivo nuevo copia la sección de cierre y no los ejemplos |
| DEF-02 | La búsqueda del propósito no reconocía el hallazgo cuando venía escrito como enlace, que es como lo escribe el modelo | [CP-006](plan_pruebas.md#cp-006--se-muestra-lo-abierto-del-propósito-y-nada-de-otros-temas) | Alta | Corregido |

Los dos los encontró la propia suite antes de dar la fase por buena. DEF-01 es el que importaba: un programa que escribe un hallazgo falso rompe justo lo que la HU declara fuera de alcance.

---

## 4. Métricas

| Métrica | Meta | Obtenido |
|---|---|---|
| Cobertura de exigencias | 100% | 100%: 7 de 7 con caso ejecutado |
| Casos automatizados | ≥ 85% | 89%: 8 de 9 en la suite; CP-008 se mide a mano |
| Avisos por sesión cuando falta el resumen | 2 como máximo | 2 como máximo, uno por hueco |
| Enlaces rotos en el índice tras renombrar | 0 | 0 |
| Lo que suma al arranque | Que no se note | 0,13 s |
| Casos nuevos en la suite | — | 14 |

---

## 5. Verificación por exigencia

| Exigencia | Veredicto | De dónde sale |
|---|---|---|
| [CA-01](../HU-008-enganche-del-resumen.md#ca-01--el-archivo-nace-solo) · el archivo nace solo | **Cumple** | CP-001, CP-002 y CP-003 |
| [CA-02](../HU-008-enganche-del-resumen.md#ca-02--avisa-cuando-la-sesión-ya-produjo-algo-y-el-resumen-sigue-vacío) · avisa qué falta | **Cumple** | CP-004 y CP-005 |
| [CA-03](../HU-008-enganche-del-resumen.md#ca-03--del-propósito-se-muestra-lo-que-sigue-abierto-y-nada-más) · lo abierto del propósito | **Cumple** | CP-006 |
| [RNF-01](../HU-008-enganche-del-resumen.md#5-requisitos-no-funcionales) · avisa durante la sesión | **Cumple** | CP-004 |
| [RNF-02](../HU-008-enganche-del-resumen.md#5-requisitos-no-funcionales) · una vez por cada cosa | **Cumple** | CP-007 |
| [RNF-03](../HU-008-enganche-del-resumen.md#5-requisitos-no-funcionales) · no demora el arranque | **Cumple** | CP-008 |
| Transversales · no toca, no estorba, no detiene | **Cumple** | CP-009 |

---

## 6. Concepto final

**Cumple.** Las siete exigencias quedaron verificadas y los dos defectos que aparecieron se corrigieron dentro de la fase.

**Un aparte sobre la suite completa.** `validadores/pruebas.py` termina con 226 casos y **una** falla, y no es de esta fase: otra sesión está escribiendo la regla `G9` en `base/09-git.md`, y el capítulo de meta-reglas usa `G9` como ejemplo inventado. Al existir la regla, la comprobación de citas empezó a leer ese ejemplo como una cita real. Se deja anotado sin tocar: el archivo es de esa sesión.
