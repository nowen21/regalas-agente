# Plan de Trabajo — Fase A-EP-004-HU-017-la-corrida-cuenta-las-hu-sin-fase (módulo Comprobación automática)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-017](../HU-017-inventario-de-hu-sin-fase.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-017-la-corrida-cuenta-las-hu-sin-fase` |
| **Épica** | [EP-004 Comprobación automática](../../epica.md) |
| **HU** | [HU-017 Decir cuántas HU quedan sin su fase completa](../HU-017-inventario-de-hu-sin-fase.md) — una sola (`F12.1`) |
| **Módulo** | Comprobación automática |
| **Especificación del módulo** | [HU-017](../HU-017-inventario-de-hu-sin-fase.md). El entregable es una línea de resumen en un programa que ya corre: sus criterios de aceptación son la especificación |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-004-HU-017-la-corrida-cuenta-las-hu-sin-fase` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): ✨ **Funcionalidad nueva**, y la más chica de la épica. [`fases.py`](../../../../../validadores/fases.py) **ya lista** la HU sin fase (`F12.2`) y los documentos que le faltan a cada una (`F12.13`) — hoy 54 avisos. Lo que no da es el **total**, y por eso la cuenta del 2026-08-16 se hizo en un script aparte que no quedó en el repositorio. La HU nació ese día, del hallazgo H-1 del [inventario de HU](../../../../../historico-chat/resumenes/2026-08-16/las-hu-sin-su-fase.md). Sale de su fila en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-017 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-017-inventario-de-hu-sin-fase.md#ca-01--la-corrida-dice-el-total-las-completas-y-las-incompletas) | La corrida dice el total, las completas y las incompletas | **No está.** El resumen dice cuántos avisos, no cuántas HU |
| [CA-02](../HU-017-inventario-de-hu-sin-fase.md#ca-02--el-total-coincide-con-las-carpetas-que-hay) | El total coincide con las carpetas que hay | **No está.** Es lo que hoy se desincroniza: el pendiente 48 decía 66 cuando ya eran 68 |
| [CA-03](../HU-017-inventario-de-hu-sin-fase.md#ca-03--una-hu-con-dos-fases-cuenta-como-completa-solo-si-las-dos-lo-están) | Una HU con dos fases cuenta como completa solo si las dos lo están | **No está**, y hay un caso real: [EP-005 · HU-008](../../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/HU-008-enganche-del-resumen.md) tiene dos fases |
| [CA-04](../HU-017-inventario-de-hu-sin-fase.md#ca-04--caso-borde-la-épica-sin-hu-y-la-carpeta-hu-sin-su-archivo) | Caso borde: la épica sin HU y la carpeta HU sin su archivo | **No está.** Y son casos que ya se dan: [`flujo.py`](../../../../../validadores/flujo.py) tiene avisos para el padre que falta |

**Por qué una sola fase.** Los cuatro CA son la misma línea de resumen y sus tres bordes (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** que la cuenta de cuánto falta la haga el programa y no una edición a mano, para que no se vuelva a perder ni a contradecir con el tablero.

**Fuera de alcance:**

- **Llenar las filas del inventario.** Eso es el trabajo del pendiente [48](../../../../../pendientes/48-inventario-hu.md); esta HU solo cuenta.
- **Escribir la cuenta en el pendiente.** El programa la reporta; quién la copia al tablero y cuándo es otra decisión.
- **El número de las demás cosas** —pendientes, reglas, señales—: acá se cuentan HU y fases.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17: `validar.py fases` termina en «0 fallas, 54 avisos» y no dice cuántas HU hay.

**Lo que ya existe:** el programa que recorre el árbol y ya sabe qué HU no tiene fase y qué documentos le faltan a cada fase; el formato del resumen, que ya cuenta fallas y avisos; el tablero del pendiente 48, con la cuenta a mano y su advertencia de corregir los dos números en la misma edición; y la evidencia de que a mano se desincroniza: el 2026-08-16 el README del backlog decía 66 y la tabla ya iba en 68.

**Lo que no existe:**

1. **La línea del total.** El programa sabe todo lo que hace falta y no lo suma.
2. **El criterio de «completa» escrito en el programa.** Hoy vive en el tablero: fila con seis casillas marcadas.
3. **Los bordes.** La épica sin HU y la carpeta de HU sin su archivo no están resueltos para la cuenta.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/fases.py` | Modificar | La línea del total, con el criterio de completa y los bordes |
| `validadores/docs/fases.md` | Modificar | Qué cuenta la línea y qué se considera completa |
| `validadores/pruebas.py` | Modificar | Los casos de los cuatro CA |
| `…/A-EP-004-HU-017-…/plan_pruebas.md` · `resultado_pruebas.md` | Nuevo | Los casos y lo que dieron |
| `HU-017-inventario-de-hu-sin-fase.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila, y la cuenta que dé el programa |

> La línea se suma al programa que ya recorre el árbol: no hay programa nuevo.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

| Archivo que cambia | Qué cambia | Quién depende | Dónde |
|---|---|---|---|
| `validadores/fases.py` | Una línea más en el resumen | Los enganches y las pruebas que leen esa salida | Se agrega al final: nada de lo que ya se imprime cambia de forma |

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque son programas de línea de comandos.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

**Sí tiene punto de entrada:** `validar.py fases`, que es donde va la línea nueva.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La cuenta va en el programa que ya recorre el árbol | Un programa nuevo que cuente | Recorrer dos veces el mismo árbol da dos verdades cuando uno de los dos se queda viejo |
| «Completa» es la HU cuyas fases tienen sus cinco documentos | Contar completa la HU que tiene al menos una fase | Es el criterio que el tablero ya usa, y cambiarlo haría que los dos números no se puedan comparar |
| La cuenta se reporta, no se escribe en el tablero | Que el programa edite el pendiente 48 | Un programa que edita el backlog pisa lo que otra sesión esté escribiendo |

### 2.7 Dudas por resolver antes de escribir

Ninguna: el criterio de completa lo fija el tablero del pendiente 48, y los bordes están verificados en el árbol.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — La corrida dice el total, las completas y las incompletas

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Sumar al final de la corrida la línea con el total, las completas y las incompletas | `validadores/fases.py` | 2,0 |
| T-02 | Caso de prueba: con dos HU, una completa y otra no, la línea dice 2, 1 y 1 | `plan_pruebas.md` | 1,5 |

### CA-02 — El total coincide con las carpetas que hay

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Prueba: el total que reporta la corrida es el número de carpetas de HU del árbol | `validadores/pruebas.py` | 2,0 |

### CA-03 — Una HU con dos fases cuenta como completa solo si las dos lo están

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-04 | Que una HU con varias fases cuente completa solo si todas tienen sus cinco documentos | `validadores/fases.py` | 1,5 |
| T-05 | Caso de prueba: sobre la HU que tiene dos fases, quitar un documento de una y ver que la HU deja de contar completa | `plan_pruebas.md` | 1,5 |

### CA-04 — Caso borde: la épica sin HU y la carpeta HU sin su archivo

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-06 | Que la épica sin HU no rompa la cuenta, y que la carpeta HU sin su archivo se cuente como incompleta | `validadores/fases.py` | 1,5 |
| T-07 | Caso de prueba: los dos bordes, en carpeta temporal | `plan_pruebas.md` | 1,5 |

### RNF — Que la cuenta no vuelva a perderse

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-08 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 8 tareas · 13,0 horas.**

---

## 4. Secuencia de ejecución

T-01 → T-04 → T-06 en el programa, y T-02, T-03, T-05, T-07 detrás de cada uno. T-08 cierra.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Árbol de dos HU, una completa | T-01, T-02 |
| CA-02 | Total contra el número de carpetas del árbol | T-03 |
| CA-03 | La HU con dos fases, con un documento quitado | T-04, T-05 |
| CA-04 | Épica sin HU y carpeta HU sin su archivo | T-06, T-07 |

---

## 6. Datos y ambiente de prueba

Este repositorio y carpetas temporales para los casos negativos. Ningún dato real y ninguna clave.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

El estándar está en producción. Es **aditivo** —una línea más en un resumen—: subida **MENOR**. Ningún proyecto tiene que hacer nada distinto.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`02·F12`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que la cuenta del programa y la del tablero no coincidan | Nadie sabe cuál creer | La corrida manda, y el resultado dice cuál era la diferencia el día que se midió |
| R-02 | Que contar cambie el código de salida | Un total alto dejaría el proyecto en rojo | La línea informa: no agrega fallas |
| R-03 | Que la HU se lea como que resuelve el pendiente 48 | Se creería que las filas se llenan solas | El README de la fase lo dice: esto cuenta, no llena |

---

## 11. Definition of Done

- [ ] La corrida termina diciendo total, completas e incompletas.
- [ ] El total coincide con las carpetas del árbol, con prueba.
- [ ] Una HU con dos fases cuenta completa solo si las dos lo están.
- [ ] Los dos bordes no rompen la cuenta.
- [ ] La cuenta del programa quedó comparada con la del tablero.
- [ ] `CHANGELOG.md` con su entrada y `VERSION` subida.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
