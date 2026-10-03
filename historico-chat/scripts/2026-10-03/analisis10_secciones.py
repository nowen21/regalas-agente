# -*- coding: utf-8 -*-
"""Análisis 10 del pendiente 103: las secciones que siguen a «Lo acordado», y sus lecciones como señales."""
import glob
import io
import os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
P = glob.glob(os.path.join(RAIZ, "documentacion", "epicas", "EP-023-*", "pendientes", "103-*"))[0]
A = os.path.join(P, "analisis-10.md")
SENALES = os.path.join(RAIZ, "documentacion", "senales.md")

HU002 = "[HU-002](../../HU-002-cada-documento-sale-del-anterior/HU-002-cada-documento-sale-del-anterior.md)"
HU007 = "[HU-007](../../HU-007-nada-se-escribe-fuera-del-plan-aprobado/HU-007-nada-se-escribe-fuera-del-plan-aprobado.md)"
S = "../../../../senales.md"

SECCIONES = """## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `02·F27` (cada documento cita su origen), `02·F1` (cargar el contexto antes de actuar) y `01·C23` (buscar en el repositorio antes de preguntar), que ya pedían leer el análisis y no bastaron: los recogen los puntos 1 y 2 de «Lo que se tiene que hacer». Aplican `02·F8` (editar solo lo que el plan declara) y `04·S9` (nada se escribe fuera del proyecto), que el freno hace cumplir según el punto 3. Ninguna choca con lo acordado.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| `validadores/origen.py` | Sigue la cadena hasta el criterio de la HU; no mira las decisiones del plan |
| `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md` | Su sección 2.6, «Decisiones técnicas», no pide de qué acuerdo sale cada decisión |
| `validadores/recuperar.py` y `adaptadores/claude-code/hook_reglas.py` | Entregan las reglas con cada mensaje; no entregan acuerdos |
| `validadores/analisis_en_curso.py` | Sabe qué análisis está prendido y de qué pendiente es |
| `adaptadores/claude-code/hook_antes.py` | Frena solo lo que sale del proyecto, y solo en la herramienta de escritura |
| `validadores/ci.py` | Avisa si el proyecto no tiene integración continua; no le agrega pasos |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| H-13 y la R-6 | La recomendación escrita no bastó: nada obliga a recorrer la cadena. Lo recoge el acuerdo 2 |
| Análisis 1, punto 26, y análisis 8, acuerdo 8 | Ya decían que el freno anota el hallazgo, y en este análisis se volvió a preguntar: confirma el H-13. Lo recoge el acuerdo 4 |
| Análisis 8, acuerdo 3 | Fijó las cuatro capas sin decir cuál es la fase activa ni cómo llega Cimiento al servidor. Lo recogen los acuerdos 5 y 6 |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | MAYOR: el plan marca lo que propone el agente y el freno no deja escribir código antes de aprobar el plan. `02·F22` no aplica: nada se deroga |
| Normas y leyes | Ninguna aplica |
| Herramientas | La herramienta resume la conversación cuando crece y se pierde lo leído; el enganche que entrega las reglas con cada mensaje es el que puede entregar los acuerdos |

### Dónde más puede pasar

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Plan escrito sin leer los acuerdos | Cualquier proyecto y agente | Vuelve a preguntar lo decidido o mete lo que nadie pidió | Puntos 1 y 2 |
| Análisis que vuelve a preguntar lo que decidió otro del mismo pendiente | Pendientes con varios análisis | La discusión se repite | Punto 1 |
| Conversación resumida por largo | Herramientas que resumen el contexto | Lo leído se pierde | Punto 1: los acuerdos llegan con cada mensaje |
| Acuerdos que no caben en el mensaje | Pendientes con muchos análisis | El mensaje se llena o se corta | Punto 1: completos los que caben y los demás nombrados |
| Código escrito antes de aprobar el plan | Cualquier fase | Código sin plan | Punto 3 |
| Trabajo sin ninguna fase en curso | Cambios fuera de la cadena | Código sin plan | Punto 3: solo lo que una regla autoriza |
| Proyecto sin integración continua | Proyectos locales | Sin la capa 4 | Punto 4: quedan las capas 1 a 3 |
| Cimiento privado, o una copia de otro usuario | Otros usuarios | El servidor no puede descargarlo | Punto 4: el origen es un dato del proyecto |
| Agente que no es Claude Code | Otras herramientas | Los acuerdos no le llegan por enganche | Punto 2: `origen.py` falla el plan con cualquier agente; el contrato del adaptador dice qué cubre (análisis 8, acuerdo 3) |

---

## Propuesta final: hallazgo y pendiente

> El H-13 no cambia. El pendiente sigue en la V3. EP-023 no suma HU: la HU-002 suma criterios y la HU-007 precisa su CA-02.

### Épica y HU que salen del análisis

EP-023, Lo que se construye es lo que se analizó.

| Orden | HU | Título | Parte del problema que resuelve | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|---|---|
| 1 | {hu002} | Cada documento sale del anterior | Nada obliga a que cada documento salga del anterior | Ninguna | Define la fase en curso y entrega los acuerdos que la HU-007 usa al escribir sus planes | 1, 2 |
| 2 | {hu007} | Nada se escribe fuera del plan aprobado | Nada detiene al agente cuando trabaja fuera del plan aprobado | HU-002, HU-003, HU-004 | Su freno usa la fase en curso de la HU-002 | 3, 4 |

## Lecciones aprendidas

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | Los planes se escribieron con el texto del CA, sin seguir su cadena hasta los acuerdos | Falló | [S-127]({s}#s-127) | complementa R-6 |
| 2 | El agente propuso una tabla que repetía la cadena que ya existía; la pregunta del usuario lo mostró | Falló | [S-128]({s}#s-128) | complementa R-2 |
| 3 | El agente dio por hecho un servidor y un repositorio público; los proyectos son locales y otros pueden usar el agente | Falló | [S-129]({s}#s-129) | complementa R-1 |
| 4 | El ejemplo del acta de una reunión aclaró la propuesta que dos explicaciones técnicas no aclararon | Funcionó | [S-130]({s}#s-130) | complementa R-10 |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Que el agente reciba con cada mensaje los acuerdos de los que sale lo que trabaja: en una fase en curso, los que citan sus CA; con un análisis prendido, los de los análisis aprobados del mismo pendiente; completos los que caben y los demás nombrados con su tema y su número | 3, 4 | EP-023, {hu002} |
| 2 | Que cada decisión del plan cite su acuerdo o vaya marcada como «propuesta del agente», y que `origen.py` falle la que no tenga ninguna de las dos | 3 | EP-023, {hu002} |
| 3 | Precisar el CA-02 de la HU-007: la fase activa es la fase en curso; antes de aprobar su plan solo se escriben los documentos de la fase y lo que una regla autoriza, y sin fase en curso, solo lo autorizado | 6 | EP-023, {hu007}, fase B |
| 4 | Precisar el CA-02 de la HU-007: la capa 4 se activa sola si el proyecto tiene integración continua, y de dónde se descarga Cimiento es un dato del proyecto | 5 | EP-023, {hu007}, fase C |

## Lo que aporta al análisis principal

**Resultado:** Amplía la idea.

**Lo que suma al análisis principal:** El agente recibe los acuerdos de los que sale lo que trabaja, y lo que el plan decide por su cuenta queda marcado como propuesta suya. El freno compara con la fase en curso, y la revisión en el servidor se activa sola donde hay integración continua.
""".format(hu002=HU002, hu007=HU007, s=S)

