# Plan de Trabajo — Fase A-EP-006-HU-007-retrodocumentar-la-marca-de-lo-que-dejo-de-aplicar (módulo Memoria)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-007](../HU-007-marcar-lo-que-dejo-de-aplicar.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-006-HU-007-retrodocumentar-la-marca-de-lo-que-dejo-de-aplicar` |
| **Épica** | [EP-006 Memoria de lo aprendido](../../epica.md) |
| **HU** | [HU-007 Marcar lo que dejó de aplicar sin borrarlo](../HU-007-marcar-lo-que-dejo-de-aplicar.md) — una sola (`F12.1`) |
| **Módulo** | Memoria |
| **Especificación del módulo** | [HU-007](../HU-007-marcar-lo-que-dejo-de-aplicar.md). El módulo de la memoria **no tiene especificación aparte**: el criterio de qué se guarda son los criterios de aceptación de esta HU y el capítulo de documentación. Es uno de los casos que [EP-001 · HU-010](../../../EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/HU-010-cuando-no-aplica-la-especificacion.md) viene a resolver |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-006-HU-007-retrodocumentar-la-marca-de-lo-que-dejo-de-aplicar` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📄 **Retro-documentación** ([`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md)). Está construido y salió del pendiente [02](../../../../../pendientes/hecho/vigencia-y-poda-de-memoria.md), ya cerrado: el esquema tiene cinco estados —activa, reemplazada, revertida, archivada y cerrada—, con la regla escrita de que **ninguna se borra**, y los subcomandos para reemplazar, revisar, archivar y cerrar. Sale de la fila de HU-007 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-007 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-007-marcar-lo-que-dejo-de-aplicar.md#ca-01--lo-que-dejó-de-aplicar-queda-marcado-y-visible) | Lo que dejó de aplicar queda marcado y visible | Corriendo: los cinco estados, con la señal que reemplaza apuntando a la reemplazada. Sin prueba propia de esta HU |
| [CA-02](../HU-007-marcar-lo-que-dejo-de-aplicar.md#ca-02--lo-marcado-no-se-confunde-con-lo-vigente) | Lo marcado no se confunde con lo vigente | Corriendo: solo lo activo aparece en la búsqueda, y lo que no se revisa hace meses se muestra atenuado |

**Por qué una sola fase.** Los dos CA son el mismo juego de estados, visto desde lo que se conserva y desde lo que se muestra (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** dejar probado que nada se borra y que lo que dejó de aplicar no se puede confundir con lo vigente.

**Fuera de alcance:**

- **Cambiar los estados.** Son cinco y así se quedan; agregar uno es decisión del usuario.
- **El ritual de revisión.** Existe como subcomando; que alguien lo corra cada tanto no es cosa de esta fase.
- **Las métricas de vigencia,** que están en [`metricas/`](../../../../../metricas/README.md) y miden otra cosa.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17 leyendo el esquema: los cinco estados están declarados, con el comentario de qué significa cada uno y la regla de que ninguna se borra.

**Lo que ya existe:** los cinco estados; el campo que dice qué señal reemplaza a cuál; la fecha de revisión, que marca la vigencia; los subcomandos para reemplazar, revisar, archivar y cerrar; y la regla escrita de que la búsqueda muestra solo lo activo.

**Lo que no existe:**

1. **La prueba de que nada se borra.** Es la exigencia central y nadie la comprueba.
2. **La prueba de que lo marcado no aparece** donde no debe.
3. **La prueba de la vigencia,** que es lo que evita creerle a un aprendizaje viejo.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `memoria/pruebas.py` | Modificar | Las pruebas de los estados y de la búsqueda |
| `…/A-EP-006-HU-007-…/plan_pruebas.md` · `resultado_pruebas.md` | Nuevo | Los casos y lo que dieron |
| `HU-007-marcar-lo-que-dejo-de-aplicar.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> Ni el esquema ni `memoria.py` se tocan.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna: se agregan pruebas sobre lo que ya corre.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque es un programa de línea de comandos sobre una base local.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

El punto de entrada son los subcomandos de `memoria.py`. Esta fase no los cambia.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La prueba comprueba que la fila sigue existiendo, no solo que no aparece | Probar solo la búsqueda | No aparecer y no existir se ven igual desde la búsqueda, y la exigencia es que exista |
| La vigencia se prueba con fechas puestas a mano | Esperar a que una señal envejezca | Una prueba no puede tardar meses |
| Los cinco estados se prueban uno por uno | Probar solo el reemplazo | Cada estado tiene su motivo, y el que no se prueba es el que se rompe en silencio |

### 2.7 Dudas por resolver antes de escribir

Ninguna: los estados están declarados y se pueden ejercitar sobre una base temporal.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Lo que dejó de aplicar queda marcado y visible

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Prueba: reemplazar una señal deja la vieja marcada y apuntando a la nueva, y ninguna se borra | `memoria/pruebas.py` | 2,0 |
| T-02 | Caso de prueba: una señal archivada se puede seguir leyendo si se la busca a propósito | `plan_pruebas.md` | 1,5 |

### CA-02 — Lo marcado no se confunde con lo vigente

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Prueba: la búsqueda no devuelve lo archivado, lo reemplazado ni lo cerrado | `memoria/pruebas.py` | 2,0 |
| T-04 | Caso de prueba: la vigencia — una señal sin revisar hace meses se distingue de una fresca | `plan_pruebas.md` | 2,0 |

### RNF — Que nada se borre y nada se confunda

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-05 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 5 tareas · 9,0 horas.**

---

## 4. Secuencia de ejecución

T-01 → T-03 primero, que son las pruebas duras. T-02 → T-04 después. T-05 cierra.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Reemplazo que conserva la vieja marcada, y lo archivado que se sigue leyendo | T-01, T-02 |
| CA-02 | Búsqueda que no devuelve lo marcado, y la vigencia | T-03, T-04 |

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

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md), [`15`](../../../../../base/15-registros-inmutables.md), [`20·M11`](../../../../../base/20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que alguno de los cinco estados no funcione como dice el comentario | Se destapa un defecto | Se anota y se propone; el estado que no funciona pierde memoria en silencio |
| R-02 | Que la prueba toque la base real | Se ensucia el aprendizaje | Base temporal, declarado como condición de arranque |
| R-03 | Que la prueba de vigencia quede atada al huso horario | Prueba frágil | Se usan fechas fijas puestas a mano, no la fecha de hoy |

---

## 11. Definition of Done

- [ ] Hay prueba de que reemplazar no borra, y de que la vieja apunta a la nueva.
- [ ] Hay prueba de que la búsqueda no devuelve lo archivado, lo reemplazado ni lo cerrado.
- [ ] Lo archivado se puede seguir leyendo si se busca a propósito.
- [ ] La vigencia está probada con fechas fijas.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
