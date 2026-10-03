# -*- coding: utf-8 -*-
"""Análisis 11 del pendiente 103: lo acordado y las secciones que siguen."""
import glob
import io
import os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
P = glob.glob(os.path.join(RAIZ, "documentacion", "epicas", "EP-023-*", "pendientes", "103-*"))[0]
A = os.path.join(P, "analisis-11.md")
HU007 = "[HU-007](../../HU-007-nada-se-escribe-fuera-del-plan-aprobado/HU-007-nada-se-escribe-fuera-del-plan-aprobado.md)"

ACORDADO = """1. El hallazgo y el plan en curso: el H-14 abre este análisis y es parte del plan en curso. El plan de la fase `B` de la HU-007 pasa a su versión siguiente con `validadores/autorizado.py` y `validadores/tests/test_nada_fuera_del_plan.py` en su tabla, y la ejecución sigue desde la T-04 (turnos 420 y 421).
2. Dónde se agrega o se quita un permiso: en la regla misma, con su línea «Autoriza escribir». Una regla que entra o sale funciona sin que se rechace y sin tocar el programa (turnos 413 a 415).
3. El estado de la regla decide: la vigente da permiso; la derogada, con `[DEROGADA…]` en su título, y la *opt-in* apagada no lo dan, aunque conserven la línea (turnos 416 a 421).
4. La prueba no fija nombres ni cantidad: comprueba con reglas de ejemplo que la vigente autoriza y que la derogada o la apagada no (turnos 413, 414 y 421).

Siguen abiertas: ninguna."""

SECCIONES = """## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `20·M11` (la regla que sale se deroga y no se borra), `02·F8` y `02·F9` (lo que el plan no previó detiene la ejecución) y el acuerdo 46 del análisis 1 (el freno solo detiene lo que no está autorizado en ninguna parte). Ninguna choca con lo acordado.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| `validadores/autorizado.py` | Lee la línea «Autoriza escribir» de toda regla, sin mirar si está derogada o apagada |
| `validadores/tests/test_nada_fuera_del_plan.py` | Su prueba `test_las_diez_reglas_traen_su_linea` exige exactamente diez reglas, con sus nombres |
| Reglas derogadas | Llevan `[DEROGADA en X → ver Y]` en su título y se quedan en `base/` |
| Reglas *opt-in* | `validadores/recuperar.py` sabe cuáles apagó el proyecto (`opt_in_apagados`) |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| Análisis 1, acuerdo 46 | La regla es la que autoriza. Lo recogen los acuerdos 2 y 3 |
| Fase `A` de la HU-007 | Decidió que la línea vive en la regla y no en una lista aparte; su prueba contradijo esa decisión con una lista fija. Lo recoge el acuerdo 4 |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | Entra en la versión MAYOR de la fase `B` de la HU-007; `02·F22` no aplica |
| Normas y leyes | Ninguna aplica |
| Herramientas | Ninguna condiciona lo acordado |

### Dónde más puede pasar

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Prueba que fija cuántas o cuáles reglas hay | Cualquier validador del estándar | Falla cada vez que una regla entra o sale | Punto 2 |
| Regla derogada que conserva su línea | Cualquier proyecto | Sigue dando permiso sin regir | Punto 1 |
| Regla *opt-in* apagada | Proyectos que apagan reglas opcionales | Da permiso aunque el proyecto no la usa | Punto 1 |
| Regla propia de un proyecto derogada | Proyectos con reglas propias | Sigue dando permiso | Punto 1: la misma marca en su título |
| Tarea que cambia algo que una prueba o un programa lee | Cualquier fase | Sale un hallazgo al ejecutar | Lección 1: al planear se buscan los que leen lo que cambia |

---

## Propuesta final: hallazgo y pendiente

> El H-14 no cambia. El pendiente sigue en la V3. EP-023 no suma HU: lo que se tiene que hacer entra en la fase `B` de la HU-007, que es el plan en curso.

### Épica y HU que salen del análisis

EP-023, Lo que se construye es lo que se analizó.

| Orden | HU | Título | Parte del problema que resuelve | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|---|---|
| 1 | {hu} | Nada se escribe fuera del plan aprobado | Nada detiene al agente cuando trabaja fuera del plan aprobado | HU-002, HU-003, HU-004 | Es el plan en curso; la ejecución sigue desde la T-04 | 1, 2, 3 |

## Lecciones aprendidas

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | Al planear un cambio de reglas no se buscó qué pruebas las leen | Falló | S-274 | complementa R-2 |
| 2 | Una prueba con una lista fija de reglas falla cada vez que una regla entra o sale | Falló | S-275 | complementa R-12 |
| 3 | El estado vive en la regla: entrar o salir no toca el programa | Funcionó | S-276 | complementa R-1 |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Que `autorizado.py` lea el estado de cada regla y use solo la vigente: la derogada y la *opt-in* apagada no autorizan | 2, 3 | EP-023, {hu}, fase B |
| 2 | Que la prueba de lo autorizado no fije nombres ni cantidad, y lo compruebe con reglas de ejemplo | 4 | EP-023, {hu}, fase B |
| 3 | Pasar el plan de la fase `B` a su versión siguiente con `validadores/autorizado.py` y `validadores/tests/test_nada_fuera_del_plan.py` en su tabla, y seguir desde la T-04 | 1 | EP-023, {hu}, fase B |

## Lo que aporta al análisis principal

**Resultado:** Aclara.

**Lo que suma al análisis principal:** Agregar o quitar un permiso es cambiar la regla, no el programa: el programa lee en cada regla si está vigente, y las pruebas no fijan cuáles ni cuántas son.
""".format(hu=HU007)


def main():
    t = io.open(A, encoding="utf-8").read()
    a = '1. «tema»: «lo que se decidió» (turno «N»).\n\nSiguen abiertas: «pregunta sin decidir, o "ninguna"».'
    assert t.count(a) == 1
    t = t.replace(a, ACORDADO)
    i = t.index("## Lo que aportó cada parte")
    t = t[:i] + SECCIONES
    io.open(A, "w", encoding="utf-8", newline="\n").write(t)


if __name__ == "__main__":
    main()
