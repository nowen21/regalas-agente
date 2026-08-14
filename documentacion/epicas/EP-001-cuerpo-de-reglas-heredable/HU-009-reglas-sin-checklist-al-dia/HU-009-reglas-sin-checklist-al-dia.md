# HU-009 — Poner al día las reglas que no pasan su propio checklist

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-009 |
| **Épica / Feature** | [EP-001 Cuerpo de reglas heredable y en capas](../epica.md) |
| **Módulo / Componente** | Cuerpo de reglas |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | L |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Backlog |

---

## 2. Narrativa

- **Como** quien confía en el cuerpo de reglas
- **Quiero** que ninguna regla esté publicada sin su checklist en CUMPLE
- **Para** que obedecer una regla no dependa de si alguien la revisó alguna vez

---

## 3. Contexto y descripción

El estándar tiene un checklist de veinte filas que toda regla debe pasar antes de publicarse. Cuando por fin se escribió el programa que lo mide, el resultado fue este: de 188 reglas, **129 no traen el bloque**, **7 lo traen en "no cumple"** y **33 no aparecen clasificadas** en el registro de lo validable, incluidos los capítulos `18` y `19` completos.

Las siete publicadas en "no cumple" son las que más pesan: `F4`, `F5`, `F12`, `M2`, `M4`, `M7` y `M8`. La regla que gobierna esto dice que sin CUMPLE una regla no se publica, y están publicadas.

No se trata de un descuido puntual. El checklist es posterior a la mayoría de las reglas, así que lo que hay es una deuda de nacimiento que hasta hoy nadie había podido contar.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Ninguna regla queda publicada con el checklist en "no cumple" |
| RN-02 | Toda regla vigente trae su bloque de checklist, con resultado y con la versión contra la que se aplicó |
| RN-03 | Toda regla aparece clasificada como validable o no |
| RN-04 | Una regla derogada no necesita checklist: se conserva por sus citas |
| RN-05 | Corregir una regla es cambiarla: pasa por el procedimiento completo, con versión y registro |

### 3.2 Supuestos

- Aplicar el checklist a una regla ya escrita toma minutos; lo que toma tiempo es decidir qué hacer con las que reprueban.

### 3.3 Fuera de alcance

- Cambiar el checklist. Aquí se aplica el que hay.
- El programa que lo mide, que ya existe.

---

## 4. Criterios de aceptación

### CA-01 — Ninguna regla queda publicada en "no cumple"

```gherkin
Dado que hay reglas publicadas con su checklist en "no cumple"
Cuando se cierra esta historia
Entonces ninguna regla vigente queda en ese estado
Y de cada una está escrito qué se hizo: se corrigió, se derogó o se acordó otra cosa
```

**Cómo validarlo:**

1. Correr la comprobación de meta-reglas sobre el cuerpo de reglas.
2. Leer los hallazgos de esa familia. Resultado esperado: ninguno dice "no cumple".
3. Tomar tres de las siete y abrir su archivo. Resultado esperado: cada una dice qué se decidió y contra qué versión.
- **Aprobado cuando:** el conteo de "no cumple" es cero y cada caso quedó explicado.

### CA-02 — Toda regla aparece clasificada

```gherkin
Dado que existe el registro de qué reglas son validables
Cuando se compara con el cuerpo de reglas
Entonces cada regla aparece en una de las tres listas
```

**Cómo validarlo:**

1. Correr la comprobación que cuenta las reglas sin clasificar.
2. Leer el resultado. Resultado esperado: cero.
3. Buscar en el registro una regla del capítulo `18` y otra del `19`. Resultado esperado: las dos están.
- **Aprobado cuando:** ninguna regla queda fuera del registro.

### CA-03 — Las que no traen bloque se van poniendo al día por capítulo

```gherkin
Dado que 129 reglas no traen su bloque de checklist
Cuando se cierra un capítulo
Entonces todas sus reglas traen el bloque con su resultado
```

**Cómo validarlo:**

1. Elegir un capítulo y aplicarle el checklist regla por regla.
2. Correr la comprobación acotada a ese capítulo. Resultado esperado: ninguna regla suya queda sin bloque.
3. Repetir con el capítulo siguiente. Resultado esperado: igual.
- **Aprobado cuando:** el trabajo avanza por capítulos y se puede medir cuánto falta.

### Criterios de aceptación transversales

- [ ] **No regresión** — una regla que ya traía su checklist no lo pierde ni cambia de resultado sin motivo escrito.
- [ ] **Límites** — está definido qué se hace con una regla derogada y con una sub-regla.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Trazabilidad** | Cada bloque dice contra qué versión se aplicó |
| **Progresividad** | El trabajo se puede partir por capítulos sin dejar el cuerpo inconsistente |
| **Honestidad** | Un resultado no se marca CUMPLE para salir del paso |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica, son documentos de texto.
- **Documento funcional:** el checklist del estándar, y el pendiente 19 que registró la medición.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Decidir qué se hace con las siete en "no cumple".
- [ ] Clasificar las 33 que faltan en el registro.
- [ ] Aplicar el checklist por capítulo a las 129 sin bloque.
- [ ] Versionar y registrar cada tanda.

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
| Dependencia | EP-004 · HU-011, porque el programa que mide ya existe | Alto |
| Riesgo | Que se marque CUMPLE en masa para bajar el número | El resultado se escribe fila por fila, y una sola ❌ reprueba |
| Riesgo | Que corregir una regla cambie lo que exige sin que nadie lo note | Cada corrección pasa por versión y registro |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] Ninguna regla vigente en "no cumple"
- [ ] Ninguna regla sin clasificar
- [ ] Los capítulos cerrados traen su bloque en todas sus reglas
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Parcial | Necesita el programa que mide, de EP-004 |
| **N**egociable | Sí | Qué se hace con las siete se puede discutir |
| **V**aliosa | Sí | Sin esto, el estándar exige lo que no cumple |
| **E**stimable | Sí | El alcance está contado: 129, 7 y 33 |
| **S**mall (pequeña) | No | Es la más grande de la épica |
| **T**esteable | Sí | Se prueba corriendo la comprobación |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde el hallazgo H-6 del 2026-08-14 |
