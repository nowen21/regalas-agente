# Plan de Trabajo — Fase A-EP-006-HU-004-retrodocumentar-la-busqueda-por-significado (módulo Memoria)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-004](../HU-004-busqueda-por-significado.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-006-HU-004-retrodocumentar-la-busqueda-por-significado` |
| **Épica** | [EP-006 Memoria de lo aprendido](../../epica.md) |
| **HU** | [HU-004 Buscar por significado con un modelo local y opcional](../HU-004-busqueda-por-significado.md) — una sola (`F12.1`) |
| **Módulo** | Memoria |
| **Especificación del módulo** | [HU-004](../HU-004-busqueda-por-significado.md). El módulo de la memoria **no tiene especificación aparte**: el criterio de qué se guarda son los criterios de aceptación de esta HU y el capítulo de documentación. Es uno de los casos que [EP-001 · HU-010](../../../EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/HU-010-cuando-no-aplica-la-especificacion.md) viene a resolver |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-006-HU-004-retrodocumentar-la-busqueda-por-significado` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📄 **Retro-documentación** ([`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-spec-antes-de-tocarlo.md)). Existe y es opcional: [`memoria/semantica.py`](../../../../../memoria/semantica.py) calcula los vectores **en la máquina** —el contenido de las señales no sale, por `00·N6`— y si sus dependencias no están, la memoria sigue funcionando con la búsqueda por palabra. Salió del pendiente [05](../../../../../pendientes/hecho/memoria-semantica.md), ya cerrado. Sale de la fila de HU-004 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-004 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-004-busqueda-por-significado.md#ca-01--encuentra-lo-que-se-escribió-con-otras-palabras) | Encuentra lo que se escribió con otras palabras | Corriendo cuando el modelo está: la búsqueda combina palabra y significado. Sin prueba propia de esta HU |
| [CA-02](../HU-004-busqueda-por-significado.md#ca-02--sin-el-modelo-la-búsqueda-sigue-funcionando) | Sin el modelo, la búsqueda sigue funcionando | Corriendo: si las dependencias no están, se degrada solo. **Es la mitad que hay que probar**, porque es la que sostiene que sea opcional |

**Por qué una sola fase.** Los dos CA son el mismo programa con y sin su parte opcional (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** dejar probado que buscar por significado funciona, que sin el modelo la memoria sigue sirviendo, y que el contenido de las señales no sale de la máquina.

**Fuera de alcance:**

- **Cambiar el modelo ni la forma de indexar.** Si al probar aparece algo, se propone.
- **La búsqueda por palabra,** que es [HU-003](../../HU-003-busqueda-por-palabra/HU-003-busqueda-por-palabra.md).
- **Instalar las dependencias en ninguna máquina.** La fase prueba los dos escenarios en carpetas temporales.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17 leyendo `semantica.py`: declara ser opt-in, calcular localmente y guardar los vectores en la misma base.

**Lo que ya existe:** el cálculo local de los vectores, guardados en la misma base; la degradación cuando las dependencias faltan; la búsqueda combinada, que suma palabra y significado; el archivo de dependencias opcionales, aparte a propósito; y la razón escrita de por qué se calcula en la máquina, que es la regla blindada de los secretos.

**Lo que no existe:**

1. **La prueba del escenario sin modelo.** Es la que sostiene que sea opcional, y nadie la corre.
2. **La constancia de que nada sale de la máquina.** Está escrito en el comentario del programa; no probado.
3. **La medida de cuánto mejora.** Sin ella no se puede decidir si vale instalar el modelo.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `memoria/pruebas.py` | Modificar | La prueba del escenario sin dependencias |
| `…/A-EP-006-HU-004-…/plan_pruebas.md` · `resultado_pruebas.md` | Nuevo | Los casos, y la medida de cuánto mejora la búsqueda |
| `HU-004-busqueda-por-significado.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> `semantica.py` no se toca.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna: se agregan pruebas sobre lo que ya corre.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque es un programa de línea de comandos sobre una base local.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

El punto de entrada es `python memoria/memoria.py search`, y `memoria.py indexar` para calcular los vectores. Esta fase no lo cambia.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El escenario sin modelo se prueba simulando la falta de dependencias | Desinstalarlas de la máquina | Desinstalar rompe el entorno de trabajo de quien corre la prueba |
| La prueba de que nada sale se hace observando que no haya salida a la red | Confiar en el comentario del programa | Es una regla blindada: se comprueba, no se supone |
| La mejora se mide con búsquedas reales | Un puntaje del modelo | Lo que importa es si encuentra lo que alguien buscaría, no cuánto puntúa |

### 2.7 Dudas por resolver antes de escribir

Ninguna: los dos escenarios se pueden montar en carpetas temporales.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Encuentra lo que se escribió con otras palabras

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Caso de prueba: buscar con palabras distintas a las de la señal y encontrarla | `plan_pruebas.md` | 2,0 |
| T-02 | Caso de prueba: comprobar que la búsqueda combinada no pierde lo que la de palabra sí encontraba | `plan_pruebas.md` | 1,5 |

### CA-02 — Sin el modelo, la búsqueda sigue funcionando

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Prueba: sin las dependencias instaladas, la búsqueda responde igual y lo dice | `memoria/pruebas.py` | 2,5 |
| T-04 | Caso de prueba: los vectores no salen de la máquina — nada se manda a ningún servicio | `plan_pruebas.md` | 2,0 |

### RNF — Que la memoria sirva aunque el modelo no esté

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-05 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 5 tareas · 9,5 horas.**

---

## 4. Secuencia de ejecución

T-03 primero, que es el escenario sin modelo. T-01 → T-02 con el modelo. T-04 en paralelo, y T-05 cierra.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Búsqueda con otras palabras, y comparación con la de palabra | T-01, T-02 |
| CA-02 | Escenario sin dependencias, y la comprobación de que nada sale de la máquina | T-03, T-04 |

---

## 6. Datos y ambiente de prueba

Bases de datos temporales para los casos, y este repositorio. Ningún dato real de cliente y ninguna clave: el contenido de las señales no sale de la máquina.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase. La base de prueba se borra al terminar.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

No aplica: no se toca nada de lo que corre. Sin subida de versión.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-spec-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`00·N6`](../../../../../base/00-nucleo-blindado.md), [`06`](../../../../../base/06-rendimiento.md), [`10`](../../../../../base/10-dependencias.md), [`12`](../../../../../base/12-privacidad-datos.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que la mejora sea chica y no valga instalar el modelo | La parte opcional queda sin usar | Es un resultado útil: se escribe la medida y se decide con dato |
| R-02 | Que la prueba de la red dependa del entorno | Prueba frágil | Se comprueba que el programa no abra ninguna conexión, no que la red esté caída |
| R-03 | Que instalar las dependencias para probar cambie el entorno de trabajo | Efecto fuera de la fase | Se instalan en un entorno aislado y temporal |

---

## 11. Definition of Done

- [ ] Buscar por significado encuentra lo escrito con otras palabras.
- [ ] Sin las dependencias, la búsqueda responde igual y lo dice.
- [ ] Está comprobado que el contenido de las señales no sale de la máquina.
- [ ] La mejora quedó medida con búsquedas reales.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
