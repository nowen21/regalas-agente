# HU-001 — Formato único para escribir una regla

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-001 |
| **Épica** | [EP-001 Cuerpo de reglas heredable y en capas](../epica.md) |
| **Componente** | Cuerpo de reglas |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Solicitante** | Quien define el estándar |
| **Estado** | Backlog |

## 2. Narrativa

- **Como** quien escribe y mantiene las reglas del estándar
- **Quiero** que toda regla se escriba con la misma forma
- **Para** poder citarla, revisarla y comprobarla sin tener que leerla completa cada vez

## 3. Contexto y descripción

Sin un molde, cada regla sale distinta: unas dicen tres cosas a la vez, otras no dan ejemplo, otras no se pueden citar porque no tienen nombre propio. Cuando eso pasa, dos personas leen la misma regla y entienden cosas diferentes, y ningún programa puede comprobarla porque no sabe dónde empieza ni dónde termina lo que exige.

Esta historia define el molde antes de escribir la primera regla. Todo lo demás del cuerpo se escribe encima de esto.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Cada regla tiene un identificador propio, único y estable |
| RN-02 | El identificador no repite el prefijo del capítulo donde vive |
| RN-03 | Una regla exige una sola cosa. Si exige dos, son dos reglas |
| RN-04 | Toda regla muestra un ejemplo de lo incorrecto y uno de lo correcto |
| RN-05 | La regla que depende de otra lo declara y la nombra |
| RN-06 | La regla con excepciones las declara, y dice quién autoriza la excepción |
| RN-07 | El cuerpo de la regla es corto. Lo largo se enlaza como anexo, no se mete adentro |

### 3.2 Supuestos

- Quien escribe las reglas es una sola persona y puede sostener el mismo molde en todas.
- Las reglas se leen tanto por una persona como por la IA, así que el molde tiene que servirle a los dos.

### 3.3 Fuera de alcance

- El contenido de las reglas. Acá solo se define la forma.
- El programa que comprueba que el molde se cumpla. Eso es EP-004.
- Cómo se numeran las versiones del cuerpo. Eso es EP-002.

## 4. Criterios de aceptación

### CA-01 — Una regla escrita con el molde queda citable y comprobable

```gherkin
Dado que existe el molde de regla escrito
Cuando alguien escribe una regla nueva siguiéndolo
Entonces la regla queda con identificador propio, una sola exigencia y sus dos ejemplos
Y se puede citar desde otro documento nombrando solo su capítulo y su identificador
```

**Cómo validarlo:**

1. Abrir el documento donde quedó escrito el molde de regla y leer qué partes exige.
2. Escribir una regla de prueba siguiendo ese molde, sobre cualquier tema. Resultado esperado: la regla tiene identificador, título, la exigencia en pocas líneas, un ejemplo de lo incorrecto y uno de lo correcto.
3. Desde otro documento cualquiera, escribir una cita a esa regla usando solo el capítulo y el identificador. Resultado esperado: la cita alcanza para encontrar la regla sin buscar por el texto.
- **Aprobado cuando:** la regla de prueba tiene todas las partes que el molde exige y la cita lleva hasta ella.

### CA-02 — Una regla que exige dos cosas no pasa

```gherkin
Dado que el molde exige una sola exigencia por regla
Cuando alguien escribe una regla que exige dos cosas distintas
Entonces al revisarla contra el molde se detecta que no cumple
Y el molde indica que hay que partirla en dos reglas
```

**Cómo validarlo:**

1. Escribir a propósito una regla que diga dos cosas, por ejemplo que un documento se guarde en cierto lugar y además que se escriba en cierto idioma.
2. Revisar esa regla contra el molde, punto por punto. Resultado esperado: la revisión señala que hay más de una exigencia.
3. Partirla en dos reglas, cada una con su identificador. Resultado esperado: las dos pasan la revisión.
- **Aprobado cuando:** la revisión señala la regla doble antes de partirla, y las dos partidas pasan.

### CA-03 — Un identificador repetido se detecta

