# Plan de Trabajo — Fase A-EP-001-HU-006-retrodocumentar-la-capa-del-proyecto (módulo Cuerpo de reglas)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en [HU-006](../HU-006-capa-propia-del-proyecto.md); el detalle de las pruebas, en el `plan_pruebas.md` de esta misma fase; lo que dieron al correrlas, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** (identificador · [`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-001-HU-006-retrodocumentar-la-capa-del-proyecto` |
| **Épica** | [EP-001 Cuerpo de reglas heredable y en capas](../../epica.md) |
| **HU** | [HU-006 La capa propia de cada proyecto](../HU-006-capa-propia-del-proyecto.md) — una sola (`F12.1`) |
| **Módulo** | Cuerpo de reglas |
| **Especificación del módulo** | [HU-006](../HU-006-capa-propia-del-proyecto.md). El entregable es texto normativo y sus modelos: los criterios de aceptación son la especificación |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-001-HU-006-retrodocumentar-la-capa-del-proyecto` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📄 **Retro-documentación** ([`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md)). La capa del proyecto existe y se usa: el instalador la crea, [`plantillas/reglas-proyecto.md`](../../../../../plantillas/reglas-proyecto.md) es su molde, [`20·M16`](../../../../../base/20-meta-reglas/reglas/M16-toda-regla-de-proyecto-nombra-la-regla-de-base-que-concreta.md) le exige respaldo y [`validadores/version.py`](../../../../../validadores/version.py) lee qué versión declara adoptada. Lo que falta es la cadena. Sale de la fila de HU-006 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-006 | Qué exige | Estado hoy, sin haber tocado nada |
|---|---|---|
| [CA-01](../HU-006-capa-propia-del-proyecto.md#ca-01--un-ajuste-del-proyecto-manda-sobre-la-convención-general) | Un ajuste del proyecto manda sobre la convención general | Exigido por [`20·M1`](../../../../../base/20-meta-reglas/reglas/M1-la-jerarquia-tiene-cuatro-niveles-y-un-solo-orden.md) y [`20·M6`](../../../../../base/20-meta-reglas/reglas/M6-ante-un-conflicto-el-desempate-es-este-y-en-este-orden.md). **Sin prueba en un proyecto real** |
| [CA-02](../HU-006-capa-propia-del-proyecto.md#ca-02--una-regla-propia-sin-respaldo-no-se-acepta) | Una regla propia sin respaldo no se acepta | Exigido por [`20·M16`](../../../../../base/20-meta-reglas/reglas/M16-toda-regla-de-proyecto-nombra-la-regla-de-base-que-concreta.md). El programa que lo comprobaría **no se puede correr** |
| [CA-03](../HU-006-capa-propia-del-proyecto.md#ca-03--un-ajuste-que-contradice-el-núcleo-no-aplica) | Un ajuste que contradice el núcleo no aplica | Exigido en la cabecera del [núcleo](../../../../../base/00-nucleo-blindado.md) y en [`estructura-regla.md`](../../../../../base/20-meta-reglas/estructura-regla.md), que prohíbe mandar hacia arriba. **Sin prueba** |

**Por qué una sola fase para los tres CA.** Los tres se comprueban con el mismo proyecto de prueba y la misma capa `.agente/`: son las tres respuestas del desempate ante un ajuste propio. Partirlos daría fases que existen para cumplir la nomenclatura (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** demostrar, con un proyecto real, que la capa propia ajusta las convenciones, que no puede tocar el núcleo y que una regla propia sin respaldo se detecta — y dejar dicho cuál de esas tres comprobaciones hoy nadie puede correr.

**Fuera de alcance:**

- **Darle punto de entrada a `metareglas.py`,** que es donde vive la comprobación de `M16`. Es el punto 2 del pendiente [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md).
- **El instalador y la puesta al día del proyecto.** Es EP-007, con sus fases ya escritas.
- **El aviso de versión atrasada.** Es [EP-002 · HU-004](../../../EP-002-versionado-y-adopcion/HU-004-aviso-al-quedar-atras/HU-004-aviso-al-quedar-atras.md).
- **Cambiar los modelos de la capa 3.** Si la prueba muestra que a alguno le falta algo, se propone: son `plantillas/`, y tocarlas sube versión.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado contra el repositorio el 2026-08-17, leyendo los modelos, las meta-reglas y los programas que las miran.

**Lo que ya existe:**

| Exigencia de la HU | Dónde está hoy | Estado |
|---|---|---|
| RN-01 · los ajustes se declaran en el proyecto, no en el cuerpo central | [`20·M13`](../../../../../base/20-meta-reglas/reglas/M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md), y el molde [`plantillas/reglas-proyecto.md`](../../../../../plantillas/reglas-proyecto.md) | Regla y modelo |
| RN-02 · toda regla propia nombra la regla de base que concreta | [`20·M16`](../../../../../base/20-meta-reglas/reglas/M16-toda-regla-de-proyecto-nombra-la-regla-de-base-que-concreta.md) | Regla |
| RN-03 · la capa del proyecto ajusta las convenciones, nunca el núcleo | Cabecera del [núcleo](../../../../../base/00-nucleo-blindado.md), [`20·M1`](../../../../../base/20-meta-reglas/reglas/M1-la-jerarquia-tiene-cuatro-niveles-y-un-solo-orden.md) y [`20·M6`](../../../../../base/20-meta-reglas/reglas/M6-ante-un-conflicto-el-desempate-es-este-y-en-este-orden.md) | Regla |
| RN-04 · el proyecto declara qué versión del cuerpo central adoptó | La línea «Versión del estándar adoptada» del [`CLAUDE.md.plantilla`](../../../../../plantillas/CLAUDE.md.plantilla), que lee [`validadores/version.py`](../../../../../validadores/version.py) · `validar.py version` | Corriendo |
| RN-05 · lo que aplica a cualquier proyecto se propone para el cuerpo central | [`20·M13`](../../../../../base/20-meta-reglas/reglas/M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md) | Regla |
| Los modelos de la capa 3 | [`plantillas/stack.md`](../../../../../plantillas/stack.md), [`dominio.md`](../../../../../plantillas/dominio.md), [`mapeo-nombres.md`](../../../../../plantillas/mapeo-nombres.md), [`marco-normativo.md`](../../../../../plantillas/marco-normativo.md) | Escritos |
| Que un documento de la capa 3 se pueda revisar contra su molde | [`validadores/plantillas.py`](../../../../../validadores/plantillas.py) · `validar.py plantilla` | Corriendo |

**Lo que no existe:**

1. **La comprobación de `M16`.** Está escrita en [`validadores/metareglas.py`](../../../../../validadores/metareglas.py), que se corre sin punto de entrada y termina en silencio con código 0: no hay subcomando en `validar.py`. Hoy nadie detecta una regla propia sin respaldo.
2. **La prueba del desempate.** Nadie ha tomado un proyecto con capa propia y comprobado que el ajuste gana a la convención y pierde contra el núcleo.
3. **La constancia de qué pasa con el ajuste que contradice el núcleo.** La prohibición está escrita; lo que hace el agente cuando se la encuentra no está registrado en ninguna parte.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `documentacion/epicas/EP-001-…/HU-006-…/A-EP-001-HU-006-…/plan_pruebas.md` | Nuevo | Documentación | Los casos de esta fase |
| `documentacion/epicas/EP-001-…/HU-006-…/A-EP-001-HU-006-…/resultado_pruebas.md` | Nuevo | Documentación | Lo que dieron, y qué quedó sin poder comprobarse |
| `documentacion/epicas/EP-001-…/HU-006-…/HU-006-capa-propia-del-proyecto.md` | Modificar | Documentación | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/53-enlaces-py-no-tiene-punto-de-entrada.md` | Modificar | Documentación | Se le suma `metareglas.py` como caso encontrado, en su punto 2 |
| `pendientes/48-inventario-hu.md` | Modificar | Documentación | Las casillas de la fila de HU-006 |

> **Ni `base/` ni `plantillas/` se tocan.** Esta fase prueba lo que ya está.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna: no se cambia ningún contrato. Lo único que se edita fuera de la carpeta de la fase es un pendiente, que nadie cita como si fuera regla.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque el entregable son archivos de texto y las corridas de un programa de línea de comandos.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

No aplica. La capa del proyecto se lee abriendo `.agente/` del proyecto, y el agente la recibe al abrir la sesión.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El CA-02 se cierra con la prueba hecha a mano y la constancia de que el programa no corre | Escribir el punto de entrada de `metareglas.py` de paso | Es otro archivo y otro problema, ya anotado en el [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md); tocarlo acá sería salirse del criterio ([`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md)) |
| Se prueba sobre un proyecto que ya tiene el estándar instalado | Armar un proyecto de prueba desde cero | Lo que se prueba es el desempate ante ajustes que alguien escribió de verdad, no ante ajustes inventados para que la prueba pase |
| El caso del CA-03 se escribe con un ajuste que contradice el núcleo a propósito, y se comprueba que no aplica | Confiar en que la prohibición escrita alcanza | Es justo lo que este trabajo corrige: una exigencia escrita y nunca probada |

### 2.7 Dudas por resolver antes de escribir

| # | Duda | A quién se consulta | Estado |
|---|---|---|---|
| 1 | Sobre qué proyecto instalado se hacen las pruebas | Usuario | Pendiente |
| 2 | Si el ajuste que contradice el núcleo se escribe en el proyecto de prueba, o basta simularlo en una copia | Usuario | Pendiente |

La duda 1 bloquea los tres CA; la duda 2, solo el CA-03.

**Decididas el 2026-08-18**, en el [pendiente 59](../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md). 👤 marca lo que sigue esperando un dato del usuario.

| Duda | Decisión |
|---|---|
| 12 | 👤 **Propuesta: `shopnest-mesa`** — el único que ya reporta al estándar y tiene estructura completa. |
| 35 | **En un proyecto de mentira, en carpeta temporal.** Nunca en uno real ([`00·N4`](../../../../../base/00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada)). |

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Un ajuste del proyecto manda sobre la convención general

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Elegir el proyecto de prueba y listar los ajustes que ya tiene escritos en su capa propia | `plan_pruebas.md` | 1,0 |
| T-02 | Caso de prueba: con un ajuste propio y la convención general en desacuerdo, se aplica el ajuste, y el desempate queda dicho | `plan_pruebas.md` | 2,0 |

### CA-02 — Una regla propia sin respaldo no se acepta

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Caso de prueba: se escribe en la copia una regla propia sin nombrar la regla de base, y se revisa a mano contra `M16` | `plan_pruebas.md` | 1,5 |
| T-04 | Dejar escrito que la comprobación automática no corre, con la evidencia de la corrida en silencio, y sumarlo al pendiente 53 | `resultado_pruebas.md` · `pendientes/53-…` | 1,5 |

### CA-03 — Un ajuste que contradice el núcleo no aplica

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-05 | Caso de prueba: un ajuste propio que afloja una regla `[BLINDADA]` no se aplica, y queda dicho por qué | `plan_pruebas.md` | 2,0 |
| T-06 | Comprobar que el mismo ajuste, puesto sobre una convención de capa 2, sí se aplica — es lo que separa el CA-03 del CA-01 | `plan_pruebas.md` | 1,0 |

### RNF — Que la capa propia se pueda revisar

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-07 | Correr `validar.py plantilla` sobre los documentos de la capa 3 del proyecto de prueba y `validar.py version` para la versión adoptada | Comprobabilidad | 1,0 |
| T-08 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 8 tareas · 11,5 horas.**

---

## 4. Secuencia de ejecución

T-01 abre, resuelta la duda 1. T-02, T-03 y T-05 → T-06 pueden ir en paralelo sobre la misma copia; T-05 espera la duda 2. T-04 y T-07 después de sus corridas, T-08 cierra.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)). El proyecto de prueba se trabaja en copia, no en su carpeta viva.

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método de verificación | Evidencia |
|---|---|---|
| CA-01 | Ajuste propio contra convención general, con el desempate escrito | Casos de T-01 y T-02 |
| CA-02 | Regla propia sin respaldo revisada a mano contra `M16`, y la corrida que no comprueba nada | Casos de T-03 y la constancia de T-04 |
| CA-03 | Ajuste que afloja una `[BLINDADA]`, y el mismo ajuste sobre una convención de capa 2 | Casos de T-05 y T-06 |
| RNF | Corridas de `validar.py plantilla` y `validar.py version` | T-07 |

