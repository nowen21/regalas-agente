# HU-006 — La capa propia de cada proyecto

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-006 |
| **Épica** | [EP-001 Cuerpo de reglas heredable y en capas](../epica.md) |
| **Componente** | Capa de proyecto |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Solicitante** | Quien administra un proyecto |
| **Estado** | Pendiente |
## 2. Narrativa

- **Como** quien administra un proyecto con su lenguaje, su dominio y su cliente
- **Quiero** poder declarar lo propio de ese proyecto sin editar el cuerpo central
- **Para** que mis ajustes no le lleguen a los demás proyectos ni se pierdan cuando el cuerpo central cambie

## 3. Contexto y descripción

El cuerpo central no puede saber que este proyecto usa cierto lenguaje, que aquel cliente redondea de cierta forma, o que en el otro las tablas se nombran de cierta manera. Eso es de cada proyecto.

Si esos ajustes se escriben dentro del cuerpo central, se contaminan todos los proyectos. Y si se escriben en cualquier lado del proyecto, nadie sabe dónde buscarlos. Esta historia define el lugar y la forma.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Los ajustes del proyecto se declaran en el proyecto, nunca en el cuerpo central |
| RN-02 | Toda regla propia de un proyecto nombra la regla de la base que concreta |
| RN-03 | La capa del proyecto ajusta las convenciones, nunca el núcleo |
| RN-04 | El proyecto declara qué versión del cuerpo central adoptó |
| RN-05 | Lo que aplica a cualquier proyecto no se escribe acá: se propone para el cuerpo central |

### 3.2 Supuestos

- Cada proyecto tiene un lugar propio bajo control de versiones donde escribir su capa.

### 3.3 Fuera de alcance

- El contenido de la capa de un proyecto real.
- Llevar los documentos modelo al proyecto. Eso es EP-007.
- Avisar cuando el proyecto quedó atrás en versión. Eso es EP-002.

## 4. Criterios de aceptación

### CA-01 — Un ajuste del proyecto manda sobre la convención general

```gherkin
Dado que existe una convención general ajustable
Cuando el proyecto declara en su capa propia un ajuste a esa convención, nombrándola
Entonces dentro de ese proyecto manda el ajuste
Y el cuerpo central queda intacto
```

**Cómo validarlo:**

1. Ubicar una convención general ajustable y anotar qué exige.
2. En el proyecto de prueba, escribir en su capa propia un ajuste a esa convención, nombrando cuál concreta. Resultado esperado: queda escrito el ajuste y a qué regla se refiere.
3. Preguntarle a la IA dentro de ese proyecto qué exige ese tema. Resultado esperado: responde según el ajuste del proyecto.
4. Revisar el cuerpo central. Resultado esperado: no se editó ningún archivo suyo.
- **Aprobado cuando:** el ajuste manda dentro del proyecto y el cuerpo central no cambió.

### CA-02 — Una regla propia sin respaldo no se acepta

```gherkin
Dado que toda regla propia debe nombrar la regla de la base que concreta
Cuando alguien escribe una regla propia que no nombra ninguna
Entonces al revisarla se detecta que le falta el respaldo
```

**Cómo validarlo:**

1. Escribir en la capa del proyecto una regla propia sin decir qué regla de la base concreta.
2. Revisarla contra la exigencia de respaldo. Resultado esperado: se señala que falta.
3. Agregarle el nombre de la regla de la base que concreta. Resultado esperado: ahora pasa.
- **Aprobado cuando:** la falta se ve antes de aceptar la regla, y agregar el respaldo la resuelve.

### CA-03 — Un ajuste que contradice el núcleo no aplica

```gherkin
Dado que la capa del proyecto solo ajusta convenciones
Cuando el proyecto declara un ajuste que contradice una regla del núcleo
Entonces sigue mandando el núcleo
```

**Cómo validarlo:**

1. Escribir en la capa del proyecto un ajuste que contradiga una regla del núcleo.
2. Preguntarle a la IA dentro del proyecto si puede hacer lo que el ajuste permite. Resultado esperado: responde que no y nombra la regla del núcleo.
3. Revisar si el ajuste quedó marcado como inaplicable. Resultado esperado: la respuesta lo dice.
- **Aprobado cuando:** el núcleo gana y la respuesta explica por qué.

### Criterios de aceptación transversales

- [ ] **Validación** — una capa de proyecto incompleta se detecta al revisarla, y dice qué falta.
- [ ] **No regresión** — un cambio en el cuerpo central no borra ni pisa lo que el proyecto escribió.

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| Aislamiento | Lo del proyecto no llega a otros proyectos |
| Trazabilidad | Toda regla propia apunta a la de la base que concreta |
| Portabilidad | El mecanismo sirve igual sin importar el lenguaje del proyecto |

## 6. Tareas técnicas derivadas

- [ ] Definir dónde vive la capa propia dentro del proyecto.
- [ ] Definir qué declara: precedencia, versión adoptada, ajustes y punteros a sus anexos.
- [ ] Escribir la exigencia de que toda regla propia nombre la regla de la base que concreta.
- [ ] Escribir qué hacer cuando un ajuste sirve a todos: proponerlo para el cuerpo central.

## 7. Fases que la implementan

> Trazabilidad hacia abajo. Se completa a medida que la historia se descompone en fases (`02·F12.2`). El enlace se escribe en los dos lados: la fase declara qué criterios cubre y acá se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
**Ejecutada el 2026-08-22.** Veredicto: [**No cumple**](A-EP-001-HU-006-retrodocumentar-la-capa-del-proyecto/resultado_pruebas.md#6-veredicto-de-la-fase) — el CA-01 y el CA-02 sí; el CA-03 no se pudo provocar sin escribir contra el núcleo en un proyecto real. Se probó sobre **AgroSystem**, no sobre el proyecto propuesto |

**La fase retro-documenta y no toca `base/` ni `plantillas/`.** La capa propia existe, tiene su molde y su regla de respaldo. Lo que falta es probar el desempate — que el ajuste propio gane a la convención general y pierda contra el núcleo — y decir que la comprobación de `20·M16` hoy no se puede correr.

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
| Dependencia | HU-002, por la precedencia entre capas | Alto |
| Dependencia | HU-005, porque lo que se ajusta son las convenciones | Alto |
| Riesgo | Que en la capa del proyecto se escriba lo que debía ir en el cuerpo central | La exigencia de nombrar la regla que concreta lo hace evidente |
| Riesgo | Que dos proyectos ajusten lo mismo de forma distinta y nadie lo note | Cada uno declara su ajuste; comparar es posible porque están en el mismo lugar |

## 9. Definition of Ready

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y verificables
- [ ] Ubicación de la capa propia acordada
- [ ] Dependencias identificadas

## 10. Definition of Done

- [ ] Está definido dónde vive y qué declara la capa propia
- [ ] Está escrita la exigencia de respaldo de toda regla propia
- [ ] Un proyecto de prueba tiene su capa y sus ajustes mandan
- [ ] Todos los criterios de aceptación verificados

## 11. Validación INVEST

| Criterio | Cumple | Observación |
|---|:--:|---|
| Independiente | Parcial | Necesita capas y convenciones |
| Negociable | Sí | Qué declara la capa se discute |
| Valiosa | Sí | Sin esto, o se contamina el cuerpo central o los ajustes se pierden |
| Estimable | Sí | Alcance acotado |
| Pequeña | Sí | Un mecanismo y su documento |
| Testeable | Sí | Se verifica con un proyecto de prueba |

## 12. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-13 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
