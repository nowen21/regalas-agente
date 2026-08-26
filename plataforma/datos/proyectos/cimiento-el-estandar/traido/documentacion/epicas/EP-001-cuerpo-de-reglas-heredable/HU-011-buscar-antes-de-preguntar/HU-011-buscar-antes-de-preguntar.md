# HU-011 — Buscar en el repositorio antes de preguntar

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-011 |
| **Épica / Feature** | [EP-001 Cuerpo de reglas heredable](../epica.md) |
| **Módulo / Componente** | Capítulo `01 · Conducta de la IA` |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Done |

---

## 2. Narrativa

- **Como** quien ya dejó una decisión escrita en el repositorio
- **Quiero** que se busque antes de preguntármela
- **Para** no volver a decidir lo que ya está decidido

---

## 3. Contexto y descripción

El estándar ya exige que el pedido incompleto se pregunte en vez de adivinarse, y esa exigencia funciona: el agente pregunta. Lo que falta es el paso de antes.

El 2026-08-14 el agente le preguntó al usuario en qué orden trabajar dos historias y le ofreció tres opciones. La respuesta ya estaba escrita: [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/HU-008-enganche-del-resumen.md](../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/HU-008-enganche-del-resumen.md) declara en su §9 que depende de HU-009, con impacto alto.

La pregunta tenía **premisa falsa**: cualquiera de las tres respuestas habría contradicho una dependencia ya escrita. Y le devolvió al usuario el trabajo de leer lo que él mismo dejó escrito.

Es el mismo daño que produce no preguntar, por el camino contrario. No preguntar hace que el agente adivine; preguntar lo ya decidido hace que el usuario decida dos veces, y la segunda vez puede contestar distinto — y entonces el repositorio se contradice consigo mismo sin que nadie lo note.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Antes de preguntarle algo al usuario se busca la respuesta en el repositorio |
| RN-02 | La búsqueda tiene un orden fijo y escrito, para que sea la misma cada vez |
| RN-03 | Si la respuesta está escrita, no se pregunta: se cita el archivo donde está y se sigue |
| RN-04 | Si lo escrito y lo que el usuario acaba de pedir se contradicen, se muestra la contradicción y se pregunta cuál manda — eso sí es pregunta legítima |
| RN-05 | Si la respuesta no está escrita, se pregunta. Esta regla no reduce las preguntas: cambia cuáles |

### 3.2 Supuestos

- Las decisiones se escriben donde el estándar manda escribirlas: la historia, la épica, el resumen de sesión, el histórico y la memoria del agente. Una decisión que nadie escribió no se puede encontrar, y eso es problema de otra regla.

### 3.3 Fuera de alcance

- Reducir las preguntas. Preguntar lo que de verdad no está decidido es lo que evita adivinar, y esta historia no lo toca.
- Buscar fuera del repositorio.
- Decidir qué manda cuando el brief y el histórico se contradicen. Es un hueco aparte, anotado en el punto 8 del [pendientes/hecho/lo-que-quedo-abierto-en-las-sesiones-viejas.md](../../../../pendientes/hecho/lo-que-quedo-abierto-en-las-sesiones-viejas.md).

---

## 4. Criterios de aceptación

### CA-01 — Lo que ya está escrito no se pregunta

```gherkin
Dado que una decisión está escrita en un documento del repositorio
Cuando el agente necesita esa decisión para seguir
Entonces la busca, la encuentra y sigue citando dónde está
Y no se la pregunta al usuario
```

**Cómo validarlo:**

1. Elegir una decisión que esté escrita en un solo sitio del repositorio. Sirve la dependencia HU-008 → HU-009 del §9 de [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/HU-008-enganche-del-resumen.md](../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/HU-008-enganche-del-resumen.md), que es el caso real que originó esta historia.
2. Abrir una sesión y pedirle al agente el trabajo que necesita esa decisión — en el caso de ejemplo, pedirle que trabaje las dos historias.
3. Leer la respuesta. Resultado esperado: nombra el orden, cita el archivo y la sección donde lo leyó, y no ofrece opciones.
- **Aprobado cuando:** la respuesta trae la cita del archivo y no trae la pregunta.

### CA-02 — Lo que no está escrito sí se pregunta

```gherkin
Dado que una decisión no está escrita en ninguna parte del repositorio
Cuando el agente la necesita para seguir
Entonces pregunta
Y dice dónde buscó antes de preguntar
```

**Cómo validarlo:**

1. Elegir algo que efectivamente no esté decidido en el repositorio. Sirve cualquiera de las 42 dudas de [pendientes/hecho/las-42-dudas-que-detenian-26-fases.md](../../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md).
2. Pedirle al agente el trabajo que la necesita.
3. Leer la respuesta. Resultado esperado: pregunta, y antes de la pregunta dice dónde buscó y no encontró.
- **Aprobado cuando:** la pregunta llega acompañada de dónde se buscó. Una pregunta sin eso incumple la regla aunque la pregunta sea correcta.

### CA-03 — Lo escrito que contradice el pedido se muestra

