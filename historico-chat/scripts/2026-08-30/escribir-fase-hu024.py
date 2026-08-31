# -*- coding: utf-8 -*-
"""Escribe la fase A de EP-004 HU-024: el validador dice sobre que corrio."""
import io
import os

RAIZ = r"c:\Ing. Jose\ia\agente"
HU = os.path.join(RAIZ, "documentacion", "epicas", "EP-004-comprobacion-automatica",
                  "HU-024-el-validador-dice-que-no-comprueba")
F = "A-EP-004-HU-024-la-salida-dice-sobre-que-corrio"
M = u"Programas de comprobación"
D = os.path.join(HU, F)
if not os.path.isdir(D):
    os.makedirs(D)


def w(nombre, texto):
    with io.open(os.path.join(D, nombre), "w", encoding="utf-8",
                 newline="\n") as f:
        f.write(texto)


w("estado-fase.md", u"""# Estado de fase — Fase `{F}` (módulo {M})   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `{F}` |
| **Módulo** | {M} |
| **Planteamiento / Épica / HU** | [EP-004](../../epica.md) · [HU-024](../HU-024-el-validador-dice-que-no-comprueba.md) |
| **Última actualización** | 2026-08-30 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ✅ El caso lo vivió el propio agente ese día |
| 2 | Proponente · alcance | 👤 alcance aprobado | ✅ 2026-08-30 |
| 3 | Escritor de épica | 👤 épica aprobada | ✅ Ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ✅ 2026-08-30 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ✅ Los tres CA de la historia |
| 6 | Diseñador | diseño coherente | ✅ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ✅ |
| 8 | Implementador | implementado + pruebas verdes | ✅ 5 pruebas nuevas, 5 en verde |
| 9 | Verificador | trazabilidad sin faltantes | ✅ 4 tareas, 4 con resultado |
| 10 | Crítico | sin hallazgos graves | ✅ |
| 11 | Cierre documental + señales | docs y señales al día | ✅ `S-083` |
| 12 | Commit | 👤 autorizado | ☐ **Pendiente de autorización** |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 3 de 3 |
| **CA en "No"** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §2 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Evidencia |
|---|---|---|
| T-01 · que la corrida cuente qué archivos miró | Terminada | CP-001 |
| T-02 · armar las dos frases del alcance con ese dato | Terminada | CP-001, CP-004 |
| T-03 · distinguir «no había nada» de «no hay marcas» | Terminada | CP-003 |
| T-04 · que el subcomando las imprima | Terminada | La corrida del §3 |

**Hechas:** 4 de 4. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  `13·DOC5`

| Decisión / aprendizaje | Señal |
|---|---|
| Un cero que sale de no mirar se lee igual que uno limpio | `S-083` |

---

## 3. Pendiente / preguntas abiertas

- **La autorización del commit**, que se pide aparte.

---

## 4. Si se bloqueó

No se bloqueó.
""".format(F=F, M=M))

