# HU-004 — Avisar al abrir sesión cuando el proyecto quedó atrás

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-004 |
| **Épica / Feature** | [EP-002 Versionado de las reglas y adopción por proyecto](../epica.md) |
| **Módulo / Componente** | Versionado del estándar |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Terminada — el CA-01 se volvió a medir y hoy cumple, en la fase `C` |
---

## 2. Narrativa

- **Como** quien abre una sesión de trabajo en un proyecto
- **Quiero** que me avisen ahí mismo si el proyecto quedó atrás y qué cambió
- **Para** enterarme cuando todavía puedo decidir, y no meses después

---

## 3. Contexto y descripción

Un aviso que hay que ir a buscar no existe. Si para saber que el proyecto quedó atrás hay que acordarse de correr algo, nadie se entera.

El momento en que sirve es al abrir la sesión, antes de empezar a trabajar. Y tiene que decir dos cosas: cuánto atrás quedó y qué cambió, porque con solo el número nadie decide.

Avisar no es migrar. El aviso informa; adoptar la versión nueva sigue siendo decisión de la persona.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | El aviso aparece al abrir la sesión, sin que nadie lo pida |
| RN-02 | Dice qué versión sigue el proyecto, cuál es la vigente y qué cambió entre las dos |
| RN-03 | No migra nada: informar y decidir son cosas distintas |
| RN-04 | Un proyecto al día no recibe aviso: el silencio es la señal de que está al día |
| RN-05 | El aviso no detiene el trabajo |

### 3.2 Supuestos

- Quien abre la sesión puede decidir si adopta, o sabe a quién preguntarle.

### 3.3 Fuera de alcance

- Aplicar la actualización. Eso es EP-007.
- El disparo automático en sí, que es la mecánica de EP-005; aquí se define qué se avisa y cuándo.

---

## 4. Criterios de aceptación

### CA-01 — El proyecto atrasado recibe el aviso al abrir sesión

```gherkin
Dado que el proyecto declara una versión anterior a la vigente
Cuando se abre una sesión de trabajo
Entonces aparece el aviso sin que nadie lo pida
Y dice qué cambió desde la versión que sigue
```

**Cómo validarlo:**

1. En un proyecto de prueba, declarar una versión anterior a la vigente.
2. Abrir una sesión. Resultado esperado: el aviso aparece en el primer mensaje.
3. Leerlo. Resultado esperado: nombra las dos versiones y resume qué cambió.
- **Aprobado cuando:** el aviso aparece solo y alcanza para decidir.

### CA-02 — El proyecto al día no recibe nada

```gherkin
Dado que el proyecto declara la versión vigente
Cuando se abre una sesión
Entonces no aparece ningún aviso de versión
```

**Cómo validarlo:**

1. Poner el proyecto de prueba en la versión vigente.
2. Abrir una sesión. Resultado esperado: no aparece el aviso.
- **Aprobado cuando:** el silencio significa que está al día.

### CA-03 — El aviso no migra ni detiene

```gherkin
Dado que aparece el aviso de versión atrasada
Cuando se sigue trabajando sin hacer nada al respecto
Entonces el trabajo continúa normal
Y ningún archivo del proyecto cambió por el aviso
```

**Cómo validarlo:**

1. Anotar el estado de los archivos del proyecto de prueba.
2. Abrir sesión, recibir el aviso y seguir trabajando.
3. Comparar los archivos. Resultado esperado: ninguno cambió por el aviso.
- **Aprobado cuando:** avisar y migrar quedan claramente separados.

### Criterios de aceptación transversales

- [ ] **Límites** — un proyecto que declara una versión más nueva que la vigente tiene comportamiento definido.
- [ ] **Errores** — si no se puede leer la versión vigente, el aviso lo dice y no supone que está al día.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Oportunidad** | Aparece al abrir, no cuando ya se trabajó |
| **Rendimiento** | No demora el arranque de la sesión |
| **Claridad** | Se entiende sin abrir el registro de cambios |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica, es texto en el chat.
- **Documento funcional:** [documentacion/epicas/EP-002-versionado-y-adopcion/epica.md](../epica.md), criterio CAE-04.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Comparar la versión declarada con la vigente.
- [ ] Redactar el aviso con las dos versiones y el resumen de lo que cambió.
- [ ] Dejar dicho que el aviso no migra.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [C-EP-002-HU-004-el-ca-01-se-vuelve-a-medir](C-EP-002-HU-004-el-ca-01-se-vuelve-a-medir/estado-fase.md) | CA-01, otra vez | **Ejecutada el 2026-08-29.** Veredicto: [**Cumple**](C-EP-002-HU-004-el-ca-01-se-vuelve-a-medir/resultado_pruebas.md#2-veredicto-de-la-fase) — el aviso sale y la apertura pasa por él: `hook_sesion` llama a `sesion.revisar`, que llama a `version.validar`. Declara reemplazar el veredicto de la fase `A` |
**Ejecutada el 2026-08-22.** Veredicto: [**No cumple**](A-EP-002-HU-004-retrodocumentar-el-aviso-de-desfase/resultado_pruebas.md#5-veredicto-de-la-fase) — el CA-02 y el CA-03 sí; el CA-01 no: el aviso existe y hay que pedirlo a mano |

**La fase retro-documenta.** El aviso sale solo al abrir la sesión. Lo que le falta es la tercera parte de la RN-02: **no dice qué cambió entre las dos versiones**. Y el CA-03 tiene una excepción que hay que dejar escrita — la derogación sin adoptar sí detiene la fase (`02·F22`).

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
| Dependencia | HU-003, porque hay que comparar contra lo que el proyecto declaró | Alto |
| Dependencia | EP-005, porque el disparo al abrir sesión es de esa épica | Medio |
| Riesgo | Que el aviso se vuelva ruido y se ignore | Solo aparece cuando hay desfase, y no detiene |
| Riesgo | Que alguien lo confunda con que ya se migró | El texto dice explícitamente que no cambió nada |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] El aviso aparece solo cuando hay desfase
- [ ] Dice las dos versiones y qué cambió
- [ ] No modifica ningún archivo
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | No | Necesita la declaración de HU-003 y el disparo de EP-005 |
| **N**egociable | Sí | El texto del aviso se puede discutir |
| **V**aliosa | Sí | Sin él, quedarse atrás no se nota |
| **E**stimable | Sí | Alcance acotado |
| **S**mall (pequeña) | Sí | Una comparación y un mensaje |
| **T**esteable | Sí | Se prueba con un proyecto atrasado y uno al día |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
