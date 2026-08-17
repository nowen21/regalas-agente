# Plan de Trabajo — Fase A-EP-007-HU-005-retrodocumentar-que-no-se-pisa-lo-escrito (módulo Instalación)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-005](../HU-005-no-pisar-lo-escrito.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-007-HU-005-retrodocumentar-que-no-se-pisa-lo-escrito` |
| **Épica** | [EP-007 Instalación y actualización](../../epica.md) |
| **HU** | [HU-005 No pisar lo que escribió la persona](../HU-005-no-pisar-lo-escrito.md) — una sola (`F12.1`) |
| **Módulo** | Instalación |
| **Especificación del módulo** | [HU-005](../HU-005-no-pisar-lo-escrito.md). El módulo de instalación **no tiene especificación aparte** —se declara como deuda en las fases hermanas de esta épica— y sus criterios de aceptación hacen de especificación |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-007-HU-005-retrodocumentar-que-no-se-pisa-lo-escrito` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📄 **Retro-documentación** ([`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-spec-antes-de-tocarlo.md)). Está construido y es lo que hace que una puesta al día sea segura: el instalador copia y actualiza sin borrar lo que el proyecto escribió, y de eso salieron las dos fases de [HU-001](../../HU-001-instalar-con-una-linea/HU-001-instalar-con-una-linea.md) y la de [HU-006](../../HU-006-poner-al-dia/HU-006-poner-al-dia.md), ya con sus documentos. Sale de la fila de HU-005 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-005 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-005-no-pisar-lo-escrito.md#ca-01--lo-que-la-persona-escribió-se-conserva) | Lo que la persona escribió se conserva | Corriendo, y es la exigencia central de esta épica. Sin prueba propia de esta HU |
| [CA-02](../HU-005-no-pisar-lo-escrito.md#ca-02--lo-que-sí-se-reemplaza-queda-dicho) | Lo que sí se reemplaza queda dicho | Hay que medirlo: el instalador escribe el registro de la versión, y si dice archivo por archivo qué reemplazó es lo que la fase establece |

**Por qué una sola fase.** Los dos CA se comprueban en la misma puesta al día (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** dejar probado que una puesta al día no borra lo que la persona escribió, y que lo que sí se reemplaza queda dicho.

**Fuera de alcance:**

- **La estructura de carpetas,** que es [HU-003](../../HU-003-estructura-de-carpetas/HU-003-estructura-de-carpetas.md).
- **El contenido del registro de la versión,** que arrastra los pendientes [44](../../../../../pendientes/44-el-registro-de-version-no-se-escribe-si-no-cambia-una-huella.md) y [46](../../../../../pendientes/46-el-registro-de-version-dice-que-falta-escribirse.md): acá se mide, no se corrige.
- **Cambiar el instalador.** Si al probar aparece que algo se pisa, se para y se reporta: es un defecto grave y merece su propia fase.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17: las fases de HU-001 y HU-006 dejaron escrito cómo se rellenan los marcadores y cómo se pone al día lo ya instalado.

**Lo que ya existe:** el instalador con su forma de copiar sin pisar; el registro de la versión adoptada, que escribe él; las tres fases hermanas de esta épica, con sus planes y sus cierres; y los dos pendientes abiertos sobre el contenido de ese registro, que dan el límite de lo que hoy se puede afirmar.

**Lo que no existe:**

1. **La prueba de que no pisa,** con un archivo modificado a mano.
2. **La lista de qué se reemplaza y qué se conserva.** Hay que reconstruirla leyendo el instalador.
3. **La constancia de qué dice el registro** después de una puesta al día, que es donde los pendientes 44 y 46 ya encontraron problemas.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/pruebas.py` | Modificar | La prueba del archivo modificado a mano |
| `…/A-EP-007-HU-005-…/plan_pruebas.md` · `resultado_pruebas.md` | Nuevo | Los casos, la lista de qué se reemplaza y lo que dieron |
| `HU-005-no-pisar-lo-escrito.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> `instalar.py` no se toca.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna: se agregan pruebas sobre lo que ya corre.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque es un programa de línea de comandos.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

**Sí tiene punto de entrada:** la puesta al día se corre por línea de comandos, y su resultado queda en el registro de la versión.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La prueba modifica un archivo a mano antes de actualizar | Comprobar solo que el archivo exista después | Existir y conservar el contenido no es lo mismo, y lo que se pierde es el contenido |
| Se prueba con el archivo que más duele: el del proyecto con texto propio | Un archivo cualquiera | El `CLAUDE.md` del proyecto es el que mezcla lo heredado con lo propio, y es donde pisar sería más grave |
| Lo que se encuentre mal se para y se reporta | Corregirlo de paso | Que el instalador pise algo es un defecto grave: merece su plan, no un arreglo al vuelo |

### 2.7 Dudas por resolver antes de escribir

Ninguna: la puesta al día se puede correr sobre una copia temporal.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Lo que la persona escribió se conserva

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Prueba: con un archivo modificado a mano en el proyecto, la puesta al día no lo cambia | `validadores/pruebas.py` | 2,5 |
| T-02 | Caso de prueba: el `CLAUDE.md` del proyecto, con texto propio agregado, sobrevive a una actualización | `plan_pruebas.md` | 2,0 |

### CA-02 — Lo que sí se reemplaza queda dicho

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Levantar qué archivos se reemplazan y qué se conserva, corriendo la puesta al día sobre un proyecto de prueba | `resultado_pruebas.md` | 2,5 |
| T-04 | Caso de prueba: el registro de la versión dice qué se actualizó | `plan_pruebas.md` | 1,5 |

### RNF — Que actualizar sea seguro

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-05 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 5 tareas · 10,0 horas.**

---

## 4. Secuencia de ejecución

T-01 primero, que es la prueba dura. T-02 después. T-03 → T-04 al final, y T-05 cierra.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Archivo modificado a mano que sobrevive, incluido el del proyecto | T-01, T-02 |
| CA-02 | Lista de qué se reemplaza, y el registro que lo dice | T-03, T-04 |

---

## 6. Datos y ambiente de prueba

Proyectos de prueba en carpetas temporales. No se instala ni se actualiza ningún proyecto vivo. Ningún dato real y ninguna clave.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase. Las carpetas de prueba se borran al terminar.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

No aplica: no se toca el instalador. Sin subida de versión.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-spec-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`00·N1`](../../../../../base/00-nucleo-blindado.md), [`00·N4`](../../../../../base/00-nucleo-blindado.md), [`02·F13`](../../../../../base/02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md), [`15`](../../../../../base/15-registros-inmutables.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que la prueba encuentre que sí se pisa algo | Defecto grave en producción | Se para, se reporta al usuario y no se sigue con el resto de la fase hasta que se decida |
| R-02 | Que la corrida de prueba se haga sobre un proyecto vivo | Daño en trabajo ajeno | Copia temporal, declarado como condición de arranque |
| R-03 | Que el registro de la versión mienta por los pendientes 44 y 46 | El CA-02 quedaría probado sobre un registro que se contradice | Se prueba igual y se anota: es la evidencia que esos pendientes necesitan |

---

## 11. Definition of Done

- [ ] Hay prueba de que un archivo modificado a mano no se cambia al actualizar.
- [ ] El archivo del proyecto con texto propio sobrevive a una actualización.
- [ ] La lista de qué se reemplaza y qué se conserva está escrita.
- [ ] Lo que el registro de la versión dice después de actualizar quedó anotado.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
