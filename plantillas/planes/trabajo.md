# Plan de Trabajo — Fase «A-EP01-HU03-Descripción» (módulo «M»)   ·   `[CAPA 3]`

> Plantilla del `plan_trabajo` de una **fase** (unidad de ejecución). Responde las **13 preguntas de `02·F4.1`** sobre una **línea base verificada** (`02·F4.3`). Se guarda en `documentacion/<modulo>/<identificador-de-fase>/plan_trabajo.md` (identificador según `02·F12`). Va junto con su `plan_pruebas` (plantilla `planes/pruebas.md`) y **no se toca código hasta que ambos estén aprobados** (`F4`). Reemplaza los `«…»`, borra las secciones marcadas *(opcional)* si no aplican, y borra esta caja.
>
> **Unidad = fase.** Una fase pertenece a **una sola HU** (`02·F12`); declara qué CA de esa HU satisface (§0). La HU es el requisito; la fase es cómo se ejecuta y se cierra.

---

## 0. Identificación y origen  ·  `F4.1` Q1–Q2 · `DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12`) | `«A-EP01-HU03-Descripción»` |
| **Épica** | `EP«01»` |
| **HU** | `HU«03»` — **una sola** (`F12`) |
| **Módulo** | «M» (`13·DOC13`) |
| **Spec del módulo** | [enlace al prompt/spec · `02·F2`] |
| **Fecha apertura** | AAAA-MM-DD |
| **Rama** | `«feature/<identificador-de-fase>»` |
| *(opcional)* Sprint · Dev · Revisor · QA | «…» |

**ORIGEN** (1 de 3, o híbrido · `DOC12`):
- 📝 **Modifica fase(s):** «cuáles y qué gap/promesa retoma» · ref. cierre de análisis (`DOC8`) si aplica.
- ✨ **Funcionalidad nueva:** «qué introduce que no estaba en el roadmap».
- 🔀 **Híbrido:** ambos.

**CA de la HU que cubre esta fase** (una sola HU · `02·F12` · trazabilidad `DOC11`):

| CA de `HU«03»` que cierra esta fase | Estado |
|---|---|
| CA-01 | ☐ |
| CA-02 | ☐ |

---

## 1. Objetivo y alcance  ·  `F4.1` Q4

**Objetivo:** ejecutar y verificar los CA declarados en §0 hasta dejarlos cumplidos con evidencia (§5).

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | [Camino feliz] | Funcional | Media |
| CA-02 | [Validación / error] | Funcional | Baja |
| CA-03 | [Caso borde] | Funcional | Alta |
| RNF-01 | [Rendimiento / seguridad] | No funcional | Media |

**Fuera de alcance** (qué explícitamente NO entra en esta fase · cierra expectativas):
- [Lo que no se aborda aquí y a qué fase futura se difiere, si aplica.]

---

## 2. Análisis previo — línea base verificada  ·  `F4.3`

> Todo lo de esta sección se **verifica contra el proyecto real** antes de escribir el plan. **Prohibido** `(o donde esté)`, `(o similar)`, `TBD`, `?`. Si algo no se puede verificar, va como duda abierta (§2.7), no como suposición.

### 2.1 Archivos que se crean o modifican  ·  `F4.1` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `[ruta/exacta]` | Nuevo / Modificar | BD / Modelo / Servicio / Endpoint / UI / Test | |

### 2.2 Matriz de dependencias del refactor  ·  `F4.3` (obligatoria si se cambian contratos de código existente)

> Por cada archivo que cambia un contrato, TODOS los que dependen de él y rompen. El §2.1 es la unión de {archivos a tocar} ∪ {dependientes directos que rompen}. Lo que no se refactoriza en esta fase se difiere explícito en §1 (fuera de alcance).

| Archivo a refactorizar | Cambio de contrato | Archivos que dependen (rompen) | Dónde rompe |
|---|---|---|---|
| `[archivo A]` | [elimina columna X · renombra método Y · cambia cardinalidad] | `[B] · [C]` | `B: lee X` · `C: carga relación Y` |

### 2.3 Rutas / endpoints y control de acceso  ·  `F4.1` Q6

| Método + ruta | Autenticación | Permiso | Alcance |
|---|---|---|---|
| `[VERBO] /...` | [sí/no] | `[permiso]` | [propio/global] |

Contrato de API (si aplica):

```http
[MÉTODO] /api/.../[recurso]
Request:  { }
Response 200: { }
Errores:  400 | 401 | 403 | 404 | 422
```

### 2.4 Punto de entrada en la UI  ·  `F4.1` Q7

- **Dónde queda accesible al usuario final:** [menú / navegación / dashboard / link desde otra vista, con el archivo de navegación real]. Si la fase no introduce UI navegable, declararlo: "No aplica porque …".

### 2.5 Permisos / roles a sembrar  ·  `F4.1` Q8

- [Permisos o roles nuevos, con la nomenclatura del proyecto. "Ninguno" si no aplica.]

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| | | |

> Las decisiones no obvias se registran también como señal (`13·DOC5`).

### 2.7 Dudas por resolver antes de codificar

| # | Duda | A quién se consulta | Estado |
|---|---|---|---|
| 1 | | usuario / PO | Pendiente / Resuelta |

> Ninguna tarea de construcción inicia con una duda abierta que la bloquee.

---

## 3. Desglose de tareas por criterio de aceptación

> Cada CA se descompone en tareas atómicas (≤ 4 h). **Depende de** ordena la ejecución; **Ev.** referencia la evidencia de §5.

