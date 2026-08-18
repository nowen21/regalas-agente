# Estado de fase — Fase A-EP-004-HU-009-el-conteo-de-hallazgos-por-regla (módulo Comprobación automática)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-009-el-conteo-de-hallazgos-por-regla` |
| **Módulo** | Comprobación automática — [`validadores/comun.py`](../../../../../validadores/comun.py) y [`validar.py`](../../../../../validadores/validar.py) |
| **Épica / HU / origen** | [EP-004](../../epica.md) · [HU-009](../HU-009-conteo-por-regla.md) · ✨ funcionalidad nueva. Fila de HU-009 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
| **Última actualización** | 2026-08-17 |

---

## 1. En qué estación va

**Estación actual:** 6 — ejecución continua, **lista para arrancar**. **Última puerta pasada:** 5, el plan aprobado por el usuario el 2026-08-17 («autorizados los planes de trabajo»).

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 orden de bajar a fase las HU del inventario 48 | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 presentado el 2026-08-17 | ☑ |
| 5 | Aprobación del plan detallado | 👤 «autorizados los planes de trabajo», 2026-08-17 | ☑ |
| 6 | Ejecución continua | 7 tareas · **detenida por las 2 dudas de §2.7** | ☐ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☐ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☐ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** Esta fase toca `comun.py`, que usan los 24 subcomandos: no se toca sin aprobación.

> **El plan quedó aprobado el 2026-08-17** y la fase **no arrancó**: las 2 dudas de §2.7 del plan sigue sin resolver, y solo la puede resolver el usuario. Lo que falta ya no es la aprobación — es la respuesta.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Todavía no se ejecutó** |
| **CA cumplidos** | 0 de 3 |
| **CA en "No"** | Los **tres están en «No» de entrada**, y por eso la fase construye: nada agrupa hallazgos por regla hoy |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Pendiente | Que cada hallazgo diga a qué regla pertenece. **No depende de las dudas** |
| T-02 | Bloqueada | Que la corrida deje el conteo — CP-001. Dudas 1 y 2 |
| T-03 | Bloqueada | Que el registro guarde solo identificador, número y fecha |
| T-04 | Bloqueada | Prueba de que el registro no contiene la clave — CP-002 |
| T-05 | Bloqueada | Fecha y versión del estándar en el registro |
| T-06 | Bloqueada | Caso de las dos corridas comparadas — CP-003 |
| T-07 | Bloqueada | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 0 de 7. **Bloqueadas:** todas menos T-01.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| El campo de la regla entra con valor por omisión: cambiar de golpe los 24 validadores rompería la suite entera de una vez | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| El registro guarda identificador, número y fecha, **nunca el texto del hallazgo**: un registro con el texto arrastra el contenido revisado, y eso choca con `00·N6` y con el capítulo de privacidad | §2.6 del plan |
| El conteo compara por **regla**, no por proyecto: comparar proyectos es calificar trabajo, y eso está fuera de alcance | §2.6 del plan y riesgo `R-01` |
| La única forma de comprobar que el registro no arrastra contenido es correrlo sobre algo que no debería aparecer nunca, y buscar esa cadena en el registro | CP-002 del [`plan_pruebas.md`](plan_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **Duda 1 de §2.7:** dónde vive el registro de conteos — carpeta versionada, no versionada, o solo en la salida de la corrida.
- **Duda 2 de §2.7:** si esta fase espera a que exista la corrida completa de [HU-008](../../HU-008-corrida-completa/HU-008-corrida-completa.md), que es la que le da un único punto donde contar.
- **La aprobación del plan.** Se toca `comun.py`, que es de todos los validadores.
- **El caso del CA-02 corre antes de dar la fase por buena** (riesgo `R-02`): un registro que arrastre contenido revisado sería una filtración por la puerta de atrás.

---

## 4. Si se bloqueó

- **Estación:** 6 — ejecución continua, detenida. **Motivo:** el plan **está aprobado** desde el 2026-08-17, y las dos dudas bloquean todo menos la primera tarea. **Qué falta para desbloquear:** que el usuario apruebe el plan, diga dónde vive el registro y si esta fase espera a la corrida completa de HU-008.

---

## Lo que la desbloqueó

**Las dudas de la §2.7 quedaron decididas el 2026-08-18**, en el [pendiente 59](../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md). La decisión está escrita en el propio plan, con su motivo.

**La fase no arrancó todavía:** decidir no es ejecutar.
