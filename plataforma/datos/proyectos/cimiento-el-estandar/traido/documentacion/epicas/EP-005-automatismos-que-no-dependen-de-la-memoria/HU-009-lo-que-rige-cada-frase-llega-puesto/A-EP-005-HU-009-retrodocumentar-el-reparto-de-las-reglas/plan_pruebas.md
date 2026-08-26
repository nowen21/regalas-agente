# Plan de Pruebas — Fase A-EP-005-HU-009-retrodocumentar-el-reparto-de-las-reglas

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ninguna exigencia quede sin al menos un caso**, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó al correrlas va en el [resultado_pruebas.md](resultado_pruebas.md). La lista de tareas vive en el [plan_trabajo.md](plan_trabajo.md).

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-005-HU-009 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-005-HU-009-retrodocumentar-el-reparto-de-las-reglas` |
| **Fecha** | 2026-08-15 |
| **Elaborado por** | Ing. José Dúmar Jiménez Ruíz |
| **Estado** | Borrador |

> **Proporcionalidad.** Una sola fase: se llenan las secciones 3, 5, 6, 9 y 12.

---

## 3. Estrategia de pruebas

**Lo que se prueba es el programa que ya corre.** Esta fase no construye nada, así que las pruebas no confirman un trabajo nuevo: son la red que hace que el reparto no se pueda cambiar por descuido.

Tres condiciones, y un caso que incumpla alguna no vale aunque pase:

1. **Se dispara por donde dispara el sistema:** el cargador se corre como lo corre el enganche de apertura, sobre un cuerpo de reglas de verdad.
2. **La precondición la produce el sistema:** el cuerpo de reglas es el de este repositorio, no uno recortado a mano, salvo en los casos de borde, donde lo que se prueba es justamente la ausencia.
3. **El resultado escribe la orden y su salida**, paso a paso.

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Integración | Que el reparto entregue completos los capítulos que deben y en índice el resto | Este repositorio | Sí |
| Límite | Que sin `base/` y con el gate sin pasar se comporte como está dicho | Carpetas temporales | Sí |
| Rendimiento | Qué pesa y cuánto tarda lo que se inyecta | Este repositorio | Parcial |

**Alcance de la corrida ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)):** `validadores/pruebas.py` y `validar.py estandar`.

---

## 5. Matriz de trazabilidad

| HU | Exigencia | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-009 | [CA-01](../HU-009-lo-que-rige-cada-frase-llega-puesto.md#ca-01--los-capítulos-que-rigen-cada-frase-llegan-con-su-texto) | [CP-001](#cp-001--los-capítulos-que-rigen-cada-frase-llegan-con-su-texto) | Funcional | Crítica | Sí | ☐ |
| HU-009 | [CA-02](../HU-009-lo-que-rige-cada-frase-llega-puesto.md#ca-02--se-dice-qué-llegó-puesto-y-qué-llegó-como-índice) | [CP-002](#cp-002--el-contexto-dice-qué-llegó-puesto-y-qué-hay-que-abrir) | Funcional | Alta | Sí | ☐ |
| HU-009 | [CA-03](../HU-009-lo-que-rige-cada-frase-llega-puesto.md#ca-03--el-arranque-no-se-vuelve-lento) · [RNF-01](../HU-009-lo-que-rige-cada-frase-llega-puesto.md#5-requisitos-no-funcionales) | [CP-004](#cp-004--lo-que-cuesta-el-arranque) | Rendimiento | Media | Parcial | ☐ |
| HU-009 | [RNF-02](../HU-009-lo-que-rige-cada-frase-llega-puesto.md#5-requisitos-no-funcionales) | [CP-002](#cp-002--el-contexto-dice-qué-llegó-puesto-y-qué-hay-que-abrir) | Usabilidad | Alta | Sí | ☐ |
| HU-009 | Transversales | [CP-003](#cp-003--sin-cuerpo-de-reglas-no-entrega-nada) y [CP-005](#cp-005--con-el-gate-sin-pasar-entrega-solo-esa-regla) | Funcional | Crítica | Sí | ☐ |

**Cobertura:** 5 de 5 exigencias cubiertas = 100%.

---

## 6. Casos de prueba

### CP-001 — Los capítulos que rigen cada frase llegan con su texto

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-009 / [CA-01](../HU-009-lo-que-rige-cada-frase-llega-puesto.md#ca-01--los-capítulos-que-rigen-cada-frase-llegan-con-su-texto) |
| **Tipo** | Funcional — camino feliz |
| **Prioridad** | Crítica |
| **Precondiciones** | Este repositorio, con su cuerpo de reglas completo |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedirle al cargador el contexto de arranque | Devuelve texto |
| 2 | Buscar el texto de una regla del capítulo de identidad | Está completo, no como título |
| 3 | Buscar el texto de una regla del capítulo de conducta | Está completo |
| 4 | Buscar una regla de cualquier otro capítulo | Aparece solo su línea de índice, con ruta, peso y título |

### CP-002 — El contexto dice qué llegó puesto y qué hay que abrir

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-009 / [CA-02](../HU-009-lo-que-rige-cada-frase-llega-puesto.md#ca-02--se-dice-qué-llegó-puesto-y-qué-llegó-como-índice) y [RNF-02](../HU-009-lo-que-rige-cada-frase-llega-puesto.md#5-requisitos-no-funcionales) |
| **Tipo** | Funcional |
| **Prioridad** | Alta |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer el encabezado de lo que llegó completo | Dice que rige la sesión y que es obligatorio |
| 2 | Leer el encabezado del índice | Dice que eso no está cargado y que hay que abrirlo antes de tocar el tema |

### CP-003 — Sin cuerpo de reglas no entrega nada

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-009 / transversal de límites |
| **Tipo** | Funcional — límite |
| **Prioridad** | Crítica |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedirle el contexto a una carpeta temporal sin `base/` | Devuelve vacío, sin fallar |
| 2 | Mirar la carpeta | Sigue vacía: no escribió nada |

### CP-004 — Lo que cuesta el arranque

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-009 / [CA-03](../HU-009-lo-que-rige-cada-frase-llega-puesto.md#ca-03--el-arranque-no-se-vuelve-lento) y [RNF-01](../HU-009-lo-que-rige-cada-frase-llega-puesto.md#5-requisitos-no-funcionales) |
| **Tipo** | Rendimiento |
| **Prioridad** | Media |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Medir cuánto pesa lo que se inyecta | Un número, en KB, escrito con la fecha y el tamaño del cuerpo de reglas |
| 2 | Medir cuánto tarda el enganche que lo entrega | Queda por debajo de lo que ya tardan los otros enganches de apertura |

### CP-005 — Con el gate sin pasar entrega solo esa regla

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-009 / transversal de límites |
| **Tipo** | Funcional — borde |
| **Prioridad** | Crítica |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedirle el contexto declarando que el gate de arranque no pasa | Entrega la regla del gate y nada más |
| 2 | Buscar cualquier otra regla en lo entregado | No está: no invita a trabajar sobre una estructura que el estándar manda detener |

---

## 9. Criterios de entrada y de salida

**Entrada:** este plan y el de trabajo aprobados.

**Salida:** los cinco casos en cumple, con su paso a paso escrito, y la medición del arranque anotada con su fecha.

---

## 12. Métricas e informe

| Métrica | Fórmula | Meta |
|---|---|---|
| Cobertura de exigencias | Exigencias con caso / totales | 100% |
| Peso de lo inyectado | KB del contexto | Anotado, con la fecha |
| Tiempo del enganche de apertura | Segundos | Por debajo del más lento que ya corre |