w("plan_trabajo.md", u"""# Plan de Trabajo — Fase `{F}` (módulo {M})   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio antes de darlo por cumplido.

---

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `{F}` |
| **Épica** | [EP-004](../../epica.md) |
| **HU** | [HU-024](../HU-024-el-validador-dice-que-no-comprueba.md), **una sola** (`F12.1`) |
| **Módulo** | {M} |
| **Fecha apertura** | 2026-08-30 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- **Defecto, y lo cobró el propio agente.** El 2026-08-30 corrió `validar.py marcas` sobre veinticinco documentos nuevos de `documentacion/`, obtuvo cero, y escribió en el cuerpo de un commit que el validador no reportaba ninguna línea de esos archivos. El enganche del commit, que sí lee lo que entra al índice, encontró **trece avisos** en esos mismos archivos. La afirmación falsa quedó publicada. Sale del [pendiente 91](../../../../../pendientes/91-el-validador-de-marcas-no-dice-que-no-comprueba.md).

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que la salida diga sobre qué corrió y qué partes de la norma no cuenta, para que un cero no se pueda leer como un aprobado.

**Fuera de alcance:**

- **Ampliar el recorrido a `documentacion/`.** Es más trabajo, produciría ruido de entrada porque esa carpeta arrastra deuda vieja, y es una decisión aparte.
- Construir la comprobación de las marcas que hoy se leen a mano.

---

## 2. Análisis previo, línea base verificada  ·  `02·F17`

> Medida antes de crear la carpeta de esta fase.

### 2.0 La línea base

```
119 cumplen, 0 no cumplen, 0 sin veredicto
```

### 2.1 Los dos filos del mismo cero

| Filo | Qué pasa |
|---|---|
| El alcance | El subcomando recorre `base/` y `plantillas/`. Sobre cualquier otra carpeta devuelve cero **porque no mira** |
| La cobertura | Cuenta las marcas mecánicas y deja para la lectura las que hay que juzgar. Su cero tampoco lo dice |

**Los dos se ven igual desde el resultado**, y por eso el primero engañó.

### 2.1.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/marcas.py` | Modificar | Comprobación | `alcance()`, y que `validar()` cuente lo que mira |
| `validadores/validar.py` | Modificar | Comprobación | Que el subcomando imprima las dos frases |
| `validadores/tests/test_el_validador_dice_sobre_que_corrio.py` | Crear | Pruebas | Cinco casos |
| Los cinco documentos de esta fase | Crear | Documentación | — |
| `HU-024-el-validador-dice-que-no-comprueba.md` | Modificar | Documentación | Su `Estado` y su tabla de fases |

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El alcance sale de **lo que la corrida recorrió** | Escribir la frase a mano | Una frase aparte envejece sin avisar, y este defecto nació de creerle a un número |
| Se nombra la carpeta **y cuántos archivos** | Solo la carpeta | El número es lo que deja ver que se miró algo, y distingue el árbol vacío |
| «No había nada que mirar» es una frase distinta | Dejar el mismo cero | Son dos respuestas y se imprimían igual |
| Las dos frases van **después** del resultado | Antes | Lo primero que se lee tiene que ser el veredicto; el alcance lo califica |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Que la corrida cuente qué archivos miró | Comprobación | 0,5 h | — | EV-01 |
| T-02 | Armar las dos frases con ese dato | Comprobación | 0,5 h | T-01 | EV-01 |
| T-03 | Distinguir «no había nada» de «no hay marcas» | Comprobación | 0,25 h | T-02 | EV-01 |
| T-04 | Que el subcomando las imprima | Comprobación | 0,25 h | T-03 | EV-02 |

**Total estimado:** 1,5 h

**Sin cambio de versión:** no se toca `base/` ni `plantillas/`.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 a T-02 a T-03 a T-04

La `T-01` va primero porque es la que hace honesto lo demás: sin contar, la
frase sería un texto escrito aparte, que es lo que se quiere evitar.

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| CA-01 · la salida nombra sobre qué corrió | Un árbol con archivos dentro y fuera del alcance | CP-001, CP-002 | ☑ |
| CA-02 · nombra qué no cuenta | La segunda frase, sobre un árbol limpio | CP-004 | ☑ |
| CA-03 · sin nada que mirar lo dice | Un árbol sin archivos en el alcance | CP-003 | ☑ |

---

## 6. Datos y ambiente de prueba

Árboles temporales que la propia prueba arma y borra.

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**Nada que desplegar.** Se nota la próxima vez que alguien corra el comando.

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `00·ID8`, las marcas que este validador comprueba.
- `04·R4`, se ejecuta en vez de afirmar sobre lo leído. Es la regla que el defecto rompió.
- `08·T5`, las pruebas corren y se reporta el número.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que la frase y el recorrido se separen con el tiempo | Volvería el mismo defecto por otra puerta | `CP-005` compara la frase con las carpetas que el programa recorre | Cerrado |
| B-02 | Que la salida se alargue tanto que nadie la lea | Dos líneas al final, y solo lo que cambia la lectura del número | — | Cerrado |

---

## 11. Definition of Done

- [x] Las dos frases, saliendo de lo recorrido
- [x] Cinco pruebas en verde
- [ ] Autorizado el commit por el usuario

---

## 12. Seguimiento diario

El avance en vivo va en el [estado-fase.md](estado-fase.md) §1.2.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
""".format(F=F, M=M))

