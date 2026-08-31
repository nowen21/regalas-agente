# -*- coding: utf-8 -*-
"""Escribe los dos documentos que le faltaban a la fase B de EP-004 HU-002.

La fase estaba detenida en la estacion 4 desde el 2026-08-17, con su plan y su
plan de pruebas escritos y sin aprobar. El usuario la aprobo el 2026-08-30.
"""
import io
import os

RAIZ = r"c:\Ing. Jose\ia\agente"
HU = os.path.join(RAIZ, "documentacion", "epicas", "EP-004-comprobacion-automatica",
                  "HU-002-marca-de-comprobable-en-cada-regla")
F = "B-EP-004-HU-002-el-analizador-ve-todas-las-reglas"
D = os.path.join(HU, F)


def w(nombre, texto):
    with io.open(os.path.join(D, nombre), "w", encoding="utf-8",
                 newline="\n") as f:
        f.write(texto)


w("resultado_pruebas.md", u"""# Resultado de Pruebas — Fase `%s`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `%s` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-30 |
| **Ciclo** | 1 |

**La fase estuvo detenida trece días en la estación 4**, con su plan escrito y sin aprobar. La aprobación llegó el 2026-08-30.

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** el analizador reconoce ahora las reglas escritas un nivel más abajo, y al verlas encontró lo que se buscaba: las cuatro del capítulo 16 nunca habían pasado su checklist. Se les aplicó, y el capítulo quedó dentro del molde.

| Métrica | Meta | Real |
|---|---|---|
| Reglas que el analizador ve | todas | **256**, eran 252 |
| Reglas del capítulo 16 visibles | 4 | **4** |
| Identificadores contados dos veces | 0 | **0** |
| Pruebas de la clase en verde | todas | **9 de 9** |
| Pruebas marcadas como fallo esperado | 0 | **0**, era 1 |

---

## 3. Resultado por caso

### CP-001 — El analizador ve las reglas escritas con `###`

Antes: `CQ1` a `CQ4` no aparecían en la lista de reglas. Después, las cuatro aparecen y el total pasa de 252 a 256.

**Resultado: pasa.**

### CP-002 — Y no cuenta como regla lo que solo la nombra

**Este es el caso que casi se pierde.** Al ensanchar el analizador sin más, `M19` empezó a contarse **dos veces**: una en su propio archivo, donde la regla vive, y otra en una sección del anexo de meta-reglas que solo la nombra. El programa reclamaba un identificador repetido que no existe.

Lo que separa una cosa de la otra es que el identificador es único: **un título de nivel bajo cuyo identificador ya se definió arriba es un eco, no una definición**. Y hay que mirarlo en una pasada previa sobre todo el árbol, porque en el orden de los archivos el eco se lee **antes** que la regla.

| Identificador | Veces contado |
|---|---|
| `M19` | 1 |
| `CQ1` a `CQ4` | 1 cada una |

**Resultado: pasa.**

### CP-003 — Lo que apareció al verlas

Las cuatro reglas nuevas a la vista traían, cada una, dos defectos que nadie había podido reclamar:

| Defecto | Cuántas |
|---|---|
| Escritas con `###` donde el molde pide `##` | 4 de 4 |
| Sin su bloque de checklist | 4 de 4 |
| Sin el ejemplo de lo incorrecto y lo correcto | 1 (`CQ3`) |

**No estaban mal clasificadas: no existían para el programa.** El capítulo salía en verde por el mismo motivo por el que pasaría un examen que no se corrige.

**Resultado: pasa**, y lo encontrado se corrigió en esta misma fase por decisión del usuario.

### CP-004 — La fila 18 detiene

Que toda regla diga si se puede comprobar con un programa pasó de avisar a detener. Con las 256 clasificadas, la corrida sigue en «sin incumplimientos».

**Resultado: pasa.**

### CP-005 — La derogada sigue exenta

Con más reglas a la vista y la fila 18 detenida, se comprueba que a una regla derogada no se le reclama nada: dejó de regir, y pedirle que declare si se comprueba sería pedirle cuentas a lo que ya no se aplica.

**Resultado: pasa.**

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Por qué el capítulo 16 se arregló acá y no en otra fase

El plan de esta fase no declaraba tocar `base/`: decía **listar** lo que apareciera, sin clasificarlo. Al aparecer, lo que había eran cuatro reglas fuera del molde, y dejarlas así habría dejado el cuerpo de reglas reclamando cuatro fallas sin dueño. **El usuario decidió el 2026-08-30 corregirlas en esta misma fase**, y por eso el archivo del capítulo entra en los archivos tocados.

### 4.2 Lo que se corrigió, y lo que no

Se corrigió la forma: el nivel del título, el ejemplo que le faltaba a una, y el bloque de checklist de las cuatro. **No se tocó lo que exigen**, que es lo que las haría cambiar de versión mayor.

---

## 5. Defectos encontrados

Los tres del `CP-003`, todos cerrados en esta fase.

---

## 6. Evidencias

- `validadores/metareglas.py`, la pasada previa que distingue la regla de su eco
- `base/16-cumplimiento-y-calidad.md`, con las cuatro reglas dentro del molde
- `validadores/pruebas.py`, clase `ClasificacionDeCadaRegla`: 9 pruebas, 9 en verde
- El guion que arregló el capítulo: `historico-chat/scripts/2026-08-30/arreglar-el-capitulo-16.py`
""" % (F, F))

