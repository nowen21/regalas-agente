# Plan de Trabajo — Fase A-EP-006-HU-003-retrodocumentar-la-busqueda-por-palabra (módulo Memoria)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-003](../HU-003-busqueda-por-palabra.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-006-HU-003-retrodocumentar-la-busqueda-por-palabra` |
| **Épica** | [EP-006 Memoria de lo aprendido](../../epica.md) |
| **HU** | [HU-003 Buscar por palabra sin instalar nada](../HU-003-busqueda-por-palabra.md) — una sola (`F12.1`) |
| **Módulo** | Memoria |
| **Especificación del módulo** | [HU-003](../HU-003-busqueda-por-palabra.md). El módulo de la memoria **no tiene especificación aparte**: el criterio de qué se guarda son los criterios de aceptación de esta HU y el capítulo de documentación. Es uno de los casos que [EP-001 · HU-010](../../../EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/HU-010-cuando-no-aplica-la-especificacion.md) viene a resolver |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-006-HU-003-retrodocumentar-la-busqueda-por-palabra` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📄 **Retro-documentación** ([`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md)). La búsqueda existe y no necesita instalar nada: [`memoria/memoria.py`](../../../../../memoria/memoria.py) busca con el índice de texto completo que ya trae la base, y el índice ignora acentos a propósito. Sale de la fila de HU-003 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-003 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-003-busqueda-por-palabra.md#ca-01--se-busca-por-palabra-y-aparece-dónde-está) | Se busca por palabra y aparece dónde está | Corriendo: `memoria.py search`, con el campo que dice archivo o área. Sin prueba propia de esta HU |
| [CA-02](../HU-003-busqueda-por-palabra.md#ca-02--se-puede-filtrar-por-tipo-y-por-alcance) | Se puede filtrar por tipo y por alcance | Corriendo: los dos filtros existen en el subcomando. Sin prueba propia |

**Por qué una sola fase.** Los dos CA los cumple el mismo subcomando (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** dejar probado que se puede encontrar lo aprendido sin instalar nada, con sus filtros, y que lo archivado no aparece pero sigue estando.

**Fuera de alcance:**

- **La búsqueda por significado,** que es [HU-004](../../HU-004-busqueda-por-significado/HU-004-busqueda-por-significado.md) y es opcional.
- **Cambiar cómo se busca.** Si al probar aparece algo, se propone.
- **Lo que se marca como que dejó de aplicar,** que es [HU-007](../../HU-007-marcar-lo-que-dejo-de-aplicar/HU-007-marcar-lo-que-dejo-de-aplicar.md); acá solo se comprueba que no aparezca.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17 leyendo `memoria.py` y el esquema: el índice de texto completo está definido con los triggers que lo mantienen al día.

**Lo que ya existe:** el subcomando de búsqueda, con filtros de tipo, alcance y cantidad; el índice de texto completo, sincronizado por triggers; la decisión de ignorar acentos, escrita en el esquema; y la regla de que solo lo activo aparece en la búsqueda, con lo archivado conservado.

**Lo que no existe:**

1. **La prueba por criterio de esta HU.**
2. **La prueba del índice sincronizado.** Si un trigger se rompe, la búsqueda devolvería resultados viejos y nadie se enteraría.
3. **La prueba de que lo archivado no aparece** y sigue existiendo, que es la mitad del valor de no borrar nada.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `memoria/pruebas.py` | Modificar | Las pruebas de acentos, filtros y sincronía del índice |
| `…/A-EP-006-HU-003-…/plan_pruebas.md` · `resultado_pruebas.md` | Nuevo | Los casos y lo que dieron |
| `HU-003-busqueda-por-palabra.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> `memoria.py` y el esquema no se tocan.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna: se agregan pruebas sobre lo que ya corre.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque es un programa de línea de comandos sobre una base local.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

El punto de entrada es `python memoria/memoria.py search`. Esta fase no lo cambia.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Se prueba que el índice esté sincronizado, no solo que la búsqueda responda | Probar solo el resultado de una búsqueda | Un índice desincronizado responde: responde mal, y eso es peor que no responder |
| Las pruebas corren sobre una base temporal | Usar la base real | La base real tiene el aprendizaje del proyecto |
| El caso de lo archivado entra en esta fase | Dejarlo para HU-007 | Que no aparezca en la búsqueda es comportamiento de la búsqueda; marcarlo es de la otra HU |

### 2.7 Dudas por resolver antes de escribir

Ninguna: la búsqueda corre y su comportamiento se puede observar.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Se busca por palabra y aparece dónde está

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Caso de prueba: buscar una palabra y comprobar que aparece la señal con su ubicación | `plan_pruebas.md` | 1,5 |
| T-02 | Prueba: la búsqueda encuentra igual con acentos y sin ellos | `memoria/pruebas.py` | 1,5 |

### CA-02 — Se puede filtrar por tipo y por alcance

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Prueba: el filtro por tipo y el de alcance devuelven solo lo que corresponde | `memoria/pruebas.py` | 2,0 |
| T-04 | Caso de prueba: una señal archivada no aparece en la búsqueda, y sigue existiendo | `plan_pruebas.md` | 1,5 |

### RNF — Que la búsqueda no dependa de instalar nada

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-05 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 5 tareas · 8,0 horas.**

---

## 4. Secuencia de ejecución

T-02 → T-03 primero, que son pruebas. T-01 → T-04 después. T-05 cierra.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Búsqueda por palabra con y sin acentos, con la ubicación | T-01, T-02 |
| CA-02 | Filtros de tipo y alcance, y la señal archivada que no aparece | T-03, T-04 |

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

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`06`](../../../../../base/06-rendimiento.md), [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que la prueba de sincronía destape un trigger roto | Se destapa un defecto real | Es exactamente para lo que sirve; se anota y se propone el arreglo |
| R-02 | Que la prueba toque la base real | Se ensucia el aprendizaje | Base temporal, declarado como condición de arranque |
| R-03 | Que otra sesión esté tocando `memoria/pruebas.py` | Pisar trabajo ajeno | Se guarda solo lo propio |

---

## 11. Definition of Done

- [ ] La búsqueda por palabra está probada, con y sin acentos.
- [ ] Los dos filtros están probados.
- [ ] Está probado que el índice se mantiene al día al agregar y cambiar señales.
- [ ] Lo archivado no aparece en la búsqueda y sigue existiendo.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
