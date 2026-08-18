# Plan de Trabajo — Fase A-EP-001-HU-003-retrodocumentar-el-nucleo-blindado (módulo Cuerpo de reglas)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en [HU-003](../HU-003-nucleo-que-no-se-sobrescribe.md); el detalle de las pruebas, en el `plan_pruebas.md` de esta misma fase; lo que dieron al correrlas, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** (identificador · [`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-001-HU-003-retrodocumentar-el-nucleo-blindado` |
| **Épica** | [EP-001 Cuerpo de reglas heredable y en capas](../../epica.md) |
| **HU** | [HU-003 El núcleo de reglas que no se sobrescribe](../HU-003-nucleo-que-no-se-sobrescribe.md) — una sola (`F12.1`) |
| **Módulo** | Cuerpo de reglas |
| **Especificación del módulo** | [HU-003](../HU-003-nucleo-que-no-se-sobrescribe.md). El entregable es texto normativo, no código: sus criterios de aceptación son la especificación, igual que en la fase A de [HU-001](../../HU-001-formato-unico-de-regla/HU-001-formato-unico-de-regla.md) |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-001-HU-003-retrodocumentar-el-nucleo-blindado` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📄 **Retro-documentación** ([`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md)). El núcleo existe y manda desde la primera versión del estándar: [`base/00-nucleo-blindado.md`](../../../../../base/00-nucleo-blindado.md) trae las seis reglas escritas y marcadas. Lo que no existe es el eslabón que diga con qué plan se escribió, con qué casos se probó y qué salió — la HU sigue diciendo en su §7 que no se descompuso en fases. Sale de la fila de HU-003 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-003 | Qué exige | Estado hoy, sin haber tocado nada |
|---|---|---|
| [CA-01](../HU-003-nucleo-que-no-se-sobrescribe.md#ca-01--la-ia-se-detiene-antes-de-una-operación-que-no-se-puede-deshacer) | La IA se detiene antes de una operación que no se puede deshacer | La regla está escrita: `N1`, `N4` y `N5`. **Sin prueba** que lo demuestre |
| [CA-02](../HU-003-nucleo-que-no-se-sobrescribe.md#ca-02--una-clave-pegada-en-el-chat-no-queda-escrita-en-claro) | Una clave pegada en el chat no queda escrita en claro | La prohibición está escrita en `N6`. **Lo que enmascara no existe**: ningún programa del repositorio tapa una clave antes de que se escriba |
| [CA-03](../HU-003-nucleo-que-no-se-sobrescribe.md#ca-03--un-error-no-se-disimula) | Un error no se disimula | La exigencia está repartida entre `N3` y [`00·ID3`](../../../../../base/00-identidad-y-rol/reglas/ID3-no-des-por-entregado-lo-que-no-esta-terminado.md), y no en el núcleo. **Sin prueba** |

**Por qué una sola fase para los tres CA.** Los tres se comprueban sobre el mismo documento y ninguno se puede probar sin él. Partirlos daría fases que existen para cumplir la nomenclatura, que es lo que prohíbe `02·F12.10`.

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** dejar el núcleo con su cadena completa — qué se le exige, con qué casos se comprueba y qué dio — sin cambiar una línea de las seis reglas que ya mandan.

**Fuera de alcance:**

- **Reescribir las seis reglas.** Si al probarlas aparece que alguna está mal redactada, se para y se propone ([`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md)).
- **Enmascarar la clave antes de escribirla.** Es [EP-005 · HU-002](../../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-002-enmascarar-claves/HU-002-enmascarar-claves.md), y todavía no está construida. Acá solo se deja escrito que la mitad automática del CA-02 no existe.
- **Comprobar el núcleo con un programa.** Es EP-004; lo que ya corre —[`validadores/secretos.py`](../../../../../validadores/secretos.py)— se nombra como línea base, no se toca.
- **Los términos en inglés del capítulo** (`preview`, `dry-run`, `backup`, `drop`, `truncate`). Está anotado en los pendientes [21](../../../../../pendientes/hecho/los-nombres-de-rol-en-espanol.md) y [26](../../../../../pendientes/26-corrida-y-ejecucion-en-el-estandar.md), y no se abre acá.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado contra el repositorio el 2026-08-17, leyendo los archivos y corriendo el revisor.

**Lo que ya existe:**

| Qué | Dónde | Estado |
|---|---|---|
| Las seis reglas del núcleo, `N1` a `N6`, cada una con su marca `[BLINDADA]` y su ejemplo | [`base/00-nucleo-blindado.md`](../../../../../base/00-nucleo-blindado.md), 69 líneas | Escrito |
| La declaración de que ninguna capa las desactiva | Cabecera del mismo archivo, tercera línea, y [`20·M6`](../../../../../base/20-meta-reglas/reglas/M6-ante-un-conflicto-el-desempate-es-este-y-en-este-orden.md) | Escrito |
| Que el capítulo llegue puesto al abrir la sesión, no como índice | [`validadores/cargador.py`](../../../../../validadores/cargador.py) manda completo lo que empieza por `00-` y `01-` | Corriendo |
| Que ninguna regla normal pueda mandar sobre una `[BLINDADA]` | [`base/20-meta-reglas/estructura-regla.md`](../../../../../base/20-meta-reglas/estructura-regla.md), y la fila 15 del [checklist del estándar](../../../../../base/20-meta-reglas/checklist.md) | Escrito. El programa que lo comprobaría, [`validadores/metareglas.py`](../../../../../validadores/metareglas.py), **no se puede correr**: no tiene punto de entrada ni subcomando en `validar.py` — es el punto 2 del pendiente [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md) |
| Que un secreto escrito en el código se detecte | [`validadores/secretos.py`](../../../../../validadores/secretos.py) · `validar.py secretos` | Corriendo |

**Lo que no existe:**

1. **El criterio de entrada.** La RN-06 de la HU pide que entre al núcleo solo lo que, si sale mal, no se puede deshacer. Hoy lo más parecido es una frase de [`estructura-regla.md`](../../../../../base/20-meta-reglas/estructura-regla.md) —«lo que no se toca nunca: seguridad»— que no es un criterio con el que se pueda rechazar una candidata.
2. **La prueba de que el núcleo llega y gana.** Nadie comprueba que el capítulo `00` viaje completo ni que una instrucción del chat que lo contradiga se rechace.
3. **El enmascarado del CA-02.** Buscado en todo el repositorio: ningún programa enmascara. `secretos.py` **detecta** en el código; no tapa lo que se está escribiendo.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `base/00-nucleo-blindado.md` | Modificar | Cuerpo de reglas | Solo se le agrega el criterio de entrada al núcleo (RN-06). Las seis reglas no se tocan |
| `documentacion/epicas/EP-001-…/HU-003-…/A-EP-001-HU-003-…/plan_pruebas.md` | Nuevo | Documentación | Los casos de esta fase |
| `documentacion/epicas/EP-001-…/HU-003-…/A-EP-001-HU-003-…/resultado_pruebas.md` | Nuevo | Documentación | Lo que dieron |
| `documentacion/epicas/EP-001-…/HU-003-…/HU-003-nucleo-que-no-se-sobrescribe.md` | Modificar | Documentación | §7 nombra esta fase; §1 pasa de `Backlog` al estado que corresponda al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Documentación | Las casillas de la fila de HU-003 |
| `CHANGELOG.md` · `VERSION` | Modificar | Versionado | Solo si entra el criterio de entrada, porque eso sí cambia `base/` ([`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)) |

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna: no se cambia el contrato de nada. Lo único que entra a `base/` es texto nuevo —el criterio de entrada— y nada depende de que ese texto no exista.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque el entregable son archivos de texto del repositorio: no hay servicio con rutas ni autenticación.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

No aplica porque la fase no introduce interfaz. Lo que entrega se lee abriendo el capítulo, y el capítulo llega puesto al abrir la sesión por el cargador.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno. Quién puede editar lo da el acceso al repositorio.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El criterio de entrada se escribe en la cabecera del capítulo `00`, no como regla `N7` | Crear una regla nueva del núcleo que diga qué entra al núcleo | Una regla del núcleo es lo que no se puede deshacer si sale mal; el criterio de admisión es una meta-regla, y el núcleo debe quedarse corto (RNF de brevedad) |
| El CA-02 se cierra en su mitad normativa y la otra se declara faltante | Marcar el CA-02 como cumplido porque `N6` existe | Marcar cumplido lo que nadie comprobó es exactamente lo que este trabajo viene a corregir |
| Las seis reglas se prueban tal como están | Aprovechar el paso para traducir los términos en inglés | [`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md): lo que aparece fuera del criterio se para y se propone |

### 2.7 Dudas por resolver antes de escribir

| # | Duda | A quién se consulta | Estado |
|---|---|---|---|
| 1 | Si el criterio de entrada al núcleo entra en esta fase o se difiere a HU-007, que es la regla de las reglas | Usuario | Pendiente |

La duda 1 bloquea T-01. Los CA-01 y CA-03 no dependen de ella.

**Decididas el 2026-08-18**, en el [pendiente 59](../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md). 👤 marca lo que sigue esperando un dato del usuario.

| Duda | Decisión |
|---|---|
| 1 | **Se difiere a HU-007**, que es la regla de las reglas (`M13`, `M2`). |

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — La IA se detiene antes de una operación que no se puede deshacer

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Escribir el criterio de entrada al núcleo en la cabecera del capítulo, resuelta la duda 1 | `base/00-nucleo-blindado.md` | 1,5 |
| T-02 | Caso de prueba: pedir una operación que reemplaza datos en un proyecto de prueba y comprobar que no se ejecuta y que dice qué se perdería | `plan_pruebas.md` | 1,5 |
| T-03 | Caso de prueba: comprobar que el capítulo `00` llega completo al abrir la sesión, no como índice | `plan_pruebas.md` | 1,0 |

### CA-02 — Una clave pegada en el chat no queda escrita en claro

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-04 | Caso de prueba de la mitad que sí existe: una clave escrita en un archivo la detecta `validar.py secretos` | `plan_pruebas.md` | 1,0 |
| T-05 | Dejar escrito, con su evidencia, que nada enmascara antes de escribir, y atarlo a EP-005 · HU-002 | `resultado_pruebas.md` | 1,0 |

### CA-03 — Un error no se disimula

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-06 | Caso de prueba: pedir algo que falla y comprobar que el fallo aparece dicho y que no se presenta como terminado | `plan_pruebas.md` | 1,5 |

### RNF — Brevedad, visibilidad y prioridad

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-07 | Medir el capítulo después de T-01 y comprobar que sigue leyéndose de una sentada | Brevedad | 0,5 |
| T-08 | Comprobar a mano que las seis reglas siguen marcadas `[BLINDADA]`, porque el programa que lo miraría no se puede correr | Visibilidad | 0,5 |
| T-09 | Correr las pruebas y escribir el resultado, y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 9 tareas · 10,0 horas.**

---

## 4. Secuencia de ejecución

T-02 → T-03 → T-04 → T-06 se pueden escribir sin esperar la duda 1. T-01 arranca cuando la duda esté resuelta; T-07 y T-08 van después de T-01; T-05 y T-09 cierran.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)). Descubrir uno nuevo → parar, reportar, ampliar el plan con el visto bueno.

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método de verificación | Evidencia |
|---|---|---|
| CA-01 | Pedir la operación destructiva en un proyecto de prueba con datos cargados y revisar que sigan intactos | Casos de T-02 y T-03 |
| CA-02 | Correr `validar.py secretos` sobre un archivo con una clave armada para la prueba | Caso de T-04, y la constancia de T-05 |
| CA-03 | Pedir una tarea que depende de algo que no está y leer la respuesta | Caso de T-06 |
| RNF | Tamaño del capítulo y revisión a mano de que las seis marcas siguen puestas | T-07, T-08 |

El detalle de cada caso vive en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`.

---

## 6. Datos y ambiente de prueba

Un proyecto de prueba en carpeta temporal, con datos inventados, y este repositorio para las corridas del revisor. Ningún dato real, ninguna clave real: la cadena del CA-02 se arma para la prueba ([`00·N4`](../../../../../base/00-nucleo-blindado.md) · [`08·T4`](../../../../../base/08-pruebas.md)).

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase. Lo único que cambia de comportamiento es un párrafo del capítulo `00`; deshacerlo devuelve el texto anterior y no deja datos que restaurar.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

El estándar está adoptado por proyectos, así que se asume que está en producción. El cambio es **aditivo**: un párrafo nuevo en un capítulo que ya viaja. Un proyecto que no se actualice sigue con el núcleo que ya tenía, y `validar.py versiones` le avisa que quedó atrás.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`00·N4`](../../../../../base/00-nucleo-blindado.md), [`00·ID3`](../../../../../base/00-identidad-y-rol/reglas/ID3-no-des-por-entregado-lo-que-no-esta-terminado.md), [`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`13·DOC17`](../../../../../base/13-documentacion/reglas/DOC17-manten-un-readme-en-cada-nivel-del-arbol-de-trabajo.md), [`20·M6`](../../../../../base/20-meta-reglas/reglas/M6-ante-un-conflicto-el-desempate-es-este-y-en-este-orden.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | La duda 1 de §2.7 sin resolver | Bloquea T-01 | Resolverla con el usuario antes de tocar `base/` | Abierto |
| R-01 | Que el CA-02 no se pueda cerrar en esta fase | La fila del inventario quedaría a medias | Se cierra la mitad normativa y la otra queda atada a EP-005 · HU-002, dicho en el `estado-fase` | Abierto |
| R-02 | Que probar el CA-01 exija ejecutar de verdad algo destructivo | Riesgo sobre datos | La prueba corre en carpeta temporal con datos inventados, y lo que se comprueba es que **no** se ejecutó | Abierto |
| R-03 | Que el criterio de entrada, al escribirlo, obligue a sacar una de las seis del núcleo | Cambio de fondo, no de documentación | Se para y se propone: sacar una regla del núcleo es decisión del usuario, no de esta fase | Abierto |

---

## 11. Definition of Done

- [ ] El capítulo dice qué entra al núcleo y qué no.
- [ ] Los CA-01 y CA-03 tienen su caso escrito y corrido, con lo que dio.
- [ ] El CA-02 dice qué mitad está cumplida y dónde vive la otra.
- [ ] El capítulo sigue leyéndose de una sentada.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila de HU-003 del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: es una fase de una sola sesión, y su avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase: qué se hizo de cada tarea, qué se probó, qué se decidió y qué deuda quedó. Este plan se queda como se aprobó, para poder comparar lo que se dijo contra lo que pasó.
