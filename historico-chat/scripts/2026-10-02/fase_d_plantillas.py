# -*- coding: utf-8 -*-
"""Fase D de la HU-001: T-01, T-03, T-07 y T-17 en la plantilla del análisis, T-04 en la de la épica,
y el registro de `recomendaciones-del-analisis.md` (T-06) y el recuerdo que enlaza la R-1 (T-12)."""
import os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))


def cambiar(relativa, pares):
    ruta = os.path.join(RAIZ, relativa)
    with open(ruta, encoding="utf-8") as f:
        t = f.read()
    for viejo, nuevo in pares:
        assert t.count(viejo) == 1, (relativa, viejo[:70])
        t = t.replace(viejo, nuevo)
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)


RECOMENDACIONES = """---

## Recomendaciones

> Antes de analizar se leen las [recomendaciones de Cimiento](«RUTA-ESTANDAR»/plantillas/recomendaciones-del-analisis.md) y las del proyecto, en `analisis/recomendaciones.md` si existe. Aquí se dice cuáles se consultaron y cómo se aplican; la que no aplica se nombra y se dice por qué.

| Recomendación | Cómo se aplica en este análisis |
|---|---|
| «R-n o RP-n» | «qué se hizo por ella, o por qué no aplica» |

---

## Hallazgo"""

DONDE_MAS = """| Herramientas | «qué condiciona lo que se va a construir» |

### Dónde más puede pasar

> Lo que destapó el hallazgo puede pasar en otros sitios, otros proyectos u otras herramientas. Cada caso dice qué lo cubre: un punto de «Lo que se tiene que hacer», un punto de «Lo acordado» o la razón por la que no hace falta cubrirlo. Ningún caso queda sin esa columna.

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| «caso» | «sitio, proyecto o herramienta» | «qué pasa» | «punto, o la razón» |
"""

TABLA_HU = """> El número identifica a la HU; el orden de construcción sale de sus dependencias. Una HU no va antes de otra de la que depende, y cada puesto dice por qué va ahí.

| Orden | HU | Título | Parte del problema que resuelve | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|---|---|
| 1 | «n» | «título que diga su resultado» | «la frase del problema que le toca a esta HU; es lo que va en su contexto» | «HU de las que depende, o "Ninguna"» | «razón» | «números» |
"""

APORTA = """| 1 | «qué hay que hacer» | «número» | «épica y HU, con su título y su enlace» |

## Lo que aporta al análisis principal

> Todo análisis se anota en el análisis principal de su alcance, aunque no cambie el sistema ([`13·DOC25`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC25-reescribe-el-analisis-principal-con-su-lista-de-cambios.md)). Al aprobar, el programa pasa tal cual lo que suma al final de la redacción del principal, y una fila con la fecha, el resultado y el enlace a su «Lista de análisis». Sin esta sección el análisis no se aprueba.

**Resultado:** «ratifica, aclara, amplía, modifica la idea o cambia lo que se construye».

**Lo que suma al análisis principal:** «la frase que se agrega a la redacción del principal, escrita para leerse dentro de ella»
"""


