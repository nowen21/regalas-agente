# -*- coding: utf-8 -*-
"""Agrega las senales de la tercera tanda de la sesion, S-090 a S-092."""
import io
import os

RAIZ = r"c:\Ing. Jose\ia\agente"
R = os.path.join(RAIZ, "documentacion", "senales.md")

NUEVAS = u"""
## S-090 · Una norma escrita dentro de un documento modelo solo la hereda quien llene ese modelo  ·  aprendizaje · activa
- **What:** la exigencia de escribir en la lengua del proyecto, en tercera persona y con las acciones en infinitivo estaba escrita como **la regla once de dos manuales**. El usuario la pidió para un documento cualquiera y no hubo regla que citar. Subió al cuerpo de reglas como `00·ID10` el 2026-08-30, en la versión `37.0.0`.
- **Why:** un documento modelo se copia para llenarlo, y lo que dice adentro viaja con esa copia y con ninguna otra. Todo lo demás que el agente entrega quedaba sin la norma, y la convención se aplicaba **copiándola a mano** de una plantilla a otra: lo que se copia a mano se copia distinto.
- **Also:** el propio estándar ya lo tenía escrito y nadie lo había leído como una tarea. El anexo de marcas de generación automática decía en su cierre que la norma del idioma «necesita su propia regla, y todavía no existe».
- **And:** el alcance lo decidió el usuario, e incluye **lo que el agente contesta en el chat**. Es lo que más se lee y lo único que no queda versionado, así que es donde la convención se pierde primero: en esta misma sesión hubo que corregirla tres veces.
- **Where:** `base/00-identidad-y-rol/reglas/ID10-escribe-en-el-idioma-del-proyecto-en-tercera-persona-y-en-infinitivo.md` · la fase `A-EP-001-HU-037`.
- **Learned:** cuando una exigencia aparece escrita dentro de un documento modelo, la pregunta es **quién más debería cumplirla**. Si la respuesta es «cualquiera que entregue algo», está en el sitio equivocado y se aplica por copia, que es la forma en que una norma se deforma sin que nadie lo decida.
- **When/Who:** 2026-08-30 · el usuario decidió el alcance; el agente escribió la regla.
- **Scope:** estándar; aplica a toda exigencia que hoy viva dentro de una plantilla.
- **Rel:** S-084 (una prueba que exige lo que se decidió no cumplir), S-089 (cuatro reglas invisibles).

## S-091 · La frase que describe lo que hace un programa se deriva, no se escribe  ·  patrón · activa
- **What:** el validador de marcas decía «0» sin decir sobre qué había corrido, y ese cero se publicó en un commit como si dijera que veinticinco documentos estaban limpios. Al arreglarlo, la frase del alcance **se arma con lo que la corrida recorrió**: las carpetas salen de la misma constante que el recorrido usa, y el número de archivos lo cuenta la propia pasada.
- **Why:** una frase escrita aparte **envejece sin avisar**. El día que alguien amplíe el alcance y no la toque, el reporte empieza a mentir y nada se cae. Derivada, la prueba se cae en vez de dejar que mienta.
- **Also:** el número importa tanto como el nombre de la carpeta. «Se recorrió `base/`» es cierto también cuando no había un solo archivo, y ese es justamente el otro cero que se confundía.
- **And:** el mismo patrón resolvió un defecto distinto el mismo día. El patrón del permiso de anular se armaba reemplazando `<recurso>` sobre el texto ya escapado, con el resultado del escapado **escrito a mano**; cuando la biblioteca cambió, el reemplazo dejó de encajar y el reclamo salió en todos los proyectos (`S-086`). La cura fue la misma: buscar lo mismo que se transformó, sin suponer cómo quedó.
- **Where:** `validadores/marcas.py`, `alcance()` · `validadores/entidades.py`, `recursos_con_permiso` · `validadores/tests/test_el_validador_dice_sobre_que_corrio.py`.
- **Learned:** todo texto que describa lo que un programa hace —su alcance, su cobertura, su patrón— se **deriva de lo que el programa usa**. Escribirlo aparte crea dos verdades que empiezan iguales y se separan sin que nadie lo note.
- **When/Who:** 2026-08-30 · agente.
- **Scope:** estándar; aplica a toda salida que describa el propio recorrido de un programa.
- **Rel:** S-083 (un cero que salía de no mirar), S-086 (un reclamo que sale siempre).

## S-092 · Trece rojos, cinco fases detenidas y siete pruebas: casi nada era trabajo  ·  aprendizaje · activa
- **What:** la jornada empezó con 13 historias en rojo, 5 terminadas sin decir si cumplían, 5 fases detenidas y 7 pruebas del estándar en rojo. Al medirlas una por una: **cinco rojos ya no eran ciertos**, cinco eran decisiones del usuario, tres eran trabajo; las cinco mudas **sí decían su veredicto** y el programa no sabía leerlo; las cinco fases estaban escritas y esperando una firma; y de las siete pruebas, una era un defecto de la propia prueba y cinco eran de archivos de otra sesión.
- **Why:** treinta ítems se leen como treinta tareas, y **menos de un tercio lo era**. Tratarlos como deuda técnica lleva a estimar mal y, peor, a no preguntar lo que hay que preguntar: cinco de esos ítems llevaban entre ocho y trece días esperando una respuesta de dos frases.
- **Also:** lo que separa una cosa de la otra es siempre lo mismo: **ejecutar el criterio**, no leer el documento que lo describe. Los cinco rojos que ya no eran ciertos se vieron corriéndolos; los tres que sí eran trabajo, también.
- **And:** la cuenta terminó en 122 historias que cumplen, cero rojas y cero mudas. Lo que queda son cuatro historias de producto sin ninguna fase, que es la única deuda que de verdad era trabajo.
- **Where:** `historico-chat/scripts/2026-08-30/` · el resumen de la sesión `2026-08-28 · plantilla-manual-instalacion`.
- **Learned:** antes de estimar una lista de pendientes, medirla. Las preguntas que la parten son tres: **¿esto se cierra construyendo, decidiendo, o solo declarándolo?** Y una cuarta que aparece cuando hay varias sesiones a la vez: **¿es mío?**
- **When/Who:** 2026-08-30 · usuario y agente, en una sola jornada.
- **Scope:** estándar; aplica a toda revisión de una cuenta de pendientes.
- **Rel:** S-085 («ocho historias en rojo» eran dos cosas distintas), S-088 (el fallo esperado es la única nota que reclama sola).
"""

with io.open(R, encoding="utf-8") as f:
    t = f.read()

if "S-090" in t:
    print("ya estaban: no se toca")
else:
    with io.open(R, "w", encoding="utf-8", newline="\n") as f:
        f.write(t.rstrip("\n") + "\n" + NUEVAS)
    print("tres senales agregadas: S-090 a S-092")