```gherkin
Dado que el usuario pide algo que contradice una decisión ya escrita
Cuando el agente encuentra la decisión escrita
Entonces muestra la contradicción, nombrando el archivo
Y pregunta cuál de las dos manda antes de tocar nada
```

**Cómo validarlo:**

1. Pedirle al agente algo que contradiga una dependencia escrita — por ejemplo, construir HU-008 antes que HU-009, al revés de lo que dice su §9.
2. Leer la respuesta. Resultado esperado: nombra el archivo y la sección que dice lo contrario, y pregunta cuál manda.
3. Comprobar que no tocó ningún archivo antes de preguntar.
- **Aprobado cuando:** la contradicción se muestra con su cita y nada se modificó antes de la respuesta del usuario.

### Criterios de aceptación transversales

- [x] **Límites** — el orden para en cuanto encuentra, así que la decisión escrita en dos sitios se resuelve por el primero; la que el orden no cubre cae en «no está» y se pregunta.
- [x] **No regresión** — [`01·C7`](../../../../base/01-conducta.md#c7--ante-dos-lecturas-pregunta) y [`01·C21`](../../../../base/01-conducta.md#c21--pide-el-dato-que-falte-antes-de-arrancar) siguen vigentes: `C23` las extiende, no las debilita.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Trazabilidad** | La respuesta cita archivo y sección, no «lo vi en el repositorio» |
| RNF-02 | **Determinismo** | El orden de búsqueda es el mismo en toda sesión, y está escrito en la regla |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica, es una regla de conducta.
- **Documento funcional:** [documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/epica.md](../epica.md).
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [x] Escribir la regla en el capítulo `01 · Conducta de la IA`, con el orden de búsqueda — es [`01·C23`](../../../../base/01-conducta.md#c23--busca-en-el-repositorio-antes-de-preguntar).
- [x] Decidir y escribir el orden: la historia y su §9, la épica, el resumen de sesión, el histórico, la memoria del agente.
- [x] Declarar si es validable (`20·M9`) y por qué. **Validable a medias:** que se haya buscado no se ve; que la respuesta traiga su cita, sí.
- [x] Versionar el cambio (`20·M10`) — 23.5.0, **MENOR**.
- [ ] **Queda:** el programa que comprueba la mitad validable. Es su propia fase.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase (`02·F12.6`) | CA que cubre | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|
| [`A-EP-001-HU-011-la-regla-de-buscar-antes-de-preguntar`](A-EP-001-HU-011-la-regla-de-buscar-antes-de-preguntar/) | CA-01, CA-02, CA-03 | [documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-011-buscar-antes-de-preguntar/A-EP-001-HU-011-la-regla-de-buscar-antes-de-preguntar/plan_trabajo.md](A-EP-001-HU-011-la-regla-de-buscar-antes-de-preguntar/plan_trabajo.md) | [documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-011-buscar-antes-de-preguntar/A-EP-001-HU-011-la-regla-de-buscar-antes-de-preguntar/plan_pruebas.md](A-EP-001-HU-011-la-regla-de-buscar-antes-de-preguntar/plan_pruebas.md) | [documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-011-buscar-antes-de-preguntar/A-EP-001-HU-011-la-regla-de-buscar-antes-de-preguntar/resultado_pruebas.md](A-EP-001-HU-011-la-regla-de-buscar-antes-de-preguntar/resultado_pruebas.md) · **Cumple** | Cerrada |

**De dónde sale esta historia:** el [pendientes/hecho/buscar-en-el-repositorio-antes-de-preguntar.md](../../../../pendientes/hecho/buscar-en-el-repositorio-antes-de-preguntar.md), que la redactó y le puso este mismo identificador.

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
| Dependencia | [HU-001](../HU-001-formato-unico-de-regla/HU-001-formato-unico-de-regla.md), porque la regla se escribe con el molde único | Medio |
| Riesgo | Que la regla se lea como «no preguntes» y el agente empiece a adivinar | Se escribe el caso contrario dentro de la propia regla, con su ejemplo INCORRECTO |
| Riesgo | Que buscar en cinco sitios antes de cada pregunta vuelva lenta toda sesión | El orden se detiene en cuanto encuentra; los sitios están ordenados de más probable a menos |

---

## 10. Definition of Ready (DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas
- [x] Decidido el orden de búsqueda

## 11. Definition of Done (DoD)

- [x] La regla escrita en el capítulo `01`, con su orden de búsqueda
- [x] Los tres criterios de aceptación verificados
- [x] Declarada validable a medias, con su motivo (`20·M9`)
- [x] Versionada (`20·M10`) — 23.5.0
- [x] El pendiente 24 cerrado nombrando la fase

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | No necesita que se construya nada antes |
| **N**egociable | Sí | El orden de búsqueda se puede discutir |
| **V**aliosa | Sí | Evita que el usuario decida dos veces la misma cosa |
| **E**stimable | Sí | Es una regla y su ejemplo |
| **S**mall (pequeña) | Sí | Una regla |
| **T**esteable | Parcial | Se comprueba por la cita en la respuesta, no por la búsqueda en sí |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-17 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU, para que el pendiente 24 deje de estar suelto |
