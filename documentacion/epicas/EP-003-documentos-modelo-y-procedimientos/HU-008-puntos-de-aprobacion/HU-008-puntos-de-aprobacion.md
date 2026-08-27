# HU-008 — Declarar los puntos donde aprueba una persona

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-008 |
| **Épica / Feature** | [EP-003 Documentos modelo y procedimientos guiados](../epica.md) |
| **Módulo / Componente** | Procedimientos guiados |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Terminada |
---

## 2. Narrativa

- **Como** quien responde por el trabajo
- **Quiero** que esté escrito en qué momentos me toca aprobar
- **Para** que nadie avance en mi nombre y yo sepa cuándo me van a preguntar

---

## 3. Contexto y descripción

Hay decisiones que no son de la IA: qué se va a construir, qué alcance tiene, si el plan se acepta, si se sube el trabajo. Si esos momentos no están escritos, terminan resolviéndose solos, casi siempre porque alguien interpretó un "listo" como una aprobación.

Esta historia los deja escritos: cuáles son, qué se aprueba en cada uno y qué cuenta como aprobación. Es corta a propósito. Su valor no está en el tamaño sino en que exista una lista que se pueda señalar.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Los puntos donde aprueba una persona están escritos en una lista |
| RN-02 | Cada punto dice qué se aprueba y qué queda habilitado al aprobarlo |
| RN-03 | Solo la persona aprueba: la IA propone y espera |
| RN-04 | Aprobar el contenido no es aprobar el paso siguiente; cada permiso se pide aparte |
| RN-05 | Una respuesta ambigua no cuenta como aprobación |
| RN-06 | Queda escrito quién aprobó y cuándo |

### 3.2 Supuestos

- Quien aprueba está disponible en la sesión, o el trabajo espera. Esperar es válido.

### 3.3 Fuera de alcance

- El procedimiento que se detiene en esos puntos. Eso es HU-007.
- Los permisos técnicos sobre el sistema. Esto es aprobación de trabajo, no de accesos.

---

## 4. Criterios de aceptación

### CA-01 — La lista existe y dice qué se aprueba en cada punto

```gherkin
Dado que el trabajo tiene momentos donde una persona decide
Cuando se busca la lista de esos momentos
Entonces existe
Y cada punto dice qué se aprueba y qué habilita
```

**Cómo validarlo:**

1. Buscar el documento que lista los puntos de aprobación.
2. Leerlo. Resultado esperado: cada punto nombra qué se aprueba y qué queda habilitado.
3. Comparar con el procedimiento que dirige. Resultado esperado: los puntos coinciden, no hay uno que exista solo en un lado.
- **Aprobado cuando:** la lista y el procedimiento dicen lo mismo.

### CA-02 — Una respuesta ambigua no habilita

```gherkin
Dado que la IA pide una aprobación
Cuando la respuesta no es una aprobación clara
Entonces el trabajo no avanza
```

**Cómo validarlo:**

1. Llevar un trabajo de prueba hasta un punto de aprobación.
2. Responder con algo ambiguo, por ejemplo un comentario sobre otra cosa. Resultado esperado: no avanza y vuelve a pedirla.
3. Responder con una aprobación clara. Resultado esperado: avanza.
- **Aprobado cuando:** avanzar exige una respuesta explícita.

### CA-03 — Aprobar una cosa no aprueba la siguiente

```gherkin
Dado que una persona aprobó el contenido de un documento
Cuando llega el momento de subir el trabajo
Entonces se pide esa aprobación aparte
```

**Cómo validarlo:**

1. Aprobar el contenido de un plan de prueba.
2. Observar qué pasa al llegar al momento de guardar el trabajo en el repositorio. Resultado esperado: se pide una aprobación nueva.
3. Revisar el registro. Resultado esperado: quedan las dos aprobaciones, por separado.
- **Aprobado cuando:** ninguna aprobación se estira para cubrir otra cosa.

### Criterios de aceptación transversales

- [ ] **Auditoría** — queda escrito quién aprobó, qué y cuándo.
- [ ] **Límites** — está definido qué pasa cuando quien aprueba no está: el trabajo espera, no avanza solo.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Claridad** | La lista se lee de una vez y se puede señalar en una discusión |
| **Trazabilidad** | Cada aprobación queda registrada |
| **Prudencia** | Ante la duda, no se avanza |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica, es un documento de texto.
- **Documento funcional:** [documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/epica.md](../epica.md), criterio CAE-04 y §5.4 fila 14.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Listar los puntos de aprobación y qué se aprueba en cada uno.
- [ ] Escribir qué cuenta como aprobación y qué no.
- [ ] Definir dónde queda registrada cada aprobación.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
**Ejecutada el 2026-08-22.** Veredicto: [**Cumple**](A-EP-003-HU-008-retrodocumentar-los-puntos-de-aprobacion/resultado_pruebas.md) — la lista sí llega a los proyectos: está en el molde del estado de fase |

**Mitad retro-documentación, mitad construcción.** Los puntos existen y las reglas que los sostienen también. Lo que falta es la lista: hoy vive dentro de un procedimiento y no en `base/`, así que un proyecto que hereda no la recibe.

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
| Dependencia | EP-001, porque la conducta de no decidir por la persona es una regla | Alto |
| Riesgo | Que se interprete cualquier respuesta como aprobación | Está escrito qué cuenta y qué no |
| Riesgo | Que los puntos se multipliquen y el trabajo se trabe | Solo son puntos de aprobación las decisiones que no son de la IA |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] La lista de puntos existe y coincide con el procedimiento que dirige
- [ ] Está escrito qué cuenta como aprobación
- [ ] Cada aprobación queda registrada
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | La lista se puede escribir antes que los procedimientos |
| **N**egociable | Sí | Cuáles son los puntos se puede discutir |
| **V**aliosa | Sí | Evita que se avance en nombre de quien responde |
| **E**stimable | Sí | Alcance corto |
| **S**mall (pequeña) | Sí | Una lista y su criterio |
| **T**esteable | Sí | Se prueba respondiendo ambiguo a propósito |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
