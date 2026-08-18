# Plan de Trabajo — Fase A-EP-004-HU-013-comparar-lo-hecho-con-el-plan-aprobado (módulo Comprobación automática)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-013](../HU-013-comparar-el-plan-con-lo-hecho.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-013-comparar-lo-hecho-con-el-plan-aprobado` |
| **Épica** | [EP-004 Comprobación automática](../../epica.md) |
| **HU** | [HU-013 Comparar el plan aprobado con lo que se hizo](../HU-013-comparar-el-plan-con-lo-hecho.md) — una sola (`F12.1`) |
| **Módulo** | Comprobación automática |
| **Especificación del módulo** | [HU-013](../HU-013-comparar-el-plan-con-lo-hecho.md). El entregable es un programa de comprobación: sus criterios de aceptación, `02·F8` y `02·F18` son la especificación |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-004-HU-013-comparar-lo-hecho-con-el-plan-aprobado` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 🔀 **Híbrido.** 📄 Retro-documenta lo que ya compara: [`flujo.py`](../../../../../validadores/flujo.py) exige que cada tarea del plan cuelgue de un criterio (`02·F18`), [`fases.py`](../../../../../validadores/fases.py) compara los dos veredictos —lo hizo la fase A de [HU-014](../../HU-014-un-solo-veredicto-por-fase/HU-014-un-solo-veredicto-por-fase.md)— y [`trazabilidad.py`](../../../../../validadores/trazabilidad.py) revisa la tabla de cierre. ✨ Y construye lo que falta: **nadie compara los archivos tocados con los que el plan declaró** (`02·F8`). Sale de la fila de HU-013 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-013 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-013-comparar-el-plan-con-lo-hecho.md#ca-01--avisa-el-archivo-tocado-que-el-plan-no-declara) | Avisa el archivo tocado que el plan no declara | **No está.** `02·F8` lo exige y nada lo comprueba: hoy depende de que quien implementa se acuerde |
| [CA-02](../HU-013-comparar-el-plan-con-lo-hecho.md#ca-02--avisa-el-caso-y-el-criterio-que-no-cuadran) | Avisa el caso y el criterio que no cuadran | Corriendo a medias: `flujo.py` avisa la tarea sin criterio y el criterio sin desglose — hoy 151 avisos. Lo que no mira es el plan de pruebas contra los criterios |
| [CA-03](../HU-013-comparar-el-plan-con-lo-hecho.md#ca-03--avisa-el-caso-cuyos-pasos-no-son-los-del-plan) | Avisa el caso cuyos pasos no son los del plan | **No está**, y es el más difícil: comparar pasos es comparar prosa |

**Por qué una sola fase.** Los tres CA comparan el mismo par de documentos —el plan y lo que quedó— y se prueban sobre las mismas fases cerradas (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** que la comparación entre lo aprobado y lo hecho no dependa de que alguien se acuerde, y que quede dicho qué parte de esa comparación no la puede hacer un programa.

**Fuera de alcance:**

- **El veredicto por fase,** ya retro-documentado en [HU-014](../../HU-014-un-solo-veredicto-por-fase/HU-014-un-solo-veredicto-por-fase.md).
- **Los 151 avisos de `F18`** que hay hoy: se cuentan como línea base, se arreglan en la fase de cada HU.
- **Juzgar si el plan estaba bien.** Acá se compara plan contra hecho, no la calidad del plan.
- **Reabrir fases cerradas.** Lo que aparezca se anota.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17: `flujo.py` comprueba `F18` y la especificación declarada; ningún programa lee la tabla de archivos del §2.1.

**Lo que ya existe:** la comprobación de que cada tarea cuelgue de un criterio; la comparación de los dos veredictos, que ya distingue lo que dice el resultado de pruebas de lo que dice el cierre; la revisión de la tabla de cierre; y la exigencia escrita de tocar solo los archivos que el plan declara.

**Lo que no existe:**

1. **La comparación de archivos.** Nadie lee la tabla del §2.1 y la contrasta con lo que la rama tocó, que es la mitad concreta de `02·F8`.
2. **La comparación de casos contra criterios.** El programa mira el plan de trabajo; el plan de pruebas no entra en esa cuenta.
3. **La decisión sobre el CA-03.** Comparar pasos escritos con pasos ejecutados puede no ser comprobable, y eso hay que declararlo en vez de dejarlo pendiente para siempre.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/plan_vs_hecho.py` | Nuevo | La comparación de archivos declarados contra tocados, y de casos contra criterios |
| `validadores/validar.py` | Modificar | Su subcomando |
| `validadores/docs/plan_vs_hecho.md` | Nuevo | Qué compara y qué no |
| `validadores/pruebas.py` | Modificar | Los casos del CA-01 y del CA-02 |
| `validadores/reglas-validables.md` | Modificar | `02·F8` pasa a validador escrito; lo del CA-03 queda declarado según T-06 |
| `…/A-EP-004-HU-013-…/plan_pruebas.md` · `resultado_pruebas.md` | Nuevo | Los casos y lo que dieron |
| `HU-013-comparar-el-plan-con-lo-hecho.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> `flujo.py`, `fases.py` y `trazabilidad.py` no se tocan: lo nuevo va aparte para no mezclar hallazgos.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

| Archivo que cambia | Qué cambia | Quién depende | Dónde |
|---|---|---|---|
| `validadores/validar.py` | Un subcomando nuevo | Los enganches que llaman por nombre | Solo se agrega |
| El formato del §2.1 de los planes | Pasa a leerse por un programa | Los 32 planes ya escritos, que llenan esa tabla a su manera | El programa tiene que aguantar las formas que ya existen, o avisar en vez de fallar: se declara en el resultado |

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque son programas de línea de comandos.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

**Sí tendrá punto de entrada:** su subcomando en `validar.py`.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Los archivos tocados se leen del control de versiones, no de una lista a mano | Pedirle a quien implementa que los liste | Una lista a mano es justo lo que el programa viene a reemplazar |
| El programa avisa y no falla cuando el §2.1 tiene una forma que no entiende | Fallar | Los 32 planes existentes llenan esa tabla de varias formas; fallar dejaría el repositorio en rojo por un formato viejo |
| Si el CA-03 no es comprobable, se declara así | Dejarlo como pendiente indefinido | El registro de reglas validables existe para eso: decir qué no se comprueba es un resultado |

### 2.7 Dudas por resolver antes de escribir

| # | Duda | A quién | Estado |
|---|---|---|---|
| 1 | Contra qué se comparan los archivos tocados: la rama de la fase, el commit único, o lo que esté sin guardar | Usuario | Pendiente |
| 2 | Si el CA-03 se intenta comprobar o se declara criterio humano | Usuario | Pendiente |

La duda 1 bloquea T-01. La duda 2 bloquea T-06, y el caso a mano de T-05 se puede hacer igual.

**Decididas el 2026-08-18**, en el [pendiente 59](../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md). 👤 marca lo que sigue esperando un dato del usuario.

| Duda | Decisión |
|---|---|
| 10 | **Criterio humano, y se declara.** Fingir que se comprueba es peor que decir que no. |
| 22 | **Contra el commit del que salió la fase.** Ni la rama, que arrastra lo ajeno, ni lo sin guardar, que cambia mientras se mira. |

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Avisa el archivo tocado que el plan no declara

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Leer del plan la tabla de archivos de su §2.1 y compararla con los archivos que la rama tocó | `validadores/` | 3,0 |
| T-02 | Caso de prueba: un archivo tocado y no declarado se avisa; uno declarado, no | `plan_pruebas.md` | 2,0 |

### CA-02 — Avisa el caso y el criterio que no cuadran

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Comparar los casos del plan de pruebas con los criterios que la fase declaró | `validadores/` | 2,5 |
| T-04 | Caso de prueba: un criterio sin caso y un caso sin criterio se avisan | `plan_pruebas.md` | 1,5 |

### CA-03 — Avisa el caso cuyos pasos no son los del plan

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-05 | Caso de prueba: decidir a mano, sobre tres fases cerradas, si el resultado ejecutó los pasos que el plan de pruebas decía | `plan_pruebas.md` | 2,5 |
| T-06 | Declarar si esta parte es comprobable por un programa o queda como criterio humano, y registrarlo | `validadores/reglas-validables.md` | 1,5 |

### RNF — Que la comparación no dependa de la memoria de nadie

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-07 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 7 tareas · 14,5 horas.**

---

## 4. Secuencia de ejecución

T-05 primero, que es lectura sobre fases cerradas. T-01 → T-02 con la duda 1. T-03 → T-04 en paralelo. T-06 con la duda 2, y T-07 cierra.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Archivo tocado y no declarado, y archivo declarado | T-01, T-02 |
| CA-02 | Criterio sin caso y caso sin criterio | T-03, T-04 |
| CA-03 | Tres fases cerradas revisadas a mano, y la declaración de si es comprobable | T-05, T-06 |

---

## 6. Datos y ambiente de prueba

Este repositorio y carpetas temporales para los casos negativos. Ningún dato real y ninguna clave.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

El estándar está en producción. El subcomando es **aditivo**: subida **MENOR**. Al correr sobre proyectos con planes viejos va a avisar por formatos que antes nadie leía, y eso se dice en la entrada del registro.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`02·F9`](../../../../../base/02-flujo-de-trabajo/reglas/F9-no-subdividas-ni-renegocies-un-plan-ya-aprobado.md), [`02·F18`](../../../../../base/02-flujo-de-trabajo/reglas/F18-deriva-el-plan-de-los-ca-aprobados-no-de-la-proactividad.md), [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md), [`20·M9`](../../../../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Las dos dudas sin resolver | Bloquean el CA-01 y la declaración del CA-03 | Se presentan al usuario |
| R-01 | Que la tabla del §2.1 tenga demasiadas formas para leerla | El programa avisa siempre y se ignora | Se mide primero sobre los 32 planes que hay, y el resultado dice cuántos se pudieron leer |
| R-02 | Que la comparación de archivos delate incumplimientos de `F8` en fases cerradas | Se destapa trabajo viejo | Se anota; reabrir lo cerrado está fuera de alcance |
| R-03 | Que el CA-03 se quede sin decidir | La fase no cierra | Es la duda 2, y el registro admite declarar que algo no es comprobable |

---

## 11. Definition of Done

- [ ] Un archivo tocado y no declarado se avisa.
- [ ] Un criterio sin caso y un caso sin criterio se avisan.
- [ ] Está decidido y registrado si comparar pasos es comprobable o criterio humano.
- [ ] El resultado dice cuántos de los 32 planes existentes se pudieron leer.
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
