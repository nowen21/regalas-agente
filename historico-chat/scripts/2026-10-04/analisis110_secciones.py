# -*- coding: utf-8 -*-
"""Llena las secciones del análisis 1 del pendiente 110 (la conversación la escribe el enganche)."""
import glob
import io
import os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
P = glob.glob(os.path.join(RAIZ, "documentacion", "epicas", "EP-023-*", "HU-003-*", "pendientes", "110-*"))[0]
A = os.path.join(P, "analisis-1.md")
t = io.open(A, encoding="utf-8").read()
COLA = t[t.index("## Conversación"):t.index("## Lo acordado")]
PEND = io.open(os.path.join(P, "pendiente.md"), encoding="utf-8").read()
PEND = PEND[PEND.index("| | |"):].strip()
B = "../../../../../../base/"
PE = "documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/"
HU7 = PE + "HU-007-nada-se-escribe-fuera-del-plan-aprobado/pendientes/112-el-control-de-commits-rechaza-lo-que-crean-las-herramientas/pendiente.md"
P111 = "documentacion/epicas/EP-004-comprobacion-automatica/HU-012-marcas-de-generacion-automatica/pendientes/111-el-control-de-redaccion-ve-guiones-suaves-en-cada-i-tildada/pendiente.md"
P113 = "historico-chat/resumenes/2026-10-04/pendientes/113-el-freno-toma-texto-de-los-comandos-como-rutas/pendiente.md"
P114 = "historico-chat/resumenes/2026-10-04/pendientes/114-el-instalador-deja-enlaces-rotos-en-stack-md/pendiente.md"

encabezado = """# Análisis 1: lo que un proyecto reporta es un defecto de Cimiento en todos los proyectos

> Este análisis se redacta aplicando estas reglas.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`]({b}00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`]({b}00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`]({b}00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`]({b}00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Reúne los cinco pendientes que reportó scilit el 2026-10-03: el 110 y el 111 a 114.

---

## Recomendaciones

| Recomendación | Cómo se aplica en este análisis |
|---|---|
| R-1 | Cada causa se revisó en los 12 proyectos reales de la base de datos, no solo en scilit |
| R-12 | Lo que se construye sirve a cualquier proyecto: cada arreglo se prueba desde un proyecto que no es Cimiento |
| Las demás | No aplican: no hay plan en ejecución |

---

## Hallazgo

Los hallazgos del proyecto scilit en el resumen de su sesión del 2026-10-03, reportados a Cimiento con los pendientes 110 a 114.

## Pendiente

{pend}

---

""".format(b=B, pend=PEND)

