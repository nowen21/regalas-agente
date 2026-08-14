# HU-005 — Separar lo que el proyecto aprendió de cómo el usuario quiere trabajar

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-005 |
| **Épica / Feature** | [EP-006 Memoria de lo aprendido](../epica.md) |
| **Módulo / Componente** | Memoria |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Backlog |

---

## 2. Narrativa

- **Como** quien corrige a la IA cuando trabaja distinto de lo que espera
- **Quiero** que eso se guarde aparte de lo que el proyecto aprendió
- **Para** que una preferencia mía no viaje como si fuera conocimiento del proyecto

---

## 3. Contexto y descripción

Son dos cosas que se parecen y no lo son. Una es lo que el proyecto aprendió: por qué se decidió esto, cómo se resolvió aquel error. La otra es cómo quiere el usuario que se trabaje: que las respuestas sean cortas, que no se commitee sin permiso.

Si se guardan juntas, pasan dos cosas malas. La preferencia del usuario se lee como si fuera una decisión técnica del proyecto, y el conocimiento del proyecto se pierde entre indicaciones de estilo.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Lo que el proyecto aprendió y cómo quiere trabajar el usuario se guardan por separado |
| RN-02 | Cada uno tiene su lugar y su índice |
| RN-03 | Una preferencia del usuario dice también por qué la pidió |
| RN-04 | Lo que aplica a cualquier proyecto se distingue de lo que aplica solo a este |
| RN-05 | Ninguna de las dos reemplaza a una regla del estándar |

### 3.2 Supuestos

- El usuario corrige a la IA cuando algo no le gusta, y esa corrección vale para las sesiones siguientes.

### 3.3 Fuera de alcance

- Convertir una preferencia repetida en regla del estándar. Esa decisión es de una persona.

---

## 4. Criterios de aceptación

### CA-01 — Las dos cosas se guardan por separado

```gherkin
Dado que se guarda una preferencia del usuario y un aprendizaje del proyecto
Cuando se abre lo guardado
Entonces están en lugares distintos, cada uno con su índice
```

**Cómo validarlo:**

1. Guardar una preferencia del usuario, por ejemplo cómo quiere las respuestas.
2. Guardar un aprendizaje del proyecto, por ejemplo por qué se eligió cierto diseño.
3. Abrir los dos índices. Resultado esperado: cada cosa aparece en el suyo, ninguna en los dos.
- **Aprobado cuando:** no se confunden.

### CA-02 — La preferencia dice por qué se pidió

```gherkin
Dado que se guarda una preferencia del usuario
Cuando se lee después
Entonces dice qué pidió, por qué lo pidió y cómo se aplica
```

**Cómo validarlo:**

1. Abrir una preferencia guardada.
2. Leerla. Resultado esperado: trae las tres cosas.
3. Preguntarse si se puede aplicar sin haber estado en esa conversación. Resultado esperado: sí.
- **Aprobado cuando:** la preferencia se puede cumplir meses después.

### Criterios de aceptación transversales

- [ ] **Límites** — algo que parece de los dos tipos tiene un criterio para decidir.
- [ ] **No regresión** — lo ya guardado no se mezcla al agregar lo nuevo.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Claridad** | Se distingue de un vistazo qué es cada cosa |
| **Trazabilidad** | La preferencia dice de qué conversación salió |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica.
- **Documento funcional:** [documentacion/epicas/EP-006-memoria-de-lo-aprendido/epica.md](../epica.md), §5.1.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Definir el lugar de cada una.
- [ ] Definir la forma de una preferencia: qué se pide, por qué y cómo se aplica.
- [ ] Escribir el criterio para decidir cuando algo parece de los dos tipos.

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
| Dependencia | HU-002, porque las dos se guardan en el repositorio | Alto |
| Riesgo | Que una preferencia se lea como norma del estándar | Está escrito que ninguna reemplaza una regla |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] Las dos cosas se guardan por separado, cada una con su índice
- [ ] La preferencia dice qué, por qué y cómo se aplica
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Parcial | Necesita el lugar de HU-002 |
| **N**egociable | Sí | Dónde vive cada una se puede discutir |
| **V**aliosa | Sí | Evita que una preferencia se confunda con conocimiento |
| **E**stimable | Sí | Alcance corto |
| **S**mall (pequeña) | Sí | Una separación y un formato |
| **T**esteable | Sí | Se prueba guardando una de cada tipo |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
