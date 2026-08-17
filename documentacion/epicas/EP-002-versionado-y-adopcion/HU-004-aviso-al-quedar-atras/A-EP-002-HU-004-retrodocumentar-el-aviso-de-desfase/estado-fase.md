# Estado de fase — Fase A-EP-002-HU-004-retrodocumentar-el-aviso-de-desfase (módulo Versionado y adopción)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-002-HU-004-retrodocumentar-el-aviso-de-desfase` |
| **Módulo** | Versionado y adopción — [`hook_sesion.py`](../../../../../validadores/hook_sesion.py) y [`version.py`](../../../../../validadores/version.py) |
| **Épica / HU / origen** | [EP-002](../../epica.md) · [HU-004](../HU-004-aviso-al-quedar-atras.md) · retro-documentación, fila de HU-004 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
| **Última actualización** | 2026-08-17 |

---

## 1. En qué estación va

**Estación actual:** 4 — pausa y presentación. **Última puerta pasada:** 3, con el plan de trabajo y el plan de pruebas escritos.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 orden de bajar a fase las HU del inventario 48 | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 pendiente: falta presentarlo, con la duda 1 sobre el texto del aviso | ☐ |
| 5 | Aprobación del plan detallado | 👤 pendiente | ☐ |
| 6 | Ejecución continua | 8 tareas, ninguna empezada | ☐ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☐ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☐ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** El texto del aviso no se cambia en esta fase: cambia lo que el usuario ve en cada apertura, y eso se decide.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Todavía no se ejecutó** |
| **CA cumplidos** | 0 de 3 |
| **CA en "No"** | Ninguno todavía. Se sabe que el **CA-01 va a quedar incompleto**: el aviso no dice qué cambió entre las dos versiones |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Pendiente | Prueba de `comparar` con desfase — CP-001 |
| T-02 | Pendiente | Constancia de lo que al mensaje le falta, con la duda 1 |
| T-03 | Pendiente | Prueba de `comparar` al día y sin versión declarada — CP-002 |
| T-04 | Pendiente | Caso de que con desfase el trabajo sigue — CP-003 |
| T-05 | Pendiente | Caso de la excepción de `F22` — CP-004 |
| T-06 | Pendiente | Anotar la excepción en el CA-03 de la HU |
| T-07 | Pendiente | Comprobar que el aviso sale una vez por apertura — CP-005 |
| T-08 | Pendiente | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 0 de 8. **Bloqueadas:** ninguna — la duda 1 no bloquea las pruebas, solo el cambio del mensaje.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Las pruebas van contra `comparar`, que está aislado de disco: probar el enganche entero obligaría a montar un proyecto para verificar aritmética | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| La HU dice «el aviso no detiene» y hay un caso en que sí, el de `F22`. La excepción se escribe **en la HU**, no solo en la regla: quien lea la HU tiene que encontrarla | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) y riesgo `R-02` |
| El CA-03 se cierra comparando los archivos contra su línea base, no leyendo la respuesta: avisar no es actualizar | §3.3 del [`plan_pruebas.md`](plan_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **Duda 1 de §2.7:** si el aviso pasa a decir qué cambió entre las dos versiones, y con qué detalle. **No bloquea las pruebas**: bloquea solo el cambio del mensaje.
- **La aprobación del plan.** Sin ella no arranca la ejecución.
- **Completar el mensaje puede romper pruebas que citan su texto** (riesgo `R-01`): solo se toca con la duda resuelta y el plan ampliado.
- **Si otra sesión está tocando `validadores/pruebas.py`** (riesgo `R-03`): se guarda solo lo propio.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 4 esperando la aprobación del plan; la duda 1 queda abierta pero no frena las ocho tareas.
