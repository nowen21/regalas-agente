# Resultado de Pruebas · Fase `A-EP-025-HU-029-reinicio-solo`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-029-reinicio-solo` |
| **HU** | [HU-029](../HU-029-el-vigilante-se-reinicia-solo-cuando-cambia-su-codigo.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-08 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | La base de pruebas de Django y esta máquina, con el vigilante de verdad; versión 58.0.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 2 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `tests_reinicio`: `QueCuentaComoCodigo`, `test_varios_cambios_seguidos_dan_un_solo_reinicio`, `ElAvisoDeVerdad` | Solo el código de Cimiento cuenta; tres cambios seguidos dan un reinicio; `watchdog` avisa del `.py` escrito | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | `ElRelevo`, `ArrancaSinConsola` y el relevo de verdad | El viejo se detiene cuando el nuevo escribe su número; si el nuevo no arranca, el viejo sigue. En esta máquina el número pasó de 29208 a 36248 y quedó uno solo | Aprobado | EV-01, EV-02 | Ninguno |

**Correspondencia con el plan:** 2 casos en el plan, 2 acá.

**Qué salió distinto de lo esperado:** al primer arranque desde el `.cmd`, el vigilante murió enseguida: sin consola, el primer mensaje lo tumbaba (H-41). Se corrigió con `sin_consola` y su prueba, y el segundo arranque quedó bien.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `proyectos\cimiento\.venv\Scripts\python.exe proyectos\cimiento\manage.py test core.consumo core.ayuda --noinput` | OK |
| 2 | El relevo de verdad | Cambiarle la fecha a `core/consumo/reinicio.py` con el vigilante corriendo | El número cambió de 29208 a 36248 en menos de 30 segundos |
| 3 | El trabajo de los mensajes nuevos | `manage.py recalcular_trabajo` | 0 de 3.720 sin trabajo |

## 4. Defectos encontrados

Uno, corregido en la fase: el vigilante no arrancaba sin consola (H-41).

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| RNF-01 | CP-001 | Aprobado: `test_no_tiene_relojes` sigue en verde | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 2 de 2 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 2 de 2 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** las pruebas pasan y el vigilante de esta máquina se relevó solo al cambiar su código.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/consumo/tests_reinicio.py` |
| EV-02 | El relevo en esta máquina | `historico-chat/scripts/2026-10-08/salida_reinicio.txt` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-08 | 2 | 0 | Primera ejecución |
