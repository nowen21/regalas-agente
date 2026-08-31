# HU-037 — La norma de redacción del agente vive en el cuerpo de reglas

> Historia de usuario del estándar. Nace del [pendiente 93](../../../../pendientes/93-la-norma-de-redaccion-vive-dentro-de-dos-plantillas.md), aprobado por el usuario el 2026-08-30.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-037 |
| **Épica / Feature** | [EP-001 — Cuerpo de reglas heredable](../epica.md) |
| **Módulo / Componente** | Cuerpo de reglas |
| **Tipo** | Técnica |
| **Prioridad** | Should |
| **Estimación** | 3 puntos |
| **Sprint** | Sin asignar |
| **Solicitante** | El usuario |
| **Responsable** | El agente |
| **Estado** | Terminada — la regla `00·ID10` existe y rige todo lo que el agente entrega, incluido el chat |

---

## 2. Narrativa

**Como** agente que entrega documentos en cualquier proyecto
**quiero** una regla del cuerpo de reglas que fije variedad del idioma, persona y forma verbal
**para** que la exigencia no dependa de qué plantilla se esté llenando.

---

## 3. Contexto y descripción

El usuario pidió que un documento se redactara en español colombiano, en tercera persona y en infinitivo. **No hubo regla del cuerpo de reglas que citar.**

Esa exigencia solo está escrita dentro de dos plantillas, como su regla 11: la del manual de usuario y la del manual de instalación. Dice, palabra por palabra, que las acciones van en infinitivo, las explicaciones en tercera persona, y que el impersonal con «se» no sirve para las acciones.

**El estándar ya sabe que le falta.** El anexo de marcas de generación automática lo dice en su cierre: la norma del idioma «necesita su propia regla, y todavía no existe».

### 3.1 Reglas de negocio

- La variedad del idioma sale del proyecto, no se fija en uno solo: ya hay una regla que dice que se habla el idioma del proyecto, y esta la concreta.
- Una norma que rige lo que el agente entrega no puede vivir dentro de un documento modelo: ahí solo la hereda quien llene ese modelo.
- Al cerrarse, las dos plantillas citan la regla en vez de repetirla.

### 3.2 Supuestos

- La regla se escribe por el procedimiento del capítulo de meta-reglas, con su checklist aplicado y su versión.
- Lo que hoy dicen las dos plantillas es correcto: lo que cambia es dónde vive.

### 3.3 Fuera de alcance

- **La ortografía y la gramática.** El anexo las nombra como pendientes suyas y son otra regla: una cosa es cómo se conjuga y otra si el texto está bien escrito.
- El texto que ve el usuario final de un producto, que ya tiene su regla.

---

## 4. Criterios de aceptación

### CA-01 — La regla existe, con su identificador y su checklist

```gherkin
Dado que la norma de redacción no está en el cuerpo de reglas
Cuando se escribe la regla por el procedimiento del capítulo de meta-reglas
Entonces existe con su identificador, su ejemplo y su checklist aplicado
Y el validador de meta-reglas no reclama nada
```

**Cómo validarlo:**
1. Abrir el capítulo donde quedó la regla y leer su cuerpo → resultado esperado: una sola exigencia, con su ejemplo de lo incorrecto y lo correcto.
2. Correr `python validadores/validar.py metareglas` → resultado esperado: sin incumplimientos.
3. Comprobar que aparece clasificada en el registro de reglas comprobables, diciendo qué mitad no lo es.
- **Aprobado cuando:** la regla está escrita, clasificada y el validador la acepta.

### CA-02 — Las dos plantillas la citan en vez de repetirla

```gherkin
Dado que la norma estaba escrita dentro de dos plantillas
Cuando la regla existe en el cuerpo de reglas
Entonces las dos plantillas la citan con su enlace
Y ninguna repite su texto
```

**Cómo validarlo:**
1. Buscar en las dos plantillas el texto de la regla 11 → resultado esperado: ya no está el texto completo.
2. Comprobar que en su lugar hay una cita con enlace a la regla nueva.
3. Correr el validador de coherencia → resultado esperado: el enlace resuelve.
- **Aprobado cuando:** la norma está en un solo sitio y las plantillas apuntan a él.

