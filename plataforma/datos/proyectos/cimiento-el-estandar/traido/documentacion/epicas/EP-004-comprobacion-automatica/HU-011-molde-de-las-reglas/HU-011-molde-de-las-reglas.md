# HU-011 — Comprobar que cada regla del estándar cumple su propio molde

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-011 |
| **Épica / Feature** | [EP-004 Comprobación automática de lo que no admite discusión](../epica.md) |
| **Módulo / Componente** | Programas de comprobación |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Backlog |

---

## 2. Narrativa

- **Como** quien define el estándar
- **Quiero** que un programa revise las reglas contra el molde con el que se escriben
- **Para** que el estándar se cumpla a sí mismo, que es lo mínimo que se le puede pedir

---

## 3. Contexto y descripción

El estándar tiene un capítulo que dice cómo se escribe una regla: qué forma tiene el identificador, cuánto puede medir el cuerpo, qué marcas se admiten, cómo se declara que una regla se apoya en otra. Y tiene un checklist de veinte filas que se aplica a cada regla antes de publicarla.

Ese checklist dice, en su último apartado, cuáles de sus veinte filas puede decidir un programa: once. Las otras nueve piden leer y entender la regla.

Hoy esas once no las comprueba nadie, y se nota: hay reglas publicadas cuyo checklist quedó en "no cumple", reglas sin bloque de checklist, y capítulos enteros que no aparecen en el registro de clasificación. Nada de eso se descubre leyendo, porque son casi doscientas reglas.

La especificación de esta historia ya está escrita: son las once filas mecánicas, ni una más.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Se comprueban las once filas que el propio checklist declara mecánicas, y ninguna más |
| RN-02 | Lo que pide leer y entender no se simula: una comprobación que se equivoca vale menos que ninguna |
| RN-03 | El identificador de cada regla es único y su prefijo pertenece a un solo capítulo |
| RN-04 | Toda dependencia declarada apunta a una regla que existe, no da vueltas en círculo y no manda sobre una regla protegida |
| RN-05 | Toda regla trae su bloque de checklist, con resultado y con la versión contra la que se aplicó |
| RN-06 | La regla derogada se conserva y no se le exige lo mismo que a una vigente |
| RN-07 | Lo que está dentro de un bloque de ejemplo no es una regla, aunque lo parezca |

### 3.2 Supuestos

- El molde y el checklist ya están escritos y no cambian con esta historia.

### 3.3 Fuera de alcance

- Las nueve filas que piden criterio.
- Corregir las reglas que incumplan. Esto reporta.
- Escribir el criterio de qué es comprobable. Eso es HU-001.

---

## 4. Criterios de aceptación

### CA-01 — Un identificador repetido o con prefijo ajeno se reporta

```gherkin
Dado que cada capítulo tiene sus propias letras
Cuando una regla usa un prefijo de otro capítulo o repite un identificador
Entonces la comprobación lo reporta y nombra los capítulos en conflicto
```

**Cómo validarlo:**

1. Agregar en un capítulo de prueba una regla con el prefijo de otro capítulo.
2. Correr la comprobación de meta-reglas. Resultado esperado: reporta el prefijo y en qué capítulos aparece.
3. Corregir el prefijo y volver a correr. Resultado esperado: no reporta nada.
- **Aprobado cuando:** el conflicto se reporta con los capítulos nombrados.

### CA-02 — Una dependencia que no existe o que manda hacia arriba se reporta

```gherkin
Dado que una regla declara que extiende, depende de o deroga a otra
Cuando la regla citada no existe, o está protegida y la que la cita no lo está
Entonces la comprobación lo reporta
```

**Cómo validarlo:**

1. Escribir en una regla de prueba una dependencia a un identificador inventado.
2. Correr. Resultado esperado: reporta que esa regla no existe.
3. Cambiarla por una dependencia que extienda una regla protegida. Resultado esperado: reporta que no se puede mandar sobre una regla protegida.
4. Escribir dos reglas que dependan una de la otra. Resultado esperado: reporta el círculo.
- **Aprobado cuando:** los tres casos se reportan por separado.

### CA-03 — Una regla sin su checklist se reporta

```gherkin
Dado que toda regla se publica con su checklist aplicado
Cuando una regla no trae el bloque, o lo trae en "no cumple"
Entonces la comprobación lo reporta, y distingue los dos casos
```

**Cómo validarlo:**

1. Correr la comprobación sobre el cuerpo de reglas actual.
2. Leer la salida. Resultado esperado: separa las reglas sin bloque de las que lo traen en "no cumple".
3. Tomar una regla derogada. Resultado esperado: no se le exige el bloque.
- **Aprobado cuando:** los dos casos se distinguen y la derogada queda fuera.

