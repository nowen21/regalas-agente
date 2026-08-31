# -*- coding: utf-8 -*-
"""Escribe la fase B de EP-006 HU-001 y pone la historia al dia."""
import io
import os

RAIZ = r"c:\Ing. Jose\ia\agente"
HU = os.path.join(RAIZ, "documentacion", "epicas", "EP-006-memoria-de-lo-aprendido",
                  "HU-001-que-se-guarda-tipos-y-alcances")
F = "B-EP-006-HU-001-la-regla-de-privacidad-de-la-memoria"
M = u"Memoria"
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
| **Planteamiento / Épica / HU** | [EP-006](../../epica.md) · [HU-001](../HU-001-que-se-guarda-tipos-y-alcances.md) |
| **Última actualización** | 2026-08-30 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ✅ Se buscó la regla que faltaba y se comprobó que no existía |
| 2 | Proponente · alcance | 👤 alcance aprobado | ✅ 2026-08-30 |
| 3 | Escritor de épica | 👤 épica aprobada | ✅ Ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ✅ Ya existía |
| 5 | Escritor de especificación | 👤 especificación aprobada | ✅ El usuario decidió que la regla se escriba, y dónde |
| 6 | Diseñador | diseño coherente | ✅ Va en `04`, no en `13` |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ✅ |
| 8 | Implementador | implementado + pruebas verdes | ✅ `validar.py metareglas` sin incumplimientos |
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
| **CA cumplidos** | 1 de 1, el transversal de privacidad |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | La mitad de la regla no es comprobable por programa, y queda declarado |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §2 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 · comprobar que la regla no existe | Terminada | `13·DOC5` no dice nada de datos personales ni claves |
| T-02 · escribir `04·S19` | Terminada | 303 caracteres de cuerpo, para un molde de 320 |
| T-03 · clasificarla en el registro de validables | Terminada | Mitad validable, mitad criterio humano, con el porqué |
| T-04 · versionar y declarar el veredicto | Terminada | `36.0.0`, MAYOR |

**Hechas:** 4 de 4. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  `13·DOC5`

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Un dato en la memoria no envejece: se vuelve a leer en cada sesión | El cuerpo de `04·S19` |
| La regla va en seguridad, no en documentación | §5 del cierre |

---

## 3. Pendiente / preguntas abiertas

- **La autorización del commit**, que se pide aparte.
- Apuntar `enmascarar.py` también a la memoria, que es la mitad comprobable.

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
| **Épica** | [EP-006](../../epica.md) |
| **HU** | [HU-001](../HU-001-que-se-guarda-tipos-y-alcances.md), **una sola** (`F12.1`) |
| **Módulo** | {M} |
| **Fecha apertura** | 2026-08-30 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- **Cierra el criterio transversal de privacidad**, que dejó la fase [`A`](../A-EP-006-HU-001-retrodocumentar-que-se-guarda-y-con-que-alcance/resultado_pruebas.md) en «No cumple» el 2026-08-17. Los dos criterios numerados quedaron verificados; lo que faltaba era que alguna regla dijera que en la memoria no van datos personales ni claves, y **no había ninguna**.

**Es un rojo de los que no se cierran midiendo.** Escribir una regla del estándar es fijar norma, y eso lo decide el usuario (`01·C4`). Estuvo trece días esperando esa decisión, que llegó el 2026-08-30.

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que exista la regla que el criterio pedía, por el procedimiento del capítulo `20`.

**Fuera de alcance:**

- **Construir la comprobación.** La mitad que un programa puede ver se declara y se enruta; no se construye acá.
- **Limpiar la memoria que ya existe.** Si hay algo que sacar, es trabajo aparte y se mide antes.
- Los otros criterios de la historia, que ya estaban en verde.

---

## 2. Análisis previo, línea base verificada  ·  `02·F17`

> Medida antes de crear la carpeta de esta fase.

### 2.0 La línea base

```
104 cumplen, 5 no cumplen, 5 sin veredicto
```

### 2.1 Que la regla no existía, comprobado

Se buscó en [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md), que es donde el criterio la esperaba: **cero menciones** de dato personal, credencial, clave o secreto. La regla dice qué se registra como señal; no dice qué no.

`00·N6` sí prohíbe escribir una credencial, en cualquier parte. Lo que no cubre el núcleo es **el dato personal**, y ese era el hueco.

