# HU-007 — La regla que gobierna cómo se escriben las reglas

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-007 |
| **Épica** | [EP-001 Cuerpo de reglas heredable y en capas](../epica.md) |
| **Componente** | Cuerpo de reglas |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Solicitante** | Quien define el estándar |
| **Estado** | Backlog |

## 2. Narrativa

- **Como** quien agrega y cambia reglas con el tiempo
- **Quiero** que esté escrito el procedimiento para hacerlo
- **Para** que el cuerpo no se degrade a punta de reglas mal ubicadas, repetidas o que exigen dos cosas

## 3. Contexto y descripción

El molde de HU-001 dice cómo se ve una regla. Falta lo otro: qué se hace antes de escribirla. Buscar si ya existe, decidir en qué capítulo va, comprobar que sirva a cualquier proyecto, elegir un identificador libre, declarar de qué depende, decidir si se puede comprobar con un programa.

Sin ese procedimiento, el cuerpo crece torcido: la misma exigencia en dos capítulos, reglas que solo sirven a un stack, identificadores que chocan.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Antes de crear una regla se busca si ya existe una que cubra el caso |
| RN-02 | Un tema tiene un solo capítulo dueño |
| RN-03 | Una regla que solo sirve a un lenguaje o a un cliente no entra al cuerpo central |
| RN-04 | El identificador es único, estable y no repite el prefijo del capítulo |
| RN-05 | La regla declara de cuál depende y qué excepciones tiene, con quién las autoriza |
| RN-06 | Se decide y se marca si la regla se puede comprobar con un programa |
| RN-07 | Ninguna regla de proyecto existe sin una regla de la base que la respalde |

### 3.2 Supuestos

- Este procedimiento se aplica también a sí mismo: las reglas de este capítulo cumplen el molde igual que las demás.

### 3.3 Fuera de alcance

- El programa que comprueba que el procedimiento se cumplió. Eso es EP-004.
- La derogación, que va en HU-008.
- El versionado del cuerpo, que es EP-002.

## 4. Criterios de aceptación

### CA-01 — Una regla nueva se enruta al capítulo correcto

```gherkin
Dado que existe el procedimiento para agregar una regla
Cuando se quiere agregar una exigencia nueva
Entonces el procedimiento lleva a buscar primero si ya existe
Y si no existe, indica en qué capítulo va y por qué
```

**Cómo validarlo:**

1. Escoger una exigencia nueva de cualquier tema, por ejemplo algo sobre manejo de archivos temporales.
2. Seguir el procedimiento paso a paso. Resultado esperado: el primer paso es buscar si ya existe algo que la cubra.
3. Continuar hasta el paso de enrutamiento. Resultado esperado: queda decidido el capítulo dueño con el motivo escrito.
- **Aprobado cuando:** la regla queda en un solo capítulo y el motivo está escrito.

### CA-02 — Una regla atada a un stack no entra

```gherkin
Dado que el procedimiento exige que la regla sirva a cualquier proyecto
Cuando alguien propone una regla que nombra un framework
Entonces el procedimiento la rechaza para el cuerpo central
Y la manda a la capa del proyecto
```

**Cómo validarlo:**

1. Proponer a propósito una regla que nombre un framework concreto.
2. Aplicarle el paso del procedimiento que revisa si es agnóstica. Resultado esperado: no pasa, y dice por qué.
3. Reescribirla sin nombrar la tecnología, dejando solo la exigencia de fondo. Resultado esperado: ahora sí pasa, y el detalle concreto queda como ajuste del proyecto.
- **Aprobado cuando:** la versión con framework no entra y la agnóstica sí.

### CA-03 — Una regla que exige dos cosas se parte antes de entrar

```gherkin
Dado que el molde exige una sola exigencia por regla
Cuando el procedimiento revisa una regla candidata con dos exigencias
Entonces indica partirla antes de aceptarla
```

**Cómo validarlo:**

1. Proponer una regla que diga dos cosas distintas.
2. Aplicarle el paso del procedimiento que revisa el molde. Resultado esperado: señala que hay dos exigencias.
3. Partirla en dos y volver a aplicar el procedimiento a cada una. Resultado esperado: las dos pasan y cada una tiene su propio identificador.
- **Aprobado cuando:** la candidata doble no entra, y las dos partidas sí.

### Criterios de aceptación transversales

- [ ] **Validación** — el procedimiento dice qué hacer cuando falta un dato, por ejemplo cuando no hay ejemplo posible.
- [ ] **No regresión** — aplicar el procedimiento a las reglas ya escritas no obliga a renumerarlas.

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| Aplicabilidad | El procedimiento se puede seguir sin haber escrito reglas antes |
| Autocumplimiento | Las reglas de este capítulo cumplen su propio procedimiento |
| Comprobabilidad | Los pasos binarios quedan marcados como comprobables por un programa |

## 6. Tareas técnicas derivadas

- [ ] Escribir los pasos del procedimiento, en orden.
- [ ] Escribir el criterio de enrutamiento entre capítulos.
- [ ] Escribir la exigencia de que una regla de proyecto nombre la de la base que concreta.
- [ ] Marcar cuáles pasos puede comprobar un programa.
- [ ] Aplicar el procedimiento a las reglas ya escritas y anotar el resultado.

## 7. Fases que la implementan

> Trazabilidad hacia abajo. Se completa a medida que la historia se descompone en fases (`02·F12.2`). El enlace se escribe en los dos lados: la fase declara qué criterios cubre y acá se nombra la fase con sus documentos.

Todavía no se descompuso en fases. `02·F12.2` pide al menos una antes de empezar a trabajarla.

**Qué documento responde qué**, para no buscar en el que no es:

| Pregunta | Documento |
|---|---|
| Qué se pide y cuándo se da por aceptado | Esta historia de usuario |
| Qué se va a hacer, en qué orden y sobre qué archivos | `plan_trabajo.md` de la fase |
| Con qué casos se comprueba cada criterio | `plan_pruebas.md` de la fase |
| Qué se ejecutó, con qué resultado, y si el criterio quedó cumplido | `resultado_pruebas.md` de la fase |
| En qué estación va y qué la tiene detenida | `estado-fase.md` de la fase |
| Qué quedó hecho al final | `funcionalidad_implementada.md` de la fase |

## 8. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-001, porque el procedimiento se apoya en el molde | Alto |
| Dependencia | HU-002, por el enrutamiento entre capas | Alto |
| Riesgo | Que el procedimiento sea tan largo que se salte | Los pasos se ordenan del más barato al más costoso |
| Riesgo | Que las reglas de este capítulo no cumplan su propio molde | Se aplican a sí mismas como parte de la definición de terminado |

## 9. Definition of Ready

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y verificables
- [ ] Molde de regla ya definido
- [ ] Dependencias identificadas

## 10. Definition of Done

- [ ] El procedimiento está escrito paso a paso
- [ ] Las reglas del capítulo cumplen su propio procedimiento
- [ ] Cada paso binario está marcado como comprobable
- [ ] Todos los criterios de aceptación verificados

## 11. Validación INVEST

| Criterio | Cumple | Observación |
|---|:--:|---|
| Independiente | Parcial | Necesita el molde y las capas |
| Negociable | Sí | El orden de los pasos se discute |
| Valiosa | Sí | Es lo que evita que el cuerpo se degrade con el tiempo |
| Estimable | Sí | Un capítulo |
| Pequeña | Sí | Pocos pasos, bien definidos |
| Testeable | Sí | Se verifica proponiendo reglas malas a propósito |

## 12. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-13 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
