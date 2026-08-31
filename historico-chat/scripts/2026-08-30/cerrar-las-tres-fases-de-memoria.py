# -*- coding: utf-8 -*-
"""Cierra las tres fases B de EP-006 que estaban detenidas en la estacion 4.

Las tres arreglan un defecto concreto que su propia fase A habia dejado probado
con `expectedFailure`. El usuario las aprobo el 2026-08-30.
"""
import io
import os

RAIZ = r"c:\Ing. Jose\ia\agente"
EP = os.path.join(RAIZ, "documentacion", "epicas", "EP-006-memoria-de-lo-aprendido")
M = u"Memoria"

CASOS = [
 dict(
  hu_dir="HU-003-busqueda-por-palabra", hu="HU-003",
  hu_md="HU-003-busqueda-por-palabra.md",
  fase="B-EP-006-HU-003-la-busqueda-dice-donde-esta",
  roja="A-EP-006-HU-003-retrodocumentar-la-busqueda-por-palabra",
  criterio=u"CA-01, el resultado alcanza para abrir lo que se encontró",
  estado_viejo=u"| **Estado** | En curso — CA-02, RNF y transversales cumplidos; el CA-01 a medias |",
  estado_nuevo=u"| **Estado** | Terminada — el CA-01 se cerró en la fase `B`: el resultado dice dónde está la señal |",
  resumen=u"""**Dos defectos, y el segundo no se veía.**

El primero es el que la historia pedía: la búsqueda encontraba y **no decía dónde está lo que encontró**, así que el resultado no alcanzaba para abrirlo. Ahora la consulta trae también ese dato y lo imprime **debajo** de cada resultado, en su propia línea: una línea de más por resultado se lee, una columna más en la misma línea no.

El segundo lo destapó la fase `A` al probarlo de una forma que vale la pena copiar: el camino «(sin señales relevantes)» **retornaba sin cerrar la conexión**, y eso no se deduce leyendo. La prueba borra el archivo después de buscar, porque en Windows no se puede borrar lo que está tomado. El descuido se ve en vez de suponerse.""",
  antes_ahora=[(u"La búsqueda encuentra y no dice dónde", u"Imprime la ubicación debajo de cada resultado"),
               (u"El camino sin resultados deja la conexión tomada", u"La cierra antes de salir")],
  tareas=[(u"T-01 · traer la ubicación en la consulta", u"CP-001"),
          (u"T-02 · imprimirla debajo, y solo si la hay", u"CP-001"),
          (u"T-03 · cerrar la conexión en el camino sin resultados", u"CP-005"),
          (u"T-04 · destapar las dos pruebas", u"59 en verde")],
  decisiones=[(u"La ubicación va en su propia línea", u"Una columna más en la misma línea deja el renglón ilegible cuando la ruta es larga"),
              (u"Solo se imprime si la señal la tiene", u"Una línea vacía por resultado es ruido"),
              (u"La conexión se cierra en el camino que retorna temprano", u"Es el único que se escapaba, y en Windows deja el archivo bloqueado")],
 ),
 dict(
  hu_dir="HU-004-busqueda-por-significado", hu="HU-004",
  hu_md="HU-004-busqueda-por-significado.md",
  fase="B-EP-006-HU-004-degradar-sin-el-modelo",
  roja="A-EP-006-HU-004-retrodocumentar-la-busqueda-por-significado",
  criterio=u"CA-02, sin el modelo la búsqueda sigue funcionando",
  estado_viejo=u"| **Estado** | En curso — CA-01 cumplido y medido; el CA-02, su RNF y el transversal de privacidad, no |",
  estado_nuevo=u"| **Estado** | Terminada — el CA-02 se cerró en la fase `B`: sin el modelo, la búsqueda degrada y lo dice |",
  resumen=u"""**El más grave de los tres, porque rompía lo que no dependía de él.**

Saber si las librerías opcionales están puestas no es lo mismo que poder cargar el modelo: puede faltar el archivo, o no haber red la primera vez. Con las librerías instaladas y el modelo ausente, la búsqueda **se caía entera y se llevaba por delante la búsqueda por palabra**, que no necesita ni modelo ni red.

Esa es la promesa que la historia hace: que instalar lo semántico sea opcional **de verdad**. Una parte opcional que al fallar tumba la que no lo es, no es opcional.""",
  antes_ahora=[(u"Con el modelo ausente, la búsqueda entera se cae", u"Degrada a búsqueda por palabra"),
               (u"El error no se explicaba", u"El modo lo dice: «léxica (el modelo no se pudo cargar)»")],
  tareas=[(u"T-01 · atrapar el fallo al cargar o al indexar", u"CP-002"),
          (u"T-02 · seguir con lo léxico", u"CP-002"),
          (u"T-03 · decirlo en el modo, sin callarlo", u"CP-002"),
          (u"T-04 · destapar la prueba", u"59 en verde")],
  decisiones=[(u"Se atrapa cualquier error, no una clase concreta", u"Quien falla es una librería de terceros bajando un modelo; el día que le cambien el nombre a su excepción, la memoria no puede dejar de servir"),
              (u"El fallo se dice en el modo, no se calla", u"Degradar en silencio deja al que busca creyendo que buscó de las dos formas"),
              (u"No se comprueba el modelo al arrancar", u"Cargarlo para saber si carga cuesta lo mismo que usarlo, y la mayoría de las búsquedas no lo necesitan")],
 ),
 dict(
  hu_dir="HU-007-marcar-lo-que-dejo-de-aplicar", hu="HU-007",
  hu_md="HU-007-marcar-lo-que-dejo-de-aplicar.md",
  fase="B-EP-006-HU-007-marcar-deja-fecha-y-referencia",
  roja="A-EP-006-HU-007-retrodocumentar-la-marca-de-lo-que-dejo-de-aplicar",
  criterio=u"CA-01, la marcada queda con la fecha y con qué la reemplazó",
  estado_viejo=u"| **Estado** | En curso — CA-02, RNF y no regresión cumplidos; el CA-01 y la trazabilidad, no |",
  estado_nuevo=u"| **Estado** | Terminada — el CA-01 y la trazabilidad se cerraron en la fase `B`: marcar y archivar dejan fecha |",
  resumen=u"""**Lo que decía la consola se perdía al cerrarla.**

Marcar una señal como reemplazada imprimía «S-001 marcada reemplazada por S-002» y **no guardaba ni por cuál ni cuándo**. Archivar tampoco dejaba fecha. De una señal marcada no se sabía nada de lo que la marca prometía.

Se notó usándolo: esta misma sesión marcó una señal de terminología como reemplazada y tuvo que rodear el defecto escribiendo la nueva con el enlace puesto a mano.

**Y apareció un tercer defecto, en la propia prueba.** La que comprueba que la marca de vigencia no dependa del huso usaba 181 días como si fueran seis meses, cuando el contador va por meses de calendario: fallaba o pasaba según el mes en que se corriera. Ahora cuenta seis meses de calendario.""",
  antes_ahora=[(u"Marcar no guardaba por cuál ni cuándo", u"Guarda las dos cosas"),
               (u"Archivar no dejaba fecha", u"La deja"),
               (u"Una prueba pasaba o fallaba según el mes", u"Cuenta meses de calendario")],
  tareas=[(u"T-01 · marcar guarda por cuál y cuándo", u"CP-001"),
          (u"T-02 · archivar deja fecha", u"CP-002"),
          (u"T-03 · destapar las dos pruebas", u"59 en verde"),
          (u"T-04 · arreglar la prueba que dependía del mes", u"CP-004")],
  decisiones=[(u"La fecha va en la columna que ya existía para el cierre", u"No hacía falta columna nueva: la que había estaba vacía"),
              (u"Marcar migra el esquema antes de escribir", u"Una base vieja no tiene esas columnas, y el comando no puede fallar por eso"),
              (u"La prueba del huso cuenta meses, no días", u"Contar días contra un contador de meses da un resultado que cambia con el calendario")],
 ),
]