### CA-04 — Una regla que nombra una tecnología se reporta

```gherkin
Dado que la base sirve a cualquier proyecto
Cuando una regla nombra un lenguaje, un marco de trabajo, un motor o una herramienta
Entonces la comprobación lo reporta con la palabra encontrada
```

**Cómo validarlo:**

1. Correr la comprobación sobre el cuerpo de reglas.
2. Leer los hallazgos de esta familia. Resultado esperado: cada uno nombra la palabra concreta y la línea.
3. Comprobar que no reporta lo que está dentro de un ejemplo. Resultado esperado: los ejemplos no se marcan.
- **Aprobado cuando:** reporta el cuerpo de la regla y no sus ejemplos.

### CA-05 — Una regla del proyecto sin respaldo en la base se reporta

```gherkin
Dado que un proyecto tiene su catálogo de reglas propias
Cuando una de ellas no declara la regla de la base que concreta
Entonces la comprobación lo reporta
Y también reporta la que cita una regla de la base que no existe
```

**Cómo validarlo:**

1. En un proyecto de prueba, escribir una regla propia sin su respaldo.
2. Correr la comprobación sobre el catálogo del proyecto. Resultado esperado: la reporta por su número.
3. Agregarle un respaldo que cite un identificador inventado. Resultado esperado: reporta que esa regla de la base no existe.
4. Citar una regla real y volver a correr. Resultado esperado: no reporta nada.
- **Aprobado cuando:** los dos casos se reportan y el respaldo correcto pasa.

### Criterios de aceptación transversales

- [ ] **Límites** — un capítulo sin reglas, una regla sin cuerpo y un anexo que se parece a una regla tienen comportamiento definido.
- [ ] **No regresión** — la comprobación de citas que ya existía sigue funcionando igual.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Determinismo** | El mismo cuerpo de reglas da el mismo resultado |
| **Autonomía** | Corre en seco sobre el estándar, sin ningún proyecto |
| **Claridad** | Cada hallazgo nombra la fila del checklist que respalda la comprobación |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica, la salida es texto en la terminal.
- **Documento funcional:** el checklist del estándar, §4, que enumera las once filas mecánicas.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Leer el cuerpo de reglas y armar el índice de todas, saltando los ejemplos.
- [ ] Comprobar identificador, prefijo y letras registradas.
- [ ] Comprobar forma del encabezado, marca y tamaño del cuerpo.
- [ ] Comprobar dependencias: que existan, que no den vueltas y que no manden hacia arriba.
- [ ] Comprobar el bloque de checklist de cada regla.
- [ ] Comprobar que la versión declarada tiene su entrada en el registro de cambios.
- [ ] Comprobar el catálogo de reglas propias de un proyecto.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-004-HU-011-la-comprobacion-del-molde-se-puede-correr](A-EP-004-HU-011-la-comprobacion-del-molde-se-puede-correr/README.md) | CA-01, CA-02, CA-03, CA-04 y CA-05 | Abierta 2026-08-17, con su plan de trabajo escrito y sin aprobar |

**Mitad retro-documentación, mitad construcción.** El programa está escrito y comprueba once de las veinte filas del checklist — incluida la que impide que una regla normal mande sobre una blindada. Lo que falta es **poder correrlo**: hoy calla y sale con código 0.

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
| Dependencia | HU-002, porque una de las filas comprueba que la regla esté clasificada | Alto |
| Dependencia | HU-003, porque los hallazgos salen con la forma ya definida | Alto |
| Riesgo | Que la medida del tamaño del cuerpo contradiga lo que el procedimiento ya aprobó | El límite se calibra contra las reglas que ya pasaron el checklist |
| Riesgo | Que la lista de tecnologías marque palabras que el estándar ya adoptó como concepto | La lista se mantiene corta y solo con nombres de producto |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] Las once filas mecánicas se comprueban
- [ ] Ninguna fila de criterio se simula
- [ ] La comprobación corre en seco y sobre el catálogo de un proyecto
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Parcial | Necesita el registro de clasificación de HU-002 |
| **N**egociable | Sí | El límite de tamaño del cuerpo se puede discutir |
| **V**aliosa | Sí | El estándar deja de depender de que alguien releá casi doscientas reglas |
| **E**stimable | Sí | La especificación son once filas ya escritas |
| **S**mall (pequeña) | Parcial | Once comprobaciones pequeñas |
| **T**esteable | Sí | Se prueba con reglas de prueba mal formadas a propósito |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde el checklist del estándar, §4 |
