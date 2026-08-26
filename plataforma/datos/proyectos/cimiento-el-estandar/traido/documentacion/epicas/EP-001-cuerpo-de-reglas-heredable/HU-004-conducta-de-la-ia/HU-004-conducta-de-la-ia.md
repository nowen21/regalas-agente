# HU-004 — Reglas de conducta de la IA

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-004 |
| **Épica** | [EP-001 Cuerpo de reglas heredable y en capas](../epica.md) |
| **Componente** | Cuerpo de reglas |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Solicitante** | Quien trabaja con la IA |
| **Estado** | Backlog |

## 2. Narrativa

- **Como** quien trabaja con la IA todos los días
- **Quiero** que esté escrito cómo debe comportarse
- **Para** no tener que corregirle lo mismo en cada chat

## 3. Contexto y descripción

El núcleo dice lo que no puede hacer. Falta lo otro: cómo se comporta cuando sí puede. Si pregunta o asume, si responde largo o corto, en qué idioma escribe, qué hace cuando encuentra un defecto, qué hace cuando el usuario le pide algo que contradice lo que ya se decidió.

Sin eso escrito, cada sesión tiene un carácter distinto y la persona pasa el día corrigiendo la forma en vez de revisar el fondo.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Trabaja con criterio de alguien con experiencia: recomienda, con el motivo |
| RN-02 | Cuando el usuario pregunta, responde. No toma la pregunta como una orden de hacer |
| RN-03 | Lo que detecta mal, lo arregla. No pregunta si lo arregla |
| RN-04 | Escribe en el idioma del proyecto, para que lo entienda quien no sabe del tema |
| RN-05 | No entrega nada que se lea como escrito por una máquina |
| RN-06 | Dice lo que no sabe y lo que no pudo hacer |
| RN-07 | Lo que el usuario quiere recordado se guarda donde se pueda revisar, no en un almacén local |

### 3.2 Supuestos

- La IA lee estas reglas al abrir sesión y las tiene presentes durante toda la conversación.

### 3.3 Fuera de alcance

- Las reglas de ingeniería, que van en HU-005.
- Los procedimientos paso a paso de cada rol del trabajo. Eso es EP-003.
- Dónde se guarda lo aprendido. Eso es EP-006.

## 4. Criterios de aceptación

### CA-01 — Una pregunta se responde, no se ejecuta

```gherkin
Dado que existe la regla que distingue una pregunta de una orden
Cuando el usuario pregunta si algo se puede hacer de otra forma
Entonces la IA responde en el chat
Y no modifica ningún archivo
```

**Cómo validarlo:**

1. Abrir una sesión en un proyecto de prueba y anotar qué archivos hay y cuándo se modificaron por última vez.
2. Preguntarle a la IA algo que suene a mejora, por ejemplo si conviene cambiar la forma de nombrar cierta carpeta. Resultado esperado: responde con su recomendación y el motivo.
3. Revisar de nuevo los archivos y sus fechas de modificación. Resultado esperado: ninguno cambió.
- **Aprobado cuando:** hubo respuesta y no hubo edición.

### CA-02 — Lo que se detecta mal se corrige sin preguntar

```gherkin
Dado que existe la regla que exige corregir el defecto detectado
Cuando la IA reporta que algo quedó mal en lo que ella misma hizo
Entonces lo corrige en el mismo momento
Y no pregunta si debe corregirlo
```

**Cómo validarlo:**

1. Pedirle a la IA que escriba un documento y luego que lo revise contra una regla concreta.
2. Leer su revisión. Resultado esperado: si señala algo mal, en la misma respuesta ya está corregido.
3. Abrir el documento. Resultado esperado: la corrección está aplicada.
- **Aprobado cuando:** no aparece la pregunta de si corregir, y la corrección está hecha.

### CA-03 — Lo entregado no se lee como escrito por una máquina

```gherkin
Dado que existe la regla y la lista de marcas que delatan generación automática
Cuando la IA entrega un documento para que lo lea una persona
Entonces el documento no trae esas marcas
```

**Cómo validarlo:**

1. Pedirle a la IA un documento de una página sobre cualquier tema del proyecto.
2. Revisar el documento contra la lista de marcas, sección por sección. Resultado esperado: no aparecen las muletillas, ni la puntuación delatora, ni la estructura pareja que la lista describe.
3. Buscar en el archivo los caracteres invisibles que la lista nombra. Resultado esperado: no hay ninguno.
- **Aprobado cuando:** ninguna sección de la lista encuentra ejemplos en el documento.

### Criterios de aceptación transversales

- [ ] **Errores** — cuando la IA no puede hacer algo, lo dice, con qué faltó.
- [ ] **Privacidad** — lo que se guarda como preferencia del usuario no incluye datos sensibles.

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| Legibilidad | Cada regla de conducta se entiende sin conocer el resto |
| Aplicabilidad | Cada regla se puede señalar en una respuesta concreta, para poder corregir citándola |

## 6. Tareas técnicas derivadas

- [ ] Escribir las reglas de conducta con el molde de HU-001.
- [ ] Escribir la lista de marcas que delatan generación automática, como anexo.
- [ ] Definir qué se considera una pregunta y qué una orden.
- [ ] Definir dónde queda lo que el usuario pide recordar.

## 7. Fases que la implementan

> Trazabilidad hacia abajo. Se completa a medida que la historia se descompone en fases (`02·F12.2`). El enlace se escribe en los dos lados: la fase declara qué criterios cubre y acá se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
**Ejecutada el 2026-08-22.** Veredicto: [**Cumple**](A-EP-001-HU-004-retrodocumentar-la-conducta-de-la-ia/resultado_pruebas.md) — los tres criterios con conducta real de la jornada, incluidos dos incumplimientos que quedaron reportados |

**La fase es mitad retro-documentación y mitad construcción.** Cinco de las siete reglas de negocio ya son regla del estándar. Las de la pregunta que no es orden y del defecto que se corrige sin preguntar **no lo son**: viven como preferencia del usuario en la memoria del repositorio, y subirlas a `base/` es decisión suya.

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
| Dependencia | HU-001, por el molde | Alto |
| Dependencia | HU-002, por la marca de capa | Medio |
| Riesgo | Que las reglas de conducta se contradigan entre ellas | Cada una declara de cuál depende |
| Riesgo | Que la lista de marcas se vuelva tan larga que nadie la aplique | Se ordena de la marca más fácil de ver a la más difícil |

## 9. Definition of Ready

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y verificables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 10. Definition of Done

- [ ] Las reglas de conducta están escritas con el molde
- [ ] La lista de marcas está escrita como anexo del capítulo
- [ ] Todos los criterios de aceptación verificados
- [ ] Ninguna regla de conducta depende de un lenguaje ni de un framework

## 11. Validación INVEST

| Criterio | Cumple | Observación |
|---|:--:|---|
| Independiente | Parcial | Necesita el molde |
| Negociable | Sí | El detalle de cada conducta se discute |
| Valiosa | Sí | Es lo que evita corregir lo mismo en cada chat |
| Estimable | Sí | Un capítulo y su anexo |
| Pequeña | Parcial | El anexo de marcas es largo, pero es una sola cosa |
| Testeable | Sí | Se verifica sobre respuestas reales |

## 12. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-13 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
