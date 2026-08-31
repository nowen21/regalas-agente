# -*- coding: utf-8 -*-
"""Cierra la fase A de EP-004 HU-010, la ultima que estaba detenida."""
import io
import os

RAIZ = r"c:\Ing. Jose\ia\agente"
HU = os.path.join(RAIZ, "documentacion", "epicas", "EP-004-comprobacion-automatica",
                  "HU-010-convencion-declarada-por-el-proyecto")
F = "A-EP-004-HU-010-declaracion-y-comprobacion"
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

**Estuvo detenida trece días en la estación 7.** El usuario la aprobó el 2026-08-30.

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los cinco criterios se ejecutaron. Dos se verificaron contra proyectos reales y tres hubo que provocarlos, porque ningún proyecto real sirve para verlos. Y provocarlos encontró un defecto que llevaba meses reclamando de más en todos los proyectos.

| Métrica | Meta | Real |
|---|---|---|
| Criterios ejecutados | 5 de 5 | **5 de 5** |
| Criterios verificados leyendo en vez de corriendo | 0 | **0** |
| Contrapruebas | una por criterio provocado | **4 de 4** |
| Defectos encontrados | — | **1**, corregido acá |

---

## 3. Resultado por caso

### CA-01 — Sin declaración no se comprueba, y se dice qué quedó sin comprobar

**Verificado contra tres proyectos reales, cada uno en un estado distinto**, que es lo que hace útil el caso:

| Proyecto | Qué declara | Qué dice la comprobación |
|---|---|---|
| shopnest-mesa | La mayoría de las claves | Nombra las tres de inmutables que faltan, y qué regla queda sin comprobar por cada una |
| agro-system | Tiene el archivo, con las claves en blanco | Nombra cada clave sin declarar, con su regla |
| rni-back | No tiene los archivos | Dice que no existen y que sin ellos no hay contra qué comparar |

**Resultado: pasa.** En los tres casos dice **qué** se dejó de comprobar y **por qué**, en vez de callar o de reclamar.

### CA-02, CA-03 y CA-04 — Provocados, porque ningún proyecto real sirve

Los tres piden que se **reporte** un incumplimiento, y no hay dónde verlo: shopnest tiene las migraciones en un formato que el programa no lee, y agro-system no declara sus entidades. Provocarlo en un proyecto real está prohibido por la decisión 35 del pendiente 59, así que se armó uno temporal, con su declaración, sus migraciones y su repositorio.

**Cada uno con su contraprueba**: el mismo proyecto sin el defecto no debe reclamar nada. Sin eso, un validador que reclamara siempre pasaría igual.

| Criterio | Con el defecto | Sin el defecto |
|---|---|---|
| CA-02 · nombre fuera de la convención | `la columna clientes.nombreCompleto no sigue snake_case (EST2)` | Ningún reclamo |
| CA-03 · tabla de dominio sin auditoría | `la tabla facturas es de dominio y le faltan columnas de auditoría` | Ningún reclamo |
| CA-04 · inmutable sin estados ni permiso | `Factura es inmutable y no aparece ninguno de los estados declarados` | Ningún reclamo |

**Resultado: pasan los tres.**

### CA-05 — Un módulo del código sin declarar se reporta

Verificado en los dos lados. Sobre shopnest-mesa, que declara su convención de módulos, reporta **siete** carpetas que encajan con ella y no están en el dominio. Y provocado en el proyecto de prueba, reporta el módulo `cobros`, que existe en el código y no está declarado; sin él, ningún reclamo.

**Resultado: pasa.**

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 El defecto que apareció al provocar, y que leyendo no se veía

**El reclamo de que una entidad inmutable no tiene su permiso salía siempre, en todo proyecto.**

El patrón se declara como `anular_<recurso>` y la comprobación arma su expresión reemplazando el marcador **sobre el texto ya escapado**. Hasta Python 3.6, `re.escape` escapaba todo lo que no fuera alfanumérico, así que los ángulos salían escapados y el reemplazo encajaba. Desde 3.7 solo escapa lo que de verdad significa algo en una expresión, y los ángulos no.

**El reemplazo dejó de ocurrir en silencio.** La expresión quedaba literal, no encontraba ningún permiso, y toda entidad inmutable de todo proyecto recibía el reclamo. Un reclamo que sale siempre es el que se aprende a ignorar, y ese es el daño: no el falso positivo, sino lo que le enseña al que lo lee.

Se corrigió buscando lo mismo que se escapó, sin suponer cómo quedó escapado. Queda con su prueba de no regresión y su contraprueba.

### 4.2 Por qué las declaraciones del proyecto de prueba se escribieron dos veces

La primera versión declaró los estados por el **nombre de la columna** y el permiso **sin el marcador**. Las dos estaban mal, y el programa tenía razón en reclamar: los estados se buscan como valores entre comillas dentro del esquema, y el patrón del permiso necesita `<recurso>` para saber de qué entidad habla.

Vale dejarlo dicho porque es la trampa de este tipo de prueba: **un caso mal armado se lee igual que un programa roto**. Lo que los separa es mirar qué espera el programa antes de acusarlo.

### 4.3 El proyecto de prueba tiene que ser un repositorio

Las comprobaciones solo miran archivos versionados, y es a propósito: lo que no está guardado todavía no es del proyecto. La primera corrida no encontró ni una migración, y el resultado se leía como si todo estuviera bien.

---

## 5. Defectos encontrados

| ID | Severidad | Qué es | Estado |
|---|---|---|---|
| D-01 | **Alta** | El patrón del permiso no reemplazaba su marcador: el reclamo de `15·IM5` salía en todo proyecto con una entidad inmutable | **Cerrado** en esta fase, con prueba |

