# Resultado de Pruebas · Fase `A-EP-025-HU-005-el-freno-lee-los-niveles`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-005-el-freno-lee-los-niveles` |
| **HU** | [HU-005](../HU-005-el-freno-aplica-el-nivel-guardado-y-sin-base-no-deja-modificar.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), versión 1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-05 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Máquina local, rama `main`, sobre el commit `29a30ad` más los cambios sin guardar; MariaDB 11.4.9; PyMySQL 1.2.3 en el `.venv` de Cimiento y en el Python general; versión 54.2.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `ElNivelDeLaRegla` (8 pruebas), `ElFrenoLeeLosNivelesGuardados` (5) y las 308 de antes | Sin fila detiene por `02·F8`; «avisa» pasa con su motivo, también por consola y fuera del proyecto con `04·S9`; «apagada» pasa sin motivo; otra regla no cambia nada; después de una orden, «avisa» va aparte y «apagada» no aparece; el lector trae el nivel solo del proyecto activo que lo tiene, sin distinguir mayúsculas | Aprobado | EV-01, EV-02 | D-01, corregido |
| CP-002 | CA-02 | Alta | `test_el_nucleo_siempre_frena` | Publicar sigue preguntando; `00·N1` con fila en «apagada» frena | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Alta | `SinBaseNoSeModifica` (5 pruebas) y el enganche como proceso con `DB_PUERTO=3399` | Escribir lo declarado y una orden que escribe: «sin_base» con «hay que prenderla»; leer pasa; después de una orden, un solo aviso; el lector real nombra `127.0.0.1:3399`; el enganche responde `deny` con «[EL FRENO NO TIENE BASE DE DATOS]» | Aprobado | EV-01, EV-03 | Ninguno |
| CP-004 | CA-04 | Media | `PyMySQLParaElFreno` (4 pruebas) y la simulación de la instalación del estándar | Con PyMySQL no hace nada; sin él lo anuncia o lo instala con el mismo Python; si falla queda «OMITIDO»; la simulación muestra el paso | Aprobado | EV-04 | Ninguno |

**Correspondencia con el plan:** 4 casos en el plan, 4 acá.

**Qué salió distinto de lo esperado:** el `.venv` de Cimiento no tenía PyMySQL y las pruebas corren ahí (D-01).

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | El enganche de antes, como lo corre Claude Code | `hook_antes.py` como proceso, sobre un proyecto temporal, con la base y con un puerto sin servidor | `deny` con «EL FRENO DETUVO» y con «EL FRENO NO TIENE BASE DE DATOS» |
| 2 | Que lo de las HU-001 a HU-004 siga andando | `manage.py test core.niveles core.proyectos core.cuentas core.inicio` | 68 pruebas, todas pasan |
| 3 | Que esta sesión siga trabajando con el freno nuevo | Las escrituras de la fase después del cambio | Pasaron: el estándar no está registrado y todo frena como antes |

## 4. Defectos encontrados

| ID | Caso | Qué pasó | Esperado | Obtenido | Estado |
|---|---|---|---|---|---|
| D-01 | CP-003 | El lector real en las pruebas | `BaseSinRespuesta` con el puerto | «falta PyMySQL»: el `.venv` de Cimiento no lo tenía | Corregido: PyMySQL en `requirements/base.txt` y `lock.txt`, agregados al plan antes de tocarlos |

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |
| CA-04 | CP-004 | Aprobado | Sí |
| RNF-01 | CP-001 | Una conexión y una consulta, sin Django | Sí |
| RNF-02 | CP-003 | Sin base no se modifica | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 4 de 4 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 4 de 4 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los cuatro criterios tienen sus casos ejecutados y aprobados, y las 308 pruebas de antes del freno siguen pasando.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Freno y pruebas | `proyectos/cimiento/core/enganches/freno.py`, `proyectos/cimiento/core/enganches/tests_freno.py` (322 pruebas) |
| EV-02 | Lector y pruebas | `proyectos/cimiento/core/enganches/niveles.py`, `proyectos/cimiento/core/niveles/tests_lectura.py` |
| EV-03 | Enganches | `adaptadores/claude-code/hook_antes.py`, `adaptadores/claude-code/hook_despues.py` |
| EV-04 | Instalador y pruebas | `proyectos/cimiento/core/herramientas/instalar.py`, `proyectos/cimiento/core/herramientas/tests_instalacion.py`, `validadores/instalar.py` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-05 | 4 | 0 | Primera ejecución |
