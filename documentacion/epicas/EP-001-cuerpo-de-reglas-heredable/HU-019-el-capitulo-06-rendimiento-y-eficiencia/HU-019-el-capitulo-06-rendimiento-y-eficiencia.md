# HU-019 — El capítulo `06` · Rendimiento y eficiencia: su texto tiene dueña

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-019 |
| **Épica** | [EP-001 — Cuerpo de reglas heredable y en capas](../epica.md) |
| **Módulo / Componente** | Capítulo `06` · Rendimiento y eficiencia |
| **Tipo** | Técnica |
| **Prioridad** | Should |
| **Estimación** | S |
| **Solicitante** | Quien define el estándar (pendiente 60, salida «una historia por capítulo», decidida por el usuario el 2026-08-22) |
| **Estado** | Pendiente |
## 2. Narrativa

- **Como** quien mantiene el estándar
- **Quiero** que el texto del capítulo `06` tenga una historia de usuario dueña, que diga de dónde baja cada una de sus reglas y reciba todo cambio de su texto
- **Para** que un cambio del capítulo tenga dónde bajarse por la cadena (`02·F23`) y la pregunta «¿de dónde salió esta regla?» tenga respuesta

## 3. Contexto y descripción

El capítulo [`06 · Rendimiento y eficiencia`](../../../../base/06-rendimiento.md) tiene hoy **6 regla(s)** y, hasta esta historia, ninguna historia de usuario declaraba su texto como módulo: se escribió sin recorrer la cadena que él mismo exige. Lo midió el [pendiente 60](../../../../pendientes/hecho/cada-capitulo-tiene-su-historia.md): 19 de 21 capítulos estaban así, y el usuario decidió una historia por capítulo.

Esta historia es la dueña del **texto** del capítulo. No de su comprobación (eso vive en EP-004) ni de su disparo (EP-005): de lo que el capítulo dice.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Todo cambio del texto del capítulo `06` entra como fase de esta historia (`02·F23`) |
| RN-02 | Toda regla nueva del capítulo nace por el procedimiento del `20` y cita esta historia como su origen |
| RN-03 | El capítulo declara su historia dueña en su cabecera, para que se lea desde el capítulo mismo |

### 3.2 Supuestos

- El capítulo existe y se usa: esta historia lo retrodocumenta; no lo reescribe.

### 3.3 Fuera de alcance

- Arreglar las reglas del capítulo que reprueban su checklist: eso es el pendiente 19 y sus fases en HU-009.
- La comprobación automática de las reglas del capítulo (EP-004).

## 4. Criterios de aceptación

### CA-01 — El capítulo nombra su historia dueña

```gherkin
Dado que el capítulo 06 existe
Cuando alguien abre su cabecera
Entonces encuentra la historia de usuario dueña de su texto, enlazada
```

**Cómo validarlo:**

1. Abrir [`base/06-rendimiento.md`](../../../../base/06-rendimiento.md). Resultado esperado: bajo el título hay una línea «Historia dueña del texto» que enlaza a esta historia.
- **Aprobado cuando:** la línea existe y el enlace resuelve.

### CA-02 — Un cambio del capítulo tiene dónde bajarse

```gherkin
Dado que hay que cambiar el texto de una regla del capítulo 06
Cuando se baja el cambio por la cadena
Entonces la fase nace bajo esta historia y su plan declara qué reglas toca
```

**Cómo validarlo:**

1. Levantar con el andamio una fase de esta historia para un cambio cualquiera del capítulo (simulado). Resultado esperado: la fase se crea bajo `HU-019-el-capitulo-06-rendimiento-y-eficiencia/`.
- **Aprobado cuando:** la cadena tiene un eslabón para el capítulo, que antes no tenía.

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| Trazabilidad | Se puede nombrar, para el capítulo `06`, la historia donde se escribe su texto |

## 6. Tareas técnicas derivadas

- [x] Declarar la historia dueña en la cabecera del capítulo (hecho al crear esta historia).
- [ ] Retrodocumentar el capítulo en una fase: de dónde baja cada regla.

## 7. Fases que la implementan

| Fase | Qué CA cubre | Estado |
|---|---|---|
| (ninguna todavía) | | La primera fase será la retrodocumentación del capítulo |

## 8. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-007 (el procedimiento de la regla) y HU-009 (checklists al día) | Medio |
| Riesgo | Que la historia quede como cascarón sin fase | Bajo: el inventario de HU (pendiente 48) la cuenta como incompleta hasta que la tenga |

## 9. Definition of Ready

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y verificables
- [x] Dependencias identificadas

## 10. Definition of Done

- [x] El capítulo declara su dueña
- [ ] Fase de retrodocumentación cerrada

## 11. Validación INVEST

| Criterio | Cumple | Observación |
|---|:--:|---|
| Independiente | Sí | Un capítulo, una historia |
| Negociable | Sí | Qué entra en la retrodocumentación se discute en su fase |
| Valiosa | Sí | Cierra la trazabilidad hacia arriba de 6 regla(s) |
| Estimable | Sí | Una fase de retrodocumentación |
| Pequeña | Sí | |
| Testeable | Sí | La línea en la cabecera y la fase que nace bajo ella |

## 12. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-22 | El agente, por decisión del usuario (pendiente 60, salida a) | Creación: una historia por capítulo |
