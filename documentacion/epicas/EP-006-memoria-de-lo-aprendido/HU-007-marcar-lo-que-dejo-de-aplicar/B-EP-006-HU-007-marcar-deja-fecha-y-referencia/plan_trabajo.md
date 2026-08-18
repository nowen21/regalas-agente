# Plan de Trabajo — Fase B-EP-006-HU-007-marcar-deja-fecha-y-referencia (módulo Memoria)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `B-EP-006-HU-007-marcar-deja-fecha-y-referencia` |
| **Épica** | [EP-006 Memoria de lo aprendido](../../epica.md) |
| **HU** | [HU-007 Marcar lo que dejó de aplicar sin borrarlo](../HU-007-marcar-lo-que-dejo-de-aplicar.md) — una sola (`F12.1`) |
| **Complementa** | [`A-EP-006-HU-007`](../A-EP-006-HU-007-retrodocumentar-la-marca-de-lo-que-dejo-de-aplicar/resultado_pruebas.md), que cerró en **No cumple** |
| **Módulo** | Memoria |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/B-EP-006-HU-007-marcar-deja-fecha-y-referencia` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 🐞 **Defecto**. `cmd_supersede` imprime «S-001 marcada reemplazada por S-002» y **no guarda ni el `--by` ni la fecha**. Archivar tampoco deja fecha. De una señal marcada no se sabe **cuándo** ni **por cuál**.

**CA de la HU que cubre esta fase**

| Exigencia de HU-007 | Qué exige | Estado tras la fase A |
|---|---|---|
| [CA-01](../HU-007-marcar-lo-que-dejo-de-aplicar.md#ca-01--lo-que-dejó-de-aplicar-queda-marcado-y-visible) | Sigue existiendo, **con la fecha y qué lo reemplazó** | **En «No».** Queda marcada; ni la fecha ni el reemplazo se guardan |
| Transversal · **Trazabilidad** | Queda **quién lo marcó y cuándo** | **En «No»** para archivar y reemplazar; al cerrar sí |

**Es el mismo defecto visto desde dos exigencias**, y por eso una sola fase: el arreglo es que los tres caminos que marcan escriban lo mismo que ya escribe uno.

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** que marcar una señal —archivar, reemplazar o cerrar— deje siempre **cuándo** y **por qué o por cuál**, en la base y no en la consola.

**Fuera de alcance:**

- **Cambiar los cinco estados.** Los que hay están bien y se comprobaron.
- **Registrar quién.** No hay identidad de usuario en la base, y agregarla es otra decisión: acá «quién» se cubre con la referencia que se guarda.
- **Migrar las señales ya marcadas.** Las que existen se quedan sin fecha; se dice, no se inventa.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17 leyendo `memoria/memoria.py` y `memoria/esquema.sql`.

**Lo que ya existe:** las columnas `reemplaza`, `cerrada_en` y `cierra_ref`; `cmd_cerrar`, que escribe las dos últimas; y las **dos pruebas en rojo esperado** `test_la_reemplazada_dice_que_la_reemplazo_y_cuando` y `test_trazabilidad_queda_cuando_se_archivo`.

**Lo que no existe:**

1. **Que `cmd_supersede` guarde el `--by`.** Solo cambia el estado.
2. **Que archivar o reemplazar dejen fecha.** `cerrada_en` la escribe únicamente `cmd_cerrar`.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `memoria/memoria.py` | Modificar | `cmd_supersede` guarda el `--by` y la fecha; `cmd_archivar` guarda la fecha |
| `memoria/pruebas.py` | Modificar | Destapar las dos pruebas, y sumar el caso de la señal marcada hace tiempo |
| `…/B-EP-006-HU-007-…/plan_pruebas.md` · `resultado_pruebas.md` | Nuevo | Los casos y lo que dieron |
| `HU-007-marcar-lo-que-dejo-de-aplicar.md` | Modificar | §8 nombra esta fase; §1 cambia de estado al cerrar |

> **El esquema no se toca:** las tres columnas ya existen y sirven para los tres caminos. Reutilizarlas evita una migración.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

`cerrada_en` y `cierra_ref` hoy solo las llena `cmd_cerrar`, y las lee `cmd_pendientes` para saber qué está cerrado. **Escribirlas también al archivar y al reemplazar no cambia esa consulta**, que filtra por `estado`, no por la fecha. Se comprueba en la prueba de no regresión.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica: es un programa de línea de comandos sobre una base local.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

`memoria.py archivar` y `memoria.py supersede`. No cambian de forma; cambian lo que dejan escrito.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Se reutilizan `cerrada_en` y `cierra_ref` para los tres caminos | Columnas nuevas `archivada_en`, `reemplazada_en` | Tres pares de columnas para lo mismo obliga a migrar y a que toda consulta mire tres sitios. El estado ya dice **qué** pasó; la fecha solo dice **cuándo** |
| El nombre de las columnas **no** se cambia | Renombrarlas a `marcada_en` / `marca_ref` | Renombrar obliga a migrar las bases que existen, y `03·D2` pide que toda migración declare su reversión. El costo no lo paga un nombre |
| Las señales ya marcadas **se quedan sin fecha** | Rellenar con la fecha de hoy | Poner hoy sería **inventar** cuándo se marcaron. Vacío dice la verdad: no se sabe |
| «Quién» se cubre con la referencia | Agregar identidad de usuario | No hay identidad en la base, y agregarla es otra decisión, no un arreglo |

### 2.7 Dudas por resolver antes de escribir

Ninguna. Las columnas existen, el defecto está probado y la decisión de reutilizarlas es de implementación.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Lo que dejó de aplicar queda marcado y visible

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | `cmd_supersede` guarda el `--by` en `cierra_ref` y la fecha en `cerrada_en` | `memoria/memoria.py` | 1,0 |
| T-02 | Destapar `test_la_reemplazada_dice_que_la_reemplazo_y_cuando` | `memoria/pruebas.py` | 0,5 |
| T-03 | Caso: desde la vieja se llega a la nueva, y desde la nueva a la vieja | `memoria/pruebas.py` | 1,0 |

### Transversal · Trazabilidad — Queda quién lo marcó y cuándo

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-04 | `cmd_archivar` guarda la fecha | `memoria/memoria.py` | 0,5 |
| T-05 | Destapar `test_trazabilidad_queda_cuando_se_archivo` | `memoria/pruebas.py` | 0,5 |
| T-06 | Caso: los tres caminos de marcar dejan fecha, y la señal vieja sin fecha **no se rellena** | `memoria/pruebas.py` | 1,5 |

### Cierre

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-07 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU | Cierre | 1,5 |

**Total: 7 tareas · 6,5 horas.**

---

## 4. Secuencia de ejecución

T-01 y T-04 son los dos arreglos. T-02 y T-05 destapan **después**, para que un rojo diga que el arreglo falló y no que la prueba estaba mal. T-03 y T-06 suman lo que falta, incluido el caso que comprueba que **no se rellena** lo viejo. T-07 cierra.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| Exigencia | Método de verificación | Evidencia |
|---|---|---|
| CA-01 | Reemplazar una señal y leer la fila de la vieja: tiene que decir cuál y cuándo | T-02, T-03 |
| Transversal · Trazabilidad | Archivar, reemplazar y cerrar, y comprobar que los tres dejan fecha | T-05, T-06 |
| No regresión | Que `pendientes` siga listando lo mismo, y que ninguna señal se borre | T-07 |

---

## 6. Datos y ambiente de prueba

Bases temporales, con la huella de `memoria/senales.db` comparada en cada caso ([`08·T4`](../../../../../base/08-pruebas.md)).

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase. **Las señales marcadas después del cambio se quedan con su fecha escrita**, y eso no molesta: son columnas que ya existían y que el código anterior ignora.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

**Sin migración:** las tres columnas ya existen en toda base creada desde el pendiente 03, y `migrar()` las agrega a las viejas. Las señales marcadas antes de este cambio **se quedan sin fecha**, y eso es lo correcto: no se sabe cuándo se marcaron.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`03·D2`](../../../../../base/03-datos.md), [`08·T4`](../../../../../base/08-pruebas.md), [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`15`](../../../../../base/15-registros-inmutables.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que reutilizar `cerrada_en` confunda «cerrada» con «archivada» al leer | Se malinterpreta la base | El **estado** dice qué pasó; la fecha solo dice cuándo. Se escribe en la documentación del módulo | Abierto |
| R-02 | Que `pendientes` cambie de resultado al llenarse la fecha en más filas | Regresión silenciosa | Filtra por `estado`, no por fecha. Se comprueba en T-07 | Abierto |
| R-03 | Que alguien rellene después las señales viejas «para que queden completas» | Se inventa historia | Queda escrito por qué se dejan vacías | Abierto |

---

## 11. Definition of Done

- [ ] Reemplazar deja **cuál** y **cuándo** en la señal marcada.
- [ ] Archivar deja **cuándo**.
- [ ] El enlace del reemplazo funciona en los dos sentidos.
- [ ] Las señales marcadas antes del cambio **siguen sin fecha**, y está escrito por qué.
- [ ] Las dos pruebas de fallo esperado quedan en verde **sin la marca**.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §8 de la HU nombra esta fase.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: es una fase de una sola sesión, y su avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
