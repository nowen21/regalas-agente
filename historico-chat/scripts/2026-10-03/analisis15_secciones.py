# -*- coding: utf-8 -*-
"""Llena las secciones del análisis 15 del pendiente 103 (la conversación la escribe el enganche)."""
import glob
import io
import os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
P = glob.glob(os.path.join(RAIZ, "documentacion", "epicas", "EP-023-*", "pendientes", "103-*"))[0]
A = os.path.join(P, "analisis-15.md")
t = io.open(A, encoding="utf-8").read()

ENC = t[:t.index("## Conversación")]
COLA = t[t.index("## Conversación"):t.index("## Lo acordado")]
BASE = "../../../../../base/"

encabezado = """# Análisis 15: la revisión de los catorce análisis deja tres cosas abiertas

> Este análisis se redacta aplicando estas reglas.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](%s00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](%s00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](%s00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](%s00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Viene del [análisis 14](analisis-14.md), aprobado el 2026-10-03. Trata lo que dejó abierto la revisión de las 113 filas de los catorce análisis, y el H-19, que el freno anotó durante esa revisión.

---

## Recomendaciones

| Recomendación | Cómo se aplica en este análisis |
|---|---|
| R-1 | La revisión cubrió las 113 filas de los catorce análisis, no solo las que fallaron |
| R-16 | Lo que falló en el freno y en `pendientes.py` se corrige de una aquí |
| R-17 | Las respuestas se miden contra `00·ID9` |
| Las demás | No aplican: no se crean reglas y no hay plan en ejecución |

---

## Hallazgo

### H-19 · El freno detuvo una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-03 23:23, el freno detuvo una orden de consola sobre `validadores/=`: no hay una fase en curso y ninguna regla autoriza escribirlo (02·F8). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |

## Pendiente

Versión 6, del análisis 14: [pendiente](pendiente.md), tal como estaba al empezar este análisis.

---

""" % (BASE, BASE, BASE, BASE)

resto = """## Lo acordado

1. Lo que deja abierto la revisión de los catorce análisis se hace de una, desde este análisis, en el orden que el usuario aprobó: `pendientes.py` entiende «HU 1» con espacio, para que el pendiente 103 cierre; el freno no toma `>=` por escritura (el H-19); y se revisan con los validadores los documentos de EP-023 contra la base construida, que es la fila 10 del análisis 9 (turno 576).

Siguen abiertas: si la revisión de «cada fila tiene su CA» se vuelve un validador. Recomendación: no por ahora; en los análisis viejos el CA cita unas veces la fila y otras el acuerdo, y daría 13 avisos falsos.

---

## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `02·F8` (el freno), `13·DOC26` (el pendiente pasa a su versión siguiente) y `20·M10` (versionar). No choca ninguna.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| Las 113 filas de los catorce análisis | 110 cumplidas; abiertas: la fila 10 del análisis 9 y el cierre del pendiente 103 |
| `validadores/pendientes.py` | Reconoce «HU-001» y no «HU 1», que es como escribe el análisis 1: el pendiente 103 sale abierto con sus siete HU terminadas |
| `validadores/freno.py` | Toma el `>` de `>=` por una redirección a un archivo llamado `=` |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| Análisis 13, acuerdo 7 | El freno ya dejó de tomar el `>` entre comillas por escritura; el `>=` es el mismo tipo de error |
| Análisis 9, fila 10 | La revisión del piloto quedó para cuando EP-023 estuviera construida, y ya lo está |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | PARCHE, 53.1.1: dos correcciones que no cambian qué se exige |
| Normas y leyes | Ninguna |
| Herramientas | Ninguna condiciona lo acordado |

### Dónde más puede pasar

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Otra comparación con `>` en una orden, como `=>` o `>=` en un guion | Cualquier proyecto | El freno detiene una lectura | Punto 3 |
| Otro análisis que nombra la HU como «HU 2» | Cualquier proyecto | El pendiente no cierra | Punto 2 |

---

## Propuesta final: hallazgo y pendiente V7, épica y HU

### Hallazgo V7. El freno toma `>=` por escritura

| Campo | Valor |
|---|---|
| Qué pasó | El freno detuvo una orden de consola que solo leía: tomó el `>` de `>=` como una redirección a un archivo llamado `=`. |
| Por qué importa | Un freno que detiene lo que no escribe obliga a dar rodeos y anota hallazgos falsos en el resumen. |

### Pendiente V7. Lo que se construye se aparta de lo aprobado

| Campo | Valor |
|---|---|
| De dónde sale | Lo de la versión 6, más el H-19 de la sesión del 2026-10-01 |
| El problema | Lo de la versión 6, más: el freno toma `>=` por escritura, y el estado del pendiente no reconoce «HU 1» escrito con espacio |
| Por qué importa | Sin cambio |

### Épica y HU que salen del análisis

Ninguna nueva: todo se hace de una en este análisis.

## Lecciones aprendidas

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | Revisar fila por fila los análisis de un pendiente antes de darlo por cerrado encontró lo que ningún validador veía | Funcionó | Por registrar | complementa R-1 |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Pasar el pendiente a su versión siguiente | `13·DOC26` | Este análisis, de una y sin fase: `documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/pendiente.md` |
| 2 | Que `validadores/pendientes.py` reconozca «HU 1» con espacio, con su prueba | 1 | Este análisis, de una y sin fase: `validadores/pendientes.py`, `validadores/tests/test_el_pendiente_tiene_solo_lo_suyo.py` |
| 3 | Que `validadores/freno.py` no tome `>=` por escritura, con su prueba, y su entrada en `CHANGELOG.md` y `VERSION` | 1 | Este análisis, de una y sin fase: `validadores/freno.py`, `validadores/tests/test_el_freno.py`, `CHANGELOG.md`, `VERSION` |
| 4 | Revisar con los validadores los documentos de EP-023 contra la base construida y anotar el resultado en este análisis | 1 | Este análisis, de una y sin fase: `documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-15.md` |

## Lo que aporta al análisis principal

**Resultado:** aclara.

**Lo que suma al análisis principal:** Antes de dar por cerrado un pendiente se revisan, fila por fila, los análisis que lo trabajaron: así aparecen las filas que ningún criterio recogió.
"""
io.open(A, "w", encoding="utf-8", newline="\n").write(encabezado + COLA + resto)
print("listo")
