# -*- coding: utf-8 -*-
"""Agrega las senales de la fase `A-EP-005-HU-012`: S-093 y S-094."""
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
R = os.path.join(RAIZ, "documentacion", "senales.md")

NUEVAS = u"""
## S-093 · Una regla escrita informa; un programa ejecuta, y el estándar no distinguía las dos  ·  aprendizaje · activa
- **What:** se contaron las 18 reglas vigentes del capítulo `00` y se buscó su identificador dentro de los programas y de los enganches. **Siete no aparecían en ninguno**, y de las once que sí, solo dos tenían una pieza que de verdad las ejecutara. **Catorce de dieciocho** dependían de que el agente se acordara, y ninguna lo decía.
- **Why:** el núcleo es lo que no se relaja, así que es justo donde una regla que solo está escrita se lee igual que una que manda. Quien la abre ve una exigencia; lo que hay detrás puede ser un programa que la rechaza o nada en absoluto, y hasta el 2026-08-31 no había forma de saber cuál de las dos.
- **Also:** «nombrarse en un programa» no es «hacerse cumplir». Once reglas se nombraban en algún archivo, casi siempre en un comentario que explicaba por qué esa comprobación existe. El paso que separa una cosa de la otra no lo da ningún guion: hay que leer la pieza y decidir si ejecuta la exigencia.
- **And:** el usuario cortó la salida fácil. Catorce reglas sin quién las ejecute daban catorce pendientes, y dijo *«no las deje como pendiente de una solución»*. Salió **una sola pieza** para las tres que sí son medibles (`ID8`, `ID9`, `ID10`) y, para las otras once, la declaración escrita de que la sostiene la puerta de aprobación, que ningún programa ve.
- **Where:** `validadores/ejecutable.py` · `base/20-meta-reglas/estructura-regla.md` sección 6 · la fase `A-EP-005-HU-012`.
- **Learned:** cuando una regla se escribe, la pregunta que falta casi siempre es **quién la ejecuta**. Las dos respuestas valen —una pieza, o nadie con su motivo—; la que no vale es callarse, porque entonces la regla que manda y la que solo está escrita se leen igual.
- **When/Who:** 2026-08-31 · el usuario decidió el alcance; el agente construyó.
- **Scope:** estándar; hoy solo el capítulo `00`, y se extiende si el caso aparece fuera.
- **Rel:** S-089 (cuatro reglas invisibles), S-090 (una norma escrita dentro de un documento modelo).

## S-094 · Una línea nueva dentro de una regla la miran cuatro comprobaciones, y ninguna sabía que existía  ·  patrón · activa
- **What:** al escribir en las dieciocho reglas del núcleo la línea que dice quién las hace cumplir, saltaron tres defectos de golpe: ocho reglas empezaron a **reprobar el largo del molde**, catorce **sellos del checklist se dieron por vencidos**, y tres declaraciones traían raya larga, que el trinquete del `pre-commit` habría rechazado. Ninguna regla había cambiado lo que exige.
- **Why:** el archivo de una regla lo leen a la vez el molde (`M5`, el largo del cuerpo), el sello (¿cambió el texto desde que se aplicó el checklist?), el contador de marcas de `00·ID8` y el validador nuevo. Las cuatro tenían su idea de dónde termina la regla, y **ninguna contemplaba una línea que fuera de la regla sin ser su cuerpo**.
- **Also:** los tres se arreglaron con el mismo argumento, que ya estaba escrito para otro caso: el sello responde por lo que la regla **exige**, y cambiar la tipografía no cambia ninguna respuesta del checklist. La declaración tampoco. Que el argumento ya existiera es la señal de que el defecto era de familia conocida.
- **And:** los tres se vieron **antes de commitear**, corriendo las comprobaciones sobre el trabajo a medio hacer. El de las rayas se contó comparando las marcas nuevas contra lo guardado, que es exactamente lo que el enganche iba a hacer al rechazar el commit.
- **Where:** `validadores/metareglas.py`, `_FUERA_DEL_CUERPO` y `_sin_declaracion` · la fase `A-EP-005-HU-012`.
- **Learned:** agregar una línea de molde a un documento que ya tiene comprobaciones cuesta más que escribirla: hay que preguntarse **quién más lee ese archivo**. Y la forma barata de averiguarlo es correr las comprobaciones sobre el cambio a medio hacer, no después del rechazo.
- **When/Who:** 2026-08-31 · agente.
- **Scope:** estándar; aplica a todo campo nuevo dentro de un documento que ya se valida.
- **Rel:** S-091 (la frase que describe lo que hace un programa se deriva), S-084 (una prueba que exige lo que se decidió no cumplir).
"""

with io.open(R, encoding="utf-8") as f:
    t = f.read()

if "S-093" in t:
    print("ya estaban: no se toca")
else:
    with io.open(R, "w", encoding="utf-8", newline="\n") as f:
        f.write(t.rstrip("\n") + "\n" + NUEVAS)
    print("dos senales agregadas: S-093 y S-094")
