# HU-013 — Capítulos opt-in de dominio

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-013 |
| **Épica / Feature** | [EP-001 Cuerpo de reglas heredable](../epica.md) |
| **Módulo / Componente** | Cuerpo de reglas — capa `[CAPA 2 · opt-in]` |
| **Tipo** | Funcional |
| **Prioridad** | Could |
| **Estimación** | L |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Backlog |

---

## 2. Narrativa

- **Como** quien arranca un proyecto de un dominio que el estándar todavía no cubre
- **Quiero** encender un capítulo de reglas propio de ese dominio sin que le llegue a los demás proyectos
- **Para** tener las exigencias del dominio escritas, sin cargarle a un CRUD las reglas de un robot o de un modelo

---

## 3. Contexto y descripción

El estándar ya tiene la capa que hace falta: [base/README.md](../../../../base/README.md) define `[CAPA 2 · opt-in]` como la regla que solo aplica si el proyecto la enciende en su `CLAUDE.md`. Y ya tiene el precedente: los capítulos `18 · Despliegue e infraestructura` y `19 · Observabilidad y operación` entraron así.

Lo que falta son los capítulos de dos dominios que el usuario ya trabaja y que hoy no tienen dónde escribir sus exigencias:

| Dominio | Capítulo | De dónde sale |
|---|---|---|
| RPA — soluciones con bots | por asignar | [pendientes/hecho/patrones-rpa.md](../../../../pendientes/hecho/patrones-rpa.md) |
| IA — proyectos que construyen con modelos | `21` | [pendientes/hecho/patron-ia.md](../../../../pendientes/hecho/patron-ia.md) |

**No son dos historias.** Es la misma: lo que un capítulo opt-in de dominio tiene que traer, y cómo se enciende, no cambia según el dominio. Lo que cambia es el contenido, y ese es el trabajo de cada fase.

**Por qué es `Could` y no `Must`.** Ninguno de los dos tiene hoy un proyecto que lo pida. Un capítulo escrito sin un proyecto que lo estrene se escribe con lo que uno se imagina, no con lo que duele — que es justo lo que el resto del estándar evitó naciendo de casos reales. Se adelanta en cuanto haya un proyecto de RPA o de IA en la mano.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Un capítulo de dominio es `[CAPA 2 · opt-in]`: no le llega a un proyecto que no lo encienda |
| RN-02 | El proyecto lo enciende en su `CLAUDE.md`, y en ningún otro sitio |
| RN-03 | Un capítulo opt-in no contradice el núcleo ni las reglas de capa superior; solo agrega |
| RN-04 | Sus reglas se escriben con el mismo molde que las demás y se citan con el mismo formato de identificador |
| RN-05 | Un capítulo de dominio se escribe cuando hay un proyecto que lo va a usar, no antes |

### 3.2 Supuestos

- La numeración de capítulos sigue libre hacia arriba y no hay que reordenar nada para agregar uno.

### 3.3 Fuera de alcance

- El contenido de cada dominio. Eso es una fase por capítulo, no esta historia.
- La clasificación de riesgo de los modelos, que el capítulo de IA reusa: sale de [HU-012](../HU-012-inventario-de-acciones-y-riesgo/HU-012-inventario-de-acciones-y-riesgo.md) y por eso aquel va primero.

---

## 4. Criterios de aceptación

### CA-01 — El capítulo apagado no le llega al proyecto

```gherkin
Dado que existe un capítulo opt-in de dominio
Cuando un proyecto no lo enciende en su CLAUDE.md
Entonces al arrancar la sesión ese capítulo no se carga
Y ninguna de sus reglas rige
```

**Cómo validarlo:**

1. Instalar el estándar en una carpeta de prueba, sin encender ningún capítulo de dominio.
2. Arrancar y mirar qué se cargó.
3. Buscar en lo cargado cualquier regla del capítulo de dominio. Resultado esperado: ninguna.
- **Aprobado cuando:** el capítulo no aparece en lo que se le entregó al agente.

### CA-02 — El capítulo encendido sí le llega

```gherkin
Dado que el proyecto enciende el capítulo en su CLAUDE.md
Cuando arranca la sesión
Entonces el capítulo se carga completo
Y sus reglas se pueden citar por su identificador
```

**Cómo validarlo:**

