# -*- coding: utf-8 -*-
"""Escribe la fase D de EP-004 HU-021: las dos formas de veredicto que faltaban."""
import io
import os

RAIZ = r"c:\Ing. Jose\ia\agente"
HU = os.path.join(RAIZ, "documentacion", "epicas", "EP-004-comprobacion-automatica",
                  "HU-021-la-cuenta-distingue-lo-terminado-de-lo-cumplido")
F = "D-EP-004-HU-021-las-dos-formas-que-quedaban-sin-leerse"
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
| **Planteamiento / Épica / HU** | [EP-004](../../epica.md) · [HU-021](../HU-021-la-cuenta-distingue-lo-terminado-de-lo-cumplido.md) |
| **Última actualización** | 2026-08-30 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ✅ Se leyeron las cinco que quedaban mudas |
| 2 | Proponente · alcance | 👤 alcance aprobado | ✅ 2026-08-30 |
| 3 | Escritor de épica | 👤 épica aprobada | ✅ Ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ✅ Ya existía |
| 5 | Escritor de especificación | 👤 especificación aprobada | ✅ El CA no cambia: cambia qué sabe leer el programa |
| 6 | Diseñador | diseño coherente | ✅ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ✅ |
| 8 | Implementador | implementado + pruebas verdes | ✅ 35 pruebas de la clase, 35 en verde |
| 9 | Verificador | trazabilidad sin faltantes | ✅ 4 tareas, 4 con resultado |
| 10 | Crítico | sin hallazgos graves | ✅ |
| 11 | Cierre documental + señales | docs y señales al día | ✅ |
| 12 | Commit | 👤 autorizado | ☐ **Pendiente de autorización** |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | El de la tercera cuenta: lo que dice su veredicto se lee |
| **CA en "No"** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §2 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 · leer las cinco que quedaban mudas | Terminada | Las cinco decían su veredicto |
| T-02 · ampliar el lector a las dos formas | Terminada | Sin tocar dónde se busca |
| T-03 · probar que no lee de más | Terminada | La tabla de criterios no se toma por el veredicto |
| T-04 · declarar el resultado | Terminada | 114 cumplen, 0 sin veredicto |

**Hechas:** 4 de 4. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  `13·DOC5`

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Cuatro fases para el mismo lector, y cada una encontró formas que la anterior no miró | §4.1 del resultado |

---

## 3. Pendiente / preguntas abiertas

- **La autorización del commit**, que se pide aparte.

---

## 4. Si se bloqueó

No se bloqueó.
""".format(F=F, M=M))

w("plan_trabajo.md", u"""# Plan de Trabajo — Fase `{F}` (módulo {M})   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** el criterio antes de darlo por cumplido.

---

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `{F}` |
| **Épica** | [EP-004](../../epica.md) |
| **HU** | [HU-021](../HU-021-la-cuenta-distingue-lo-terminado-de-lo-cumplido.md), **una sola** (`F12.1`) |
| **Módulo** | {M} |
| **Fecha apertura** | 2026-08-30 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- **Quedaban cinco historias contadas como «no dicen si cumplen», y las cinco lo dicen.** Al listarlas una por una aparecieron dos formas de escribir el veredicto que el lector no reconoce, después de tres fases dedicadas justamente a eso.

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que el lector reconozca las dos formas que faltaban, sin ampliar dónde busca.

**Fuera de alcance:**

- **Tocar los cinco resultados.** Son fases cerradas: se corrige el lector, no lo leído (`20·M11`).
- Aceptar títulos que empiecen por «Veredicto» y sean la tabla criterio por criterio. Eso es lo que la fase `C` dejó cerrado a propósito.

---

## 2. Análisis previo, línea base verificada  ·  `02·F17`

> Medida antes de crear la carpeta de esta fase.

### 2.0 La línea base

```
109 cumplen, 0 no cumplen, 5 sin veredicto
```

### 2.1 Las dos formas, y en cuántas fases está cada una

| Forma | Dónde | Cuántas |
|---|---|---|
| `**Concepto: Cumple.**`, con los dos puntos **dentro** de la negrita | Bajo `## 6. Veredicto de la fase` | 3 |
| `## 6. Concepto final` y la palabra debajo | El título dice «Concepto», no «Veredicto» | 2 |

