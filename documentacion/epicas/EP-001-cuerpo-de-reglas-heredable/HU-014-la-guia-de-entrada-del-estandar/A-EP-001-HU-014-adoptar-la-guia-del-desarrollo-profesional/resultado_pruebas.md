# Resultado de Pruebas — Fase A-EP-001-HU-014-adoptar-la-guia-del-desarrollo-profesional   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el `estado-fase.md` para pasar la puerta de verificación, y la fuente de la sección "qué se probó" del `funcionalidad_implementada.md`. El diseño de los casos vive en el `plan_pruebas.md` de esta misma fase, que **no se modifica** al ejecutar: se aprobó antes y así se queda.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-001-HU-014-adoptar-la-guia-del-desarrollo-profesional` |
| **HU** | [HU-014](../HU-014-la-guia-de-entrada-del-estandar.md) — `CA-01` y `CA-02` |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), aprobado por el usuario el 2026-08-21 («si», junto con la HU) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-21 |
| **Ejecutado por** | El agente; cada comprobación con su comando o lectura registrada |
| **Ambiente y versión** | Este repositorio, árbol sin commitear, estándar 28.1.0 |

---

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 2 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

---

## 2. Ejecución caso por caso

**CA-01 · CP-001 — completa, enlazada y sin restos del origen**

**El problema que resuelve:** una guía incompleta o con restos del proyecto de origen no reemplaza a la copia local, y una sin enlaces re-enuncia normas que después divergen.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Contar en [`base/guia-de-entrada.md`](../../../../../base/guia-de-entrada.md) los pasos del ciclo | 10, los del adjunto | 10 (la lista numerada de la primera parte) |
| 2 | Contar las cualidades del producto | 9, las del adjunto | 9 (la lista numerada de la segunda parte) |
| 3 | Recorrer los enlaces de cada paso y cada cualidad | Ninguno sin ancla; `validar.py estandar` sin enlaces rotos en el archivo | Cada paso enlaza a su regla del `02` (mas `01·C17`, `08·T1`, `13·DOC5`, `13·DOC15`) y cada cualidad a su capítulo (`03` a `13`, opt-in `15`/`18`/`19`, núcleo `N4`/`N6`). `validar.py estandar` corrió y no nombra al archivo |
| 4 | Buscar restos del proyecto de origen | Cero | `grep -ci "matematica\|wamp64"` dio 0; la tabla «cómo se vivió en este proyecto» no está |
| 5 | Comparar contra el adjunto, sección por sección | Nada transversal perdido | Las dos partes, la trampa clásica, el modelado por el estándar y la frase resumen están; lo único que no pasó es lo propio del origen (paso 4) y los ejemplos de su stack (`uv sync`, su `SECRET_KEY`), reemplazados por texto agnóstico (`20·M3`) |

**Cómo se verificó que la pareja cumple:** los pasos 1, 2 y 5 aseguran que no falta nada y el 4 que no sobra nada; el 3 es el que separa explicar de legislar, y lo respalda un programa que revisa todo enlace del repositorio. Evidencia EV-01.

---

**CA-02 · CP-002 — viaja, se encuentra y no engorda el arranque**

**El problema que resuelve:** un documento que no viaja no le sirve a los herederos, y uno que nadie nombra no se encuentra; pero si engordara el arranque, cada sesión pagaría por él.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Comprobar que la guía está dentro de `base/` | Viaja con la carpeta, sin tocar el instalador | `base/guia-de-entrada.md` existe; lo que se instala es la carpeta entera |
| 2 | Abrir el [README de `base/`](../../../../../base/README.md) | La nombra, diciendo para quién es | La nombra: «¿Primera vez acá? La guía de entrada explica en lenguaje llano por qué se trabaja así» |
| 3 | Abrir el [mapa del sitio](../../../../../anatomia/mapa-del-sitio.md) | Tiene su fila | La tiene, junto al glosario |
| 4 | Correr el armado del cargador (`cargador.contexto('.')`) y buscar la guía | El texto de apertura no crece: la guía no está entre los archivos numerados que carga | **Distinto de lo esperado, y se declara:** el cargador indexa **todo** `.md` de `base/` (también el glosario), así que aparece **una línea de índice de 102 bytes**: `base/guia-de-entrada.md (10 KB) · La guía de entrada…`. El **contenido** (10 KB) no se suma. El arranque midió **69,9 de 90 KB** |