### 2.1.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `base/04-seguridad.md` | Modificar | Estándar | La regla `S19`, al final del capítulo |
| `validadores/reglas-validables.md` | Modificar | Estándar | Su clasificación, con lo que sí y lo que no |
| `CHANGELOG.md` y `VERSION` | Modificar | Estándar | `36.0.0`, MAYOR |
| Los cinco documentos de esta fase | Crear | Documentación | — |
| `HU-001-que-se-guarda-tipos-y-alcances.md` | Modificar | Documentación | Su `Estado` y su tabla de fases |

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La regla va en `04`, seguridad | Ponerla en `13`, documentación | No es cómo se escribe un documento: es qué dato puede salir de una sesión y quedar guardado |
| No declara depender de `00·N6` | Escribir «extiende `N6`» | `20·M7` prohíbe extender una `[BLINDADA]`. La regla la nombra y no la toca |
| Se declara qué mitad **no** es comprobable | Clasificarla como validable a secas | El dato personal no se detecta sin decidir qué nombre propio es de una persona; prometerlo sería un veredicto falso |
| **MAYOR**, no menor | Versionarla como aditiva | Un proyecto al día tiene que revisar su memoria: eso es algo nuevo que hacer |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Comprobar que la regla no existe | Análisis | 0,25 h | — | EV-01 |
| T-02 | Escribir `04·S19` con su checklist | Estándar | 1 h | T-01 | EV-02 |
| T-03 | Clasificarla en el registro de validables | Estándar | 0,5 h | T-02 | EV-02 |
| T-04 | Versionar y declarar el veredicto | Documentación | 0,5 h | T-03 | EV-03 |

**Total estimado:** 2,25 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 a T-02 a T-03 a T-04

La `T-01` va primero porque si la regla existiera, esto no sería escribir sino enlazar.

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| Transversal · Privacidad | Que exista la regla, con su checklist aplicado y `validar.py metareglas` en verde | EV-02 | ☑ |

---

## 6. Datos y ambiente de prueba

Ninguno. La fase escribe norma; no toca datos ni memoria existente.

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit. La regla no se deroga: nunca llegó a regir.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**Obliga a migrar.** Un proyecto al día tiene que revisar su memoria y sacar lo que no debería estar. El aviso de desfase lo informa al abrir sesión; no migra solo.

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `20·M5`, el formato canónico de la regla, con una sola exigencia y su ejemplo.
- `20·M7`, nada extiende ni deroga una `[BLINDADA]`: por eso `S19` nombra a `N6` sin declarar dependencia.
- `20·M9`, se decide si es validable, y se dice qué mitad no lo es.
- `20·M10`, todo cambio de regla se versiona y se registra.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Declarar la regla validable entera | Prometería una comprobación que nadie puede escribir | `T-03` dice qué mitad no lo es | Cerrado |
| B-02 | Escribir «extiende `N6`» | `20·M7` lo prohíbe y la comprobación lo caza | La regla lo nombra sin declararlo | Cerrado |
| B-03 | Firmar el checklist sin aplicarlo | Es lo que le pasó a `S18` el 2026-08-27 | El cuerpo se midió antes de escribirlo: 303 de 320 | Cerrado |

---

## 11. Definition of Done

- [x] La regla escrita, con su checklist
- [x] Clasificada en el registro de validables
- [x] `validar.py metareglas` sin incumplimientos
- [x] `CHANGELOG.md` y `VERSION` al día
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

Comprobar que la regla que el criterio transversal de privacidad pedía **existe, está bien formada y está clasificada**.

### 1.2 Alcance

**Dentro:** que la regla no existiera antes, que cumpla el molde del capítulo `20`, y que quede dicho qué mitad de ella un programa no puede comprobar.

**Fuera:** construir esa comprobación, y limpiar la memoria que ya existe.

### 1.3 Documentos de referencia

- [HU-001](../HU-001-que-se-guarda-tipos-y-alcances.md)
- [Resultado de la fase A](../A-EP-006-HU-001-retrodocumentar-que-se-guarda-y-con-que-alcance/resultado_pruebas.md)
- El [checklist del estándar](../../../../../base/20-meta-reglas/checklist.md)

---

## 2. Elementos a probar

| Elemento | Por qué entra |
|---|---|
| Que la regla no existiera | Si existía, esto no era escribir sino enlazar |
| El molde de la regla nueva | Una regla mal formada no rige: la primera discusión es sobre su forma |
| Su clasificación | Una regla sin decir si es comprobable queda a la espera de un programa que nadie va a escribir |

---

## 3. Estrategia de pruebas

De ejecución sobre el propio estándar, en seco: `validar.py metareglas` comprueba el molde, el identificador, las dependencias y la clasificación.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- La decisión del usuario de que la regla se escriba, y dónde.

### 4.2 Criterios de salida

- `validar.py metareglas` sin incumplimientos.
- `validar.py versionado` sin fallas.
- El cuerpo de la regla dentro del molde, medido.