resto = """## Lo acordado

1. Todo lo que un proyecto reporta a Cimiento es un defecto que ya está en todos los proyectos que lo usan. No se analiza como un caso aislado: se busca su causa en Cimiento, se revisa cómo afecta a los demás proyectos y se corrige en la raíz. Va como regla, `02·F29`, que complementa `02·F24` desde el lado de Cimiento, y como recuerdo en Cimiento (turno 615).
2. Los cinco reportes de scilit tienen tres causas, y las tres se corrigen en su raíz: las herramientas suponen que corren dentro de Cimiento (110 y 114); los controles no conocen lo que escriben las mismas herramientas (112 y 113); cinco enganches no leen la entrada en UTF-8 (111). Cada arreglo se prueba desde un proyecto que no es Cimiento y se comprueba contra scilit y matematica sin escribir en ellos (turno 615).
3. Los proyectos son los de la base de datos de la interfaz, no los de `plantillas/proyectos.md`. Las pruebas dejan de registrar proyectos en la base real y se borran sus 860 registros de prueba; toda revisión que recorra los proyectos los toma de la base (turnos 614 y 615).
4. Los pendientes 111 a 114 se resuelven en este análisis: cada uno dice que se resuelve aquí, y su estado es el del 110, para que el aviso de resuelto le llegue a scilit por cada uno (turno 615).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `02·F24` (el proyecto reporta), `20·M3` (lo de `base/` sirve a cualquier proyecto) y `20·M10` (versionar). No choca ninguna; `02·F29` llena el lado de Cimiento que `02·F24` no decía.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| Proyectos reales en la base | 12, todos en Windows; la base tiene además 860 de prueba |
| `validadores/andamio.py` | Busca las plantillas en el proyecto y arma enlaces relativos a Cimiento |
| `.agente/stack.md` | Enlaces rotos en scilit (5) y matematica (1); los demás tienen uno anterior |
| `documentacion/versiones/` | La tienen los 12; los controles no saben que la escribe el instalador |
| Enganches que leen la entrada | Cinco usan la codificación de la consola, no UTF-8 |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| Análisis 16 del pendiente 103, acuerdo 2 | «Corrija» es para lo que bloquea dentro de Cimiento; un reporte de un proyecto pide análisis de causa y alcance (acuerdo 1) |
| Lección S-290 | No abrir análisis de más; aquí uno solo reúne cinco reportes |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | MENOR: una regla de Cimiento y correcciones que no piden nada nuevo a los proyectos |
| Normas y leyes | Ninguna |
| Herramientas | La consola de Windows no es UTF-8 |

### Dónde más puede pasar

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Otra herramienta que arma rutas relativas a Cimiento | Cualquier proyecto | Enlaces rotos | Punto 2 |
| Otro archivo que escriben las herramientas y los controles no conocen | Cualquier proyecto | Commits rechazados | Punto 3 |
| Otro enganche que lea la entrada sin UTF-8 | Cualquier proyecto en Windows | Avisos falsos | Punto 4: una sola función común |
| Otra prueba que escriba en la base real | Cimiento | Registro contaminado | Punto 5 |

---

## Propuesta final: hallazgo y pendiente V«N+1», épica y HU

No aplica: es el análisis que origina el pendiente.

### Épica y HU que salen del análisis

Ninguna nueva: se hace de una en este análisis.

## Lecciones aprendidas

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | Los arreglos de un reporte se empezaron pensando solo en Cimiento | Falló | Por registrar | complementa R-12 |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Crear `02·F29`, con su índice, las copias por tarea, el registro de validables, y su entrada en `CHANGELOG.md` y `VERSION`; y el recuerdo en Cimiento | 1 | Este análisis, de una y sin fase: `base/02-flujo-de-trabajo/reglas/F29-el-reporte-de-un-proyecto-se-corrige-para-todos.md`, `base/02-flujo-de-trabajo/base.md`, `base/reglas-por-tarea/README.md`, `base/reglas-por-tarea/trabajar-cadena-1.md`, `base/reglas-por-tarea/trabajar-cadena-2.md`, `base/mapa-de-tareas.md`, `validadores/reglas-validables.md`, `historico-chat/memory/el-reporte-de-un-proyecto-es-de-todos.md`, `historico-chat/memory/memory.md`, `CHANGELOG.md`, `VERSION` |
| 2 | Que el andamio tome las plantillas del estándar y arme los enlaces para el proyecto, que cree el pendiente también en una épica, y que el instalador deje `stack.md` sin enlaces rotos, con sus pruebas desde un proyecto | 2 | Este análisis, de una y sin fase: `validadores/andamio.py`, `validadores/instalar.py`, `validadores/tests/test_el_reporte_de_un_proyecto_se_corrige_para_todos.py` |
| 3 | Que los controles conozcan lo que escriben las herramientas del estándar (`documentacion/versiones/`, el `README.md` de cada HU) y la carpeta de un archivo declarado | 2 | Este análisis, de una y sin fase: `validadores/autorizado.py`, `validadores/freno.py`, `validadores/tests/test_el_reporte_de_un_proyecto_se_corrige_para_todos.py` |
| 4 | Que todo enganche lea la entrada en UTF-8 con una sola función común | 2 | Este análisis, de una y sin fase: `validadores/comun.py`, `adaptadores/claude-code/hook_md.py`, `adaptadores/claude-code/hook_checkpoint.py`, `adaptadores/claude-code/hook_externo.py`, `adaptadores/claude-code/hook_presupuesto.py`, `adaptadores/claude-code/hook_redaccion.py` |
| 5 | Que las pruebas no registren proyectos en la base real, y borrar sus 860 registros | 3 | Este análisis, de una y sin fase: `validadores/instalar.py`, `plantillas/proyectos.md` |
| 6 | Que los pendientes 111 a 114 digan que se resuelven aquí y tomen el estado del 110 | 4 | Este análisis, de una y sin fase: `validadores/pendientes.py`, `validadores/tests/test_el_reporte_de_un_proyecto_se_corrige_para_todos.py`, `{p111}`, `{p112}`, `{p113}`, `{p114}` |

## Lo que aporta al análisis principal

**Resultado:** amplía.

**Lo que suma al análisis principal:** Lo que un proyecto reporta se corrige en Cimiento para todos los proyectos que lo usan, y se comprueba en ellos.
""".format(p111=P111, p112=HU7, p113=P113, p114=P114)
io.open(A, "w", encoding="utf-8", newline="\n").write(encabezado + COLA + resto)
print("listo")