**La primera es la que más engaña:** `**Concepto: Cumple.**` y `**Concepto:** Cumple` se leen igual y solo se diferencian en dónde cierran los asteriscos. El lector pedía los asteriscos justo después de «Concepto:».

**La segunda ya se aceptaba con la otra palabra.** La fase `B` leía la palabra sola bajo `## N. Veredicto de la fase`; estas dos usan `## N. Concepto final`, que es el otro término del glosario para lo mismo.

### 2.1.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/fases.py` | Modificar | Comprobación | Dos patrones más, y su uso |
| `validadores/pruebas.py` | Modificar | Pruebas | Tres casos: los dos nuevos y el que impide leer de más |
| Los cinco documentos de esta fase | Crear | Documentación | — |
| `HU-021-la-cuenta-distingue-lo-terminado-de-lo-cumplido.md` | Modificar | Documentación | Su tabla de fases |

**No se toca ninguno de los cinco resultados que quedaban mudos.**

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Se corrige el lector | Reescribir los cinco resultados | Son fases cerradas: `20·M11` |
| Se amplía **qué título vale**, no dónde se busca | Buscar la palabra suelta | En un resultado «Cumple» aparece en cada fila de criterio |
| El título nuevo se acepta con `[^\\n]*` detrás | Exigir «Concepto final» exacto | «Concepto» y «Concepto final» son la misma sección; lo que se exige es que sea un encabezado |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Leer las cinco que quedaban mudas | Análisis | 0,5 h | — | EV-01 |
| T-02 | Ampliar el lector | Comprobación | 0,5 h | T-01 | EV-02 |
| T-03 | Probar que no lee de más | Pruebas | 0,5 h | T-02 | EV-03 |
| T-04 | Declarar el resultado | Documentación | 0,25 h | T-03 | EV-03 |

**Total estimado:** 1,75 h

**Sin cambio de versión:** no se toca `base/` ni `plantillas/`.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 a T-02 a T-03 a T-04

La `T-01` va primero y no es trámite: **si las cinco no dijeran su veredicto, esto no sería un defecto del lector sino trabajo de cinco fases.**

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| La tercera cuenta dice la verdad: lo que declara su veredicto se lee | Contar antes y después, y probar el caso que no debe leerse | EV-01, EV-03 | ☑ |

---

## 6. Datos y ambiente de prueba

Árboles temporales que la propia prueba arma y borra, y el árbol real para la
línea base.

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**Nada que desplegar.** Lo que cambia es que el número deja de contar cinco
historias como mudas.

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `20·M11`, lo cerrado no se reescribe: se arregla quien lo lee.
- `04·R4`, se ejecuta en vez de afirmar sobre lo leído.
- `08·T5`, las pruebas corren y se reporta el número.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que el lector tome la fila de un criterio por el veredicto | Daría por cumplida una fase que no lo está: la mentira peor | `T-03` lo prueba | Cerrado |
| B-02 | Que la línea base se mueva al abrir la fase | `S-053` | Está anotada en el §2.0 | Cerrado |

---

## 11. Definition of Done

- [x] Las cinco, leídas antes de tocar nada
- [x] El lector, ampliado
- [x] Las 35 pruebas de la clase en verde
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

Comprobar que el lector del veredicto reconoce las dos formas que faltaban, y que sigue sin leer de más.

### 1.2 Alcance

**Dentro:** las dos formas nuevas, y el caso que no debe leerse.

**Fuera:** las tres formas que las fases `A`, `B` y `C` ya cubrían, que siguen con sus pruebas.

### 1.3 Documentos de referencia

- [HU-021](../HU-021-la-cuenta-distingue-lo-terminado-de-lo-cumplido.md)
- Los cinco resultados que quedaban mudos

---

## 2. Elementos a probar

| Elemento | Por qué entra |
|---|---|
| `**Concepto: Cumple.**` | Tres fases lo escriben así |
| `## N. Concepto final` con la palabra debajo | Dos fases lo escriben así |
| Una tabla de criterios antes del veredicto | Es lo que el lector **no** debe tomar |

---

## 3. Estrategia de pruebas

Sobre árboles temporales armados con el texto exacto de cada forma, y sobre el
árbol real para la línea base.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- Las cinco fases mudas, leídas: las cinco dicen su veredicto.

### 4.2 Criterios de salida

- Las 35 pruebas de la clase en verde.
- La cuenta de «sin veredicto» en cero, sin que ninguna pase de «No cumple» a «Cumple».

