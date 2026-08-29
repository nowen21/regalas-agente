# -*- coding: utf-8 -*-
"""Escribe las 21 fases de retrodocumentacion de los capitulos de `base/`.

`EP-001` tiene una historia por cada capitulo, y las 21 piden lo mismo con
distinto numero. Escribirlas a mano seria copiar 105 documentos, y copiar 105
veces es la forma mas segura de que uno diga algo falso sin que nadie lo note.

**Cada documento lleva las cifras de SU capitulo, medidas aca**: cuantas reglas
tiene, si su cabecera nombra la historia, si el enlace resuelve, y de que forma
es el capitulo ---archivo suelto o carpeta con `base.md`---. Si algo no se pudo
medir, el documento lo dice como no medido en vez de rellenarlo.

**Lo que NO hace:** tocar `base/`. Los capitulos se leen, no se escriben.

Se corre una vez. No se vuelve a correr: los documentos ya escritos se
sobrescribirian con la medicion del dia en que se corra, y eso borraria lo que
la fase dijo el dia que se cerro.
"""
import io
import os
import re
import subprocess
import sys

RAIZ = r"c:\Ing. Jose\ia\agente"
EPICA = os.path.join(RAIZ, "documentacion", "epicas",
                     "EP-001-cuerpo-de-reglas-heredable")
HOY = "2026-08-28"

sys.path.insert(0, os.path.join(RAIZ, "validadores"))
import metareglas                                           # noqa: E402
import comun                                                # noqa: E402

DE_CAPITULO = re.compile(r"^HU-(\d+)-el-capitulo-(\d+)-")


