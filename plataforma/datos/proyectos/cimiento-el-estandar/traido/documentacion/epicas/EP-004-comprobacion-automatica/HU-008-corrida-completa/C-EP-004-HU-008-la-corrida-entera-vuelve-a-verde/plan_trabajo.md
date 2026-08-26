# Plan de Trabajo — Fase C-EP-004-HU-008-la-corrida-entera-vuelve-a-verde (módulo Programas de comprobación — la corrida)

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden y sobre qué archivos, y cómo se comprueba cada criterio antes de darlo por cumplido. Se aprueba antes de tocar nada. El requisito vive en la HU; las pruebas, en el [plan_pruebas.md](plan_pruebas.md); lo que dieron, en el [resultado_pruebas.md](resultado_pruebas.md); lo que quedó, en el [funcionalidad_implementada.md](funcionalidad_implementada.md).

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `C-EP-004-HU-008-la-corrida-entera-vuelve-a-verde` |
| **Épica** | [EP-004 Comprobación automática](../../epica.md) |
| **HU** | [HU-008 Corrida completa](../HU-008-corrida-completa.md) — una sola ([`02·F12.1`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) |
| **Módulo** | Programas de comprobación — la corrida |
| **Especificación del módulo** | N/A: la HU es la especificación (`02·F2`, como en las fases A y B de esta historia) |
| **Fecha apertura** | 2026-08-20 |
| **Rama** | `main` — el repositorio del estándar trabaja sobre su rama principal, con el commit autorizado aparte |

**ORIGEN:** 🐛 **Defecto.** Sale del [pendientes/hecho/la-corrida-entera-vuelve-a-verde.md](../../../../../pendientes/hecho/la-corrida-entera-vuelve-a-verde.md): dos pruebas en rojo por causas ajenas a cualquier fase abierta, y dos de los cuatro enlaces reprobados los escriben los enganches en cada sesión.

**CA de la HU que cubre esta fase:**

| CA de HU-008 que cierra esta fase | Estado |
|---|---|
| [CA-04](../HU-008-corrida-completa.md#ca-04--lo-que-los-programas-del-estándar-escriben-no-pone-la-corrida-en-rojo) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que la suite entera termine en `OK`, y que los dos enganches que escriben índices lo hagan con el texto del enlace que `DOC14` pide, para que la próxima sesión no vuelva a ponerla en rojo.

**Fuera de alcance:**

- Cambiar qué dicen los resúmenes o los índices: solo la forma del encabezado y del enlace.
- Lo que el validador de enlaces considera vecino: sigue igual.

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

Leído y medido el 2026-08-20 con `enlaces.reparar_formato(escribir=False)` y `_texto_esperado`:

- `historico-chat/resumenes/2026-08-19/sesion-3.md` línea 11: `### 1 · …` sin la `H-`. `resumen.py` lo cuenta como vacío.
- `evals/README.md` línea 23: `[fixtures/](fixtures/)`; debe decir `evals/fixtures/`.
- `historico-chat/README.md` línea 106: `[resumenes/2026-08-20/…](resumenes/…)`; lo escribe [validadores/historico.py](../../../../../validadores/historico.py) `_enlace_al_resumen` (línea 441: `f" · [{{rel}}]({{rel}})"`), y debe decir `historico-chat/resumenes/…`.
- `historico-chat/resumenes/README.md` líneas 47 y 48: `[2026-08-19/](2026-08-19/)`; lo escribe [validadores/resumen.py](../../../../../validadores/resumen.py) `_indexar_dias` (`linea = f"- [{{dia}}/]({{dia}}/) — …"`), y debe decir `historico-chat/resumenes/2026-08-19/`.
- Los otros índices que escriben los enganches (el del histórico y el del día) enlazan vecinos de la misma carpeta, que `DOC14` admite por su nombre.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/historico.py` | Modificar | `_enlace_al_resumen`: el texto lleva `historico-chat/` adelante |
| `validadores/resumen.py` | Modificar | `_indexar_dias`: el texto lleva `historico-chat/resumenes/` adelante |
| `historico-chat/resumenes/2026-08-19/sesion-3.md` | Modificar | `### 1 ·` → `### H-1 ·` |
| `evals/README.md` · `historico-chat/README.md` · `historico-chat/resumenes/README.md` | Modificar | Los cuatro enlaces ya escritos |
| `validadores/tests/test_los_indices_nacen_legibles.py` | Nuevo | Los casos |

### 2.2 Matriz de dependencias del refactor

No aplica porque no cambia el contrato de ningún código existente: lo que ya llamaba a estos programas sigue llamándolos igual.

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

No aplica porque no hay servicio: son programas de línea de comandos que corren en la máquina de quien trabaja.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

No aplica porque no hay interfaz: el resultado se ve como texto en la consola o en la sesión.

### 2.5 Permisos / roles a sembrar  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Corregir el programa y los cuatro enlaces ya escritos | Solo los cuatro | Sin tocar el programa, la próxima sesión agrega el quinto |
| Los vecinos de la misma carpeta se quedan por su nombre | Ruta completa en todos | Es la excepción que `DOC14` escribe, y el validador ya la respeta |

### 2.7 Dudas por resolver antes de codificar

Ninguna. Todo lo que el plan afirma se leyó en el código el 2026-08-20.

## 3. Desglose de tareas por criterio de aceptación

### CA-04 — en la HU: [CA-04](../HU-008-corrida-completa.md#ca-04--lo-que-los-programas-del-estándar-escriben-no-pone-la-corrida-en-rojo)

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | `_enlace_al_resumen` y `_indexar_dias` escriben el texto con la ruta desde la raíz | Validador | 0,25 h | — | EV-01 |
| T-02 | Renumerar el hallazgo de `sesion-3.md` y corregir los cuatro enlaces escritos | Datos | 0,25 h | — | EV-02 |
| T-03 | Los casos: las dos funciones producen el texto esperado; la suite entera en `OK` | Prueba | 0,5 h | T-01, T-02 | EV-01, EV-02 |

**Total estimado:** 1 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-03. **Paralelizable:** T-02.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)). Descubrir uno nuevo detiene la ejecución y amplía el plan con el OK del usuario.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| [CA-04](../HU-008-corrida-completa.md#ca-04--lo-que-los-programas-del-estándar-escriben-no-pone-la-corrida-en-rojo) | Dos casos unitarios y la suite entera | EV-01, EV-02 | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Suite | `validadores/tests/test_los_indices_nacen_legibles.py` |
| EV-02 | La corrida entera | `resultado_pruebas.md` §2 |

## 6. Datos y ambiente de prueba

Carpetas temporales para las dos funciones; el repositorio para la corrida entera.

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Se revierte el commit. Los cuatro enlaces volverían a la forma vieja y la suite al rojo: es el estado de hoy.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12

Los proyectos instalados reciben el cambio en su próxima sesión: los índices nuevos nacen bien y los viejos se corrigen con `validar.py enlaces --reparar` cuando cada proyecto quiera. Entra en la **27.2.0 (MENOR)** del día.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`13·DOC14`](../../../../../base/13-documentacion/reglas/DOC14-enlaza-cada-md-con-ruta-legible-y-destino-relativo.md), [`08·T1`](../../../../../base/08-pruebas.md#t1--todo-cambio-con-lógica-lleva-prueba), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que otro resumen viejo tenga la misma forma sin `H-` | La corrida sigue en rojo | La prueba del molde recorre los 50; hoy reporta solo uno | Cerrado al medir |

## 11. Definition of Done

- [ ] CA-04 verificado: la suite entera en `OK`
- [ ] Señal registrada
- [ ] Listo para el commit único del día, que el usuario autoriza aparte

## 12. Seguimiento diario

N/A: el trabajo lo lleva una sola persona y el avance va en el `estado-fase.md` §1.2.

## 13. Cierre

**No se escribe acá.** Vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
