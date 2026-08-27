# -*- coding: utf-8 -*-
"""El alcance de la HU-012 crece: se traduce. Aprobado por el usuario."""
import io
import os

os.chdir(r"c:\Ing. Jose\ia\agente")

HU = ("documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/"
      "HU-012-una-sola-palabra-para-cada-estado/"
      "HU-012-una-sola-palabra-para-cada-estado.md")
PLAN = ("documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/"
        "HU-012-una-sola-palabra-para-cada-estado/"
        "A-EP-003-HU-012-una-sola-palabra-por-estado/plan_trabajo.md")

VOCAB = """
### 3.4 El vocabulario, acordado el 2026-08-26

**Mismo concepto, misma palabra.** Que los conjuntos difieran es correcto; que «terminado» se diga de tres formas, no.

| Concepto | Palabra | La usan |
|---|---|---|
| Todavía no empezó | **Pendiente** | épica · historia · tarea |
| Propuesta, sin aprobar | **Propuesta** | épica |
| Aprobada, sin empezar | **Aprobada** | épica |
| Escrita y lista para construir | **Lista** | historia |
| Se está construyendo | **En curso** | épica · historia · tarea |
| Construida, probándose | **En prueba** | historia |
| Terminada | **Terminada** | épica · historia · tarea |
| Detenida por algo de afuera | **Bloqueada** | tarea |
| Se decidió no hacerla | **Cancelada** | épica |

Los tres conjuntos quedan:

- **Épica:** Propuesta · Aprobada · En curso · Terminada · Cancelada
- **Historia:** Pendiente · Lista · En curso · En prueba · Terminada
- **Tarea:** Pendiente · En curso · Terminada · Bloqueada

**«Terminada» y no «Cerrada»**, aunque seis historias usen `Cerrada` hoy: `cerrada` ya significa otra cosa en el estándar — es como se marca una **estación** de fase. Reusarla mezclaría dos vocabularios.
"""

CAMBIOS = [
 # -- La HU: el alcance ya no excluye traducir --
 (HU,
  "- **Traducir el vocabulario al español.** `Backlog`, `Ready` y `Done` están "
  "en inglés y eso choca con `01·C8`. Es una decisión aparte, y mezclarla acá "
  "volvería este cambio mucho más grande.",
  "- **Los estados de otros documentos del proyecto** que no sean épica, "
  "historia o tarea. Si también divergen, sale de un barrido aparte."),

 (HU,
  "| RN-07 | Épica, historia y fase pueden tener **conjuntos** distintos, pero "
  "la palabra de un concepto compartido es una sola | Una épica se cancela y "
  "una historia no; «terminado» es lo mismo en las tres |",
  "| RN-07 | Épica, historia y fase pueden tener **conjuntos** distintos, pero "
  "la palabra de un concepto compartido es una sola | Una épica se cancela y "
  "una historia no; «terminado» es lo mismo en las tres |\n"
  "| RN-08 | El vocabulario se escribe **en español** | `01·C20` lo exige, y "
  "el glosario es justamente el documento que lleva la lista de lo que se "
  "queda en otro idioma y por qué. Escribir ahí `Backlog` sin razón sería "
  "incumplir en el archivo donde más se nota |"),

 (HU,
  "- El vocabulario de [`04-HU.md`](../../../../plantillas/ciclo-vida-proyectos/"
  "04-HU.md) —`Backlog / Ready / En curso / En QA / Done`— sirve de base. No "
  "hay que inventar uno.",
  "- El vocabulario de [`04-HU.md`](../../../../plantillas/ciclo-vida-proyectos/"
  "04-HU.md) sirve de base **en su forma**, no en sus palabras: tres de las "
  "cinco están en inglés y hay que traducirlas (`RN-08`)."),

 # -- La HU: el conteo real --
 (HU,
  "| RN-05 | Los 51 documentos existentes se normalizan, incluidos los de "
  "fases cerradas | Decisión del usuario. El campo es un índice, no el "
  "registro de lo que pasó |",
  "| RN-05 | Los documentos existentes se normalizan, incluidos los de fases "
  "cerradas | Decisión del usuario. El campo es un índice, no el registro de "
  "lo que pasó. **Al traducir son 111 de 115, no 51**: `Backlog` solo son 54 |"),

 # -- La HU: el vocabulario, escrito --
 (HU,
  "---\n\n## 4. Criterios de aceptación",
  VOCAB + "\n---\n\n## 4. Criterios de aceptación"),

 # -- El plan: fuera de alcance --
 (PLAN,
  "- **Traducir el vocabulario al español**, que choca con `01·C8` y es "
  "decisión aparte.",
  "- **Los estados de documentos que no sean épica, historia o tarea.**"),

 # -- El plan: la tarea de normalizar, con el numero real --
 (PLAN,
  "| T-05 | Normalizar las 51, **conservando el texto que sigue a la palabra** "
  "| Documentación | 2 h | T-04, T-02 | EV-02 |",
  "| T-05 | Normalizar las **111 de 115**, conservando el texto que sigue a la "
  "palabra | Documentación | 3 h | T-04, T-02 | EV-02 |"),

 (PLAN,
  "| T-01 | Escribir en el glosario los tres conjuntos, con qué significa cada "
  "estado | Documentación | 2 h | — | EV-01 |",
  "| T-01 | Escribir en el glosario los tres conjuntos **en español**, con qué "
  "significa cada estado | Documentación | 2 h | — | EV-01 |"),
]

for ruta, viejo, nuevo in CAMBIOS:
    t = io.open(ruta, encoding="utf-8").read()
    assert t.count(viejo) == 1, "no coincide en %s -> %s" % (ruta[-24:], viejo[:46])
    io.open(ruta, "w", encoding="utf-8", newline="\n").write(
        t.replace(viejo, nuevo, 1))

print("HU-012 y su plan, con el alcance real: %d cambios" % len(CAMBIOS))
