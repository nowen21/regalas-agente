# Plan de Trabajo — Fase `C-EP-014-HU-001-se-tapa-lo-que-se-teclea-no-lo-que-se-copia` (módulo Seguridad)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas` de esta misma fase; lo que quedó hecho, en el `funcionalidad_implementada.md` del cierre.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `C-EP-014-HU-001-se-tapa-lo-que-se-teclea-no-lo-que-se-copia` |
| **Épica** | [EP-014](../../epica.md) |
| **HU** | [HU-001 Tapar la clave al escribirla](../HU-001-tapar-la-clave-al-escribirla.md) — **una sola** (`F12.1`) |
| **Módulo** | Seguridad |
| **Especificación del módulo** | [documentacion/seguridad/spec.md](../../../../seguridad/spec.md), aprobada el 2026-09-01 |
| **Fecha apertura** | 2026-09-01 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN:**

- 🩹 **Agujero abierto:** `F-031` estaba construida a medias y sin declarar. El puente que tapa claves existía y **lo usaba un solo camino de los seis que escriben**.

> **El usuario autorizó ejecutar la épica entera sin aprobar paso por paso.** Lo dijo el 2026-09-01: *«haga todo y no me pregunte tanto»*. El plan y la implementación fueron juntos, con el alcance que la medición previa fijó. Queda escrito porque `02·F0` pide aprobación por eslabón y acá se dio una sola vez, para todos.

**CA de la HU que cubre esta fase:**

