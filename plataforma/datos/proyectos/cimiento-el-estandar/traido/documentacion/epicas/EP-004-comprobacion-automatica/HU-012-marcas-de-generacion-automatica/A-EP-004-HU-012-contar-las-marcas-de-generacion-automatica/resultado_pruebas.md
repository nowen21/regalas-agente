# Resultado de Pruebas — Fase A-EP-004-HU-012: contar las marcas de generación automática

| Campo | Valor |
|---|---|
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-18 |

---

## 1. Casos ejecutados

| Caso | Veredicto | Qué dio |
|---|---|---|
| [CP-001](plan_pruebas.md#cp-001--la-notación-propia-del-estándar-no-se-reporta) | ✅ **Pasa** | La cita `NN·ID` no cuenta como punto medio |
| [CP-002](plan_pruebas.md#cp-002--el-texto-con-marcas-de-tipografía-se-reporta-y-el-limpio-no) | ✅ **Pasa** | Con archivo y línea; el limpio, en silencio |
| [CP-003](plan_pruebas.md#cp-003--las-marcas-invisibles-se-reportan-por-su-posición) | ✅ **Pasa** | Las ocho invisibles |
| [CP-004](plan_pruebas.md#cp-004--el-símbolo-que-es-notación-en-un-contexto-y-marca-en-otro) | ✅ **Pasa** | Ver §3 — el límite quedó escrito |

**4 de 4 ejecutados. 4 pasan.** 19 casos automatizados en [validadores/tests/test_las_marcas_de_ia_se_cuentan.py](../../../../../validadores/tests/test_las_marcas_de_ia_se_cuentan.py).

| Qué se corrió | Resultado |
|---|---|
| `validadores/tests/` | **187 · OK** — eran 168 |
| `validadores/pruebas.py` | **357 · OK** (5 fallos esperados) |
| `validar.py estandar` | **Sin incumplimientos** |

---

## 2. El recuento — que era el punto 1 del pendiente 11

**Fuera del histórico**, que es transcripción y no se reescribe:

| Marca | Cuántas |
|---|---:|
| Raya larga (`—`) como inciso | **7 286** |
| Punto medio (`·`) fuera de una cita `NN·ID` | **6 237** |
| Viñeta que abre con negrita y dos puntos | **1 539** |
| Semiraya (`–`) donde va un guion | **1 087** |
| Puntos suspensivos en un carácter (`…`) | 191 |
| Semáforo (🔴 🟡 🟢) | 123 |
| Flecha o visto como viñeta | 10 |
| Encabezado que termina en dos puntos | 4 |
| **Total** | **16 477 en 820 archivos** |

**Lo que se hereda, que es por dónde manda empezar el pendiente:**

| | |
|---|---:|
| `base/` y `plantillas/` | **4 491 marcas en 137 archivos** |
| Líneas afectadas | 3 874 |

**Y con el histórico incluido: 26 920 en 945 archivos.** Se cuenta aparte a propósito: es transcripción literal de lo que se dijo, no se reescribe, y mezclarlo con lo demás convierte deuda en algo que nunca va a bajar.

| Los que más pesan | Marcas |
|---|---:|
| `analisis/base-2026-08-07-cumplimiento-meta-reglas.md` | 757 |
| `CHANGELOG.md` | 457 |
| `base/01-conducta.md` | 418 |
| `base/04-seguridad.md` | 213 |
| `base/03-datos.md` | 183 |

**La pregunta del pendiente era si limpiar son dos horas o dos días. La respuesta es que no son ninguna de las dos.**

---

## 3. CP-004 · Dónde está el límite del programa, escrito

El caso pedía que, si el programa no puede distinguir notación de marca, **quede declarado en vez de simulado**. Dos casos:

**El punto medio sí se distingue.** La cita `NN·ID` de [`20·M4`](../../../../../base/20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md) se descuenta, y el anexo la exceptúa por escrito. El `·` suelto **sí cuenta** — el anexo lo llama *«adornando títulos»*, y eso incluye la forma en que este repositorio titula sus capítulos y sus fases. **No se le hizo excepción**: si el estándar quiere conservar esa forma, es una decisión que se escribe, no un descuento que el programa hace callando.

**Lo que pide criterio no se cuenta, y es la mitad del anexo.** Si la raya aparece «muy seguido», si el paralelismo es «perfecto», si el español «no es de acá», si la negrita cae sobre una frase entera. **Un programa que opinara de eso llenaría de ruido lo que hoy nadie mira**, y una salida sepultada se deja de leer. Queda declarado acá y en un caso de prueba.

---

## 4. La duda que detenía la fase ya estaba contestada

**La fase estaba en la estación 6 desde el 2026-08-17**, detenida por la duda 1 de su §2.7: *«si la comprobación aplica a todo el repositorio o solo a lo que se entrega — el histórico, por ejemplo, es transcripción y no entregable»*.

**La respuesta estaba escrita en el pendiente 11 desde el 2026-08-10**, en su paso 3: *«No tocar el histórico. `historico-chat/` es transcripción literal de lo que se dijo. Reescribirlo lo dañaría»*. Y el paso 2 daba el orden: primero `base/` y `plantillas/`, que es lo que viaja a los proyectos.

> **Una fase esperó un día a que alguien contestara lo que su propio origen ya decía.** Es exactamente lo que [`01·C23`](../../../../../base/01-conducta.md#c23--busca-en-el-repositorio-antes-de-preguntar) vino a evitar — la regla se escribió ayer, y este es su primer caso encontrado.

---

## 5. Lo que queda abierto  ·  [`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md)

**Limpiar es otro trabajo, y grande.** Este contó; el pendiente 11 sigue abierto con sus pasos 2 y 4 — empezar por lo que se hereda, y **reaplicar el checklist a cada regla que se reescriba**, porque editar el texto anula su sello.

**Y hay algo que decir del conteo de hoy:** buena parte de esas 16 477 se escribieron **después** del 2026-08-10, cuando la marca ya estaba registrada. [`02·F21`](../../../../../base/02-flujo-de-trabajo/reglas/F21-un-incumplimiento-ya-identificado-no-se-repite-en-lo-nuevo.md) dice que desde que un incumplimiento queda registrado, lo nuevo nace cumpliendo. **No pasó.** El recuento no separa lo viejo de lo nuevo, y saberlo cambiaría de qué tamaño es el problema: si la deuda es histórica, se limpia una vez; si sigue creciendo, limpiarla sin más es rehacer el trabajo el mes que viene.

---

## 6. Veredicto

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | los tres — tipografía, invisibles, y la notación que no se cuenta |
| **CA en «No»** | ninguno |
| **Defectos abiertos aceptados** | dos: la mitad del anexo que pide criterio, y que el recuento no separa lo viejo de lo nuevo |
| **Ciclos** | 1 |
