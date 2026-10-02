# HU-007 · Nada se escribe fuera del plan aprobado

> Sus criterios salen de «Lo que se tiene que hacer» del [análisis 1](../103-cada-documento-de-la-cadena-sale-del-anterior/analisis-1.md), puntos 25, 26, 27 y 31. Los campos que no son alcance (módulo, tipo, estimación y responsable) son propuesta del agente y esperan la aprobación del usuario.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-007 |
| **Épica / Feature** | [EP-023 Lo que se construye es lo que se analizó](../epica.md) |
| **Módulo / Componente** | `adaptadores/claude-code/`, `plantillas/`, `validadores/` |
| **Tipo** | Técnica |
| **Prioridad** | Orden 6 de 7: necesita que la HU-004 defina qué pasa con un hallazgo |
| **Estimación** | M |
| **Sprint** | N/A |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | Claude |
| **Estado** | Lista: aprobada el 2026-10-01 |

---

## 2. Narrativa

- **Como** el usuario, que plantea la necesidad y aprueba (análisis 1, conclusión 40)
- **Quiero** que nada se escriba fuera del plan aprobado
- **Para** que al ejecutar un plan solo aparezcan los hallazgos que no se podían prever

---

## 3. Contexto y descripción

Del [problema de la épica](../epica.md#31-situación-actual), esta HU resuelve que nada detiene al agente cuando trabaja fuera del plan aprobado, y la plantilla del plan no permite comprobarlo con un programa ([análisis 4](../103-cada-documento-de-la-cadena-sale-del-anterior/analisis-4.md), conclusión 4).

### 3.1 Reglas de negocio

Son las conclusiones de las que salen los puntos de esta HU.

| ID | Regla | Sale de |
|---|---|---|
| RN-01 | Cuando aparece un hallazgo, la ejecución se detiene en ese momento | Análisis 1, conclusión 18 |
| RN-02 | Lo que el pendiente 105 llamaba «ampliar el plan» se reemplaza por volver al análisis | Análisis 1, conclusión 44 |
| RN-03 | El freno solo detiene lo que no está autorizado en ninguna parte. Lee el plan aprobado y la lista de lo que las reglas autorizan, y cada entrada de esa lista cita la regla que la autoriza | Análisis 1, conclusión 46 |
| RN-04 | Lo que se construya llega a los proyectos que heredan por el instalador, y la lista de lo autorizado incluye las reglas propias de cada proyecto | Análisis 1, conclusión 47 |

### 3.2 Supuestos

Ninguno.

### 3.3 Fuera de alcance

- Los puntos que la propuesta final reparte a las otras HU.

---

## 4. Criterios de aceptación

### CA-01 · El plan solo acepta rutas exactas y dice quién lo aprobó

**Sale de:** análisis 1, punto 25.

```gherkin
Dado un plan de trabajo
Cuando su tabla de archivos trae una fila que no es una ruta exacta
Entonces no se acepta
Y el plan registra quién lo aprobó y cuándo
```

**Cómo validarlo:**
1. Abrir la plantilla del plan de trabajo en `plantillas/ciclo-vida-proyectos/`.
2. Correr el validador del plan sobre un plan con una fila que no es ruta.

**Aprobado cuando:** la plantilla pide quién aprobó y cuándo, y el validador rechaza la fila.

### CA-02 · El freno detiene lo que no está en el plan ni autorizado

**Sale de:** análisis 1, punto 26.

```gherkin
Dado un plan aprobado en la fase activa
Cuando se va a escribir un archivo o a correr pruebas que no coinciden con el plan
Entonces el freno detiene, anota el hallazgo en el resumen y vuelve al análisis
Y si una regla ya lo autoriza, según la lista donde cada entrada cita su regla, no lo frena
```

**Cómo validarlo:**
1. Con un plan aprobado, intentar escribir un archivo que el plan no declara.
2. Intentar escribir un archivo que la lista de lo autorizado incluye.

**Aprobado cuando:** el primero se detiene con su hallazgo anotado en el resumen y el segundo pasa.

### CA-03 · El commit se rechaza si trae archivos no declarados

**Sale de:** análisis 1, punto 27.

```gherkin
Dado un plan aprobado
Cuando el commit trae un archivo que el plan no declara
Entonces se rechaza
```

**Cómo validarlo:**
1. Intentar un commit con un archivo que el plan no declara.

**Aprobado cuando:** se rechaza.

### CA-04 · La lista de lo autorizado incluye las reglas de cada proyecto

**Sale de:** análisis 1, punto 31.

```gherkin
Dado un proyecto que hereda Cimiento, con reglas propias
Cuando el freno lee la lista de lo autorizado
Entonces la lista incluye lo que autorizan esas reglas
```

**Cómo validarlo:**
1. En un proyecto con una regla propia que autoriza escribir un archivo, intentar escribirlo.

**Aprobado cuando:** el freno no lo detiene.

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
| Documento funcional | [análisis 1](../103-cada-documento-de-la-cadena-sale-del-anterior/analisis-1.md) |
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
| Dependencia | HU-004: define qué pasa con un hallazgo | Bloqueante |

---

## 10. Precondiciones  (Definition of Ready - DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [ ] Diseño / mockup disponible: N/A
- [ ] Dependencias identificadas y desbloqueadas: depende de las HU 1 y 4
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
| **I**ndependiente | ☐ | Depende de las HU 1 y 4 |
| **N**egociable | ✅ | |
| **V**aliosa | ✅ | |
| **E**stimable | ✅ | Talla M |
| **S**mall (pequeña) | ✅ | Cuatro criterios |
| **T**esteable | ✅ | Cada criterio dice dónde mirar |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-01 | Claude, por pedido de Ing. José Dúmar Jiménez Ruíz | Creación de la HU |
| 2026-10-01 | Claude, por pedido de Ing. José Dúmar Jiménez Ruíz | El contexto dice la parte del problema de la épica que resuelve, según el análisis 4 |
| 2026-10-01 | Ing. José Dúmar Jiménez Ruíz | **Aprobada** |
