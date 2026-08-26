# HU-011 — El inventario de funcionalidades como puerta de las épicas

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-011 |
| **Épica** | [EP-003 Documentos modelo y procedimientos guiados](../epica.md) |
| **Componente** | Documentos modelo · Flujo de trabajo |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Solicitante** | El usuario, vía el proyecto `shopnest-mesa` (pendiente 74): «esto es importante que cimiento lo sepa» |
| **Estado** | Terminada |
## 2. Narrativa

- **Como** quien encarga un desarrollo
- **Quiero** que la propuesta venga acompañada de un inventario con todas las funcionalidades de lo que se va a desarrollar, aprobado por mí antes de que se deriven las épicas
- **Para** que el alcance lo confirme yo y no lo asuma el agente, y la corrección no llegue cuando ya hay épicas, historias y código encima

## 3. Contexto y descripción

En `shopnest-mesa` el agente escribió el planteamiento asumiendo el alcance (lo centró en el taller de la universidad) y de ahí salieron tres épicas y 21 HU. Seis días después una pregunta del usuario destapó el alcance real (ITIL 4 completo; el taller era el punto de partida, no el techo). Ninguna estación del flujo lo habría preguntado antes: el §6 del molde de planteamiento lista requerimientos, pero nada obliga a que esa lista sea **el** inventario acordado ni a que las épicas bajen de él.

Es el [pendiente 74](../../../../pendientes/hecho/el-inventario-es-la-puerta-de-las-epicas.md). El usuario agregó un rasgo que define el molde: el inventario **se convierte en la documentación final del producto** («manuales y todo eso») — no es un artefacto de planeación que se bota al derivar, sino un documento que madura con el sistema. `shopnest-mesa` ya escribió el suyo (`propuesta-desarrollo/inventario-funcionalidades.md`) y sirve de caso semilla.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | El inventario lista **todas** las funcionalidades, con estado por ítem: existe / parcial / por construir / **por confirmar** (lo por confirmar es pregunta, no decisión) |
| RN-02 | Lo aprueba **el usuario**, y su aprobación es la puerta: sin inventario aprobado no se derivan épicas |
| RN-03 | Toda épica baja de uno o más ítems del inventario; una que no baje de ninguno no arranca |
| RN-04 | El molde nace pensado para madurar hasta manual: cada fila se escribe para quien va a **usar** el producto |
| RN-05 | La regla de flujo nace por el procedimiento del capítulo `20`, con su checklist y su versión (`20·M14`, `20·M10`) |

### 3.2 Supuestos

- La regla rige hacia adelante: los planteamientos ya escritos de los proyectos instalados no se reabren (límite del pendiente).

### 3.3 Fuera de alcance

- Construir un programa que valide la puerta: `20·M19` manda que primero la regla demuestre servir a mano.
- Migrar los inventarios de los proyectos existentes.
- El pendiente 75 (la administración desde la interfaz).

## 4. Criterios de aceptación

### CA-01 — El molde del inventario existe y nace para madurar hasta manual

```gherkin
Dado que la propuesta debe venir acompañada del inventario de funcionalidades
Cuando se escribe el molde en plantillas/
Entonces trae la lista completa con estado por ítem (existe / parcial / por construir / por confirmar)
Y las preguntas abiertas quedan marcadas como preguntas, no como decisiones
Y cada fila se escribe para quien va a usar el producto, porque el documento madura hasta ser el manual
```

**Cómo validarlo:**

1. Abrir `plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md`. Resultado esperado: existe, con los cuatro estados, la sección de lo que el usuario ya definió, y las preguntas abiertas con su marca.
2. Compararlo contra el inventario semilla de `shopnest-mesa`. Resultado esperado: todo lo que aquel tiene, el molde lo pide; si el molde pide algo que aquel no tiene, queda anotado para reportárselo (es el cierre que el pendiente fija).
3. Leer la caja del molde. Resultado esperado: dice que el documento madura hasta manual y que acompaña a la propuesta.
- **Aprobado cuando:** las tres cosas dan lo esperado y el molde pasa `validar.py plantilla`.

### CA-02 — Sin inventario aprobado no se derivan épicas

```gherkin
Dado que el alcance lo confirma el usuario y no lo asume el agente
Cuando alguien va a derivar épicas de una propuesta
Entonces una regla del flujo exige el inventario de funcionalidades aprobado por el usuario como puerta
Y una épica que no baje de un ítem del inventario no arranca
```

**Cómo validarlo:**

