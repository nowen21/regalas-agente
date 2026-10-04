# -*- coding: utf-8 -*-
"""Llena las secciones del análisis 16 del pendiente 103 (la conversación la escribe el enganche)."""
import glob
import io
import os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
P = glob.glob(os.path.join(RAIZ, "documentacion", "epicas", "EP-023-*", "pendientes", "103-*"))[0]
A = os.path.join(P, "analisis-16.md")
t = io.open(A, encoding="utf-8").read()
COLA = t[t.index("## Conversación"):t.index("## Lo acordado")]
BASE = "../../../../../base/"
EP = "documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/"

encabezado = """# Análisis 16: el commit rechaza lo que un análisis aprobado mandó hacer de una

> Este análisis se redacta aplicando estas reglas.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](%s00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](%s00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](%s00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](%s00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Viene del [análisis 15](analisis-15.md), aprobado el 2026-10-03. Trata el H-20, que apareció al guardar el commit de los análisis 14 y 15.

---

## Recomendaciones

| Recomendación | Cómo se aplica en este análisis |
|---|---|
| R-16 | Lo que falló en el control del commit se corrige de una aquí |
| R-17 | Las respuestas se miden contra `00·ID9` |
| Las demás | No aplican: no se crean reglas y no hay plan en ejecución |

---

## Hallazgo

### H-20 · El commit rechaza lo que un análisis aprobado mandó hacer de una

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-03, el control del commit rechazó 12 archivos que las filas «de una» de los análisis 14 y 15 del pendiente 103 mandaron hacer: solo acepta esas filas mientras el análisis está prendido, y los dos ya estaban aprobados. |
| Por qué importa | Lo que un análisis manda hacer de una no se puede guardar después de aprobarlo, y aprobarlo es el paso anterior al commit. |

## Pendiente

Versión 7, del análisis 15: [pendiente](pendiente.md), tal como estaba al empezar este análisis.

---

""" % (BASE, BASE, BASE, BASE)

resto = """## Lo acordado

1. El control del commit acepta también las rutas «de una» de todo análisis que entra en el mismo commit, prendido o aprobado: el análisis y lo que mandó hacer se guardan juntos. Se corrige de una (turnos 580 a 582).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `02·F8` (lo que entra al commit está en el plan o lo autoriza algo) y `20·M10` (versionar). No choca ninguna.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| `validadores/plan_vs_hecho.py` | Acepta las rutas «de una» solo del análisis prendido (análisis 14, acuerdo 5) |
| `validadores/freno.py` | `_de_una` lee el análisis prendido; no hay una función que lea un análisis cualquiera |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| Análisis 14, acuerdo 5 | El freno y el control del commit usan la misma lista; aquí la del commit se amplía a los análisis que entran con él |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | PARCHE, 53.1.2: el commit deja de rechazar lo que un análisis aprobado mandó hacer |
| Normas y leyes | Ninguna |
| Herramientas | Ninguna condiciona lo acordado |

### Dónde más puede pasar

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Un análisis aprobado en una sesión y guardado en otra | Cualquier proyecto | El commit lo rechaza | Punto 1: basta con que el análisis entre en el mismo commit |
| Un archivo «de una» que se guarda sin su análisis | Cualquier proyecto | Se rechaza | No hace falta cubrirlo: así el commit no se lleva lo que nadie mandó |

---

## Propuesta final: hallazgo y pendiente V8, épica y HU

### Hallazgo V8. El commit rechaza lo que un análisis aprobado mandó hacer de una

| Campo | Valor |
|---|---|
| Qué pasó | El control del commit solo aceptaba las filas «de una» del análisis prendido. |
| Por qué importa | Lo que se manda hacer de una no se podía guardar después de aprobar el análisis. |

### Pendiente V8. Lo que se construye se aparta de lo aprobado

| Campo | Valor |
|---|---|
| De dónde sale | Lo de la versión 7, más el H-20 de la sesión del 2026-10-01 |
| El problema | Lo de la versión 7, más: el control del commit no aceptaba lo que un análisis aprobado mandó hacer de una |
| Por qué importa | Sin cambio |

### Épica y HU que salen del análisis

Ninguna nueva: se hace de una en este análisis.

## Lecciones aprendidas

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | Una autorización que vale solo mientras el análisis está prendido se acaba antes del commit, que viene después de aprobar | Falló | Por registrar | complementa R-16 |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Pasar el pendiente a su versión siguiente | `13·DOC26` | Este análisis, de una y sin fase: `%spendiente.md` |
| 2 | Que el control del commit acepte las rutas «de una» de todo análisis que entra en el mismo commit, con su prueba, y su entrada en `CHANGELOG.md` y `VERSION` | 1 | Este análisis, de una y sin fase: `validadores/plan_vs_hecho.py`, `validadores/freno.py`, `validadores/tests/test_nada_fuera_del_plan.py`, `CHANGELOG.md`, `VERSION` |

## Lo que aporta al análisis principal

**Resultado:** aclara.

**Lo que suma al análisis principal:** Lo que un análisis manda hacer de una se guarda en el mismo commit que el análisis.
""" % EP
io.open(A, "w", encoding="utf-8", newline="\n").write(encabezado + COLA + resto)
print("listo")
