# -*- coding: utf-8 -*-
"""Escribe los cinco documentos de la fase B de EP-001 HU-006."""
import io
import os

RAIZ = r"c:\Ing. Jose\ia\agente"
F = "B-EP-001-HU-006-el-ajuste-que-afloja-el-nucleo-se-reprueba"
M = u"Programas de comprobación"
D = os.path.join(RAIZ, "documentacion", "epicas",
                 "EP-001-cuerpo-de-reglas-heredable",
                 "HU-006-capa-propia-del-proyecto", F)
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
| **Planteamiento / Épica / HU** | [EP-001](../../epica.md) · [HU-006](../HU-006-capa-propia-del-proyecto.md) |
| **Última actualización** | 2026-08-30 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ✅ Se leyó la fase `A` y su defecto `D-03` |
| 2 | Proponente · alcance | 👤 alcance aprobado | ✅ 2026-08-30 |
| 3 | Escritor de épica | 👤 épica aprobada | ✅ Ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ✅ Ya existía |
| 5 | Escritor de especificación | 👤 especificación aprobada | ✅ `02·F19`: la redacción del CA-03 |
| 6 | Diseñador | diseño coherente | ✅ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ✅ |
| 8 | Implementador | implementado + pruebas verdes | ✅ 2 pruebas nuevas, las dos en verde |
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
| **CA cumplidos** | 1 de 1, el CA-03 |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno nuevo. Siguen abiertos el `D-01` y el `D-02` de la fase `A`, que son de otro asunto |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §2 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 · provocar el caso en una carpeta temporal | Terminada | Cero hallazgos: el rojo era cierto y seguía siéndolo |
| T-02 · hacer que la comprobación lo vea | Terminada | `_afloja_una_blindada`, en `metareglas.py` |
| T-03 · probar el caso malo y el bueno | Terminada | 2 pruebas, las dos en verde |
| T-04 · declarar el veredicto que deja atrás | Terminada | §0 del cierre |

**Hechas:** 4 de 4. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  `13·DOC5`

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Una regla escrita y no aplicada donde importa es una regla que no rige | `S-061` |
| Se mira el verbo con que la regla declara su respaldo, no la intención | §5 del cierre |

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
| **Épica** | [EP-001](../../epica.md) |
| **HU** | [HU-006](../HU-006-capa-propia-del-proyecto.md), **una sola** (`F12.1`) |
| **Módulo** | {M} |
| **Fecha apertura** | 2026-08-30 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- **Cierra el CA-03, que quedó en rojo por no haberse podido ejecutar.** La fase [`A`](../A-EP-001-HU-006-retrodocumentar-la-capa-del-proyecto/resultado_pruebas.md) cerró el 2026-08-17 con una razón honesta en su defecto `D-03`: ningún proyecto real tenía un ajuste que contradijera el núcleo, y escribir uno en un proyecto real está prohibido por la decisión 35 del pendiente 59. Se comprobó por lectura, y por lectura no se comprueba nada.

**Lo que faltaba no era el caso: era dónde provocarlo.** La misma decisión 35 dice cómo: en una carpeta temporal, que es lo que hizo la fase `B` de `EP-002·HU-003` con una versión inventada.

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** provocar el caso y, si falla, hacer que la comprobación lo vea.

**Fuera de alcance:**

- Los defectos `D-01` y `D-02` de la fase `A`, que son de otro asunto.
- Detectar una contradicción que el proyecto **no declare**. Eso no se lee de un verbo.

---

## 2. Análisis previo, línea base verificada  ·  `02·F17`

> Medida antes de crear la carpeta de esta fase.

### 2.0 La línea base

```
101 cumplen, 8 no cumplen, 5 sin veredicto
```

### 2.1 Qué se provocó, y qué salió

Un proyecto de prueba en carpeta temporal, con este `.agente/reglas-proyecto.md`:

```
## P1 · El agente puede commitear sin pedir permiso
- **Respaldo:** afloja `N2`, que exige pedido explícito.

## P2 · Las credenciales de prueba se pueden dejar escritas
- **Respaldo:** deroga `N6`, que prohíbe escribir una credencial.
```

`validar_catalogo` devolvió **cero hallazgos**.

