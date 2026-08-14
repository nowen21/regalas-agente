# HU-005 — Sellar el trabajo cerrado con su versión

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-005 |
| **Épica / Feature** | [EP-002 Versionado de las reglas y adopción por proyecto](../epica.md) |
| **Módulo / Componente** | Versionado del estándar |
| **Tipo** | Técnica |
| **Prioridad** | Should |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Backlog |

---

## 2. Narrativa

- **Como** quien ya cerró un trabajo
- **Quiero** que quede sellado con la versión de reglas bajo la que se cerró
- **Para** que un cambio posterior de las reglas no obligue a reabrirlo

---

## 3. Contexto y descripción

Si cada cambio de reglas obligara a revisar todo lo ya terminado, nadie cambiaría una regla nunca. Y si no obligara a nada, las reglas no servirían de nada.

La salida es sellar: lo cerrado queda con la versión que regía ese día, y se juzga contra esa. La regla nueva aplica al trabajo en curso y al que viene.

Sin el sello, la pregunta "¿esto cumple?" no tiene respuesta, porque depende de contra qué versión se pregunte.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Todo trabajo que se cierra queda con la versión de reglas bajo la que se cerró |
| RN-02 | Un cambio de reglas no reabre lo ya cerrado |
| RN-03 | La versión nueva aplica al trabajo en curso y al que viene |
| RN-04 | El sello se escribe al cerrar, no después |
| RN-05 | Si un trabajo cerrado se reabre por otro motivo, se juzga contra la versión vigente en ese momento |

### 3.2 Supuestos

- Cerrar un trabajo es un momento identificable, con su documento de cierre.

### 3.3 Fuera de alcance

- Migrar trabajo viejo a reglas nuevas. Si se decide hacerlo, es una tarea propia y acordada.

---

## 4. Criterios de aceptación

### CA-01 — Lo cerrado queda sellado

```gherkin
Dado que se cierra una unidad de trabajo
Cuando se escribe su documento de cierre
Entonces queda registrada la versión de reglas vigente ese día
```

**Cómo validarlo:**

1. Cerrar una unidad de trabajo de prueba.
2. Abrir su documento de cierre. Resultado esperado: trae la versión con que se cerró.
3. Compararla con la versión vigente ese día. Resultado esperado: coinciden.
- **Aprobado cuando:** el cierre dice contra qué reglas se hizo.

### CA-02 — Un cambio de reglas no reabre lo cerrado

```gherkin
Dado que existe trabajo cerrado y sellado
Cuando el estándar sube de versión
Entonces ese trabajo no se marca como incumplido
```

**Cómo validarlo:**

1. Tomar una unidad cerrada y sellada con una versión anterior.
2. Subir la versión del estándar con un cambio que obligue.
3. Revisar el estado de esa unidad. Resultado esperado: sigue cerrada y nadie pide revisarla.
- **Aprobado cuando:** cambiar una regla no genera trabajo sobre lo terminado.

### Criterios de aceptación transversales

- [ ] **Límites** — una unidad que quedó a medias y se retoma después del cambio se juzga contra la versión nueva.
- [ ] **No regresión** — los cierres ya escritos sin sello no se invalidan; se les puede agregar cuando se toquen.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Trazabilidad** | Cada cierre dice contra qué versión se juzgó |
| **Estabilidad** | Lo cerrado no cambia de estado por un cambio de reglas |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica.
- **Documento funcional:** [documentacion/epicas/EP-002-versionado-y-adopcion/epica.md](../epica.md), criterio CAE-05 y §5.4 detalle 25.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Definir dónde se escribe el sello dentro del cierre.
- [ ] Escribir la regla de que lo cerrado no se reabre por un cambio de versión.
- [ ] Definir qué pasa con lo que quedó a medias.

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
| Dependencia | HU-001, porque el sello es un número de versión | Alto |
| Dependencia | EP-003, porque el sello vive en el documento de cierre | Medio |
| Riesgo | Que el sello se use como excusa para no actualizar nunca | El sello vale para lo cerrado; lo en curso sigue la versión vigente |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] El cierre registra la versión con que se cerró
- [ ] Está escrito que un cambio de reglas no reabre lo cerrado
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Parcial | Necesita el número de HU-001 |
| **N**egociable | Sí | Dónde va el sello se puede discutir |
| **V**aliosa | Sí | Permite cambiar reglas sin generar trabajo sobre lo terminado |
| **E**stimable | Sí | Alcance corto |
| **S**mall (pequeña) | Sí | Un dato en el cierre y una regla |
| **T**esteable | Sí | Se prueba subiendo la versión con trabajo ya cerrado |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
