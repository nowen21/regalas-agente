# -*- coding: utf-8 -*-
"""Escribe la fase B de EP-002 HU-001 y pone la historia al dia."""
import io
import os

RAIZ = r"c:\Ing. Jose\ia\agente"
HU = os.path.join(RAIZ, "documentacion", "epicas", "EP-002-versionado-y-adopcion",
                  "HU-001-numero-de-version-y-que-significa")
F = "B-EP-002-HU-001-el-numero-repetido-se-declara"
M = u"Versionado y adopción"
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
| **Planteamiento / Épica / HU** | [EP-002](../../epica.md) · [HU-001](../HU-001-numero-de-version-y-que-significa.md) |
| **Última actualización** | 2026-08-30 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ✅ Se leyeron las dos entradas `15.4.0` y el pendiente 22 |
| 2 | Proponente · alcance | 👤 alcance aprobado | ✅ 2026-08-30, sobre la propuesta escrita |
| 3 | Escritor de épica | 👤 épica aprobada | ✅ Ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ✅ Ya existía |
| 5 | Escritor de especificación | 👤 especificación aprobada | ✅ La lectura del CA-01, acordada en esta sesión |
| 6 | Diseñador | diseño coherente | ✅ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ✅ |
| 8 | Implementador | implementado + pruebas verdes | ✅ 5 pruebas de la clase, 5 en verde |
| 9 | Verificador | trazabilidad sin faltantes | ✅ 3 tareas, 3 con resultado |
| 10 | Crítico | sin hallazgos graves | ✅ |
| 11 | Cierre documental + señales | docs y señales al día | ✅ |
| 12 | Commit | 👤 autorizado | ☐ **Pendiente de autorización** |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 1 de 1, el CA-01 |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §2 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 · leer qué exige el CA-01 y qué decidió el registro | Terminada | El registro decidió no renumerar, y dice por qué |
| T-02 · que la prueba exija lo que se sostiene | Terminada | Sale del fallo esperado |
| T-03 · probar el repetido callado | Terminada | Sin eso, la prueba nueva pasa con cualquier registro |

**Hechas:** 3 de 3. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  `13·DOC5`

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Una prueba que exige lo que se decidió no cumplir no mide nada: enseña a ignorarla | Este cierre, §5 |
| El número repetido no se renumera, se declara | Registro del 2026-08-15 |

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
| **Épica** | [EP-002](../../epica.md) |
| **HU** | [HU-001](../HU-001-numero-de-version-y-que-significa.md), **una sola** (`F12.1`) |
| **Módulo** | {M} |
| **Fecha apertura** | 2026-08-30 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- **Cierra el CA-01, que quedó en rojo por una exigencia que el propio registro decidió no cumplir.** La fase [`A`](../A-EP-002-HU-001-retrodocumentar-el-numero-de-version/resultado_pruebas.md) cerró el 2026-08-22 porque `15.4.0` aparece dos veces, del 2026-08-14 y del 2026-08-15. Lo dejaron dos sesiones abiertas a la vez sobre el mismo repositorio, que es el [pendiente 22](../../../../../pendientes/hecho/dos-sesiones-versionando-a-la-vez.md).

**Y el registro ya decidió qué hacer con eso, el mismo 15 de agosto:** no se renumera. Un proyecto pudo haber adoptado `15.4.0`, y cambiarle el número después le mueve el piso sin que se entere. La segunda entrada lleva la marca de repetido y el motivo escrito.

**Entonces lo que estaba mal no era el registro: era la prueba.** Exigía unicidad, una exigencia que la casa decidió no cumplir por un motivo mejor, y por eso llevaba ocho días marcada como fallo esperado. Una prueba así no mide: enseña a ignorar los fallos esperados.

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que la prueba exija lo que de verdad se sostiene —que un número repetido esté declarado, con las dos entradas a la vista— y que salga del fallo esperado.

**Fuera de alcance:**

- **Renumerar la entrada.** Es lo que el registro decidió no hacer, y por buen motivo.
- **Tocar el `CHANGELOG.md`.** No se modifica ni una línea.
- **El aviso de `validar.py versionado`.** Ya dice lo que hay que decir, y se conserva: es lo que hace visible el caso en cada corrida.

---

## 2. Análisis previo, línea base verificada  ·  `02·F17`

> Medida antes de crear la carpeta de esta fase.

### 2.0 La línea base

```
102 cumplen, 7 no cumplen, 5 sin veredicto
```

