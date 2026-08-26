# HU-010 — Cuándo no aplica la exigencia de especificación

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-010 |
| **Épica / Feature** | [EP-001 Cuerpo de reglas heredable y en capas](../epica.md) |
| **Módulo / Componente** | Cuerpo de reglas |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Done |

---

## 2. Narrativa

- **Como** quien abre una fase cuyo entregable no es código
- **Quiero** saber si necesita especificación aparte
- **Para** no incumplir la regla ni escribir un documento que repite la historia de usuario

---

## 3. Contexto y descripción

La regla que exige especificación acordada antes de tocar código está escrita dando por hecho que lo que se construye es el código de un módulo.

Dos fases seguidas de este repositorio se abrieron declarando que no la tienen, y con buenos motivos: una entrega texto normativo y la otra programas cortos cuya especificación son los criterios de aceptación de su historia. En los dos casos, un documento aparte diría lo mismo que la historia.

Una regla que se incumple dos veces seguidas con buenos motivos se vuelve costumbre incumplirla, y la próxima vez nadie va a saber si el caso era legítimo o si se saltó el paso.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Queda escrito cuándo la exigencia de especificación no aplica |
| RN-02 | Si es una excepción, trae sus tres partes: condición, límite y quién la autoriza |
| RN-03 | El caso en que la historia de usuario hace de especificación queda dicho en la propia regla |
| RN-04 | El cambio pasa por el procedimiento completo del capítulo de meta-reglas |
| RN-05 | Lo que se decida vale hacia adelante: las fases ya cerradas no se reabren |

### 3.2 Supuestos

- El caso se repite: el estándar se construye a sí mismo, y ahí el entregable casi nunca es código de un módulo.

### 3.3 Fuera de alcance

- Cambiar qué exige la regla cuando sí se construye código.
- Revisar las fases ya cerradas.

---

## 4. Criterios de aceptación

### CA-01 — La regla dice cuándo no aplica

```gherkin
Dado que se va a abrir una fase cuyo entregable no es código de un módulo
Cuando se lee la regla que exige especificación
Entonces dice si ese caso está cubierto y con qué condición
```

**Cómo validarlo:**

1. Abrir la regla.
2. Buscar el caso del entregable que no es código. Resultado esperado: está escrito, con condición, límite y quién autoriza, o dice que la historia hace de especificación.
3. Preguntarle a alguien que no participó de la decisión si su fase necesita especificación. Resultado esperado: responde leyendo solo la regla.
- **Aprobado cuando:** el caso deja de resolverse por criterio de cada sesión.

### CA-02 — Las dos fases abiertas quedan resueltas

```gherkin
Dado que hay dos fases que declararon no tener especificación
Cuando se aplica lo que la regla ahora dice
Entonces las dos quedan conformes o se les escribe lo que falta
```

**Cómo validarlo:**

1. Abrir el plan de las dos fases y leer su casilla de especificación.
2. Contrastarla con la regla nueva. Resultado esperado: o quedan cubiertas por lo escrito, o se ve qué les falta.
3. Correr la comprobación del plan. Resultado esperado: no reporta que falte la especificación en un caso que la regla exime.
- **Aprobado cuando:** ninguna fase queda en el limbo.

### Criterios de aceptación transversales

- [ ] **No regresión** — la exigencia sigue en pie para el código de un módulo.
- [ ] **Límites** — está definido qué pasa cuando la fase mezcla las dos cosas.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Claridad** | Quien abre la fase decide leyendo solo la regla |
| **Trazabilidad** | El cambio queda versionado y con su checklist |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica.
- **Documento funcional:** el pendiente 20, que registró el caso, y los planes de las dos fases.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Decidir entre escribir la excepción o declarar que la historia hace de especificación.
- [ ] Escribirlo en la regla, con el procedimiento completo.
- [ ] Ajustar la comprobación del plan si el caso queda eximido.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-001-HU-010-cuando-la-historia-hace-de-especificacion](A-EP-001-HU-010-cuando-la-historia-hace-de-especificacion/README.md) | CA-01 y CA-02 | Abierta 2026-08-17, con su plan de trabajo escrito y sin aprobar |

**La fase construye: acá no hay nada que retro-documentar.** Y trae una corrección al CA-02: las fases abiertas sin especificación aparte **ya no son dos**. Contadas el 2026-08-17 son diecisiete — nueve que se apoyan en su historia de usuario y ocho que declararon la deuda.

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
| Dependencia | EP-003, porque el modelo de especificación define qué documento se estaría eximiendo | Medio |
| Riesgo | Que la excepción se estire y termine tapando el caso normal | Se escribe con límite explícito y con quién autoriza |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] La regla dice cuándo no aplica
- [ ] Las dos fases abiertas quedan resueltas
- [ ] El cambio está versionado y con checklist
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | Se puede escribir sin nada más |
| **N**egociable | Sí | Excepción o aclaración, se discute |
| **V**aliosa | Sí | Evita que incumplir se vuelva costumbre |
| **E**stimable | Sí | Es una regla |
| **S**mall (pequeña) | Sí | Alcance corto |
| **T**esteable | Sí | Se prueba contra las dos fases que lo destaparon |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde el hallazgo H-7 del 2026-08-14 |
