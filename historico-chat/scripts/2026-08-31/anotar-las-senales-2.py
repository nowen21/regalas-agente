# -*- coding: utf-8 -*-
"""Agrega las senales de las dos fases de arreglo: S-095 y S-096."""
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
R = os.path.join(RAIZ, "documentacion", "senales.md")

NUEVAS = u"""
## S-095 · La comprobación de la frontera miraba un canal, y había dos  ·  patrón · activa
- **What:** al mover `hook_estacion.py` de `validadores/` al adaptador, la prueba que vigila la frontera dio rojo. Comparaba los enganches que hay contra los que el instalador conecta, y para eso leía **una sola tabla**: la de la herramienta. Ese enganche va por el otro canal, el `post-commit` de git, así que recién mudado parecía un archivo que nadie usa.
- **Why:** la pieza estaba mal puesta desde el día que nació y la prueba lo decía; lo que impedía arreglarlo era que **arreglarlo rompía otra prueba**. El defecto no era el archivo: era que la cuenta de lo conectado estaba incompleta, y nadie lo iba a ver hasta que alguien intentara la mudanza.
- **Also:** la lista ahora se **deriva de las mismas plantillas que el instalador escribe**, no de una escrita al lado. Es el patrón de `S-091` otra vez: dos verdades que empiezan iguales se separan sin que nadie lo note.
- **And:** al escribir los mensajes nuevos apareció un efecto lateral medible. Decir «lo corre el enganche `hook_rutas.py`» hizo que el contador del amarre leyera **dos programas agnósticos como amarrados a la herramienta**: busca la palabra dentro del texto y no distingue nombrar de ser. El recuento subió de 27 a 29, y por eso se vio. Se resolvió nombrando al corredor sin su archivo.
- **Where:** `validadores/instalar.py`, `enganches_enchufados()` · `validadores/tests/test_la_frontera_del_adaptador.py` · la fase `C-EP-005-HU-011`.
- **Learned:** cuando una prueba lleva meses en rojo y el arreglo obvio rompe otra, el defecto casi nunca está donde apunta la falla. Está en el criterio que la otra prueba da por supuesto.
- **When/Who:** 2026-08-31 · agente.
- **Scope:** estándar; aplica a toda comprobación que compare «lo que hay» contra «lo que se conecta».
- **Rel:** S-091 (la frase que describe lo que hace un programa se deriva), S-094 (una línea nueva la miran cuatro comprobaciones).

## S-096 · Dos reglas puestas se rompieron igual: lo nuevo no pasó por donde la regla vigila  ·  aprendizaje · activa
- **What:** dos criterios de la misma historia estaban cumplidos y dejaron de estarlo. Ningún programa termina en silencio: dos nacidos después no lo cumplían. La corrida termina con un resumen único: un bloque agregado después quedó **debajo** de ese resumen. Las dos pruebas lo decían desde entonces.
- **Why:** una regla escrita se cumple el día que se escribe y se rompe el día siguiente, cuando alguien agrega algo por un camino donde la regla no vigila. La prueba existía, pasaba a rojo, y **nadie la corría**: es la misma raíz que hizo falta cerrar en `EP-005·HU-021`, cuando 650 pruebas escritas no las ejecutaba ningún comando.
- **Also:** el arreglo obligó a **ampliar la comprobación que reportaba el defecto**, y ahí está el riesgo: es la forma más fácil de hacer desaparecer un rojo sin arreglar nada. Se cubrió con sabotaje — un módulo de mentiras que no imprime nada y sale con 0, escrito y borrado por la propia prueba, para comprobar que el silencio se sigue cazando.
- **And:** lo que se amplió no fue cuánto silencio se acepta, sino **qué cuenta como decir por dónde se corre**. Dos programas no cuelgan del validador: los llama un enganche, y exigirles que nombraran `validar.py` era obligarlos a mandar al lector a un subcomando que no existe.
- **Where:** `validadores/comun.py`, `no_es_punto_de_entrada` · `validadores/validar.py`, `cmd_todo` · la fase `D-EP-004-HU-008`.
- **Learned:** al ampliar una comprobación para que deje de reportar algo, **sabotearla en la misma vuelta**. Si el caso original sigue cazándose, la ampliación era correcta; si no, lo que se hizo fue apagar el reporte.
- **When/Who:** 2026-08-31 · agente.
- **Scope:** estándar; aplica a todo cambio sobre una prueba que está reportando en rojo.
- **Rel:** S-093 (una regla escrita informa; un programa ejecuta), S-075 (tres registros con comprobador y rotos días igual).
"""

with io.open(R, encoding="utf-8") as f:
    t = f.read()

if "S-095" in t:
    print("ya estaban: no se toca")
else:
    with io.open(R, "w", encoding="utf-8", newline="\n") as f:
        f.write(t.rstrip("\n") + "\n" + NUEVAS)
    print("dos senales agregadas: S-095 y S-096")