```gherkin
Dado que ya existe una regla con cierto identificador
Cuando se escribe otra regla con el mismo identificador
Entonces se detecta el choque antes de aceptarla
```

**Cómo validarlo:**

1. Tomar el identificador de una regla que ya exista.
2. Escribir una regla nueva usando ese mismo identificador. Resultado esperado: al revisar el capítulo aparece el identificador dos veces.
3. Cambiar el identificador de la regla nueva por uno libre. Resultado esperado: ya no hay repetición.
- **Aprobado cuando:** el identificador repetido se ve en la revisión y el cambio lo resuelve.

### Criterios de aceptación transversales

- [ ] **Límites** — el molde dice qué pasa cuando la regla no tiene ejemplo posible, cuando no depende de nada y cuando no tiene excepciones.
- [ ] **No regresión** — las reglas ya escritas siguen cumpliendo el molde después de cualquier ajuste que se le haga.

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| Legibilidad | El molde lo entiende quien no sabe del tema |
| Estabilidad | El identificador de una regla no cambia nunca |
| Comprobabilidad | El molde se puede revisar sin interpretar: o están las partes, o no están |

## 6. Tareas técnicas derivadas

- [ ] Escribir el molde con sus partes obligatorias y opcionales.
- [ ] Definir la forma del identificador y de la cita entre capítulos.
- [ ] Escribir dos reglas de prueba con el molde, una simple y una con excepciones.
- [ ] Documentar qué hacer cuando una regla no admite ejemplo.

## 7. Fases que la implementan

> Trazabilidad hacia abajo. Se completa a medida que la historia se descompone en fases (`02·F12.2`). El enlace se escribe en los dos lados: la fase declara qué criterios cubre y acá se nombra la fase con sus documentos.

| Fase | Criterios que cubre | Plan de trabajo | Plan de pruebas | Estado |
|---|---|---|---|---|
| `A-EP-001-HU-001-molde-de-regla` | CA-01, CA-02, CA-03 | [plan_trabajo.md](A-EP-001-HU-001-molde-de-regla/plan_trabajo.md) | [plan_pruebas.md](A-EP-001-HU-001-molde-de-regla/plan_pruebas.md) | Sin empezar |

**Qué documento responde qué**, para no buscar en el que no es:

| Pregunta | Documento |
|---|---|
| Qué se pide y cuándo se da por aceptado | Esta historia de usuario |
| Qué se va a hacer, en qué orden y sobre qué archivos | `plan_trabajo.md` de la fase |
| Con qué casos se comprueba cada criterio | `plan_pruebas.md` de la fase |
| En qué estación va y qué la tiene detenida | `estado-fase.md` de la fase |
| Qué quedó hecho al final | `funcionalidad_implementada.md` de la fase |

## 8. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | Ninguna. Es la primera historia del cuerpo de reglas | Alto |
| Riesgo | Que el molde sea tan estricto que escribir una regla se vuelva pesado | Se prueba con dos reglas reales antes de darlo por bueno |
| Riesgo | Que el molde no aguante una regla que sí exige varias cosas relacionadas | Se define desde el principio el anexo, para lo que no cabe en el cuerpo |

## 9. Definition of Ready

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y verificables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 10. Definition of Done

- [ ] El molde está escrito y guardado en el cuerpo de reglas
- [ ] Dos reglas de prueba escritas con él
- [ ] Todos los criterios de aceptación verificados
- [ ] Ninguna parte del molde depende de un lenguaje ni de un framework

## 11. Validación INVEST

| Criterio | Cumple | Observación |
|---|:--:|---|
| Independiente | Sí | No necesita nada previo |
| Negociable | Sí | Las partes del molde se pueden discutir |
| Valiosa | Sí | Sin molde, ninguna regla posterior es citable ni comprobable |
| Estimable | Sí | Alcance acotado |
| Pequeña | Sí | Un documento y dos reglas de prueba |
| Testeable | Sí | Se verifica escribiendo reglas y revisándolas |

## 12. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-13 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
