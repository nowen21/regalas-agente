# Plan de Trabajo — Fase A-EP-007-HU-002-retrodocumentar-el-mostrar-antes-de-hacer (módulo Instalación)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-002](../HU-002-mostrar-antes-de-hacer.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-007-HU-002-retrodocumentar-el-mostrar-antes-de-hacer` |
| **Épica** | [EP-007 Instalación y actualización](../../epica.md) |
| **HU** | [HU-002 Mostrar qué va a hacer antes de hacerlo](../HU-002-mostrar-antes-de-hacer.md) — una sola (`F12.1`) |
| **Módulo** | Instalación |
| **Especificación del módulo** | [HU-002](../HU-002-mostrar-antes-de-hacer.md). El módulo de instalación **no tiene especificación aparte** —se declara como deuda en las fases hermanas de esta épica— y sus criterios de aceptación hacen de especificación |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-007-HU-002-retrodocumentar-el-mostrar-antes-de-hacer` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📄 **Retro-documentación** ([`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md)). El instalador existe y está en producción: [`instalar.py`](../../../../../validadores/instalar.py) es el que copia el estándar a un proyecto, deja puestos los seis enganches y escribe el registro de la versión adoptada. Sale de la fila de HU-002 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-002 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-002-mostrar-antes-de-hacer.md#ca-01--antes-de-tocar-nada-dice-qué-va-a-hacer) | Antes de tocar nada, dice qué va a hacer | Hay que medirlo: el instalador informa lo que hace, y si lo muestra **antes** y espera, o lo cuenta mientras lo hace, es lo que esta fase tiene que establecer |
| [CA-02](../HU-002-mostrar-antes-de-hacer.md#ca-02--nada-se-toca-sin-autorización) | Nada se toca sin autorización | Es exigencia del núcleo, `00·N1`, y el instalador la hereda. Sin prueba propia de esta HU |

**Por qué una sola fase.** Los dos CA se comprueban en la misma corrida del instalador (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** establecer si el instalador muestra lo que va a hacer antes de hacerlo, y dejar escrito qué falta si no lo hace.

**Fuera de alcance:**

- **Cambiar el instalador.** Si falta la vista previa, se propone: es el programa que toca los archivos de otros proyectos y no se cambia sin plan aprobado.
- **Poner al día lo ya instalado,** que es [HU-006](../../HU-006-poner-al-dia/HU-006-poner-al-dia.md) y ya tiene su fase.
- **Rellenar los marcadores al copiar,** que es [HU-001](../../HU-001-instalar-con-una-linea/HU-001-instalar-con-una-linea.md) y tiene dos fases.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17 leyendo `instalar.py` y la lista de enganches que deja puestos.

**Lo que ya existe:** el instalador, con lo que copia y los seis enganches que registra; el registro de la versión adoptada, que él escribe; la revisión de instalación, que dice qué le falta a un proyecto; y la regla del núcleo que prohíbe cambiar estado sin aprobación.

**Lo que no existe:**

1. **La constancia de qué se ve antes.** Nadie anotó, paso por paso, qué dice el instalador y en qué momento.
2. **La prueba del CA-01.**
3. **La vista previa, si no está.** Es lo que la fase tiene que establecer con dato en vez de suponerlo.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `…/A-EP-007-HU-002-…/plan_pruebas.md` · `resultado_pruebas.md` | Nuevo | Los casos, la bitácora de la corrida y la propuesta si falta |
| `HU-002-mostrar-antes-de-hacer.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> `instalar.py` no se toca: esta fase mide.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna: la fase solo observa y escribe.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque es un programa de línea de comandos.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

**Sí tiene punto de entrada:** el instalador se corre por línea de comandos. Lo que la fase mide es qué muestra antes de actuar.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Se mide antes de proponer | Suponer que falta la vista previa y escribirla | Ya pasó en esta casa: una HU nació pidiendo algo que ya existía, y hubo que recortarla el mismo día |
| La corrida es sobre un proyecto de prueba | Correrlo sobre un proyecto real | El instalador escribe archivos: sobre un proyecto vivo eso es tocar trabajo ajeno |
| Si falta, se propone con el costo | Escribirlo de una | Es el programa que modifica otros proyectos: cambiarlo se aprueba aparte |

### 2.7 Dudas por resolver antes de escribir

Ninguna: el instalador se puede correr sobre una carpeta temporal y observar.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Antes de tocar nada, dice qué va a hacer

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Correr el instalador sobre un proyecto de prueba y anotar, paso por paso, qué dice y en qué momento | `resultado_pruebas.md` | 2,5 |
| T-02 | Caso de prueba: comprobar si hay una forma de ver el plan sin ejecutarlo | `plan_pruebas.md` | 2,0 |

### CA-02 — Nada se toca sin autorización

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Caso de prueba: sobre un proyecto de prueba, comprobar qué se escribe y qué se pide antes | `plan_pruebas.md` | 2,0 |
| T-04 | Anotar el resultado: si el CA-01 se cumple, si falta la vista previa, y qué costaría | `resultado_pruebas.md` | 1,5 |

### RNF — Que se pueda saber qué va a pasar antes de que pase

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-05 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 5 tareas · 9,5 horas.**

---

## 4. Secuencia de ejecución

T-01 primero, que es la bitácora. T-02 → T-03 después. T-04 con lo que se vea, y T-05 cierra.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Bitácora de la corrida, paso por paso, y la búsqueda de una vista previa | T-01, T-02 |
| CA-02 | Qué se escribe y qué se pide antes, en un proyecto de prueba | T-03, T-04 |

---

## 6. Datos y ambiente de prueba

Proyectos de prueba en carpetas temporales. No se instala ni se actualiza ningún proyecto vivo. Ningún dato real y ninguna clave.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase. Las carpetas de prueba se borran al terminar.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

No aplica mientras el instalador no se toque. Si falta la vista previa y se decide agregarla, sería **MENOR**: una forma nueva de correrlo, sin cambiar la que ya existe.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`00·N1`](../../../../../base/00-nucleo-blindado.md), [`00·N5`](../../../../../base/00-nucleo-blindado.md), [`02·F13`](../../../../../base/02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que el CA-01 resulte cumplido y la fase parezca vacía | Se lee como trabajo perdido | Es un resultado: queda escrito qué muestra y en qué momento, que hoy no está en ninguna parte |
| R-02 | Que la corrida de prueba toque algo fuera de su carpeta | Daño en otro proyecto | Carpeta temporal, y el resultado comprueba qué se escribió y dónde |
| R-03 | Que la propuesta se lea como decidida | Se cambiaría el instalador sin aprobación | Se escribe como propuesta, con su costo |

---

## 11. Definition of Done

- [ ] Está escrito, paso por paso, qué dice el instalador y en qué momento.
- [ ] Está establecido si hay forma de ver el plan sin ejecutarlo.
- [ ] Si falta, quedó propuesto con su costo, sin cambiar el instalador.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
