# Plan de Trabajo — Fase A-EP-006-HU-001-retrodocumentar-que-se-guarda-y-con-que-alcance (módulo Memoria)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-001](../HU-001-que-se-guarda-tipos-y-alcances.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-006-HU-001-retrodocumentar-que-se-guarda-y-con-que-alcance` |
| **Épica** | [EP-006 Memoria de lo aprendido](../../epica.md) |
| **HU** | [HU-001 Definir qué se guarda, con qué tipos y qué alcances](../HU-001-que-se-guarda-tipos-y-alcances.md) — una sola (`F12.1`) |
| **Módulo** | Memoria |
| **Especificación del módulo** | [HU-001](../HU-001-que-se-guarda-tipos-y-alcances.md). El módulo de la memoria **no tiene especificación aparte**: el criterio de qué se guarda son los criterios de aceptación de esta HU y el capítulo de documentación. Es uno de los casos que [EP-001 · HU-010](../../../EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/HU-010-cuando-no-aplica-la-especificacion.md) viene a resolver |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-006-HU-001-retrodocumentar-que-se-guarda-y-con-que-alcance` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📄 **Retro-documentación** ([`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-spec-antes-de-tocarlo.md)). Los tipos y los alcances existen y están en producción: [`memoria/esquema.sql`](../../../../../memoria/esquema.sql) declara diez tipos de señal y tres formas de alcance —organización, proyecto y módulo—, y [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md) dice qué merece guardarse. Sale de la fila de HU-001 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-001 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-001-que-se-guarda-tipos-y-alcances.md#ca-01--el-criterio-de-qué-se-guarda-está-escrito) | El criterio de qué se guarda está escrito | Cumplido: `13·DOC5` lo dice —lo que no se recupera leyendo el código—, y es una regla `opt-in`. Sin prueba |
| [CA-02](../HU-001-que-se-guarda-tipos-y-alcances.md#ca-02--cada-cosa-guardada-tiene-tipo-y-alcance) | Cada cosa guardada tiene tipo y alcance | Cumplido por el esquema, que no admite una señal sin tipo y le pone alcance de proyecto por omisión. Sin prueba |

**Por qué una sola fase.** Los dos CA se comprueban sobre el mismo esquema y el mismo criterio (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** dejar escrito y probado qué merece guardarse, con qué tipo y con qué alcance — y saber cuáles de los diez tipos se usan de verdad.

**Fuera de alcance:**

- **Buscar,** que son [HU-003](../../HU-003-busqueda-por-palabra/HU-003-busqueda-por-palabra.md) y [HU-004](../../HU-004-busqueda-por-significado/HU-004-busqueda-por-significado.md).
- **Separar el aprendizaje del proyecto de la preferencia del usuario,** que es [HU-005](../../HU-005-separar-aprendizaje-de-preferencia/HU-005-separar-aprendizaje-de-preferencia.md).
- **Agregar o quitar tipos.** Si alguno no se usa nunca, se anota: quitarlo es decisión del usuario y rompería las señales que ya lo tienen.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17 leyendo el esquema: diez tipos, cinco estados y tres formas de alcance.

**Lo que ya existe:** el esquema con sus diez tipos —decisión, error resuelto, patrón, aprendizaje, alternativa descartada, supuesto, restricción, pregunta abierta, tropiezo y deuda técnica—; los tres alcances; los cinco estados, con la regla escrita de que ninguna señal se borra; y la regla `opt-in` que dice qué merece registrarse.

**Lo que no existe:**

1. **La prueba del criterio.** Decidir si algo es señal se hace a ojo cada vez.
2. **La cuenta de uso de los tipos.** Diez tipos son muchos: si tres no se usan nunca, el criterio no está funcionando.
3. **La prueba del esquema** por criterio de esta HU.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `memoria/pruebas.py` | Modificar | La prueba del tipo obligatorio y del alcance por omisión |
| `…/A-EP-006-HU-001-…/plan_pruebas.md` · `resultado_pruebas.md` | Nuevo | Los casos y lo que dieron, con la tabla de uso de los diez tipos |
| `HU-001-que-se-guarda-tipos-y-alcances.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> Ni el esquema ni `memoria.py` se tocan.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna: se agregan pruebas sobre lo que ya corre.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque es un programa de línea de comandos sobre una base local.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

El punto de entrada es `python memoria/memoria.py`, con sus subcomandos. Esta fase no lo cambia.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Los tipos que no se usan se anotan, no se quitan | Limpiar el esquema | Quitar un tipo rompe las señales que ya lo tienen, y ninguna se borra |
| El criterio se prueba con decisiones reales de fases cerradas | Inventar cinco ejemplos | Las decisiones reales son las que cuesta clasificar; los ejemplos inventados siempre caen claros |
| La prueba corre sobre una base temporal | Usar `senales.db` | La base tiene el aprendizaje real: una prueba no lo toca |

### 2.7 Dudas por resolver antes de escribir

Ninguna: el esquema y el criterio están escritos y se pueden leer.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — El criterio de qué se guarda está escrito

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Caso de prueba: tomar cinco decisiones de las fases cerradas y decir, con el criterio, cuáles son señal y cuáles no | `plan_pruebas.md` | 2,0 |

### CA-02 — Cada cosa guardada tiene tipo y alcance

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-02 | Prueba: una señal sin tipo no entra, y una sin alcance entra con el de proyecto | `memoria/pruebas.py` | 2,0 |
| T-03 | Levantar la tabla de los diez tipos con un ejemplo real de cada uno, o dejar dicho cuál no se ha usado nunca | `resultado_pruebas.md` | 2,5 |

### RNF — Que el criterio se pueda aplicar sin discutir cada vez

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-04 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 4 tareas · 8,0 horas.**

---

## 4. Secuencia de ejecución

T-02 primero, que es la prueba corta. T-01 y T-03 después. T-04 cierra.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Cinco decisiones reales clasificadas con el criterio | T-01 |
| CA-02 | Señal sin tipo y sin alcance, y la tabla de uso | T-02, T-03 |

---

## 6. Datos y ambiente de prueba

Bases de datos temporales para los casos, y este repositorio. Ningún dato real de cliente y ninguna clave: el contenido de las señales no sale de la máquina.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase. La base de prueba se borra al terminar.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

No aplica: el esquema no se toca. Sin subida de versión.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-spec-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md), [`15`](../../../../../base/15-registros-inmutables.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que la mitad de los tipos no se use nunca | El criterio no está sirviendo | Se anota con la cuenta; simplificar el esquema es decisión del usuario |
| R-02 | Que la prueba toque la base real | Se ensucia el aprendizaje del proyecto | Base temporal, declarado como condición de arranque |
| R-03 | Que clasificar cinco decisiones reales resulte ambiguo | El criterio no alcanza | Es el resultado honesto: se escribe cuál no se pudo clasificar y por qué |

---

## 11. Definition of Done

- [ ] Cinco decisiones reales quedaron clasificadas con el criterio.
- [ ] Hay prueba de que el tipo es obligatorio y el alcance tiene valor por omisión.
- [ ] La tabla de uso de los diez tipos está escrita, con los que no se usan nunca.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