LECCIONES = """
## S-127 · Los planes se escribieron con el texto del CA, sin seguir su cadena hasta los acuerdos  ·  leccion · activa
- **What:** al escribir los planes de las HU-003 y HU-004 de EP-023, el agente leyó solo el texto de cada criterio y no siguió su «Sale de» hasta los acuerdos del análisis; preguntó lo que ya estaba decidido.
- **Why:** la cadena del criterio al acuerdo existe y `origen.py` la revisa, pero nada obliga a recorrerla, y lo leído se pierde cuando la conversación se resume.
- **Where:** [análisis 10 del pendiente 103](epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-10.md), acuerdos 2 a 4.
- **Learned:** antes de escribir o preguntar, seguir el «Sale de» de cada criterio hasta sus acuerdos. Complementa la R-6.
- **When/Who:** 2026-10-03 · usuario + agente.
- **Scope:** todo plan de cualquier proyecto.
- **Rel:** —

## S-128 · Se propuso una tabla que repetía una cadena que ya existía  ·  leccion · activa
- **What:** para el H-13 el agente propuso que el plan copiara los acuerdos en una tabla; el usuario preguntó si el criterio no sabía ya de dónde salía, y sí lo sabía.
- **Why:** se propuso sin revisar lo que ya existía, y la tabla habría escrito lo mismo en dos sitios.
- **Where:** [análisis 10 del pendiente 103](epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-10.md), acuerdo 2.
- **Learned:** antes de proponer algo nuevo, revisar si ya existe lo que lo resuelve. Complementa la R-2.
- **When/Who:** 2026-10-03 · usuario + agente.
- **Scope:** todo análisis.
- **Rel:** S-127.

## S-129 · Se dio por hecho un servidor y un repositorio público  ·  leccion · activa
- **What:** para la capa 4 del freno el agente preguntó si el repositorio de Cimiento era público, como si cada proyecto tuviera un servidor; el usuario aclaró que los proyectos son locales y que otros pueden usar el agente.
- **Why:** se pensó en un solo caso y no en todos los usuarios posibles.
- **Where:** [análisis 10 del pendiente 103](epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-10.md), acuerdo 5.
- **Learned:** lo que depende del entorno de cada proyecto se activa solo donde ese entorno existe, y lo que cambia de un usuario a otro queda como dato del proyecto. Complementa la R-1.
- **When/Who:** 2026-10-03 · usuario + agente.
- **Scope:** todo lo que viaja a los proyectos.
- **Rel:** —

## S-130 · El ejemplo del acta de una reunión aclaró lo que dos explicaciones técnicas no aclararon  ·  leccion · activa
- **What:** la propuesta de entregar los acuerdos con cada mensaje no se entendió explicada con fases, criterios y enganches; se entendió con el acta de una reunión que nadie vuelve a abrir.
- **Why:** el texto técnico escondía qué cambiaba para el usuario.
- **Where:** [análisis 10 del pendiente 103](epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-10.md), turnos 369 a 372.
- **Learned:** si una explicación no se entiende, cambiarla por un ejemplo de la vida diaria en vez de agregar detalle. Complementa la R-10.
- **When/Who:** 2026-10-03 · usuario + agente.
- **Scope:** todo análisis.
- **Rel:** —
"""


def main():
    t = io.open(A, encoding="utf-8").read()
    i = t.index("## Lo que aportó cada parte")
    io.open(A, "w", encoding="utf-8", newline="\n").write(t[:i] + SECCIONES)
    s = io.open(SENALES, encoding="utf-8").read()
    assert "## S-127 " not in s
    io.open(SENALES, "w", encoding="utf-8", newline="\n").write(s.rstrip("\n") + "\n" + LECCIONES)


if __name__ == "__main__":
    main()
