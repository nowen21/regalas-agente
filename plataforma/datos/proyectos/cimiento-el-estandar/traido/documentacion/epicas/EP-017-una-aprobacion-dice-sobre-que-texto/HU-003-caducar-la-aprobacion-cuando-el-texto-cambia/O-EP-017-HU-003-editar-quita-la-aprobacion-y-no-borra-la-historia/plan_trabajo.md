# Plan de Trabajo — Fase `O-EP-017-HU-003-editar-quita-la-aprobacion-y-no-borra-la-historia` (módulo Aprobaciones)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación. El requisito vive en la HU; las pruebas, en el `plan_pruebas`; lo que quedó hecho, en el `funcionalidad_implementada.md`.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `O-EP-017-HU-003-editar-quita-la-aprobacion-y-no-borra-la-historia` |
| **Épica** | [EP-017](../../epica.md) |
| **HU** | [HU-003 Caducar la aprobación cuando el texto cambia](../HU-003-caducar-la-aprobacion-cuando-el-texto-cambia.md), una sola (`F12.1`) |
| **Módulo** | Aprobaciones |
| **Especificación del módulo** | [documentacion/aprobaciones/spec.md](../../../../aprobaciones/spec.md) |
| **Fecha apertura** | 2026-09-01 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN:**

- 🩹 **Caso real, escrito en la ficha de `F-017`:** se aprobaron tres documentos y al día siguiente el cambio de producto los dejó sin valor. **Nada avisó.**

> **El usuario autorizó ejecutar sin aprobar paso por paso** el 2026-09-01.

**CA de la HU que cubre esta fase:** los tres, todos ☑.

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** que editar un documento aprobado le quite la aprobación, que se diga cuánto cambió, y que la aprobación anterior no se borre.

**Lo que la vuelve posible es la huella** de la fase `M`. Sin ella no hay forma de saber si el texto cambió: solo que alguien firmó alguna vez.

**Fuera de alcance:** el diff completo, que lo da el control de versiones; y volver a aprobar solo.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Lo que ya existe y se reutiliza:** la aprobación con su huella y su tamaño.

**Lo verificado:** el caso que originó la funcionalidad está escrito en su propia ficha, y es el único de todo el inventario que cuenta un daño ya ocurrido.

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `plataforma/nucleo/aprobaciones/core.py` | Modificar | Servicio | Caducar y medir el cambio |
| `plataforma/nucleo/aprobaciones/tests.py` | Modificar | Prueba | Los tres CA |
| `documentacion/aprobaciones/spec.md` | Modificar | Especificación | Su §13, para nombrar la fase |

**Ninguna entidad nueva y ninguna migración.**

### 2.2 Matriz de dependencias del refactor

`core.py` crece; lo de las dos fases anteriores no cambia, y sus pruebas lo comprueban.

### 2.3 Rutas · 2.4 UI · 2.5 Permisos

No aplican.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **La huella decide** | Comparar fechas de modificación | Una fecha cambia al tocar el archivo aunque el texto sea el mismo |
| **Nada se borra** | Reemplazar la aprobación anterior | Es la historia de qué se autorizó y cuándo |
| **Lo que cambió se mide en caracteres** | Un diff completo | El diff lo da el control de versiones; acá alcanza para decidir si mirar |
| **Un documento que desaparece también caduca** | Dejarlo aprobado | Una aprobación sobre algo que no está no cubre nada |
| **Un cambio de tipografía caduca la aprobación** | Descontarlo | **Se acepta:** una aprobación responde por el texto exacto, no por lo que significa |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | CA | Ev. |
|---|---|---|:--:|---|---|---|
| T-01 | Comparar la huella con la de la última aprobación | Servicio | 1 h | — | CA-01 | EV-01 |
| T-02 | Medir cuánto cambió | Servicio | 1 h | T-01 | CA-02 | EV-01 |
| T-03 | Conservar la historia | Servicio | 1 h | — | CA-03 | EV-01 |
| T-04 | Tratar el documento que desapareció | Servicio | 1 h | T-01 | Transversal | EV-01 |
| T-05 | Las pruebas de los tres CA | Test | 2 h | T-04 | Todos | EV-01 |

**Total estimado:** 6 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-05.

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Aprobando y editando | EV-01 | 2026-09-01 | ☑ |
| CA-02 | Editando para agregar y para quitar | EV-01 | 2026-09-01 | ☑ |
| CA-03 | Aprobando dos veces | EV-01 | 2026-09-01 | ☑ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Las pruebas de la caducidad | `plataforma/nucleo/aprobaciones/tests.py` |

---

## 6. Datos y ambiente de prueba

Carpetas temporales con documentos de mentiras.

---

## 7. Reversión / rollback  ·  Q11

Nada que revertir: esta fase no borra nada, y ese es justamente su punto.

---

## 8. Producción y migración incremental  ·  Q12

**Aditivo puro.** Ninguna migración, ninguna dependencia nueva.

---

## 9. Reglas aplicadas  ·  Q13

- Base: el capítulo [`15`](../../../../../base/15-registros-inmutables.md), por lo de que nada se borra.
- Producto: las `RN-1` a `RN-4` de la historia.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | **Que caducar borre la aprobación anterior** | **Alto: se pierde la historia** | Cada aprobación se agrega, y hay prueba de que quedan las dos | Cerrado |
| B-02 | Que un documento borrado siga apareciendo como aprobado | Alto | También caduca, y se dice | Cerrado |
| B-03 | Que un cambio de tipografía caduque una aprobación | Bajo | **Se acepta y se declara:** una aprobación responde por el texto exacto | Declarado |

---

## 11. Definition of Done

- [x] Los tres CA verificados con evidencia
- [x] Comprobado que editar caduca
- [x] Comprobado que la anterior no se borra
- [x] Las dos baterías en verde
- [x] Señales registradas
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
