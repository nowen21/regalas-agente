# HU-004 — Comprobar la forma de los documentos y sus espacios sin llenar

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-004 |
| **Épica / Feature** | [EP-004 Comprobación automática de lo que no admite discusión](../epica.md) |
| **Módulo / Componente** | Programas de comprobación |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | En curso. CA-04 cerrado en la fase A; el CA-05, abierto en la fase B |
---

## 2. Narrativa

- **Como** quien aprueba un documento de trabajo
- **Quiero** que un programa avise si le faltan secciones o quedaron espacios sin llenar
- **Para** no aprobar un plan que todavía trae los marcadores de la plantilla

---

## 3. Contexto y descripción

Los documentos de trabajo salen de plantillas. Al llenarlas se olvidan cosas: una sección que no se copió, un marcador que quedó tal cual, una pregunta obligatoria que nadie respondió.

Eso se descubre tarde, casi siempre cuando alguien necesita el dato que faltaba. Y es lo más fácil de revisar con un programa, porque no exige entender lo que dice el documento: solo mirar si está lo que la plantilla pide.

Aquí entra también lo que el estándar exige del contenido de un plan y que se responde con un sí o un no: que declare la especificación que lo respalda, que responda las preguntas obligatorias, que no deje marcas de duda y que cada tarea cuelgue del criterio de aceptación que la justifica.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Un documento se compara contra la plantilla de la que salió, no contra una copia de la plantilla escrita dentro del programa |
| RN-02 | Un marcador de plantilla sin reemplazar es un hallazgo |
| RN-03 | Una sección ausente es aviso, no falla: las plantillas permiten borrar lo que no aplica |
| RN-04 | El plan de una fase declara la especificación que lo respalda, y esa especificación existe |
| RN-05 | El plan responde las preguntas obligatorias y no deja marcas de duda sin resolver |
| RN-06 | Toda tarea del plan cuelga de un criterio de aceptación, salvo la que se declara como soporte técnico |
| RN-07 | El texto fijo que la plantilla pone antes de su primer separador sobrevive al llenado: es instrucción de uso, no relleno |
| RN-08 | Ese lugar dice cómo se usa el documento, no de dónde salió: una fecha ahí es procedencia, y la procedencia va en la identificación |

### 3.2 Supuestos

- Las plantillas viven en el estándar y son la fuente de la verdad. Si cambian, la comprobación cambia con ellas sin tocar el programa.

### 3.3 Fuera de alcance

- Juzgar si lo escrito en cada sección es bueno. Eso es criterio.
- Los enlaces y las citas del documento. Eso es HU-005.

---

## 4. Criterios de aceptación

### CA-01 — Un documento con marcadores sin llenar se marca

```gherkin
Dado que existe un documento hecho desde una plantilla
Cuando quedó un marcador sin reemplazar
Entonces la comprobación lo reporta con su archivo y su línea
```

**Cómo validarlo:**

1. Copiar una plantilla del estándar a un documento de prueba y llenar solo la mitad.
2. Correr la comprobación del documento contra su plantilla. Resultado esperado: reporta cada marcador que quedó, con la línea exacta.
3. Reemplazar los marcadores y volver a correr. Resultado esperado: no reporta ninguno.
- **Aprobado cuando:** reporta todos los pendientes y ninguno de los ya llenados.

### CA-02 — Una sección ausente avisa pero no detiene

```gherkin
Dado que existe un documento al que le falta una sección de la plantilla
Cuando se corre la comprobación
Entonces reporta la sección ausente como aviso
Y la corrida termina sin error
```

**Cómo validarlo:**

1. Borrar una sección opcional del documento de prueba.
2. Correr la comprobación. Resultado esperado: sale el aviso con el nombre de la sección.
3. Mirar el código con que terminó la corrida. Resultado esperado: termina en cero.
- **Aprobado cuando:** el aviso aparece y la corrida no se detiene.

### CA-03 — Un plan sin especificación y con tareas sueltas se marca

```gherkin
Dado que existe el plan de una fase
Cuando no declara la especificación que lo respalda, o alguna tarea no cuelga de ningún criterio de aceptación
Entonces la comprobación reporta cada caso por separado
Y nombra la regla que se incumple
```

**Cómo validarlo:**

1. Tomar el plan de una fase de prueba y borrarle la fila donde declara su especificación.
2. Correr la comprobación. Resultado esperado: reporta que el plan no declara especificación, citando la regla.
3. Agregar al plan una tarea fuera de todo bloque de criterio de aceptación y volver a correr. Resultado esperado: reporta esa tarea por su identificador.
4. Declarar esa misma tarea como soporte de un criterio y volver a correr. Resultado esperado: deja de reportarla.
- **Aprobado cuando:** los tres casos se reportan y el soporte declarado deja de reportarse.

### CA-04 — Una regla de negocio sin origen se marca

```gherkin
Dado que una especificación de módulo trae una regla de negocio
Cuando esa regla no dice de dónde baja
Entonces se reporta como falla, con la línea y el texto de la regla
```

**Cómo validarlo:**

