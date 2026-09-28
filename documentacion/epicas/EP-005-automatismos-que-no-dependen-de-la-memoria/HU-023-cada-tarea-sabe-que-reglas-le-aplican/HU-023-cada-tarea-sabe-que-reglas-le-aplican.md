# HU-023 · Cada tarea sabe qué reglas le aplican

> Nace del [pendiente 100](../../../../pendientes/100-cada-tarea-sabe-que-reglas-le-aplican.md), aprobado por el usuario el 2026-09-28.

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-023 |
| **Épica / Feature** | [EP-005 · Automatismos que no dependen de que alguien se acuerde](../epica.md) |
| **Módulo / Componente** | Cuerpo de reglas, todos los capítulos, y `validadores/` |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | L |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | El usuario |
| **Responsable** | El agente |
| **Estado** | Terminada |

## 2. Narrativa

- **Como** agente que va a hacer una tarea
- **Quiero** un mapa que lleve de la tarea a las reglas que le aplican, con su enlace
- **Para** leer solo esas antes de actuar, sin cargar todas

## 3. Contexto y descripción

No hay un mapa que lleve de una tarea a las reglas que le aplican. El 2026-09-28 el usuario decidió que el agente no cargue las reglas al arrancar, sino que antes de cada tarea identifique y lea las que le corresponden. Hoy los índices de `base/` están ordenados por capítulo, y para encontrar una regla hay que saber de antemano en qué capítulo está.

El antecedente, [validadores/reglas-antes-de-la-accion.md](../../../../validadores/reglas-antes-de-la-accion.md), clasifica las reglas por cuándo se pueden comprobar, no por a qué tarea aplican, y cuenta 248 reglas cuando `metareglas.py` cuenta hoy 261.

Va en esta épica y no por la historia dueña de cada capítulo porque toca las reglas de todos los capítulos a la vez, con una línea que no cambia qué exige ninguna. Es el mismo caso de [`EP-005·HU-012`](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda/HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md), que agregó a cada regla del núcleo quién la hace cumplir.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Hay una lista cerrada de tareas, escrita en `base/`. Una tarea que no está en la lista no se usa |
| RN-02 | Cada regla vigente declara a qué tareas aplica, en una línea `**Aplica a:**` después de su ejemplo. La línea no es parte del cuerpo: no cuenta para el largo ni anula el checklist, igual que «Nadie la hace cumplir» |
| RN-03 | El mapa `base/mapa-de-tareas.md` lo escribe un programa leyendo esas líneas, nunca una persona. Por cada tarea lista sus reglas, con el enlace a cada una |
| RN-04 | Un validador falla si una regla vigente no declara sus tareas, si nombra una tarea fuera de la lista o si el mapa no coincide con lo que declaran las reglas. Corre solo antes de publicar, sin que nadie tenga que llamarlo |
| RN-05 | El validador del mapa del amarre da por clasificado un programa solo si lo nombra una fila de tabla o una línea que lista nombres, no una frase cualquiera. Todo programa de `validadores/` y del adaptador queda clasificado. Viene de H-8 de la sesión del 2026-09-28, que salió en la fase `A` |
| RN-06 | Con cada mensaje del usuario, el recuperador reconoce las tareas que el mensaje pide y le entrega al agente las reglas que el mapa pone bajo esas tareas. `recibir-pedido` y `responder` van siempre, porque todo mensaje es un pedido y lleva respuesta. Ningún capítulo queda fuera por suponer que llegó al arrancar. Viene de H-9 de la sesión del 2026-09-28 |

### 3.2 Supuestos

- `metareglas.py` cuenta 261 reglas: 252 vigentes y 9 derogadas. Se anotan las vigentes; las derogadas no.

### 3.3 Fuera de alcance

- La instrucción que el agente recibe al arrancar la sesión.
- El enganche que le muestra al agente la regla en el momento de actuar.
- Cambiar qué exige cualquier regla.

## 4. Criterios de aceptación

### CA-01 · La lista de tareas existe y es cerrada

```gherkin
Dado que el mapa necesita agrupar las reglas por tarea
Cuando se abre la lista de tareas en base/
Entonces cada tarea tiene su nombre y una frase que dice cuándo aplica
Y no hay dos tareas que cubran lo mismo
```

**Cómo validarlo:**

1. Abrir `base/tareas.md`. Resultado esperado: una tabla con cada tarea, su nombre corto y cuándo aplica.
2. Leer las filas de dos en dos. Resultado esperado: ninguna acción del agente cae en dos tareas a la vez.
- **Aprobado cuando:** la lista existe y ninguna tarea se superpone con otra.

### CA-02 · Una regla declara sus tareas sin cambiar lo que exige

```gherkin
Dado una regla vigente con su checklist en CUMPLE
Cuando se le agrega su línea **Aplica a:**
Entonces el largo de su cuerpo no cambia
Y su checklist no queda anulado
```

**Cómo validarlo:**

