# Plan de Pruebas — Fase `D-EP-001-HU-007-el-ca-04-se-mide-contra-lo-que-pide`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** el criterio de esta fase, con qué datos y cuándo se da por aprobado. Lo que se pide vive en la [HU-007](../HU-007-regla-de-las-reglas.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Medir el `CA-04` **contra sus tres exigencias escritas**, y no contra el estado de los datos que alguien interpretó como falta.

### 1.2 Alcance

**Entra:** que la lista exista, que esté ordenada, que diga cuándo y cuántos incumplimientos, y que no corrija nada.

**No entra:** revisar reglas, tocar la fase `A`, ni reabrir los otros criterios.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| El `CA-04` de la historia | Las tres exigencias, palabra por palabra |
| [revision-de-vigencia.md](../../../../../base/20-meta-reglas/revision-de-vigencia.md) | Que la ausencia de fechas es **deliberada** |
| `S-069` | Cómo se recomendó tres veces un trabajo sin leer el criterio |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| `vigencia.py` | Que dé la lista con sus tres datos, **ordenada** |
| El procedimiento | Que diga que la ausencia de fechas es a propósito |
| El efecto | Que correrlo no cambie ningún archivo |

---

## 3. Estrategia de pruebas

**Se corre, no se cita.** Apoyarse en la medición de la fase `A` heredaría su error de raíz.

**Y se mide contra el criterio, no contra el resumen del rojo.** El resumen decía «249 de 249 sin dato»; el criterio no menciona esa cifra en ninguna parte.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- Los dos planes, aprobados.
- El `CA-04` transcrito palabra por palabra en el plan §2.1.
- La línea base, medida antes de crear la carpeta.

### 4.2 Criterios de salida

- Los cinco casos **ejecutados**.
- El hallazgo de la fase `A`, **conservado** y con su destino dicho.
- La suite completa en verde.

### 4.3 Criterios de suspensión y reanudación

Se suspende si:

- **La lista no está ordenada.** Ahí el `CA-04` sigue incumplido, la fase cierra en rojo y el trabajo es otro: arreglar el orden.
- **Falta alguna de las tres columnas** que el criterio nombra.
- **Al releer el criterio resulta que sí pedía reglas revisadas.** En ese caso la fase `A` tenía razón, esta fase no tiene sentido, y `S-069` habría que reescribirla.

**El tercero es la forma de que esta fase pueda equivocarse**, y por eso está escrito.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| CA-04 — se obtiene la lista | CP-001 | De ejecución |
| CA-04 — dice cuándo y cuántos | CP-002 | De contenido |
| CA-04 — **ordenada** de la más vieja a la más nueva | CP-003 | De orden |
| Transversal — el programa avisa, no corrige | CP-004 | De efecto |
| Transversal — la ausencia de fechas es deliberada | CP-005 | De documentación |

---

## 6. Casos de prueba

### CP-001 — Se obtiene la lista

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `python validadores/vigencia.py` | Se ejecuta |
| 2 | Buscar la cabecera de la tabla | Existe |
| 3 | Contar las reglas que cubre | **Las 251**, dicho en la salida |

---

### CP-002 — La lista dice cuándo y cuántos

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer las columnas | Traen **`REVISADA`** |
| 2 | Y la de incumplimientos | Traen **`FALLA HOY`** |

**Son las dos que el criterio nombra**, y por eso se comprueban por separado en vez de dar por buena «la tabla».

---

### CP-003 — Está ordenada de la más vieja a la más nueva

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer la columna del sello en el orden en que sale | Se obtiene la secuencia |
| 2 | Comprobar que **no retrocede** | Va de la más vieja a la más nueva |
| 3 | Que las que no tienen sello vayan **primero** | Sí: son las que más llevan |

**Es el caso que puede fallar de verdad.** Que la lista exista es fácil de ver; **que esté ordenada** es lo que el criterio exige y lo que nadie mira.

---

### CP-004 — El programa avisa, no corrige

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Anotar el estado del repositorio | — |
| 2 | Correr la comprobación | — |
| 3 | Comparar | **Ningún archivo cambió** |

---

### CP-005 — La ausencia de fechas es deliberada

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir el procedimiento de revisión | Existe |
| 2 | Buscar qué dice sobre las reglas sin fecha | **«Arranca ausente en todas, a propósito»** |
| 3 | Comprobar que el `CA-04` no pide reglas revisadas | No lo pide |

**No es parte del `CA-04`, y se comprueba igual.** Es lo que separa «el criterio se cumple» de «además, tratarlo como deuda habría sido un error» — y ese error casi se comete tres veces.

---

## 7. Datos y ambientes de prueba

El árbol real. **Ninguna prueba usa credenciales** (`00·N6`) y no se edita ningún documento para probar (`08·T4`).

---

## 8. Herramientas

`vigencia.py`, corrido sobre el árbol real. **No hace falta sabotaje:** esta fase no cambia código.

---

## 9. Gestión de defectos

| Severidad | Qué la define |
|---|---|
| Crítica | La lista no está ordenada |
| Alta | Falta alguna de las dos columnas que el criterio nombra |
| Media | Correrlo modifica algún archivo |

Si aparece cualquiera, **la fase cierra con lo que salga**: el punto es medir contra el criterio, no llegar a un verde.

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
| Casos ejecutados | 5 de 5 |
| **Mediciones heredadas de la fase `A`** | **0** |
| Exigencias del criterio comprobadas | 3 de 3 |
| Archivos que cambian al correrlo | 0 |

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Dar por buena «la tabla» sin mirar sus columnas | `CP-002` las comprueba por separado |
| Comprobar que existe y no que está ordenada | `CP-003`, que es el crítico |
| Citar a la fase `A` | Todos los casos corren |
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
