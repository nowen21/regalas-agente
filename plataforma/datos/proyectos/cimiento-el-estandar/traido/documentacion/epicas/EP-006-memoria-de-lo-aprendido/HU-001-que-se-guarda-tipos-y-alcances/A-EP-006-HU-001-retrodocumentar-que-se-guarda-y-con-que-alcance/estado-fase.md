# Estado de fase — Fase A-EP-006-HU-001-retrodocumentar-que-se-guarda-y-con-que-alcance (módulo Memoria)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-006-HU-001-retrodocumentar-que-se-guarda-y-con-que-alcance` |
| **Módulo** | Memoria — [`memoria/esquema.sql`](../../../../../memoria/esquema.sql) y [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md) |
| **Épica / HU / origen** | [EP-006](../../epica.md) · [HU-001](../HU-001-que-se-guarda-tipos-y-alcances.md) · retro-documentación, fila de HU-001 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
| **Última actualización** | 2026-08-17 |

---

## 1. En qué estación va

**Estación actual:** 9 — commit único. **Última puerta pasada:** 8, con la trazabilidad cerrada.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 orden de bajar a fase las HU del inventario 48 | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 presentado el 2026-08-17 | ☑ |
| 5 | Aprobación del plan detallado | 👤 «autorizados los planes de trabajo», 2026-08-17 | ☑ |
| 6 | Ejecución continua | 4 tareas, las 4 hechas | ☑ |
| 7 | Pruebas | [`resultado_pruebas.md`](resultado_pruebas.md) con veredicto **No cumple** | ☑ |
| 8 | Cierre documental | [`funcionalidad_implementada.md`](funcionalidad_implementada.md), §8 de la HU y fila del inventario 48 | ☑ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Los cinco documentos están escritos y la fase no cierra en «Cumple».** Un criterio transversal de la HU quedó en «No» y otro sin probar, y ninguno de los dos cabía en el plan aprobado. Lo que sigue es una fase `B-EP-006-HU-001` que los tome — propuesta, no abierta: abrirla es del usuario.

**El esquema no se tocó.** Los tres tipos que nunca se usaron siguen declarados: quitar uno rompería las señales que ya lo tienen.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **No cumple** |
| **CA cumplidos** | 2 de 4 — los dos numerados sí; de los dos transversales, ninguno |
| **CA en "No"** | El transversal de **privacidad**: `13·DOC5` no dice que no se guarden datos personales ni claves. El transversal de **límites** quedó sin probar, porque el plan no le escribió caso |
| **Defectos abiertos aceptados** | 4 — `D-01` el criterio no se aplica en este repositorio (1 señal de 237); `D-02` «leyendo el código» deja fuera lo escrito en un documento; `D-03` la lista cerrada está en el programa, no en el esquema; `D-04` el plan declaró 100% de cobertura sin contar los transversales |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) de esta fase |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | **Hecha** | Cinco decisiones reales clasificadas — CP-001. Cuatro son señal; ninguna se había guardado |
| T-02 | **Hecha** | Clase `TiposYAlcances` en [`memoria/pruebas.py`](../../../../../memoria/pruebas.py): 5 casos en verde — CP-002 |
| T-03 | **Hecha** | Tabla de los diez tipos con su uso real — CP-003. Siete vivos, tres nunca usados |
| T-04 | **Hecha** | Corrida completa (21 pruebas en verde), resultado escrito y trazabilidad cerrada |

**Hechas:** 4 de 4. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Los tipos que no se usan se **anotan, no se quitan**: quitar un tipo rompe las señales que ya lo tienen, y ninguna se borra | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| El criterio se prueba con decisiones reales de fases cerradas: las reales son las que cuesta clasificar, y los ejemplos inventados siempre caen claros | §2.6 del plan |
| Las pruebas corren sobre base temporal: la base real tiene el aprendizaje del proyecto | §2.6 del plan y riesgo `R-02` |
| Una decisión que no se pueda clasificar vale más que un cinco de cinco forzado: dice dónde al criterio le falta | CP-001 del [`plan_pruebas.md`](plan_pruebas.md) |
| **Ninguna de las cuatro decisiones que son señal se guarda retroactivamente**: `RN-04` dice que lo que se guarda se decide al guardarlo, no automáticamente | `D-01` del [`resultado_pruebas.md`](resultado_pruebas.md) |
| La lista de tipos es cerrada **en el programa**, no en el esquema; se dice en vez de taparse | `D-03` del resultado |

---

## 3. Pendiente / preguntas abiertas

- **Que `13·DOC5` diga que no se guardan datos personales ni claves.** Es el criterio transversal de privacidad de la HU, y hoy la regla no lo dice. Cambio de `base/`: lo decide el usuario.
- **Que el criterio cubra lo que está escrito en un documento del repositorio**, no solo lo que no está en el código (`D-02`).
- **Qué hacer con `D-01`:** el criterio decide bien y este repositorio tiene una sola señal en 237.
- **Los tres tipos sin uso y el alcance `modulo:` sin usar** (riesgo `R-01`): quedan anotados con la cuenta. Simplificar el esquema lo decide el usuario.
- **El módulo de la memoria no tiene especificación aparte.** Es uno de los casos que [EP-001 · HU-010](../../../EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/HU-010-cuando-no-aplica-la-especificacion.md) viene a resolver.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 9 esperando la autorización del commit, que es la puerta normal.
