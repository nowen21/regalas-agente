# -*- coding: utf-8 -*-
"""Escribe las secciones del análisis 9 después de la conversación (turno 200, «Hágalo»)."""
import os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
RUTA = os.path.join(RAIZ, "documentacion", "epicas", "EP-023-lo-que-se-construye-es-lo-que-se-analizo",
                    "103-cada-documento-de-la-cadena-sale-del-anterior", "analisis-9.md")
H1 = ("../HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes/"
      "HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes.md")

RESTO = """## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplica `13·DOC25`, que hoy pide anotar en el análisis principal solo «cuando un análisis individual cambia algo»; choca con la conclusión 1 y se resuelve en el punto 1. Aplican también `13·DOC24` (el análisis aprobado no se reescribe) y `20·M10` (cambiar una regla se versiona).

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| `analisis/proyecto-2026-10-02-analisis-principal.md` | Su «Lista de cambios» tiene los análisis 1, 2, 4 y 5; faltan el 3, el 6, el 7 y el 8. No guarda lo que se ratificó o se aclaró |
| `analisis/base-2026-08-07-cumplimiento-meta-reglas.md` | Análisis con la forma anterior, que aclaró el cumplimiento de las meta-reglas; no está anotado |
| Plantilla del análisis | No tiene dónde decir qué le aporta al análisis principal |
| Fase `D` de la HU-001 | Planes escritos, sin aprobar; su CA-20 nombra solo los análisis 6, 7 y 8 |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| Fase `C` de la HU-001 | Dejó fuera el análisis 3 porque no cambió lo que se construye; este análisis corrige ese criterio |
| Análisis 8, conclusión 11 | Ya pedía poner el análisis principal al día; este análisis amplía qué se anota |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | Cambia `13·DOC25`: va en la versión MAYOR de la fase `D` |
| Normas y leyes | Ninguna aplica |
| Herramientas | El enganche que pone la marca de aprobado es el que copia la sección al análisis principal |

### Dónde más puede pasar

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Análisis que solo ratifica o aclara | Cualquier proyecto | Se pierde lo aclarado y el tema se vuelve a discutir | Conclusiones 1 y 2 |
| Proyecto con un análisis principal por módulo | Proyectos grandes | La línea va al principal equivocado | Conclusión 5 |
| Análisis con la forma anterior | Proyectos que ya tenían análisis | Queda fuera de la lista | Conclusión 4 |
| Texto cambiado al pasar al principal | Cualquier agente | El principal dice algo que nadie aprobó | Conclusión 3 |

---

## Conclusiones

| # | Tema | Conclusión | Sale de |
|---|---|---|---|
| 1 | Todo análisis se anota | Cada análisis que se aprueba se anota en el análisis principal, aunque no cambie el sistema, porque en él se trataron temas que aclararon cosas | Turnos 193 y 194 |
| 2 | Lo que hace un análisis | El análisis no sirve solo para decidir qué se construye: también confirma, aclara, amplía o modifica la idea que se había planteado. Ratificar que una idea estaba bien entendida es un resultado | Turno 194 |
| 3 | Lo que aporta al análisis principal | El análisis lleva, antes de aprobarse, la sección «Lo que aporta al análisis principal», con su resultado (ratifica, aclara, amplía, modifica la idea o cambia lo que se construye), qué en una frase y qué cambia en «Lo que está definido» o en «Qué se construye hoy». El usuario la aprueba con el análisis. Al aprobarlo, un programa la copia tal cual al análisis principal, y el validador falla si las dos copias no son idénticas | Turnos 196 a 199 |
| 4 | Los análisis que faltan | Se anotan los análisis 3, 6, 7 y 8, y el análisis con la forma anterior de `analisis/`; el aviso revisa todos los análisis aprobados, sin puerta de versión | Turno 194 |
| 5 | En qué principal | Cada análisis se anota en el análisis principal de su alcance, del módulo o del proyecto; si no se sabe, en el del proyecto | Turno 194 |
| 6 | Dónde se pide | En la fase `D` de la HU-001, que pasa su plan a la versión siguiente | Turno 194 |

Siguen abiertas:

1. Si un análisis que solo ratifica o aclara puede cerrar sin «Lo que se tiene que hacer», y el validador no lo detiene por eso.
2. Si la «Lista de cambios» del análisis principal pasa a llamarse «Lista de análisis», con las columnas fecha, resultado, qué y análisis.

## Propuesta final: hallazgo y pendiente

> El H-11 no cambia. El pendiente sigue en la V3. EP-023 no suma HU.

## Lecciones aprendidas

| # | Lección | Tipo | Señal |
|---|---|---|---|
| 1 | El estándar trataba el análisis solo como la puerta de lo que se construye, y dejaba sin registro lo que se ratifica o se aclara | Falló | Por escribir |
| 2 | Escribir lo que va al análisis principal dentro del análisis permite que el usuario lo apruebe una sola vez y que un programa lo pase sin cambios | Funcionó | Por escribir |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de la conclusión | Pasó a |
|---|---|---|---|
| 1 | Cambiar `13·DOC25`: cada análisis aprobado se anota en el análisis principal de su alcance con lo que aportó, copiado tal cual | 1, 2, 3, 5 | EP-023, [HU-001](H1), fase D |
| 2 | Sumar a la plantilla del análisis la sección «Lo que aporta al análisis principal»; que el enganche de aprobar la copie tal cual y que el validador compare las dos copias | 3 | EP-023, [HU-001](H1), fase D |
| 3 | Pasar el CA-20 de la HU-001 a su versión siguiente: el análisis principal con «Lo que está definido» y las líneas de los análisis 3, 6, 7 y 8 y del análisis con la forma anterior; el aviso revisa todos los aprobados | 2, 4 | EP-023, [HU-001](H1), fase D |
| 4 | Pasar el plan de la fase `D` a su versión siguiente | 6 | EP-023, HU-001, fase D |
""".replace("(H1)", "(" + H1 + ")")


def main():
    with open(RUTA, encoding="utf-8") as f:
        texto = f.read()
    i = texto.index("## Lo que aportó cada parte")
    with open(RUTA, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto[:i] + RESTO)


if __name__ == "__main__":
    main()