w("funcionalidad_implementada.md", u"""# Funcionalidad implementada — Fase `%s` (módulo Comprobación automática)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `%s` |
| **Módulo** | Comprobación automática |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), escrito el 2026-08-17 y aprobado el 2026-08-30 |
| **HU / CA cubiertas** | [HU-002](../HU-002-marca-de-comprobable-en-cada-regla.md) |
| **Fecha de cierre** | 2026-08-30 |
| **Versión del estándar al cerrar** | `36.0.2` — **PARCHE**, y este cambio es el que la sube |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | Pendiente de autorización |
| **Reemplaza el veredicto de** | `A-EP-004-HU-002-retrodocumentar-la-clasificacion-de-cada-regla` |

> **Por qué se declara el reemplazo:** la fase `A` cerró en «No cumple» porque el analizador no veía todas las reglas. Ahora las ve. **El veredicto de aquella fase no se toca** (`20·M11`).

---

## 1. Qué se implementó — resumen

**Que el analizador vea todas las reglas, y que sepa distinguir la regla de su eco.**

| Antes | Ahora |
|---|---|
| 252 reglas visibles; las 4 del capítulo 16 no existían para el programa | 256, y el capítulo 16 dentro del molde |
| Un título de nivel bajo con forma de regla se ignoraba siempre | Se acepta si su identificador no está definido arriba |
| Que una regla declare si se comprueba era un aviso | Es una falla |

**Y lo que apareció al verlas**, corregido acá por decisión del usuario: las cuatro escritas con `###`, ninguna con su checklist, y una sin su ejemplo.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| El analizador ve todas las reglas | comprobación | `validadores/metareglas.py` | ✅ | CP-001, CP-002 |
| Toda regla declara si se comprueba | comprobación | `validadores/metareglas.py` | ✅ | CP-004, CP-005 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Estado | Evidencia |
|---|---|---|
| T-01 · reconocer las escritas con `###` | ✅ | CP-001 |
| T-02 · no confundirlas con su eco | ✅ | CP-002 |
| T-03 · destapar la prueba del analizador | ✅ | 9 de 9 en verde |
| T-04 · listar lo que apareciera | ✅ | CP-003 |
| T-05 · el subcomando en `validar.py` | ✅ | Ya existía al llegar acá |
| T-06 · la fila 18 pasa a falla | ✅ | CP-004 |
| T-07 · destapar la prueba de la regla sin clasificar | ✅ | Ya estaba destapada |
| T-08 · caso de las derogadas | ✅ | CP-005 |

**Correspondencia:** 8 tareas, 8 con resultado.

**Archivos tocados que el plan no declaraba** (`02·F8`): `base/16-cumplimiento-y-calidad.md`, `CHANGELOG.md` y `VERSION`. **Se declaran acá, y entraron por decisión expresa del usuario** al ver lo que la fase destapó.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, ciclo 1 |
| **Suites ejecutadas** | `pruebas.ClasificacionDeCadaRegla`: 9 pruebas, 9 en verde, 0 fallos esperados |
| **Defectos abiertos** | Ninguno |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

```
python validadores/validar.py metareglas
```

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué |
|---|---|
| El identificador separa la regla de su eco | `M4` lo exige único: el que ya se definió arriba no puede ser otra definición |
| La distinción se hace en una pasada previa | En el orden del árbol, el eco se lee antes que la regla |
| La fila 18 detiene ahora y no antes | Reclamar por algo que el programa no podía mirar entero es ruido que se aprende a ignorar |
| El capítulo 16 se corrigió en esta fase | Dejarlo habría dejado cuatro fallas sin dueño en el cuerpo de reglas |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| Ninguna | — |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] El `Estado` de la historia y su tabla de fases.
- [x] `CHANGELOG.md` y `VERSION`, en `36.0.2`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**Nada que desplegar.**
""" % (F, F))

print("dos documentos escritos")
