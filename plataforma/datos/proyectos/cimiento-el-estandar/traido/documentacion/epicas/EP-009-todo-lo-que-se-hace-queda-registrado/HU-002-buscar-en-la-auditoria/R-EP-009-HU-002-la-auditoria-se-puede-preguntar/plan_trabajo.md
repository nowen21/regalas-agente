# Plan de Trabajo — Fase `R-EP-009-HU-002-la-auditoria-se-puede-preguntar` (módulo Auditoría)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación. El requisito vive en la HU; las pruebas, en el `plan_pruebas`; lo que quedó hecho, en el `funcionalidad_implementada.md`.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `R-EP-009-HU-002-la-auditoria-se-puede-preguntar` |
| **Épica** | [EP-009](../../epica.md) |
| **HU** | [HU-002 Buscar en la auditoría](../HU-002-buscar-en-la-auditoria.md), una sola (`F12.1`) |
| **Módulo** | Auditoría |
| **Especificación del módulo** | [documentacion/auditoria/spec.md](../../../../auditoria/spec.md) |
| **Fecha apertura** | 2026-09-01 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN:**

- 📋 **Ficha de `F-019`:** *«sin esta, la auditoría existe pero no sirve»*.

> **El usuario autorizó ejecutar sin aprobar paso por paso** el 2026-09-01.

**CA de la HU que cubre esta fase:** los tres, todos ☑.

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** poder preguntarle a la auditoría por proyecto, por fecha y por tipo de acción.

**Es la segunda mitad de `EP-009`.** La primera dejó todo registrado con la constancia antes que el efecto; esta lo vuelve consultable.

**Fuera de alcance:** la pantalla y exportar el resultado.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Lo que ya existe y se reutiliza:** el registro de auditoría de la fase `D`, con su entidad y sus campos.

**Lo verificado:** la fecha se guarda como texto, y por eso el rango se arma comparando texto. **El día del hasta no entra solo:** hay que hacerlo entrar.

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `plataforma/nucleo/auditoria/busqueda.py` | Crear | Servicio | Los tres filtros |
| `plataforma/nucleo/auditoria/management/commands/buscar_en_la_auditoria.py` | Crear | Consola | La orden |
| `plataforma/nucleo/auditoria/tests_busqueda.py` | Crear | Prueba | Los tres CA |
| `documentacion/auditoria/spec.md` | Modificar | Especificación | Su §13 |

**Ninguna entidad nueva y ninguna migración:** se consulta lo que ya está.

### 2.2 Matriz de dependencias del refactor

**Nada de la fase `D` se toca.** El registro sigue igual; esta fase solo lee.

### 2.3 Rutas · 2.4 UI · 2.5 Permisos

No aplican.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **El día del `hasta` entra completo** | Comparar solo la fecha | La hora va pegada al texto; sin esto, el último día se pierde entero |
| **La respuesta dice cuántos y en cuánto tiempo** | Devolver solo la lista | El CA-03 pide un tiempo medido, no supuesto |
| **Un resultado vacío se dice con palabras** | Devolver una lista vacía | Un vacío se ve igual que una falla — `S-110` |
| **Si se recorta, se avisa** | Recortar en silencio | Un recorte callado se lee como «eso es todo lo que hay» |
| **Los tipos de acción se sacan de lo registrado** | Una lista fija en el código | Una lista fija envejece sin avisar |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | CA | Ev. |
|---|---|---|:--:|---|---|---|
| T-01 | Filtrar por proyecto, fecha y tipo | Servicio | 1,5 h | — | CA-01 | EV-01 |
| T-02 | Que el día del `hasta` entre completo | Servicio | 30 min | T-01 | Transversal | EV-01 |
| T-03 | Decir cuando no hay coincidencias | Servicio | 30 min | T-01 | CA-02 | EV-01 |
| T-04 | Medir el tiempo y avisar del recorte | Servicio | 1 h | T-01 | CA-03 | EV-01 |
| T-05 | Los tipos de acción, sacados de lo registrado | Servicio | 30 min | T-01 | CA-01 | EV-01 |
| T-06 | La orden de consola | Consola | 1 h | T-05 | — | EV-01 |
| T-07 | Las pruebas de los tres CA | Test | 2 h | T-06 | Todos | EV-01 |

**Total estimado:** 7 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-04 → T-07.

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Con registros de varios proyectos, fechas y acciones | EV-01 | 2026-09-01 | ☑ |
| CA-02 | Buscando algo que no está | EV-01 | 2026-09-01 | ☑ |
| CA-03 | Midiendo con un volumen de un año | EV-01 | 2026-09-01 | ☑ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Las pruebas de la búsqueda | `plataforma/nucleo/auditoria/tests_busqueda.py` |

---

## 6. Datos y ambiente de prueba

Registros de mentiras, de varios proyectos y varias fechas, en la base de pruebas.

---

## 7. Reversión / rollback  ·  Q11

**Esta fase solo lee.** Se quita el archivo y no queda rastro.

---

## 8. Producción y migración incremental  ·  Q12

**Aditivo puro.** Ninguna migración, ninguna dependencia nueva.

---

## 9. Reglas aplicadas  ·  Q13

- Base: el capítulo [`06`](../../../../../base/06-rendimiento.md) por el tiempo de respuesta, y [`15`](../../../../../base/15-registros-inmutables.md) porque nada de lo registrado se toca.
- Producto: las `RN-1` a `RN-4` de la historia.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | **Que el rango deje por fuera el último día** | **Alto: se pierde justo lo más reciente** | El `hasta` entra completo, y hay prueba | Cerrado |
| B-02 | Que un vacío se lea como una falla | Medio | Se dice con palabras | Cerrado |
| B-03 | Que un resultado grande se recorte en silencio | Medio | Se avisa que se recortó | Cerrado |
| B-04 | Que el tiempo se suponga en vez de medirse | Medio | La respuesta trae los segundos | Cerrado |

---

## 11. Definition of Done

- [x] Los tres CA verificados con evidencia
- [x] Comprobado que el último día entra
- [x] El tiempo medido, no supuesto
- [x] Las dos baterías en verde
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
