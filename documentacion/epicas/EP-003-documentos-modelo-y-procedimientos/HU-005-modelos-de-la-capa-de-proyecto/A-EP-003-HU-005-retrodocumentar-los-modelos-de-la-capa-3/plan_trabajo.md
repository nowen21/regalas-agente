# Plan de Trabajo — Fase A-EP-003-HU-005-retrodocumentar-los-modelos-de-la-capa-3 (módulo Documentos modelo)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-005](../HU-005-modelos-de-la-capa-de-proyecto.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-003-HU-005-retrodocumentar-los-modelos-de-la-capa-3` |
| **Épica** | [EP-003 Documentos modelo y procedimientos](../../epica.md) |
| **HU** | [HU-005 Crear los modelos de la capa de proyecto: stack, dominio, nombres propios](../HU-005-modelos-de-la-capa-de-proyecto.md) — una sola (`F12.1`) |
| **Módulo** | Documentos modelo |
| **Especificación del módulo** | [documentacion/documentos-modelo/spec.md](../../../../documentos-modelo/spec.md). Existe y crece por incrementos; esta fase le agrega el suyo (`02·F2`) |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-003-HU-005-retrodocumentar-los-modelos-de-la-capa-3` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📄 **Retro-documentación** ([`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md)). Los tres modelos existen y el instalador los pone en cada proyecto: [`plantillas/stack.md`](../../../../../plantillas/stack.md), [`plantillas/dominio.md`](../../../../../plantillas/dominio.md) y [`plantillas/mapeo-nombres.md`](../../../../../plantillas/mapeo-nombres.md). Y hay un programa que los lee: [`declaracion.py`](../../../../../validadores/declaracion.py). Sale de la fila de HU-005 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-005 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-005-modelos-de-la-capa-de-proyecto.md#ca-01--los-tres-modelos-existen-y-no-se-pisan) | Los tres modelos existen y no se pisan | Los tres existen. Que no se pisen no está comprobado |
| [CA-02](../HU-005-modelos-de-la-capa-de-proyecto.md#ca-02--lo-que-un-programa-lee-tiene-forma-fija) | Lo que un programa lee tiene forma fija | Corriendo: `declaracion.py` lee los módulos y su especificación declarados en el dominio |
| [CA-03](../HU-005-modelos-de-la-capa-de-proyecto.md#ca-03--lo-no-declarado-no-se-comprueba) | Lo no declarado no se comprueba | Corriendo, y es el criterio de [EP-004 · HU-010](../../../EP-004-comprobacion-automatica/HU-010-convencion-declarada-por-el-proyecto/A-EP-004-HU-010-declaracion-y-comprobacion/plan_trabajo.md), ya retro-documentada |

**Por qué una sola fase.** Los tres CA se comprueban sobre los mismos tres modelos y la misma corrida (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** dejar en la especificación qué exige cada modelo de la capa del proyecto, qué parte de cada uno la lee un programa y qué pasa con lo que el proyecto no declara.

**Fuera de alcance:**

- **Que el ajuste propio mande sobre la convención general,** que es [EP-001 · HU-006](../../../EP-001-cuerpo-de-reglas-heredable/HU-006-capa-propia-del-proyecto/HU-006-capa-propia-del-proyecto.md).
- **El programa que comprueba el código contra la convención declarada,** ya retro-documentado en EP-004 · HU-010.
- **Los demás archivos de la capa 3** —el marco normativo y las reglas propias—: la HU nombra tres modelos y son esos tres.
- **Cambiar los modelos.** Lo que falte se propone: son `plantillas/` y suben versión.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17 leyendo los tres modelos y `declaracion.py`.

**Lo que ya existe:** el modelo del stack, donde el proyecto declara con qué está hecho; el del dominio, con sus módulos y la especificación de cada uno; el de nombres propios, que traduce el vocabulario del cliente al del código; `declaracion.py`, que lee esas declaraciones y las entrega a los validadores que las necesitan; y la regla de que lo no declarado no se comprueba, que es lo que evita que el revisor invente exigencias.

**Lo que no existe:**

1. **El incremento en la especificación** de estos tres modelos.
2. **La prueba de que no se pisan.** Un módulo se nombra en el dominio y su nombre propio en el mapeo: nada comprueba que no haya dos verdades sobre el mismo dato.
3. **La prueba de la forma fija.** `declaracion.py` sabe leer el formato correcto; qué hace con uno mal escrito no está probado por criterio de esta HU.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `documentacion/documentos-modelo/spec.md` | Modificar | Le entra el incremento: los tres modelos, qué parte lee un programa y qué pasa con lo no declarado |
| `…/A-EP-003-HU-005-…/plan_pruebas.md` | Nuevo | Los casos de los tres CA |
| `…/A-EP-003-HU-005-…/resultado_pruebas.md` | Nuevo | Lo que dieron |
| `validadores/pruebas.py` | Modificar | Pruebas: una declaración mal escrita se detecta, y lo no declarado no genera exigencia |
| `HU-005-modelos-de-la-capa-de-proyecto.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> `plantillas/` y `declaracion.py` no se tocan.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna: las pruebas se escriben contra la interfaz que `declaracion.py` ya expone.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque el entregable son modelos de documento.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

No aplica. Los modelos viven en la capa del proyecto y se leen ahí.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El solape se prueba por dato, no por sección | Comparar los tres modelos línea a línea | Lo que no puede repetirse es el dato del que hay una sola verdad; las secciones parecidas no molestan |
| El caso de la declaración mal escrita se prueba en carpeta temporal | Escribirla mal en un proyecto real | Romper a propósito la capa 3 de un proyecto vivo es tocar trabajo ajeno |
| Lo no declarado se prueba comprobando el silencio | Comprobar que aparezca un aviso | El criterio es justamente que **no** exija nada: la prueba es que no diga nada |

### 2.7 Dudas por resolver antes de escribir

Ninguna: los tres CA se prueban contra lo que ya está.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Los tres modelos existen y no se pisan

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Escribir el incremento: los tres modelos y qué dato es de cuál | `documentos-modelo/spec.md` | 2,5 |
| T-02 | Caso de prueba: por cada dato de la capa 3, comprobar que solo un modelo es su dueño | `plan_pruebas.md` | 1,5 |

### CA-02 — Lo que un programa lee tiene forma fija

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Prueba: una declaración de dominio mal escrita se detecta, y una bien escrita se lee entera | `validadores/pruebas.py` | 2,0 |

### CA-03 — Lo no declarado no se comprueba

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-04 | Prueba: sin declaración de stack, el revisor no exige nada de un stack que nadie nombró | `validadores/pruebas.py` | 2,0 |
| T-05 | Caso de prueba: con el dominio declarado a medias, se exige solo por lo declarado | `plan_pruebas.md` | 1,0 |

### RNF — Que la capa 3 se pueda leer sin el código

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-06 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 6 tareas · 10,5 horas.**

---

## 4. Secuencia de ejecución

T-03 → T-04 → T-05 primero, que son las corridas. T-02 en paralelo. T-01 con lo que salga. T-06 cierra.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Tabla dato → modelo dueño, sin dato repetido | T-02 |
| CA-02 | Declaración mal escrita y bien escrita contra el lector | T-03 |
| CA-03 | Silencio del revisor sobre lo que nadie declaró | T-04, T-05 |

---

## 6. Datos y ambiente de prueba

Carpetas temporales con capas 3 de mentira, y este repositorio. No se escribe en la capa 3 de ningún proyecto vivo. Ningún dato real y ninguna clave.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase. Lo único ejecutable que entra son dos pruebas.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

No aplica: no cambia lo que corre en los proyectos instalados. Sin subida de versión, porque no se toca `base/` ni `plantillas/`.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F2`](../../../../../base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md), [`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md), [`20·M3`](../../../../../base/20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que aparezca un dato con dos dueños entre los tres modelos | Se destapa trabajo sobre `plantillas/` | Se anota y se propone; cambiar un modelo sube versión | Abierto |
| R-02 | Que la prueba del silencio sea difícil de escribir sin falsos verdes | Prueba que pasa por no mirar | La prueba comprueba que el revisor **corrió** y no dijo nada, no que no corrió | Abierto |
| R-03 | Que otra sesión esté tocando la especificación del módulo | Pisar trabajo ajeno | Se relee justo antes de escribir | Abierto |

---

## 11. Definition of Done

- [ ] La especificación cubre los tres modelos y qué dato es de cuál.
- [ ] Hay prueba de que una declaración mal escrita se detecta.
- [ ] Hay prueba de que lo no declarado no genera exigencia, y de que el revisor sí corrió.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
