# HU-005 · Nada se agrega fuera de lo pedido

> Sus criterios salen de «Lo que se tiene que hacer» del [análisis 1](../103-cada-documento-de-la-cadena-sale-del-anterior/analisis-1.md), puntos 8, 22 y 28. Los campos que no son alcance (módulo, tipo, estimación y responsable) son propuesta del agente y esperan la aprobación del usuario.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-005 |
| **Épica / Feature** | [EP-023 Lo que se construye es lo que se analizó](../epica.md) |
| **Módulo / Componente** | `base/01-conducta.md`, `base/02-flujo-de-trabajo/`, `historico-chat/memory/` |
| **Tipo** | Técnica |
| **Prioridad** | Orden 2 de 7: es pequeña y ataca la causa más directa |
| **Estimación** | S |
| **Sprint** | N/A |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | Claude |
| **Estado** | Lista: aprobada el 2026-10-01 |

---

## 2. Narrativa

- **Como** el usuario, que plantea la necesidad y aprueba (análisis 1, conclusión 40)
- **Quiero** que nada se agregue fuera de lo pedido
- **Para** que al ejecutar un plan solo aparezcan los hallazgos que no se podían prever

---

## 3. Contexto y descripción

Del [problema de la épica](../epica.md#31-situación-actual), esta HU resuelve que el agente agrega lo que no se pidió, porque `01·C14` se lo permite ([análisis 4](../103-cada-documento-de-la-cadena-sale-del-anterior/analisis-4.md), conclusión 4).

### 3.1 Reglas de negocio

Son las conclusiones de las que salen los puntos de esta HU.

| ID | Regla | Sale de |
|---|---|---|
| RN-01 | Si se pide la clase `Matematicas` con `suma`, se hace eso y nada más. El nombre de lo pedido no autoriza agregar lo que sugiere | Análisis 1, conclusión 7 |
| RN-02 | Las reglas no se contradicen, se complementan | Análisis 1, conclusión 12 |
| RN-03 | El agente solo puede preguntar en el análisis si se agrega lo que el oficio suele incluir, y decide el usuario. Nunca lo agrega por su cuenta | Análisis 1, conclusión 17 |
| RN-04 | Un hallazgo es lo que el análisis no previó y queda fuera del plan o de los criterios. Un error dentro de lo aprobado se corrige y se sigue. El permiso de corregir por cuenta propia queda limitado a lo que está dentro del plan aprobado | Análisis 1, conclusión 45 |

### 3.2 Supuestos

Ninguno.

### 3.3 Fuera de alcance

- Los puntos que la propuesta final reparte a las otras HU.

---

## 4. Criterios de aceptación

### CA-01 · `01·C14` y `02·F19` se complementan

**Sale de:** análisis 1, punto 8.

```gherkin
Dado que se leen 01·C14 y 02·F19
Cuando se comparan
Entonces se complementan y ninguna contradice a la otra
```

**Cómo validarlo:**
1. Abrir [`01·C14`](../../../../base/01-conducta.md#c14--lo-que-el-oficio-ya-da-por-sentado-se-aplica-sin-ofrecerlo-como-opción) y [`02·F19`](../../../../base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md).

**Aprobado cuando:** se complementan.

### CA-02 · `01·C14` queda derogada y reemplazada, y `01·C25` reubicada

**Sale de:** análisis 1, punto 22.

```gherkin
Dado que 01·C14 se deroga según 20·M11
Entonces queda marcada como derogada, con la regla que la reemplaza
Y 01·C25, que hoy la extiende, queda reubicada
```

**Cómo validarlo:**
1. Abrir `01·C14`, la regla que la reemplaza y `01·C25` en [`01-conducta.md`](../../../../base/01-conducta.md).

**Aprobado cuando:** `C14` está derogada según `20·M11`, la nueva existe y `C25` ya no extiende a una regla derogada.

### CA-03 · Los recuerdos se ajustan al plan aprobado

**Sale de:** análisis 1, punto 28.

```gherkin
Dado el recuerdo «Corregir el defecto detectado»
Cuando se ajusta
Entonces solo vale dentro del plan aprobado
Y «Una instrucción se cumple entera» queda revisado contra la conclusión 18
```

**Cómo validarlo:**
1. Abrir [corregir-el-defecto-que-uno-mismo-detecta.md](../../../../historico-chat/memory/corregir-el-defecto-que-uno-mismo-detecta.md) y [una-instruccion-se-cumple-entera.md](../../../../historico-chat/memory/una-instruccion-se-cumple-entera.md).

**Aprobado cuando:** el primero vale solo dentro del plan aprobado y el segundo no choca con detener la ejecución ante un hallazgo.

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
- [ ] `VERSION` y `CHANGELOG.md` actualizados
- [ ] Aceptada por el usuario

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | ☐ | Depende de la HU-001 |
| **N**egociable | ✅ | |
| **V**aliosa | ✅ | Ataca la causa más directa |
| **E**stimable | ✅ | Talla S |
| **S**mall (pequeña) | ✅ | Tres criterios |
| **T**esteable | ✅ | Cada criterio dice dónde mirar |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-01 | Claude, por pedido de Ing. José Dúmar Jiménez Ruíz | Creación de la HU |
| 2026-10-01 | Claude, por pedido de Ing. José Dúmar Jiménez Ruíz | El contexto dice la parte del problema de la épica que resuelve, según el análisis 4 |
| 2026-10-01 | Ing. José Dúmar Jiménez Ruíz | **Aprobada** |
