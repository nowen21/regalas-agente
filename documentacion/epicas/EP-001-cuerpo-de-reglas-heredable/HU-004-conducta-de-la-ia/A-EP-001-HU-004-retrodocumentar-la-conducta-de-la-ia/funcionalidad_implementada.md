# Funcionalidad implementada — Fase `A-EP-001-HU-004-retrodocumentar-la-conducta-de-la-ia` (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-001-HU-004-retrodocumentar-la-conducta-de-la-ia` |
| **Módulo** | Cuerpo de reglas |
| **Especificación del módulo** | La propia [HU-004](../HU-004-conducta-de-la-ia.md). El entregable es texto normativo, y sus criterios son la especificación |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-17 |
| **HU / CA cubiertas** | [HU-004](../HU-004-conducta-de-la-ia.md): `CA-01`, `CA-02` y `CA-03`. Los tres |
| **Fecha de cierre** | 2026-08-26 |
| **Versión del estándar al cerrar** | `35.1.0` |
| **Commit** | `b19ca91` |

> **Se ejecutó el 2026-08-22 y se cierra el 2026-08-26.** Entre las dos fechas no se tocó nada de esta fase: lo que faltaba era este documento. Las dos fechas se dejan escritas porque **son distintas**, y confundirlas haría creer que se verificó hoy lo que se verificó entonces.

---

## 1. Qué se implementó — resumen

**Nada nuevo en el cuerpo de reglas, y ese es el resultado.** Las tres exigencias de conducta de la historia **ya eran regla** cuando se abrió la fase: `01·C13` y `01·C17` para la primera, y `00·ID8` con su lista y su programa para la tercera.

**Lo que faltaba era la cadena que lo respalda**, que es lo que significa retrodocumentar: el plan, las pruebas y el resultado que dicen con qué se comprobó y qué salió.

**Y lo que hace especial a esta fase es cómo se probó.** Los tres criterios son sobre **cómo se comporta el agente**, así que la única evidencia honesta era cómo se comportó de verdad — no leer la regla y declararla cumplida.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem de la historia | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| `CA-01` una pregunta se responde, no se ejecuta | norma | [`01·C13`](../../../../../base/01-conducta.md) y [`01·C17`](../../../../../base/01-conducta.md) | ✅ | Dos casos reales del 2026-08-22, uno de ellos un **contraejemplo** |
| `CA-02` lo detectado mal se corrige sin preguntar | norma | El recuerdo del repositorio, apuntando a su regla | ✅ | Tres correcciones hechas y una diferida con motivo |
| `CA-03` lo entregado no se lee como escrito por una máquina | norma | `00·ID8`, con su lista de marcas y su programa | ✅ | Un incumplimiento medido **el mismo día** |

**Las reglas no las escribió esta fase.** `C17` está en el repositorio desde el 2026-08-04, antes de que la fase se abriera. El plan preveía escribir dos reglas nuevas; al ejecutar se encontró que el capítulo ya las tenía, y **eso es un resultado, no un incumplimiento del plan**.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Evidencia |
|---|---|---|---|
| T-01, T-04 | Escribir las dos reglas que faltaban | ✅ **resuelta sin escribir**: ya existían | §1 del resultado |
| T-02, T-05, T-07 | Los tres casos de prueba, uno por criterio | ✅ hecha | §1 del resultado, con conducta real |
| T-03, T-06 | Dejar los dos recuerdos apuntando a su regla | ✅ hecha | Los recuerdos del repositorio |
| T-08 | Dejar escrito que nadie lo comprueba con un programa | ✅ hecha | La deuda `D-01` |
| T-09 | Clasificar las reglas en `reglas-validables.md` | ✅ hecha | Están clasificadas |
| T-10 | Correr, escribir el resultado, versionar y cerrar la trazabilidad | ✅ **hecha en parte** | Ver abajo |

**Correspondencia con el plan:** 10 tareas, y las 10 tienen resultado.

**Lo que no se hizo, y hay que decirlo:** la `T-10` incluía **cerrar la trazabilidad**, y este documento es justamente lo que faltaba de ella. **La fase quedó cuatro días en la estación 11 sin cerrarse**, y por eso el inventario la contaba entre las incompletas.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Qué | Resultado |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, los tres criterios |
| **Cómo se probó** | Conducta real del agente el 2026-08-22, no lectura de las reglas |
| **Defectos abiertos que se aceptaron** | `D-01` (alta) y `D-02` (media). Ver §6 |

**El contraejemplo vale más que el ejemplo.** El mismo día en que se verificó `CA-01`, el agente tomó un «siga» como orden de continuar en vez de como pregunta. Que eso quedara escrito en el resultado, y no solo los casos que salieron bien, es lo que hace que el veredicto se pueda creer.

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

No hay punto de entrada: el entregable es **texto normativo**. Las reglas se cargan solas al abrir sesión, con el resto de `base/`.

- **Una pregunta se responde:** `01·C13` y `01·C17`.
- **Lo entregado no se lee como escrito por una máquina:** `00·ID8`, y el programa que la cuenta es `validar.py marcas`.

---

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué | Dónde quedó |
|---|---|---|
| Un recuerdo de este repositorio **no viaja** a un proyecto heredero | Lo que se le exige a cualquier proyecto es **regla**, no memoria. Por eso las dos exigencias tenían que ser regla y no quedarse en el recuerdo | §2.6 del plan |
| La regla de corregir sin preguntar lleva su **límite en el cuerpo**, no al pie | Sin él le pasaría por encima a una regla blindada | §2.6 del plan |
| Una regla de conducta se prueba **pidiéndole a la IA justo lo que no debe hacer, y mirando el disco** | Mirar la respuesta no sirve: puede decir lo correcto y haber tocado el archivo igual | §3.3 del plan de pruebas |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Severidad | Estado al cerrar |
|---|---|---|
| **`D-01` · Nada obliga a correr el recuento de marcas antes de entregar un documento.** La regla existe, el programa existe, y el enganche **solo mira lo que entra al commit**. Un documento que se muestra en el chat y nunca se commitea no pasa por ningún filtro | Alta | **Sigue abierta.** Se verificó el 2026-08-26: el enganche corre `validar.py marcas --preparados`, y eso es exactamente lo que la deuda describe |
| **`D-02` · El `CA-02` se lee como «corrige de una»**, y hay correcciones que exigen su cadena porque suben versión. El criterio no distingue | Media | Sigue abierta |

**`D-01` explica el incumplimiento del `CA-03` del mismo día**, y por eso el criterio se marcó cumplido **como regla** y con el incumplimiento escrito al lado. No se tapó.

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] La historia [HU-004](../HU-004-conducta-de-la-ia.md): su §8 nombra esta fase.
- [x] `validadores/reglas-validables.md`: las reglas están clasificadas.
- [x] Los dos recuerdos del repositorio, apuntando a su regla.
- [x] El inventario de historias: **ya no se mantiene a mano** desde la `35.0.0`, así que la cuenta se corrige sola al cerrar esto.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

- **Migraciones a correr:** ninguna. El entregable es texto.
- **Qué cambia para quien ya tenía el estándar:** nada. Las reglas ya estaban publicadas; lo que esta fase agrega es el respaldo de por qué se dan por cumplidas.
- **Reversión:** no aplica. No hay nada que revertir: la fase no cambió el cuerpo de reglas.
