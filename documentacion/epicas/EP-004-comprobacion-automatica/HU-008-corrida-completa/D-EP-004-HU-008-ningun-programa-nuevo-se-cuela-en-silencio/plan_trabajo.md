# Plan de Trabajo — Fase «D-EP-004-HU-008-ningun-programa-nuevo-se-cuela-en-silencio» (módulo «Comprobación automática»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas` de esta misma fase; lo que quedó hecho, en el `funcionalidad_implementada.md` del cierre.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `D-EP-004-HU-008-ningun-programa-nuevo-se-cuela-en-silencio` |
| **Épica** | [documentacion/epicas/EP-004-comprobacion-automatica/epica.md](../../epica.md) |
| **HU** | [documentacion/epicas/EP-004-comprobacion-automatica/HU-008-corrida-completa/HU-008-corrida-completa.md](../HU-008-corrida-completa.md) — **una sola** (`F12.1`) |
| **Módulo** | Comprobación automática |
| **Especificación del módulo** | La HU citada arriba |
| **Fecha apertura** | 2026-08-31 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- 📝 **Modifica fase(s):** retoma dos criterios que esta misma historia dejó cumplidos y que **el trabajo posterior deshizo sin darse cuenta**. La fase `B` puso la regla de que ningún programa termina en silencio; dos programas nacidos después no la cumplen. Y la fase `A` dejó la corrida terminando con un resumen único; un bloque agregado después quedó **debajo** de ese resumen.

**CA de la HU que cubre esta fase:**