w("plan_pruebas.md", u"""# Plan de Pruebas — Fase `{F}`   ·   `[CAPA 3]`

---

## 1. Introducción

### 1.1 Propósito

Comprobar que la salida del validador dice sobre qué corrió y qué no cuenta, y que esas frases salen de lo que la corrida recorrió.

### 1.2 Alcance

**Dentro:** los tres criterios de la historia, y la prueba de que la frase no se separa del recorrido.

**Fuera:** el conteo de marcas en sí, que ya tiene sus pruebas.

### 1.3 Documentos de referencia

- [HU-024](../HU-024-el-validador-dice-que-no-comprueba.md)
- El [pendiente 91](../../../../../pendientes/91-el-validador-de-marcas-no-dice-que-no-comprueba.md)

---

## 2. Elementos a probar

| Elemento | Por qué entra |
|---|---|
| El número de archivos mirados | Es lo que hace honesta la frase |
| Un archivo fuera del alcance | Es exactamente el cero que se leyó como aprobado |
| Un árbol sin nada que mirar | Las dos respuestas se imprimían igual |
| La lista de carpetas de la frase | Para que no se separe del recorrido |

---

## 3. Estrategia de pruebas

Sobre árboles temporales, armados con archivos dentro y fuera del alcance.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- El defecto, reproducido: ya lo estaba, en un commit publicado.

### 4.2 Criterios de salida

- Las cinco pruebas en verde.
- La corrida real imprime las dos frases.

### 4.3 Criterios de suspensión y reanudación

Si la frase tuviera que escribirse a mano para pasar, se suspende: sería el
mismo defecto con otra cara.

---

## 5. Matriz de trazabilidad

| CA | Caso |
|---|---|
| CA-01 | CP-001, CP-002, CP-005 |
| CA-02 | CP-004 |
| CA-03 | CP-003 |

---

## 6. Casos de prueba

### CP-001 — Dice cuántos archivos miró

Dos archivos dentro del alcance, y la frase dice «2 archivos».

### CP-002 — No cuenta lo que está fuera de su alcance

Un archivo de `documentacion/` **con una marca** no se reporta, y la frase deja
claro que no se miró. **Es el caso que originó la historia.**

### CP-003 — El árbol sin nada que mirar lo dice

Un árbol con archivos, pero ninguno en el alcance: la frase dice que no se miró
ninguno, en vez de callar.

### CP-004 — Dice qué partes no cuenta

La segunda frase nombra lo que hay que leer para verlo.

### CP-005 — La frase y el recorrido salen del mismo sitio

**La prueba que sostiene a las otras.** Si alguien amplía el alcance y no toca
la frase, esta se cae en vez de dejar que el reporte mienta.

---

## 7. Datos y ambientes de prueba

Carpetas temporales. Ningún archivo real se toca.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Pruebas en verde | 5 de 5 |
| Frases escritas a mano en vez de derivadas | **0** |

---

## 15. Aprobación

Alcance aprobado el 2026-08-30.
""".format(F=F))

w("resultado_pruebas.md", u"""# Resultado de Pruebas — Fase `{F}`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `{F}` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-30 |
| **Ciclo** | 1 |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los tres criterios se cumplen, y la frase del alcance sale de lo que la corrida recorrió, no de un texto escrito aparte.

| Métrica | Meta | Real |
|---|---|---|
| Pruebas en verde | 5 | **5** |
| Frases escritas a mano en vez de derivadas | 0 | **0** |

---

## 3. Resultado por caso

### La corrida real, sobre este repositorio

```
0 falla(s), 746 aviso(s).
Alcance: se recorrió `base/`, `plantillas/` (189 archivos), que es lo que viaja
a los proyectos.
Y no se cuenta lo que hay que leer para verlo: el español de otra parte, la
estructura demasiado pareja, el tono, y el contraste con lo escrito antes.
```

### Y sobre un árbol sin nada en su alcance

```
OK: sin incumplimientos.
Alcance: no se miró ningún archivo: en `base/`, `plantillas/` no hay ninguno
que revisar.
```

**Los dos ceros ya no se leen igual**, que era todo el defecto.

### Las cinco pruebas

```
Ran 5 tests in 0.087s
OK
```

**La que sostiene a las otras es la `CP-002`:** un archivo de `documentacion/`
**con una marca** no se reporta, y la frase dice que no se miró. Es exactamente
el cero que el 2026-08-30 se leyó como aprobado y terminó publicado en el cuerpo
de un commit.

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Por qué el número va en la frase

Nombrar la carpeta no alcanza: «se recorrió `base/`» es cierto también cuando no
había un solo archivo. El número es lo que separa «miré y no hay» de «no había
qué mirar», y es el que hace que la frase no pueda escribirse de antemano.

### 4.2 Lo que esta fase no promete

El alcance sigue siendo `base/` y `plantillas/`. Ampliarlo es una decisión
aparte, y lo que cambia acá es que **deja de ser invisible**.

---

## 5. Defectos encontrados

**Ninguno.**

---

## 6. Evidencias

- `validadores/marcas.py`, `alcance()` y el conteo de `validar()`
- `validadores/validar.py`, `cmd_marcas`
- `validadores/tests/test_el_validador_dice_sobre_que_corrio.py`
""".format(F=F))

