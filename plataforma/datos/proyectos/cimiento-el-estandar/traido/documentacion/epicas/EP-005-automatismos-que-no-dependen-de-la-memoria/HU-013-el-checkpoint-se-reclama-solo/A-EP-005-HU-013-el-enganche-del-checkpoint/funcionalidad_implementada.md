# Funcionalidad implementada — Fase «A-EP-005-HU-013-el-enganche-del-checkpoint» (módulo «Automatismos — enganches»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito **qué quedó hecho**, con la trazabilidad de la especificación y del plan, para que quien llegue después no tenga que deducirlo del código ni del historial.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-005-HU-013-el-enganche-del-checkpoint` |
| **Módulo** | Automatismos — enganches |
| **Especificación del módulo** | [documentacion/automatismos/spec.md](../../../../automatismos/spec.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | [HU-013](../HU-013-el-checkpoint-se-reclama-solo.md) (CA-01, CA-02, CA-03) |
| **Fecha de cierre** | 2026-08-20 |
| **Commit** | se completa al commitear; el usuario lo autoriza aparte |

## 1. Qué se implementó — resumen

Al escribir el plan de trabajo, el resultado de pruebas o el cierre de una fase, un programa mira el `estado-fase.md` de esa fase: si falta o se escribió antes que el documento, avisa nombrando la fase y el documento. Compara fechas; no lee ni escribe el checkpoint. Instalado en los nueve proyectos del registro.

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| RN-32 · tres documentos marcan puerta | programa | `validadores/checkpoint.py` (`DOCUMENTOS_DE_PUERTA`) | ✅ | CP-004 |
| RN-33 · falta o atrasado, nombrando fase y documento | programa | `validadores/checkpoint.py` (`rezago`, `como_texto`) | ✅ | CP-001, CP-002, CP-003 |
| RN-34 · fechas, no contenido; no escribe | programa | `validadores/checkpoint.py` | ✅ | CP-005, CP-007 |
| RN-35 · no detiene | programa | `adaptadores/claude-code/hook_checkpoint.py` | ✅ | CP-006 |
| RN-07 de la HU · llega por el instalador | programa | `validadores/instalar.py` (`HOOKS_CLAUDE`) | ✅ | Salida del instalador, 9 de 9 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-01 | `checkpoint.py`: reconocer la fase, comparar fechas, armar el texto | ✅ hecha | `validadores/checkpoint.py` | 8 casos |
| T-02 | `hook_checkpoint.py`: leer la entrada, llamar, imprimir, salir con 0 | ✅ hecha | `adaptadores/claude-code/hook_checkpoint.py` | CP-001 a CP-006 |
| T-03 | Fila en `HOOKS_CLAUDE` y corrección de la prueba de la frontera | ✅ hecha | `validadores/instalar.py` · `validadores/tests/test_la_frontera_del_adaptador.py` | CP-008 |
| T-04 | Los casos | ✅ hecha | `validadores/tests/test_el_checkpoint_se_reclama_solo.py` | 8 de 8 |
| T-05 | Especificación, mapa del sitio, mapa del amarre | ✅ hecha | `documentacion/automatismos/spec.md` §4.5 y §13 · `anatomia/` | `validar.py amarre`: 22 de 64 |
| T-06 | Instalar en los 9 proyectos y verificar uno | ✅ hecha | `.claude/settings.json` de cada proyecto | AgroSystem trae `hook_checkpoint.py` |

**Correspondencia con el plan:** 6 tareas en el plan, 6 acá.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba**  ·  [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md): ninguno.

**Esfuerzo real contra estimado:** cerca de media hora de sesión contra 3,75 h estimadas. Se sobreestimó: el código es corto; lo que tomó tiempo fue la cadena de documentos, que el plan no cuenta.

## 3. Qué se probó

- **Fuente:** [resultado_pruebas.md](resultado_pruebas.md) · **Veredicto:** Cumple.
- **Suites ejecutadas:** `validadores/tests/test_el_checkpoint_se_reclama_solo.py` 8 de 8; `validadores/tests/` y `validadores/pruebas.py` enteras, ver el resultado §2.
- **Verificaciones manuales:** el instalador corrido sobre los 9 proyectos y el `settings.json` de AgroSystem leído.
- **Defectos abiertos aceptados:** ninguno.

## 4. Cómo se usa / puntos de entrada

- **Punto de entrada:** el enganche `PostToolUse` sobre `Write|Edit`, instalado por `instalar.py`. Se ve como un aviso en la sesión al escribir un documento de puerta.
- **Permisos o datos base:** ninguno.

## 5. Decisiones no obvias  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Comparar fechas, no contenido | Leer el checkpoint es opinar sobre el texto; decir la estación es criterio | S-008 |
| Solo tres documentos disparan | Escribir el plan de pruebas o el README no pasa puerta; avisar ahí es ruido | S-008 |
| El aviso se repite mientras el checkpoint siga atrás | La marca de «ya avisé» exigiría escribir en un archivo del agente | S-008 |
| La prueba de la frontera cuenta contra la lista del instalador | Estaba en rojo desde la 27.0.0 por un número escrito a mano | S-007 (la lección del canal invisible) |

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino |
|---|---|---|
| Los puentes `validadores/hook_*.py` de la 26.0.1 los exime la prueba de la frontera por su docstring | Diferido por el plan | Se quitan cuando todos los proyectos hayan reinstalado; lo decide el usuario |

## 7. Índices y mapas actualizados

- [x] Especificación del módulo actualizada (§4.5, §13 y la tabla de incrementos).
- [x] Mapa del sitio y mapa del amarre al día.
- [x] README de la HU, de la fase y de la épica al día.
- N/A el mapa de dependencias y el catálogo de módulos: no cambió ningún módulo ni ninguna dependencia entre ellos.

## 8. Despliegue

N/A en el sentido de producción: el cambio llega a cada proyecto corriendo `python validadores/instalar.py --todos --aplicar`, que ya se corrió sobre los 9 del registro. Reversión: revertir el commit y volver a correr el instalador.
