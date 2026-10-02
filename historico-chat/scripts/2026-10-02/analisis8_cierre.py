# -*- coding: utf-8 -*-
"""Escribe las secciones del análisis 8 después de la conversación (pedido «Hágalo», turno 155)."""
import os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
RUTA = os.path.join(RAIZ, "documentacion", "epicas", "EP-023-lo-que-se-construye-es-lo-que-se-analizo",
                    "103-cada-documento-de-la-cadena-sale-del-anterior", "analisis-8.md")
H7 = "../HU-007-nada-se-escribe-fuera-del-plan-aprobado/HU-007-nada-se-escribe-fuera-del-plan-aprobado.md"
H1 = ("../HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes/"
      "HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes.md")

RESTO = """## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `04·S9` (escribir solo dentro del proyecto), `01·C29` (todo lo del proyecto vive en el repositorio), `20·M12` (no se duplica una regla), `20·M3` (la base sirve a cualquier herramienta), `00·N1` (lo que no se deshace se pide cada vez), `04·S10` y `04·S11` (procesos ajenos y datos reales). No hace falta una regla nueva: `S9` ya rige en todas partes, y lo que falta es que un programa la haga cumplir por todos los canales (turno 142).

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| `adaptadores/claude-code/hook_antes.py` | Freno antes de escribir, enganchado solo a `Write`, `Edit`, `MultiEdit` y `NotebookEdit`; nació en EP-005, HU-023 |
| CA-02 de la [HU-007](H7) | El freno que compara con el plan; dice «escribir un archivo», sin nombrar los demás canales |
| `plantillas/analisis.md` y `validadores/analisis.py` | De la [HU-001](H1): la plantilla no pide considerar otros casos ni las dependencias de las HU; el validador mira cuatro secciones |
| Hoja de ruta de EP-023 | Orden con razón solo en tres puestos; los demás dicen «sigue el orden de la propuesta final» |
| Enganche del análisis | La respuesta entraba un turno tarde; corregido en este análisis (H-9) |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| H-6 y H-9 | Dos veces el programa no cubrió lo que pasa en la realidad: un análisis aprobado que seguía recibiendo turnos y una respuesta que entraba tarde. Lo recoge la conclusión 7 |
| Lecciones de los análisis 6 y 7 | Se decidió sin revisar todo lo que la decisión toca. Lo recogen las conclusiones 4 y 5 |
| El orden de las HU dado por claro en el análisis 3 | Un número no dice en qué orden se construye. Lo recoge la conclusión 5 |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | Usan otras herramientas y otros agentes, algunos sin enganches; el freno tiene que funcionar también al guardar el commit y en la integración continua. Los cambios en la plantilla y el validador del análisis son MAYOR |
| Normas y leyes | Ninguna aplica |
| Herramientas | Claude Code corre a la vez los enganches de un mismo evento y deja la salida del segundo plano en su carpeta temporal |

### Dónde más puede pasar

> El análisis se hace desde todas las perspectivas: lo que pasa en un caso puede pasar en muchos otros. Este análisis es el piloto de la sección.

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Herramienta de escritura | Cualquier agente | Escribe fuera del proyecto o del plan | Capa 1 |
| Redirección, copiar, mover o borrar por consola, git | Cualquier proyecto con consola | Lo mismo, sin que nadie lo vea | Capas 1 y 2 |
| Programa que escribe por dentro | Guiones, pruebas, instaladores | No se ve al leer la orden | Capa 2 dentro del proyecto; afuera queda sin cubrir y lo declara el contrato del adaptador |
| Segundo plano | Herramientas que guardan la salida afuera | La evidencia queda fuera del repositorio | Capa 1 lo detiene |
| Instalar paquetes, cachés, configuración global, variables de entorno, registro | Cualquier sistema | Cambia la máquina, no solo el proyecto | Capa 1, con autorización de la ruta exacta (`S9`) |
| Rutas que engañan: `..`, `~`, variables, enlaces que apuntan afuera, mayúsculas | Windows, Linux, macOS | El freno cree que es adentro | Capa 1 resuelve la ruta real antes de comparar |
| Procesos que siguen después del turno, tareas programadas | Servidores de desarrollo | Actúan sin que nadie mire | Capa 1 los detiene salvo autorización (`S10`) |
| Bases de datos reales, máquinas remotas, despliegues | Proyectos con servicios | Daño que no se deshace | `S11` y `00·N1`: se pide cada vez |
| Subagentes y flujos de varios agentes | Herramientas que los permiten | Escriben sin freno | El mismo freno; si la herramienta no lo pasa, lo declara el contrato |
| Servicios externos y almacenes de la herramienta | Documentos, artefactos, memoria, planes | Lo del proyecto queda fuera de él | `00·N1` y `C29`; la memoria ya la mueve `hook_recuerdos.py` |
| Herramienta sin enganches | Otros agentes | Ninguna capa antes de actuar | Capas 3 y 4 |
| Respuesta que entra tarde al análisis | Cualquier herramienta que corra enganches a la vez | El análisis no tiene lo último | Resuelto: un solo programa escribe las dos cosas |

---

## Conclusiones

| # | Tema | Conclusión | Sale de |
|---|---|---|---|
| 1 | Una regla rige en todas partes | No se crea una regla por cada canal: `04·S9` ya cubre toda escritura fuera del proyecto, y lo que falta es que un programa la haga cumplir por todos | Turno 142 |
| 2 | Dónde queda el freno | En la HU-007, que ya trata del freno; no nace un pendiente aparte | Turnos 143 y 145 |
| 3 | El freno en cuatro capas | Antes de actuar, sobre toda acción y por su efecto; después de actuar, comparando el estado de git con el plan; al guardar el commit; y en la integración continua. Cada adaptador declara qué capas cubre en su herramienta y por qué no las demás | Turnos 144, 153 y 155 |
| 4 | El análisis abre todas las posibilidades | La plantilla del análisis lleva la sección «Dónde más puede pasar», con el caso, dónde se presenta, el riesgo si queda sin cubrir y lo que lo cubre; el validador no deja cerrar un análisis con un caso sin cubrir ni razón | Turnos 146, 152, 153 y 155 |
| 5 | Las HU con su dependencia y su orden | La tabla de HU de la propuesta final lleva de qué HU depende cada una, su orden de ejecución y por qué. El número identifica a la HU y no cambia; el orden sale de las dependencias. El validador revisa que ninguna vaya antes de una de la que depende y que cada puesto tenga razón. La hoja de ruta de la épica copia ese orden | Turnos 152, 153 y 155 |
| 6 | Dónde se pide lo de la plantilla | En una fase D de la HU-001, que es dueña de la plantilla y del validador del análisis | Turno 152 |
| 7 | La respuesta entraba tarde al análisis | `hook_historico.py` la pasa apenas la escribe; ya se corrigió (H-9), porque este análisis es el piloto | Turno 148 |
| 8 | El orden de EP-023 | Primero la fase D de la HU-001, porque todo análisis que venga usa la plantilla. Después la HU-003, que da la forma del hallazgo y del pendiente y resuelve las dos fallas que hoy dejan los validadores. La HU-006 no depende de ninguna y frena las lecciones que se acumulan «por escribir». La HU-004 depende de la HU-003. La HU-007 va al final: depende de la HU-003 y de la HU-004, porque el freno anota el hallazgo y vuelve al análisis | Turnos 153 y 155 |

Siguen abiertas: ninguna.

## Propuesta final: hallazgo y pendiente

> El H-8 no cambia. El pendiente sigue en la V3. EP-023 no suma HU.

### HU que siguen, con su dependencia y su orden

| Orden | HU | Depende de | Por qué en ese orden |
|---|---|---|---|
| 1 | HU-001, fase D | Ninguna | Todo análisis que venga usa la plantilla |
| 2 | HU-003 | HU-001 | Da la forma del hallazgo y del pendiente que usan la HU-004 y la HU-007; resuelve las fallas de `fases` y de `pendientes` |
| 3 | HU-006 | HU-001 | No depende de las demás; cada análisis suma lecciones que hoy no tienen dónde quedar |
| 4 | HU-004 | HU-003 | Detener la ejecución necesita la forma del hallazgo |
| 5 | HU-007 | HU-003, HU-004 | El freno anota el hallazgo y vuelve al análisis |

## Lecciones aprendidas

| # | Lección | Tipo | Señal |
|---|---|---|---|
| 1 | El agente propuso cubrir solo el canal que falló; el usuario pidió considerar todos los casos de todos los proyectos | Falló | Por escribir |
| 2 | Listar todos los canales en una tabla mostró los huecos antes de decidir | Funcionó | Por escribir |
| 3 | Corregir en el piloto lo que falla del propio enganche evita que falle en los análisis siguientes | Funcionó | Por escribir |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de la conclusión | Pasó a |
|---|---|---|---|
| 1 | Reescribir el CA-02 de la HU-007 con el freno en cuatro capas y el contrato de cada adaptador, y repartirlo en las fases que haga falta | 1, 2, 3 | EP-023, [HU-007](H7) |
| 2 | Sumar a la HU-001 el criterio de la sección «Dónde más puede pasar», en la plantilla y en el validador | 4, 6 | EP-023, [HU-001](H1), fase D |
| 3 | Sumar a la HU-001 el criterio de la tabla de HU con dependencia, orden de ejecución y razón, en la plantilla del análisis, la hoja de ruta de la épica y el validador | 5, 6 | EP-023, [HU-001](H1), fase D |
| 4 | Reescribir la hoja de ruta de EP-023 con el orden de este análisis | 8 | EP-023, [épica](../epica.md) |
""".replace("(H7)", "(" + H7 + ")").replace("(H1)", "(" + H1 + ")")


def main():
    with open(RUTA, encoding="utf-8") as f:
        texto = f.read()
    i = texto.index("## Lo que aportó cada parte")
    with open(RUTA, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto[:i] + RESTO)


if __name__ == "__main__":
    main()
