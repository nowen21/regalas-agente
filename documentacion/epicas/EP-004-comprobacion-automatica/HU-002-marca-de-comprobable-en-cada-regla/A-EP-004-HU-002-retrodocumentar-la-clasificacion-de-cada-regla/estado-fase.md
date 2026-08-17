# Estado de fase — Fase A-EP-004-HU-002-retrodocumentar-la-clasificacion-de-cada-regla (módulo Comprobación automática)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-002-retrodocumentar-la-clasificacion-de-cada-regla` |
| **Módulo** | Comprobación automática — [`validadores/reglas-validables.md`](../../../../../validadores/reglas-validables.md) y la fila 18 del [checklist](../../../../../base/20-meta-reglas/checklist.md) |
| **Épica / HU / origen** | [EP-004](../../epica.md) · [HU-002](../HU-002-marca-de-comprobable-en-cada-regla.md) · retro-documentación, fila de HU-002 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
| **Última actualización** | 2026-08-17 |

---

## 1. En qué estación va

**Estación actual:** 4 — pausa y presentación. **Última puerta pasada:** 3, con el plan de trabajo y el plan de pruebas escritos.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 orden de bajar a fase las HU del inventario 48 | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 pendiente: falta presentarlo | ☐ |
| 5 | Aprobación del plan detallado | 👤 pendiente | ☐ |
| 6 | Ejecución continua | 7 tareas, ninguna empezada | ☐ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☐ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☐ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** §2.7 no dejó dudas abiertas: todo lo que la fase afirma se verificó contra el repositorio.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Todavía no se ejecutó** |
| **CA cumplidos** | 0 de 3 |
| **CA en "No"** | Ninguno todavía. Se sabe que el **CA-03 va a quedar en «No»**: nada impide hoy publicar una regla sin clasificar, porque el programa que lo vería no corre |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Pendiente | Prueba del cruce en los dos sentidos — CP-001 |
| T-02 | Pendiente | Caso del rango que no clasifica — CP-002 |
| T-03 | Pendiente | Tabla regla → programa contra los subcomandos que existen |
| T-04 | Pendiente | Caso de llegar al programa leyendo solo el registro — CP-003 |
| T-05 | Pendiente | Caso de la regla nueva sin clasificar — CP-004 |
| T-06 | Pendiente | Constancia de que la vigilancia depende de un programa sin punto de entrada |
| T-07 | Pendiente | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 0 de 7. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| La prueba se escribe en `pruebas.py` y no arreglando el programa que no corre: es otro archivo y otro problema, ya anotado en el [53](../../../../../pendientes/53-enlaces-py-no-tiene-punto-de-entrada.md) | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| Un rango escrito como «C1–C17» no clasifica diecisiete reglas. Ese error produjo un diagnóstico falso que costó una sesión, y por eso se escribe como prueba y no como confianza | §2.6 del plan y CP-002 del [`plan_pruebas.md`](plan_pruebas.md) |
| La columna del programa va en el registro y no en un documento nuevo: dos documentos sobre lo mismo se separan solos | §2.6 del plan |
| La tabla distingue «no la comprueba nadie porque es humana» de «debería y no está»: sin esa distinción, la clasificación correcta se lee como hueco | Riesgo `R-02` del plan |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del plan.** Es lo único que falta para arrancar.
- **El CA-03 no lo cierra esta fase.** Lo que falta —que la regla sin clasificar no se publique— depende de un programa sin punto de entrada (pendiente [53](../../../../../pendientes/53-enlaces-py-no-tiene-punto-de-entrada.md)). Acá solo queda la evidencia.
- **Si la prueba encuentra reglas sin clasificar otra vez** (riesgo `R-01`): se listan. Clasificarlas es de la fase de [EP-001 · HU-009](../../../EP-001-cuerpo-de-reglas-heredable/HU-009-reglas-sin-checklist-al-dia/A-EP-001-HU-009-clasificar-las-que-faltan/README.md).
- **Si otra sesión está tocando `validadores/pruebas.py`** (riesgo `R-03`): se guarda solo lo propio.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 4 esperando la aprobación del plan, que es la puerta normal, no un bloqueo.
