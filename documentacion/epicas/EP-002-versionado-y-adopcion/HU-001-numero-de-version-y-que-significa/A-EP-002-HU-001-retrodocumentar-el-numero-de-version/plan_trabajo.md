# Plan de Trabajo — Fase A-EP-002-HU-001-retrodocumentar-el-numero-de-version (módulo Versionado y adopción)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-001](../HU-001-numero-de-version-y-que-significa.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-002-HU-001-retrodocumentar-el-numero-de-version` |
| **Épica** | [EP-002 Versionado y adopción](../../epica.md) |
| **HU** | [HU-001 Fijar el número de versión y qué significa cada parte](../HU-001-numero-de-version-y-que-significa.md) — una sola (`F12.1`) |
| **Módulo** | Versionado y adopción |
| **Especificación del módulo** | [HU-001](../HU-001-numero-de-version-y-que-significa.md). El entregable es texto normativo y un archivo de una línea: sus criterios de aceptación son la especificación |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-002-HU-001-retrodocumentar-el-numero-de-version` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📄 **Retro-documentación** ([`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-spec-antes-de-tocarlo.md)). El número existe y se usó 23 veces: [`VERSION`](../../../../../VERSION) va en `23.2.0`, el [`CHANGELOG`](../../../../../CHANGELOG.md) explica las tres partes y [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md) obliga a subirlo. Sale de la fila de HU-001 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-001 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-001-numero-de-version-y-que-significa.md#ca-01--el-número-existe-y-se-lee-en-un-solo-lugar) | El número existe y se lee en un solo lugar | Cumplido: `VERSION`, una línea, y [`version.py`](../../../../../validadores/version.py) lo lee de ahí. Sin prueba escrita |
| [CA-02](../HU-001-numero-de-version-y-que-significa.md#ca-02--un-cambio-que-obliga-sube-la-parte-mayor) | Un cambio que obliga sube la parte mayor | Escrito en el `CHANGELOG` y en `M10`. **Nadie comprueba** que el tipo elegido sea el correcto |
| [CA-03](../HU-001-numero-de-version-y-que-significa.md#ca-03--una-corrección-de-redacción-no-sube-la-parte-mayor) | Una corrección de redacción no sube la parte mayor | Igual: escrito, sin comprobación |

**Por qué una sola fase.** Los tres CA se comprueban sobre el mismo archivo y el mismo registro (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** dejar probado, contra las 23 subidas que ya ocurrieron, que el número vive en un solo lugar y que cada parte significa lo que el `CHANGELOG` dice.

**Fuera de alcance:**

- **Quién sube la versión cuando hay dos sesiones abiertas.** Es [HU-006](../../HU-006-quien-sube-la-version/HU-006-quien-sube-la-version.md) y el pendiente [22](../../../../../pendientes/22-dos-sesiones-versionando-a-la-vez.md).
- **El registro de cambios,** que es [HU-002](../../HU-002-registro-de-cambios/HU-002-registro-de-cambios.md).
- **Reclasificar subidas viejas.** Si alguna quedó con el tipo mal puesto, se anota como hallazgo: el registro es rastro y no se reescribe.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17: `VERSION` dice `23.2.0`; el `CHANGELOG` define las tres partes y la regla de retroactividad en su cabecera.

**Lo que ya existe:** `VERSION` como fuente única (RN-05); las tres partes con su significado en la cabecera del `CHANGELOG` (RN-01 a RN-04); `M10`, que obliga a subir y registrar; [`version.py`](../../../../../validadores/version.py), que compara la versión del estándar con la que declara un proyecto.

**Lo que no existe:**

1. **La prueba de que `VERSION` es la única fuente.** Nadie comprueba que no haya otro número escrito por ahí que se contradiga con él.
2. **La comprobación del tipo de subida.** Elegir MAYOR, MENOR o PARCHE es criterio, y hoy no queda escrito **por qué** se eligió: la entrada del registro dice el tipo, no el razonamiento.
3. **La revisión de que ninguna parte se saltó** (RN-06) a lo largo de las 23 versiones.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `…/A-EP-002-HU-001-…/plan_pruebas.md` | Nuevo | Los casos de los tres CA |
| `…/A-EP-002-HU-001-…/resultado_pruebas.md` | Nuevo | Lo que dieron, con la revisión de las 23 subidas |
| `validadores/pruebas.py` | Modificar | Prueba de que `VERSION` es un número bien formado y que ninguna parte se saltó entre entradas consecutivas del registro |
| `HU-001-numero-de-version-y-que-significa.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> `VERSION`, el `CHANGELOG` y `base/` no se tocan.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna: se agrega una prueba, sin cambiar el contrato de ningún validador.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque el entregable es un archivo de texto y una prueba de línea de comandos.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

No aplica. El número se lee abriendo `VERSION`, y el agente lo recibe al abrir la sesión.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La prueba lee el número del propio `VERSION` | Escribir `23.2.0` dentro de la prueba | Una versión escrita a mano en la prueba envejece en la subida siguiente |
| Las subidas mal clasificadas se anotan, no se corrigen | Reescribir la entrada del registro | La RN-04 de [HU-002](../../HU-002-registro-de-cambios/HU-002-registro-de-cambios.md) dice que el registro es rastro y no se reescribe |

### 2.7 Dudas por resolver antes de escribir

Ninguna: los tres CA se prueban contra lo que ya está en el repositorio.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — El número existe y se lee en un solo lugar

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Prueba: `VERSION` trae un número de tres partes y es el que devuelve `version.version_estandar()` | `validadores/pruebas.py` | 1,5 |
| T-02 | Caso de prueba: buscar en el repositorio otro número de versión del estándar escrito aparte, y comprobar que ninguno manda | `plan_pruebas.md` | 1,5 |

### CA-02 — Un cambio que obliga sube la parte mayor

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Caso de prueba: tomar tres entradas MAYOR del registro y comprobar que cada una obliga a un proyecto al día a hacer algo | `plan_pruebas.md` | 2,0 |

### CA-03 — Una corrección de redacción no sube la parte mayor

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-04 | Caso de prueba: tomar tres entradas PARCHE y comprobar que ninguna cambió qué se exige | `plan_pruebas.md` | 1,5 |

### RNF — Que ninguna parte se salte

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-05 | Prueba: entre entradas consecutivas del registro no hay saltos ni reinicios de ninguna de las tres partes | `validadores/pruebas.py` | 2,0 |
| T-06 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 6 tareas · 10,0 horas.**

---

## 4. Secuencia de ejecución

T-01 → T-05 primero, que comparten la lectura del registro. T-02, T-03 y T-04 en paralelo. T-06 cierra.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Prueba automática sobre `VERSION`, más la búsqueda de números sueltos | T-01, T-02 |
| CA-02 | Tres entradas MAYOR revisadas contra la definición del `CHANGELOG` | T-03 |
| CA-03 | Tres entradas PARCHE revisadas igual | T-04 |
| RNF | Prueba automática de continuidad de las tres partes | T-05 |

---

## 6. Datos y ambiente de prueba

Este repositorio. Las pruebas leen y no escriben. Ningún dato real y ninguna clave.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase. Lo único ejecutable que entra son dos pruebas.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

No aplica: no cambia nada de lo que corre en los proyectos instalados. Sin subida de versión, porque no se toca `base/` ni `plantillas/`.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-spec-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`13·DOC17`](../../../../../base/13-documentacion/reglas/DOC17-manten-un-readme-en-cada-nivel-del-arbol-de-trabajo.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que aparezcan subidas con el tipo mal elegido | Se destapa trabajo de fondo | Se anotan como hallazgo; el registro no se reescribe | Abierto |
| R-02 | Que la prueba de continuidad falle por las dos numeraciones vivas del 2026-08-14 | Suite roja por un hecho ya conocido | Se declara ese tramo como excepción documentada, atada al pendiente [22](../../../../../pendientes/22-dos-sesiones-versionando-a-la-vez.md) | Abierto |
| R-03 | Que otra sesión esté tocando `validadores/pruebas.py` | Pisar trabajo ajeno | Se guarda solo lo propio | Abierto |

---

## 11. Definition of Done

- [ ] Los tres CA tienen su caso escrito y corrido.
- [ ] `VERSION` es la única fuente, y hay prueba que lo sostiene.
- [ ] La continuidad de las tres partes está probada, con su excepción documentada si aparece.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
