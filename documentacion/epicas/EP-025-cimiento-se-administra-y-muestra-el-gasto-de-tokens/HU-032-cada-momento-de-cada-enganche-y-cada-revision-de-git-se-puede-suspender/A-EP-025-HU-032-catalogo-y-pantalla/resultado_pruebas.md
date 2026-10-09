# Resultado de Pruebas · Fase `A-EP-025-HU-032-catalogo-y-pantalla`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-032-catalogo-y-pantalla` |
| **HU** | [HU-032](../HU-032-cada-momento-de-cada-enganche-y-cada-revision-de-git-se-puede-suspender.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-09 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Python 3.11.9 de `proyectos/cimiento/.venv/`, la base de pruebas de Django, Windows 11; versión 56.8.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 2 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Crítica | `test_cada_momento_tiene_nombre_y_solo_el_freno_se_repite`, `test_los_momentos_y_las_revisiones_no_comparten_nombre` | Los 24 momentos tienen nombre; solo «freno» se repite, en sus dos enganches; las revisiones y lo que no conviene están en el catálogo | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-01 | Crítica | `test_el_historico_y_una_revision_de_git_se_suspenden`, `test_un_nombre_fuera_del_catalogo_se_rechaza`, `test_la_pantalla_muestra_la_recomendacion`, `test_el_enganche_sin_nombre_se_guarda_como_freno` | Se guardan `historico-del-usuario` y `git-versionado`; `hook_inventado.py` se rechaza; la pantalla muestra la tabla con la advertencia del histórico; sin nombre queda «freno» | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 2 casos en el plan, 2 acá.

**Qué salió distinto de lo esperado:** el formulario pedía el nombre antes de poder decir que un enganche sin nombre es el freno; se dejó opcional.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `python manage.py test core.proyectos.tests_suspender_enganches core.proyectos.tests_configuracion core.ayuda` | Ran 35 tests in 21.507s, OK |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001, CP-002 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 1 de 1 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 2 de 2 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los 2 casos pasan, y las 33 pruebas de configuración y de ayuda siguen pasando.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `core/comun/enganches.py`, `core/proyectos/ajustes.py`, `forms.py`, `views.py`, `templates/proyectos/suspensiones.html`, `core/ayuda/textos.py`, `core/proyectos/tests_suspender_enganches.py` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-09 | 2 | 0 | Primera ejecución |
