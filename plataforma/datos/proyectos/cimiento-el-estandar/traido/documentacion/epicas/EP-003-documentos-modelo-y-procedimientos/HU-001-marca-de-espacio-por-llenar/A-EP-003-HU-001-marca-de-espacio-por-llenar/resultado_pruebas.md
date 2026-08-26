# Resultado de pruebas — Fase A-EP-003-HU-001-marca-de-espacio-por-llenar

**Para qué sirve este documento.** Dice **qué se ejecutó y cuánto dio**. El plan de pruebas no se toca al correrlo: la línea base aprobada se queda como está y lo que pasó se escribe acá. Sin este documento, un criterio de aceptación no se puede dar por cumplido.

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-003-HU-001-marca-de-espacio-por-llenar` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md) · PP-A-EP-003-HU-001 v1.0 |
| **Fecha de ejecución** | 2026-08-14 |
| **Ejecutado por** | El agente, con el usuario aprobando el plan y sus dos ampliaciones |

---

## 1. Línea base antes de ejecutar

Medido el 2026-08-14, antes de tocar nada:

| Medida | Valor de partida |
|---|---|
| Archivos en `plantillas/` | 30 |
| Archivos que usan `«…»` | 25 |
| Archivos que **además** usan corchetes como hueco | 11, con 179 huecos |
| Archivos con huecos en `<texto>` | 2 |
| Regla que exija una marca | Ninguna |

---

## 2. Casos ejecutados

| Caso | CA | Con qué se probó | Veredicto | Evidencia |
|---|---|---|---|---|
| [CP-001](plan_pruebas.md#cp-001--la-marca-se-ve-sin-buscarla) | [CA-01](../HU-001-marca-de-espacio-por-llenar.md#ca-01--la-marca-se-ve-y-se-distingue-del-texto) | `plantillas/ciclo-vida-proyectos/04-HU.md`, `plantillas/ciclo-vida-proyectos/03-epica.md` y `plantillas/senales.md` | Cumple | Recuento a ojo y con `grep`: el mismo número |
| [CP-002](plan_pruebas.md#cp-002--todo-modelo-usa-la-misma-marca) | [CA-02](../HU-001-marca-de-espacio-por-llenar.md#ca-02--todos-los-modelos-usan-la-misma-marca) | Los 30 archivos de `plantillas/`, incluidos `planes/`, `prompts/` y `CLAUDE.md.plantilla` | Cumple | 26 de 30 con marca; los 4 sin marca son los declarados en la nota |
| [CP-003](plan_pruebas.md#cp-003--no-sobrevive-ninguna-marca-de-las-descartadas) | [CA-02](../HU-001-marca-de-espacio-por-llenar.md#ca-02--todos-los-modelos-usan-la-misma-marca) | Las cuatro descartadas, buscadas una por una: `[texto]`, `<texto>`, `{{texto}}` y `XXX` | Cumple | Ningún acierto es un hueco. El de `ADR.md` es DEF-03 |
| [CP-004](plan_pruebas.md#cp-004--un-documento-con-marcas-sin-llenar-no-está-terminado) | [CA-03](../HU-001-marca-de-espacio-por-llenar.md#ca-03--un-documento-con-marcas-sin-llenar-no-se-da-por-terminado) | Cumple | [`DOC20`](../../../../../base/13-documentacion/reglas/DOC20-no-entregues-como-terminado-un-documento-con-marcas.md) y [`DOC21`](../../../../../base/13-documentacion/reglas/DOC21-escribe-n-a-en-la-seccion-que-no-aplica.md) escritas, con su ejemplo y su checklist en CUMPLE |
| [CP-005](plan_pruebas.md#cp-005--la-marca-no-estorba-la-lectura-ni-rompe-la-corrida) | [RNF-01](../HU-001-marca-de-espacio-por-llenar.md#5-requisitos-no-funcionales) | `python validadores/validar.py estandar` sobre este repositorio | Cumple | 0 fallas y 2 avisos, los mismos de antes de la fase |

**Detalle de CP-001.** Se abrieron `plantillas/ciclo-vida-proyectos/04-HU.md`, `plantillas/ciclo-vida-proyectos/03-epica.md` y `plantillas/senales.md` y se recorrieron de arriba abajo una vez. Los huecos se pudieron señalar sin volver atrás. Después se contaron a ojo y con `grep -c "«"`: el mismo número en las tres.

**Detalle de CP-002.** Los cuatro archivos sin marca son [`historico-chat.md`](../../../../../plantillas/historico-chat.md), [`memoria.md`](../../../../../plantillas/memoria.md), [`retrodocumentacion.md`](../../../../../base/13-documentacion/retrodocumentacion.md) y [`prompts/prompt-base-usuario.md`](../../../../../plantillas/prompts/prompt-base-usuario.md). Ninguno es un modelo que alguien llene: los tres primeros son procedimientos y explicaciones, y el motivo quedó escrito en [`notas/marca-del-espacio-por-llenar.md`](../../../../../notas/marca-del-espacio-por-llenar.md). El cuarto es el molde con que el usuario pide trabajo, y se llena escribiendo, no reemplazando huecos.

**Detalle de CP-003.** Se buscaron las cuatro marcas descartadas en `plantillas/`. `{{` y `XXX` dieron un solo acierto, el `«ADR-XXX»` de `ADR.md`, que va dentro de la marca. Los aciertos de corchete resultaron ser enlaces de markdown, casillas `[ ]` y bloques de guía `[[…]]`; los de `<>`, sintaxis de comandos. Ninguno era un hueco del modelo.

**Detalle de CP-004.** Se llenó una copia de `plantillas/senales.md` dejando dos `«…»` a propósito y se presentó como terminada. Con `13·DOC20` escrita, la respuesta es que no lo está, y se pueden señalar las dos. Reemplazándolas, sí. Dejando una sección con la marca en vez de `N/A`, sigue sin estar terminada, que es lo que agrega `13·DOC21`.

**Detalle de CP-005.** La corrida quedó en **0 fallas y 2 avisos**. Los dos avisos venían de antes de la fase: una cita de `G1` en `base/09-git.md` y otra de `G9` en `base/20-meta-reglas/estructura-regla.md`. Ninguno nace de este trabajo, así que la métrica de fallas nuevas da 0.

---

## 3. Defectos encontrados

| ID | Título | Caso | Severidad | Estado |
|---|---|---|---|---|
| DEF-01 | El primer barrido convirtió también los bloques de guía `[[…]]` de `plantilla-especificacion-modulo.md` y de `senales.md`, que no son huecos sino instrucciones que se borran al llenar | [CP-002](plan_pruebas.md#cp-002--todo-modelo-usa-la-misma-marca) | Media | Corregido en la misma fase: 14 bloques restaurados |
| DEF-02 | El mismo barrido dejó una marca anidada, `«HU-«NNN»»`, en `planes/resultados.md` | [CP-002](plan_pruebas.md#cp-002--todo-modelo-usa-la-misma-marca) | Baja | Corregido |
| DEF-03 | `ADR.md` usa `«ADR-XXX»`. El `XXX` es una de las marcas descartadas, pero acá va **dentro** de la marca, como texto que describe el hueco | [CP-003](plan_pruebas.md#cp-003--no-sobrevive-ninguna-marca-de-las-descartadas) | Baja | Aceptado sin cambio: cumple [`DOC19`](../../../../../base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md). Queda anotado por si se prefiere `«ADR-NNN»` |

Los dos primeros los encontró la propia verificación de CP-002, no una revisión posterior. Es lo que se buscaba al pedir dos recuentos independientes.

---

## 4. Métricas

| Métrica | Meta | Obtenido |
|---|---|---|
| Cobertura de criterios | 100% | 100%: 6 de 6 con caso ejecutado |
| Plantillas con una sola marca | 100% | 100%: 26 de 26 con huecos. Las otras 4 no tienen |
| Marcas descartadas sobrevivientes | 0 | 0 como marca. 1 como texto dentro de una marca (DEF-03) |
| Fallas nuevas en la corrida del estándar | 0 | 0 |
| Huecos convertidos | — | 179 en 11 archivos, más los de `epica.md` y `marco-normativo.md` |
| Marcas en el catálogo, al cerrar | — | 611 en 30 archivos |

---

## 5. Verificación por criterio de aceptación

| CA | Veredicto | De dónde sale |
|---|---|---|
| [CA-01](../HU-001-marca-de-espacio-por-llenar.md#ca-01--la-marca-se-ve-y-se-distingue-del-texto) · la marca se ve y se distingue | **Cumple** | CP-001 |
| [CA-02](../HU-001-marca-de-espacio-por-llenar.md#ca-02--todos-los-modelos-usan-la-misma-marca) · todos los modelos usan la misma | **Cumple** | CP-002 y CP-003 |
| [CA-03](../HU-001-marca-de-espacio-por-llenar.md#ca-03--un-documento-con-marcas-sin-llenar-no-se-da-por-terminado) · con marcas no está terminado | **Cumple** | CP-004 |
| [RNF-01](../HU-001-marca-de-espacio-por-llenar.md#5-requisitos-no-funcionales) · no estorba la lectura | **Cumple** | CP-005 |
| [RNF-02](../HU-001-marca-de-espacio-por-llenar.md#5-requisitos-no-funcionales) · un programa la encuentra sin falsos positivos | **Cumple** | CP-003 |
| [RNF-03](../HU-001-marca-de-espacio-por-llenar.md#5-requisitos-no-funcionales) · una sola marca en el catálogo | **Cumple** | CP-002 |

---

## 6. Concepto final

**Cumple.** Los tres criterios de aceptación y los tres requisitos no funcionales quedaron verificados, con un defecto aceptado y anotado (DEF-03) que no toca ningún criterio.

Lo que falta para cerrar la fase no es prueba: es la aprobación del usuario y el commit.
