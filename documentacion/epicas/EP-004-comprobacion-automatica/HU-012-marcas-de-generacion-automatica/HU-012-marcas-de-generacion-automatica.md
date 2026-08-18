# HU-012 — Comprobar las marcas de generación automática en lo que se entrega

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-012 |
| **Épica / Feature** | [EP-004 Comprobación automática de lo que no admite discusión](../epica.md) |
| **Módulo / Componente** | Programas de comprobación |
| **Tipo** | Técnica |
| **Prioridad** | Should |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Backlog |

---

## 2. Narrativa

- **Como** quien entrega un documento escrito con ayuda de una IA
- **Quiero** que un programa cuente las marcas que delatan que lo escribió una máquina
- **Para** releer solo lo que hace falta, en vez de todo el documento

---

## 3. Contexto y descripción

El estándar tiene una lista cerrada de marcas que hacen que un texto se lea como escrito por una máquina. La lista misma dice cuáles de esas marcas puede contar un programa: las de puntuación y tipografía, y las invisibles, que no se ven leyendo y sobreviven a cualquier reescritura.

Lo demás de la lista es criterio: que las secciones tengan todas el mismo tamaño, que el tono no cambie respecto de lo escrito antes, que no haya opinión propia. Eso lo decide quien lee.

Hoy nadie cuenta ni siquiera las mecánicas, y son las más fáciles: una raya larga usada como inciso, un espacio duro, unas comillas curvas mezcladas con rectas. Son marcas que quedan invisibles y que aparecen en cada documento entregado.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Se cuentan solo las marcas que la propia lista declara contables |
| RN-02 | Los bloques de código, la salida de herramientas y las citas no se revisan |
| RN-03 | La notación que el estándar define no es una marca: la cita por identificador, las marcas de regla y los símbolos del resultado del checklist |
| RN-04 | Todo hallazgo es aviso: quitar una marca puede volver el texto confuso, y ahí manda escribir claro |
| RN-05 | La comprobación se corre sobre el documento que se va a entregar, no sobre todo el repositorio |

### 3.2 Supuestos

- La lista de marcas ya está escrita y es cerrada. Esta historia no la amplía.

### 3.3 Fuera de alcance

- Reescribir el texto. Reporta y no corrige.
- Las marcas que piden leer y entender.
- Juzgar si el texto está bien escrito. Eso es criterio.

---

## 4. Criterios de aceptación

### CA-01 — Las marcas de tipografía se cuentan

```gherkin
Dado que un documento trae rayas largas usadas como inciso y comillas mezcladas
Cuando se corre la comprobación sobre ese documento
Entonces cada marca se reporta con su línea y con qué se escribe en su lugar
```

**Cómo validarlo:**

1. Escribir un documento de prueba con tres rayas largas como inciso y con comillas curvas mezcladas con rectas.
2. Correr la comprobación sobre ese archivo. Resultado esperado: reporta cada caso con su línea.
3. Leer el mensaje. Resultado esperado: dice con qué se reemplaza cada marca.
- **Aprobado cuando:** las marcas se cuentan y el mensaje dice qué poner en su lugar.

### CA-02 — Las marcas invisibles se encuentran

```gherkin
Dado que un documento trae un espacio duro y un carácter de ancho cero
Cuando se corre la comprobación
Entonces los reporta, aunque no se vean al leer
```

**Cómo validarlo:**

1. Insertar en el documento de prueba un espacio duro entre dos palabras y un carácter de ancho cero.
2. Correr la comprobación. Resultado esperado: reporta los dos, con su línea y su posición.
3. Reemplazarlos por espacio normal y quitar el invisible. Resultado esperado: no reporta nada.
- **Aprobado cuando:** encuentra lo que no se ve leyendo.

### CA-03 — La notación del estándar no se cuenta como marca

```gherkin
Dado que un documento del estándar usa la cita por identificador y las marcas de regla
Cuando se corre la comprobación
Entonces no las reporta
```

**Cómo validarlo:**

1. Tomar una regla del estándar que use la cita por identificador y traiga una marca de regla.
2. Correr la comprobación sobre ese archivo. Resultado esperado: no reporta esos símbolos.
3. Comprobar que sí reporta una raya larga en el mismo archivo, si la hay. Resultado esperado: la reporta.
- **Aprobado cuando:** distingue la notación acordada del adorno.

### Criterios de aceptación transversales

- [ ] **Límites** — un documento sin texto, uno que es solo código y uno con una tabla larga tienen comportamiento definido.
- [ ] **No regresión** — la comprobación no cambia el archivo revisado.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Determinismo** | El mismo documento da la misma cuenta |
| **Claridad** | El mensaje dice qué se escribe en lugar de la marca |
| **Alcance** | Corre sobre los archivos que se le indican, no sobre el repositorio entero |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica, la salida es texto en la terminal.
- **Documento funcional:** la lista de marcadores del capítulo de identidad y rol, secciones 2 y 3, que son las que la propia lista declara contables.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Escribir la comprobación de las marcas de puntuación y tipografía.
- [ ] Escribir la comprobación de las marcas invisibles.
- [ ] Excluir bloques de código, salida de herramientas y la notación del estándar.
- [ ] Definir cómo se le indican los archivos a revisar.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-004-HU-012-contar-las-marcas-de-generacion-automatica](A-EP-004-HU-012-contar-las-marcas-de-generacion-automatica/README.md) | CA-01, CA-02 y CA-03 | **Cerrada 2026-08-18** · Cumple · 16 477 marcas contadas, 4 491 en lo que se hereda |

**La fase construye.** La exigencia existe —`00·ID8` y su lista— y ningún programa la comprueba. Lo que decide si sirve es el CA-03: el estándar usa a propósito el punto medio y las comillas angulares, y un programa ingenuo reportaría casi cada línea.

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
| Dependencia | HU-003, porque los hallazgos salen con la forma ya definida | Alto |
| Riesgo | Que se corra sobre todo el repositorio y sepulte la salida en avisos | Se corre sobre los archivos que se indican |
| Riesgo | Que se marque la notación que el estándar definió | Las excepciones están escritas en la propia lista y se respetan |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] Las marcas contables se cuentan
- [ ] La notación del estándar no se marca
- [ ] La comprobación se corre sobre archivos indicados
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Parcial | Necesita la forma del hallazgo de HU-003 |
| **N**egociable | Sí | Qué marcas entran se puede discutir dentro de lo que la lista declara contable |
| **V**aliosa | Sí | Releer un documento entero cuesta; revisar diez avisos, no |
| **E**stimable | Sí | El alcance lo fija la lista |
| **S**mall (pequeña) | Sí | Dos familias de marcas |
| **T**esteable | Sí | Se prueba con un documento sembrado de marcas |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la lista de marcadores |