### 4.3 Criterios de suspensión y reanudación

Si el checklist diera ❌ en alguna fila, la regla se corrige antes de cerrar. Firmar el checklist sin aplicarlo es lo que le pasó a `04·S18`.

---

## 5. Matriz de trazabilidad

| CA | Caso |
|---|---|
| Transversal · Privacidad | CP-001, CP-002, CP-003 |

---

## 6. Casos de prueba

### CP-001 — La regla no existía

| Campo | Valor |
|---|---|
| **Tipo** | De análisis, ejecutado |
| **Cómo** | Buscar dato personal, credencial, clave y secreto en `13·DOC5` |
| **Resultado esperado** | Cero menciones |

### CP-002 — La regla nueva cumple su molde

| Campo | Valor |
|---|---|
| **Tipo** | De ejecución |
| **Prioridad** | **Crítica** |
| **Cómo** | `python validadores/validar.py metareglas` |
| **Resultado esperado** | Sin incumplimientos |

### CP-003 — El versionado queda consistente

| Campo | Valor |
|---|---|
| **Tipo** | De ejecución |
| **Cómo** | `python validadores/validar.py versionado` |
| **Resultado esperado** | Cero fallas |

---

## 7. Datos y ambientes de prueba

El propio repositorio. Ninguna prueba usa datos personales ni credenciales, que es lo que la regla prohíbe.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Filas del checklist en ❌ | **0** |
| Caracteres del cuerpo | 320 o menos |

---

## 15. Aprobación

Alcance y sitio de la regla aprobados por el usuario el 2026-08-30.
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

**Justificación:** la regla existe, cumple su molde y está clasificada diciendo qué mitad no es comprobable. El criterio transversal de privacidad pedía que la exigencia estuviera escrita, y ahora lo está.

| Métrica | Meta | Real |
|---|---|---|
| Filas del checklist en ❌ | 0 | **0** |
| Caracteres del cuerpo | 320 o menos | **303** |
| Incumplimientos de `metareglas` | 0 | **0** |

---

## 3. Resultado por caso

### CP-001 — La regla no existía

Buscando dato personal, credencial, clave y secreto en `13·DOC5`: **cero menciones**. La regla dice qué se registra como señal y no dice qué no.

**Resultado: pasa.**

### CP-002 — La regla nueva cumple su molde

```
== El estándar contra sus meta-reglas · . ==
OK: sin incumplimientos.
```

**Resultado: pasa.**

### CP-003 — El versionado queda consistente

```
0 falla(s), 1 aviso(s).
```

El único aviso es el de la `15.4.0` duplicada, reconocido en el registro desde el 2026-08-15.

**Resultado: pasa.**

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 El cuerpo se midió antes de escribirlo

303 caracteres para un molde de 320. **No es un detalle de forma:** a `04·S18` le pasó lo contrario el 2026-08-27, nació con 360 y su checklist declaraba «CUMPLE» en las veinte filas. Se firmó sin medirlo.

### 4.2 La regla no declara depender de `N6`

`20·M7` prohíbe que algo extienda o derogue una `[BLINDADA]`. `S19` **nombra** a `00·N6` para decir qué ya está cubierto, y no declara dependencia. La comprobación que lo caza es la misma que se construyó hoy para las reglas de proyecto.

### 4.3 Lo que la regla no promete

La clave sí se puede cazar con un programa; el dato personal no, sin decidir qué nombre propio es de una persona y cuál de un módulo. Queda escrito en el registro de validables, y no como una promesa a medias.

---

## 5. Defectos encontrados

**Ninguno.**

---

## 6. Evidencias

- [`base/04-seguridad.md`](../../../../../base/04-seguridad.md), regla `S19`
- [`validadores/reglas-validables.md`](../../../../../validadores/reglas-validables.md)
- `CHANGELOG.md` `36.0.0` y `VERSION`
""".format(F=F))

w("funcionalidad_implementada.md", u"""# Funcionalidad implementada — Fase `{F}` (módulo {M})   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `{F}` |
| **Módulo** | {M} |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-30 |
| **HU / CA cubiertas** | [HU-001](../HU-001-que-se-guarda-tipos-y-alcances.md): el transversal de privacidad |
| **Fecha de cierre** | 2026-08-30 |
| **Versión del estándar al cerrar** | `36.0.0` — **MAYOR**, y este cambio es el que la sube |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | Pendiente de autorización |
| **Reemplaza el veredicto de** | `A-EP-006-HU-001-retrodocumentar-que-se-guarda-y-con-que-alcance` |