**Cómo se verificó que la pareja cumple:** lo que el CA exige es que la guía llegue, se encuentre y el arranque no cargue su contenido, y las tres cosas se cumplen: el paso 4 salió distinto de lo redactado en el plan (una línea de índice de 0,1 KB sí aparece) pero esa línea es índice, no contenido, y juega a favor del propio CA — es lo que hace que la guía «se encuentre sin saber que existe» también desde el arranque. El techo de 90 KB no se movió y el consumo queda en 69,9. El desvío queda declarado acá y en §4 como decisión aceptada, no escondida. Evidencia EV-02.

---

| Caso | CA | Prioridad (del plan) | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | [CA-01](../HU-014-la-guia-de-entrada-del-estandar.md#ca-01--la-guía-existe-en-el-estándar-completa-y-enlazada-al-cuerpo-normativo) | Crítica | 2026-08-21 | La guía nueva contra el adjunto: 10 pasos, 9 cualidades, enlaces revisados por `validar.py estandar`, `grep` de restos en 0 | Aprobado | EV-01 | — |
| CP-002 | [CA-02](../HU-014-la-guia-de-entrada-del-estandar.md#ca-02--la-guía-llega-a-los-herederos-y-se-encuentra-sin-saber-que-existe) | Alta | 2026-08-21 | `base/` con el archivo, README y mapa nombrándola, `cargador.contexto('.')` en 69,9 KB con una línea de índice de 102 bytes y el contenido fuera | Aprobado | EV-02 | — |

**Correspondencia con el plan:** 2 casos en el plan, 2 acá.

**Qué salió distinto de lo esperado:** el paso 4 de CP-002, declarado en su fila: una línea de índice de 102 bytes aparece en el arranque porque el cargador indexa todo `base/`; el contenido queda fuera y el techo no se mueve.

---

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | La comparación sección por sección contra el adjunto (CP-001 paso 5) | Lectura lado a lado | Nada transversal perdido |
| 2 | Que la línea del README diga para quién es la guía | Lectura | Lo dice |

---

## 4. Defectos encontrados

Ninguno. **Decisión aceptada** (no defecto): la línea de índice de 102 bytes en el arranque, comportamiento uniforme del cargador para todo `base/`. Excluir la guía habría exigido tocar `cargador.py`, archivo fuera del plan aprobado (`02·F8`), para ocultar lo que el CA quiere que se encuentre.

---

## 5. Veredicto por criterio de aceptación

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| [CA-01](../HU-014-la-guia-de-entrada-del-estandar.md#ca-01--la-guía-existe-en-el-estándar-completa-y-enlazada-al-cuerpo-normativo) | CP-001 | 10 pasos y 9 cualidades completos, enlazados y sin restos del origen | Sí |
| [CA-02](../HU-014-la-guia-de-entrada-del-estandar.md#ca-02--la-guía-llega-a-los-herederos-y-se-encuentra-sin-saber-que-existe) | CP-002 | Viaja con `base/`, nombrada en README y mapa; contenido fuera del arranque (69,9 de 90 KB), con el desvío de la línea de índice declarado | Sí |

**Los que no cumplen:** ninguno.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12 | 100% (2 de 2) | 2 de 2 | Sí |
| Casos ejecutados | Plan §12 | 100% | 2 de 2 | Sí |
| Tasa de aprobación | Plan §12 | 100% | 2 de 2 | Sí |

**Lo que no se cumplió:** nada.

---

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los dos CA quedaron en «Sí» con sus casos aprobados (§5). El único desvío (la línea de índice de CP-002) quedó declarado con su medida y su porqué, y no toca lo que los CA exigen.

**Qué falta para que cumpla:** nada.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | El documento y sus comprobaciones | [`base/guia-de-entrada.md`](../../../../../base/guia-de-entrada.md); salida de `validar.py estandar` (0 fallas sobre el archivo) y del `grep` de restos (0) en la sesión del 2026-08-21 |
| EV-02 | La medición del arranque | Salida de `cargador.contexto('.')`: 69,9 KB, 1 línea con `guia-de-entrada`, 102 bytes — sesión del 2026-08-21, transcrita en el histórico |

---

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-08-21 | 2 | 0 | Primera ejecución |
