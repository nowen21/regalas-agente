# HU-007 — Escribir el procedimiento que dirige a los demás y controla los cortes

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-007 |
| **Épica / Feature** | [EP-003 Documentos modelo y procedimientos guiados](../epica.md) |
| **Módulo / Componente** | Procedimientos guiados |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | L |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Pendiente |
---

## 2. Narrativa

- **Como** quien encarga un trabajo completo
- **Quiero** un procedimiento que llame a los demás en orden y no deje saltar pasos
- **Para** no tener que acordarme yo de cuál sigue ni de qué falta

---

## 3. Contexto y descripción

Tener un procedimiento por rol no alcanza. Alguien tiene que decidir cuál va ahora, comprobar que el anterior terminó y detenerse donde una persona debe aprobar.

Si esa decisión la toma quien va pidiendo cosas en el chat, los pasos se saltan sin querer: se pide el plan antes de la especificación, o se empieza a construir sin que nadie haya aprobado el alcance.

Este procedimiento es el que dirige. También es el que guarda dónde quedó todo, porque una conversación larga se corta y lo que no está escrito se pierde.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Hay un procedimiento que llama a los demás en el orden acordado |
| RN-02 | No pasa al siguiente paso sin la salida del anterior |
| RN-03 | Se detiene en cada punto donde una persona debe aprobar, y espera |
| RN-04 | Deja escrito en qué paso va, para poder retomar en otra sesión |
| RN-05 | Si un paso queda a medias, dice cuál y qué falta |
| RN-06 | No decide por la persona ni asume una aprobación que no recibió |

### 3.2 Supuestos

- Una sesión de trabajo se puede cortar en cualquier momento, así que el estado se guarda en el repositorio y no en la conversación.

### 3.3 Fuera de alcance

- Los procedimientos de cada rol. Eso es HU-006.
- La lista de puntos de aprobación. Eso es HU-008.
- Que arranque solo al abrir la sesión. Eso es EP-005.

---

## 4. Criterios de aceptación

### CA-01 — Llama a los procedimientos en orden

```gherkin
Dado que se encarga un trabajo completo
Cuando se ejecuta el procedimiento que dirige
Entonces llama a los demás en el orden acordado
Y no arranca uno sin la salida del anterior
```

**Cómo validarlo:**

1. Encargar un trabajo de prueba desde cero.
2. Seguir qué procedimientos se ejecutan. Resultado esperado: van en el orden declarado.
3. Intentar pedir el paso de construir antes del plan. Resultado esperado: se niega y dice qué falta.
- **Aprobado cuando:** el orden no depende de cómo se pida.

### CA-02 — Se detiene donde aprueba una persona

```gherkin
Dado que el trabajo llega a un punto donde una persona debe aprobar
Cuando el procedimiento llega ahí
Entonces se detiene y lo pide
Y no continúa hasta recibir la respuesta
```

**Cómo validarlo:**

1. Llevar el trabajo de prueba hasta el punto donde se aprueba el alcance.
2. Observar. Resultado esperado: pide la aprobación y espera.
3. Responder algo que no sea una aprobación clara. Resultado esperado: no sigue.
4. Aprobar. Resultado esperado: sigue.
- **Aprobado cuando:** ninguna aprobación se da por supuesta.

### CA-03 — El trabajo se retoma en otra sesión sin perder el hilo

```gherkin
Dado que una sesión se cortó a mitad del trabajo
Cuando se abre una sesión nueva
Entonces se puede saber en qué paso quedó y qué falta
```

**Cómo validarlo:**

1. Cortar el trabajo de prueba en la mitad.
2. Abrir una sesión nueva y ejecutar el procedimiento que dirige. Resultado esperado: lee dónde quedó y lo dice.
3. Continuar. Resultado esperado: sigue desde ahí, sin repetir lo hecho.
- **Aprobado cuando:** retomar no exige releer la conversación anterior.

### Criterios de aceptación transversales

- [ ] **Límites** — un trabajo que ya venía empezado sin este procedimiento tiene un camino para engancharse.
- [ ] **Errores** — si un paso falla, dice cuál y qué falta, y no continúa como si nada.
- [ ] **Auditoría** — queda escrito qué se decidió en cada paso y quién aprobó.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Persistencia** | El estado sobrevive al corte de la sesión |
| **Claridad** | En cualquier momento se puede decir en qué paso va el trabajo |
| **Autonomía** | No depende de que alguien recuerde el orden |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica, es un documento de texto.
- **Documento funcional:** [documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/epica.md](../epica.md), criterio CAE-03.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Definir el orden de los pasos y qué comprueba antes de pasar al siguiente.
- [ ] Definir dónde se guarda en qué paso va el trabajo.
- [ ] Escribir qué hace cuando un paso queda a medias.
- [ ] Escribir cómo se engancha un trabajo que ya venía empezado.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
**Ejecutada el 2026-08-22.** Veredicto: [**Cumple**](A-EP-003-HU-007-retrodocumentar-el-procedimiento-que-dirige/resultado_pruebas.md) — probada sobre tres sesiones y cinco días de distancia |

**La fase retro-documenta.** El director existe, con sus trece estaciones y sus puertas. El CA-03 —retomar en otra sesión sin perder el hilo— es el que más ha fallado en la práctica, y la fase lo prueba con el resultado que dé.

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
| Dependencia | HU-006, porque dirige a esos procedimientos | Alto |
| Dependencia | HU-008, porque los cortes son los puntos de aprobación | Alto |
| Riesgo | Que el estado se guarde solo en la conversación y se pierda | Se guarda en un documento del repositorio |
| Riesgo | Que se vuelva tan rígido que estorbe en trabajos chicos | Se declara qué pasos aplican según el tamaño del encargo |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] El procedimiento existe y llama a los demás en orden
- [ ] Se detiene en los puntos de aprobación
- [ ] El estado del trabajo sobrevive al corte de la sesión
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | No | Necesita los procedimientos de HU-006 |
| **N**egociable | Sí | El orden y los cortes se pueden discutir |
| **V**aliosa | Sí | Es lo que impide saltarse pasos sin querer |
| **E**stimable | Sí | El alcance lo fija la lista de pasos |
| **S**mall (pequeña) | No | Coordina a todos los demás |
| **T**esteable | Sí | Se prueba llevando un trabajo de punta a punta y cortándolo a la mitad |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