**Por qué pasaba.** La comprobación mira lo que pide `20·M16`: que haya respaldo y que el ID citado exista. `N2` y `N6` existen, así que el respaldo era válido. La prohibición vive en `20·M7`, y esa comprobación solo recorría las reglas del estándar, nunca las del proyecto. La regla estaba escrita y no se aplicaba donde importa.

### 2.1.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/metareglas.py` | Modificar | Comprobación | `_afloja_una_blindada` y su uso en `validar_catalogo` |
| `validadores/pruebas.py` | Modificar | Pruebas | Dos casos: el que afloja y el que endurece |
| Los cinco documentos de esta fase | Crear | Documentación | — |
| `HU-006-capa-propia-del-proyecto.md` | Modificar | Documentación | Su `Estado` y su tabla de fases |

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Se mira **el verbo del respaldo** | Interpretar si la regla contradice el núcleo | Interpretar la intención de un texto no es comprobar. El verbo es lo que la propia regla declara |
| Lista cerrada de verbos que aflojan | Reprobar toda mención de una regla del núcleo | Endurecer una `[BLINDADA]` es legítimo, y es para lo que existe la capa propia. Reprobarlo la volvería inútil |
| Se declara lo que **no** se promete | Callarlo | Un proyecto que contradiga el núcleo sin decirlo sigue sin detectarse, y el comentario del código lo dice |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Provocar el caso en una carpeta temporal | Calidad | 0,5 h | — | EV-01 |
| T-02 | Hacer que la comprobación lo vea | Comprobación | 1 h | T-01 | EV-02 |
| T-03 | Probar el caso malo y el bueno | Pruebas | 0,5 h | T-02 | EV-03 |
| T-04 | Declarar el veredicto que deja atrás | Documentación | 0,25 h | T-03 | EV-03 |

**Total estimado:** 2,25 h

**Sin cambio de versión:** no se toca `base/` ni `plantillas/`. Lo que cambia es un programa que hace cumplir una regla que ya existía.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 a T-02 a T-03 a T-04

La `T-01` va primero y no es trámite: si el caso hubiera pasado, no había nada que construir.

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| CA-03, el ajuste que contradice el núcleo no aplica | Provocarlo en carpeta temporal, con su contraprueba | EV-01, EV-03 | ☑ |

---

## 6. Datos y ambiente de prueba

Carpetas temporales que la propia prueba crea y borra. Ningún proyecto real se toca, que es justamente lo que impedía ejecutar este criterio.

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**Nada que desplegar.** El proyecto que ya tenga reglas propias las verá comprobadas la próxima vez que corra `validar.py metareglas --catalogo`.

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `20·M7`, nada extiende ni deroga una `[BLINDADA]`. Es la regla que esta fase hace cumplir.
- `20·M16`, toda regla del proyecto declara su respaldo.
- `04·R4`, se ejecuta en vez de afirmar sobre lo leído.
- `08·T5`, las pruebas corren y se reporta el número.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que la comprobación repruebe al que endurece | La capa propia quedaría inservible | `T-03` prueba el caso bueno | Cerrado |
| B-02 | Que se dé por cumplido sin provocar el caso | Es el defecto que dejó este CA en rojo | `T-01` | Cerrado |

---

## 11. Definition of Done

- [x] El caso, provocado
- [x] La comprobación, construida
- [x] Las dos pruebas, en verde
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

Comprobar el CA-03 de la HU-006: **un ajuste del proyecto que contradiga el núcleo no aplica.** El criterio quedó en rojo el 2026-08-17 sin haberse podido ejecutar.

### 1.2 Alcance

**Dentro:** una regla `P` que declara aflojar una `[BLINDADA]`, y una que declara endurecerla.

**Fuera:** la contradicción que el proyecto no declare, y los defectos `D-01` y `D-02` de la fase `A`.

### 1.3 Documentos de referencia

- [HU-006](../HU-006-capa-propia-del-proyecto.md)
- [Resultado de la fase A](../A-EP-001-HU-006-retrodocumentar-la-capa-del-proyecto/resultado_pruebas.md), defecto `D-03`
- `20·M7` y `20·M16`

---

## 2. Elementos a probar

| Elemento | Por qué entra |
|---|---|
| La regla `P` que afloja una `[BLINDADA]` | Es el caso que el CA-03 prohíbe |
| La regla `P` que endurece una `[BLINDADA]` | Es el caso que el CA-03 **permite**, y el que hace útil la capa propia |

