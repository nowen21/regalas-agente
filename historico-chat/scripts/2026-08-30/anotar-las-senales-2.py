# -*- coding: utf-8 -*-
"""Agrega las senales de la segunda tanda de la sesion, S-086 a S-089."""
import io
import os

RAIZ = r"c:\Ing. Jose\ia\agente"
R = os.path.join(RAIZ, "documentacion", "senales.md")

NUEVAS = u"""
## S-086 · Un reclamo que sale siempre es el que se aprende a ignorar  ·  error-resuelto · activa
- **What:** el reclamo de que una entidad inmutable no tiene su permiso salía en **todo proyecto con una entidad inmutable**, desde hacía meses. El patrón se declara como `anular_<recurso>` y la expresión se arma reemplazando el marcador **sobre el texto ya escapado**: hasta Python 3.6 `re.escape` escapaba los ángulos y el reemplazo encajaba; desde 3.7 no. La expresión quedaba literal y no encontraba ningún permiso.
- **Why:** el daño no es el falso positivo: es **lo que le enseña al que lo lee**. Un veredicto que sale siempre deja de leerse, y con él dejan de leerse los que sí eran ciertos. Es el mismo mecanismo por el que un enganche que estorba se apaga en una tarde.
- **Also:** se rompió **en silencio y sin tocar el código**. Nadie editó esa línea: cambió lo que hacía una función de la biblioteca estándar por debajo. Una prueba lo habría cazado el día del cambio de versión, y no la había.
- **And:** apareció al **provocar** el criterio en un proyecto de prueba, no al leerlo. Los cinco criterios de esa historia llevaban trece días sin ejecutarse, y el defecto llevaba meses.
- **Where:** `validadores/entidades.py`, `recursos_con_permiso` · la fase `A-EP-004-HU-010-declaracion-y-comprobacion`.
- **Learned:** cuando un reemplazo depende de **cómo quedó** un texto después de pasar por otra función, se busca lo mismo que se transformó (`re.escape("<recurso>")`) en vez de escribir a mano el resultado esperado. Y todo validador merece la pregunta: **¿este reclamo puede salir siempre?** Si puede, hay que probar el caso en que no debe salir.
- **When/Who:** 2026-08-30 · agente, al ejecutar los cinco criterios de `EP-004·HU-010`.
- **Scope:** estándar; aplica a toda comprobación que arme una expresión desde un patrón declarado.
- **Rel:** S-083 (un cero que salía de no mirar se publicó como limpio), S-082 (el aviso disparó y no cambió nada).

## S-087 · Un caso mal armado se lee igual que un programa roto  ·  aprendizaje · activa
- **What:** al provocar los criterios de `EP-004·HU-010`, las dos primeras vueltas dieron «no cumple» y el programa tenía razón: la declaración de prueba nombraba los estados por el **nombre de la columna** cuando se buscan como **valores entre comillas**, y el patrón del permiso iba **sin su marcador**. El proyecto de prueba tampoco era un repositorio, y las comprobaciones solo miran lo versionado.
- **Why:** el resultado se lee idéntico en los dos casos: «el programa no reporta lo que debería». Acusar al programa cuando el caso está mal armado lleva a «arreglar» lo que funcionaba, y eso sí rompe.
- **Also:** la tercera vuelta sí encontró un defecto de verdad (`S-086`). Las tres se distinguen por lo mismo: **mirar qué espera el programa antes de acusarlo**.
- **And:** que el proyecto de prueba no fuera un repositorio no dio error: dio **cero hallazgos**, que se lee como «todo bien». El silencio otra vez.
- **Where:** `historico-chat/scripts/2026-08-30/provocar-los-ca-de-hu010.py`.
- **Learned:** antes de reportar que una comprobación no reporta, hay que leer **qué busca exactamente**: qué formato, en qué archivos y bajo qué condición. Y el caso de prueba se arma con las mismas exigencias que el real, incluida la de estar versionado.
- **When/Who:** 2026-08-30 · agente.
- **Scope:** estándar; aplica a toda provocación de un criterio en un proyecto de prueba.
- **Rel:** S-086 (el reclamo que salía siempre), S-081 (las cifras las mide un programa).

## S-088 · El fallo esperado es la única nota que reclama sola  ·  patrón · activa
- **What:** cinco fases anteriores encontraron defectos que **no podían arreglar**, porque su plan aprobado declaraba no tocar el programa. En vez de anotarlo en prosa, dejaron la prueba escrita y marcada como **fallo esperado**. Al arreglarlos el 2026-08-30, la corrida reportó «éxitos inesperados» y obligó a volver a destapar cada una.
- **Why:** un defecto anotado en un documento se pierde: nadie relee el §6 de una fase cerrada. Uno anotado como fallo esperado **reclama solo el día que deja de ser cierto**, y no hay forma de cerrarlo sin verlo.
- **Also:** funcionó cinco veces el mismo día, en dos archivos de pruebas distintos. Ninguna de las cinco se habría encontrado leyendo.
- **And:** tiene su límite, y conviene decirlo: un fallo esperado que se queda años deja de avisar y pasa a ser paisaje. Eso es lo que le pasó al de la versión repetida, que llevaba ocho días exigiendo algo que la casa ya había decidido no cumplir (`S-084`).
- **Where:** `validadores/pruebas.py` y `memoria/pruebas.py`, en las fases `B` cerradas el 2026-08-30.
- **Learned:** cuando `02·F8` impida arreglar lo que una fase encuentra, se deja **la prueba escrita y marcada**, no una nota. Y se revisa: un fallo esperado con más de una sesión encima es una decisión pendiente, no una tarea.
- **When/Who:** 2026-08-30 · agente y usuario, al ejecutar las cinco fases detenidas.
- **Scope:** estándar; aplica a todo defecto que una fase encuentra y no puede tocar.
- **Rel:** S-084 (una prueba que exige lo que se decidió no cumplir no mide nada), S-061 (nadie vuelve a mirar un rojo).

## S-089 · Cuatro reglas invisibles: el capítulo salía en verde porque nadie lo corregía  ·  error-resuelto · activa
- **What:** las cuatro reglas del capítulo de cumplimiento estaban escritas un nivel más abajo que las demás, porque el capítulo agrupa en partes. El analizador solo reconocía los dos niveles de arriba, así que **no existían para el programa**: ninguna de las veinte filas del checklist se les aplicó nunca. Ninguna traía su bloque de checklist y una no tenía su ejemplo.
- **Why:** el capítulo pasaba **por el mismo motivo por el que pasaría un examen que no se corrige**. Y no había forma de notarlo desde el resultado: cero incumplimientos se lee igual que cumplir.
- **Also:** ensanchar el analizador sin más creaba un defecto nuevo. Una sección del anexo de meta-reglas **nombra** a una regla que vive en su propio archivo, y pasó a contarse como una segunda definición: reclamaba un identificador repetido que no existe.
- **And:** lo que separa la regla de su eco es que **el identificador es único**: el que ya se definió arriba no puede ser otra definición. Y hay que mirarlo en una **pasada previa** sobre todo el árbol, porque en el orden de los archivos el eco se lee antes que la regla.
- **Where:** `validadores/metareglas.py`, `reglas()` · `base/16-cumplimiento-y-calidad.md` · la fase `B-EP-004-HU-002-el-analizador-ve-todas-las-reglas`.
- **Learned:** cuando un analizador recorre por forma —el nivel de un título, la posición de una marca—, lo que no encaja **desaparece sin decir nada**. La pregunta que lo caza es «¿cuántas encontró?», no «¿cuántas fallaron?». Y al ensanchar el criterio hay que preguntar de inmediato qué **más** empieza a encajar.
- **When/Who:** 2026-08-30 · agente, con la decisión del usuario de corregir el capítulo en la misma fase.
- **Scope:** estándar; aplica a todo programa que reconozca documentos por su forma.
- **Rel:** S-081 (las cifras las mide un programa), S-083 (un cero que salía de no mirar).
"""

with io.open(R, encoding="utf-8") as f:
    t = f.read()

if "S-086" in t:
    print("ya estaban: no se toca")
else:
    with io.open(R, "w", encoding="utf-8", newline="\n") as f:
        f.write(t.rstrip("\n") + "\n" + NUEVAS)
    print("cuatro senales agregadas: S-086 a S-089")
