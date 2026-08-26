# HU-001 — Definir qué se guarda, con qué tipos y qué alcances

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-001 |
| **Épica / Feature** | [EP-006 Memoria de lo aprendido](../epica.md) |
| **Módulo / Componente** | Memoria |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | En curso — CA-01 y CA-02 cumplidos y probados; el transversal de privacidad, no |
---

## 2. Narrativa

- **Como** quien va a guardar algo aprendido
- **Quiero** saber qué merece guardarse, de qué tipo es y a quién le sirve
- **Para** que la memoria no se llene de cosas que nadie va a buscar

---

## 3. Contexto y descripción

Una memoria donde se guarda todo es igual de inútil que una vacía: nadie encuentra nada. Y una donde cada quien guarda con su criterio termina siendo un montón de notas sueltas.

Hacen falta tres decisiones antes de guardar la primera: qué merece guardarse, de qué tipo es lo que se guarda, y a quién le sirve. Ese último punto es el que hace que una lección aprendida en un proyecto aparezca en otro.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Se guarda lo que no se puede recuperar leyendo el código |
| RN-02 | Cada cosa guardada tiene un tipo: decisión tomada, error resuelto, patrón que se repite o aprendizaje |
| RN-03 | Cada cosa guardada tiene un alcance: solo este proyecto, o cualquiera |
| RN-04 | Lo que se guarda se decide al guardarlo, no automáticamente |
| RN-05 | Lo que se guarda dice también por qué, no solo qué |

### 3.2 Supuestos

- Quien cierra una unidad de trabajo sabe distinguir lo que le va a servir a otro proyecto de lo que no.

### 3.3 Fuera de alcance

- Dónde se guarda. Eso es HU-002.
- Cómo se busca. Eso es HU-003 y HU-004.

---

## 4. Criterios de aceptación

### CA-01 — El criterio de qué se guarda está escrito

```gherkin
Dado que se cierra una unidad de trabajo
Cuando hay que decidir si algo merece guardarse
Entonces existe un criterio escrito que responde
```

**Cómo validarlo:**

1. Buscar el documento que define qué se guarda.
2. Leerlo. Resultado esperado: dice qué merece guardarse y qué no, con un ejemplo de cada lado.
3. Aplicarlo a tres casos reales de un trabajo cerrado. Resultado esperado: los tres se resuelven sin discusión.
- **Aprobado cuando:** el criterio decide sin depender de quién lo aplique.

### CA-02 — Cada cosa guardada tiene tipo y alcance

```gherkin
Dado que se guarda algo aprendido
Cuando se abre lo guardado
Entonces dice de qué tipo es y a quién le sirve
```

**Cómo validarlo:**

1. Guardar tres cosas de tipos distintos.
2. Abrirlas. Resultado esperado: cada una declara su tipo y su alcance.
3. Buscar una sin tipo o sin alcance. Resultado esperado: no hay ninguna.
- **Aprobado cuando:** los dos datos son obligatorios, no opcionales.

### Criterios de aceptación transversales

- [ ] **Límites** — está definido qué se hace cuando algo parece de dos tipos a la vez.
- [ ] **Privacidad** — el criterio dice explícitamente que no se guardan datos personales ni claves.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Claridad** | El criterio se aplica sin haber diseñado el método |
| **Estabilidad** | Los tipos son una lista cerrada; agregar uno es una decisión, no un impulso |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica.
- **Documento funcional:** [documentacion/epicas/EP-006-memoria-de-lo-aprendido/epica.md](../epica.md), §5.1.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Escribir el criterio de qué merece guardarse, con ejemplos.
- [ ] Definir la lista de tipos.
- [ ] Definir los alcances y cómo se decide entre ellos.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-006-HU-001-retrodocumentar-que-se-guarda-y-con-que-alcance](A-EP-006-HU-001-retrodocumentar-que-se-guarda-y-con-que-alcance/README.md) | CA-01 y CA-02 | **Ejecutada el 2026-08-17.** Veredicto: [**No cumple**](A-EP-006-HU-001-retrodocumentar-que-se-guarda-y-con-que-alcance/resultado_pruebas.md#6-veredicto-de-la-fase) — los dos CA que cubre quedaron verificados, y los dos transversales de la HU no. Pendiente el commit |
| `B-EP-006-HU-001` — **propuesta, sin abrir** | Los dos transversales: privacidad y límites | Sale del veredicto de la fase A. Abrirla la decide el usuario: el de privacidad toca `13·DOC5`, que es `base/` |

**La fase retro-documentó, y midió.** Los diez tipos y los tres alcances están en producción, con el criterio de qué merece guardarse en `13·DOC5`. La cuenta del 2026-08-17, sobre 237 señales: **siete tipos vivos y tres nunca usados** —`alternativa-descartada`, `supuesto`, `pregunta-abierta`—, y de los tres alcances, `modulo:` tampoco se ha usado nunca. Ninguno se quitó del esquema.

**Lo que la fase dejó abierto**, y que esta HU todavía no cumple:

| Qué | Estado |
|---|---|
| CA-01 y CA-02 | Cumplidos y probados |
| Transversal · **Privacidad** | **No cumple.** `13·DOC5` no dice que no se guarden datos personales ni claves |
| Transversal · Límites | Sin probar: el plan de pruebas no le escribió caso |
| El criterio, aplicado | De 237 señales, **una sola** es de este repositorio. Cuatro decisiones de fases cerradas eran señal y ninguna se guardó |

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
| Dependencia | Ninguna: es la primera de la épica | Bajo |
| Riesgo | Que el criterio sea tan amplio que se guarde todo | Se escribe con ejemplos de lo que no se guarda |
| Riesgo | Que los tipos se multipliquen | La lista es cerrada |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] El criterio de qué se guarda está escrito
- [ ] Los tipos y los alcances están definidos
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | Es una definición previa a todo lo demás |
| **N**egociable | Sí | Los tipos se pueden discutir |
| **V**aliosa | Sí | Evita que la memoria se vuelva un depósito |
| **E**stimable | Sí | Es un documento |
| **S**mall (pequeña) | Sí | Alcance corto |
| **T**esteable | Sí | Se prueba aplicándolo a casos reales |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
| 2026-08-17 | Ing. José Dúmar Jiménez Ruíz | Se ejecuta la fase A. CA-01 y CA-02 verificados; el transversal de privacidad queda en «No» y el de límites sin probar. Medición: 7 tipos vivos de 10, y 1 señal de este repositorio en 237 |
