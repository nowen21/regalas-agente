# Plan de Trabajo — Fase A-EP-001-HU-007-retrodocumentar-el-procedimiento-de-la-regla (módulo Cuerpo de reglas)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en [HU-007](../HU-007-regla-de-las-reglas.md); el detalle de las pruebas, en el `plan_pruebas.md` de esta misma fase; lo que dieron al correrlas, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** (identificador · [`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-001-HU-007-retrodocumentar-el-procedimiento-de-la-regla` |
| **Épica** | [EP-001 Cuerpo de reglas heredable y en capas](../../epica.md) |
| **HU** | [HU-007 La regla que gobierna cómo se escriben las reglas](../HU-007-regla-de-las-reglas.md) — una sola (`F12.1`) |
| **Módulo** | Cuerpo de reglas |
| **Especificación del módulo** | [HU-007](../HU-007-regla-de-las-reglas.md). El entregable es texto normativo: sus criterios de aceptación son la especificación |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-001-HU-007-retrodocumentar-el-procedimiento-de-la-regla` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📄 **Retro-documentación** ([`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md)). El procedimiento existe y se usa en cada cambio: el capítulo [`20 · Meta-reglas`](../../../../../base/20-meta-reglas/base.md) trae dieciséis reglas, el molde en [`estructura-regla.md`](../../../../../base/20-meta-reglas/estructura-regla.md) y el [checklist](../../../../../base/20-meta-reglas/checklist.md) de veinte filas. Lo que falta es la cadena que diga con qué plan se escribió y con qué casos se comprueba que enruta, rechaza y parte. Sale de la fila de HU-007 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-007 | Qué exige | Estado hoy, sin haber tocado nada |
|---|---|---|
| [CA-01](../HU-007-regla-de-las-reglas.md#ca-01--una-regla-nueva-se-enruta-al-capítulo-correcto) | Una regla nueva se enruta al capítulo correcto | Exigido por las filas 1 a 4 del checklist, y por [`20·M1`](../../../../../base/20-meta-reglas/reglas/M1-la-jerarquia-tiene-cuatro-niveles-y-un-solo-orden.md), [`20·M2`](../../../../../base/20-meta-reglas/reglas/M2-un-tema-un-capitulo-un-dueno.md) y [`20·M13`](../../../../../base/20-meta-reglas/reglas/M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md). **Sin prueba escrita** |
| [CA-02](../HU-007-regla-de-las-reglas.md#ca-02--una-regla-atada-a-un-stack-no-entra) | Una regla atada a un stack no entra | Exigido por [`20·M3`](../../../../../base/20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md) y la fila 5. El programa que la mira **no se puede correr** |
| [CA-03](../HU-007-regla-de-las-reglas.md#ca-03--una-regla-que-exige-dos-cosas-se-parte-antes-de-entrar) | Una regla que exige dos cosas se parte antes de entrar | Exigido por [`20·M5`](../../../../../base/20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md) y la fila 9, que es de las que **pide leer** | 

**Por qué una sola fase para los tres CA.** Los tres son el mismo procedimiento visto en tres momentos —dónde va, si entra, cómo entra—, y se prueban con el mismo recorrido sobre una regla candidata. Partirlos daría fases que existen para cumplir la nomenclatura (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** dejar probado, con reglas candidatas de verdad, que el procedimiento enruta al capítulo correcto, rechaza lo atado a un stack y parte lo que exige dos cosas — y que esa prueba quede como el caso de referencia para el próximo cambio de reglas.

**Fuera de alcance:**

- **Las 121 reglas sin bloque de checklist y las siete publicadas en «no cumple».** Es el pendiente [19](../../../../../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md), y su parte hecha se cerró en la fase A de [HU-009](../../HU-009-reglas-sin-checklist-al-dia/HU-009-reglas-sin-checklist-al-dia.md). Acá no se abre.
- **Darle punto de entrada a `metareglas.py`.** Pendiente [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md), punto 2.
- **Que el sello del checklist caduque con el texto.** Pendiente [52](../../../../../pendientes/hecho/el-sello-del-checklist-se-comprueba.md).
- **Escribir reglas nuevas.** Las candidatas de la prueba son reglas que ya existen o que ya se rechazaron, no inventos que después haya que borrar.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado contra el repositorio el 2026-08-17: dieciséis archivos de regla en `base/20-meta-reglas/reglas/`, el checklist de veinte filas y el molde.

**Lo que ya existe:**

| Exigencia de la HU | Dónde está hoy | Estado |
|---|---|---|
| RN-01 · antes de crear una regla se busca si ya existe | [`20·M12`](../../../../../base/20-meta-reglas/reglas/M12-antes-de-crear-una-regla-buscar-la-duplicacion-es-el-defecto-mas-caro.md) y la fila 2 | Regla |
| RN-02 · un tema, un capítulo dueño | [`20·M2`](../../../../../base/20-meta-reglas/reglas/M2-un-tema-un-capitulo-un-dueno.md) y la fila 4 | Regla |
| RN-03 · lo atado a un lenguaje o a un cliente no entra | [`20·M3`](../../../../../base/20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md) y la fila 5 | Regla |
| RN-04 · identificador único, estable y sin repetir el prefijo | [`20·M4`](../../../../../base/20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md) y la fila 6 | Regla |
| RN-05 · declara dependencias y excepciones, con quién autoriza | [`20·M7`](../../../../../base/20-meta-reglas/reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md), [`20·M8`](../../../../../base/20-meta-reglas/reglas/M8-la-excepcion-se-escribe-dentro-de-la-regla-que-la-admite.md) y las filas 14 a 16 | Regla |
| RN-06 · se decide y se marca si es comprobable | [`20·M9`](../../../../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md), la fila 18 y el registro [`validadores/reglas-validables.md`](../../../../../validadores/reglas-validables.md) | Regla y registro |
| RN-07 · ninguna regla de proyecto existe sin respaldo en la base | [`20·M16`](../../../../../base/20-meta-reglas/reglas/M16-toda-regla-de-proyecto-nombra-la-regla-de-base-que-concreta.md) | Regla |
| Que ninguna regla nazca fuera del procedimiento | [`20·M14`](../../../../../base/20-meta-reglas/reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md) | Regla |
| El molde, parte por parte | [`estructura-regla.md`](../../../../../base/20-meta-reglas/estructura-regla.md) | Escrito |

**Lo que no existe:**

1. **La prueba del enrutado.** El procedimiento se aplica en cada cambio, pero no hay un caso escrito que muestre una candidata entrando por la puerta correcta y otra siendo devuelta.
2. **La comprobación automática de las filas que un programa puede decidir.** [`validadores/metareglas.py`](../../../../../validadores/metareglas.py) las tiene escritas —filas 5, 6, 7, 10, 12, 13, 14, 15, 18, 19— y hoy **no se puede correr**: sin punto de entrada ni subcomando, termina en silencio con código 0.
3. **El registro de lo rechazado.** Las reglas que se propusieron y no entraron no quedan escritas en ninguna parte, así que el criterio de rechazo no se puede citar.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `documentacion/epicas/EP-001-…/HU-007-…/A-EP-001-HU-007-…/plan_pruebas.md` | Nuevo | Documentación | Los casos de esta fase, con las candidatas |
| `documentacion/epicas/EP-001-…/HU-007-…/A-EP-001-HU-007-…/resultado_pruebas.md` | Nuevo | Documentación | Lo que dieron, y qué quedó sin poder comprobarse |
| `notas/` | Nuevo | Notas | Las candidatas rechazadas y por qué, que es el porqué del procedimiento y no una regla ([`20·M13`](../../../../../base/20-meta-reglas/reglas/M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md)) |
| `documentacion/epicas/EP-001-…/HU-007-…/HU-007-regla-de-las-reglas.md` | Modificar | Documentación | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Documentación | Las casillas de la fila de HU-007 |

> **`base/20-meta-reglas/` no se toca.** La fase prueba el procedimiento; cambiarlo es otra cosa y pasa por el propio procedimiento.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna: no entra ni sale una regla, así que ninguna cita cambia de destino.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque el entregable son archivos de texto del repositorio.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

No aplica. El capítulo `20` llega como índice al abrir la sesión y se abre cuando se va a tocar una regla; el `CLAUDE.md` del repositorio manda al procedimiento en su §2.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Las candidatas de la prueba son reglas que ya pasaron por el procedimiento, y candidatas que ya se rechazaron | Inventar reglas de mentira para probar | Una regla inventada no tiene el defecto real que el procedimiento tiene que atajar, y después hay que borrarla |
| Lo rechazado se escribe en `notas/`, no en `base/` | Dejar una sección de rechazadas dentro del capítulo `20` | `base/` es lo que se exige; por qué algo no entró es razonamiento, y su sitio es `notas/` ([`20·M13`](../../../../../base/20-meta-reglas/reglas/M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md)) |
| Las filas del checklist que un programa podría decidir se corren a mano y se dice que fue a mano | Marcarlas como comprobadas sin decir cómo | El programa no se puede correr, y marcar comprobado lo que nadie corrió es el defecto que este trabajo viene a cerrar |

### 2.7 Dudas por resolver antes de escribir

| # | Duda | A quién se consulta | Estado |
|---|---|---|---|
| 1 | Cuáles candidatas rechazadas se usan como caso — el usuario es quien recuerda las que se propusieron y no entraron | Usuario | **Resuelta el 2026-08-18**, decisión 1 del pendiente 59: el criterio de entrada al núcleo se difiere a esta misma HU, que es la regla de las reglas |

La duda 1 bloquea T-02 y T-05. El resto no depende de ella.

**Decididas el 2026-08-18**, en el [pendiente 59](../../../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md). 👤 marca lo que sigue esperando un dato del usuario.

| Duda | Decisión |
|---|---|
| 16 | **Ya estaba contestada:** las 22 fichas con su salida están en [`prompts/analisis/reglas-2026-08-13-candidatas-a-regla.md`](../../../../../prompts/analisis/reglas-2026-08-13-candidatas-a-regla.md). Diecisiete no entraron. |

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Una regla nueva se enruta al capítulo correcto

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Caso de prueba: una regla de las que ya existen se recorre por las filas 1 a 4 y se comprueba que su capítulo es el dueño del tema | `plan_pruebas.md` | 2,0 |
| T-02 | Caso de prueba: una candidata cuyo destino no era `base/` se devuelve a su sitio, y queda escrito a cuál | `plan_pruebas.md` | 1,5 |

### CA-02 — Una regla atada a un stack no entra

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Caso de prueba: una candidata que nombra lenguaje, framework o herramienta se rechaza por la fila 5, y se comprueba que la versión agnóstica sí pasa | `plan_pruebas.md` | 2,0 |
| T-04 | Dejar escrito que la fila 5 hoy se decide leyendo, porque el programa que la mira no corre, y con qué evidencia | `resultado_pruebas.md` | 1,0 |

### CA-03 — Una regla que exige dos cosas se parte antes de entrar

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-05 | Caso de prueba: una candidata con dos exigencias se parte en dos, y las dos pasan la fila 9 por separado | `plan_pruebas.md` | 2,0 |
| T-06 | Comprobar el criterio de partición con un caso real del propio estándar: `F4` y las reglas que salieron de ella | `plan_pruebas.md` | 1,5 |

### RNF — Que el procedimiento quede citable

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-07 | Escribir en `notas/` las candidatas rechazadas y el motivo de cada una | Trazabilidad | 2,0 |
| T-08 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 8 tareas · 13,5 horas.**

---

## 4. Secuencia de ejecución

T-01, T-03, T-04 y T-06 pueden arrancar de entrada. T-02 y T-05 esperan la duda 1, y T-07 va después de las dos. T-08 cierra.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)). Ninguna regla se edita para que la prueba pase.

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método de verificación | Evidencia |
|---|---|---|
| CA-01 | Recorrido de las filas 1 a 4 sobre una regla existente y sobre una candidata devuelta | Casos de T-01 y T-02 |
| CA-02 | Fila 5 aplicada a una candidata con nombre propio y a su versión agnóstica | Caso de T-03, y la constancia de T-04 |
| CA-03 | Fila 9 aplicada a una candidata doble, antes y después de partirla, y el caso real de `F4` | Casos de T-05 y T-06 |
| RNF | La nota con las candidatas rechazadas, cada una con su motivo | T-07 |

---

## 6. Datos y ambiente de prueba

Este repositorio, en una rama aparte. Las candidatas se escriben en el `plan_pruebas` de la fase, no en `base/`: así ninguna regla de mentira queda suelta en el cuerpo. Ningún dato real y ninguna clave.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase. Nada de lo que entrega cambia comportamiento: son documentos de la fase y una nota. No hay datos que restaurar.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

No aplica: nada cambia en los proyectos que adoptaron el estándar. No hay subida de versión, porque no se toca `base/` ni `plantillas/`.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`13·DOC17`](../../../../../base/13-documentacion/reglas/DOC17-manten-un-readme-en-cada-nivel-del-arbol-de-trabajo.md), [`20·M1`](../../../../../base/20-meta-reglas/reglas/M1-la-jerarquia-tiene-cuatro-niveles-y-un-solo-orden.md), [`20·M2`](../../../../../base/20-meta-reglas/reglas/M2-un-tema-un-capitulo-un-dueno.md), [`20·M3`](../../../../../base/20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md), [`20·M4`](../../../../../base/20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md), [`20·M5`](../../../../../base/20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md), [`20·M7`](../../../../../base/20-meta-reglas/reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md), [`20·M8`](../../../../../base/20-meta-reglas/reglas/M8-la-excepcion-se-escribe-dentro-de-la-regla-que-la-admite.md), [`20·M9`](../../../../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md), [`20·M12`](../../../../../base/20-meta-reglas/reglas/M12-antes-de-crear-una-regla-buscar-la-duplicacion-es-el-defecto-mas-caro.md), [`20·M13`](../../../../../base/20-meta-reglas/reglas/M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md), [`20·M14`](../../../../../base/20-meta-reglas/reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md), [`20·M16`](../../../../../base/20-meta-reglas/reglas/M16-toda-regla-de-proyecto-nombra-la-regla-de-base-que-concreta.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | La duda 1 sin resolver | Bloquea dos casos de tres CA | Recuperar con el usuario qué candidatas se rechazaron | Abierto |
| R-01 | Que al recorrer el checklist sobre una regla existente aparezca que reprueba | Se destapa trabajo del pendiente [19](../../../../../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md) | Se anota como evidencia y se suma al 19; corregir la regla no es de esta fase | Abierto |
| R-02 | Que la prueba se lea como que el procedimiento ya está comprobado por un programa | Falsa confianza | El resultado dice, fila por fila, cuál se decidió leyendo y cuál no se pudo correr | Abierto |
| R-03 | Que las candidatas rechazadas no se recuerden | El CA-02 y el CA-03 quedarían probados solo con casos armados | Se admite y se dice: el caso armado se marca como tal en el `plan_pruebas` | Abierto |

---

## 11. Definition of Done

- [ ] Los tres CA tienen su caso escrito y corrido, con lo que dio.
- [ ] Cada fila del checklist usada en la prueba dice si la decidió una persona o un programa.
- [ ] Las candidatas rechazadas están escritas en `notas/` con su motivo.
- [ ] Ninguna regla de mentira quedó suelta en `base/`.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila de HU-007 del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase. Este plan se queda como se aprobó, para poder comparar lo que se dijo contra lo que pasó.
