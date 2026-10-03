# -*- coding: utf-8 -*-
"""Análisis 12 del pendiente 103: lo acordado y las secciones que siguen."""
import glob
import io
import os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
P = glob.glob(os.path.join(RAIZ, "documentacion", "epicas", "EP-023-*", "pendientes", "103-*"))[0]
A = os.path.join(P, "analisis-12.md")
HU004 = "[HU-004](../../HU-004-un-hallazgo-detiene-la-ejecucion-y-vuelve-al-analisis/HU-004-un-hallazgo-detiene-la-ejecucion-y-vuelve-al-analisis.md)"
P109 = ("[pendiente 109](../../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-023-cada-tarea-sabe-que-reglas-le-aplican/"
        "pendientes/109-las-pruebas-del-freno-describen-el-freno-viejo/pendiente.md)")

ACORDADO = """1. Qué hallazgo detiene: solo el que afecta al plan en curso, es decir, el que obliga a tocar algo que el plan no declara para cerrar la fase. El que no lo afecta se anota con su pendiente donde pertenece y el trabajo sigue, sin análisis. Precisa el acuerdo 18 del análisis 1 (turnos 443 y 444).
2. El H-15 no afecta al plan en curso: las pruebas que fallan son de la EP-005 y la fase `B` de la HU-007 cierra sin tocarlas. Su pendiente, el 109, vive en la HU-023 de EP-005, donde nacieron el freno viejo y sus pruebas, y la fase sigue (turnos 440 a 444).

Siguen abiertas: ninguna."""

SECCIONES = """## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `02·F8` y `02·F9` (lo que el plan no previó detiene la ejecución) y `13·DOC24` (el análisis siguiente decide si el hallazgo es parte del plan en curso). El acuerdo 1 precisa cuándo detener: antes de esa decisión ya se distingue si el hallazgo afecta al plan. Lo recoge el punto 1 de «Lo que se tiene que hacer».

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| `validadores/tests/test_las_reglas_llegan_antes_de_actuar.py` | Tres pruebas de la EP-005 esperan el freno viejo y fallan |
| `02·F9` | Dice que lo no previó detiene la ejecución, sin distinguir si afecta al plan en curso |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| Análisis 1, acuerdo 18 | Detener ante un hallazgo; se aplicaba a todos. Lo precisa el acuerdo 1 |
| Análisis 11, lección S-274 | Al planear no se buscaron las pruebas que leen lo que cambia; volvió a pasar en el H-15 |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | Cambia `02·F9`: va con la fase que lo construya, en versión MENOR, porque detiene menos |
| Normas y leyes | Ninguna aplica |
| Herramientas | Ninguna condiciona lo acordado |

### Dónde más puede pasar

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Prueba de otra épica que falla por un cambio aprobado | Cualquier proyecto | Se detiene una fase que podía cerrar | Punto 1 |
| Hallazgo que sí obliga a tocar algo fuera del plan | Cualquier fase | Se escribe fuera del plan | Punto 1: ese sí detiene |
| Pendiente que nace en el sitio equivocado | Cualquier hallazgo | Nadie lo encuentra con su dueño | Acuerdo 2: nace donde pertenece |

---

## Propuesta final: hallazgo y pendiente

> El H-15 no cambia. El pendiente 103 no pasa de versión: el H-15 no es de él, y su pendiente es el {p109}. EP-023 no suma HU.

### Épica y HU que salen del análisis

EP-023, Lo que se construye es lo que se analizó.

| Orden | HU | Título | Parte del problema que resuelve | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|---|---|
| 1 | {hu004} | Un hallazgo detiene la ejecución y vuelve al análisis | Nada distingue el hallazgo que afecta al plan en curso del que no | HU-003 | Es la dueña de `02·F9` | 1 |

## Lecciones aprendidas

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | Se detuvo una fase por un hallazgo que no la afectaba | Falló | S-278 | complementa R-15 |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Que `02·F9` diga que solo detiene el hallazgo que obliga a tocar algo que el plan no declara, y que el que no afecta se anota con su pendiente donde pertenece y el trabajo sigue | 1 | EP-023, {hu004} |
| 2 | Crear el {p109} en la HU-023 de EP-005 y seguir la fase `B` de la HU-007 | 2 | Este análisis, de una y sin fase: `documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-023-cada-tarea-sabe-que-reglas-le-aplican/pendientes/109-las-pruebas-del-freno-describen-el-freno-viejo/pendiente.md`, hecho el 2026-10-03 |

## Lo que aporta al análisis principal

**Resultado:** Aclara.

**Lo que suma al análisis principal:** Solo detiene la ejecución el hallazgo que afecta al plan en curso; el que no, se anota con su pendiente donde pertenece y el trabajo sigue.
""".format(p109=P109, hu004=HU004)


def main():
    t = io.open(A, encoding="utf-8").read()
    a = '1. «tema»: «lo que se decidió» (turno «N»).\n\nSiguen abiertas: «pregunta sin decidir, o "ninguna"».'
    assert t.count(a) == 1
    t = t.replace(a, ACORDADO)
    i = t.index("## Lo que aportó cada parte")
    io.open(A, "w", encoding="utf-8", newline="\n").write(t[:i] + SECCIONES)


if __name__ == "__main__":
    main()