| CA de `HU-001` que cierra esta fase | Estado |
|---|---|
| [CA-01 — Una clave tecleada al llenar un hueco queda tapada](../HU-001-tapar-la-clave-al-escribirla.md#ca-01--una-clave-tecleada-al-llenar-un-hueco-queda-tapada) | ☑ |
| [CA-02 — Se dice que se tapó](../HU-001-tapar-la-clave-al-escribirla.md#ca-02--se-dice-que-se-tapó) | ☑ |
| [CA-03 — Lo importado no se altera](../HU-001-tapar-la-clave-al-escribirla.md#ca-03--lo-importado-no-se-altera) | ☑ |
| [CA-04 — Lo que no se tapa se dice](../HU-001-tapar-la-clave-al-escribirla.md#ca-04--lo-que-no-se-tapa-se-dice) | ☑ |
| [CA-05 — Sin enmascarador no se escribe](../HU-001-tapar-la-clave-al-escribirla.md#ca-05--sin-enmascarador-no-se-escribe) | ☑ |

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** que lo que alguien teclea desde la plataforma llegue al archivo con la clave tapada, y que lo que ya existía entre como está y se diga.

**La decisión que gobierna la fase, medida antes de empezar.** Se midió qué pasaría si taparan los seis caminos: cambiaría **7 documentos y 21 fragmentos** de los 1 002 guardados. Los 21 son claves inventadas en los documentos de las fases **que construyeron el tapador**. Tapar al importar corrompería la documentación del propio tapador, en silencio y sin vuelta atrás.

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | La clave tecleada se tapa | Funcional | Baja |
| CA-02 | Se dice cuántas | Funcional | Baja |
| CA-03 | **Lo importado no se altera** | Funcional | **Alta** |
| CA-04 | Lo que no se tapa se dice | Funcional | Media |
| CA-05 | **Sin enmascarador no se escribe** | Funcional | **Alta** |

**Fuera de alcance:**

- Tapar lo importado.
- Reconocer formas nuevas de credencial: eso vive en el estándar.
- Pantalla.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Lo que ya existe y se reutiliza:**

| Pieza | Qué aporta |
|---|---|
| `validadores/enmascarar.py` | Reconoce ocho formas de secreto, con y sin comillas, y no tapa los moldes |
| `plataforma/nucleo/seguridad/claves.py` | El puente, que revienta si el enmascarador no está |
| `plataforma/nucleo/auditoria/core.py` | El único camino que ya tapaba |
| `plataforma/nucleo/ciclo_de_vida/core.py` | El camino que teclea, abierto por `EP-013` |

**Lo medido sobre lo real el 2026-09-01:**

| Qué se midió | Resultado |
|---|---|
| Caminos que escriben | 6 |
| Caminos que tapaban | **1** |
| Documentos guardados | 1 002 |
| Los que el tapador cambiaría | **7**, con 21 fragmentos |
| Cuántos de esos 21 son claves de verdad | **Ninguna** |

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `plataforma/nucleo/seguridad/revision.py` | Nuevo | Servicio | Contar sin tocar |
| `plataforma/nucleo/seguridad/apps.py` | Nuevo | Config | El módulo pasa a ser aplicación, para tener órdenes |
| `plataforma/nucleo/seguridad/management/commands/revisar_claves.py` | Nuevo | Orden | El aviso |
| `plataforma/nucleo/seguridad/tests.py` | Nuevo | Prueba | Los cinco CA |
| `plataforma/nucleo/ciclo_de_vida/core.py` | Modificar | Servicio | Tapar antes de escribir, y devolver cuántas |
| `plataforma/config/settings/base.py` | Modificar | Config | `nucleo.seguridad` en la lista de aplicaciones |
| `documentacion/seguridad/spec.md` | Nuevo | Especificación | El módulo no tenía |

**Ninguna entidad y ninguna migración.**

### 2.2 Matriz de dependencias del refactor

`ciclo_de_vida/core.py` gana dos líneas en `llenar` y una clave más en lo que devuelve. Lo que ya tenía no cambia, y sus 50 pruebas lo comprueban.

### 2.3 Rutas · 2.4 UI · 2.5 Permisos

No aplican.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **Se tapa lo que se teclea, no lo que se copia** | Tapar en los seis caminos | Medido: alteraría 7 documentos reales sin vuelta atrás |
| **La importación avisa en vez de tapar** | Callarse | Perder en silencio es perder igual |
| **Se devuelve cuántas se taparon** | Tapar en silencio | El usuario tiene que saber que lo que escribió no quedó igual |
| **Contar tapa una copia y la descarta** | Escribir un reconocedor aparte para contar | Dos listas de secretos se separan; contar con el mismo tapador garantiza que la cuenta y el tapado coincidan |
| **Cada camino se declara en la especificación** | Dejarlo implícito | El camino que nace sin declararse es el que va a dejar pasar la próxima |

### 2.7 Dudas por resolver antes de codificar

Ninguna: la de qué caminos tapan se resolvió con la medición.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | CA | Ev. |
|---|---|---|:--:|---|---|---|
| T-01 | Medir qué pasaría si taparan todos los caminos | Medición | 1 h | — | CA-03 | EV-02 |
| T-02 | Tapar en el camino que llena, y devolver cuántas | Servicio | 1 h | T-01 | CA-01, CA-02 | EV-01 |
| T-03 | Contar sin tocar, y ordenar de más a menos | Servicio | 1 h | T-01 | CA-04 | EV-01 |
| T-04 | El módulo como aplicación, y su orden de consola | Orden | 1 h | T-03 | CA-04 | EV-02 |
| T-05 | La especificación del módulo, que no existía | Doc | 2 h | T-01 | — | — |
| T-06 | Las pruebas de los cinco CA | Test | 2 h | T-04 | Todos | EV-01 |
| T-07 | Correr la orden sobre los 1 002 documentos reales | Medición | 1 h | T-04 | CA-04 | EV-02 |

**Total estimado:** 9 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-04 → T-07. La medición va primero: es la que fija el alcance.

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Llenar un hueco con una clave y leer el archivo | EV-01 | 2026-09-01 | ☑ |
| CA-02 | Llenar y mirar el número que vuelve | EV-01 | 2026-09-01 | ☑ |
| CA-03 | Comprobar que un documento con clave de ejemplo se guarda tal cual | EV-01 | 2026-09-01 | ☑ |
| CA-04 | **La orden sobre los 1 002 documentos reales** | EV-02 | 2026-09-01 | ☑ |
| CA-05 | Apuntar la ruta de validadores a una carpeta que no existe | EV-01 | 2026-09-01 | ☑ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Las pruebas del módulo | `plataforma/nucleo/seguridad/tests.py` |
| EV-02 | La orden sobre este repositorio | `resultado_pruebas.md` §1 |

---

## 6. Datos y ambiente de prueba

Carpetas temporales, con **claves inventadas** escritas por la prueba. Nunca una real: es lo que exige [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar), y acá con más razón.

---

## 7. Reversión / rollback  ·  Q11

El código está versionado. **Lo que esta fase no puede deshacer es lo que tapa**, y por eso el alcance se recortó antes de construir.

---

## 8. Producción y migración incremental  ·  Q12

**Aditivo puro.** Ninguna migración, ninguna dependencia nueva. Una aplicación más en la lista.

---

## 9. Reglas aplicadas  ·  Q13

- Base: [`00·N6`](../../../../../base/00-nucleo-blindado.md), blindada, de la que baja todo el módulo. Y [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar).
- Producto: `RF-31`, y las `RN-1` a `RN-6` de la especificación del módulo.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | **Tapar de más y corromper un documento sin vuelta atrás** | **Alto — no se deshace** | Se midió antes de construir: por eso lo importado no se tapa | Cerrado por diseño |
| B-02 | Tapar de menos y que una clave quede escrita | Alto | El reconocimiento vive en el estándar, con sus pruebas | Cerrado |
| B-03 | Que un camino nuevo nazca sin tapar | Medio | Los seis quedan declarados en la §5.1 de la especificación | Cerrado |

---

## 11. Definition of Done

- [x] Los cinco CA verificados con evidencia
- [x] La orden corrida sobre los 1 002 documentos reales
- [x] Comprobado que ningún documento importado cambia
- [x] Las dos baterías en verde
- [x] Señales registradas
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
