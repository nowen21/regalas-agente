# Plan de Trabajo — Fase A-EP-007-HU-008-la-regla-y-el-aviso-de-vuelta (módulo Canal proyecto ↔ estándar)

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden y sobre qué archivos. El requisito vive en [HU-008](../HU-008-el-proyecto-reporta-al-estandar.md); las pruebas, en el [plan_pruebas.md](plan_pruebas.md).

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-007-HU-008-la-regla-y-el-aviso-de-vuelta` |
| **Épica** | [EP-007 Instalación y actualización](../../epica.md) |
| **HU** | [HU-008 El proyecto reporta lo que es del estándar](../HU-008-el-proyecto-reporta-al-estandar.md) — una sola (`F12.1`) |
| **Módulo** | Canal proyecto ↔ estándar |
| **Fecha apertura** | 2026-08-18 |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): ✨ **Funcionalidad nueva.** Primera fase de la historia.

**De dónde sale:** el [pendientes/hecho/el-defecto-del-estandar-se-reporta-y-se-avisa-de-vuelta.md](../../../../../pendientes/hecho/el-defecto-del-estandar-se-reporta-y-se-avisa-de-vuelta.md), reportado por `shopnest-mesa`.

**CA que cubre:** los cuatro de la HU.

---

## 1. Objetivo y alcance

**Objetivo:** que un defecto del estándar encontrado por un proyecto llegue acá, se corrija, y el proyecto se entere — sin que nadie tenga que acordarse de ninguna de las tres cosas.

**El paso que faltaba es el 6.** Los siete los dictó el usuario el 2026-08-16. Los cinco primeros se venían haciendo por criterio de cada sesión; el aviso de vuelta **no lo hacía nadie**, y hay tres cierres anteriores que lo demuestran.

**Fuera de alcance:**

- **Corregir los defectos ya reportados.** Cada uno tiene su propia historia.
- **Avisarle a un proyecto que no esté en el registro o viva en otra máquina.** Se dice cuando pasa, en vez de fallar en silencio.
- **Comprobar que el pendiente del otro lado existe.** Vive en otro repositorio y desde acá no se ve.

---

## 2. Análisis previo — línea base verificada

**Medido el 2026-08-18:**

| Qué | Cuánto |
|---|---|
| Reglas del capítulo `02` | 24, la última `F23` → el libre es **`F24`** |
| Proyectos en el registro | 10 |
| Cierres anteriores con el aviso sin mandar | 3 |

### 2.1 Archivos que se crean o modifican

| Archivo | Tipo | Nota |
|---|---|---|
| `base/02-flujo-de-trabajo/reglas/F24-…md` | Nuevo | La regla, con su bloque de checklist |
| `base/02-flujo-de-trabajo/base.md` | Modificar | Su fila en el índice del capítulo |
| `plantillas/pendiente-reportado.md` | Nuevo | El molde del lado del estándar |
| `plantillas/pendiente-de-seguimiento.md` | Nuevo | El molde del lado del proyecto |
| `validadores/cerrar.py` | Modificar | El aviso de vuelta al cerrar |
| `validadores/pendientes.py` | Modificar | Que el proyecto de origen se nombre |
| `validadores/reglas-validables.md` | Modificar | `F24` clasificada |
| `validadores/tests/test_aviso_de_vuelta.py` | Nuevo | Los casos |
| `CHANGELOG.md` · `VERSION` | Modificar | **MENOR** |

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La regla va al capítulo **`02`** | A la épica de instalación | Lo que gobierna es **un paso del flujo**: qué hace el agente cuando lo que hay que arreglar no es suyo. La instalación es por dónde viaja el aviso, no de qué trata la regla |
| El aviso lo escribe **`cerrar.py`** | Un programa aparte | Ya es quien cierra, y el aviso es parte de cerrar. Separarlo abre la puerta a cerrar sin avisar, que es justo el defecto |
| El aviso escribe **un pendiente y nada más** | Tocar la configuración o el código del proyecto | Escribir en el repositorio ajeno es bastante delicado como para que el alcance sea de una línea. Hay una prueba que lo fija |
| **Idempotente:** cerrar dos veces no duplica | Escribir siempre | Un archivo por cierre; el segundo no tiene nada nuevo que decir |
| La fecha entra por parámetro | Leerla del reloj | El programa no inventa fechas: quien lo corre sabe qué día es |

### 2.7 Dudas por resolver antes de escribir

**Una, y se resolvió con la fila 4 del checklist:** en qué capítulo va la regla. La HU la dejaba abierta entre `01 · Conducta` y `02 · Flujo`. Ver §2.6.

---

## 3. Desglose de tareas

| ID | Tarea | Est. |
|---|---|:--:|
| T-01 | Comprobar el identificador libre del capítulo `02` | 0,25 h |
| T-02 | Escribir `F24` con su bloque de checklist | 1 h |
| T-03 | Las dos plantillas del pendiente | 0,75 h |
| T-04 | El aviso de vuelta en `cerrar.py` | 1,5 h |
| T-05 | Que el proyecto de origen se nombre, en `pendientes.py` | 0,5 h |
| T-06 | Los casos de prueba | 1 h |
| T-07 | Clasificar y versionar | 0,25 h |

**Total estimado:** 5,25 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-04 → T-06.

**T-02 va antes que T-04.** Escribir el programa antes que la regla sería construir sin saber qué se exige — el defecto que [`02·F2`](../../../../../base/02-flujo-de-trabajo/reglas/F2-sin-spec-acordada-no-hay-codigo.md) prohíbe.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación

| CA | Método | Estado |
|---|---|---|
| CA-01 · los dos pendientes | Las dos plantillas, cada una nombrando a la otra | ☑ |
| CA-02 · sin proyecto de origen se reporta | `validar.py pendientes` | ☑ |
| CA-03 · el aviso llega solo al de origen | Prueba sobre tres proyectos de mentira | ☑ |
| CA-04 · «a todos» llega a todos | La misma prueba, con la ficha cambiada | ☑ |
| Transversal · errores | El proyecto sin backlog y el que no está en el registro | ☑ |
| No regresión | Las dos suites | ☑ |

---

## 6. Datos y ambiente de prueba

Proyectos de mentira en carpetas temporales. **Nunca un proyecto real** ([`00·N4`](../../../../../base/00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada)) — y acá pesa más que de costumbre, porque el programa escribe en repositorios ajenos.

---

## 7. Reversión / rollback

Se revierte volviendo el commit atrás. Los avisos ya escritos en otros proyectos **no se recogen solos**: son archivos de ese repositorio y se borran allá.

---

## 8. Producción y migración incremental

**Es aditiva.** Un proyecto al día no tiene que hacer nada; lo que cambia es que la próxima vez que reporte un defecto va a recibir el aviso de vuelta.

---

## 9. Reglas del estándar aplicadas

[`02·F2`](../../../../../base/02-flujo-de-trabajo/reglas/F2-sin-spec-acordada-no-hay-codigo.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar), [`20·M4`](../../../../../base/20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md), [`20·M5`](../../../../../base/20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md), [`20·M9`](../../../../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md), [`20·M14`](../../../../../base/20-meta-reglas/reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Acción | Estado |
|---|---|---|---|
| B-01 | Escribir en el repositorio de otro proyecto sin que nadie lo autorizara | Solo un archivo de pendiente, nunca código; y solo a proyectos del registro. Con prueba | **Cerrado** |
| B-02 | Que el aviso se duplique al cerrar dos veces | Idempotente por nombre de archivo. Con prueba | **Cerrado** |
| B-03 | Que el procedimiento quede escrito y nadie lo siga, como `ID9` | Dos de los cuatro CA son comprobaciones, no recordatorios | **Cerrado a medias** — el aviso corre solo; que el proyecto lo compruebe, no |
| B-04 | Los tres cierres anteriores que quedaron sin aviso | No se mandan hacia atrás: se anota cuáles y quién los espera | Abierto |
| B-05 | Que el aviso quede escrito y el comando no lo llame | **Pasó.** Las pruebas llamaban a `avisar()` directo, así que la pieza estaba bien y desconectada. Corregido en la 23.7.1 | **Cerrado** |

---

## 11. Definition of Done

- [x] `F24` escrita, con su checklist en **CUMPLE**
- [x] Las dos plantillas, cada una nombrando a la otra
- [x] El aviso de vuelta funcionando, con sus casos
- [x] El proyecto de origen comprobado por programa
- [x] Clasificada y versionada
- [ ] Aceptada por el usuario
- [x] `shopnest-mesa` avisado el 2026-08-18, al cerrar el 36. **Los demás no:** ocho de nueve no tienen carpeta `pendientes/` — el [61](../../../../../pendientes/61-el-aviso-de-vuelta-llega-a-uno-de-nueve.md)

---

## 13. Cierre

**No se escribe acá.** Vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