1. En la misma carpeta de prueba, encender el capítulo en el `CLAUDE.md`.
2. Arrancar y mirar qué se cargó. Resultado esperado: el capítulo entero.
3. Citar una de sus reglas por identificador y correr la comprobación de citas. Resultado esperado: la cita resuelve.
- **Aprobado cuando:** el capítulo se carga y sus reglas se citan sin que la comprobación las reporte.

### CA-03 — Un capítulo de dominio no puede contradecir el núcleo

```gherkin
Dado que un capítulo opt-in escribe una regla que contradice una regla blindada
Cuando se corre la comprobación del molde de las reglas
Entonces se reporta la contradicción
Y la corrida termina con error
```

**Cómo validarlo:**

1. Escribir en un capítulo de dominio de prueba una regla que contradiga una regla del núcleo.
2. Correr la comprobación. Resultado esperado: la reporta y nombra las dos reglas.
3. Quitar la contradicción y volver a correr. Resultado esperado: no reporta nada.
- **Aprobado cuando:** la contradicción se reporta y la regla que solo agrega no.

### Criterios de aceptación transversales

- [ ] **Límites** — dos capítulos de dominio encendidos a la vez, y uno encendido que no existe, tienen comportamiento definido.
- [ ] **No regresión** — los capítulos `18` y `19`, que ya son opt-in, se siguen comportando igual.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Compatibilidad** | Agregar un capítulo de dominio no obliga a tocar ninguno de los proyectos ya instalados |
| RNF-02 | **Trazabilidad** | El `CLAUDE.md` del proyecto deja escrito qué capítulos encendió y desde cuándo |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica.
- **Documento funcional:** [documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/epica.md](../epica.md).
- **Precedente ya construido:** los capítulos `18` y `19`, cerrados con el [pendientes/hecho/patrones-devops.md](../../../../pendientes/hecho/patrones-devops.md).
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Escribir qué trae un capítulo opt-in de dominio y cómo se enciende, si el precedente de `18`/`19` no lo dejó ya escrito.
- [ ] Fase por capítulo: RPA, con su numeración.
- [ ] Fase por capítulo: IA (`21`), que reusa la tabla de riesgo de [HU-012](../HU-012-inventario-de-acciones-y-riesgo/HU-012-inventario-de-acciones-y-riesgo.md).
- [ ] Versionar cada capítulo por separado (`20·M10`): cada uno es un **MENOR**, porque es aditivo y opt-in.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase (`02·F12.6`) | CA que cubre | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|
| — | — | — | — | — | Sin empezar |

**De dónde sale esta historia:** los pendientes [pendientes/hecho/patrones-rpa.md](../../../../pendientes/hecho/patrones-rpa.md) y [pendientes/hecho/patron-ia.md](../../../../pendientes/hecho/patron-ia.md), que son un capítulo cada uno.

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
| Dependencia | [HU-002](../HU-002-capas-y-precedencia/HU-002-capas-y-precedencia.md), porque `[CAPA 2 · opt-in]` es una de sus capas | Alto |
| Dependencia | [HU-012](../HU-012-inventario-de-acciones-y-riesgo/HU-012-inventario-de-acciones-y-riesgo.md), solo para el capítulo de IA: reusa su tabla de riesgo | Medio |
| Riesgo | Escribir el capítulo sin un proyecto que lo estrene, y llenarlo de reglas imaginadas | `RN-05`: no se escribe hasta que haya proyecto |
| Riesgo | Que un capítulo de dominio se cuele a proyectos que no lo pidieron | El CA-01 lo comprueba en una instalación limpia |

---

## 10. Definition of Ready (DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas
- [ ] Hay un proyecto real que estrene el capítulo (`RN-05`)

## 11. Definition of Done (DoD)

- [ ] Los tres criterios de aceptación verificados
- [ ] Cada capítulo con su numeración y su versión **MENOR**
- [ ] Los pendientes 08 y 12 cerrados nombrando su fase

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | La capa opt-in ya existe; esto agrega capítulos encima |
| **N**egociable | Sí | Qué dominios entran y en qué orden |
| **V**aliosa | Parcial | Hoy nadie la pide; vale en cuanto aparezca el proyecto |
| **E**stimable | Parcial | El armazón sí; el contenido de cada dominio depende del dominio |
| **S**mall (pequeña) | No | Son dos capítulos completos, uno por fase |
| **T**esteable | Sí | Se prueba encendiendo y apagando en una instalación limpia |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-17 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU, para que los pendientes 08 y 12 dejen de estar sueltos |
