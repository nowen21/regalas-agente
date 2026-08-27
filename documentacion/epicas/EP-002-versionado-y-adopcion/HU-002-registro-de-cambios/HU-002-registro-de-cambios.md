# HU-002 — Llevar el registro de qué cambió en cada versión

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-002 |
| **Épica / Feature** | [EP-002 Versionado de las reglas y adopción por proyecto](../epica.md) |
| **Módulo / Componente** | Versionado del estándar |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Terminada |
---

## 2. Narrativa

- **Como** quien tiene que decidir si actualiza su proyecto
- **Quiero** leer qué cambió en cada versión y por qué
- **Para** decidir con lo que dice el registro y no abriendo regla por regla

---

## 3. Contexto y descripción

El número dice que algo cambió, pero no qué. Quien tiene que decidir si adopta una versión nueva necesita saber qué se le va a exigir de más, y sobre todo por qué: un cambio sin motivo escrito se lee como capricho y no se adopta.

El registro también es el rastro. Cuando alguien pregunte dentro de un año por qué una regla dice lo que dice, la respuesta está ahí.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Toda versión tiene su entrada en el registro, sin excepción |
| RN-02 | La entrada dice versión, fecha, tipo de cambio, qué cambió y por qué |
| RN-03 | Cambiar una regla sin dejar entrada no se acepta |
| RN-04 | Las entradas no se borran ni se reescriben: el registro es rastro |
| RN-05 | La entrada nombra las reglas que cambiaron, por su identificador |
| RN-06 | Se escribe para que lo entienda quien no siguió el detalle del cambio |

### 3.2 Supuestos

- Quien cambia la regla es quien mejor puede explicar por qué. Si se deja para después, ya nadie se acuerda.

### 3.3 Fuera de alcance

- El número en sí. Eso es HU-001.
- Avisar a los proyectos. Eso es HU-004.

---

## 4. Criterios de aceptación

### CA-01 — Cada versión tiene su entrada

```gherkin
Dado que el número de versión subió
Cuando se busca esa versión en el registro
Entonces existe su entrada
Y dice qué cambió y por qué
```

**Cómo validarlo:**

1. Leer el número de versión vigente.
2. Buscarlo en el registro de cambios. Resultado esperado: hay una entrada con ese número.
3. Leerla. Resultado esperado: trae fecha, tipo de cambio, qué cambió y el motivo.
- **Aprobado cuando:** ninguna versión queda sin entrada.

### CA-02 — Un cambio sin entrada no pasa

```gherkin
Dado que se cambia una regla
Cuando no se agrega la entrada al registro
Entonces el cambio no se da por terminado
```

**Cómo validarlo:**

1. Cambiar una regla en una copia de prueba y no tocar el registro.
2. Revisar el procedimiento de cambio de regla. Resultado esperado: exige la entrada como paso, no como recomendación.
3. Correr la comprobación de versionado, si ya existe. Resultado esperado: reporta que falta la entrada.
- **Aprobado cuando:** el cambio sin registro se detecta.

### CA-03 — El registro se entiende sin haber seguido el cambio

```gherkin
Dado que existe una entrada del registro
Cuando la lee alguien que no participó del cambio
Entonces entiende qué le van a exigir de más y por qué
```

**Cómo validarlo:**

1. Tomar una entrada cualquiera del registro.
2. Dársela a leer a alguien que no siguió ese cambio. Resultado esperado: puede decir con sus palabras qué cambió y si le obliga a algo.
3. Preguntarle qué haría con su proyecto. Resultado esperado: responde sin abrir las reglas.
- **Aprobado cuando:** la entrada alcanza para decidir.

### Criterios de aceptación transversales

- [ ] **Límites** — una versión que solo corrige redacción también deja entrada, aunque sea corta.
- [ ] **No regresión** — las entradas viejas no se modifican al agregar una nueva.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Claridad** | Se entiende sin haber seguido el cambio |
| **Trazabilidad** | Cada entrada nombra las reglas tocadas por su identificador |
| **Permanencia** | Las entradas no se borran |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica, es un archivo de texto.
- **Documento funcional:** [documentacion/epicas/EP-002-versionado-y-adopcion/epica.md](../epica.md), §5.4 filas 4 y 15.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Definir el archivo del registro y el orden de las entradas.
- [ ] Definir los campos de una entrada.
- [ ] Sumar la entrada al procedimiento de cambiar una regla.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
**Ejecutada el 2026-08-22.** Veredicto: [**Cumple**](A-EP-002-HU-002-retrodocumentar-el-registro-de-cambios/resultado_pruebas.md) — y la comprobación reprobó una entrada escrita ese mismo día |
| [B-EP-002-HU-002-la-entrada-se-entiende-sin-conocer-el-proyecto](B-EP-002-HU-002-la-entrada-se-entiende-sin-conocer-el-proyecto/README.md) | CA-03 | Cerrada 2026-08-18 (v23.9.0) |

**La fase retro-documenta y no toca el registro.** Y trae un hallazgo: el CA-02 —«un cambio sin entrada no pasa»— hoy no lo impide nada. La fila 19 del checklist lo decidiría, y su programa no se puede correr.

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
| Dependencia | HU-001, porque la entrada se identifica por el número | Alto |
| Riesgo | Que las entradas se escriban en jerga y no sirvan para decidir | Se exige el porqué, no solo el qué |
| Riesgo | Que el registro se llene al final del día, de memoria | La entrada va en el mismo movimiento del cambio |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] El registro existe y tiene una entrada por versión
- [ ] La entrada trae sus campos definidos
- [ ] El procedimiento de cambiar una regla exige la entrada
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Parcial | Necesita el número de HU-001 |
| **N**egociable | Sí | Los campos de la entrada se pueden discutir |
| **V**aliosa | Sí | Sin él, adoptar una versión es a ciegas |
| **E**stimable | Sí | Alcance corto |
| **S**mall (pequeña) | Sí | Un archivo y un formato |
| **T**esteable | Sí | Se prueba leyendo entradas reales |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