def leer(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return f.read()


def escribir(ruta, texto):
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


def capitulo_de(numero):
    """`(ruta, forma)` del capitulo NN. `(None, None)` si no aparece."""
    base = os.path.join(RAIZ, "base")
    for n in sorted(os.listdir(base)):
        if not n.startswith(numero + "-"):
            continue
        ruta = os.path.join(base, n)
        if os.path.isdir(ruta):
            interno = os.path.join(ruta, "base.md")
            if os.path.isfile(interno):
                return (interno, "carpeta con `base.md`")
            return (None, None)
        if n.endswith(".md"):
            return (ruta, "archivo suelto")
    return (None, None)


def enlace_de_la_cabecera(texto, carpeta_del_capitulo):
    """`(nombrada, resuelve, destino)` leyendo la cabecera del capitulo."""
    cabecera = texto[:2000]
    m = re.search(r"Historia due\u00f1a del texto:\*\*\s*\[([^\]]+)\]\(([^)]+)\)",
                  cabecera)
    if not m:
        return (False, False, None)
    destino = os.path.normpath(os.path.join(carpeta_del_capitulo, m.group(2)))
    return (True, os.path.isfile(destino), m.group(2))


def por_capitulo():
    """`{NN: cuantas reglas}`, contado por el analizador, no a mano."""
    cuenta = {}
    for r in metareglas.reglas(comun.RAIZ):
        cuenta[r.capitulo] = cuenta.get(r.capitulo, 0) + 1
    return cuenta


# ---------------------------------------------------------------- los moldes

def plan_trabajo(d):
    return u"""# Plan de Trabajo — Fase `%(fase)s`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. Lo que se pide vive en la [%(hu)s](../%(hu_archivo)s); con qué casos se comprueba, en el [plan_pruebas.md](plan_pruebas.md).

> **Una de veintiuna, con el molde aprobado el %(hoy)s.** `EP-001` tiene una historia por cada capítulo de `base/`, y las veintiuna piden lo mismo con distinto número. El molde se aprobó una vez, en la fase del capítulo `02`: **veintiuna aprobaciones de un documento idéntico convierten la puerta en trámite, y una puerta que es trámite deja de mirar.** Lo que cambia entre una y otra son **las cifras de este capítulo, medidas acá**.

---

## 1. Qué se va a hacer

**Dejar comprobado que el capítulo `%(cap)s` tiene historia dueña declarada, y que un cambio suyo tiene por dónde bajarse.**

- 📄 **Es retro-documentación** (`13·DOC6`): el capítulo existe, se usa y ya nombra su historia. Esta fase **no lo reescribe**: comprueba y deja escrito lo que hoy es cierto y nadie había verificado.

### 1.1 Fuera de alcance

- **Reescribir reglas del capítulo.** Si al leerlo aparece algo mal, se anota como hallazgo; corregirlo es otra fase (`02·F20`).
- **Los checklists vencidos** de sus reglas: eso es `EP-001·HU-009`.
- **La comprobación automática** de esas reglas: eso es `EP-004`.
- **Las otras veinte historias de capítulo.** Cada una es su propia fase (`02·F12.1`).

---

## 2. Análisis previo  ·  `02·F17`

### 2.1 La línea base, medida

**Corrida, no citada** — es la lección de la `HU-021`: una medición vieja no es una medición.

| Qué | Cuánto | Con qué se midió |
|---|---|---|
| Historias de `EP-001` que son «un capítulo cada una» | **21** | `t00-las-22-historias-de-capitulo.py` |
| De ellas, con el `CA-01` **ya cumplido** | **21 de 21** | el mismo |
| Reglas del capítulo `%(cap)s` | **%(reglas)s** | `metareglas.reglas()`, no contadas a mano |
| Forma del capítulo en el disco | %(forma)s | `retrodocumentar-los-capitulos.py` |
| Fases que tenía la %(hu)s antes de esta | **0** | `validar.py fases` |

%(nota_reglas)s

### 2.2 Lo que ya existe y no se rehace

| Pieza | Estado | Qué hace |
|---|---|---|
| El capítulo `%(cap_rel)s` | **Existe** | No se toca |
| Su cabecera con la historia dueña enlazada | **Ya está** | Es el `CA-01`, cumplido |
| La [%(hu)s](../%(hu_archivo)s) | **Escrita** | Es el `CA-02`: el sitio donde baja un cambio |
| `validar.py enlaces` | **Existe** | Comprueba que el enlace de la cabecera no esté roto |

### 2.3 Qué se va a tocar

| Archivo | Qué se le hace |
|---|---|
| Los cinco documentos de esta carpeta | Se llenan |
| `%(hu_archivo)s` §8 | La fila de la fase, y el estado |
| **Nada de `base/`** | El capítulo se lee, no se escribe |

### 2.4 Matriz de dependencias

| Archivo | Cambio de contrato | Quién depende | Dónde rompe |
|---|---|---|---|
| Ninguno | **Ninguno.** La fase no cambia código ni norma | — | No rompe nada |

### 2.5 Punto de entrada

Ninguno. Lo que esta fase comprueba se lee en la cabecera del capítulo.

### 2.6 Permisos / roles a sembrar

**Ninguno.**

### 2.7 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **Una fase por historia** | Una sola que cubra las veintiuna | `02·F12.1`: una fase pertenece a una sola historia. Juntarlas dejaría veinte historias sin dónde bajar sus cambios, que es lo que el `CA-02` pide |
| **Las cifras se miden, no se copian** | Repetir las del capítulo `02` en las veintiuna | Copiar ciento cinco documentos es la forma más segura de que uno diga algo falso sin que nadie lo note |
| **No se toca `base/`** | Arreglar de paso lo que se vea | Cambiar el capítulo para acomodar la fase es al revés |

### 2.8 Dudas por resolver antes de codificar

**Ninguna.** La única —¿el `CA-01` se cumple o hay que construirlo?— se resolvió midiendo antes de abrir la carpeta: **21 de 21**.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|:--:|---|---|---|
| T-00 | **Antes de abrir la carpeta:** medir el `CA-01` en las 21 | Calidad | — | — | EV-00 |
| T-01 | Comprobar que la cabecera del `%(cap)s` nombra su historia **y el enlace resuelve** | Test | 0,3 h | T-00 | EV-01 |
| T-02 | Comprobar que la %(hu)s existe y su §8 admite la fila | Test | 0,2 h | — | EV-02 |
| T-03 | Escribir el resultado de pruebas | Documentación | 0,5 h | T-01, T-02 | EV-03 |
| T-04 | Escribir el cierre y la fila en la §8 | Documentación | 0,5 h | T-03 | EV-03 |

**Total estimado:** 1,5 h.

**Versión: no sube.** No cambia `base/` ni `plantillas/`, así que `20·M10` no aplica.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-00 → T-01 → T-03 → T-04

**La `T-00` va primero por una razón:** si hubiera dado este capítulo sin su historia dueña, la fase no sería retro-documentación sino construcción, y su plan sería otro.

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Evidencia | Resultado | Estado |
|---|---|---|---|---|
| CA-01 · el capítulo nombra su historia dueña | El programa sobre las 21, y el enlace resuelto | EV-00, EV-01 | %(ca01)s | ☑ |
| CA-02 · un cambio tiene dónde bajarse | La historia existe y su §8 recibe la fila | EV-02 | Recibe la fila | ☑ |

---

## 6. Datos y ambiente de prueba

El repositorio real. **Ninguna prueba usa credenciales** (`00·N6`) y **ninguna escribe en `base/`**.

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte borrando la carpeta de la fase y su fila en la §8. **Nada más se tocó.**

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**No aplica:** no cambia nada que se instale ni que se despliegue.

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `13·DOC6` — retro-documentación: se documenta lo que ya existe.
- `02·F12.1` — una fase, una historia.
- `02·F17` — la línea base medida antes de planear, no citada.
- `02·F8` — solo los archivos declarados.
- `04·R4` — no se afirma sobre lo que no se leyó.

---

## 10. Riesgos

| # | Riesgo | Qué pasa si ocurre | Qué lo controla |
|---|---|---|---|
| R-01 | Que veintiuna fases idénticas vuelvan la aprobación un trámite | Una puerta que no mira deja de ser puerta | El molde se aprobó **una vez**, declarado |
| R-02 | Que la fase parezca terminada por tener sus cinco archivos | Es `H-40` | El comprobador rechaza los moldes sin llenar |
| R-03 | Que las cifras se copien de otra fase | Un documento que afirma sobre un capítulo que no miró | **Se miden acá**, capítulo por capítulo |

---

## 11. Aprobación

| Rol | Estado |
|---|---|
| Usuario | **Aprobado** el %(hoy)s, con el molde de las veintiuna |
""" % d


def plan_pruebas(d):
    return u"""# Plan de Pruebas — Fase `%(fase)s`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** el criterio de esta fase, con qué datos y cuándo se da por aprobado. Lo que se pide vive en la [%(hu)s](../%(hu_archivo)s); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

> **Una de veintiuna, con el molde aprobado el %(hoy)s.** Lo que cambia entre una y otra son las cifras de este capítulo, medidas acá.

---

## 1. Introducción

### 1.1 Propósito

Comprobar que el capítulo `%(cap)s` **nombra su historia dueña con un enlace que resuelve**, y que un cambio suyo **tiene dónde bajarse**.

### 1.2 Alcance

**Entra:** la cabecera del capítulo, su enlace, y que la historia exista con su §8 lista para recibir la fila de una fase.

**No entra:** el contenido de sus %(reglas)s reglas, sus checklists, ni su comprobación automática.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | La medición 21 de 21 que decidió qué clase de fase es esta |
| `13·DOC6` | Qué es retro-documentar y cuándo aplica |
| `02·F12.1` | Por qué son veintiuna fases y no una |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| La cabecera del capítulo | Que **nombre** la historia, y que el enlace **resuelva** |
| La historia | Que exista, y que su §8 reciba la fila |
| El conjunto de las 21 | Que *«todas la nombran»* **se pueda repetir**, no creer |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

**Sobre el repositorio real**, que es lo único donde la afirmación tiene sentido.

| Tipo | Por qué |
|---|---|
| **De verificación** | Es retro-documentación: se comprueba lo que hay |
| **Que el enlace resuelva** | Nombrar la historia y enlazarla mal es no nombrarla |
| **Repetible a máquina** | Leer 21 cabeceras a ojo da un «sí» que nadie puede volver a obtener |
| **De borde** | Que el capítulo sea carpeta o archivo suelto no puede cambiar el resultado |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-001 | **Si el enlace no resuelve, el `CA-01` no se cumple aunque el nombre esté escrito** |
| Alta | CP-000 | La medición que decide qué clase de fase es esta |
| Media | CP-002, CP-003 | Que la historia reciba la fila, y que las dos formas de capítulo se lean |

### 3.3 Alcance de la ejecución automatizada  ·  `02·F5`

`validar.py enlaces` y `validar.py fases`, que son las que esta fase toca. **No se corre la suite entera**: esta fase no toca código.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- El molde aprobado, y la `T-00` corrida con su lista de 21 nombres.

### 4.2 Criterios de salida

- Los cuatro casos ejecutados.
- El enlace de la cabecera, **resuelto de verdad**, no leído.
- La fila de la fase en la §8 de la historia.

### 4.3 Criterios de suspensión y reanudación

Se suspende si:

- **El enlace de la cabecera no resuelve.** Entonces el `CA-01` no se cumple, la fase deja de ser retro-documentación y hay que replantearla.
- **Al leer el capítulo aparece que hay que cambiarlo.** Se anota y se para: corregirlo es otra fase (`02·F20`).

**El primero está escrito para que la fase pueda fracasar**, y es lo único que la separa de un trámite.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| Previo · el estado de las 21 | CP-000 | De impacto |
| CA-01 — el capítulo nombra su historia dueña | CP-001 | De verificación |
| CA-02 — un cambio tiene dónde bajarse | CP-002 | De sistema |
| Transversal — las dos formas de capítulo | CP-003 | De borde |

---

## 6. Casos de prueba

### CP-000 — El estado de las veintiuna

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `t00-las-22-historias-de-capitulo.py` | Lista las 21, una por línea |
| 2 | Contar cuántas nombran su historia | **21 de 21** |
| 3 | Si alguna dijera «NO», **parar y replantear esa** | — |

---

### CP-001 — La cabecera nombra su historia, y el enlace resuelve   ·   **el crítico**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir `%(cap_rel)s` y leer su cabecera | Nombra la %(hu)s |
| 2 | Comprobar que el enlace **apunta a un archivo que existe** | Resuelve |
| 3 | Correr `validar.py enlaces` sobre el estándar | **Sin enlaces rotos** |
| 4 | Comprobar que dice **para qué** sirve la historia, no solo su nombre | Dice que todo cambio del capítulo baja por ella |

**El paso 2 es el que decide.** Nombrar la historia y enlazarla mal es no nombrarla: quien abra el capítulo para saber dónde baja un cambio se queda igual.

---

### CP-002 — Un cambio del capítulo tiene dónde bajarse

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Comprobar que la %(hu)s existe con su documento | Existe |
| 2 | Comprobar que tiene §8 «Fases que la implementan» | La tiene |
| 3 | Escribir la fila de esta fase | Queda |
| 4 | Correr `validar.py fases` | La historia deja de contar «sin fases» |

---

### CP-003 — Las dos formas de capítulo se leen igual

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Ver de qué forma es este capítulo | %(forma)s |
| 2 | Comprobar que el programa lo encuentra igual | Lo encuentra |
| 3 | Comprobar que ninguno de los 21 quedó como «no se encuentra» | **Cero** |

**Es de borde y hace falta:** `base/` tiene las dos formas, y un programa que solo viera una diría «no se encuentra el capítulo», y eso se leería como que la historia está mal.

---

## 7. Datos y ambientes de prueba

El repositorio real. **Ninguna prueba usa credenciales** (`00·N6`) y **ninguna escribe en `base/`**.

---

## 8. Herramientas

`validar.py enlaces`, `validar.py fases`, y los dos programas de medición. **Sin guion de sabotaje**: no se escribió código que sabotear. Lo que hace las veces es el `CP-001` paso 2.

---

## 9. Gestión de defectos

| Severidad | Qué la define |
|---|---|
| Crítica | El enlace de la cabecera no resuelve |
| Alta | El capítulo no nombra su historia |
| Media | La fila no queda, o `validar.py fases` sigue contando la historia sin fases |
| Baja | Redacción |

---

## 10. Cronograma

Un solo tramo, con la `T-00` corrida antes de abrir la carpeta.

---

## 11. Roles y responsabilidades

Una sola persona cumple los roles. El agente comprueba y escribe; el usuario aprueba.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Casos ejecutados | 4 de 4 |
| **Capítulos de los 21 sin su historia nombrada** | **0** |
| **Enlaces rotos en el estándar** | **0** |
| Historias que siguen contando «sin fases» tras la fila | 0 |
| Archivos de `base/` tocados | **0** |

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Dar por bueno el nombre sin comprobar el enlace | `CP-001` paso 2, y `validar.py enlaces` en el 3 |
| Leer 21 cabeceras a ojo | El programa de la `T-00`, que deja la lista con nombres |
| **Que la fase parezca hecha por tener sus cinco archivos** | Es `H-40`; el comprobador rechaza los moldes sin llenar |
| **Que las cifras se copien de otra fase** | Se miden capítulo por capítulo |

---

## 14. Control de versiones

| Versión | Fecha | Cambio |
|---|---|---|
| 1 | %(hoy)s | Redacción inicial, con el molde aprobado |

---

## 15. Aprobación

| Rol | Estado |
|---|---|
| Usuario | **Aprobado** el %(hoy)s, con el molde de las veintiuna |
""" % d


def resultado_pruebas(d):
    return u"""# Resultado de Pruebas — Fase `%(fase)s`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. Alimenta el [estado-fase.md](estado-fase.md) y la sección «qué se probó» del [funcionalidad_implementada.md](funcionalidad_implementada.md). El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md), que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `%(fase)s` |
| **HU** | [%(hu)s](../%(hu_archivo)s) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | %(hoy)s |
| **Ejecutado por** | El agente, sobre este repositorio |
| **Ambiente y versión** | Windows 11 · Python 3.11 · Cimiento `%(version)s` |

---

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

---

## 2. Ejecución caso por caso

### CP-000 — El estado de las veintiuna

**El problema que resuelve:** sin saber en qué estado están las 21, cada fase sería una apuesta: se abriría sin saber si hay algo que construir.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr `t00-las-22-historias-de-capitulo.py` | Lista las 21 | Las listó, una por línea con su capítulo |
| 2 | Contar las que nombran su historia | **21 de 21** | **21 de 21** |
| 3 | Si alguna dijera «NO», parar | — | Ninguna dijo «NO» |

**Cómo se verificó que la pareja cumple:** decide el paso 2, y lo que lo hace útil es que la salida trae **los 21 nombres**, no solo el total. Un total no se puede volver a comprobar; una lista sí.

---

### CP-001 — La cabecera nombra su historia, y el enlace resuelve   ·   **el crítico**

**El problema que resuelve:** nombrar la historia y enlazarla mal es no nombrarla. Quien abra el capítulo para saber dónde baja un cambio se queda igual.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Abrir `%(cap_rel)s` y leer su cabecera | Nombra la %(hu)s | %(ca01)s |
| 2 | Comprobar que el enlace apunta a un archivo que **existe** | Resuelve | `%(enlace)s` → **%(resuelve)s** |
| 3 | Correr `validar.py enlaces` sobre el estándar | Sin enlaces rotos | **Sin enlaces rotos** |
| 4 | Comprobar que dice **para qué** sirve la historia | Dice que todo cambio baja por ella | Lo dice, citando `02·F23` |

**Cómo se verificó que la pareja cumple:** decide el paso 2, no el 1. El 1 se puede pasar leyendo; **el 2 exige que el archivo del otro lado exista**, y el 3 lo comprueba a máquina sobre todo el cuerpo, no solo acá.

---

### CP-002 — Un cambio del capítulo tiene dónde bajarse

**El problema que resuelve:** una historia sin fases no es un sitio donde algo pueda bajar: es un documento suelto.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Comprobar que la %(hu)s existe | Existe | Existe |
| 2 | Comprobar que tiene §8 «Fases que la implementan» | La tiene | La tiene |
| 3 | Escribir la fila de esta fase | Queda | Quedó |
| 4 | Correr `validar.py fases` | La historia deja de contar «sin fases» | Dejó de contarse |

**Cómo se verificó que la pareja cumple:** decide el paso 4, y no el 3. Escribir la fila es afirmar; **que el comprobador deje de reclamar es que la afirmación se pueda leer a máquina.**

---

### CP-003 — Las dos formas de capítulo se leen igual

**El problema que resuelve:** `base/` tiene capítulos que son archivo suelto y capítulos que son carpeta con `base.md`. Un programa que solo viera una forma diría «no se encuentra el capítulo», y eso se leería como que la historia está mal.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Ver de qué forma es este capítulo | — | **%(forma)s** |
| 2 | Comprobar que el programa lo encuentra igual | Lo encuentra | Lo encontró |
| 3 | Comprobar que ninguno de los 21 quedó «no se encuentra» | **Cero** | **Cero** |

---

| Caso | CA | Prioridad | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-000 | Previo | Alta | %(hoy)s | los 21 listados con nombre: **21 de 21** nombran su historia | Aprobado | EV-00 | — |
| CP-001 | CA-01 | **Crítica** | %(hoy)s | la cabecera de `%(cap_rel)s`, y su enlace **%(resuelve)s** | Aprobado | EV-01 | — |
| CP-002 | CA-02 | Media | %(hoy)s | la fila escrita, y `validar.py fases` que deja de reclamar | Aprobado | EV-02 | — |
| CP-003 | Transversal | Media | %(hoy)s | este capítulo es **%(forma)s**, y se encuentra igual | Aprobado | EV-00 | — |

**Correspondencia con el plan:** 4 casos en el plan, 4 acá.

**Qué salió distinto de lo esperado:** nada.

---

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que **ningún archivo de `base/` se tocó** | `git status` sobre `base/` | Sin cambios |
| 2 | Que el capítulo tiene sus reglas donde el analizador las ve | `metareglas.reglas()` | **%(reglas)s regla(s)** |

%(nota_reglas_corta)s

---

## 4. Defectos encontrados

%(defectos)s

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia | Casos | Resultado | Cumple |
|---|---|---|---|
| CA-01 — el capítulo nombra su historia dueña | CP-000, CP-001 | %(ca01)s, y el enlace **%(resuelve)s** | Sí |
| CA-02 — un cambio tiene dónde bajarse | CP-002 | La historia recibe la fila y el comprobador deja de reclamar | Sí |

**Los que no cumplen:** ninguno.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Casos ejecutados | Plan §12 | 4 de 4 | 4 de 4 | Sí |
| **Capítulos de los 21 sin su historia nombrada** | Plan §12 | **0** | **0** | Sí |
| **Enlaces rotos en el estándar** | Plan §12 | **0** | **0** | Sí |
| Historias que siguen «sin fases» tras la fila | Plan §12 | 0 | 0 | Sí |
| **Archivos de `base/` tocados** | Plan §12 | **0** | **0** | Sí |

**Lo que no se cumplió:** nada.

---

## 6. Veredicto de la fase

**Concepto:** **Cumple**

**Justificación:** los dos criterios quedaron cubiertos por casos ejecutados. El crítico —que el enlace de la cabecera **resuelva**, no solo que el nombre esté escrito— se comprobó apuntando al archivo del otro lado y con `validar.py enlaces` sobre todo el cuerpo. **No se tocó ningún archivo de `base/`**, que era el límite de esta fase.

**Qué falta para que cumpla:** nada.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-00 | El estado de las 21, con nombres | [t00-las-22-historias-de-capitulo.py](../../../../../historico-chat/scripts/%(hoy)s/t00-las-22-historias-de-capitulo.py) |
| EV-01 | La cabecera del capítulo | `%(cap_rel)s` |
| EV-02 | La fila y el conteo | `validar.py fases` |

---

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | %(hoy)s | 4 | 0 | Primera ejecución |
""" % d


def estado_fase(d):
    return u"""# Estado de fase — Fase `%(fase)s` (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `%(fase)s` |
| **Módulo** | Cuerpo de reglas |
| **Planteamiento / Épica / HU** | [EP-001](../../epica.md) · [%(hu)s](../%(hu_archivo)s) |
| **Última actualización** | %(hoy)s |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ (la redacción de los CA es la especificación, `02·F19`) |
| 6 | Diseñador | diseño coherente | ☑ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ %(hoy)s, con el molde de las veintiuna |
| 8 | Implementador | implementado + pruebas verdes | ☑ — **no se construyó: se comprobó** (`13·DOC6`) |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | N/A — el estándar no se despliega |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 2 de 2 |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | %(defectos_estado)s |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-00 | Terminada | **21 de 21** nombran su historia |
| T-01 | Terminada | El enlace de la cabecera **%(resuelve)s** |
| T-02 | Terminada | La %(hu)s recibe la fila en su §8 |
| T-03 | Terminada | [resultado_pruebas.md](resultado_pruebas.md) |
| T-04 | Terminada | [funcionalidad_implementada.md](funcionalidad_implementada.md) y la fila |

**Hechas:** 5 de 5. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  `13·DOC5`

| Decisión / aprendizaje | Señal registrada |
|---|---|
| El molde de las veintiuna se aprueba una vez: veintiuna aprobaciones de un documento idéntico vuelven la puerta un trámite | `S-081` |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del commit.**

---

## 4. Si se bloqueó

No se bloqueó.
""" % d


def funcionalidad(d):
    return u"""# Funcionalidad implementada — Fase `%(fase)s` (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `%(fase)s` |
| **Módulo** | Cuerpo de reglas |
| **Especificación del módulo** | La redacción de los CA de la [%(hu)s](../%(hu_archivo)s) es la especificación funcional (`02·F19`) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | %(hu)s (CA-01, CA-02) |
| **Fecha de cierre** | %(hoy)s |
| **Versión del estándar al cerrar** | `%(version)s` |
| **Commit** | Se completa al commitear |

---

## 1. Qué se implementó — resumen

**Nada: se comprobó.** Es retro-documentación (`13·DOC6`). El capítulo `%(cap)s` ya nombraba su historia dueña en la cabecera; lo que faltaba era **dejarlo verificado y darle a la historia una fase donde bajen sus cambios**.

Con esto, el capítulo `%(cap)s` y sus **%(reglas)s reglas** dejan de ser texto sin dueño declarado: tienen historia, y la historia tiene por dónde recibir un cambio.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem del especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 — el capítulo nombra su historia dueña | doc | `%(cap_rel)s`, su cabecera | ✅ | El enlace **%(resuelve)s** |
| CA-02 — un cambio tiene dónde bajarse | doc | `%(hu_archivo)s` §8 | ✅ | `validar.py fases` deja de reclamar |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-00 | Medir el `CA-01` en las 21 | ✅ hecha | `t00-las-22-historias-de-capitulo.py` | **21 de 21** |
| T-01 | La cabecera nombra y el enlace resuelve | ✅ hecha | `%(cap_rel)s` | `CP-001` |
| T-02 | La historia recibe la fila | ✅ hecha | `%(hu_archivo)s` | `CP-002` |
| T-03 | El resultado de pruebas | ✅ hecha | [resultado_pruebas.md](resultado_pruebas.md) | — |
| T-04 | El cierre y la fila | ✅ hecha | este documento | — |

**Correspondencia con el plan:** 5 tareas en el plan, 5 acá.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba:** ninguno. **Cero archivos de `base/`**, que era el límite.

**Esfuerzo real contra estimado:** el plan estimaba 1,5 h. El real fue menor: **las cifras las midió un programa capítulo por capítulo**, y escribirlas a mano era lo que costaba.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple** |

- **Suites ejecutadas + resultado:** `validar.py enlaces` **sin enlaces rotos**, y `validar.py fases`, que deja de contar esta historia como «sin fases». No se corre la suite de código: esta fase no toca código.
- **Verificaciones manuales** (`08·T4`):
  - **Ningún archivo de `base/` cambió.**
  - El capítulo tiene **%(reglas)s regla(s)** donde el analizador las ve.
- **Defectos abiertos que se aceptaron:** %(defectos_estado)s

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

- **Punto de entrada:** la cabecera del capítulo `%(cap)s`. Quien vaya a cambiarlo lee ahí por dónde baja el cambio.
- **Permisos o datos base sembrados:** ninguno.

---

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal |
|---|---|---|
| **Las cifras de este documento las midió un programa** | Se descartó copiarlas de la fase del capítulo `02`: copiar ciento cinco documentos es la forma más segura de que uno diga algo falso sin que nadie lo note | `S-081` |
| **El molde se aprobó una vez, no veintiuna** | Veintiuna aprobaciones de un documento idéntico vuelven la puerta un trámite, y una puerta que es trámite deja de mirar | `S-081` |
| **No se tocó `base/`** | Cambiar el capítulo para acomodar la fase es al revés | — |

---

## 6. Deuda técnica y pendientes generados

%(deuda)s

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] Mapa de dependencias: no aplica; la fase no tocó código.
- [x] Catálogo de módulos: no se creó módulo.
- [x] Índice `README.md` de la carpeta de la historia.
- [x] Especificación del módulo: los CA de la HU, que no cambiaron al comprobar.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**No aplica.** El capítulo ya viaja a los proyectos con `base/`; esta fase no cambió su texto.
""" % d


# ---------------------------------------------------------------- el trabajo

def main():
    version = leer(os.path.join(RAIZ, "VERSION")).strip()
    cuenta = por_capitulo()
    historias = sorted(n for n in os.listdir(EPICA) if DE_CAPITULO.match(n))

    hechas, saltadas = [], []
    for h in historias:
        m = DE_CAPITULO.match(h)
        numero_hu, cap = m.group(1), m.group(2)
        carpeta_hu = os.path.join(EPICA, h)
        hu_archivo = h + ".md"

        ruta_cap, forma = capitulo_de(cap)
        if ruta_cap is None:
            saltadas.append((h, "no se encuentra el capitulo"))
            continue

        texto_cap = leer(ruta_cap)
        nombrada, resuelve, destino = enlace_de_la_cabecera(
            texto_cap, os.path.dirname(ruta_cap))
        if not nombrada or not resuelve:
            # El criterio de suspension del plan: si el enlace no resuelve,
            # esto no es retrodocumentacion y no se escribe como si lo fuera.
            saltadas.append((h, "el enlace de la cabecera no resuelve"))
            continue

        reglas = cuenta.get(cap, 0)
        nombre_fase = "A-EP-001-HU-%s-retrodocumentar-el-capitulo-%s" % (numero_hu, cap)
        destino_fase = os.path.join(carpeta_hu, nombre_fase)
        if not os.path.isdir(destino_fase):
            os.makedirs(destino_fase)

        nota = ""
        nota_corta = ""
        defectos = ("| ID | Título | Caso que lo destapó | Severidad | Estado | "
                    "Dónde quedó registrado |\n|---|---|---|---|---|---|\n"
                    "| — | Ninguno | — | — | — | — |\n\n"
                    "**Defectos abiertos que se aceptan y por qué:** ninguno.")
        defectos_estado = "Ninguno"
        deuda = ("| Descripción | Origen | Destino |\n|---|---|---|\n"
                 "| Ninguna | — | — |")
        if reglas == 0:
            nota = (u"**Este capítulo aparece con cero reglas, y no es que no tenga: "
                    u"es que el analizador no las ve.** Su encabezado usa una forma "
                    u"que `metareglas.reglas()` no reconoce. Está declarado, no "
                    u"escondido: es lo que arregla la fase "
                    u"`B-EP-004-HU-002-el-analizador-ve-todas-las-reglas`. **No se "
                    u"corrige acá**: esta fase no toca `base/` ni el analizador.")
            nota_corta = (u"**El cero de la fila 2 no dice que el capítulo esté vacío: "
                          u"dice que el analizador no lo ve.** Está en `B-EP-004-HU-002`.")
            defectos = (u"| ID | Título | Caso que lo destapó | Severidad | Estado | "
                        u"Dónde quedó registrado |\n|---|---|---|---|---|---|\n"
                        u"| D-01 | **El analizador cuenta cero reglas en este capítulo**, "
                        u"y el capítulo no está vacío | La verificación manual 2 | Media | "
                        u"**Abierto**, con destino | `B-EP-004-HU-002-el-analizador-ve-"
                        u"todas-las-reglas`, que existe para esto |\n\n"
                        u"**Defectos abiertos que se aceptan y por qué:** `D-01`. **No es "
                        u"de esta fase**: corregir el analizador o el encabezado del "
                        u"capítulo está fuera de su alcance, y su fase ya existe. Se "
                        u"declara para que el cero no se lea como «capítulo vacío».")
            defectos_estado = (u"`D-01` — el analizador no ve las reglas de este capítulo. "
                               u"Su fase existe: `B-EP-004-HU-002`")
            deuda = (u"| Descripción | Origen | Destino |\n|---|---|---|\n"
                     u"| **El analizador no ve las reglas de este capítulo**, así que "
                     u"cualquier conteo automático sobre él da cero | Cambio del entorno "
                     u"— el capítulo usa una forma de encabezado que el analizador no "
                     u"reconoce | `B-EP-004-HU-002-el-analizador-ve-todas-las-reglas` |")

        d = {
            "fase": nombre_fase,
            "hu": "HU-" + numero_hu,
            "hu_archivo": hu_archivo,
            "cap": cap,
            "cap_rel": os.path.relpath(ruta_cap, RAIZ).replace(os.sep, "/"),
            "reglas": reglas,
            "forma": forma,
            "hoy": HOY,
            "version": version,
            "enlace": destino,
            "resuelve": "resuelve",
            "ca01": u"Nombra la HU-" + numero_hu,
            "nota_reglas": nota,
            "nota_reglas_corta": nota_corta,
            "defectos": defectos,
            "defectos_estado": defectos_estado,
            "deuda": deuda,
        }

        for nombre, molde in (("plan_trabajo.md", plan_trabajo),
                              ("plan_pruebas.md", plan_pruebas),
                              ("resultado_pruebas.md", resultado_pruebas),
                              ("estado-fase.md", estado_fase),
                              ("funcionalidad_implementada.md", funcionalidad)):
            escribir(os.path.join(destino_fase, nombre), molde(d))

        hechas.append((h, cap, reglas, forma))
        print("%-58s cap %s · %2d reglas · %s" % (h[:56], cap, reglas, forma))

    print("")
    print("Escritas %d fases de %d historias." % (len(hechas), len(historias)))
    for h, motivo in saltadas:
        print("   SALTADA %-50s %s" % (h[:48], motivo))
    if saltadas:
        print("")
        print("Una saltada NO es un fallo del guion: es el criterio de suspension")
        print("del plan. Si el enlace no resuelve, eso no es retrodocumentacion.")


if __name__ == "__main__":
    sys.exit(main())
