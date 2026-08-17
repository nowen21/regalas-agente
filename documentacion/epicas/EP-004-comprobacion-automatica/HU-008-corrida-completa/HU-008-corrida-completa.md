# HU-008 — Correr todas las comprobaciones de una sola vez

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-008 |
| **Épica / Feature** | [EP-004 Comprobación automática de lo que no admite discusión](../epica.md) |
| **Módulo / Componente** | Programas de comprobación |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Backlog |

---

## 2. Narrativa

- **Como** quien va a entregar un trabajo
- **Quiero** correr todas las comprobaciones con una sola línea
- **Para** no tener que acordarme de cuáles existen ni en qué orden se corren

---

## 3. Contexto y descripción

Tener veinte comprobaciones sueltas es casi lo mismo que no tenerlas: nadie recuerda cuáles hay, y la que se olvida es justo la que hubiera atajado el problema.

Hace falta una sola puerta de entrada: un comando que las liste, que las corra y que devuelva un resultado único. Y hace falta que se pueda correr una sola cuando se está arreglando algo puntual, porque esperar la corrida entera para ver si un cambio quedó bien desanima a correrla.

También hay comprobaciones que no pueden ir en la corrida de todos los días: las que dependen de herramientas instaladas, las que tardan y las que tocan la red. Esas se corren a propósito, y eso tiene que estar dicho.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Hay una sola puerta de entrada que lista y corre las comprobaciones |
| RN-02 | Se puede correr una sola comprobación por su nombre |
| RN-03 | El resultado de la corrida es uno solo: si hubo alguna falla, la corrida falla |
| RN-04 | Los avisos no hacen fallar la corrida |
| RN-05 | La comprobación que necesita una herramienta instalada, red o tiempo largo no entra en la corrida automática, y se dice por qué |
| RN-06 | Cuando una comprobación detiene el trabajo, el mensaje dice cómo saltarse el control y cuándo es válido hacerlo |

### 3.2 Supuestos

- Quien corre las comprobaciones tiene el intérprete del lenguaje instalado y nada más. Sin dependencias externas.

### 3.3 Fuera de alcance

- Dispararlas solas en el momento de trabajar. Eso es EP-005.
- El conteo de hallazgos por regla. Eso es HU-009.

---

## 4. Criterios de aceptación

### CA-01 — Una sola línea corre todo

```gherkin
Dado que existen varias comprobaciones
Cuando se corre la puerta de entrada sin indicar cuál
Entonces se ejecutan todas las que corresponden a la corrida automática
Y el resultado sale ordenado por comprobación
```

**Cómo validarlo:**

1. Abrir una terminal en la raíz del proyecto.
2. Correr la puerta de entrada sin argumentos de comprobación. Resultado esperado: se ejecutan y su salida sale agrupada, cada una con su título.
3. Contar las que corrieron contra las que existen. Resultado esperado: están todas las de la corrida automática, y ninguna de las que se corren a demanda.
- **Aprobado cuando:** una línea corre el conjunto y la salida dice cuál es cuál.

### CA-02 — Se puede correr una sola

```gherkin
Dado que se está arreglando un hallazgo puntual
Cuando se corre la puerta de entrada indicando una sola comprobación
Entonces se ejecuta solo esa
```

**Cómo validarlo:**

1. Elegir una comprobación por su nombre.
2. Correrla indicándola. Resultado esperado: se ejecuta solo esa y termina rápido.
3. Indicar un nombre que no existe. Resultado esperado: dice cuáles hay, en vez de fallar sin explicación.
- **Aprobado cuando:** se puede correr una sola y el nombre equivocado se responde con la lista.

### CA-03 — El resultado de la corrida es uno solo

```gherkin
Dado que se corren todas las comprobaciones
Cuando al menos una encuentra una falla
Entonces la corrida completa termina con error
Y si solo hubo avisos, termina sin error
```

**Cómo validarlo:**

1. Provocar una falla en un archivo de prueba y correr todo. Resultado esperado: la corrida termina en error.
2. Arreglar la falla dejando algo que solo produzca avisos y correr de nuevo. Resultado esperado: los avisos se ven y la corrida termina sin error.
3. Dejarlo todo limpio y correr otra vez. Resultado esperado: termina sin error y lo dice.
- **Aprobado cuando:** el código de salida distingue los tres casos.

### Criterios de aceptación transversales

- [ ] **Errores** — si una comprobación se cae, la corrida sigue con las demás y lo reporta.
- [ ] **Rendimiento** — la corrida completa termina en un tiempo que no invite a saltársela.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Rendimiento** | La corrida completa sobre cientos de archivos no puede volverse una espera |
| **Autonomía** | Sin dependencias externas, sin red y sin IA |
| **Compatibilidad** | Corre en Windows con rutas que llevan espacios y tildes |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica, la salida es texto en la terminal.
- **Documento funcional:** [documentacion/epicas/EP-004-comprobacion-automatica/epica.md](../epica.md), §5.1 y §5.4 fila 8.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Escribir la puerta de entrada única con un subcomando por comprobación.
- [ ] Definir cuáles entran en la corrida automática y cuáles se corren a demanda.
- [ ] Unificar el código de salida de la corrida.
- [ ] Escribir el texto de ayuda que lista las comprobaciones disponibles.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-004-HU-008-la-corrida-completa-en-una-linea](A-EP-004-HU-008-la-corrida-completa-en-una-linea/README.md) | CA-01, CA-02 y CA-03 | Abierta 2026-08-17, con su plan de trabajo escrito y sin aprobar |

**Mitad retro-documentación, mitad construcción.** Los 24 subcomandos existen; **ninguno los corre todos**. Hoy, para saber cómo está el proyecto, hay que acordarse de los 24 y leer 24 resúmenes.

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
| Dependencia | Las comprobaciones que se corren, de HU-004 a HU-007 | Alto |
| Riesgo | Que la corrida se vuelva lenta y la gente la evite | Lo lento se corre a demanda, no en la corrida de todos los días |
| Riesgo | Que una comprobación caída oculte a las demás | Cada una se aísla y la corrida sigue |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] Existe una sola puerta de entrada
- [ ] Se puede correr una comprobación sola
- [ ] El código de salida distingue falla, aviso y limpio
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Parcial | Necesita comprobaciones que correr |
| **N**egociable | Sí | Cuáles entran en la corrida automática se puede discutir |
| **V**aliosa | Sí | Sin ella, nadie recuerda qué comprobaciones existen |
| **E**stimable | Sí | Alcance corto |
| **S**mall (pequeña) | Sí | Es un punto de entrada |
| **T**esteable | Sí | Se prueba con casos de falla, de aviso y limpio |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