---

## 6. Datos y ambiente de prueba

Una copia local del proyecto que decida la duda 1, con datos inventados si los pide. No se escribe en la carpeta viva de ningún proyecto ajeno ([`00·N4`](../../../../../base/00-nucleo-blindado.md)), y ninguna clave real entra en los archivos de prueba.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase. Lo que se toca fuera de la carpeta de la fase es un pendiente y la §7 de la HU: revertir devuelve el texto y no deja datos que restaurar. La copia del proyecto de prueba se borra al terminar.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

No aplica: nada de lo que entrega esta fase cambia lo que ya corre en los proyectos instalados. No hay subida de versión, porque no se toca `base/` ni `plantillas/`.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`00·N4`](../../../../../base/00-nucleo-blindado.md), [`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`13·DOC17`](../../../../../base/13-documentacion/reglas/DOC17-manten-un-readme-en-cada-nivel-del-arbol-de-trabajo.md), [`20·M1`](../../../../../base/20-meta-reglas/reglas/M1-la-jerarquia-tiene-cuatro-niveles-y-un-solo-orden.md), [`20·M6`](../../../../../base/20-meta-reglas/reglas/M6-ante-un-conflicto-el-desempate-es-este-y-en-este-orden.md), [`20·M13`](../../../../../base/20-meta-reglas/reglas/M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md), [`20·M16`](../../../../../base/20-meta-reglas/reglas/M16-toda-regla-de-proyecto-nombra-la-regla-de-base-que-concreta.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Las dudas de §2.7 sin resolver | Bloquean el arranque | Elegir proyecto y forma de la prueba con el usuario | Abierto |
| R-01 | Que el proyecto de prueba tenga reglas propias sin respaldo y la fase se vuelva una limpieza ajena | Se desborda el alcance, y es trabajo de otro proyecto | Se anotan y se reportan al dueño del proyecto; acá solo cuentan como evidencia | Abierto |
| R-02 | Que el CA-02 quede cerrado con prueba a mano y mañana nadie la repita | La comprobación se pierde | El resultado dice qué se hizo a mano y por qué, y el pendiente 53 queda con el caso anotado | Abierto |
| R-03 | Tocar por error la carpeta viva del proyecto de prueba | Daño en trabajo ajeno | Se trabaja en copia, y el `plan_pruebas` lo declara como condición de arranque | Abierto |

---

## 11. Definition of Done

- [ ] El desempate ajuste-propio contra convención está probado en un proyecto real.
- [ ] Una regla propia sin respaldo quedó detectada, aunque haya sido a mano.
- [ ] Un ajuste que contradice el núcleo quedó demostrado que no aplica.
- [ ] El resultado dice qué comprobación no se pudo correr y dónde quedó anotada.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila de HU-006 del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase. Este plan se queda como se aprobó, para poder comparar lo que se dijo contra lo que pasó.