### CA-03 — La regla dice el idioma del proyecto, no uno fijo

```gherkin
Dado un proyecto que no trabaja en español
Cuando se aplica la regla
Entonces exige la variedad del idioma que ese proyecto declara
Y no exige español colombiano
```

**Cómo validarlo:**
1. Leer el cuerpo de la regla → resultado esperado: nombra el idioma del proyecto, no uno concreto.
2. Comprobar que se sostiene sobre la regla que ya fija el idioma del proyecto.
- **Aprobado cuando:** la regla sirve a un proyecto en cualquier idioma.

### Criterios de aceptación transversales

- [x] **No regresión** — el validador de meta-reglas y el de coherencia quedan sin fallas.
- [x] **Trazabilidad** — la regla queda clasificada, diciendo qué se puede comprobar con un programa y qué no.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Trazabilidad** | La regla nueva se versiona y se registra, como cualquier cambio del cuerpo de reglas |
| RNF-02 | **Compatibilidad** | Un proyecto que ya tenga documentos escritos no queda obligado a reescribirlos: la regla rige lo que se entrega de aquí en adelante |

---

## 6. Diseño y referencias

- **Documento funcional:** el [pendiente 93](../../../../pendientes/93-la-norma-de-redaccion-vive-dentro-de-dos-plantillas.md).
- **Documentos afectados:** el capítulo donde quede la regla, las dos plantillas de manual, y el registro de reglas comprobables.

---

## 7. Tareas técnicas derivadas

- [ ] Decidir el alcance con el usuario: si rige para todo documento o solo para los que lee alguien de fuera del oficio
- [ ] Escribir la regla, con su checklist aplicado
- [ ] Clasificarla en el registro de comprobables
- [ ] Cambiar las dos plantillas para que la citen
- [ ] Versionar y registrar el cambio
- [ ] Cerrar el pendiente 93

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados.

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| [`A-EP-001-HU-037-la-norma-sube-al-cuerpo-de-reglas`](A-EP-001-HU-037-la-norma-sube-al-cuerpo-de-reglas/) | CA-01 a CA-03 | — | [plan_trabajo](A-EP-001-HU-037-la-norma-sube-al-cuerpo-de-reglas/plan_trabajo.md) | [plan_pruebas](A-EP-001-HU-037-la-norma-sube-al-cuerpo-de-reglas/plan_pruebas.md) | [resultado](A-EP-001-HU-037-la-norma-sube-al-cuerpo-de-reglas/resultado_pruebas.md) · cumple | Terminada |

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
| Dependencia | La decisión de alcance es del usuario y bloquea la redacción | Alto |
| Riesgo | Que la regla quede fijada a un idioma y no sirva a otros proyectos | El CA-03 lo comprueba |
| Riesgo | Que se escriba como norma de estilo y termine siendo discutible en cada documento | Se escribe con una sola exigencia y su ejemplo, como cualquier regla |

---

## 10. Definition of Ready (DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Diseño / mockup disponible: no aplica, no hay interfaz
- [x] Dependencias identificadas y desbloqueadas
- [ ] Estimada por el equipo
- [x] Cumple criterios INVEST

## 11. Definition of Done (DoD)

- [ ] Código implementado y en rama principal
- [ ] Pruebas unitarias e integración pasando
- [ ] Code review aprobado
- [ ] Todos los criterios de aceptación verificados
- [ ] Requisitos no funcionales validados
- [ ] Documentación técnica actualizada
- [ ] Desplegada: no aplica, no hay ambiente
- [ ] Aceptada por el usuario

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | ☑ | Depende de una decisión del usuario, no de otra historia |
| **N**egociable | ☑ | El alcance es justamente lo que se negocia |
| **V**aliosa | ☑ | Hoy la convención se copia a mano de una plantilla, y lo copiado a mano se copia distinto |
| **E**stimable | ☑ | Una regla, dos plantillas y un registro |
| **S**mall (pequeña) | ☑ | Una fase |
| **T**esteable | ☑ | Los tres criterios se comprueban leyendo y corriendo dos validadores |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-30 | El agente | Se crea la historia a partir del pendiente 93, aprobado por el usuario |
