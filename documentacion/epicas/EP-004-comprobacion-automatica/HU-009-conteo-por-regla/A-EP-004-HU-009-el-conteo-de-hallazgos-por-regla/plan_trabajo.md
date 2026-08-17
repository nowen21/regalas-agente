# Plan de Trabajo — Fase A-EP-004-HU-009-el-conteo-de-hallazgos-por-regla (módulo Comprobación automática)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-009](../HU-009-conteo-por-regla.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-009-el-conteo-de-hallazgos-por-regla` |
| **Épica** | [EP-004 Comprobación automática](../../epica.md) |
| **HU** | [HU-009 Registrar cuántos hallazgos hubo por regla](../HU-009-conteo-por-regla.md) — una sola (`F12.1`) |
| **Módulo** | Comprobación automática |
| **Especificación del módulo** | [HU-009](../HU-009-conteo-por-regla.md). El entregable es un registro de conteos: sus criterios de aceptación son la especificación |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-004-HU-009-el-conteo-de-hallazgos-por-regla` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): ✨ **Funcionalidad nueva.** Acá **no hay nada construido**: los validadores cuentan fallas y avisos del total de la corrida, y ninguno agrupa por regla. Lo más parecido es [`metricas/`](../../../../../metricas/README.md), que mide señales del proceso y no hallazgos. Sale de la fila de HU-009 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-009 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-009-conteo-por-regla.md#ca-01--la-corrida-deja-el-conteo-por-regla) | La corrida deja el conteo por regla | **No está.** El resumen dice «0 fallas, 54 avisos» y no por cuál regla |
| [CA-02](../HU-009-conteo-por-regla.md#ca-02--el-registro-no-guarda-lo-revisado) | El registro no guarda lo revisado | **No está**, y es la parte delicada: un registro de hallazgos podría arrastrar el contenido del archivo revisado |
| [CA-03](../HU-009-conteo-por-regla.md#ca-03--dos-corridas-se-pueden-comparar) | Dos corridas se pueden comparar | **No está.** Sin conteo no hay con qué comparar |

**Por qué una sola fase.** Los tres CA son el mismo registro: qué guarda, qué no guarda y para qué sirve (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** saber por cuál regla se incumple más, para decidir qué regla cambiar — sin que el registro se convierta en una copia de lo revisado.

**Fuera de alcance:**

- **Usar el conteo para calificar el trabajo.** Es la advertencia que [`metricas/`](../../../../../metricas/README.md) pone primero y no se negocia: una métrica visible se vuelve objetivo y deja de medir.
- **La corrida completa,** que es [HU-008](../../HU-008-corrida-completa/HU-008-corrida-completa.md) y va antes: sin corrida única, el conteo queda partido en 24.
- **El formato del hallazgo,** que es [HU-003](../../HU-003-formato-del-hallazgo/HU-003-formato-del-hallazgo.md).

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17: `comun.py` no agrupa por regla, y `metricas/metricas.py` deriva de las señales del proceso, no de los hallazgos.

**Lo que ya existe:** el formato del hallazgo, que ya cita la regla dentro de su texto; el resumen por corrida con el total de fallas y avisos; el módulo de métricas, con su advertencia escrita de que los números orientan qué norma cambiar y no califican a nadie; y el registro de reglas validables, que dice qué regla mira cada programa.

**Lo que no existe:**

1. **La regla como dato.** Hoy el identificador va dentro del texto del hallazgo, así que agrupar por regla obligaría a leer prosa.
2. **El registro de conteos.** No existe ni el archivo ni su formato.
3. **La decisión de dónde vive.** El conteo de un proyecto no puede quedar en la carpeta que no se versiona, ni ensuciar el repositorio con un archivo por corrida.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/comun.py` | Modificar | El hallazgo declara su regla como dato, no solo dentro del texto |
| `validadores/validar.py` | Modificar | El conteo por regla al terminar la corrida, con fecha y versión |
| `validadores/pruebas.py` | Modificar | Las pruebas del CA-02 y del CA-03 |
| `validadores/docs/comun.md` · `docs/validar.md` | Modificar | Qué se guarda y qué no |
| `…/A-EP-004-HU-009-…/plan_pruebas.md` | Nuevo | Los casos de los tres CA |
| `…/A-EP-004-HU-009-…/resultado_pruebas.md` | Nuevo | Lo que dieron |
| `HU-009-conteo-por-regla.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> Los 24 validadores no se tocan uno por uno: la regla sale del hallazgo que ya construyen.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

| Archivo que cambia | Qué cambia | Quién depende | Dónde |
|---|---|---|---|
| `validadores/comun.py` | El hallazgo gana un campo | Los 24 validadores que lo construyen, y las 246 pruebas | El campo entra con valor por omisión, así que nada de lo que ya lo construye rompe; lo que no lo llene, no cuenta por regla |

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque son programas de línea de comandos.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

El conteo se ve al terminar la corrida, en la misma salida. No hay interfaz gráfica.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El campo de la regla entra con valor por omisión | Cambiar de golpe los 24 validadores | Con valor por omisión nada rompe, y los validadores lo van llenando de a uno |
| El registro guarda identificador, número y fecha | Guardar el hallazgo entero para poder revisarlo después | Un registro con el texto del hallazgo arrastra el contenido revisado, y eso choca con `00·N6` y con el capítulo de privacidad |
| El conteo se compara por regla, no por proyecto | Un tablero por proyecto | La HU pide saber qué regla se incumple; comparar proyectos es calificar trabajo, y eso está fuera de alcance |

### 2.7 Dudas por resolver antes de escribir

| # | Duda | A quién | Estado |
|---|---|---|---|
| 1 | Dónde vive el registro de conteos: en la carpeta versionada del proyecto, en la que no se versiona, o solo en la salida de la corrida | Usuario | Pendiente |
| 2 | Si esta fase espera a que exista la corrida completa de HU-008, que es la que le da un único punto donde contar | Usuario | Pendiente |

Las dos bloquean T-02 en adelante. T-01 —la regla como dato— se puede hacer sin ellas.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — La corrida deja el conteo por regla

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Que cada hallazgo diga a qué regla pertenece de forma que se pueda agrupar | `validadores/comun.py` | 2,5 |
| T-02 | Que la corrida deje el conteo por regla al terminar | `validadores/validar.py` | 2,5 |

### CA-02 — El registro no guarda lo revisado

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Que el registro guarde solo el identificador de la regla y el número, nunca el texto del hallazgo ni la línea del archivo | `validadores/validar.py` | 2,0 |
| T-04 | Prueba: el registro de una corrida sobre un archivo con una clave no contiene la clave | `validadores/pruebas.py` | 2,0 |

### CA-03 — Dos corridas se pueden comparar

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-05 | Que el registro lleve fecha y versión del estándar, para poder poner dos corridas al lado | `validadores/validar.py` | 1,5 |
| T-06 | Caso de prueba: dos corridas con un arreglo en medio muestran la baja en la regla arreglada | `plan_pruebas.md` | 2,0 |

### RNF — Que el número sirva para decidir y no para puntuar

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-07 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 7 tareas · 14,0 horas.**

---

## 4. Secuencia de ejecución

T-01 primero, que no depende de las dudas. T-02 → T-03 → T-05 con las dudas resueltas. T-04, T-06 y T-07 cierran.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Corrida que deja el conteo agrupado por regla | T-01, T-02 |
| CA-02 | Registro de una corrida sobre un archivo con una clave, que no la contiene | T-03, T-04 |
| CA-03 | Dos corridas con un arreglo en medio, comparadas | T-05, T-06 |

---

## 6. Datos y ambiente de prueba

Este repositorio y carpetas temporales para los casos negativos. Ningún dato real y ninguna clave: lo que parezca una clave se arma para la prueba.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

El estándar está en producción. El campo nuevo del hallazgo es **aditivo** y entra con valor por omisión: subida **MENOR**. Si el registro se guarda en una carpeta del proyecto, hay que decir dónde y eso sí obliga — se declara al cerrar, con la duda 1 resuelta.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-spec-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`00·N6`](../../../../../base/00-nucleo-blindado.md), [`12`](../../../../../base/12-privacidad-datos.md), [`15`](../../../../../base/15-registros-inmutables.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Las dos dudas sin resolver | Bloquean casi toda la fase | Se presentan al usuario antes de tocar `comun.py` |
| R-01 | Que el conteo se use para calificar el trabajo | Deja de medir | La advertencia se escribe en la documentación del conteo, no solo en `metricas/` |
| R-02 | Que el registro arrastre contenido revisado | Filtración por la puerta de atrás | El CA-02 es exactamente esa prueba, y va antes de dar la fase por buena |
| R-03 | Que el campo nuevo rompa alguna de las 246 pruebas | Suite roja | Entra con valor por omisión, y la suite se corre completa antes y después |

---

## 11. Definition of Done

- [ ] El hallazgo declara su regla como dato.
- [ ] La corrida deja el conteo por regla, con fecha y versión.
- [ ] Está probado que el registro no guarda lo revisado.
- [ ] Dos corridas se pueden poner al lado y se ve la baja.
- [ ] La advertencia de para qué sirve el número quedó escrita.
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
