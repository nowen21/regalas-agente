# Plan de Trabajo — Fase `E-EP-015-HU-002-el-estado-sale-de-la-fase-que-corrio` (módulo Comprobaciones)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación. El requisito vive en la HU; las pruebas, en el `plan_pruebas`; lo que quedó hecho, en el `funcionalidad_implementada.md`.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `E-EP-015-HU-002-el-estado-sale-de-la-fase-que-corrio` |
| **Épica** | [EP-015](../../epica.md) |
| **HU** | [HU-002 Fijar el estado desde la evidencia](../HU-002-fijar-el-estado-desde-la-evidencia.md) — **una sola** (`F12.1`) |
| **Módulo** | Comprobaciones |
| **Especificación del módulo** | [documentacion/comprobaciones/spec.md](../../../../comprobaciones/spec.md) |
| **Fecha apertura** | 2026-09-01 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN:**

- ✨ **Funcionalidad nueva:** `F-021`. El inventario tiene 35 funcionalidades y **las 35 dicen «Sin verificar»**.

> **El usuario autorizó ejecutar sin aprobar paso por paso** el 2026-09-01.

**CA de la HU que cubre esta fase:** los cuatro, todos ☑.

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** que el estado de una funcionalidad salga de la fase que la construyó, y no de lo que alguien escribió.

**La cadena ya existe**, y hay que seguirla, no inventarla:

```
inventario -> especificacion del modulo (13) -> fase -> veredicto
```

**Fuera de alcance:** escribir el estado en el inventario, e impedir publicar.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Lo medido el 2026-09-01, antes de construir:**

| Qué se midió | Resultado |
|---|---|
| Funcionalidades en el inventario | **35** |
| Cuántas dicen «Sin verificar» | **35** |
| Especificaciones con tabla de trazabilidad | 8 de 10 |
| Funcionalidades con fila de trazabilidad | 18 |
| **Filas que nombran la fase por su letra sola** | **7** |

**Las siete que nombran por letra son de la versión 1**, cuando la convención era otra. Una letra sola no se puede seguir: cada épica tiene su «A».

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `plataforma/nucleo/comprobaciones/estado.py` | Nuevo | Servicio | Derivar el estado |
| `plataforma/nucleo/comprobaciones/management/commands/estado_funcionalidades.py` | Nuevo | Orden | Pedirlo |
| `plataforma/nucleo/comprobaciones/tests_estado.py` | Nuevo | Prueba | Los cuatro CA |
| `documentacion/proyectos/spec.md` | Modificar | Especificación | Su §13: cuatro filas con el nombre completo |
| `documentacion/auditoria/spec.md` | Modificar | Especificación | Su §13: una fila |
| `documentacion/importacion/spec.md` | Modificar | Especificación | Su §13: dos filas |
| `cvds/analisis-requisitos/inventario-funcionalidades.md` | Modificar | Inventario | Decir que la columna se deriva |

**Las tres especificaciones se tocan por su §15**, que existe para esto: registrar un cambio después de aprobada.

### 2.2 Matriz de dependencias del refactor

`core.py` no se toca. `estado.py` es nuevo y solo lee.

### 2.3 Rutas · 2.4 UI · 2.5 Permisos

No aplican.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **El estado se deriva al pedirlo** | Escribirlo en el inventario | Una copia escrita envejece, y volvería a ser lo que alguien cree |
| **Se leen las dos formas de veredicto** | Reescribir las fases viejas | Una fase cerrada dice lo que era cierto el día que cerró |
| **Las filas de trazabilidad se completan con el nombre entero** | Aceptar la letra sola | Cada épica tiene su «A»: la letra sola es ambigua |
| **El estado dice de dónde sale** | Devolver solo la palabra | Un estado sin origen es una opinión |
| **Varias fases: verificada solo si todas declararon** | Con una basta | Una funcionalidad a medias no está verificada |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | CA | Ev. |
|---|---|---|:--:|---|---|---|
| T-01 | Leer las funcionalidades del inventario | Servicio | 1 h | — | — | EV-01 |
| T-02 | Seguir la §13 de cada especificación hasta la fase | Servicio | 2 h | T-01 | CA-01 | EV-01 |
| T-03 | Leer el veredicto, **en sus dos formas** | Servicio | 1 h | T-02 | CA-04 | EV-01 |
| T-04 | Derivar el estado, con su porqué | Servicio | 1 h | T-03 | CA-01 a CA-03 | EV-01 |
| T-05 | Completar las siete filas que nombran por letra | Doc | 1 h | T-02 | CA-01 | EV-02 |
| T-06 | La orden de consola | Orden | 1 h | T-04 | Todos | EV-02 |
| T-07 | Las pruebas de los cuatro CA | Test | 2 h | T-06 | Todos | EV-01 |
| T-08 | **Correrlo sobre este repositorio y contar** | Medición | 1 h | T-06 | CA-01 | EV-02 |

**Total estimado:** 10 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-04 → T-06 → T-08. T-05 sale de lo que T-02 encuentra.

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Sobre este repositorio: que las construidas salgan verificadas | EV-01, EV-02 | 2026-09-01 | ☑ |
| CA-02 | Sin fase, y con fase sin veredicto | EV-01 | 2026-09-01 | ☑ |
| CA-03 | Con una fase que declare «No cumple» | EV-01 | 2026-09-01 | ☑ |
| CA-04 | Con la forma de veredicto de la versión 1 | EV-01, EV-02 | 2026-09-01 | ☑ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Las pruebas del estado | `plataforma/nucleo/comprobaciones/tests_estado.py` |
| EV-02 | La cuenta sobre este repositorio | `resultado_pruebas.md` §1 |

---

## 6. Datos y ambiente de prueba

Carpetas temporales con inventario, especificación y fases de mentiras, y este repositorio para la cuenta. Solo se lee.

---

## 7. Reversión / rollback  ·  Q11

Nada que revertir: no escribe. Los siete cambios de trazabilidad están versionados.

---

## 8. Producción y migración incremental  ·  Q12

**Aditivo puro.** Ninguna migración, ninguna dependencia nueva.

---

## 9. Reglas aplicadas  ·  Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F19`](../../../../../base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md).
- Producto: `DA-01`, y las `RN-1` a `RN-4` de la historia.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que la cadena esté rota en alguna especificación | Medio | Entonces queda sin verificar, que es la respuesta correcta | Cerrado por diseño |
| B-02 | **Que el molde del veredicto haya cambiado** | Alto | Se leen las dos formas. **Apareció construyendo**, con siete funcionalidades cerradas saliendo sin verificar | Cerrado |
| B-03 | Que el estado derivado y el escrito en el inventario se contradigan | Medio | El inventario deja de mantener esa columna a mano y apunta a la orden | Cerrado |

---

## 11. Definition of Done

- [x] Los cuatro CA verificados con evidencia
- [x] Este repositorio medido, con la cuenta escrita
- [x] Las dos baterías en verde
- [x] Señales registradas
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