### CA-01 — [Nombre del escenario]

| ID | Tarea | Capa | Est. | Depende de | Estado | Ev. |
|---|---|---|:--:|---|---|---|
| T-01 | Crear migración `[nombre]` | BD | 1 h | — | ☐ | |
| T-02 | Definir modelo / entidad | Backend | 1 h | T-01 | ☐ | |
| T-03 | Implementar lógica en servicio | Backend | 3 h | T-02 | ☐ | |
| T-04 | Exponer endpoint y validaciones | Backend | 2 h | T-03 | ☐ | |
| T-05 | Prueba del servicio | Test | 2 h | T-03 | ☐ | EV-01 |
| T-06 | Consumir API desde la UI | Frontend | 2 h | T-04 | ☐ | |
| T-07 | Construir vista / componente | Frontend | 3 h | T-06 | ☐ | EV-02 |

### CA-02 — [Nombre del escenario: validación / error]

| ID | Tarea | Capa | Est. | Depende de | Estado | Ev. |
|---|---|---|:--:|---|---|---|
| T-08 | Validaciones de entrada | Backend | 2 h | T-04 | ☐ | |
| T-09 | Manejo y mensajes de error en UI | Frontend | 2 h | T-07 | ☐ | EV-03 |
| T-10 | Prueba de caso negativo | Test | 1 h | T-08 | ☐ | EV-03 |

### RNF — Requisitos no funcionales

| ID | Tarea | Categoría | Est. | Estado | Ev. |
|---|---|---|:--:|---|---|
| T-11 | Verificar autorización por rol | Seguridad | 1 h | ☐ | EV-04 |
| T-12 | Registrar evento en bitácora | Auditoría | 1 h | ☐ | EV-05 |
| T-13 | Medir respuesta con [n] registros | Rendimiento | 1 h | ☐ | EV-06 |

**Total estimado:** [suma] h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-04 → T-06 → T-07
**Paralelizables:** [tareas independientes que pueden avanzar en simultáneo].

> Solo se tocan los archivos declarados en §2.1 (`F8`). Descubrir uno nuevo → PAUSAR, reportar, ampliar el plan con OK, no editar por iniciativa.

---

## 5. Verificación de criterios de aceptación  ·  `F4.1` Q10

> Un CA no se marca cumplido sin evidencia. La fase no cierra con algún CA en rojo. El detalle de casos vive en el `plan_pruebas`.

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Prueba + verificación manual | EV-01, EV-02 | | ☐ |
| CA-02 | Prueba de caso negativo | EV-03 | | ☐ |
| CA-03 | Prueba con datos límite | EV-07 | | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Reporte de pruebas | `[ruta / enlace]` |
| EV-02 | Captura | `[enlace]` |

---

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | [dónde corren las pruebas — nunca datos reales, `00·N4`/`08·T4`] |
| Usuarios de prueba | [rol + credencial de prueba, sin claves reales] |
| Datos precargados | [script / dataset] |

> El detalle completo (matriz, casos, técnicas de triangulación) va en el `plan_pruebas` (`planes/pruebas.md`).

---

## 7. Reversión / rollback  ·  `F4.1` Q11

Plan B concreto si algo sale mal: [reversión de commit · rollback de esquema (`down()`) · backfill inverso · feature flag · script de emergencia]. Cada cambio destructivo declara cómo se revierte.

---

## 8. Producción y migración incremental  ·  `F4.1` Q12 · `F10`

Asumir **"probablemente está en producción"**. Estrategia según el tipo de cambio:
- **Aditivo** (columna/tabla nueva): migración nueva, backfill si aplica.
- **Rename:** migración nueva reversible (no editar la original de una fase cerrada).
- **Drop / cambio de tipo con datos:** avisar el riesgo específico antes de aplicar + `down()` que reconstruye.
- «Declarar la que aplica, o "No aplica porque …".»

---

## 9. Reglas del estándar y del proyecto aplicadas  ·  `F4.1` Q13

Trazabilidad de decisiones — reglas por su identificador:
- Base: [ej. `02·F8`, `04·S…`, `08·T4`, `13·DOC11`].
- Proyecto: [ej. `P<N>` de `.agente/reglas-proyecto.md`].

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | | Retrasa T-0x | | Abierto / Cerrado |

---

## 11. Definition of Done

- [ ] Todos los CA de §0 verificados con evidencia (§5)
- [ ] Requisitos no funcionales validados
- [ ] Pruebas de la fase en verde (alcance quirúrgico · `F5`)
- [ ] Trazabilidad spec → implementación sin faltantes (`DOC11`)
- [ ] Sin errores de linter / análisis estático (`07`)
- [ ] Documentación e índices/mapas del proyecto actualizados (`13`)
- [ ] Señales registradas (`DOC5`)
- [ ] Rama lista para el commit único de la fase (`G1`)
- *(opcional)* Aceptada por el Product Owner / usuario

---

## 12. Seguimiento diario  ·  *(opcional — equipo)*

| Fecha | Tareas cerradas | Avance CA | Bloqueos | Ajuste al plan |
|---|---|---|---|---|
| AAAA-MM-DD | T-01, T-02 | CA-01 en curso | Ninguno | — |

---

## 13. Cierre

**Resultado:** [CA cumplidos / total] · **Esfuerzo real vs. estimado:** [h] / [h]

**Lecciones aprendidas:** [qué se subestimó, qué patrón conviene reutilizar → señal `DOC5`].

**Deuda técnica generada:**

| Descripción | Registro / ticket |
|---|---|
| | |
