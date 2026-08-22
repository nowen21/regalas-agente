# Plan de Trabajo — Fase A-EP-007-HU-003-retrodocumentar-la-estructura-de-carpetas (módulo Instalación)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-003](../HU-003-estructura-de-carpetas.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-007-HU-003-retrodocumentar-la-estructura-de-carpetas` |
| **Épica** | [EP-007 Instalación y actualización](../../epica.md) |
| **HU** | [HU-003 Crear la estructura de carpetas del trabajo](../HU-003-estructura-de-carpetas.md) — una sola (`F12.1`) |
| **Módulo** | Instalación |
| **Especificación del módulo** | [HU-003](../HU-003-estructura-de-carpetas.md). El módulo de instalación **no tiene especificación aparte** —se declara como deuda en las fases hermanas de esta épica— y sus criterios de aceptación hacen de especificación |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-007-HU-003-retrodocumentar-la-estructura-de-carpetas` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📄 **Retro-documentación** ([`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md)). La estructura existe y está exigida: [`02·F13`](../../../../../base/02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md) la pide antes de trabajar, [`estructura-base.md`](../../../../../base/02-flujo-de-trabajo/estructura-base.md) la declara, el instalador la crea y [`estructura.py`](../../../../../validadores/estructura.py) comprueba que esté. Sale de la fila de HU-003 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-003 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-003-estructura-de-carpetas.md#ca-01--la-estructura-se-crea-sola) | La estructura se crea sola | Corriendo: el instalador la deja puesta. Sin prueba propia de esta HU |
| [CA-02](../HU-003-estructura-de-carpetas.md#ca-02--lo-que-ya-existe-no-se-pisa) | Lo que ya existe no se pisa | Corriendo, y es la mitad que importa: instalar sobre un proyecto que ya trabajó no puede borrarle nada |
| [CA-03](../HU-003-estructura-de-carpetas.md#ca-03--la-estructura-que-falta-se-reporta) | La estructura que falta se reporta | Corriendo: la revisión de instalación dice qué falta. **Y sobre esta casa reporta un punto con razón** — el planteamiento que no está, pendiente [56](../../../../../pendientes/hecho/el-estandar-tiene-su-planteamiento.md) |

**Por qué una sola fase.** Los tres CA se comprueban con las mismas dos corridas: instalar y revisar (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** dejar probado que la estructura se crea sola, que no pisa nada y que lo que falta se reporta — incluido el caso de esta casa, que no se instala a sí misma.

**Fuera de alcance:**

- **Escribir el planteamiento de este repositorio.** Es el pendiente [56](../../../../../pendientes/hecho/el-estandar-tiene-su-planteamiento.md) y sale de una conversación, no de leer el repositorio.
- **No pisar lo escrito,** que es [HU-005](../../HU-005-no-pisar-lo-escrito/HU-005-no-pisar-lo-escrito.md) y lo mira desde el contenido de los archivos; acá se mira desde las carpetas.
- **Cambiar la estructura declarada.** Si falta algo, se propone.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17: la revisión de instalación sobre esta casa da «6 de 14», y ocho de esos puntos no le aplican porque el estándar no se instala a sí mismo.

**Lo que ya existe:** la regla que exige la estructura antes de trabajar; el documento que la declara; el instalador que la crea; la revisión que dice qué falta; y la advertencia ya escrita de cómo leer esa revisión en esta casa, para no sacar la conclusión equivocada del «6 de 14».

**Lo que no existe:**

1. **La prueba de que no pisa.** Es lo que decide si el instalador se puede correr sobre un proyecto que ya trabajó.
2. **La prueba de instalar dos veces,** que es la forma corta de comprobar lo mismo.
3. **La constancia de cómo se lee la revisión en esta casa,** que hoy vive en un pendiente y no en el resultado de una fase.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/pruebas.py` | Modificar | La prueba de que no pisa |
| `…/A-EP-007-HU-003-…/plan_pruebas.md` · `resultado_pruebas.md` | Nuevo | Los casos y lo que dieron |
| `HU-003-estructura-de-carpetas.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> `instalar.py` y `estructura.py` no se tocan.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna: se agregan pruebas sobre lo que ya corre.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque es un programa de línea de comandos.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

**Sí tienen punto de entrada:** el instalador y `validar.py checklist`, que es la revisión de instalación.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La prueba de que no pisa usa archivos con contenido | Comprobar solo que la carpeta siga existiendo | Pisar es perder contenido, y una carpeta que sigue ahí con un archivo vacío se ve igual de bien |
| Instalar dos veces se prueba como caso propio | Confiar en la prueba anterior | Es la forma en que esto se rompe de verdad: la segunda corrida es la que borra |
| El caso de esta casa se anota en el resultado | Dejarlo solo en el pendiente 56 | Quien lea el resultado de la fase tiene que entender por qué la revisión reprueba acá |

### 2.7 Dudas por resolver antes de escribir

Ninguna: las dos corridas se pueden hacer sobre carpetas temporales.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — La estructura se crea sola

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Caso de prueba: instalar en una carpeta vacía y comprobar que la estructura queda completa | `plan_pruebas.md` | 2,0 |

### CA-02 — Lo que ya existe no se pisa

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-02 | Prueba: con carpetas y archivos ya presentes, la instalación no los cambia | `validadores/pruebas.py` | 2,5 |
| T-03 | Caso de prueba: instalar dos veces seguidas deja el mismo resultado | `plan_pruebas.md` | 1,5 |

### CA-03 — La estructura que falta se reporta

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-04 | Caso de prueba: quitar una carpeta en el proyecto de prueba y comprobar que la revisión lo dice | `plan_pruebas.md` | 1,5 |
| T-05 | Anotar cómo se lee la revisión en esta casa, que no se instala a sí misma | `resultado_pruebas.md` | 1,5 |

### RNF — Que instalar no borre nada

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-06 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 6 tareas · 10,5 horas.**

---

## 4. Secuencia de ejecución

T-01 primero. T-02 → T-03 después, que son la parte dura. T-04 y T-05 al final, y T-06 cierra.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Instalación en carpeta vacía | T-01 |
| CA-02 | Archivos con contenido que no cambian, e instalar dos veces | T-02, T-03 |
| CA-03 | Carpeta quitada que la revisión reporta, y el caso de esta casa | T-04, T-05 |

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

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`00·N1`](../../../../../base/00-nucleo-blindado.md), [`02·F13`](../../../../../base/02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md), [`13·DOC17`](../../../../../base/13-documentacion/reglas/DOC17-manten-un-readme-en-cada-nivel-del-arbol-de-trabajo.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que la prueba de que no pisa falle | Defecto grave: el instalador borraría trabajo | Se para y se reporta de inmediato; corregirlo es una fase con su propio plan |
| R-02 | Que la corrida de prueba escriba fuera de su carpeta | Daño en otro proyecto | Carpeta temporal, y el resultado comprueba dónde se escribió |
| R-03 | Que el «6 de 14» de esta casa se lea como que el estándar está mal instalado | Conclusión equivocada | El resultado explica los ocho puntos que no le aplican |

---

## 11. Definition of Done

- [ ] La estructura se crea sola en una carpeta vacía, con prueba.
- [ ] Hay prueba de que instalar no cambia archivos con contenido, y de que dos corridas dan el mismo resultado.
- [ ] Una carpeta que falta se reporta.
- [ ] Está escrito cómo se lee la revisión en esta casa, que no se instala a sí misma.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
