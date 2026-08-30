# -*- coding: utf-8 -*-
"""Agrega al final de `documentacion/senales.md` las senales de esta sesion.

Se escribe como guion y no a mano porque el archivo tiene 800 lineas y el
molde de la senal tiene diez campos: pegarlo a mano es donde se pierde uno.
"""
import io
import os

RAIZ = r"c:\Ing. Jose\ia\agente"
R = os.path.join(RAIZ, "documentacion", "senales.md")

NUEVAS = u"""
## S-082 · El aviso disparó las tres veces y no cambió nada  ·  error-resuelto · activa
- **What:** el agente escribió tres guiones de apoyo en la carpeta temporal de la herramienta, fuera del repositorio, y los documentos de fase que esos guiones produjeron quedaron sin su evidencia. **El enganche que avisa de eso existe, está colgado y disparó las tres veces**: se comprobó corriéndolo, `hook_rutas.py` imprime el aviso y nombra el destino correcto.
- **Why:** la regla es `04·S18` y salió del [pendiente 89](../pendientes/hecho/los-guiones-de-apoyo-quedan-en-el-repositorio.md), que se cerró seis días antes por exactamente esto. **No faltaba el control: el control habló y no cambió nada.** El enganche sale con código 0, así que avisa y sigue.
- **Also:** lo notó el usuario, no el agente ni el enganche. La causa no fue una duda sobre dónde va el guion: fue tomar el camino que no fallaba, porque el heredoc de la terminal se rompía con las comillas.
- **And:** el contraste está dentro de la misma sesión. El enganche del commit **sí detiene**, con código 2, y rechazó un commit por dos puntos suspensivos de un solo carácter. Ese se notó en el acto y se corrigió en el acto.
- **Where:** `adaptadores/claude-code/hook_rutas.py` · `historico-chat/scripts/2026-08-30/` · el `H-7` del resumen de la sesión.
- **Learned:** un aviso con código 0 sobre una regla **que ya se dejó de cumplir dos veces** no es un control, es una nota al pie. Lo que distingue a los dos enganches de esta sesión no es qué comprueban: es si detienen. Antes de dar por cubierta una regla con un aviso, vale preguntar cuántas veces se ha incumplido con el aviso puesto.
- **When/Who:** 2026-08-30 · el usuario lo vio y preguntó por qué el agente escribía afuera.
- **Scope:** estándar; aplica a toda regla que hoy se sostiene solo con un aviso.
- **Rel:** S-057 (los guiones de apoyo se borraban con el temporal), S-070 (un checklist que uno firma sobre su propio trabajo no comprueba nada).

## S-083 · Un cero que salía de no mirar se publicó como «limpio»  ·  error-resuelto · activa
- **What:** el agente corrió `validar.py marcas` sobre veinticinco documentos nuevos, obtuvo cero, y escribió en el cuerpo de un commit que el validador no reportaba ninguna línea de esos archivos. El enganche del commit, que lee lo que entra al índice, encontró **trece avisos en esos mismos archivos**.
- **Why:** el subcomando solo recorre `base/` y `plantillas/`. Sobre `documentacion/` devuelve cero **porque no mira**, no porque esté limpio, y la salida no distingue una cosa de la otra.
- **Also:** el mismo programa tiene el otro filo, más viejo: cuenta las secciones 2 y 3 del anexo de marcadores y las de la 4 en adelante piden lectura. Su «0 en 0 archivos» tampoco lo dice.
- **And:** la afirmación falsa quedó publicada y hubo que corregirla en el commit siguiente. El commit no se enmendó porque el enganche `post-commit` ya había escrito su hash dentro de los documentos de fase.
- **Where:** [pendiente 91](../pendientes/91-el-validador-de-marcas-no-dice-que-no-comprueba.md) · `validadores/marcas.py` · commits `b7b8fc0` y `870ef69`.
- **Learned:** antes de citar un cero como evidencia, hay que saber **sobre qué corrió el programa**. Un validador que no dice qué recorrió no entrega un veredicto: entrega un número que el lector completa con lo que quiere creer.
- **When/Who:** 2026-08-30 · agente, al cerrar cinco veredictos en rojo.
- **Scope:** estándar; aplica a toda salida de validador que se cite en un documento o en un commit.
- **Rel:** S-081 (las cifras de cada documento las mide un programa), S-061 (nadie vuelve a mirar un veredicto en rojo).

## S-084 · Una prueba que exige lo que la casa decidió no cumplir no mide nada  ·  decisión · activa
- **What:** la versión `15.4.0` aparece dos veces en el registro porque dos sesiones numeraron a la vez. El registro decidió el 2026-08-15 **no renumerar**, con el motivo escrito: un proyecto pudo haber adoptado ese número. La prueba del criterio seguía exigiendo unicidad, y llevaba ocho días marcada como fallo esperado.
- **Why:** el veredicto de la historia quedaba en rojo por una exigencia que nadie pensaba cumplir. **Un fallo esperado permanente enseña a mirar los fallos esperados como paisaje**, y entonces el que aparezca de verdad tampoco se mira.
- **Also:** la salida no fue aflojar la prueba. Pasó a exigir lo que sí se sostiene, que la repetición esté declarada con sus dos entradas a la vista, y se le agregó la contraprueba: un número repetido **sin** declarar sí falla. Sin esa segunda mitad, aceptar el declarado era aceptar cualquiera.
- **And:** el `CHANGELOG.md` no se tocó. Lo que estaba mal no era el dato: era la exigencia.
- **Where:** `validadores/pruebas.py`, clase `NumeroDeVersion` · la fase `B-EP-002-HU-001-el-numero-repetido-se-declara`.
- **Learned:** cuando una prueba lleva días en fallo esperado, la primera pregunta no es cómo arreglarla sino **si lo que exige sigue siendo lo que la casa quiere**. A veces el rojo no señala trabajo pendiente: señala una decisión que se tomó y que nadie bajó a la prueba.
- **When/Who:** 2026-08-30 · usuario decide la lectura del criterio, agente la implementa.
- **Scope:** estándar; aplica a toda prueba marcada como fallo esperado por más de una sesión.
- **Rel:** S-065 (un rojo entraba en la cuenta y no salía nunca), S-061 (nadie vuelve a mirar un veredicto en rojo).

## S-085 · «Ocho historias en rojo» eran dos cosas distintas  ·  aprendizaje · activa
- **What:** ocho historias terminadas arrastraban un «No cumple» y ninguna tenía fase posterior. Medidas una por una, tres eran trabajo y se hicieron; **las otras cinco no son trabajo: son decisiones del usuario**, y cuatro de ellas ya estaban escritas como tales dentro del propio repositorio.
- **Why:** «ocho en rojo» se lee como ocho tareas, y confundirlas lleva a lo peor de los dos lados: o el agente decide por su cuenta lo que no le toca (`01·C4`), o el trabajo que sí está hecho se queda sin declarar.
- **Also:** el repositorio lo tenía dicho y nadie lo estaba leyendo. La prueba de `EP-006·HU-006` lo escribe textual: *«las dos salidas son malas y elegir entre ellas no es del que ejecuta... queda como fallo esperado y como pregunta al usuario, no como parche»*.
- **And:** la partición sale de **ejecutar el criterio**, no de leer el documento de la fase. Dos de los tres que resultaron ser trabajo estaban en rojo por razones honestas que ya no eran ciertas o que nunca se habían podido provocar.
- **Where:** `historico-chat/scripts/2026-08-30/` · las fases `B` de `EP-001·HU-006`, `EP-002·HU-001` y `EP-007·HU-002`.
- **Learned:** antes de estimar una lista de rojos, medirla. La pregunta que la parte en dos es **«¿esto se cierra construyendo, o se cierra decidiendo?»**, y la respuesta cambia quién tiene que hacer el siguiente movimiento.
- **When/Who:** 2026-08-30 · el usuario pidió terminar las ocho.
- **Scope:** estándar; aplica a cualquier lote de veredictos en rojo.
- **Rel:** S-081 (el molde se aprueba una vez y las cifras se miden), S-061 (nadie vuelve a mirar un rojo).
"""

with io.open(R, encoding="utf-8") as f:
    t = f.read()

if "S-082" in t:
    print("ya estaban: no se toca")
else:
    with io.open(R, "w", encoding="utf-8", newline="\n") as f:
        f.write(t.rstrip("\n") + "\n" + NUEVAS)
    print("cuatro senales agregadas: S-082 a S-085")