1. Tomar una regla con su checklist en CUMPLE y medir su cuerpo con `Regla.largo()` de `validadores/metareglas.py`.
2. Agregarle la línea `**Aplica a:**` con una tarea de la lista.
3. Medir de nuevo. Resultado esperado: el mismo número.
4. Correr `python validadores/validar.py metareglas`. Resultado esperado: no dice que el checklist de esa regla quedó anulado.
- **Aprobado cuando:** el largo no cambia y el checklist sigue vigente.

### CA-03 · El mapa sale de las reglas

```gherkin
Dado que las reglas declaran sus tareas
Cuando se corre el programa que arma el mapa
Entonces base/mapa-de-tareas.md lista cada tarea con sus reglas, enlazadas
Y si una regla cambia sus tareas, el mapa cambia al volver a correrlo
```

**Cómo validarlo:**

1. Correr el programa. Resultado esperado: escribe `base/mapa-de-tareas.md`.
2. Abrir el mapa y buscar una regla que declare dos tareas. Resultado esperado: aparece bajo las dos, con su enlace.
3. Cambiarle a esa regla una tarea por otra y volver a correr el programa. Resultado esperado: el mapa la muestra bajo la tarea nueva y no bajo la vieja.
- **Aprobado cuando:** los tres pasos dan lo esperado.

### CA-04 · El validador detecta lo que falta o no cuadra

```gherkin
Dado el validador del mapa
Cuando una regla no declara tareas, o nombra una fuera de la lista, o el mapa quedó viejo
Entonces falla y dice cuál regla y por qué
Y con el repositorio al día, pasa
```

**Cómo validarlo:**

1. En una copia de prueba, quitarle a una regla su línea `**Aplica a:**` y correr el validador. Resultado esperado: falla nombrando la regla.
2. Ponerle una tarea que no está en la lista. Resultado esperado: falla nombrando la tarea.
3. Cambiar una tarea sin volver a generar el mapa. Resultado esperado: falla diciendo que el mapa quedó viejo.
4. Correrlo sobre el repositorio como queda. Resultado esperado: pasa.
- **Aprobado cuando:** los cuatro pasos dan lo esperado.

### CA-05 · Toda regla vigente declara sus tareas

```gherkin
Dado que el formato y el mapa existen
Cuando se recorren las reglas vigentes de base/
Entonces todas tienen su línea **Aplica a:**
```

**Cómo validarlo:**

1. Correr el validador del mapa sobre el repositorio. Resultado esperado: 0 reglas sin tareas.
2. Contar las reglas del mapa y las que cuenta `metareglas.py`. Resultado esperado: el mismo número.
- **Aprobado cuando:** ninguna regla vigente queda fuera del mapa.

### CA-06 · El mapa del amarre no da por clasificado lo que solo se nombra

```gherkin
Dado un programa de validadores/ que el mapa del amarre solo nombra en una frase
Cuando se corre validar.py amarre
Entonces lo reporta como sin clasificar
Y con todos los programas clasificados en su tabla o su lista, pasa
```

**Cómo validarlo:**

1. En una copia de prueba, nombrar un programa sin clasificar dentro de una frase del mapa y correr el validador. Resultado esperado: lo reporta como sin clasificar.
2. Ponerlo en una fila de tabla con su columna. Resultado esperado: deja de reportarlo.
3. Correr `python validadores/validar.py amarre` sobre el repositorio. Resultado esperado: 0 fallas, con todos los programas de `validadores/` y del adaptador clasificados.
4. Correr `python -m unittest test_el_mapa_del_amarre_no_envejece` desde `validadores/tests`. Resultado esperado: OK.
- **Aprobado cuando:** los cuatro pasos dan lo esperado.

### CA-07 · El recuperador trae las reglas de la tarea que pide el mensaje

```gherkin
Dado que el usuario escribe un mensaje
Cuando el enganche de cada turno llama al recuperador
Entonces el agente recibe las reglas que el mapa pone bajo las tareas del mensaje
Y siempre las de recibir-pedido y responder
```

**Cómo validarlo:**

1. Pasarle al recuperador «suba a git». Resultado esperado: trae `00·N2`.
2. Pasarle «aplique las reglas de la caja de reglas de redacción al readme». Resultado esperado: trae `00·ID8`, `00·ID9`, `00·ID11` y `00·ID12`.
3. Pasarle «cree el pendiente del H2». Resultado esperado: trae `02·F23` y `01·C28`.
4. Abrir `.claude/settings.json` del estándar. Resultado esperado: el enganche `hook_reglas.py` está en `UserPromptSubmit`.
- **Aprobado cuando:** los cuatro pasos dan lo esperado.

### Criterios de aceptación transversales

- [ ] No regresión: `metareglas`, `estandar` y la suite de pruebas quedan sin fallas nuevas (`08`, [`02·F5`](../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)).

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Trazabilidad** | El cambio se registra en `CHANGELOG.md` y sube `VERSION` |
| RNF-02 | **Mantenibilidad** | El programa y el validador tienen sus pruebas en `validadores/tests/` |

## 6. Diseño y referencias

