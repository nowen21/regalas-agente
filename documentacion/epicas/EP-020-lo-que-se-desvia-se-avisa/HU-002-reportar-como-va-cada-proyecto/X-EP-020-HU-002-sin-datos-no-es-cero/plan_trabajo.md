# Plan de Trabajo — Fase `X-EP-020-HU-002-sin-datos-no-es-cero` (módulo Avisos)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación. El requisito vive en la HU; las pruebas, en el `plan_pruebas`; lo que quedó hecho, en el `funcionalidad_implementada.md`.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `X-EP-020-HU-002-sin-datos-no-es-cero` |
| **Épica** | [EP-020](../../epica.md) |
| **HU** | [HU-002 Reportar cómo va cada proyecto](../HU-002-reportar-como-va-cada-proyecto.md), una sola (`F12.1`) |
| **Módulo** | Avisos |
| **Especificación del módulo** | [documentacion/avisos/spec.md](../../../../avisos/spec.md) |
| **Fecha apertura** | 2026-09-01 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN:**

- 📋 **Ficha de `F-030`:** *«decidir dónde poner el tiempo con datos, y no con impresión»*, y su advertencia: *«comparar proyectos distintos con la misma medida engaña si no se dice qué mide»*.

> **El usuario autorizó ejecutar sin aprobar paso por paso** el 2026-09-01.

**CA de la HU que cubre esta fase:** los tres, todos ☑.

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** mostrar el avance y la deuda de cada proyecto con la misma medida, y con la medida escrita al lado.

**Y que un proyecto sin datos aparezca así, no en cero.** Cero por cien dice «va mal»; sin datos dice «no se sabe», y son cosas distintas.

**Fuera de alcance:** ordenar los proyectos por bueno o malo, y la pantalla.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Lo que ya existe y se reutiliza:** la cuenta de fases de `EP-019` y los avisos de la fase `W`.

**Lo verificado:** hay un solo proyecto conectado, así que la comparación entre proyectos se probó con dos de mentiras. El caso del proyecto vacío es real: cualquiera recién conectado lo es.

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `plataforma/nucleo/avisos/reporte.py` | Crear | Servicio | La fila de cada proyecto |
| `plataforma/nucleo/avisos/management/commands/como_van.py` | Crear | Consola | La orden |
| `plataforma/nucleo/avisos/tests.py` | Modificar | Prueba | Los tres CA |
| `documentacion/avisos/spec.md` | Modificar | Especificación | Su §13 |

**Ninguna entidad y ninguna migración:** todo aviso se calcula al pedirlo, `DA-01`.

### 2.2 Matriz de dependencias del refactor

`core.py` no cambia: esta fase lo usa.

### 2.3 Rutas · 2.4 UI · 2.5 Permisos

No aplican: órdenes de consola.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **Cada columna sale con su definición debajo** | Documentarlo aparte | Comparar con la misma medida engaña si no se dice qué mide, y una definición que vive en otro archivo no se lee |
| **Sin datos no es cero** | Escribir «0 %%» | Cero dice «va mal»; sin datos dice «no se sabe» (`S-107`) |
| **Los sin datos van al final** | Ponerlos primeros, como los peores | No son los peores: son los que no se sabe |
| **La deuda y la vencida en columnas distintas** | Una sola cuenta | Diez avisos recientes y diez de hace un año no son lo mismo |
| **Las fases que no dicen desde cuándo tienen su columna** | Sumarlas a la deuda | No saber no es deuda: es no saber |

### 2.7 Dudas por resolver antes de codificar

Una, y hubo que resolverla antes de codificar: **el estándar nunca le puso fecha a una deuda**, así que «vencida» no estaba definida. Se definió acá, y sale escrita en el reporte.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | CA | Ev. |
|---|---|---|:--:|---|---|---|
| T-01 | La fila de un proyecto | Servicio | 1,5 h | — | CA-01 | EV-01 |
| T-02 | El avance, o «sin datos» | Servicio | 1 h | T-01 | CA-03 | EV-01 |
| T-03 | La deuda y la vencida, separadas | Servicio | 1 h | T-01 | CA-02 | EV-01 |
| T-04 | La definición de cada columna, con la tabla | Servicio | 1 h | T-03 | CA-01 | EV-01 |
| T-05 | La orden de consola | Consola | 30 min | T-04 | — | EV-01 |
| T-06 | Las pruebas de los tres CA | Test | 1,5 h | T-05 | Todos | EV-01 |

**Total estimado:** 6,5 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-06.

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Con dos proyectos de tamaños distintos | EV-01 | 2026-09-01 | ☑ |
| CA-02 | Con las dos clases de deuda mezcladas | EV-01 | 2026-09-01 | ☑ |
| CA-03 | Con un proyecto vacío | EV-01 | 2026-09-01 | ☑ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Las pruebas de la fase | `plataforma/nucleo/avisos/tests.py` |

---

## 6. Datos y ambiente de prueba

Carpetas temporales con fases, historias e inventarios de mentiras. Y **la corrida contra este repositorio**, que es de solo lectura.

---

## 7. Reversión / rollback  ·  Q11

**Módulo nuevo y de solo lectura.** Se quita y no queda rastro; lo único que escribe es el archivo de avisos callados, y lo escribe el usuario.

---

## 8. Producción y migración incremental  ·  Q12

**Aditivo puro.** Ninguna migración, ninguna dependencia nueva.

---

## 9. Reglas aplicadas  ·  Q13

- Base: `03·DA-01`, y el capítulo [`16`](../../../../../base/16-cumplimiento-y-calidad.md) por lo de reportar lo no verificado como tal.
- Producto: las `RN-1` a `RN-5` de la historia.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | **Que comparar proyectos distintos engañe** | **Alto: se decide mal con datos** | Cada columna sale con su definición debajo, siempre | Cerrado |
| B-02 | **Que un proyecto sin datos parezca el peor** | Alto | Sale como «sin datos», y de últimas | Cerrado |
| B-03 | Que la deuda vieja y la reciente se confundan | Medio | Van en columnas distintas | Cerrado |
| B-04 | Que el avance se lea como funcionalidad entregada | Medio | **Se declara en la definición:** mide fases cerradas | Declarado |

---

## 11. Definition of Done

- [x] Los tres CA verificados con evidencia
- [x] Comprobado que sin datos no es cero
- [x] Comprobado que la definición sale con la tabla
- [x] Las dos baterías en verde
- [x] Señales registradas
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
