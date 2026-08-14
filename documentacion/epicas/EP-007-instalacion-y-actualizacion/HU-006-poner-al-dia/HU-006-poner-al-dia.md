# HU-006 — Poner al día lo ya instalado

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-006 |
| **Épica / Feature** | [EP-007 Instalación y actualización](../epica.md) |
| **Módulo / Componente** | Instalador |
| **Tipo** | Técnica |
| **Prioridad** | Should |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Backlog |

---

## 2. Narrativa

- **Como** quien instaló el estándar hace meses
- **Quiero** poner al día lo instalado con la misma línea
- **Para** no quedarme con una copia vieja y un aviso que termino ignorando

---

## 3. Contexto y descripción

La mitad que suele olvidarse no es instalar: es mantener al día. Un proyecto con una copia vieja y un aviso permanente termina ignorando el aviso, y a partir de ahí el estándar deja de servirle.

Actualizar tiene que ser el mismo movimiento que instalar, y tiene que saber qué quedó viejo de verdad. No basta con comparar fechas: una copia se ve más nueva por cualquier edición local.

Lo que sí dice la verdad es la huella del documento del que salió cada copia. Si el original cambió, la huella deja de coincidir, y eso no depende de fechas ni de quién editó qué.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | La misma línea que instala pone al día |
| RN-02 | Se detecta lo viejo comparando contra el documento del que salió cada copia, no por fecha |
| RN-03 | Lo que ya está al día no se toca |
| RN-04 | Cada actualización deja un registro de qué cambió y desde cuándo |
| RN-05 | Subir la versión adoptada del estándar sigue siendo decisión de la persona |

### 3.2 Supuestos

- Cada documento heredado puede llevar la marca del original del que salió.

### 3.3 Fuera de alcance

- Migrar el trabajo del proyecto a reglas nuevas. El aviso de desfase es de EP-002.
- Actualizar varios proyectos a la vez.

---

## 4. Criterios de aceptación

### CA-01 — Lo viejo se detecta y se pone al día

```gherkin
Dado que un documento del estándar cambió
Cuando se corre la actualización en un proyecto que lo tenía
Entonces ese componente se detecta como viejo y queda al día
```

**Cómo validarlo:**

1. Cambiar un documento modelo en el estándar.
2. Correr la actualización en un proyecto ya instalado. Resultado esperado: reporta ese componente como viejo y lo actualiza.
3. Volver a correr. Resultado esperado: ya no lo reporta.
- **Aprobado cuando:** la detección no depende de fechas.

### CA-02 — Queda registro de qué se actualizó

```gherkin
Dado que se puso al día un proyecto
Cuando se mira el registro de actualizaciones
Entonces dice qué componentes cambiaron y desde cuándo
```

**Cómo validarlo:**

1. Actualizar el proyecto de prueba.
2. Abrir el registro. Resultado esperado: hay una entrada con la fecha y los componentes actualizados.
3. Actualizar otra vez sin cambios. Resultado esperado: no se agrega una entrada vacía.
- **Aprobado cuando:** se puede reconstruir desde cuándo el proyecto usa cada versión.

### Criterios de aceptación transversales

- [ ] **No regresión** — actualizar no pierde lo escrito por la persona.
- [ ] **Límites** — un proyecto que nunca se instaló se instala, no falla.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Determinismo** | La detección de lo viejo no depende de fechas ni de la máquina |
| **Trazabilidad** | Cada actualización queda registrada |
| **Simplicidad** | Es la misma línea que instala |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica.
- **Documento funcional:** [documentacion/epicas/EP-007-instalacion-y-actualizacion/epica.md](../epica.md), criterio CAE-04.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Marcar cada copia con la huella del documento del que salió.
- [ ] Comparar la huella para detectar lo viejo.
- [ ] Escribir el registro de cada actualización.

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
| Dependencia | HU-001 y HU-005, porque actualiza sin pisar lo escrito | Alto |
| Dependencia | EP-002, porque el aviso de desfase de versión viene de ahí | Medio |
| Riesgo | Que el aviso de desactualización se vuelva permanente y se ignore | Actualizar es una línea, así que apagarlo cuesta menos que ignorarlo |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] Lo viejo se detecta por huella y se pone al día
- [ ] Queda registro de cada actualización
- [ ] Lo escrito por la persona no se pierde
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | No | Se apoya en el instalador |
| **N**egociable | Sí | Qué queda en el registro se puede discutir |
| **V**aliosa | Sí | Evita el proyecto que se queda viejo para siempre |
| **E**stimable | Sí | Alcance acotado |
| **S**mall (pequeña) | Sí | Comparar huellas y registrar |
| **T**esteable | Sí | Se prueba cambiando un modelo del estándar |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