> **Por qué se declara el reemplazo:** el criterio pedía una regla que no existía, y ahora existe. Aquel rojo era cierto el 2026-08-17 y siguió siéndolo trece días. **El veredicto de aquella fase no se toca** (`20·M11`).

---

## 1. Qué se implementó — resumen

**La regla [`04·S19`](../../../../../base/04-seguridad.md), que hasta hoy no existía.**

La fase `A` cerró en rojo porque el criterio transversal de privacidad pedía que la memoria no guardara datos personales ni claves, y al buscar la regla que lo dijera no había ninguna. `13·DOC5` dice qué se registra como señal, y no dice qué no.

| Antes | Ahora |
|---|---|
| Ninguna regla decía qué **no** puede entrar a la memoria | `04·S19` lo dice, y con su ejemplo |
| `00·N6` cubría la credencial, en cualquier parte | Sigue igual. `S19` agrega el dato personal, y nombra el sitio |

**Este es un rojo de los que no se cierran midiendo.** Escribir una regla es fijar norma, y eso lo decide el usuario (`01·C4`). Estuvo trece días esperando esa decisión.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| Transversal · Privacidad | norma | `base/04-seguridad.md`, `S19` | ✅ | CP-001, CP-002 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Estado | Evidencia |
|---|---|---|
| T-01 · comprobar que no existía | ✅ | Cero menciones en `13·DOC5` |
| T-02 · escribir la regla | ✅ | 303 caracteres de cuerpo |
| T-03 · clasificarla | ✅ | `reglas-validables.md` |
| T-04 · versionar y declarar | ✅ | `36.0.0` |

**Correspondencia:** 4 tareas, 4 con resultado.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, ciclo 1 |
| **Suites ejecutadas** | `validar.py metareglas` sin incumplimientos · `validar.py versionado` 0 fallas |
| **Defectos abiertos** | Ninguno |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

La regla se lee al abrir sesión, con el resto de `base/`. No agrega comando.

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué |
|---|---|
| Va en `04` y no en `13` | No es cómo se escribe un documento: es qué dato puede salir de una sesión y quedar guardado |
| Nombra a `00·N6` sin declarar dependencia | `20·M7` prohíbe extender una `[BLINDADA]` |
| **MAYOR** | Un proyecto al día tiene que revisar su memoria: eso es algo nuevo que hacer |
| Se declara qué mitad no es comprobable | El dato personal no se detecta sin decidir qué nombre propio es de una persona |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| `enmascarar.py` corre sobre la transcripción y no sobre la memoria | **Abierta y declarada** en el registro de validables. Es la mitad comprobable de `S19` |
| La memoria que ya existe no se revisó | **Abierta.** Se mide antes de tocar nada |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] El `Estado` de la historia y su tabla de fases.
- [x] `CHANGELOG.md` y `VERSION`, en `36.0.0`.
- [x] `validadores/reglas-validables.md`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**Obliga a migrar.** Un proyecto al día tiene que revisar su memoria y sacar lo que no debería estar. El aviso de desfase lo informa al abrir sesión; no migra solo.
""".format(F=F, M=M))

# La historia, al dia.
R = os.path.join(HU, "HU-001-que-se-guarda-tipos-y-alcances.md")
with io.open(R, encoding="utf-8") as f:
    t = f.read()
viejo = (u"| **Estado** | En curso \u2014 CA-01 y CA-02 cumplidos y probados; "
         u"el transversal de privacidad, no |")
nuevo = (u"| **Estado** | Terminada \u2014 CA-01 y CA-02 cumplidos, y el transversal "
         u"de privacidad quedó cubierto por la regla `04\u00b7S19`, escrita en la "
         u"fase `B` |")
if viejo in t:
    t = t.replace(viejo, nuevo, 1)
    print("estado al dia")
sep = u"| Fase | Qu\u00e9 CA cubre | Estado |\n|---|---|---|\n"
fila = (u"| [%s](%s/estado-fase.md) | El transversal de privacidad | "
        u"**Ejecutada el 2026-08-30.** Veredicto: "
        u"[**Cumple**](%s/resultado_pruebas.md#2-veredicto-de-la-fase) \u2014 se "
        u"escribi\u00f3 la regla `04\u00b7S19`, que no exist\u00eda, y el est\u00e1ndar sube a "
        u"`36.0.0`. Declara reemplazar el veredicto de la fase `A` |\n"
        % (F, F, F))
if sep in t:
    t = t.replace(sep, sep + fila, 1)
    print("fila puesta")
with io.open(R, "w", encoding="utf-8", newline="\n") as f:
    f.write(t)
print("fase escrita:", F)
