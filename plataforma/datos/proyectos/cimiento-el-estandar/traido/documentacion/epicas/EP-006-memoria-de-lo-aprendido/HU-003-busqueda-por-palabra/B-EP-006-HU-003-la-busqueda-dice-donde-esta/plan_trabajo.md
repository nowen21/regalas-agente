# Plan de Trabajo — Fase B-EP-006-HU-003-la-busqueda-dice-donde-esta (módulo Memoria)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-003](../HU-003-busqueda-por-palabra.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `B-EP-006-HU-003-la-busqueda-dice-donde-esta` |
| **Épica** | [EP-006 Memoria de lo aprendido](../../epica.md) |
| **HU** | [HU-003 Buscar por palabra sin instalar nada](../HU-003-busqueda-por-palabra.md) — una sola (`F12.1`) |
| **Complementa** | [`A-EP-006-HU-003`](../A-EP-006-HU-003-retrodocumentar-la-busqueda-por-palabra/resultado_pruebas.md), que cerró en **No cumple** |
| **Módulo** | Memoria |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/B-EP-006-HU-003-la-busqueda-dice-donde-esta` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 🐞 **Defecto**. La fase A ejecutó su plan completo y dejó el CA-01 en «No»: la búsqueda encuentra y **no dice dónde está lo que encontró**. Los dos defectos que lo causan están probados con `expectedFailure` en [`memoria/pruebas.py`](../../../../../memoria/pruebas.py); arreglarlos no cabía en el plan de la fase A, que declara que `memoria.py` no se toca ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

**CA de la HU que cubre esta fase**

| CA de HU-003 | Qué exige | Estado tras la fase A |
|---|---|---|
| [CA-01](../HU-003-busqueda-por-palabra.md#ca-01--se-busca-por-palabra-y-aparece-dónde-está) | Se busca por palabra y **aparece dónde está** | **En «No».** Encuentra, con acentos y sin ellos, pero no imprime `where_`. El CA se da por aprobado «cuando el resultado alcanza para abrir lo que se encontró», y no alcanza |

**Por qué una sola fase para dos arreglos.** Los dos tocan la misma función, `cmd_search`, y los dos tienen su prueba ya escrita esperando. Partirlos daría dos fases que tocan el mismo bloque de veinte líneas, que es lo que prohíbe `02·F12.10`.

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** que el resultado de la búsqueda alcance para abrir lo que se encontró, y que el camino sin resultados no deje la base tomada.

**Fuera de alcance:**

- **Cambiar qué se busca o cómo se ordena.** La relevancia, los filtros y la fusión con la semántica no se tocan.
- **Los otros defectos de la memoria.** El de `HU-004` —que sin el modelo la búsqueda se cae— es su propia fase `B`.
- **Rediseñar la salida.** Se le agrega un dato a la línea; no se cambia el formato de las demás.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17 leyendo `memoria/memoria.py` y corriendo la suite.

**Lo que ya existe:** la columna `where_` en el esquema, poblada por `memoria.py add --where`; la búsqueda léxica e híbrida; y **las dos pruebas que fallan a propósito**, `test_el_resultado_dice_donde_esta_la_senal` y `test_la_busqueda_sin_resultados_cierra_su_conexion`, marcadas `expectedFailure` en la clase `BusquedaPorPalabra`.

**Lo que no existe:**

1. **`where_` en la salida.** `cmd_search` selecciona `rowid, id, tipo, titulo, scope, revisada` y no lo trae.
2. **El cierre de la conexión** en el camino que imprime «(sin señales relevantes)» y retorna.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `memoria/memoria.py` | Modificar | `cmd_search`: agregar `where_` al `SELECT` y a la línea; cerrar la conexión antes del `return` del camino vacío |
| `memoria/pruebas.py` | Modificar | Quitarles el `expectedFailure` a las dos pruebas, y sumar el caso de la señal **sin** `where_` |
| `…/B-EP-006-HU-003-…/plan_pruebas.md` · `resultado_pruebas.md` | Nuevo | Los casos y lo que dieron |
| `HU-003-busqueda-por-palabra.md` | Modificar | §8 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | La fila de HU-003 vuelve a quedar completa |

> El esquema **no** se toca: la columna ya existe.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

`cmd_search` la llama `validar.py` de ninguna forma y `memoria.py search` desde la línea de comandos. **Lo único que cambia de contrato es la línea que imprime**, y nada la lee de vuelta: no hay programa que la parsee. Las pruebas de la clase `BusquedaPorPalabra` sí la leen, y son parte de esta fase.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica: es un programa de línea de comandos sobre una base local.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

`python memoria/memoria.py search "…"`. Esta fase no lo cambia; cambia lo que imprime.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| `where_` va al final de la línea, entre paréntesis, y **solo si tiene valor** | Una columna fija, vacía cuando no hay dato | Una señal sin `where_` es normal —el criterio de `13·DOC5` no lo exige— y una columna vacía en cada línea ensucia la salida de todas para servir a algunas |
| La conexión se cierra en el camino vacío, sin reestructurar la función | Envolver `cmd_search` en un `with` | Reestructurar toca los tres caminos de salida y el riesgo no lo paga: el defecto es una línea |
| Las dos pruebas **se destapan**, no se reescriben | Escribir pruebas nuevas y borrar las viejas | Están escritas contra el criterio y ya describen el defecto. Quitarles la marca es lo que convierte el rojo esperado en verde real |

### 2.7 Dudas por resolver antes de escribir

Ninguna. Los dos defectos están medidos, sus pruebas escritas y el arreglo es de una línea cada uno.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Se busca por palabra y aparece dónde está

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Agregar `where_` al `SELECT` de `cmd_search` y a la línea que imprime, solo cuando tiene valor | `memoria/memoria.py` | 1,0 |
| T-02 | Quitarle el `expectedFailure` a `test_el_resultado_dice_donde_esta_la_senal` | `memoria/pruebas.py` | 0,5 |
| T-03 | Prueba: una señal **sin** `where_` sale sin paréntesis vacíos y no rompe la línea | `memoria/pruebas.py` | 1,0 |

### RNF — Inocuidad: buscar no modifica lo guardado

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-04 | Cerrar la conexión antes del `return` del camino sin resultados | `memoria/memoria.py` | 0,5 |
| T-05 | Quitarle el `expectedFailure` a `test_la_busqueda_sin_resultados_cierra_su_conexion` | `memoria/pruebas.py` | 0,5 |
| T-06 | Comprobar que la carpeta temporal se puede borrar sin `ignore_cleanup_errors` | `memoria/pruebas.py` | 1,0 |

### Cierre

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-07 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 7 tareas · 6,0 horas.**

---

## 4. Secuencia de ejecución

T-01 y T-04 son los dos arreglos, y se pueden hacer juntos: son la misma función. T-02 y T-05 destapan las pruebas que ya existen — **el orden importa**: si se destapan antes de arreglar, la suite queda en rojo y no se sabe si el arreglo funcionó o si la prueba estaba mal. T-03 y T-06 suman lo que falta. T-07 cierra.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método de verificación | Evidencia |
|---|---|---|
| CA-01 | Buscar una señal guardada con `--where` y comprobar que la ubicación sale en la línea | T-02, y el caso de T-03 para la que no lo tiene |
| RNF · Inocuidad | Buscar sin resultados y borrar el archivo de la base | T-05, T-06 |

---

## 6. Datos y ambiente de prueba

Bases temporales, como en la fase A. Ninguna prueba toca `memoria/senales.db`: la clase compara su huella SHA-256 antes y después ([`08·T4`](../../../../../base/08-pruebas.md)).

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase. Lo que cambia es una consulta y una línea impresa; deshacerlo devuelve la salida anterior y no deja datos que restaurar.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

El esquema no cambia, así que ninguna base existente necesita migración. La salida de `search` cambia para todos los proyectos que la usen, y es **aditiva**: se agrega un dato al final de la línea.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`05·E1`](../../../../../base/05-errores-y-logging.md), [`08·T4`](../../../../../base/08-pruebas.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que agregar `where_` alargue la línea y la vuelva ilegible con rutas largas | La salida se ensucia | Va al final y solo cuando hay dato; si molesta, se decide con la salida a la vista | Abierto |
| R-02 | Que al destapar las pruebas aparezca que el defecto era otro | La fase no cierra donde creía | Es el resultado honesto: se escribe qué salió y se propone | Abierto |
| R-03 | Que otra sesión esté tocando `memoria/` | Se mezcla el versionado | Se guarda solo lo propio | Abierto |

---

## 11. Definition of Done

- [ ] La búsqueda imprime dónde está la señal, cuando lo tiene.
- [ ] Una señal sin `where_` sale limpia, sin paréntesis vacíos.
- [ ] El camino sin resultados cierra su conexión, y la carpeta temporal se borra sin ayuda.
- [ ] Las dos pruebas de fallo esperado quedan en verde **sin la marca**.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §8 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: es una fase de una sola sesión, y su avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
