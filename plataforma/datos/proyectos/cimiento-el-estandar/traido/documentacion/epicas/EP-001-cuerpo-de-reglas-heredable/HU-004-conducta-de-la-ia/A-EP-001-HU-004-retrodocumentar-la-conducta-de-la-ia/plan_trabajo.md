# Plan de Trabajo — Fase A-EP-001-HU-004-retrodocumentar-la-conducta-de-la-ia (módulo Cuerpo de reglas)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en [HU-004](../HU-004-conducta-de-la-ia.md); el detalle de las pruebas, en el `plan_pruebas.md` de esta misma fase; lo que dieron al correrlas, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** (identificador · [`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-001-HU-004-retrodocumentar-la-conducta-de-la-ia` |
| **Épica** | [EP-001 Cuerpo de reglas heredable y en capas](../../epica.md) |
| **HU** | [HU-004 Reglas de conducta de la IA](../HU-004-conducta-de-la-ia.md) — una sola (`F12.1`) |
| **Módulo** | Cuerpo de reglas |
| **Especificación del módulo** | [HU-004](../HU-004-conducta-de-la-ia.md). El entregable es texto normativo: sus criterios de aceptación son la especificación |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-001-HU-004-retrodocumentar-la-conducta-de-la-ia` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 🔀 **Híbrido.** 📄 Retro-documenta lo que ya manda ([`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md)): el capítulo [`01 · Conducta`](../../../../../base/01-conducta.md) trae veintidós reglas y el capítulo [`00 · Identidad y rol`](../../../../../base/00-identidad-y-rol/base.md) trae nueve. ✨ Y construye lo que falta: dos de las tres exigencias de la HU **no son regla del estándar**, viven solo como preferencia del usuario en [`historico-chat/memory/`](../../../../../historico-chat/memory/memory.md). Sale de la fila de HU-004 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-004 | Qué exige | Estado hoy, sin haber tocado nada |
|---|---|---|
| [CA-01](../HU-004-conducta-de-la-ia.md#ca-01--una-pregunta-se-responde-no-se-ejecuta) | Una pregunta se responde, no se ejecuta | **No es regla.** Está en el recuerdo [`pregunta-no-es-instruccion.md`](../../../../../historico-chat/memory/pregunta-no-es-instruccion.md), que rige la sesión pero no viaja a un proyecto heredero |
| [CA-02](../HU-004-conducta-de-la-ia.md#ca-02--lo-que-se-detecta-mal-se-corrige-sin-preguntar) | Lo que se detecta mal se corrige sin preguntar | **No es regla.** Está en el recuerdo [`corregir-el-defecto-que-uno-mismo-detecta.md`](../../../../../historico-chat/memory/corregir-el-defecto-que-uno-mismo-detecta.md) |
| [CA-03](../HU-004-conducta-de-la-ia.md#ca-03--lo-entregado-no-se-lee-como-escrito-por-una-máquina) | Lo entregado no se lee como escrito por una máquina | La regla está: [`00·ID8`](../../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) y su lista en [`marcadores-de-ia.md`](../../../../../base/00-identidad-y-rol/marcadores-de-ia.md). **Sin prueba y sin comprobación automática** |

**Por qué una sola fase para los tres CA.** Los tres tratan del mismo cuerpo de texto —la conducta— y los dos primeros son el mismo movimiento repetido: subir un recuerdo a regla. Partirlos daría fases que existen para cumplir la nomenclatura (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** que las tres exigencias de conducta de la HU sean regla del estándar, con su prueba y su resultado escritos, y que ninguna dependa de que el agente se acuerde.

**Fuera de alcance:**

- **Reescribir las veintidós reglas del capítulo `01`.** Se leen para no duplicar, no para corregirlas.
- **Limpiar los marcadores de IA que ya tiene escrito el estándar.** Está anotado en el pendiente [11](../../../../../pendientes/hecho/limpiar-marcadores-de-ia-del-texto-del-estandar.md) y es trabajo aparte.
- **Comprobar con un programa que un texto tiene marcadores de IA.** Sería de EP-004 y hoy no existe ningún validador que lo mire; esta fase lo deja dicho, no lo construye.
- **Vaciar los dos recuerdos.** Suban o no a regla, el recuerdo se queda: dice cómo lo quiere el usuario en este repositorio, y eso no es lo mismo que la regla que heredan los proyectos.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado contra el repositorio el 2026-08-17, leyendo los capítulos y buscando en todo el árbol.

**Lo que ya existe:**

| Exigencia de la HU | Dónde está hoy | Estado |
|---|---|---|
| RN-01 · criterio de alguien con experiencia, y recomienda con el motivo | [`00·ID1`](../../../../../base/00-identidad-y-rol/reglas/ID1-trabaja-con-criterio-de-desarrollador-senior.md) y `01·C14` | Regla |
| RN-04 · escribe en el idioma del proyecto y para quien no sabe del tema | `01·C8`, `01·C20` y [`00·ID7`](../../../../../base/00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md) | Regla |
| RN-05 · nada que se lea como escrito por una máquina | [`00·ID8`](../../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) y [`marcadores-de-ia.md`](../../../../../base/00-identidad-y-rol/marcadores-de-ia.md) | Regla |
| RN-06 · dice lo que no sabe y lo que no pudo hacer | `01·C9` y [`00·ID3`](../../../../../base/00-identidad-y-rol/reglas/ID3-no-des-por-entregado-lo-que-no-esta-terminado.md) | Regla |
| RN-07 · lo que el usuario quiere recordado va donde se pueda revisar | `01·C19`, y [`validadores/hook_recuerdos.py`](../../../../../validadores/hook_recuerdos.py) lo mueve solo | Regla y programa |
| Que el capítulo llegue puesto al abrir la sesión | [`validadores/cargador.py`](../../../../../validadores/cargador.py) manda completo lo que empieza por `00-` y `01-` | Corriendo |

**Lo que no existe:**

1. **RN-02 · la pregunta no es una orden.** Buscado en todo `base/`: no hay regla que lo diga. Lo sostiene un recuerdo, y un recuerdo de este repositorio no viaja a un proyecto heredero.
2. **RN-03 · lo que se detecta mal se arregla.** Igual: recuerdo, no regla. Y con un límite que el recuerdo sí precisa —vale mientras se ejecuta algo ya autorizado— que hay que conservar al subirlo, o la regla contradiría [`00·N1`](../../../../../base/00-nucleo-blindado.md).
3. **La prueba de las tres.** Ninguna de las tres exigencias tiene caso escrito ni resultado registrado.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `base/01-conducta.md` | Modificar | Cuerpo de reglas | Entran las dos reglas que faltan, con el identificador libre que siga a `C22` |
| `validadores/reglas-validables.md` | Modificar | Comprobación | Cada regla nueva declara si es comprobable ([`20·M9`](../../../../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md)) |
| `documentacion/epicas/EP-001-…/HU-004-…/A-EP-001-HU-004-…/plan_pruebas.md` | Nuevo | Documentación | Los casos de esta fase |
| `documentacion/epicas/EP-001-…/HU-004-…/A-EP-001-HU-004-…/resultado_pruebas.md` | Nuevo | Documentación | Lo que dieron |
| `documentacion/epicas/EP-001-…/HU-004-…/HU-004-conducta-de-la-ia.md` | Modificar | Documentación | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `historico-chat/memory/pregunta-no-es-instruccion.md` · `corregir-el-defecto-que-uno-mismo-detecta.md` | Modificar | Memoria | Cada uno nombra la regla en que quedó, para que no queden dos versiones del mismo mandato |
| `pendientes/48-inventario-hu.md` | Modificar | Documentación | Las casillas de la fila de HU-004 |
| `CHANGELOG.md` · `VERSION` | Modificar | Versionado | Dos reglas nuevas: sube **MENOR** ([`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)) |

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna: las dos reglas nuevas se agregan al final del capítulo con identificador libre, así que ninguna cita existente cambia de destino. Los dos recuerdos que se editan no son citados por ninguna regla.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque el entregable son archivos de texto del repositorio.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

No aplica. Lo que entrega llega puesto al abrir la sesión, por el cargador, y el capítulo `01` viaja completo.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Las dos exigencias suben a regla del capítulo `01`, y el recuerdo se queda apuntando a ellas | Dejarlas solo como recuerdo | Un recuerdo de este repositorio no viaja: un proyecto heredero recibe `base/`, no `historico-chat/`. Si la exigencia es para cualquier proyecto, es regla ([`20·M13`](../../../../../base/20-meta-reglas/reglas/M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md)) |
| La regla de corregir el defecto conserva el límite del recuerdo: vale mientras se ejecuta algo ya autorizado | Escribirla sin límite | Sin el límite le pasaría por encima a [`00·N1`](../../../../../base/00-nucleo-blindado.md), y ninguna regla normal manda sobre una `[BLINDADA]` |
| Se agregan al final, con el identificador que siga a `C22` | Insertarlas por tema y recorrer la numeración | [`20·M4`](../../../../../base/20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md): el identificador es estable, y renumerar rompe toda cita hecha |
| El CA-03 se cierra con prueba leída, no con programa | Escribir el validador de marcadores de IA en esta fase | Comprobar es EP-004, y esta fase no construye validadores |

### 2.7 Dudas por resolver antes de escribir

| # | Duda | A quién se consulta | Estado |
|---|---|---|---|
| 1 | Si las dos exigencias suben a regla del capítulo `01` — es cambio de `base/` y lo decide el usuario | Usuario | **Resuelta el 2026-08-18**, decisiones 2 y 3 del pendiente 59: las dos exigencias suben al capítulo `01`, y el recuerdo se recorta a un puntero |
| 2 | Si al subirlas, el recuerdo se queda con su texto o se recorta a un puntero a la regla | Usuario | **Resuelta el 2026-08-18**, decisiones 2 y 3 del pendiente 59: las dos exigencias suben al capítulo `01`, y el recuerdo se recorta a un puntero |

La duda 1 bloquea T-01 y T-04. El CA-03 no depende de ninguna de las dos.

**Decididas el 2026-08-18**, en el [pendiente 59](../../../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md). 👤 marca lo que sigue esperando un dato del usuario.

| Duda | Decisión |
|---|---|
| 2 | **Sí suben** al capítulo `01`: le exigen algo al agente en cualquier proyecto. |
| 3 | **El recuerdo se recorta a un puntero.** Si la exigencia vive en `base/`, repetirla es texto prestado (fila 11). |

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Una pregunta se responde, no se ejecuta

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Escribir la regla con el molde de [`20·M5`](../../../../../base/20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md), recorriendo el procedimiento de [`20·M14`](../../../../../base/20-meta-reglas/reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md) | `base/01-conducta.md` | 2,0 |
| T-02 | Caso de prueba: una pregunta que suena a orden se responde sin tocar nada, y el archivo del que se pregunta queda igual | `plan_pruebas.md` | 1,5 |
| T-03 | Dejar el recuerdo apuntando a la regla nueva | `historico-chat/memory/pregunta-no-es-instruccion.md` | 0,5 |

### CA-02 — Lo que se detecta mal se corrige sin preguntar

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-04 | Escribir la regla con su límite: vale mientras se ejecuta algo ya autorizado | `base/01-conducta.md` | 2,0 |
| T-05 | Caso de prueba: dentro de un trabajo aprobado, el defecto detectado se arregla sin preguntar; fuera de él, se para y se propone | `plan_pruebas.md` | 1,5 |
| T-06 | Dejar el recuerdo apuntando a la regla nueva | `historico-chat/memory/corregir-el-defecto-que-uno-mismo-detecta.md` | 0,5 |

### CA-03 — Lo entregado no se lee como escrito por una máquina

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-07 | Caso de prueba: revisar un documento entregado contra la lista de [`marcadores-de-ia.md`](../../../../../base/00-identidad-y-rol/marcadores-de-ia.md) y comprobar que no aparece ninguno | `plan_pruebas.md` | 1,5 |
| T-08 | Dejar escrito que hoy nadie lo comprueba con un programa, y atarlo al pendiente [11](../../../../../pendientes/hecho/limpiar-marcadores-de-ia-del-texto-del-estandar.md) | `resultado_pruebas.md` | 1,0 |

### RNF — Que la conducta se pueda revisar y no se contradiga

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-09 | Clasificar las dos reglas nuevas en `validadores/reglas-validables.md` y aplicarles a mano el [checklist del estándar](../../../../../base/20-meta-reglas/checklist.md), sus veinte filas | Comprobabilidad | 1,5 |
| T-10 | Correr las pruebas, escribir el resultado, versionar y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 10 tareas · 13,5 horas.**

---

## 4. Secuencia de ejecución

T-07 y T-08 se pueden hacer de entrada: no dependen de ninguna duda. T-01 y T-04 arrancan resuelta la duda 1; T-02 y T-05 van detrás de la regla que prueban; T-03 y T-06 detrás de la duda 2; T-09 y T-10 cierran.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)). Descubrir uno nuevo → parar, reportar, ampliar el plan con el visto bueno.

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método de verificación | Evidencia |
|---|---|---|
| CA-01 | Se hace una pregunta redactada como orden y se revisa que nada se haya escrito | Caso de T-02 |
| CA-02 | Se provoca un defecto dentro de un trabajo aprobado y otro fuera, y se comparan las dos conductas | Caso de T-05 |
| CA-03 | Se revisa un documento entregado contra la lista de marcadores | Caso de T-07, y la constancia de T-08 |
| RNF | Las dos reglas nuevas están clasificadas en `reglas-validables.md` y traen su bloque de checklist con el resultado y la versión contra la que se aplicó | T-09 |

---

## 6. Datos y ambiente de prueba

Este repositorio y una carpeta temporal para el caso del CA-01, donde el archivo que se toca es de mentira. Ningún dato real y ninguna clave.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase. Deshacerlo saca las dos reglas nuevas y devuelve los recuerdos a su texto anterior; no hay datos que restaurar. `VERSION` vuelve con el mismo revert, porque va en el mismo commit.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

Se asume que el estándar está en producción. El cambio es **aditivo**: dos reglas nuevas al final de un capítulo que ya viaja. Un proyecto que no se actualice sigue sin ellas, y `validar.py versiones` le avisa que quedó atrás. Nada obliga a un proyecto al día a hacer algo distinto de lo que ya hacía, así que la subida es **MENOR**.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`00·N1`](../../../../../base/00-nucleo-blindado.md), [`00·ID3`](../../../../../base/00-identidad-y-rol/reglas/ID3-no-des-por-entregado-lo-que-no-esta-terminado.md), [`00·ID8`](../../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md), [`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`20·M4`](../../../../../base/20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md), [`20·M5`](../../../../../base/20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md), [`20·M9`](../../../../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md), [`20·M13`](../../../../../base/20-meta-reglas/reglas/M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md), [`20·M14`](../../../../../base/20-meta-reglas/reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | La duda 1 sin resolver | Bloquea T-01 y T-04, que son el corazón de la fase | Resolverla antes de tocar `base/` | Abierto |
| R-01 | Que la regla de corregir sin preguntar se lea como permiso para tocar sin aprobación | Choca con el núcleo | El límite va en el cuerpo de la regla, no en una nota al pie | Abierto |
| R-02 | Que las dos exigencias ya estén dichas dentro de alguna de las veintidós y no se vea | Regla duplicada, el defecto más caro ([`20·M12`](../../../../../base/20-meta-reglas/reglas/M12-antes-de-crear-una-regla-buscar-la-duplicacion-es-el-defecto-mas-caro.md)) | Releer el capítulo completo antes de escribir, y dejar en el resultado qué se descartó por parecido | Abierto |
| R-03 | Que probar conducta dependa de leer una respuesta, y eso no lo cierra un programa | El CA queda con evidencia leída, no medida | Se acepta y se dice: la conducta se prueba pidiéndole a la IA justo lo que no debe hacer | Abierto |

---

## 11. Definition of Done

- [ ] Las tres exigencias de la HU son regla del estándar.
- [ ] Cada una tiene su caso escrito y corrido, con lo que dio.
- [ ] Ningún recuerdo repite el texto de la regla en que quedó.
- [ ] Las dos reglas nuevas están clasificadas y pasan su checklist.
- [ ] `CHANGELOG.md` con su entrada y `VERSION` subida.
- [ ] §7 de la HU nombra esta fase, y la fila de HU-004 del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase. Este plan se queda como se aprobó, para poder comparar lo que se dijo contra lo que pasó.