w("funcionalidad_implementada.md", u"""# Funcionalidad implementada — Fase `{F}` (módulo {M})   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `{F}` |
| **Módulo** | {M} |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-30 |
| **HU / CA cubiertas** | [HU-024](../HU-024-el-validador-dice-que-no-comprueba.md): los tres |
| **Fecha de cierre** | 2026-08-30 |
| **Versión del estándar al cerrar** | `36.0.2` — **sin cambio** |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | Pendiente de autorización |

---

## 1. Qué se implementó — resumen

**Que el cero diga sobre qué corrió.**

| Antes | Ahora |
|---|---|
| «0 falla(s)» sin decir sobre qué | Dice qué carpetas recorrió y cuántos archivos miró |
| El mismo cero para «no hay marcas» y «acá no miré» | Dos frases distintas |
| No decía qué partes de la norma no cuenta | Las nombra |

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| CA | Ubicación | Estado | Evidencia |
|---|---|---|---|
| CA-01 | `marcas.alcance()` y el conteo de `validar()` | ✅ | CP-001, CP-002, CP-005 |
| CA-02 | `marcas.NO_SE_CUENTAN` | ✅ | CP-004 |
| CA-03 | `marcas.alcance()` con cero mirados | ✅ | CP-003 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Evidencia |
|---|---|
| T-01 · contar lo que mira | CP-001 |
| T-02 · armar las frases con ese dato | CP-001, CP-004 |
| T-03 · distinguir el árbol sin nada | CP-003 |
| T-04 · que el subcomando las imprima | La corrida del §3 |

**Correspondencia:** 4 tareas, 4 con resultado.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, ciclo 1 |
| **Suites ejecutadas** | 5 pruebas nuevas, 5 en verde |
| **Defectos abiertos** | Ninguno |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

```
python validadores/validar.py marcas
```

Sin cambios en cómo se llama: cambia lo que responde.

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué |
|---|---|
| El alcance sale de lo recorrido | Una frase escrita aparte envejece sin avisar |
| Se dice **cuántos** archivos, no solo la carpeta | «Se recorrió base/» es cierto también con cero archivos |
| Las frases van después del resultado | Lo primero que se lee tiene que ser el veredicto |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| El alcance sigue siendo `base/` y `plantillas/` | **Abierta y declarada.** Ampliarlo es una decisión aparte; lo que cambia acá es que deja de ser invisible |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] El `Estado` de la historia y su tabla de fases.
- [ ] `VERSION` y `CHANGELOG.md`: **no aplica**.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**Nada que desplegar.**
""".format(F=F, M=M))

# La historia, al dia.
R = os.path.join(HU, "HU-024-el-validador-dice-que-no-comprueba.md")
with io.open(R, encoding="utf-8") as f:
    t = f.read()
t = t.replace(u"| **Estado** | Pendiente |",
              u"| **Estado** | Terminada — los tres criterios se cerraron en la "
              u"fase `A` |", 1)
v = (u"| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | "
     u"Plan de pruebas | Resultado | Estado |\n|---|---|---|---|---|---|---|\n"
     u"| Sin abrir todavía | — | — | — | — | — | Sin empezar |")
n = (u"| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | "
     u"Plan de pruebas | Resultado | Estado |\n|---|---|---|---|---|---|---|\n"
     u"| [`%s`](%s/) | CA-01 a CA-03 | — | [plan_trabajo](%s/plan_trabajo.md) | "
     u"[plan_pruebas](%s/plan_pruebas.md) | [resultado](%s/resultado_pruebas.md) "
     u"· cumple | Terminada |" % (F, F, F, F, F))
if v in t:
    t = t.replace(v, n, 1)
    print("tabla de fases al dia")
with io.open(R, "w", encoding="utf-8", newline="\n") as f:
    f.write(t)
print("fase escrita:", F)