---

## 6. Evidencias

- El guion que provoca los cuatro casos con sus contrapruebas: `historico-chat/scripts/2026-08-30/provocar-los-ca-de-hu010.py`
- `validadores/entidades.py`, `recursos_con_permiso`
- `validadores/tests/test_las_entidades_no_acusan_a_ciegas.py`: 7 pruebas, 7 en verde
- Las corridas contra shopnest-mesa, agro-system y rni-back
""" % (F, F))

w("funcionalidad_implementada.md", u"""# Funcionalidad implementada — Fase `%s` (módulo Comprobación automática)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `%s` |
| **Módulo** | Comprobación automática |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), escrito el 2026-08-17 y aprobado el 2026-08-30 |
| **HU / CA cubiertas** | [HU-010](../HU-010-convencion-declarada-por-el-proyecto.md): los cinco |
| **Fecha de cierre** | 2026-08-30 |
| **Versión del estándar al cerrar** | `36.0.2` — **sin cambio**: no se toca `base/` ni `plantillas/` |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | Pendiente de autorización |

---

## 1. Qué se implementó — resumen

**Lo que el proyecto declara es lo que se le comprueba, y lo que no declara se dice.**

Los programas ya estaban escritos cuando llegó la aprobación. Lo que faltaba era **ejecutar los cinco criterios**, y ahí apareció lo que importa.

| Antes | Ahora |
|---|---|
| Los cinco criterios, sin ejecutar | Los cinco ejecutados, tres provocados con su contraprueba |
| El reclamo de que un inmutable no tiene permiso salía **siempre** | Sale solo cuando el permiso de verdad falta |

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| CA | Cómo se verificó | Estado |
|---|---|---|
| CA-01 | Contra tres proyectos reales, en tres estados distintos | ✅ |
| CA-02 | Provocado, con contraprueba | ✅ |
| CA-03 | Provocado, con contraprueba | ✅ |
| CA-04 | Provocado, con contraprueba, y encontró el defecto | ✅ |
| CA-05 | Contra un proyecto real y provocado | ✅ |

### 2.2 Plan de trabajo → ejecución

Las tareas del plan que construían los programas ya estaban hechas al llegar la
aprobación. Lo que esta fase ejecutó es la verificación de los cinco criterios,
y la corrección del defecto que encontró.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno. `entidades.py`
estaba declarado en el §2.1 del plan.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, ciclo 1 |
| **Suites ejecutadas** | `test_las_entidades_no_acusan_a_ciegas.py`: 7 pruebas, 7 en verde |
| **Defectos abiertos** | Ninguno |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

```
python validadores/validar.py estructura --raiz <proyecto>
python validadores/validar.py entidades  --raiz <proyecto>
python validadores/validar.py esquema    --raiz <proyecto>
```

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué |
|---|---|
| Tres criterios se provocan en un proyecto temporal | Ningún proyecto real sirve para verlos, y provocarlos en uno real está prohibido |
| Cada provocación lleva su contraprueba | Un validador que reclamara siempre pasaría igual |
| El marcador se reemplaza sobre lo escapado, buscando lo mismo que se escapó | No suponer cómo quedó escapado: eso fue lo que se rompió al cambiar de versión de Python |
| El proyecto de prueba es un repositorio con sus archivos guardados | Las comprobaciones solo miran lo versionado, y sin eso no encuentran nada |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| Ningún proyecto real tiene migraciones legibles **y** entidades declaradas a la vez | **Abierta y declarada.** Por eso tres criterios se provocan; el día que haya uno, se verifican también ahí |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] El `Estado` de la historia y su tabla de fases.
- [ ] `VERSION` y `CHANGELOG.md`: **no aplica**.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**Nada que desplegar.** El proyecto que corra las comprobaciones deja de recibir
el reclamo falso del permiso.
""" % (F, F))

# El estado de la fase.
R = os.path.join(D, "estado-fase.md")
with io.open(R, encoding="utf-8") as f:
    t = f.read()
v = u"**Estación actual:** 7 — Task Planner. **Última puerta pasada:** 4."
n = (u"**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.\n\n"
     u"**Estuvo detenida trece días en la estación 7.** El usuario la aprobó el "
     u"2026-08-30 y la fase se ejecutó ese mismo día: los programas ya estaban "
     u"escritos, y lo que faltaba era ejecutar los cinco criterios.")
if v in t:
    t = t.replace(v, n, 1)
    print("estado-fase al dia")
with io.open(R, "w", encoding="utf-8", newline="\n") as f:
    f.write(t)

# La historia.
R = os.path.join(HU, "HU-010-convencion-declarada-por-el-proyecto.md")
with io.open(R, encoding="utf-8") as f:
    t = f.read()
import re
t = re.sub(r"\| \*\*Estado\*\* \| [^|]*\|",
           u"| **Estado** | Terminada — los cinco criterios ejecutados en la "
           u"fase `A`, tres de ellos provocados con su contraprueba |", t, count=1)
sep = u"| Fase | Qué CA cubre | Estado |\n|---|---|---|\n"
fila = (u"| [%s](%s/estado-fase.md) | CA-01 a CA-05 | **Ejecutada el 2026-08-30.** "
        u"Veredicto: [**Cumple**](%s/resultado_pruebas.md#2-veredicto-de-la-fase) "
        u"— y encontró que el reclamo del permiso de anular salía en todo "
        u"proyecto |\n" % (F, F, F))
if sep in t:
    t = t.replace(sep, sep + fila, 1)
    print("fila puesta")
with io.open(R, "w", encoding="utf-8", newline="\n") as f:
    f.write(t)
print("fase cerrada:", F)