- Documento funcional: el [pendiente 100](../../../../pendientes/100-cada-tarea-sabe-que-reglas-le-aplican.md).
- Precedente de una línea fuera del cuerpo de la regla: `_FUERA_DEL_CUERPO` en `validadores/metareglas.py`.
- Antecedente de clasificación: [validadores/reglas-antes-de-la-accion.md](../../../../validadores/reglas-antes-de-la-accion.md).

## 7. Tareas técnicas derivadas

- [ ] Escribir la lista cerrada de tareas
- [ ] Hacer que `metareglas.py` deje la línea `**Aplica a:**` fuera del cuerpo
- [ ] Escribir el programa que arma el mapa, con sus pruebas
- [ ] Escribir el validador del mapa, con sus pruebas
- [ ] Anotar las 252 reglas vigentes
- [ ] Corregir el validador del amarre y clasificar los programas que le faltan
- [ ] Versionar el cambio

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| [`A-EP-005-HU-023-la-lista-de-tareas-y-el-mapa`](A-EP-005-HU-023-la-lista-de-tareas-y-el-mapa/) | CA-01, CA-02, CA-03 | | [plan_trabajo](A-EP-005-HU-023-la-lista-de-tareas-y-el-mapa/plan_trabajo.md) | [plan_pruebas](A-EP-005-HU-023-la-lista-de-tareas-y-el-mapa/plan_pruebas.md) | [resultado](A-EP-005-HU-023-la-lista-de-tareas-y-el-mapa/resultado_pruebas.md) | Cerrada 2026-09-28 · Cumple |
| [`B-EP-005-HU-023-todas-las-reglas-declaran-sus-tareas`](B-EP-005-HU-023-todas-las-reglas-declaran-sus-tareas/) | CA-04, CA-05, CA-06, CA-07 | CA-01, CA-02 | [plan_trabajo](B-EP-005-HU-023-todas-las-reglas-declaran-sus-tareas/plan_trabajo.md) | [plan_pruebas](B-EP-005-HU-023-todas-las-reglas-declaran-sus-tareas/plan_pruebas.md) | [resultado](B-EP-005-HU-023-todas-las-reglas-declaran-sus-tareas/resultado_pruebas.md) | Cerrada 2026-09-28 · Cumple |

**Qué documento responde qué**, para no buscar en el que no es:

| Pregunta | Documento |
|---|---|
| Qué se pide y cuándo se da por aceptado | Esta HU |
| Qué se va a hacer, en qué orden y sobre qué archivos | `plan_trabajo.md` de la fase |
| Con qué casos se comprueba cada CA | `plan_pruebas.md` de la fase |
| Qué se ejecutó, con qué resultado, y si el CA quedó cumplido | `resultado_pruebas.md` de la fase |
| En qué estación va y qué la tiene detenida | `estado-fase.md` de la fase |
| Qué quedó hecho al final | `funcionalidad_implementada.md` de la fase |

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Que la lista de tareas quede tan fina que cada regla caiga en muchas, o tan gruesa que no sirva para elegir | La lista se prueba en la fase `A` contra las reglas del núcleo antes de anotar el resto |
| Riesgo | Que anotar 252 reglas a mano meta errores | El validador de la fase `B` los detecta, y cada tarea nombrada tiene que estar en la lista |

## 10. Definition of Ready (DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas y desbloqueadas
- [ ] Estimada por el equipo
- [x] Cumple criterios INVEST

## 11. Definition of Done (DoD)

- [ ] Lista, mapa, programa y validador en rama principal
- [ ] Pruebas del programa y del validador pasando
- [ ] Todos los criterios de aceptación verificados
- [ ] Requisitos no funcionales validados
- [ ] Aceptada por el usuario

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | ☑ | No espera a otra historia |
| **N**egociable | ☑ | La lista de tareas se decide en la fase `A` |
| **V**aliosa | ☑ | Sin el mapa, el agente no sabe qué regla leer antes de una tarea |
| **E**stimable | ☑ | Una lista, dos programas y una línea por regla |
| **S**mall (pequeña) | ☑ | Partida en dos fases: el formato y el mapa, y después las 242 que faltan, con el validador |
| **T**esteable | ☑ | El programa y el validador se prueban con casos; la lista se lee |

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-09-28 | El agente | Creación de la HU, a partir del pendiente 100 |
| 2026-09-28 | El agente | Fase `A` cerrada con veredicto Cumple: la lista de tareas, la línea `**Aplica a:**` en el núcleo y el programa del mapa, versión 39.2.0 |
| 2026-09-28 | El agente | Suma RN-05 y CA-06 por H-8, que salió en la fase `A`: el usuario decidió que se resuelve en esta HU. Se abre la fase `B`, con CA-04 a CA-06 |
| 2026-09-28 | El agente | Suma RN-06 y CA-07 por H-9: el recuperador de reglas ya existía y fallaba, y el usuario eligió que la fase `B` lo haga trabajar con el mapa. El plan de la fase se reescribe y vuelve a aprobación |
| 2026-09-28 | El agente | Fase `B` cerrada con veredicto Cumple: las 252 reglas con sus tareas, el validador, la corrección del amarre y el recuperador por tareas conectado en el estándar, versión 39.3.0 |