---

## 3. Estrategia de pruebas

De ejecución, sobre carpetas temporales. La decisión 35 del pendiente 59 prohíbe provocarlo en un proyecto real, y es lo que dejó este criterio sin medir.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- La fase `A` y su defecto `D-03`, leídos.

### 4.2 Criterios de salida

- El catálogo que afloja produce **una falla que nombra la regla y la marca `[BLINDADA]`**.
- El catálogo que endurece produce **cero hallazgos**.

### 4.3 Criterios de suspensión y reanudación

Si el caso malo hubiera pasado sin reclamo desde el principio, no había nada que construir y la fase se habría cerrado declarando. Se provocó primero, y falló.

---

## 5. Matriz de trazabilidad

| CA | Caso |
|---|---|
| CA-03 | CP-001, CP-002 |

---

## 6. Casos de prueba

### CP-001 — La regla que afloja una blindada se reprueba

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-03 |
| **Tipo** | De ejecución |
| **Prioridad** | Alta |
| **Cómo** | Un `.agente/reglas-proyecto.md` temporal con `P1` cuyo respaldo dice «afloja `N2`» |
| **Resultado esperado** | Una falla que nombre `N2` y la marca `[BLINDADA]` |

### CP-002 — La regla que endurece una blindada pasa

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-03, contraprueba |
| **Tipo** | Que **no** pase |
| **Prioridad** | **Crítica** |
| **Cómo** | Un `P1` cuyo respaldo dice «concreta `N4`» |
| **Resultado esperado** | Cero hallazgos |

**La crítica es la segunda.** Una comprobación que reprobara cualquier mención de una regla del núcleo cazaría al tramposo y volvería inservible la capa propia, que existe para concretar.

---

## 7. Datos y ambientes de prueba

Carpetas temporales creadas y borradas por la propia prueba. Ninguna credencial, ni real ni inventada (`00·N6`).

---

## 8. Herramientas

`python -m unittest pruebas.ElAjusteDelProyectoNoAflojaElNucleo`

---

## 9. Gestión de defectos

Un fallo en CP-002 es más grave que uno en CP-001: significa que la comprobación rompe el uso legítimo.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Casos ejecutados | 2 de 2 |
| Casos comprobados leyendo en vez de corriendo | **0** |

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

**Justificación:** el CA-03 se ejecutó por primera vez. Falló, se construyó la comprobación que faltaba, y ahora el caso malo se reprueba y el bueno pasa. El rojo de la fase `A` era cierto el 2026-08-17 y siguió siéndolo hasta hoy: nadie lo había podido provocar.

| Métrica | Meta | Real |
|---|---|---|
| Casos ejecutados | 2 de 2 | 2 de 2 |
| Casos comprobados leyendo en vez de corriendo | 0 | **0** |
| Pruebas nuevas en verde | 2 | **2** |

---

## 3. Resultado por caso

### CP-001 — La regla que afloja una blindada se reprueba

**Antes de construir nada**, con el catálogo que declara «afloja `N2`» y «deroga `N6`»:

```
hallazgos: 0
```

**Después**, sobre el mismo catálogo:

```
[FALLA] .agente/reglas-proyecto.md:3 — `P1` declara que afloja `N2`, que está
        `[BLINDADA]` — M7 lo prohíbe: un ajuste del proyecto endurece el
        núcleo, nunca lo afloja
[FALLA] .agente/reglas-proyecto.md:9 — `P2` declara que deroga `N6`, que está
        `[BLINDADA]` — M7 lo prohíbe: un ajuste del proyecto endurece el
        núcleo, nunca lo afloja
```

**Resultado: pasa.**

### CP-002 — La regla que endurece una blindada pasa

Con un catálogo cuyo respaldo dice «concreta `N4`» y «concreta `C11`»:

```
hallazgos: 0
```

**Resultado: pasa.** Endurecer sigue siendo legítimo.

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Qué no promete esta comprobación

Se mira **el verbo con que la regla declara su respaldo**. Un proyecto que contradiga el núcleo sin decirlo sigue sin detectarse, y eso queda escrito en el comentario del código. Prometer más sería el defecto que esta casa llama veredicto falso: enseña a ignorar los veredictos.