1. Escribir una especificación con una regla que baje de un requisito y otra que no baje de nada. Comprobar. Resultado esperado: sale una sola falla, la de la segunda.
2. Ponerle una procedencia a la segunda y volver a comprobar. Resultado esperado: ninguna falla.
3. Dejar el molde de la plantilla sin llenar. Resultado esperado: no se reporta dos veces; de eso ya se queja la comprobación de marcadores.
- **Aprobado cuando:** una regla sin fuente no pasa en silencio.

> **Es falla y no aviso.** Una regla sin procedencia ya se coló hasta un criterio de aceptación en un proyecto real. Lo que avisa, se ignora.

### CA-05 — El texto fijo de la plantilla sobrevive al llenado

```gherkin
Dado un documento que salió de una plantilla con texto fijo antes del primer separador
Cuando se comprueba contra su plantilla
Entonces se reprueba si ese texto se borró o se reemplazó por otro contenido
Y se reprueba si ese texto trae una fecha y el de la plantilla no
```

**Cómo validarlo:**

1. Tomar un planteamiento llenado y correr la comprobación contra su plantilla. Resultado esperado: pasa.
2. Borrarle el texto fijo y volver a correrla. Resultado esperado: falla, nombrando el archivo y diciendo qué había ahí.
3. Reemplazar ese texto por una nota de procedencia, con la fecha en que se escribió el documento. Resultado esperado: falla.
4. Correr la comprobación sobre un encuadre que deletrea la cadena en palabras, sin citar ningún identificador, y sobre un documento con su tabla de ficha antes del separador. Resultado esperado: ninguno de los dos se reprueba.
- **Aprobado cuando:** el caso que ya ocurrió, sustituir el encuadre por una nota de procedencia, deja de pasar en silencio, y ningún documento de otra plantilla se reprueba por esto.

### Criterios de aceptación transversales

- [ ] **Límites** — un documento vacío, uno sin encabezados y uno que no salió de ninguna plantilla tienen comportamiento definido.
- [ ] **Errores** — si la plantilla no se puede deducir, lo dice y no adivina.
- [ ] **No regresión** — un documento que ya pasaba sigue pasando.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Determinismo** | El mismo documento da siempre el mismo resultado |
| **Autonomía** | Corre sin internet y sin IA |
| **Mantenimiento** | La exigencia vive en la plantilla; el programa no la copia |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica, la salida es texto en la terminal.
- **Documento funcional:** [documentacion/epicas/EP-004-comprobacion-automatica/epica.md](../epica.md), §5.1.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Deducir de qué plantilla salió un documento a partir de su identificador.
- [ ] Comparar secciones y marcadores contra la plantilla.
- [ ] Comprobar que el plan declara su especificación y que la especificación existe.
- [ ] Comprobar que cada tarea cuelga de un criterio de aceptación.
- [ ] Escribir pruebas con documentos reales, incluidos los que se llenaron a medias.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-004-HU-004-la-regla-de-negocio-declara-su-origen](A-EP-004-HU-004-la-regla-de-negocio-declara-su-origen/README.md) | CA-04 | Cerrada 2026-08-16 (v22.1.0) |
| [B-EP-004-HU-004-el-encuadre-de-la-plantilla-sobrevive-al-llenado](B-EP-004-HU-004-el-encuadre-de-la-plantilla-sobrevive-al-llenado/plan_trabajo.md) | CA-05 | Abierta 2026-08-22. Sale del [pendiente 77](../../../../pendientes/hecho/el-planteamiento-conserva-su-encuadre.md) |

**Los tres primeros criterios no tienen fase:** las comprobaciones que los cumplen se escribieron antes de que la épica se descompusiera.

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
| Dependencia | HU-003, porque los hallazgos salen con la forma y la severidad ya definidas | Alto |
| Dependencia | EP-003, porque se comprueba contra los documentos modelo | Alto |
| Riesgo | Que un documento anterior a la plantilla se llene de hallazgos | Se reporta como aviso y se documenta que es correcto, no un falso positivo |
| Riesgo | Que la plantilla cambie y el programa quede viejo | El programa lee la plantilla, no la copia |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] La comprobación corre sobre un documento y sobre un árbol completo
- [ ] Compara contra la plantilla y no contra una copia interna
- [ ] Reporta marcadores, secciones, especificación y tareas sin criterio
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Parcial | Necesita la forma del hallazgo de HU-003 |
| **N**egociable | Sí | Qué es aviso y qué es falla se puede discutir |
| **V**aliosa | Sí | Evita aprobar documentos a medio llenar |
| **E**stimable | Sí | El alcance lo fijan las plantillas existentes |
| **S**mall (pequeña) | Parcial | Son varias plantillas |
| **T**esteable | Sí | Se prueba con documentos llenados a medias |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
| 2026-08-16 | Ing. José Dúmar Jiménez Ruíz | Nace el `CA-04`, del pendiente 43: una regla de negocio sin procedencia se reporta. Al construirlo se vio que un `spec.md` no se comparaba contra ninguna plantilla, y que las dos especificaciones de este repositorio traen 31 reglas sin origen |
