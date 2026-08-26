# Funcionalidad implementada — Fase A-EP-006-HU-004-retrodocumentar-la-busqueda-por-significado (módulo Memoria)

> **Veredicto de la fase: [No cumple](resultado_pruebas.md#6-veredicto-de-la-fase).** La búsqueda por significado hace lo que promete y ahora está medida: tres consultas reales pasaron de **0 a 5 resultados**. Lo que no cumple es la promesa de ser opcional — **sin el modelo, la búsqueda se cae entera**. Lo que falta pide una fase `B-EP-006-HU-004`.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-006-HU-004-retrodocumentar-la-busqueda-por-significado` |
| **Módulo** | Memoria — [`memoria/semantica.py`](../../../../../memoria/semantica.py) · [`memoria/memoria.py`](../../../../../memoria/memoria.py) |
| **Especificación del módulo** | No la hay aparte: la especificación son los CA de [HU-004](../HU-004-busqueda-por-significado.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / exigencias cubiertas** | HU-004: [CA-01](../HU-004-busqueda-por-significado.md#ca-01--encuentra-lo-que-se-escribió-con-otras-palabras), [CA-02](../HU-004-busqueda-por-significado.md#ca-02--sin-el-modelo-la-búsqueda-sigue-funcionando), su RNF y sus dos transversales |
| **Fecha de cierre** | 2026-08-17 |
| **Commit** | Pendiente de autorización del usuario |

---

## 1. Qué se implementó — resumen

**Nada de programa: la fase midió lo que nadie había medido y encontró dos defectos.** La búsqueda híbrida está en producción desde el pendiente 05. Lo que faltaba era el número que responde la única pregunta que importa —**¿vale la pena instalarlo?**— y la prueba de la promesa que la hace opcional.

El número apareció. La promesa, no se cumple.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| Vectores calculados en local | programa | [`semantica.py`](../../../../../memoria/semantica.py) · `embed` · `indexar` | ✅ Ya existía | CP-004 |
| Fusión de léxica y semántica sin perder nada | programa | [`memoria.py`](../../../../../memoria/memoria.py) · `_rrf` | ✅ Ya existía | CP-002 |
| Degradar a léxica si faltan las **librerías** | programa | `semantica.disponible()` | ✅ Ya existía | CP-003 |
| **Degradar a léxica si falta el modelo** | programa | Nadie lo comprueba; `cmd_search` no atrapa el error | ❌ **No existe** | CP-003 |
| **Cargar el modelo sin salir a la red** | programa | `_cargar()` usa `from_pretrained` sin modo offline | ❌ **Falta** | CP-004, paso 2 |
| No recalcular lo que no cambió | programa | `indexar` compara por hash del texto | ✅ Ya existía | RNF |
| Las cinco exigencias, con red | pruebas | [`memoria/pruebas.py`](../../../../../memoria/pruebas.py), clase `BusquedaPorSignificado` | ✅ Escritas acá | 7 pruebas |
| **Cuánto mejora, con datos reales** | medición | §2 del [resultado_pruebas.md](resultado_pruebas.md) | ✅ Medido acá | CP-001 |

### 2.2 Criterios de aceptación

| CA | Cómo quedó cubierto | Estado |
|---|---|---|
| CA-01 | Encuentra con otras palabras; 3 de 3 consultas reales de 0 a 5, sin perder nada | ✅ |
| CA-02 | Sin **librerías** sí y lo dice; sin **modelo**, se cae entera | ❌ |
| RNF · sirve aunque el modelo no esté | Lo mismo | ❌ |
| Transversal · Privacidad | El contenido no sale; pero abre una conexión al cargar el modelo | ❌ |
| Transversal · Rendimiento | 5,02 s la primera búsqueda · 0,009 s las siguientes | ✅ |

---

## 3. Lo que la fase midió, que es lo que venía a buscar

| Medición, 2026-08-17, sobre las 237 señales reales | Valor |
|---|---|
| Consultas reales que mejoran con significado | **3 de 3** |
| Resultados de esas consultas **sin** significado | **0, 0 y 0** |
| Resultados **con** significado | 5, 5 y 5 |
| Resultados que la híbrida **pierde** respecto de la léxica | **0** |
| De cinco resultados de una consulta, cuántos sirven | **2**; los otros **3** son ruido |
| Primera búsqueda, en frío | **5,02 s** |
| Búsquedas siguientes | **0,009 s** |
| Conexiones abiertas al indexar y buscar | **1**, al cargar el modelo |

**La primera fila es el argumento para instalarlo y la quinta es la advertencia.** Escritas como las escribe una persona —preguntas, no palabras clave—, la búsqueda por palabra **no devuelve nada**. Con significado devuelve cinco, de los que dos sirven. Pasar de nada a algo mayormente ruido es una mejora real; confundirlo con precisión, no.

---

## 4. Los dos defectos, y por qué no se arreglaron acá

| Defecto | Qué le falta | Por qué no se tocó |
|---|---|---|
| `D-01` · sin el modelo se cae todo | Que `disponible()` compruebe que el modelo carga, o que `cmd_search` atrape el fallo y degrade | §2.1 del [plan aprobado](plan_trabajo.md) declara solo `memoria/pruebas.py`. [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md) no deja salirse |
| `D-02` · la carga sale a la red | Cargar el modelo en modo sin conexión | Lo mismo |

**`D-01` es el más grave de todo lo encontrado en esta épica.** Un proyecto que instale las librerías y se quede sin el modelo —una máquina nueva, una caché borrada, un despliegue sin red la primera vez— **pierde la memoria entera**, no solo el significado. La parte que no necesita nada se cae con la que sí.

**Por qué nadie lo vio:** `disponible()` responde `True` en cuanto las dos librerías importan, y en la máquina donde se construyó el modelo ya estaba descargado. El escenario que falla no aparece nunca donde se desarrolla.

---

## 5. Decisiones y señales

| Decisión | Dónde quedó |
|---|---|
| La mejora se mide con **consultas reales sobre la base real**, en copia y solo lectura: consultas inventadas sobre datos inventados no dicen si vale instalarlo | §2 del [resultado](resultado_pruebas.md) |
| **El ruido se mide y se escribe**, aunque el plan no lo obligara a cuantificar: una fusión por rango recíproco siempre devuelve `k` resultados | `D-03` del resultado |
| Las pruebas que necesitan el modelo se saltan si no está, en vez de fallar: probar el complemento opcional no puede volverlo obligatorio | `skipUnless` en la clase de pruebas |
| El escenario «sin el modelo» se separa del escenario «sin las librerías», que el plan mezclaba | CP-003 del resultado |

---

## 6. Lo que no entró, y dónde sigue

| Qué | Dónde |
|---|---|
| Que la búsqueda degrade cuando falta el modelo (`D-01`) | Fase `B-EP-006-HU-004`, propuesta |
| Que el modelo se cargue sin salir a la red (`D-02`) | La misma |
| Buscar por palabra | [HU-003](../../HU-003-busqueda-por-palabra/HU-003-busqueda-por-palabra.md) |

**La advertencia que deja esta fase:** lo opcional solo es opcional si se probó sin ello. Acá se probó sin las librerías —y funciona— pero nunca sin el modelo, que es el escenario que de verdad ocurre en una máquina nueva.
