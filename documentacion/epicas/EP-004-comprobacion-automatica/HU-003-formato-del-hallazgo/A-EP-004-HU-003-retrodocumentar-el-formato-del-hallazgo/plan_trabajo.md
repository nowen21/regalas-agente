# Plan de Trabajo — Fase A-EP-004-HU-003-retrodocumentar-el-formato-del-hallazgo (módulo Comprobación automática)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-003](../HU-003-formato-del-hallazgo.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-003-retrodocumentar-el-formato-del-hallazgo` |
| **Épica** | [EP-004 Comprobación automática](../../epica.md) |
| **HU** | [HU-003 Definir el formato de un hallazgo y su severidad](../HU-003-formato-del-hallazgo.md) — una sola (`F12.1`) |
| **Módulo** | Comprobación automática |
| **Especificación del módulo** | [HU-003](../HU-003-formato-del-hallazgo.md). El entregable es el formato con que hablan los validadores: sus criterios de aceptación son la especificación |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-004-HU-003-retrodocumentar-el-formato-del-hallazgo` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📄 **Retro-documentación** ([`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md)). El formato existe y lo usan los 24 subcomandos: [`validadores/comun.py`](../../../../../validadores/comun.py) define el hallazgo con su severidad —`FALLA` rompe la ejecución, `AVISO` no— y la salida dice archivo, línea y qué regla se incumplió. Sale de la fila de HU-003 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-003 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-003-formato-del-hallazgo.md#ca-01--el-hallazgo-alcanza-para-arreglar-sin-abrir-el-programa) | El hallazgo alcanza para arreglar sin abrir el programa | Se cumple en la práctica: cada línea trae archivo, línea y la regla citada. Sin prueba que lo fije |
| [CA-02](../HU-003-formato-del-hallazgo.md#ca-02--lo-dudoso-sale-como-aviso-y-no-detiene) | Lo dudoso sale como aviso y no detiene | Cumplido: el aviso no cambia el código de salida. Sin prueba propia de esta HU |
| [CA-03](../HU-003-formato-del-hallazgo.md#ca-03--una-falla-detiene) | Una falla detiene | Cumplido: con una falla, el código de salida es 1. Sin prueba propia |

**Por qué una sola fase.** Los tres CA se comprueban sobre la misma salida y la misma corrida (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** dejar escrito y probado el contrato de la salida —qué trae un hallazgo y qué hace cada severidad— para que nadie tenga que abrir un validador para entender lo que reportó.

**Fuera de alcance:**

- **Los mensajes de cada validador uno por uno.** Acá se prueba el formato, no la redacción de los 24.
- **El conteo por regla,** que es [HU-009](../../HU-009-conteo-por-regla/HU-009-conteo-por-regla.md).
- **La corrida completa,** que es [HU-008](../../HU-008-corrida-completa/HU-008-corrida-completa.md).
- **Cambiar las severidades.** Son dos y así se quedan; una tercera sería otra decisión.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17 leyendo `comun.py` y las corridas de `estandar`, `fases`, `flujo` y `trazabilidad`.

**Lo que ya existe:** las dos severidades, con su efecto declarado en el propio archivo —la falla rompe la ejecución, el aviso lo mira un humano—; el hallazgo con archivo, línea, severidad y texto; la función que imprime y devuelve el código de salida; y la línea de resumen que cierra cada corrida con cuántas fallas y cuántos avisos.

**Lo que no existe:**

1. **La prueba del contrato.** Que la salida siempre traiga archivo, línea y regla no lo comprueba nadie: si un validador nuevo reporta sin línea, nada avisa.
2. **La prueba del código de salida** por criterio de esta HU.
3. **El registro de por qué hay dos severidades y no tres.** Está en el código como comentario, no como decisión escrita.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/pruebas.py` | Modificar | Pruebas del código de salida con solo avisos y con una falla |
| `validadores/docs/comun.md` | Modificar | Le entra el contrato de la salida: qué trae un hallazgo y qué hace cada severidad |
| `…/A-EP-004-HU-003-…/plan_pruebas.md` | Nuevo | Los casos de los tres CA |
| `…/A-EP-004-HU-003-…/resultado_pruebas.md` | Nuevo | Lo que dieron |
| `HU-003-formato-del-hallazgo.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> `comun.py` no se toca: el formato ya es el que la HU pide.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna: se agregan pruebas contra el comportamiento que ya tiene `comun.py`, sin cambiarlo.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque son programas de línea de comandos.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

**Sí tiene punto de entrada:** cualquiera de los 24 subcomandos de `validar.py` muestra el formato en su salida.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El contrato se escribe en la documentación del módulo común | Escribirlo como regla de `base/` | El formato de la salida es de esta herramienta; `base/` es agnóstico de herramienta ([`20·M3`](../../../../../base/20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md)) |
| Las pruebas del código de salida se hacen sobre hallazgos armados | Correr un validador real y provocar la falla | Con hallazgos armados la prueba no depende de que exista un archivo roto en el repositorio |
| Se prueba que el hallazgo trae los tres datos, no que el texto esté bien redactado | Revisar la redacción de los 24 | La redacción es criterio; los tres datos son sí o no |

### 2.7 Dudas por resolver antes de escribir

Ninguna: todo lo que la fase afirma se verificó contra el repositorio.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — El hallazgo alcanza para arreglar sin abrir el programa

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Caso de prueba: tomar diez hallazgos de una corrida real y comprobar que cada uno trae archivo, línea y regla | `plan_pruebas.md` | 2,0 |
| T-02 | Caso de prueba: arreglar dos de ellos sin abrir el programa que los reportó | `plan_pruebas.md` | 1,5 |

### CA-02 — Lo dudoso sale como aviso y no detiene

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Prueba: una corrida con solo avisos termina con código de salida 0 | `validadores/pruebas.py` | 1,5 |

### CA-03 — Una falla detiene

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-04 | Prueba: una corrida con una falla termina con código de salida 1 | `validadores/pruebas.py` | 1,5 |

### RNF — Que el contrato de la salida quede escrito

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-05 | Escribir el contrato en la documentación del módulo común, correr las pruebas y cerrar la trazabilidad | Cierre | 1,5 |

**Total: 5 tareas · 8,0 horas.**

---

## 4. Secuencia de ejecución

T-03 → T-04 primero, que son pruebas cortas. T-01 → T-02 después, sobre una corrida real. T-05 cierra.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Diez hallazgos revisados, y dos arreglados sin abrir el programa | T-01, T-02 |
| CA-02 | Prueba del código de salida con solo avisos | T-03 |
| CA-03 | Prueba del código de salida con una falla | T-04 |

---

## 6. Datos y ambiente de prueba

Este repositorio, con hallazgos armados en memoria para las pruebas del código de salida. Ningún dato real y ninguna clave.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase. Lo único ejecutable que entra son dos pruebas.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

No aplica: no cambia el comportamiento de ningún validador instalado. Sin subida de versión.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`05`](../../../../../base/05-errores-y-logging.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`20·M3`](../../../../../base/20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que algún validador reporte sin línea y la prueba del CA-01 lo destape | Se destapa trabajo en otro archivo | Se anota con el validador y la corrida; corregirlo es de su propia fase |
| R-02 | Que la prueba del código de salida choque con la suite en rojo por trabajo ajeno | No se distingue lo propio | Se anota el estado de la suite antes de tocarla |
| R-03 | Que el contrato escrito se quede viejo cuando alguien agregue un validador | Documento que miente | La prueba del CA-01 recorre todos los hallazgos de la corrida, así que un validador nuevo entra solo |

---

## 11. Definition of Done

- [ ] El contrato de la salida está escrito: qué trae un hallazgo y qué hace cada severidad.
- [ ] Hay prueba de que solo avisos no detiene y una falla sí.
- [ ] Diez hallazgos reales quedaron revisados, y dos arreglados sin abrir el programa.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