### 4.3 Criterios de suspensión y reanudación

Si al ampliar el lector alguna fase cambiara de «No cumple» a «Cumple», se
suspende: significaría que se está leyendo la fila de un criterio.

---

## 5. Matriz de trazabilidad

| CA | Caso |
|---|---|
| La tercera cuenta dice la verdad | CP-001, CP-002, CP-003 |

---

## 6. Casos de prueba

### CP-001 — Los dos puntos dentro de la negrita

| Campo | Valor |
|---|---|
| **Cómo** | Un resultado con `## 6. Veredicto de la fase` y `**Concepto: Cumple.**` |
| **Resultado esperado** | `(1, 0, 0)` |

### CP-002 — El encabezado que dice «Concepto»

| Campo | Valor |
|---|---|
| **Cómo** | Un resultado con `## 6. Concepto final` y `**Cumple.**` debajo |
| **Resultado esperado** | `(1, 0, 0)` |

### CP-003 — La tabla de criterios no se toma por el veredicto

| Campo | Valor |
|---|---|
| **Tipo** | Que **no** pase |
| **Prioridad** | **Crítica** |
| **Cómo** | Un resultado con una tabla de criterios en «Cumple» y el veredicto de la fase en «No cumple» |
| **Resultado esperado** | `(0, 1, 0)` |

**La CP-003 es la que sostiene a las otras dos.** Sin ella, ampliar el lector
sería aflojarlo.

---

## 7. Datos y ambientes de prueba

Carpetas temporales. Ningún resultado real se modifica.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Pruebas de la clase en verde | 35 de 35 |
| Fases que pasan de «No cumple» a «Cumple» | **0** |

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

**Justificación:** las cinco historias que se contaban como «no dicen si cumplen» lo decían. El lector reconoce ahora las dos formas que faltaban, y la cuenta de mudas queda en cero sin que ninguna fase cambie de «No cumple» a «Cumple».

| Métrica | Meta | Real |
|---|---|---|
| Pruebas de la clase en verde | 35 | **35** |
| Fases que pasan de «No cumple» a «Cumple» | 0 | **0** |
| Historias sin veredicto | 0 | **0**, eran 5 |

---

## 3. Resultado por caso

### CP-001 y CP-002 — Las dos formas que faltaban

Antes y después, sobre el árbol real:

```
antes:    109 cumplen ·  0 no cumplen ·  5 sin veredicto
después:  114 cumplen ·  0 no cumplen ·  0 sin veredicto
```

Las cinco, leídas una por una:

| Fase | Cómo lo escribe | Ahora se lee |
|---|---|---|
| `A-EP-003-HU-001-marca-de-espacio-por-llenar` | `## 6. Concepto final` | Cumple |
| `A-EP-003-HU-009-modelo-del-resumen-de-sesion` | `## 6. Concepto final` | Cumple |
| `A-EP-003-HU-010-glosario-de-la-terminologia` | `**Concepto: Cumple.**` | Cumple |
| `A-EP-005-HU-015-el-portero-del-contenido-externo` | `**Concepto: Cumple.**` | Cumple |
| `A-EP-005-HU-016-el-lector-de-la-traza` | `**Concepto: Cumple.**` | Cumple |

**Resultado: pasan.**

### CP-003 — La tabla de criterios no se toma por el veredicto

Un resultado con la tabla de criterios en «Cumple» y el veredicto de la fase en
«No cumple» devuelve `(0, 1, 0)`.

**Resultado: pasa.** Es la prueba que sostiene a las otras dos: sin ella,
ampliar el lector sería aflojarlo.

```
Ran 35 tests in 2.701s
OK
```

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Cuatro fases para el mismo lector, y cada una encontró lo que la anterior no miró

Vale dejarlo dicho porque es un patrón, no una casualidad:

| Fase | Qué agregó | Qué no había mirado |
|---|---|---|
| `A` | Que la cuenta mire el veredicto | — |
| `B` | La palabra sola bajo el encabezado | Contó las formas que ya sabía buscar |
| `C` | El mismo encabezado sin «de la fase» | La `B` dijo «39 sin encabezado» y eran 2 |
| `D` | Los dos puntos dentro de la negrita, y el título «Concepto» | Las cinco que quedaban, que nadie había abierto |

