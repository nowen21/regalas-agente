# Resultado de Pruebas · Fase `A-EP-025-HU-011-el-vigilante`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-011-el-vigilante` |
| **HU** | [HU-011](../HU-011-el-gasto-llega-a-la-base-en-cuanto-claude-code-lo-escribe.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-05 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Máquina local, rama `main`, sobre el commit `2c3b67b` más los cambios sin guardar; base de pruebas y base real en MariaDB 11.4.9; `watchdog` 6.0.0; versión 55.0.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `LoNuevoSeGuardaCuandoCambia` (3) y `ElVigilanteDeVerdad` (1) | El archivo avisado dos veces se lee una; lo nuevo se suma; lo de un proyecto inactivo, de una carpeta ajena o de fuera de la base no se lee; al arrancar lee lo que quedó; con `watchdog` real lo escrito llega en menos de 5 segundos | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Media | `SeArrancaYSeDetiene` (2), `ElVigilanteArrancaAlIniciarSesion` (5) y `test_quita_el_arranque_del_vigilante` | `--parar` detiene el proceso y borra su número; con uno vivo no arranca otro; la instalación escribe el arranque con `pythonw`, lo arranca y quita la tarea diaria; la desinstalación quita el arranque y lo detiene | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Alta | `test_al_abrir_no_lee_el_jsonl` de `tests_tablero` | Abrir «Gasto» y su parte que se recarga no llama al lector | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 3 casos en el plan, 3 acá.

**Qué salió distinto de lo esperado:** `close_old_connections` de Django cierra también la conexión sana cuando `CONN_MAX_AGE` es 0; se cambió por cerrar solo la que ya no responde. Y dos pruebas que pedían lo contrario de esta HU (la tarea diaria y leer al abrir el tablero) pasaron a probar lo nuevo.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `cd proyectos\cimiento && .venv\Scripts\python.exe manage.py test core.consumo && python -m unittest core.herramientas.tests_desinstalar core.herramientas.tests_instalacion` | Ran 238 tests in 35.275s, OK |
| 2 | En vivo | `programar_vigilante(True)` en esta máquina; `manage.py vigilar_consumo` otra vez; las llamadas de la sesión `c3d82767` en la base | El arranque quedó en la carpeta de inicio; corre como proceso 17076 y no deja arrancar otro; la última llamada guardada era de 8 segundos antes |

## 4. Defectos encontrados

Ninguno abierto.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 3 de 3 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 3 de 3 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los tres criterios pasan, y en vivo la última llamada de esta sesión estaba en la base 8 segundos después de escribirse.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/consumo/tests_vigilante.py` (6), `tests_tablero.py`, `tests_instalacion.py` y `tests_desinstalar.py` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-05 | 3 | 0 | Primera ejecución |