1. Comprobar que la regla existe en el capítulo `02`, escrita por el procedimiento del `20` con su checklist en CUMPLE y su ejemplo INCORRECTO/CORRECTO.
2. Aplicarla al caso real de `shopnest-mesa` (2026-08-15): con la regla vigente, el planteamiento centrado en el taller no habría derivado épicas sin que el usuario aprobara antes el inventario. Resultado esperado: la regla detiene ese caso.
3. Aplicarla al mismo proyecto hoy: su inventario existe y está en revisión del usuario. Resultado esperado: la regla no exige rehacer nada; espera la aprobación, que es lo que el documento ya dice.
- **Aprobado cuando:** la regla está publicada y versionada (MAYOR: obliga hacia adelante), detiene el caso histórico y no reabre lo ya escrito.

### CA-03 — Queda escrito si la conducta existente cubría preguntar el alcance

```gherkin
Dado que el agente asumió un alcance que el usuario no había declarado
Cuando se revisa la conducta del capítulo 01 (C4, C7, C17, C21)
Entonces queda escrito, con citas, si alguna exigía preguntar el alcance antes del planteamiento
Y si ninguna lo exigía, la brecha queda cerrada por la regla del CA-02 o propuesta como extensión, con el porqué
```

**Cómo validarlo:**

1. Releer `C4`, `C7`, `C17` y `C21` contra el caso: el usuario pidió la propuesta, el agente asumió el techo del alcance. Resultado esperado: el veredicto escrito dice cuál regla aplicaba, o que ninguna (el pedido traía el dato «sobre qué»; lo que faltaba era el techo, que no es dos lecturas ni un dato ausente de los cuatro campos).
2. Comprobar que la conclusión quedó en la fase (resultado de pruebas o nota enlazada), con el porqué.
- **Aprobado cuando:** el veredicto está escrito y, si hay brecha, dice con qué se cierra.

### Criterios de aceptación transversales

- [ ] **No regresión** — ningún molde ni regla existente cambia de exigencia; solo se agrega.

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| Legibilidad | Molde y regla los entiende quien no conoce el estándar (`00·ID7`) |
| Neutralidad | Agnósticos de stack y dominio (`20·M3`): nada de ITIL ni del caso semilla en el texto normativo |

## 6. Tareas técnicas derivadas

- [x] Escribir el molde en `plantillas/` desde el caso semilla, generalizado.
- [x] Escribir la regla del `02` por el procedimiento del `20`, con checklist.
- [x] Escribir el veredicto sobre la conducta del `01`.
- [x] Versionar (MAYOR) y cerrar el pendiente 74 con su aviso a los instalados.

## 7. Fases que la implementan

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-003-HU-011-el-inventario-como-puerta-de-las-epicas](A-EP-003-HU-011-el-inventario-como-puerta-de-las-epicas/plan_trabajo.md) | CA-01, CA-02 y CA-03 | **Cerrada 2026-08-21, Cumple** (3 de 3 casos; v29.0.0) |

## 8. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | El caso semilla de `shopnest-mesa` como material del molde | Medio |
| Dependencia | HU-002 de esta épica (modelos del encargo): el inventario acompaña a la propuesta que aquella moldea | Medio |
| Riesgo | Que la regla se lea como burocracia para proyectos chicos | El molde escala: en uno chico el inventario es una tabla de diez filas; la puerta es la aprobación, no el tamaño |
| Riesgo | Que el capítulo `02` no tenga dueño claro para la regla ([pendiente 60](../../../../pendientes/hecho/cada-capitulo-tiene-su-historia.md)) | Esta HU la respalda como CA-02, que es exactamente el remedio que el 60 pide historia por historia |

## 9. Definition of Ready

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y verificables
- [x] Caso semilla disponible y pedido del usuario literal en el pendiente
- [x] Dependencias identificadas

## 10. Definition of Done

- [ ] Molde publicado y regla del `02` con checklist en CUMPLE
- [ ] Todos los criterios de aceptación verificados
- [ ] Versión subida (MAYOR) y pendiente 74 cerrado con su aviso

## 11. Validación INVEST

| Criterio | Cumple | Observación |
|---|:--:|---|
| Independiente | Sí | El caso semilla ya está escrito allá |
| Negociable | Sí | La forma del molde y la redacción de la regla se discuten |
| Valiosa | Sí | Evita la clase de error que costó 21 HU sobre alcance asumido |
| Estimable | Sí | Un molde, una regla, un veredicto |
| Pequeña | Sí | Una fase |
| Testeable | Sí | El caso histórico de `shopnest-mesa` es el oráculo |

## 12. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-21 | El agente, por orden del usuario («siga», con el orden acordado) | Creación desde el pendiente 74, reportado por `shopnest-mesa` |
| 2026-08-21 | El agente, con HU y planes aprobados por el usuario | Fase A cerrada en Cumple: nacen `02·F26` y el molde del inventario; versión 29.0.0 (MAYOR); pendiente 74 a `hecho/` con aviso a los 9 instalados |
