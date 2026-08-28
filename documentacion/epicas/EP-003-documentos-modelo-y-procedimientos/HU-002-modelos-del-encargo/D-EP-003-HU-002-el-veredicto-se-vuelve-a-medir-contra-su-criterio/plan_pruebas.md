# Plan de Pruebas — Fase `D-EP-003-HU-002-el-veredicto-se-vuelve-a-medir-contra-su-criterio`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** el criterio de esta fase, con qué datos y cuándo se da por aprobado. Lo que se pide vive en la [HU-002](../HU-002-modelos-del-encargo.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Volver a medir el `CA-01` **contra lo que su criterio pide**, y no contra lo que la fase `A` decidió medir.

### 1.2 Alcance

**Entra:** que existan los tres modelos, y que la cadena se recorra en los dos sentidos.

**No entra:** tocar la fase `A`, descartar su hallazgo, ni reabrir los otros criterios de la historia.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| La fase [`A`](../A-EP-003-HU-002-retrodocumentar-los-modelos-del-encargo/resultado_pruebas.md) | El veredicto que se corrige, y el hallazgo que sí valía |
| `S-063` | Un veredicto puede estar mal el día que se escribe |
| El `CA-01` de la historia | Lo que de verdad se exige |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| Los tres modelos | Que existan, con nombre reconocible |
| El encadenamiento | Que se recorra hacia abajo **y** hacia arriba |
| Lo que la fase `A` señaló | Que se compruebe, no que se suponga |

---

## 3. Estrategia de pruebas

**Se corre, no se cita.** Apoyarse en la medición de la fase `A` heredaría su error de raíz, y el punto de esta fase es no heredarlo.

**Y se lee el criterio entero antes de medir**, incluida su línea de «aprobado cuando». Ahí está lo que la fase `A` no miró: dice *«la cadena se puede recorrer de arriba abajo y de abajo arriba»* — nada del planteamiento de este repositorio.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- Los dos planes, aprobados.
- El `CA-01` transcrito palabra por palabra en el plan §2.1.
- La línea base, medida antes de crear la carpeta.

### 4.2 Criterios de salida

- Los tres casos **ejecutados**.
- El hallazgo de la fase `A`, **conservado** y con su destino corregido.
- La suite completa en verde, con conteo distinto de cero.

### 4.3 Criterios de suspensión y reanudación

**Se suspende si la cadena falla hoy.** Ahí la fase cerraría en rojo con razón, y el trabajo sería otro: arreglar la cadena, no corregir un veredicto.

**Y se suspende si al leer el criterio completo resulta que sí pedía lo que la fase `A` midió.** En ese caso el veredicto era correcto, esta fase no tiene sentido, y `S-063` habría que reescribirla. **Se dice acá porque es la forma de que esta fase pueda equivocarse.**

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| CA-01 — los tres modelos existen | CP-001 | De existencia |
| CA-01 — y la cadena se recorre en los dos sentidos | CP-002 | De sistema |
| El hallazgo de la fase `A` | CP-003 | De comprobación |

---

## 6. Casos de prueba

### CP-001 — Los tres modelos existen

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-01 |
| **Tipo** | De existencia |
| **Prioridad** | Alta |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir la carpeta de modelos del estándar | Está |
| 2 | Ubicar el de la necesidad, el de la épica y el de la historia | **Los tres, con nombre reconocible** |
| 3 | Abrir el de la historia y buscar dónde nombra su épica | Hay campo |
| 4 | Abrir el de la épica y buscar dónde lista sus historias | Hay tabla |

---

### CP-002 — La cadena se recorre en los dos sentidos

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-01 |
| **Tipo** | **De sistema** |
| **Prioridad** | **Crítica** |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr la comprobación de trazabilidad sobre el árbol real | Se ejecuta |
| 2 | Contar las fallas de enlace bidireccional | **Cero** |
| 3 | Anotar sobre cuántas épicas e historias se midió | El número real de hoy |

**Es el crítico, y es el que la fase `A` ya había dado verde.** Se vuelve a correr en vez de copiarlo, porque **una fase que hereda la medición de otra hereda también su error**.

**El paso 3 importa:** decir «sin fallas» sin decir sobre cuántas es un registro que no demuestra nada (`S-040`).

---

### CP-003 — El hueco que la fase `A` señaló

| Campo | Valor |
|---|---|
| **HU / CA** | Transversal |
| **Tipo** | De comprobación |
| **Prioridad** | Media |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar el planteamiento de este repositorio | **Existe** |
| 2 | Comprobar que no es el molde en blanco | Sin marcadores de plantilla |
| 3 | Buscar el pendiente que la fase `A` citó | **Cerrado** |

**No es parte del `CA-01`** — se comprueba precisamente porque **el hallazgo de la fase `A` valía aunque estuviera mal ubicado**, y hay que saber si sigue abierto antes de decir que no.

---

## 7. Datos y ambientes de prueba

El árbol real del repositorio. **Ninguna prueba usa credenciales** (`00·N6`) y **no se edita ningún documento para probar** (`08·T4`).

---

## 8. Herramientas

La comprobación de trazabilidad que ya existe, corrida sobre el árbol real. **No hace falta sabotaje:** esta fase no cambia código.

---

## 9. Gestión de defectos

| Severidad | Qué la define |
|---|---|
| Crítica | La cadena falla hoy |
| Alta | Alguno de los tres modelos no está |
| Media | El hueco que la `A` señaló sigue abierto |

Si aparece cualquiera, **la fase lo dice y cierra con lo que salga** — el punto es medir contra el criterio, no llegar a un verde.

---

## 10. Cronograma

Un solo tramo. La suite completa al final.

---

## 11. Roles y responsabilidades

Una sola persona cumple los roles. El agente comprueba; el usuario aprueba.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Casos ejecutados | 3 de 3 |
| **Mediciones heredadas de la fase `A`** | **0** |
| Fallas de enlace bidireccional | 0, **y dicho sobre cuántas** |

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Citar a la fase `A` en vez de medir | `CP-002` corre la comprobación |
| Cerrar el rojo y perder el hallazgo | `CP-003` lo comprueba, y el cierre lo conserva |
| Buscar el verde en vez de la verdad | El §4.3 dice qué haría que esta fase no tuviera sentido |

---

## 14. Control de versiones

| Versión | Fecha | Cambio |
|---|---|---|
| 1 | 2026-08-27 | Redacción inicial, junto con el plan de trabajo |

---

## 15. Aprobación

| Rol | Estado |
|---|---|
| Usuario | Pendiente. **No se toca nada hasta que este plan y el de trabajo estén aprobados** (`02·F4`) |
