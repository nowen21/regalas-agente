# HU-003 — Crear los modelos de la fase: plan de trabajo, plan de pruebas, cierre

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-003 |
| **Épica / Feature** | [EP-003 Documentos modelo y procedimientos guiados](../epica.md) |
| **Módulo / Componente** | Documentos modelo |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Backlog |

---

## 2. Narrativa

- **Como** quien aprueba antes de que se toque código
- **Quiero** modelos para el plan de trabajo, el plan de pruebas y el cierre de una fase
- **Para** saber qué estoy aprobando y, al final, comparar lo prometido con lo entregado

---

## 3. Contexto y descripción

La fase es donde se ejecuta. Ahí se decide qué archivos se tocan, en qué orden, con qué se comprueba cada criterio y qué quedó hecho.

Son documentos distintos y no se pueden mezclar. El plan se aprueba antes; si los resultados se escriben encima, se pierde la línea base y ya no hay contra qué comparar. Por eso el registro de lo ejecutado va aparte, y el cierre resume lo entregado.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | La fase tiene su plan de trabajo, su plan de pruebas, su registro de resultados y su cierre |
| RN-02 | Los dos planes se aprueban antes de tocar código |
| RN-03 | El plan aprobado no se modifica para anotarle resultados |
| RN-04 | Ningún criterio de aceptación queda sin al menos un caso de prueba |
| RN-05 | Toda tarea del plan cuelga del criterio de aceptación que la justifica |
| RN-06 | El plan declara qué archivos se van a tocar, verificados contra el proyecto real |
| RN-07 | Un plan chico no llena el formato de uno grande: se declara qué secciones son obligatorias |

### 3.2 Supuestos

- Una fase pertenece a una sola historia de usuario y cubre criterios suyos.

### 3.3 Fuera de alcance

- Los modelos del encargo. Eso es HU-002.
- El procedimiento que los llena. Eso es HU-006.
- Comprobar automáticamente que quedaron completos. Eso es EP-004.

---

## 4. Criterios de aceptación

### CA-01 — Los documentos de la fase existen y no se pisan

```gherkin
Dado que se abre una fase
Cuando se buscan sus modelos
Entonces existen el plan de trabajo, el plan de pruebas, el registro de resultados y el cierre
Y ninguno pide anotar lo que le toca a otro
```

**Cómo validarlo:**

1. Abrir la carpeta de modelos del estándar.
2. Ubicar los cuatro. Resultado esperado: están los cuatro y cada uno dice para qué sirve.
3. Buscar en el plan de pruebas dónde se anota el resultado de una corrida. Resultado esperado: no se anota ahí, y el modelo lo dice y apunta al que corresponde.
- **Aprobado cuando:** cada documento responde una sola pregunta.

### CA-02 — El plan se aprueba antes y no se reescribe después

```gherkin
Dado que un plan de pruebas fue aprobado
Cuando se ejecutan las pruebas
Entonces lo ejecutado se registra en el documento de resultados
Y el plan aprobado queda igual
```

**Cómo validarlo:**

1. Llenar un plan de pruebas de prueba y darlo por aprobado.
2. Anotar su contenido.
3. Registrar una corrida en el documento de resultados y volver a abrir el plan. Resultado esperado: el plan no cambió.
- **Aprobado cuando:** se puede comparar lo acordado con lo ejecutado.

### CA-03 — Cada criterio de aceptación tiene su caso y cada tarea su criterio

```gherkin
Dado que se llena el plan de trabajo y el de pruebas de una fase
Cuando se revisan
Entonces cada criterio de aceptación tiene al menos un caso de prueba
Y cada tarea del plan cuelga de un criterio
```

**Cómo validarlo:**

1. Llenar los dos planes para una fase de prueba con tres criterios.
2. Revisar la tabla que cruza criterios con casos. Resultado esperado: los tres criterios tienen caso.
3. Revisar el desglose de tareas. Resultado esperado: cada tarea está bajo un criterio, o declarada como apoyo de uno.
- **Aprobado cuando:** no hay criterio sin probar ni tarea sin justificar.

### Criterios de aceptación transversales

- [ ] **Límites** — una fase recién abierta, sin nada ejecutado, tiene forma definida en el documento de resultados.
- [ ] **No regresión** — los planes ya escritos con estos modelos siguen siendo válidos.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Proporción** | Una fase chica no llena el formato de un release |
| **Trazabilidad** | Se puede ir del criterio al caso, del caso al resultado y del resultado al cierre |
| **Claridad** | Cada documento dice en su primera línea para qué sirve |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica, son documentos de texto.
- **Documento funcional:** [documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/epica.md](../epica.md), §5.1 y §5.4 fila 6.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Escribir el modelo del plan de trabajo, con el desglose por criterio de aceptación.
- [ ] Escribir el modelo del plan de pruebas, con la tabla que cruza criterios y casos.
- [ ] Escribir el modelo del registro de resultados, separado del plan.
- [ ] Escribir el modelo del cierre.
- [ ] Declarar qué secciones son obligatorias y cuáles se pueden borrar.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

Todavía no se descompuso en fases.

**Qué documento responde qué**, para no buscar en el que no es:

| Pregunta | Documento |
|---|---|
| Qué se pide y cuándo se da por aceptado | Esta HU |
| Qué se va a hacer, en qué orden y sobre qué archivos | `plan_trabajo.md` de la fase |
| Con qué casos se comprueba cada CA | `plan_pruebas.md` de la fase |
| Qué se ejecutó, con qué resultado, y si el CA quedó cumplido | `resultado_pruebas.md` de la fase |
| En qué estación va y qué la tiene detenida | `estado-fase.md` de la fase |
| Qué quedó hecho al final | `funcionalidad_implementada.md` de la fase |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-001, porque los modelos usan la marca acordada | Alto |
| Dependencia | HU-002, porque la fase cubre criterios de una historia | Alto |
| Riesgo | Que los resultados se escriban encima del plan aprobado | Son documentos separados y cada uno lo dice |
| Riesgo | Que el formato ahogue a las fases chicas | Se declara el mínimo obligatorio |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] Los cuatro documentos de la fase existen
- [ ] El plan aprobado no recibe resultados
- [ ] Ningún criterio queda sin caso ni tarea sin criterio
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Parcial | Necesita HU-001 y HU-002 |
| **N**egociable | Sí | Las secciones obligatorias se pueden discutir |
| **V**aliosa | Sí | Es lo que se aprueba antes de gastar tiempo en código |
| **E**stimable | Sí | Son cuatro documentos |
| **S**mall (pequeña) | No | Cuatro modelos en una historia |
| **T**esteable | Sí | Se prueba llevando una fase de punta a punta |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
