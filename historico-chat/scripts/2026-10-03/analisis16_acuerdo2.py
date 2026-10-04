# -*- coding: utf-8 -*-
"""Suma al análisis 16 el acuerdo 2 (salir del ciclo de análisis) y sus filas de una."""
import glob
import io
import os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
A = glob.glob(os.path.join(RAIZ, "documentacion", "epicas", "EP-023-*", "pendientes", "103-*", "analisis-16.md"))[0]
t = io.open(A, encoding="utf-8").read()

viejo = "Se corrige de una (turno 582).\n"
assert t.count(viejo) == 1
t = t.replace(viejo, viejo + (
    "2. Salir del ciclo de análisis: de los 16 análisis del pendiente, solo el 1, el 8, el 10 y el 13 trajeron trabajo nuevo. "
    "Se hacen de una cuatro cosas: con «Corrija», el agente corrige una herramienta del proceso (`validadores/`, `adaptadores/`) "
    "que bloquea el trabajo sin abrir análisis, y lo anota en el resumen; un programa avisa qué pruebas leen los archivos que el plan "
    "cambia y el plan no declara; el freno no lee como escritura lo que va dentro de un heredoc, y el commit no cuenta como tocada una "
    "fase solo porque se anotó su hash. El pendiente 103 cierra con este análisis: lo que aparezca después va a un pendiente nuevo "
    "(turnos 583 a 589).\n"))

ANT = "| 2 | Que el control del commit acepte"
i = t.index(ANT)
j = t.index("\n", i) + 1
filas = (
    "| 3 | Que «Corrija» deje corregir las herramientas del proceso sin abrir análisis: el enganche lo anota al recibir el mensaje, "
    "el freno deja escribir `validadores/` y `adaptadores/` en esa respuesta, y `02·F8` lo dice como excepción, con su prueba, "
    "las copias por tarea y su entrada en `CHANGELOG.md` | 2 | Este análisis, de una y sin fase: "
    "`validadores/analisis_en_curso.py`, `adaptadores/claude-code/hook_analisis.py`, `validadores/freno.py`, "
    "`validadores/tests/test_el_freno.py`, "
    "`base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md`, "
    "`base/reglas-por-tarea/trabajar-cadena-1.md`, `base/reglas-por-tarea/trabajar-cadena-2.md`, "
    "`base/reglas-por-tarea/escribir-documento-1.md`, `base/reglas-por-tarea/escribir-documento-2.md`, "
    "`base/reglas-por-tarea/cambiar-codigo-1.md`, `base/reglas-por-tarea/cambiar-codigo-2.md`, "
    "`base/reglas-por-tarea/cambiar-codigo-3.md`, `base/reglas-por-tarea/cambiar-codigo-4.md`, "
    "`base/reglas-por-tarea/README.md`, `base/mapa-de-tareas.md` |\n"
    "| 4 | Que `validar.py plan` avise qué pruebas leen los archivos que el plan cambia y el plan no declara, con su prueba | 2 | "
    "Este análisis, de una y sin fase: `validadores/plan_vs_hecho.py`, `validadores/validar.py`, "
    "`validadores/tests/test_nada_fuera_del_plan.py` |\n"
    "| 5 | Que el freno no lea como escritura lo que va dentro de un heredoc, con su prueba | 2 | "
    "Este análisis, de una y sin fase: `validadores/freno.py`, `validadores/tests/test_el_freno.py` |\n"
    "| 6 | Que el commit no cuente como tocada una fase solo porque entra su `estado-fase.md`, con su prueba | 2 | "
    "Este análisis, de una y sin fase: `validadores/plan_vs_hecho.py`, `validadores/tests/test_nada_fuera_del_plan.py` |\n")
t = t[:j] + filas + t[j:]
io.open(A, "w", encoding="utf-8", newline="\n").write(t)
print("listo")