### 2.1 Qué exige el CA-01 y qué hay

| Pieza | Estado |
|---|---|
| El número existe y sale de un solo archivo | Ya cumplía |
| Las entradas del registro declaran su tipo | Ya cumplía |
| Ningún número identifica dos cambios distintos | **`15.4.0` lo hace, y se decidió dejarlo** |
| La repetición está declarada donde se lee el número | **Sí**, en el encabezado de la entrada del 15 |

### 2.1.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/pruebas.py` | Modificar | Pruebas | La clase `NumeroDeVersion` |
| Los cinco documentos de esta fase | Crear | Documentación | — |
| `HU-001-numero-de-version-y-que-significa.md` | Modificar | Documentación | Su `Estado` y su tabla de fases |

**No se toca `CHANGELOG.md`, ni `VERSION`, ni ningún validador.**

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La prueba exige que lo repetido **se declare** | Exigir unicidad | Es lo que el registro decidió sostener, y con motivo escrito |
| La marca vale en **cualquiera de las dos entradas** | Exigirla en la segunda | Las dos comparten número; lo que importa es que la repetición esté dicha donde se lee |
| Se prueba también el **repetido callado** | Solo el caso real | Sin la contraprueba, la prueba nueva pasaría con un registro que pisa números en silencio |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Leer qué exige el CA-01 y qué decidió el registro | Análisis | 0,25 h | — | EV-01 |
| T-02 | Que la prueba exija lo que se sostiene | Pruebas | 0,75 h | T-01 | EV-02 |
| T-03 | Probar el repetido callado | Pruebas | 0,5 h | T-02 | EV-02 |

**Total estimado:** 1,5 h

**Sin cambio de versión:** no se toca `base/` ni `plantillas/`.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 a T-02 a T-03

La `T-03` no es opcional: sin ella, aceptar el repetido declarado es aceptar cualquier repetido.

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| CA-01, el número dice qué cambió y no se pisa en silencio | La prueba sobre el registro real, y la contraprueba sobre uno inventado | EV-02 | ☑ |

---

## 6. Datos y ambiente de prueba

El `CHANGELOG.md` real, sin tocarlo, y una secuencia inventada dentro de la prueba.

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**Nada que desplegar.**

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `20·M10`, todo cambio de regla se versiona y se registra. Es la regla que el número sostiene.
- `20·M11`, lo que ya se publicó no se reescribe. Es el motivo de no renumerar.
- `08·T5`, las pruebas corren y se reporta el número.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Aflojar la prueba para que pase | Sería tapar el defecto en vez de medirlo | `T-03`, la contraprueba | Cerrado |
| B-02 | Que alguien lea esto como permiso para repetir números | Dos cambios con el mismo número, a propósito | La prueba exige la declaración; el aviso de `versionado` sigue saliendo | Cerrado |

---

## 11. Definition of Done

- [x] La prueba, fuera del fallo esperado
- [x] La contraprueba, en verde
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

Comprobar el CA-01 de la HU-001 con la exigencia que el registro sí sostiene: **un número repetido queda declarado**, con sus dos entradas a la vista.

### 1.2 Alcance

**Dentro:** la secuencia de números del registro real, y una secuencia inventada con un repetido callado.

**Fuera:** renumerar nada, y el resto de criterios de la historia, que ya estaban en verde.

### 1.3 Documentos de referencia

- [HU-001](../HU-001-numero-de-version-y-que-significa.md)
- [Resultado de la fase A](../A-EP-002-HU-001-retrodocumentar-el-numero-de-version/resultado_pruebas.md)
- Las dos entradas `15.4.0` del `CHANGELOG.md`

---

## 2. Elementos a probar

| Elemento | Por qué entra |
|---|---|
| La secuencia del registro real | Es lo que el CA-01 mide |
| Un repetido **sin** declarar | Es el defecto de verdad, y en el registro real no ocurre |

---

## 3. Estrategia de pruebas

La comprobación se saca a un método propio que recibe la secuencia. Así el caso que no existe en el registro real se puede probar igual, sin inventar nada en el `CHANGELOG.md`.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- Las dos entradas `15.4.0` y su motivo, leídos.

### 4.2 Criterios de salida

- El registro real no produce ningún reclamo.
- El repetido callado produce exactamente uno.
- El mismo repetido, declarado, no produce ninguno.

### 4.3 Criterios de suspensión y reanudación

