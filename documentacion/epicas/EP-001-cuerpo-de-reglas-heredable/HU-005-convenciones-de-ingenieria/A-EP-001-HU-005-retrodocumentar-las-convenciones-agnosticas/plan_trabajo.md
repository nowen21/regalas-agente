# Plan de Trabajo — Fase A-EP-001-HU-005-retrodocumentar-las-convenciones-agnosticas (módulo Cuerpo de reglas)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en [HU-005](../HU-005-convenciones-de-ingenieria.md); el detalle de las pruebas, en el `plan_pruebas.md` de esta misma fase; lo que dieron al correrlas, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** (identificador · [`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-001-HU-005-retrodocumentar-las-convenciones-agnosticas` |
| **Épica** | [EP-001 Cuerpo de reglas heredable y en capas](../../epica.md) |
| **HU** | [HU-005 Convenciones de ingeniería agnósticas](../HU-005-convenciones-de-ingenieria.md) — una sola (`F12.1`) |
| **Módulo** | Cuerpo de reglas |
| **Especificación del módulo** | [HU-005](../HU-005-convenciones-de-ingenieria.md). El entregable es texto normativo: sus criterios de aceptación son la especificación |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-001-HU-005-retrodocumentar-las-convenciones-agnosticas` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📄 **Retro-documentación** ([`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md)). Las convenciones existen: diecisiete capítulos, del `03` al `19`, todos marcados `[CAPA 2]` y cinco de ellos `opt-in`. Lo que falta es la cadena que diga con qué plan se escribieron, con qué casos se comprueba que sirven en cualquier stack y qué dio. Sale de la fila de HU-005 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-005 | Qué exige | Estado hoy, sin haber tocado nada |
|---|---|---|
| [CA-01](../HU-005-convenciones-de-ingenieria.md#ca-01--una-convención-sirve-igual-en-dos-proyectos-de-lenguajes-distintos) | Una convención sirve igual en dos proyectos de lenguajes distintos | Exigido por [`20·M3`](../../../../../base/20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md) y por la fila 5 del checklist. **Sin prueba en dos proyectos reales** |
| [CA-02](../HU-005-convenciones-de-ingenieria.md#ca-02--un-tema-no-aparece-en-dos-capítulos) | Un tema no aparece en dos capítulos | Exigido por [`20·M2`](../../../../../base/20-meta-reglas/reglas/M2-un-tema-un-capitulo-un-dueno.md) y por la fila 4 del checklist, que es de las que **pide leer**: ningún programa la decide |
| [CA-03](../HU-005-convenciones-de-ingenieria.md#ca-03--una-convención-que-solo-sirve-a-cierto-tipo-de-proyecto-queda-marcada-como-opcional) | Una convención que solo sirve a cierto tipo de proyecto queda marcada como opcional | Cumplido: la marca `*opt-in*` es una de las tres de la lista cerrada, y los capítulos `15` a `19` la llevan en su cabecera. **Sin prueba** |

**Por qué una sola fase para los tres CA.** Los tres se comprueban sobre el mismo cuerpo de diecisiete capítulos y con la misma lectura. Partirlos daría fases que existen para cumplir la nomenclatura (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** dejar demostrado —con dos proyectos de lenguajes distintos y con una revisión de solapes— que las convenciones se pueden heredar sin tocarlas, y que lo opcional está marcado como tal.

**Fuera de alcance:**

- **Reescribir convenciones.** Si la prueba muestra que alguna nombra tecnología, se anota como hallazgo y se propone; corregirla es otra fase ([`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md)).
- **Poner al día los checklists vencidos de cada regla.** Eso es [HU-009](../../HU-009-reglas-sin-checklist-al-dia/HU-009-reglas-sin-checklist-al-dia.md), que ya tiene su fase abierta.
- **Darle punto de entrada a `metareglas.py`.** El programa que comprobaría la fila 5 no se puede correr, y eso es el punto 2 del pendiente [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md), no trabajo de esta fase.
- **La capa del proyecto.** Que el ajuste propio mande sobre la convención general es [HU-006](../../HU-006-capa-propia-del-proyecto/HU-006-capa-propia-del-proyecto.md).

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado contra el repositorio el 2026-08-17, leyendo las cabeceras de los diecisiete capítulos y el checklist del estándar.

**Lo que ya existe:**

| Exigencia de la HU | Dónde está hoy | Estado |
|---|---|---|
| RN-01 · ninguna convención nombra lenguaje, framework ni producto | [`20·M3`](../../../../../base/20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md) y la fila 5 del [checklist](../../../../../base/20-meta-reglas/checklist.md) | Regla |
| RN-02 · un tema, un capítulo dueño; lo que aparece en dos se enlaza | [`20·M2`](../../../../../base/20-meta-reglas/reglas/M2-un-tema-un-capitulo-un-dueno.md) y la fila 4 | Regla |
| RN-03 · cada convención es ajustable desde la capa del proyecto | La marca `[CAPA 2]` en la cabecera de los diecisiete capítulos, y [`20·M1`](../../../../../base/20-meta-reglas/reglas/M1-la-jerarquia-tiene-cuatro-niveles-y-un-solo-orden.md) | Regla |
| RN-04 · lo que solo aplica a cierto tipo de proyecto se marca opcional | `[CAPA 2 · opt-in]` en los capítulos `15` a `19`, y la fila 13 con la lista cerrada de marcas | Regla |
| RN-05 · antes de escribir una convención se busca si ya existe | [`20·M12`](../../../../../base/20-meta-reglas/reglas/M12-antes-de-crear-una-regla-buscar-la-duplicacion-es-el-defecto-mas-caro.md) y la fila 2 | Regla |
| Los capítulos, escritos | `base/03-datos.md` a `base/19-observabilidad-y-operacion.md`, más `base/13-documentacion/` con sus reglas en archivo propio | Escrito |

**Lo que no existe:**

1. **La prueba en dos stacks.** El CA-01 se afirma por la forma de la regla, no porque alguien haya tomado la misma convención y la haya cumplido en dos proyectos de lenguajes distintos.
2. **El inventario de solapes.** La fila 4 se aplica regla por regla al escribirla; nadie revisó el cuerpo entero buscando el mismo tema en dos capítulos.
3. **La comprobación automática de la fila 5.** [`validadores/metareglas.py`](../../../../../validadores/metareglas.py) está escrito para eso y **no se puede correr**: no tiene punto de entrada ni subcomando.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `documentacion/epicas/EP-001-…/HU-005-…/A-EP-001-HU-005-…/plan_pruebas.md` | Nuevo | Documentación | Los casos de esta fase |
| `documentacion/epicas/EP-001-…/HU-005-…/A-EP-001-HU-005-…/resultado_pruebas.md` | Nuevo | Documentación | Lo que dieron, incluida la tabla de solapes |
| `analisis/` | Nuevo | Análisis | La foto de los diecisiete capítulos: qué tema es de quién ([`13·DOC8`](../../../../../base/13-documentacion/reglas/DOC8-cierra-todo-analisis-con-su-tabla-de-decisiones.md)) |
| `documentacion/epicas/EP-001-…/HU-005-…/HU-005-convenciones-de-ingenieria.md` | Modificar | Documentación | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Documentación | Las casillas de la fila de HU-005 |

> **`base/` no se toca.** Esta fase mira y demuestra. Si aparece algo que corregir, se propone.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna: no se cambia ningún contrato. No entra ni sale una regla, así que nada de lo que cita `base/` cambia de destino.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque el entregable son archivos de texto del repositorio.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

No aplica. Los capítulos llegan al agente como índice al abrir la sesión —completo solo viaja `00` y `01`— y se abren cuando toca el tema.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El CA-01 se prueba con dos proyectos que ya existen y usan el estándar, no con dos de juguete | Armar dos proyectos de prueba para la ocasión | Un proyecto de juguete cumple cualquier convención: no hay código real donde la convención estorbe |
| El solape se revisa por tema, con una tabla de tema → capítulo dueño | Buscar palabras repetidas entre capítulos | Un tema se repite aunque las palabras cambien; la fila 4 pide leer, y por eso no la decide un programa |
| Lo que se encuentre mal queda como hallazgo numerado, no corregido | Corregir al pasar | El paso 5 del procedimiento de [retro-documentación](../../../../../base/13-documentacion/retrodocumentacion.md) pide listar los huecos numerados para poder citarlos desde otra fase |

### 2.7 Dudas por resolver antes de escribir

| # | Duda | A quién se consulta | Estado |
|---|---|---|---|
| 1 | Cuáles dos proyectos se usan para el CA-01, y de qué lenguajes | Usuario | **Resuelta** el 2026-08-22, propuesta 11 del [pendiente 59](../../../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md), comprobada contra el registro de proyectos: **AgroSystem** (`C:\wamp64\www\proyectos\personalesgro-system`, Laravel + Livewire + Spatie) y **RNI** (`C:\DesarrollosClaude\dp`, Angular más Python). Son los dos stacks más distintos del registro, que es lo que la prueba necesita; los dos tienen el estándar instalado |

La duda 1 bloquea T-01. Los CA-02 y CA-03 no dependen de ella.

**Decididas el 2026-08-18**, en el [pendiente 59](../../../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md). 👤 marca lo que sigue esperando un dato del usuario.

| Duda | Decisión |
|---|---|
| 11 | 👤 **Propuesta: AgroSystem (Laravel · PHP) y RNI (Angular + Python)** — los dos stacks más distintos del registro. |
---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Una convención sirve igual en dos proyectos de lenguajes distintos

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Elegir con el usuario los dos proyectos y las convenciones que se van a poner a prueba | `plan_pruebas.md` | 1,0 |
| T-02 | Caso de prueba: la misma convención se cumple en los dos, y lo que cambia queda declarado en la capa del proyecto, no en el capítulo | `plan_pruebas.md` | 2,0 |
| T-03 | Recorrer los diecisiete capítulos buscando nombre de lenguaje, framework, motor, nube o herramienta, y anotar cada aparición con su línea | `resultado_pruebas.md` | 3,0 |

### CA-02 — Un tema no aparece en dos capítulos

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-04 | Levantar la tabla tema → capítulo dueño de los diecisiete capítulos | `analisis/` | 3,0 |
| T-05 | Caso de prueba: por cada tema con dos apariciones, comprobar si la segunda enlaza o repite | `plan_pruebas.md` | 2,0 |
| T-06 | Numerar como hallazgo cada repetición encontrada, sin corregirla | `resultado_pruebas.md` | 1,0 |

### CA-03 — Una convención que solo sirve a cierto tipo de proyecto queda marcada como opcional

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-07 | Caso de prueba: los cinco capítulos `opt-in` llevan la marca de la lista cerrada, y un proyecto que no los enciende no queda incumpliendo | `plan_pruebas.md` | 1,5 |
| T-08 | Revisar si algún capítulo sin marca solo le sirve a cierto tipo de proyecto, y anotarlo | `resultado_pruebas.md` | 1,5 |

### RNF — Que el cuerpo se pueda heredar sin tocarlo

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-09 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 9 tareas · 16,5 horas.**

---

## 4. Secuencia de ejecución

T-04 → T-05 → T-06 y T-07 → T-08 pueden arrancar de entrada: no dependen de la duda. T-01 → T-02 esperan la duda 1. T-03 va en paralelo a T-04, porque las dos son lectura del mismo cuerpo. T-09 cierra.

> No se toca ningún archivo de `base/` ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)). Lo que aparezca se propone.

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método de verificación | Evidencia |
|---|---|---|
| CA-01 | La misma convención cumplida en dos proyectos de lenguajes distintos, y el recorrido de los diecisiete capítulos buscando nombres propios | Casos de T-02 y la tabla de T-03 |
| CA-02 | Tabla tema → capítulo dueño, y revisión de cada tema que aparece dos veces | Casos de T-05 y los hallazgos de T-06 |
| CA-03 | Revisión de las marcas de los cinco capítulos opcionales y de los que no la llevan | Casos de T-07 y T-08 |

---

## 6. Datos y ambiente de prueba

Este repositorio y los dos proyectos que decida la duda 1, leídos en copia local. No se escribe en ellos: la prueba es de lectura. Ningún dato real sale del proyecto que lo tiene.

---

## 7. Reversión / rollback  ·  `F14` Q11

No hay nada que revertir en el comportamiento: la fase solo agrega documentos. Si el análisis queda mal hecho, se descarta la rama.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

No aplica: nada de lo que entrega esta fase cambia lo que ya corre en los proyectos que adoptaron el estándar. No hay subida de versión, porque no se toca `base/` ni `plantillas/`.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), [`13·DOC8`](../../../../../base/13-documentacion/reglas/DOC8-cierra-todo-analisis-con-su-tabla-de-decisiones.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`13·DOC17`](../../../../../base/13-documentacion/reglas/DOC17-manten-un-readme-en-cada-nivel-del-arbol-de-trabajo.md), [`20·M1`](../../../../../base/20-meta-reglas/reglas/M1-la-jerarquia-tiene-cuatro-niveles-y-un-solo-orden.md), [`20·M2`](../../../../../base/20-meta-reglas/reglas/M2-un-tema-un-capitulo-un-dueno.md), [`20·M3`](../../../../../base/20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md), [`20·M12`](../../../../../base/20-meta-reglas/reglas/M12-antes-de-crear-una-regla-buscar-la-duplicacion-es-el-defecto-mas-caro.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | La duda 1 sin resolver | Bloquea el CA-01 | Elegir los dos proyectos con el usuario antes de escribir los casos | Abierto |
| R-01 | Que el recorrido encuentre muchos nombres de tecnología y la fase se convierta en una limpieza | Se desborda el alcance | Se anotan numerados y se propone una fase aparte; acá no se corrige | Abierto |
| R-02 | Que la tabla de solapes quede a criterio de quien la escribe | Dos personas la llenarían distinto | Se escribe el criterio antes de llenarla, y cada fila cita el párrafo que la sostiene | Abierto |
| R-03 | Que probar en dos proyectos exija tocarlos | Riesgo sobre trabajo ajeno | La prueba es de lectura, en copia local, y no se escribe en ninguno de los dos | Abierto |

---

## 11. Definition of Done

- [ ] La misma convención está demostrada en dos proyectos de lenguajes distintos.
- [ ] La tabla tema → capítulo dueño existe y cubre los diecisiete capítulos.
- [ ] Cada solape encontrado quedó numerado como hallazgo.
- [ ] Los capítulos opcionales tienen su marca, y los que no la llevan quedaron revisados.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila de HU-005 del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase. Este plan se queda como se aprobó, para poder comparar lo que se dijo contra lo que pasó.
