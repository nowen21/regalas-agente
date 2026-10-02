# HU-002 · Cada documento sale del anterior

> Sus criterios salen de «Lo que se tiene que hacer» del [análisis 1](../103-cada-documento-de-la-cadena-sale-del-anterior/analisis-1.md), puntos 4 y 5, y del [análisis 4](../103-cada-documento-de-la-cadena-sale-del-anterior/analisis-4.md), punto 1. Los campos que no son alcance (módulo, tipo, estimación y responsable) son propuesta del agente y esperan la aprobación del usuario.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-002 |
| **Épica / Feature** | [EP-023 Lo que se construye es lo que se analizó](../epica.md) |
| **Módulo / Componente** | `base/02-flujo-de-trabajo/`, `validadores/` |
| **Tipo** | Técnica |
| **Prioridad** | Orden 3 de 7 |
| **Estimación** | S |
| **Sprint** | N/A |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | Claude |
| **Estado** | Lista: aprobada el 2026-10-01 |

---

## 2. Narrativa

- **Como** el usuario, que plantea la necesidad y aprueba (análisis 1, conclusión 40)
- **Quiero** que cada documento salga del anterior
- **Para** que al ejecutar un plan solo aparezcan los hallazgos que no se podían prever

---

## 3. Contexto y descripción

Del [problema de la épica](../epica.md#31-situación-actual), esta HU resuelve que nada obliga a que cada documento salga del anterior ([análisis 4](../103-cada-documento-de-la-cadena-sale-del-anterior/analisis-4.md), conclusión 4).

### 3.1 Reglas de negocio

Son las conclusiones de las que salen los puntos de esta HU.

| ID | Regla | Sale de |
|---|---|---|
| RN-01 | Cada documento conserva lo del anterior y le agrega precisión, sin cambiarlo. Lo que no sale del anterior no entra | Análisis 1, conclusión 6 |
| RN-02 | Si se pide la clase `Matematicas` con `suma`, se hace eso y nada más. El nombre de lo pedido no autoriza agregar lo que sugiere | Análisis 1, conclusión 7 |
| RN-03 | Si cambia la necesidad, el cambio se aplica en el documento donde nace y baja en orden: épica, HU, especificación y plan | Análisis 1, conclusión 8 |
| RN-04 | La secuencia lógica va en una regla nueva que extiende `02·F18`; `F18` no se toca | Análisis 1, conclusión 28 |
| RN-05 | Cada punto lleva «Sale de»: el pendiente, su hallazgo; la conclusión, el turno; el criterio de la HU, el punto de lo que se tiene que hacer; la tarea del plan, el criterio. Lo que no tenga origen se detiene | Análisis 1, conclusión 39 |

### 3.2 Supuestos

Ninguno.

### 3.3 Fuera de alcance

- Los puntos que la propuesta final reparte a las otras HU.

---

## 4. Criterios de aceptación

### CA-01 · Cada punto cita su origen, y un validador sigue la cadena

**Sale de:** análisis 1, punto 4.

```gherkin
Dado un documento de la cadena
Cuando un punto no tiene «Sale de», o cita un punto que no existe en el documento anterior
Entonces el validador lo detiene
Y si todos los puntos citan un origen que existe, pasa
```

**Cómo validarlo:**
1. Leer la regla nueva que extiende [`02·F18`](../../../../base/02-flujo-de-trabajo/reglas/F18-deriva-el-plan-de-los-ca-aprobados-no-de-la-proactividad.md).
2. Correr el validador sobre un documento con todos sus orígenes, uno con un punto sin «Sale de» y uno con una cita a un punto que no existe.

**Aprobado cuando:** la regla exige «Sale de», el primer documento pasa y los otros dos se detienen.

### CA-02 · El cambio se aplica donde nace y baja en orden

**Sale de:** análisis 1, punto 5.

```gherkin
Dado que cambia la necesidad
Cuando se lee lo que exige el estándar
Entonces el cambio se aplica en el documento donde nace y baja en orden
```

**Cómo validarlo:**
1. Buscar en `base/` la regla que lo exige.

**Aprobado cuando:** la regla existe y dice lo del criterio.

### CA-03 · La plantilla de la HU distingue de dónde sale su contexto

**Sale de:** análisis 4, punto 1.

```gherkin
Dada la plantilla de la HU
Cuando se lee su sección «Contexto y descripción»
Entonces dice que, si la HU sale directo de un pendiente, el contexto es el problema del pendiente
Y que, si sale de una épica, es la parte del problema de la épica que le toca, con el enlace a la épica
```

**Cómo validarlo:**
1. Abrir [`04-HU.md`](../../../../plantillas/ciclo-vida-proyectos/04-HU.md).

**Aprobado cuando:** la sección pide lo del criterio para los dos casos.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | N/A |
| RNF-02 | **Seguridad** | N/A |
| RNF-03 | **Auditoría** | N/A |
| RNF-04 | **Accesibilidad** | N/A |
| RNF-05 | **Compatibilidad** | N/A |
| RNF-06 | **Trazabilidad** | Cada criterio cita el punto de lo que se tiene que hacer del que sale (análisis 1, conclusión 39) |

---

## 6. Diseño y referencias

| Campo | Valor |
|---|---|
| Documento funcional | [análisis 1](../103-cada-documento-de-la-cadena-sale-del-anterior/analisis-1.md). |
| Mockup / Prototipo | N/A |
| Contrato de API | N/A |

---

## 7. Tareas técnicas derivadas

Las fija el plan de cada fase (`02·F14`).

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| N/A: todavía no se descompone en fases | | | | | | |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-001: las demás HU se apoyan en el análisis | Bloqueante |

---

## 10. Precondiciones  (Definition of Ready - DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [ ] Diseño / mockup disponible: N/A
- [ ] Dependencias identificadas y desbloqueadas: depende de la HU-001
- [x] Estimada
- [ ] Cumple criterios INVEST: no es independiente

## 11. Poscondiciones (Definition of Done - DoD)

- [ ] Todos los criterios de aceptación verificados
- [ ] Pruebas pasando
- [ ] `VERSION` y `CHANGELOG.md` actualizados
- [ ] Aceptada por el usuario

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | ☐ | Depende de la HU-001 |
| **N**egociable | ✅ | |
| **V**aliosa | ✅ | |
| **E**stimable | ✅ | Talla S |
| **S**mall (pequeña) | ✅ | Tres criterios |
| **T**esteable | ✅ | Cada criterio dice dónde mirar |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-01 | Claude, por pedido de Ing. José Dúmar Jiménez Ruíz | Creación de la HU, corregida según el análisis 3 |
| 2026-10-01 | Claude, por pedido de Ing. José Dúmar Jiménez Ruíz | El contexto dice la parte del problema de la épica que resuelve, según el análisis 4 |
| 2026-10-01 | Ing. José Dúmar Jiménez Ruíz | **Aprobada** |