Si el registro real hubiera traído un repetido **sin** declarar, la fase no cierra: eso es un defecto y no una excepción.

---

## 5. Matriz de trazabilidad

| CA | Caso |
|---|---|
| CA-01 | CP-001, CP-002 |

---

## 6. Casos de prueba

### CP-001 — El registro real avanza, y lo repetido está declarado

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-01 |
| **Tipo** | De ejecución |
| **Prioridad** | Alta |
| **Cómo** | Recorrer las entradas del `CHANGELOG.md` de la más vieja a la más nueva |
| **Resultado esperado** | Cero reclamos |

### CP-002 — El repetido que no se declara sí falla

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-01, contraprueba |
| **Tipo** | Que **no** pase |
| **Prioridad** | **Crítica** |
| **Cómo** | Una secuencia inventada con `1.1.0` dos veces, primero callada y después declarada |
| **Resultado esperado** | Un reclamo en la callada, ninguno en la declarada |

---

## 7. Datos y ambientes de prueba

El registro real, sin modificarlo, y una lista escrita dentro de la prueba.

---

## 8. Herramientas

`python -m unittest pruebas.NumeroDeVersion`

---

## 9. Gestión de defectos

Un fallo en CP-001 significa que alguien pisó un número en silencio, y eso se arregla declarándolo, no renumerando.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Pruebas de la clase en verde | 5 de 5 |
| Pruebas marcadas como fallo esperado | **0** |

---

## 15. Aprobación

Alcance y lectura del CA-01 aprobados el 2026-08-30.
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

**Justificación:** el CA-01 se mide ahora contra lo que la casa sostiene. `15.4.0` sigue apareciendo dos veces y **eso no cambió**: cambió que la prueba dejó de exigir una unicidad que el registro decidió no cumplir, y pasó a exigir lo que sí se sostiene, que la repetición esté declarada. La prueba salió del fallo esperado.

| Métrica | Meta | Real |
|---|---|---|
| Pruebas de la clase en verde | 5 de 5 | **5 de 5** |
| Pruebas marcadas como fallo esperado | 0 | **0** |
| Líneas tocadas del `CHANGELOG.md` | 0 | **0** |

---

## 3. Resultado por caso

### CP-001 — El registro real avanza, y lo repetido está declarado

```
Ran 5 tests in 0.013s
OK
```

Las 133 entradas del registro recorridas de la más vieja a la más nueva: ningún salto mal formado, ninguna versión que baje, y la única repetición viene con su marca.

**Resultado: pasa.**

### CP-002 — El repetido que no se declara sí falla

| Secuencia | Reclamos |
|---|---|
| `1.0.0`, `1.1.0`, `1.1.0` sin marca | **1** |
| `1.0.0`, `1.1.0`, `1.1.0` con marca | **0** |

**Resultado: pasa.**

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Un detalle que cambió la comprobación

La marca de repetido está en la entrada del **2026-08-15**, y en el archivo esa entrada aparece **debajo** de la del 14. Al recorrer la secuencia de vieja a nueva, la declarada queda como la anterior del par y no como la siguiente, así que mirar solo el encabezado del segundo la daba por callada.

Se cambió a mirar los dos encabezados del par. No es un rodeo: **lo que se exige es que la repetición esté dicha donde se lee el número**, y las dos entradas comparten ese número.

Salió al ejecutar. Leyendo el código no aparecía.

### 4.2 El aviso de `validar.py versionado` sigue saliendo

```
[AVISO] CHANGELOG.md — el registro tiene 2 entradas para la 15.4.0
```

Se conserva a propósito: la prueba dice que está bien declarado, y el aviso lo mantiene a la vista en cada corrida.

---

## 5. Defectos encontrados

**Ninguno.**

---

## 6. Evidencias

- `validadores/pruebas.py`, clase `NumeroDeVersion`
- Las dos entradas `15.4.0` del `CHANGELOG.md`, sin tocar
""".format(F=F))

w("funcionalidad_implementada.md", u"""# Funcionalidad implementada — Fase `{F}` (módulo {M})   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `{F}` |
| **Módulo** | {M} |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-30 |
| **HU / CA cubiertas** | [HU-001](../HU-001-numero-de-version-y-que-significa.md): el CA-01 |
| **Fecha de cierre** | 2026-08-30 |
| **Versión del estándar al cerrar** | `35.10.0`, **sin cambio** |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | Pendiente de autorización |
| **Reemplaza el veredicto de** | `A-EP-002-HU-001-retrodocumentar-el-numero-de-version` |

