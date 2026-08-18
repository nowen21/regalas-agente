# Plan de Trabajo — Fase A-EP-006-HU-006-retrodocumentar-el-vaciado-del-almacen-local (módulo Memoria)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-006](../HU-006-sacar-del-almacen-local.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-006-HU-006-retrodocumentar-el-vaciado-del-almacen-local` |
| **Épica** | [EP-006 Memoria de lo aprendido](../../epica.md) |
| **HU** | [HU-006 Sacar del almacén local lo que deba vivir en el repositorio](../HU-006-sacar-del-almacen-local.md) — una sola (`F12.1`) |
| **Módulo** | Memoria |
| **Especificación del módulo** | [HU-006](../HU-006-sacar-del-almacen-local.md). El módulo de la memoria **no tiene especificación aparte**: el criterio de qué se guarda son los criterios de aceptación de esta HU y el capítulo de documentación. Es uno de los casos que [EP-001 · HU-010](../../../EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/HU-010-cuando-no-aplica-la-especificacion.md) viene a resolver |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-006-HU-006-retrodocumentar-el-vaciado-del-almacen-local` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📄 **Retro-documentación** ([`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md)). El vaciado existe y corre solo: [`recuerdos.py`](../../../../../validadores/recuerdos.py) y [`hook_recuerdos.py`](../../../../../validadores/hook_recuerdos.py) recogen del almacén local de la herramienta y lo dejan vacío, como exige `01·C19`. Es la otra cara de [EP-005 · HU-007](../../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-007-recoger-lo-guardado-por-fuera/HU-007-recoger-lo-guardado-por-fuera.md): allá se prueba el enganche, acá el resultado. Sale de la fila de HU-006 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-006 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-006-sacar-del-almacen-local.md#ca-01--el-almacén-queda-vacío) | El almacén queda vacío | Corriendo, y es lo que el índice de la memoria declara en su primera línea. Sin prueba propia de esta HU |
| [CA-02](../HU-006-sacar-del-almacen-local.md#ca-02--no-queda-un-puntero-en-lugar-del-texto) | No queda un puntero en lugar del texto | Corriendo, y es la parte fina: un puntero es peor que nada, porque parece que hay memoria donde no hay |

**Por qué una sola fase.** Los dos CA se comprueban sobre el mismo almacén después de la misma corrida (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** dejar probado que el almacén local queda vacío de verdad — ni el texto ni un puntero — para que no haya dos versiones del mismo recuerdo.

**Fuera de alcance:**

- **El enganche que lo dispara,** que es [EP-005 · HU-007](../../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-007-recoger-lo-guardado-por-fuera/HU-007-recoger-lo-guardado-por-fuera.md).
- **La forma del recuerdo en el repositorio,** que es [HU-005](../../HU-005-separar-aprendizaje-de-preferencia/HU-005-separar-aprendizaje-de-preferencia.md).
- **Tocar el almacén de la máquina del usuario.** Se lee para el registro; las pruebas corren sobre almacenes de mentira.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17: el índice de la memoria del repositorio declara que el almacén local queda vacío, y el `CLAUDE.md` del repositorio lo repite.

**Lo que ya existe:** el programa que recoge y el enganche que lo dispara; la razón escrita de por qué el almacén queda vacío —dos versiones del mismo recuerdo terminan diciendo cosas distintas, y la que manda es la que nadie puede leer—; y la insistencia del `CLAUDE.md`, que es la señal de que esto se incumplió alguna vez.

**Lo que no existe:**

1. **La prueba del vacío** por criterio de esta HU.
2. **La prueba de que tampoco queda un puntero.** Es el caso que el índice de la memoria nombra explícitamente, y nadie lo comprueba.
3. **El registro de qué había en el almacén de esta máquina** la última vez que se recogió.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/pruebas.py` | Modificar | Las pruebas del vacío y del puntero |
| `…/A-EP-006-HU-006-…/plan_pruebas.md` · `resultado_pruebas.md` | Nuevo | Los casos y lo que dieron |
| `HU-006-sacar-del-almacen-local.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> `recuerdos.py` y `hook_recuerdos.py` no se tocan.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna: se agregan pruebas sobre lo que ya corre.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque es un programa de línea de comandos sobre una base local.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

No hay interfaz: el recogido corre solo al abrir la sesión y después de cada escritura.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Las pruebas usan almacenes de mentira | Probar contra el almacén real | El almacén real puede tener algo del usuario sin recoger todavía |
| El caso del puntero se prueba a propósito | Confiar en que el programa no lo deja | Es el caso que el índice de la memoria nombra: merece su prueba |
| Lo que haya en el almacén de esta máquina se anota, no se borra a mano | Vaciarlo de paso | Vaciar a mano es hacer el trabajo del programa y perder la evidencia de si funcionaba |

### 2.7 Dudas por resolver antes de escribir

Ninguna: el programa corre y el almacén se puede observar.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — El almacén queda vacío

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Prueba: después de recoger, el almacén local no tiene archivos | `validadores/pruebas.py` | 2,0 |
| T-02 | Caso de prueba: comprobar el almacén de esta máquina y dejar escrito qué había | `resultado_pruebas.md` | 1,5 |

### CA-02 — No queda un puntero en lugar del texto

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Prueba: no queda ni el texto ni un archivo que apunte al del repositorio | `validadores/pruebas.py` | 2,0 |
| T-04 | Caso de prueba: con un puntero puesto a mano, el recogido lo saca | `plan_pruebas.md` | 1,5 |

### RNF — Que no haya dos versiones del mismo recuerdo

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-05 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 5 tareas · 8,5 horas.**

---

## 4. Secuencia de ejecución

T-01 → T-03 primero, que son las pruebas. T-04 después. T-02 al final, y T-05 cierra.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Almacén vacío después de recoger, y el registro de qué había | T-01, T-02 |
| CA-02 | Ni texto ni puntero, con el puntero puesto a mano | T-03, T-04 |

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

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`01·C19`](../../../../../base/01-conducta.md), [`15`](../../../../../base/15-registros-inmutables.md), [`20·M13`](../../../../../base/20-meta-reglas/reglas/M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que en el almacén de esta máquina haya algo sin recoger | Se destapa un defecto del recogido | Se anota qué había y se propone; se deja que el programa lo recoja, no la mano |
| R-02 | Que la prueba borre algo del almacén real | Se perdería un recuerdo | Almacenes de mentira, declarado como condición de arranque |
| R-03 | Que otra sesión esté tocando `validadores/pruebas.py` | Pisar trabajo ajeno | Se guarda solo lo propio |

---

## 11. Definition of Done

- [ ] Hay prueba de que el almacén local queda sin archivos.
- [ ] Hay prueba de que tampoco queda un puntero.
- [ ] Quedó escrito qué había en el almacén de esta máquina.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