**Lo que se repite es la forma de equivocarse:** contar lo que el programa ya
sabe reconocer y llamar «otra cosa» a todo lo demás, sin abrirlo. Las cinco de
esta fase se resolvieron leyéndolas una por una, que es lo que ninguna de las
tres anteriores hizo con las que le quedaban.

### 4.2 No se tocó ninguno de los cinco resultados

Son fases cerradas. Se corrige quien lee, no lo leído (`20·M11`).

---

## 5. Defectos encontrados

**Ninguno.**

---

## 6. Evidencias

- `validadores/fases.py`, los patrones `_VEREDICTO` y `_VEREDICTO_CONCEPTO_TITULO`
- `validadores/pruebas.py`, clase `LaCuentaMiraElVeredicto`
- El guion que listó las mudas: `historico-chat/scripts/2026-08-30/medir-lo-que-queda.py`
""".format(F=F))

w("funcionalidad_implementada.md", u"""# Funcionalidad implementada — Fase `{F}` (módulo {M})   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `{F}` |
| **Módulo** | {M} |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-30 |
| **HU / CA cubiertas** | [HU-021](../HU-021-la-cuenta-distingue-lo-terminado-de-lo-cumplido.md): la tercera cuenta |
| **Fecha de cierre** | 2026-08-30 |
| **Versión del estándar al cerrar** | `36.0.0` — **sin cambio**: no se toca `base/` ni `plantillas/` |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | Pendiente de autorización |

---

## 1. Qué se implementó — resumen

**Que el lector del veredicto reconozca las dos formas que quedaban.**

Cinco historias se contaban como «no dicen si cumplen» y las cinco lo dicen, en
la primera línea de su sección final.

| Antes | Ahora |
|---|---|
| `**Concepto: Cumple.**` no se leía | Se lee |
| `## 6. Concepto final` con la palabra debajo, tampoco | Se lee |
| 5 historias sin veredicto | **0** |

**No se tocó ninguno de los cinco resultados.** Son fases cerradas: se corrige
quien lee, no lo leído.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| La tercera cuenta | comprobación | `validadores/fases.py` | ✅ | CP-001, CP-002, CP-003 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Estado | Evidencia |
|---|---|---|
| T-01 · leer las cinco mudas | ✅ | §3 del resultado |
| T-02 · ampliar el lector | ✅ | Dos patrones más |
| T-03 · probar que no lee de más | ✅ | CP-003 |
| T-04 · declarar el resultado | ✅ | Este documento |

**Correspondencia:** 4 tareas, 4 con resultado.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, ciclo 1 |
| **Suites ejecutadas** | `pruebas.LaCuentaMiraElVeredicto`: 35 pruebas, 35 en verde |
| **Defectos abiertos** | Ninguno |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Sin cambios: `python validadores/validar.py fases`.

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué |
|---|---|
| Se corrige el lector, no los cinco resultados | Son fases cerradas (`20·M11`) |
| Se amplía qué título vale, nunca dónde se busca | «Cumple» aparece en cada fila de criterio |
| La prueba que más importa es la que **no** debe leer | Ampliar sin ella sería aflojar |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| Cuatro fases para el mismo lector, cada una contando lo que ya sabía reconocer | **Anotada** en el §4.1 del resultado. El remedio no es otro patrón: es abrir lo que queda |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] La tabla de fases de la historia.
- [ ] `VERSION` y `CHANGELOG.md`: **no aplica**.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**Nada que desplegar.**
""".format(F=F, M=M))

# La historia, al dia: solo la fila, porque su Estado ya dice «Terminada».
R = os.path.join(HU, "HU-021-la-cuenta-distingue-lo-terminado-de-lo-cumplido.md")
with io.open(R, encoding="utf-8") as f:
    t = f.read()
sep = u"| Fase | Qué CA cubre | Estado |\n|---|---|---|\n"
fila = (u"| [%s](%s/estado-fase.md) | La tercera cuenta | **Ejecutada el "
        u"2026-08-30.** Veredicto: "
        u"[**Cumple**](%s/resultado_pruebas.md#2-veredicto-de-la-fase) — el "
        u"lector reconoce las dos formas que quedaban, y las historias sin "
        u"veredicto pasan de 5 a 0 |\n" % (F, F, F))
if sep in t:
    t = t.replace(sep, sep + fila, 1)
    print("fila puesta")
with io.open(R, "w", encoding="utf-8", newline="\n") as f:
    f.write(t)
print("fase escrita:", F)