MOLDE_ESTADO = u"""# Estado de fase — Fase `{fase}` (módulo {M})   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `{fase}` |
| **Módulo** | {M} |
| **Planteamiento / Épica / HU** | [EP-006](../../epica.md) · [{hu}](../{hu_md}) |
| **Última actualización** | 2026-08-30 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

**Estuvo detenida trece días en la estación 4**, con su plan y su plan de pruebas escritos y sin aprobar. El usuario la aprobó el 2026-08-30 y la fase se ejecutó ese mismo día.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ✅ La fase `A` dejó el defecto probado |
| 2 | Proponente · alcance | 👤 alcance aprobado | ✅ 2026-08-30 |
| 3 | Escritor de épica | 👤 épica aprobada | ✅ Ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ✅ Ya existía |
| 5 | Escritor de especificación | 👤 especificación aprobada | ✅ El CA no cambia |
| 6 | Diseñador | diseño coherente | ✅ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ✅ Escritos el 2026-08-17, aprobados el 2026-08-30 |
| 8 | Implementador | implementado + pruebas verdes | ✅ 59 pruebas de la memoria, 59 en verde |
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
| **CA cumplidos** | El {criterio} |
| **CA en "No"** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §2 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Evidencia |
|---|---|---|
{tareas}

**Hechas:** 4 de 4. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  `13·DOC5`

| Decisión / aprendizaje | Dónde queda |
|---|---|
| Un defecto que la fase anterior dejó probado con fallo esperado se arregla y se destapa, no se borra | §4 del resultado |

---

## 3. Pendiente / preguntas abiertas

- **La autorización del commit**, que se pide aparte.

---

## 4. Si se bloqueó

No se bloqueó. Estuvo esperando una aprobación, que es distinto.
"""

