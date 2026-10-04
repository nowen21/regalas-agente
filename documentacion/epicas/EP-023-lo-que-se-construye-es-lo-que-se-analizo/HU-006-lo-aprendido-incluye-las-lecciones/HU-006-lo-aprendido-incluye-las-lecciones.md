# HU-006 · Lo aprendido incluye las lecciones

> Su criterio sale de «Lo que se tiene que hacer» del [análisis 1](../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-1.md), punto 9, y del [análisis 8](../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-8.md), punto 6. Los campos que no son alcance (módulo, tipo, estimación y responsable) son propuesta del agente y esperan la aprobación del usuario.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-006 |
| **Épica / Feature** | [EP-023 Lo que se construye es lo que se analizó](../epica.md) |
| **Módulo / Componente** | `memoria/`, `plantillas/` |
| **Tipo** | Técnica |
| **Prioridad** | Orden 7 de 7 |
| **Estimación** | S |
| **Sprint** | N/A |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | Claude |
| **Estado** | Terminada el 2026-10-03, con sus criterios probados |

---

## 2. Narrativa

- **Como** el usuario, que plantea la necesidad y aprueba (análisis 1, conclusión 40)
- **Quiero** que lo aprendido incluya las lecciones
- **Para** que al ejecutar un plan solo aparezcan los hallazgos que no se podían prever

---

## 3. Contexto y descripción

Esta HU no resuelve una frase del [problema de la épica](../epica.md#31-situación-actual): ataca su «por qué importa», para que los hallazgos que se podían evitar no se repitan ([análisis 4](../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-4.md), conclusión 4).

### 3.1 Reglas de negocio

Es la conclusión de la que sale el punto de esta HU.

| ID | Regla | Sale de |
|---|---|---|
| RN-01 | La señal habla del proyecto y la lección, de cómo se analizó. La lección sale tanto de lo que funcionó como de lo que falló. Se escribe en el almacén de señales con su propia categoría y el análisis la enlaza | Análisis 1, conclusión 13 |

### 3.2 Supuestos

Ninguno.

### 3.3 Fuera de alcance

- Los puntos que la propuesta final reparte a las otras HU.

---

## 4. Criterios de aceptación

### CA-01 · La lección aprendida tiene su categoría y el análisis la enlaza

**Sale de:** análisis 1, punto 9.

```gherkin
Dado el almacén de señales
Cuando se escribe una lección aprendida
Entonces queda con su propia categoría
Y la tabla de lecciones del análisis la enlaza
```

**Cómo validarlo:**
1. Buscar la categoría de lección en `memoria/memoria.py`.
2. Escribir una lección y abrir el análisis que la cita.

**Aprobado cuando:** la categoría existe y el análisis enlaza la lección.

### CA-02 · Las lecciones alimentan las recomendaciones

**Sale de:** análisis 8, punto 6.

```gherkin
Dada la tabla de lecciones del análisis
Entonces cada lección dice si complementa una recomendación, crea una nueva o no aplica
Y antes de crear una se busca si ya existe
```

**Cómo validarlo:**
1. Abrir la tabla de lecciones de la plantilla del análisis.
2. Llenarla con una lección que complementa una recomendación.

**Aprobado cuando:** la columna existe y la recomendación queda complementada, sin una nueva repetida.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | N/A |
| RNF-02 | **Seguridad** | N/A |
| RNF-03 | **Auditoría** | N/A |
| RNF-04 | **Accesibilidad** | N/A |
| RNF-05 | **Compatibilidad** | N/A |
| RNF-06 | **Trazabilidad** | El criterio cita el punto de lo que se tiene que hacer del que sale (análisis 1, conclusión 39) |

---

## 6. Diseño y referencias

| Campo | Valor |
|---|---|
| Documento funcional | [análisis 1](../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-1.md) |
| Mockup / Prototipo | N/A |
| Contrato de API | N/A |

---

## 7. Tareas técnicas derivadas

Las fija el plan de cada fase (`02·F14`).

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| [`A-EP-023-HU-006-la-leccion-tiene-su-categoria-y-alimenta-las-recomendaciones`](A-EP-023-HU-006-la-leccion-tiene-su-categoria-y-alimenta-las-recomendaciones/estado-fase.md) | CA-01, CA-02 | HU-001 | [plan](A-EP-023-HU-006-la-leccion-tiene-su-categoria-y-alimenta-las-recomendaciones/plan_trabajo.md) | [pruebas](A-EP-023-HU-006-la-leccion-tiene-su-categoria-y-alimenta-las-recomendaciones/plan_pruebas.md) | [resultado](A-EP-023-HU-006-la-leccion-tiene-su-categoria-y-alimenta-las-recomendaciones/resultado_pruebas.md) | Cumple |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-001: las demás HU se apoyan en el análisis | Bloqueante |
| Dependencia | HU-001, fase D: crea las recomendaciones que las lecciones alimentan | Bloqueante |

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

- [ ] El criterio de aceptación verificado
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
| **S**mall (pequeña) | ✅ | Un criterio |
| **T**esteable | ✅ | El criterio dice dónde mirar |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-01 | Claude, por pedido de Ing. José Dúmar Jiménez Ruíz | Creación de la HU |
| 2026-10-01 | Claude, por pedido de Ing. José Dúmar Jiménez Ruíz | El contexto dice la parte del problema de la épica que resuelve, según el análisis 4 |
| 2026-10-01 | Ing. José Dúmar Jiménez Ruíz | **Aprobada** |
| 2026-10-02 | Claude, por pedido de Ing. José Dúmar Jiménez Ruíz | Nace el CA-02, las lecciones alimentan las recomendaciones; depende de la fase D de la HU-001, según el análisis 8. La aprobación queda sin efecto hasta que se revise |
| 2026-10-02 | Ing. José Dúmar Jiménez Ruíz | **Aprobada**, con los cambios del análisis 8 |