> **Por qué se declara el reemplazo:** el CA-01 se mide ahora contra lo que la casa sostiene. Aquel rojo era cierto el 2026-08-22 con la lectura de entonces. **El veredicto de aquella fase no se toca** (`20·M11`).

---

## 1. Qué se implementó — resumen

**Que la prueba exija lo que se sostiene, no lo que se decidió no cumplir.**

`15.4.0` aparece dos veces porque dos sesiones numeraron a la vez. El registro decidió el 2026-08-15 **no renumerar**, y escribió el motivo: un proyecto pudo haber adoptado ese número, y cambiárselo después le mueve el piso sin que se entere.

La prueba, mientras tanto, seguía exigiendo unicidad y llevaba ocho días marcada como fallo esperado. **Una prueba que exige lo que la casa decidió no cumplir no mide nada:** enseña a mirar los fallos esperados como paisaje.

| Antes | Ahora |
|---|---|
| La prueba exige unicidad y está en fallo esperado | Exige que la repetición esté declarada, y corre |
| Un número repetido en silencio pasaría igual | Falla |

**El `CHANGELOG.md` no se tocó.**

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | prueba | `validadores/pruebas.py`, clase `NumeroDeVersion` | ✅ | CP-001, CP-002 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Estado | Evidencia |
|---|---|---|
| T-01 · leer qué exige el CA y qué decidió el registro | ✅ | §1 de este documento |
| T-02 · que la prueba exija lo que se sostiene | ✅ | 5 de 5 en verde |
| T-03 · probar el repetido callado | ✅ | CP-002 |

**Correspondencia:** 3 tareas, 3 con resultado.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, ciclo 1 |
| **Suites ejecutadas** | `pruebas.NumeroDeVersion`: 5 pruebas, 5 en verde, 0 fallos esperados |
| **Defectos abiertos** | Ninguno |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Sin cambios. El aviso de `validar.py versionado` sigue saliendo en cada corrida, y se conserva a propósito: mantiene el caso a la vista.

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué |
|---|---|
| No renumerar | Ya estaba decidido en el registro, con su motivo: quien adoptó `15.4.0` tiene las dos cosas |
| Cambiar la prueba, no el registro | Lo que estaba mal era la exigencia, no el dato |
| La marca vale en cualquiera de las dos entradas del par | Comparten número; lo que importa es que la repetición esté dicha |
| Probar el repetido callado | Sin eso, aceptar el declarado es aceptar cualquiera |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| Dos sesiones pueden volver a numerar a la vez | **Abierta.** Es el pendiente 22, y la comprobación de sesiones mezcladas es lo que se construyó para eso |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] El `Estado` de la historia y su tabla de fases.
- [ ] `VERSION` y `CHANGELOG.md`: **no aplica**, y en esta fase es lo importante: no se tocan.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**Nada que desplegar.**
""".format(F=F, M=M))

# La historia, al dia.
R = os.path.join(HU, "HU-001-numero-de-version-y-que-significa.md")
with io.open(R, encoding="utf-8") as f:
    t = f.read()
viejo = (u"| **Estado** | En curso \u2014 CA-02, CA-03 y transversales cumplidos; "
         u"el CA-01, no |")
nuevo = (u"| **Estado** | Terminada \u2014 el CA-01 se mide contra lo que el "
         u"registro sostiene: el n\u00famero repetido se declara, y as\u00ed se "
         u"comprueba desde la fase `B` |")
if viejo in t:
    t = t.replace(viejo, nuevo, 1)
    print("estado al dia")
sep = u"| Fase | Qu\u00e9 CA cubre | Estado |\n|---|---|---|\n"
fila = (u"| [%s](%s/estado-fase.md) | CA-01 | **Ejecutada el 2026-08-30.** "
        u"Veredicto: [**Cumple**](%s/resultado_pruebas.md#2-veredicto-de-la-fase) "
        u"\u2014 la prueba dej\u00f3 de exigir unicidad y exige que lo repetido est\u00e9 "
        u"declarado; el `CHANGELOG.md` no se toc\u00f3. Declara reemplazar el "
        u"veredicto de la fase `A` |\n" % (F, F, F))
if sep in t:
    t = t.replace(sep, sep + fila, 1)
    print("fila puesta")
with io.open(R, "w", encoding="utf-8", newline="\n") as f:
    f.write(t)
print("fase escrita:", F)