def main():
    cambiar("plantillas/analisis.md", [
        ("---\n\n## Hallazgo", RECOMENDACIONES),
        ("| Herramientas | «qué condiciona lo que se va a construir» |\n", DONDE_MAS),
        ("| HU | Título | Parte del problema que resuelve | Puntos de lo que se tiene que hacer |\n"
         "|---|---|---|---|\n"
         "| «n» | «título que diga su resultado» | «la frase del problema que le toca a esta HU; es lo que va en su contexto» | «números» |\n"
         "\n«orden en que se construyen y por qué»\n", TABLA_HU),
        ("| 1 | «qué hay que hacer» | «número» | «épica y HU, con su título y su enlace» |\n", APORTA),
    ])
    cambiar("plantillas/ciclo-vida-proyectos/03-epica.md", [
        ("> Reparte las HU en fases de entrega, cada una con su fecha y su entregable.\n\n"
         "| Fase | Contenido | HU incluidas | Fecha objetivo | Entregable |\n"
         "|---|---|---|---|---|\n"
         "| Fase 1 — MVP | | HU-001, HU-002 | | |\n"
         "| Fase 2 | | HU-003 | | |\n"
         "| Fase 3 | | | | |\n",
         "> El orden en que se construyen las HU, copiado de la tabla de HU del análisis que las sacó. Una HU no va antes de otra de la que depende, y cada puesto dice por qué va ahí.\n\n"
         "| Orden | HU | Depende de | Por qué en ese orden | Estado |\n"
         "|---|---|---|---|---|\n"
         "| 1 | HU-001 | Ninguna | | |\n"
         "| 2 | HU-002 | HU-001 | | |\n"),
    ])
    cambiar("validadores/plantillas.py", [
        ('    "cierre-analisis": "plantillas/cierre-analisis.md",\n',
         '    "cierre-analisis": "plantillas/cierre-analisis.md",\n'
         '    "recomendaciones-del-analisis": "plantillas/recomendaciones-del-analisis.md",\n'),
    ])
    cambiar("anatomia/mapa-del-sitio.md", [
        ("│   ├── historico-chat.md · cierre-analisis.md\n",
         "│   ├── historico-chat.md · cierre-analisis.md\n"
         "│   ├── recomendaciones-del-analisis.md  lo que todo análisis consulta antes de empezar\n"),
    ])
    cambiar("historico-chat/memory/el-analisis-cubre-todos-los-casos.md", [
        ("- Antes de proponer, listar todas las formas en que puede pasar lo mismo, en cualquier herramienta o proyecto, y decir cuáles cubre cada propuesta.\n",
         "- Es la recomendación R-1 de las [recomendaciones del análisis](../../plantillas/recomendaciones-del-analisis.md), y se aplica como ella dice; aquí queda el registro de que el usuario lo pidió.\n"),
    ])
    cambiar("historico-chat/memory/memory.md", [
        ("y en él se propone todo lo que haga falta discutir.",
         "y en él se propone todo lo que haga falta discutir. Hoy es la R-1 de las recomendaciones del análisis."),
    ])


def doc25():
    """T-16: el texto de `DOC25`, su ejemplo y su checklist contra 44.0.0."""
    cambiar("base/13-documentacion/reglas/DOC25-reescribe-el-analisis-principal-con-su-lista-de-cambios.md", [
        ("El análisis principal del proyecto o del módulo dice siempre lo que se va a construir hoy: cuando un análisis individual cambia algo, se reescribe y suma a su lista de cambios la fecha y el enlace a ese análisis",
         "El análisis principal del proyecto o del módulo se forma con lo que aportan los análisis individuales: cada uno que se aprueba se anota en él, aunque no cambie el sistema, y lo que suma pasa tal cual a su redacción, con la fecha, el resultado y el enlace en su lista de análisis"),
        ("INCORRECTO: el principal dice «la clase con suma», un análisis individual\n"
         "            agregó sus propiedades y el principal quedó congelado\n"
         "CORRECTO:   el principal dice «la clase con suma y sus propiedades» y su\n"
         "            lista de cambios enlaza el análisis que lo cambió\n",
         "INCORRECTO: un análisis solo confirmó que «la clase con suma» estaba bien\n"
         "            entendida, y no se anotó porque no cambió nada\n"
         "CORRECTO:   su frase pasa tal cual al principal, y la lista de análisis\n"
         "            dice la fecha, «Ratifica» y el enlace\n"),
        ("contra **v40.0.0**, el **2026-10-01**.", "contra **v44.0.0**, el **2026-10-02**."),
        ("Fila 9: la exigencia es una sola, que el principal diga lo vigente con la traza de cada cambio;",
         "Fila 9: la exigencia es una sola, que todo análisis aprobado quede anotado en el principal con lo que aportó;"),
        ("Nace en `EP-023·HU-001`, fase `A`, del análisis 1 del pendiente 103 (conclusión 32) y del análisis 5.",
         "Nace en `EP-023·HU-001`, fase `A`, del análisis 1 del pendiente 103 (conclusión 32) y del análisis 5. Cambia en la fase `D`, por el análisis 9 (puntos 1 a 5 de «Lo acordado»)."),
    ])


if __name__ == "__main__":
    # Se corrieron en dos pasos: primero main() y después doc25().
    main()
    doc25()