MOLDE_RESULTADO = u"""# Resultado de Pruebas — Fase `{fase}`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `{fase}` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-30 |
| **Ciclo** | 1 |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** el defecto que la fase `{roja}` dejó probado con fallo esperado quedó arreglado, y su prueba pasó a correr como cualquier otra.

| Métrica | Meta | Real |
|---|---|---|
| Pruebas de la memoria en verde | 59 | **59** |
| Pruebas marcadas como fallo esperado | 0 | **0**, eran 5 |

---

## 3. Qué se arregló

{resumen}

| Antes | Ahora |
|---|---|
{antes_ahora}

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 El fallo esperado se destapa, no se borra

La fase `A` no podía arreglar esto: su plan declaraba que no se tocaba el programa (`02·F8`). Dejó el defecto **probado y marcado como fallo esperado**, que es la forma de que no se pierda: el día que se arregle, la prueba pasa a «éxito inesperado» y obliga a volver.

Es exactamente lo que ocurrió acá: al arreglar, la corrida reportó éxitos inesperados y hubo que volver a destaparlas una por una.

### 4.2 La corrida completa

```
Ran 59 tests in 5.7s
OK
```

Sin un solo fallo esperado en el archivo, donde había cinco.

---

## 5. Defectos encontrados

**Ninguno nuevo.**

---

## 6. Evidencias

- `memoria/memoria.py` y `memoria/semantica.py`
- `memoria/pruebas.py`, con las pruebas destapadas
"""

MOLDE_CIERRE = u"""# Funcionalidad implementada — Fase `{fase}` (módulo {M})   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `{fase}` |
| **Módulo** | {M} |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), escrito el 2026-08-17 y aprobado el 2026-08-30 |
| **HU / CA cubiertas** | [{hu}](../{hu_md}): el {criterio} |
| **Fecha de cierre** | 2026-08-30 |
| **Versión del estándar al cerrar** | `36.0.2` — **sin cambio**: no se toca `base/` ni `plantillas/` |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | Pendiente de autorización |
| **Reemplaza el veredicto de** | `{roja}` |

> **Por qué se declara el reemplazo:** el defecto que dejó aquella fase en rojo está arreglado y su prueba corre. **El veredicto de aquella fase no se toca** (`20·M11`).

---

## 1. Qué se implementó — resumen

{resumen}

| Antes | Ahora |
|---|---|
{antes_ahora}

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem | Categoría | Ubicación | Estado |
|---|---|---|---|
| {criterio} | servicio | `memoria/` | ✅ |

### 2.2 Plan de trabajo → ejecución

| Tarea | Evidencia |
|---|---|
{tareas_cierre}

**Correspondencia:** 4 tareas, 4 con resultado.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, ciclo 1 |
| **Suites ejecutadas** | Las 59 pruebas de la memoria, 59 en verde |
| **Defectos abiertos** | Ninguno |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Sin punto de entrada nuevo.

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué |
|---|---|
{decisiones}

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| Ninguna | — |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] El `Estado` de la historia y su tabla de fases.
- [ ] `VERSION` y `CHANGELOG.md`: **no aplica**.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**Nada que desplegar.**
"""


def w(D, nombre, texto):
    with io.open(os.path.join(D, nombre), "w", encoding="utf-8",
                 newline="\n") as f:
        f.write(texto)


for c in CASOS:
    D = os.path.join(EP, c["hu_dir"], c["fase"])
    d = dict(c, M=M,
             tareas="\n".join(u"| %s | Terminada | %s |" % t for t in c["tareas"]),
             tareas_cierre="\n".join(u"| %s | %s |" % t for t in c["tareas"]),
             antes_ahora="\n".join(u"| %s | %s |" % t for t in c["antes_ahora"]),
             decisiones="\n".join(u"| %s | %s |" % t for t in c["decisiones"]))
    w(D, "estado-fase.md", MOLDE_ESTADO.format(**d))
    w(D, "resultado_pruebas.md", MOLDE_RESULTADO.format(**d))
    w(D, "funcionalidad_implementada.md", MOLDE_CIERRE.format(**d))

    R = os.path.join(EP, c["hu_dir"], c["hu_md"])
    with io.open(R, encoding="utf-8") as f:
        t = f.read()
    if c["estado_viejo"] in t:
        t = t.replace(c["estado_viejo"], c["estado_nuevo"], 1)
    sep = u"| Fase | Qué CA cubre | Estado |\n|---|---|---|\n"
    fila = (u"| [%s](%s/estado-fase.md) | %s | **Ejecutada el 2026-08-30.** "
            u"Veredicto: [**Cumple**](%s/resultado_pruebas.md#2-veredicto-de-la-fase) "
            u"— el defecto que la fase `A` dejó probado quedó arreglado. Declara "
            u"reemplazar el veredicto de la fase `A` |\n"
            % (c["fase"], c["fase"], c["criterio"], c["fase"]))
    if sep in t:
        t = t.replace(sep, sep + fila, 1)
    with io.open(R, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)
    print("cerrada:", c["fase"])