| CA de `HU-008` que cierra esta fase | Estado |
|---|---|
| [CA-03 — El resultado de la corrida es uno solo](../HU-008-corrida-completa.md#ca-03--el-resultado-de-la-corrida-es-uno-solo) | ☐ |
| [CA-04 — Lo que los programas del estándar escriben no pone la corrida en rojo](../HU-008-corrida-completa.md#ca-04--lo-que-los-programas-del-estándar-escriben-no-pone-la-corrida-en-rojo) | ☐ |

---

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que ningún programa del estándar termine con código 0 sin decir nada, y que la corrida completa vuelva a terminar con su resumen.

**Por qué vuelve a hacer falta.** Las dos reglas ya estaban puestas y las dos se rompieron por el mismo camino: **algo nuevo se agregó sin pasar por donde la regla vigila**. Dos programas nacieron después de la fase `B` y nadie corrió su prueba; un bloque de salida se agregó después de la fase `A` y quedó debajo del resumen. La prueba lo dice desde entonces, y nadie la corría — hasta que `EP-005·HU-021` puso a correr las 650.

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-03 | Un programa que no es entrada dice quién lo corre y sale con 2 | Funcional | Baja |
| CA-03 | La corrida completa termina con su resumen | Funcional | Baja |
| CA-04 | La batería interna sin fallas de estas causas | Funcional | Baja |

**Fuera de alcance:**

- La mudanza de `hook_estacion.py`, que es de `EP-005·HU-011` y va en su propia fase, el mismo día.
- Las tres fallas restantes de la batería, que son de otras causas y otras historias.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

### 2.1 Archivos que se crean o modifican

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/comun.py` | Modificar | Común | `no_es_punto_de_entrada` acepta decir **quién** lo corre, cuando no es `validar.py` |
| `validadores/estacion_commit.py` | Modificar | Validador | Dice que lo corre el `post-commit` y sale con 2 |
| `validadores/rutas_fuera.py` | Modificar | Validador | Dice que lo corre el enganche del adaptador y sale con 2 |
| `validadores/validar.py` | Modificar | Punto de entrada | El conteo por regla se imprime **antes** del resumen |
| `validadores/tests/test_ninguno_termina_en_silencio.py` | Modificar | Prueba | Acepta que el corredor no sea `validar.py` |

### 2.2 Matriz de dependencias del refactor

| Archivo a refactorizar | Cambio de contrato | Archivos que dependen | Dónde rompe |
|---|---|---|---|
| `comun.no_es_punto_de_entrada` | Un parámetro nuevo, opcional | Los 40 módulos que ya la llaman | No rompen: el parámetro es opcional y el camino viejo queda igual |

### 2.3 Rutas / endpoints · 2.4 Punto de entrada en la UI · 2.5 Permisos

No aplican.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El mensaje nombra **al corredor de verdad** | Decir «es una pieza de `validar.py`», como los demás | Los dos no cuelgan del validador: mandarían a quien lee a un subcomando que no existe, y un mensaje que se equivoca al indicar es peor que no decir nada |
| Nombrar al corredor **sin su archivo** | Nombrar `hook_rutas.py` y `hook_estacion.py` | Escribir el nombre del enganche hacía que el contador del amarre leyera esos dos programas como amarrados a la herramienta. Un mensaje que **habla de** un enganche no es un enganche |
| El conteo por regla sube; el resumen baja | Recortar el conteo a tres líneas | El conteo dice **qué regla cambiar** y su valor está en verlo entero; lo que tiene que quedar de último es el veredicto |
| La prueba acepta «enganche» además de `validar.py` | Exigir `validar.py` en toda salida | La regla es **decir quién lo corre**, no decir un nombre concreto |

### 2.7 Dudas por resolver antes de codificar

Ninguna abierta.

---

## 3. Desglose de tareas por criterio de aceptación

### [CA-03](../HU-008-corrida-completa.md#ca-03--el-resultado-de-la-corrida-es-uno-solo) — El resultado de la corrida es uno solo

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | `no_es_punto_de_entrada` acepta nombrar al corredor | Común | 1 h | — | EV-01 |
| T-02 | Los dos programas lo usan, cada uno con su corredor real | Validador | 1 h | T-01 | EV-01 |
| T-03 | La prueba acepta un corredor que no sea `validar.py` | Test | 1 h | T-02 | EV-01 |
| T-04 | El conteo por regla se imprime antes del resumen | Punto de entrada | 1 h | — | EV-02 |

### [CA-04](../HU-008-corrida-completa.md#ca-04--lo-que-los-programas-del-estándar-escriben-no-pone-la-corrida-en-rojo) — La batería no queda en rojo por esto

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-05 | Correr la batería interna completa y comparar con la línea base | Test | 1 h | T-03, T-04 | EV-03 |

**Total estimado:** 5 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-05. T-04 es independiente.

---

## 5. Verificación de criterios de aceptación

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| [CA-03](../HU-008-corrida-completa.md#ca-03--el-resultado-de-la-corrida-es-uno-solo) | Correr cada programa solo, y la corrida completa | EV-01, EV-02 | | ☐ |
| [CA-04](../HU-008-corrida-completa.md#ca-04--lo-que-los-programas-del-estándar-escriben-no-pone-la-corrida-en-rojo) | La batería interna completa | EV-03 | | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Las seis pruebas del silencio | `resultado_pruebas.md` §2 |
| EV-02 | Las siete pruebas de la corrida completa | `resultado_pruebas.md` §2 |
| EV-03 | La batería interna | `resultado_pruebas.md` §2 |

---

## 6. Datos y ambiente de prueba

El propio repositorio. Ningún dato real ([`00·N4`](../../../../../base/00-nucleo-blindado.md)).

---

## 7. Reversión / rollback

Todo versionado; `git revert` deshace la fase entera.

---

## 8. Producción y migración incremental

**Aditivo.** Un proyecto instalado no cambia: lo que se toca son programas del estándar y su salida por consola.

---

## 9. Reglas del estándar y del proyecto aplicadas

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F21`](../../../../../base/02-flujo-de-trabajo/reglas/F21-un-incumplimiento-ya-identificado-no-se-repite-en-lo-nuevo.md), [`05·E1`](../../../../../base/05-errores-y-logging.md).
- Proyecto: no aplica.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que ampliar la prueba se lea como aflojarla | Alto — sería el defecto que la fase viene a arreglar | La prueba sigue exigiendo que **diga quién lo corre**; lo que se amplía es qué corredores existen | Cerrado |
| B-02 | Que el parámetro nuevo rompa las cuarenta llamadas que ya existen | Alto | Es opcional, y el camino viejo queda intacto; lo cubre la prueba entera | Cerrado |

---

## 11. Definition of Done

- [ ] Los dos CA verificados con evidencia
- [ ] Pruebas de la fase en verde
- [ ] Batería interna sin fallas de estas causas
- [ ] Señales registradas
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