### 4.2 El estándar contra sus propias meta-reglas

`validar.py metareglas` sigue en «OK: sin incumplimientos» después del cambio.

---

## 5. Defectos encontrados

**Ninguno nuevo.** El defecto era el que la fase venía a medir.

---

## 6. Evidencias

- `validadores/metareglas.py`, `_afloja_una_blindada` y su uso en `validar_catalogo`
- `validadores/pruebas.py`, clase `ElAjusteDelProyectoNoAflojaElNucleo`
- La corrida: `Ran 2 tests in 0.097s — OK`
""".format(F=F))

w("funcionalidad_implementada.md", u"""# Funcionalidad implementada — Fase `{F}` (módulo {M})   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `{F}` |
| **Módulo** | {M} |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-30 |
| **HU / CA cubiertas** | [HU-006](../HU-006-capa-propia-del-proyecto.md): el CA-03 |
| **Fecha de cierre** | 2026-08-30 |
| **Versión del estándar al cerrar** | `35.10.0`, **sin cambio**: no se toca `base/` ni `plantillas/` |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | Pendiente de autorización |
| **Reemplaza el veredicto de** | `A-EP-001-HU-006-retrodocumentar-la-capa-del-proyecto` |

> **Por qué se declara el reemplazo:** el CA-03 se ejecutó por primera vez, falló, se construyó lo que faltaba y ahora se cumple. Aquel rojo era cierto el 2026-08-17 y siguió siéndolo hasta hoy. **El veredicto de aquella fase no se toca** (`20·M11`).

---

## 1. Qué se implementó — resumen

**Que `validar_catalogo` vea lo que `20·M7` prohíbe.**

La fase `A` cerró en rojo con una razón honesta: el caso no se pudo provocar sin escribir en un proyecto real, y eso está prohibido. Provocado en una carpeta temporal, **falló**: un proyecto que declaraba «afloja `N2`» y «deroga `N6`» pasaba con cero hallazgos, porque la comprobación solo miraba lo que pide `20·M16` —que haya respaldo y que el ID exista— y esos dos IDs existen.

| Antes | Ahora |
|---|---|
| Un ajuste que declara aflojar el núcleo pasa sin reclamo | Falla, nombrando la regla y su marca `[BLINDADA]` |
| Un ajuste que endurece el núcleo pasa | Sigue pasando |

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| CA-03 | comprobación | `validadores/metareglas.py` | ✅ | CP-001, CP-002 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Estado | Evidencia |
|---|---|---|
| T-01 · provocar el caso | ✅ | «hallazgos: 0» antes de construir |
| T-02 · construir la comprobación | ✅ | `_afloja_una_blindada` |
| T-03 · probar los dos casos | ✅ | 2 pruebas en verde |
| T-04 · declarar el veredicto | ✅ | Este documento |

**Correspondencia:** 4 tareas, 4 con resultado.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, ciclo 1 |
| **Suites ejecutadas** | `pruebas.ElAjusteDelProyectoNoAflojaElNucleo`: 2 pruebas, 2 en verde. `validar.py metareglas`: sin incumplimientos |
| **Defectos abiertos** | Ninguno nuevo |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Sin punto de entrada nuevo. Corre dentro de lo que ya existía:

```
python validadores/validar.py metareglas --catalogo <ruta del proyecto>
```

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué |
|---|---|
| Se mira el **verbo del respaldo**, no la intención del texto | Interpretar intención no es comprobar |
| Lista cerrada de verbos que aflojan | Reprobar toda mención del núcleo volvería inservible la capa propia |
| Se dice lo que **no** se detecta | Un proyecto que contradiga el núcleo sin declararlo sigue sin verse. Prometer más sería un veredicto falso |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| La contradicción que el proyecto no declara sigue sin detectarse | **Abierta y declarada**, con su motivo |
| Los defectos `D-01` y `D-02` de la fase `A` | **Abiertos.** Son de otro asunto |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] El `Estado` de la historia y su tabla de fases.
- [ ] `VERSION` y `CHANGELOG.md`: **no aplica**, no se toca `base/` ni `plantillas/`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**Nada que desplegar.** Un proyecto con reglas propias verá la comprobación la próxima vez que la corra.
""".format(F=F, M=M))

print("cinco documentos escritos en %s" % F)
