# Resultado de Pruebas · Fase C-EP-005-HU-002-claves-de-anthropic-y-con-prefijo   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra qué se ejecutó de verdad y con qué resultado, y de ahí sale el **veredicto** de la fase: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el `estado-fase.md` para pasar la puerta de verificación, y la fuente de la sección *Qué se probó* del `funcionalidad_implementada.md`. El diseño de los casos vive en el `plan_pruebas.md` de esta misma fase, que no se modifica al ejecutar: se aprobó antes y así se queda.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `C-EP-005-HU-002-claves-de-anthropic-y-con-prefijo` |
| **HU** | [HU-002](../HU-002-enmascarar-claves.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-06 |
| **Ejecutado por** | El agente |
| **Ambiente y versión** | Cimiento local, sobre el commit `2513a97` con los cambios de la fase sin guardar, versión 55.3.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

**[CA-03](../HU-002-enmascarar-claves.md#ca-03--las-claves-de-anthropic-y-las-variables-con-prefijo-también-se-tapan) con CP-001 a CP-004, que las claves de Anthropic y las variables con prefijo se tapen y se señalen**

**El problema que resuelve:** sin esto, una clave de Anthropic queda en claro en la base, en el histórico o en un commit.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Antes del cambio, tapar `sk-ant-...`, `ANTHROPIC_API_KEY=`, `GITHUB_TOKEN="..."`, `DB_PASSWORD="..."` y `OPENAI_API_KEY:` | Línea base | Las cinco quedaron en claro: 0 tapadas |
| 2 | Después del cambio, lo mismo | Las cinco tapadas | 1 tapada en cada una, y el valor ya no aparece |
| 3 | Tapar lo que lee del entorno, un molde, el nombre solo y `max_tokens=4096` | Nada | 0 en las cuatro |
| 4 | En `proyectos/cimiento/`, correr `.venv/Scripts/python manage.py test core.enganches.tests_claves_con_prefijo core.enganches.tests_sesion core.validadores core.consumo.tests_lineas` | En verde | `Ran 569 tests in 532.227s` y `OK (skipped=4)` |
| 5 | En la raíz, correr `python validadores/validar.py secretos` | Sin fallas nuevas por esta fase | 9 fallas y 3 avisos, todos de formas que ya existían (AWS, Stripe, `password`, `API_KEY`) en archivos ya versionados; ninguno de Anthropic ni de prefijo |

**Cómo se verificó que la pareja cumple:** el paso 1 deja la línea base y el 2 decide; el 3 cubre lo que no hay que tapar; el 4 trae las pruebas automáticas, que no repiten la clave al fallar; el 5 muestra que el validador no señala nada nuevo en el repositorio.

| Caso | CA | Prioridad (del plan) | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-03 | Crítica | 2026-10-06 | Clave `sk-ant-` armada al correr: tapada | Aprobado | EV-01 | — |
| CP-002 | CA-03 | Crítica | 2026-10-06 | `ANTHROPIC_API_KEY=`, `OPENAI_API_KEY:`, `GITHUB_TOKEN`, `DB_PASSWORD` y `APP_SECRET`: tapadas | Aprobado | EV-01 | — |
| CP-003 | CA-03 | Crítica | 2026-10-06 | Entorno, molde, nombre solo y `max_tokens`: sin tocar | Aprobado | EV-01 | — |
| CP-004 | CA-03 | Crítica | 2026-10-06 | `revisar_texto` señala la clave de Anthropic y la variable con prefijo; `validar.py secretos` sin fallas nuevas; 569 pruebas en verde | Aprobado | EV-02, EV-03 | — |

**Correspondencia con el plan:** 4 casos en el plan, 4 acá.

**Qué salió distinto de lo esperado:** nada.

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

Ninguna.

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU (`CA-0N` · `RNF-0N`) | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| [CA-03](../HU-002-enmascarar-claves.md#ca-03--las-claves-de-anthropic-y-las-variables-con-prefijo-también-se-tapan) | CP-001 a CP-004 | Aprobados | Sí |

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura | Plan §5 | 100 % | 1 de 1 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** el único criterio de la fase tiene sus cuatro casos aprobados, y el validador no señala nada nuevo en el repositorio.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Salida de `tests_claves_con_prefijo` | §2 |
| EV-02 | Salida de las suites | §2 |
| EV-03 | Salida de `validar.py secretos` | §2 |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-06 | 4 | 0 | Primera ejecución |
