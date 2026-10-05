# Resultado de Pruebas · Fase `A-EP-004-HU-027-el-control-avisa-las-reglas-parecidas`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-004-HU-027-el-control-avisa-las-reglas-parecidas` |
| **HU** | [HU-027](../HU-027-una-regla-parecida-se-avisa-al-crearla.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), versión 1.0, con el paso 3 de CP-001 que sumó el cambio del 2026-10-05 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-05 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Repositorio del estándar en la máquina local, rama `main`, sobre el commit `29a30ad` más los cambios sin guardar, versión 54.3.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01, RNF-01 | Alta | `tests_parecidas.py` (2 pruebas) y el enganche corrido tres veces sobre la escritura de `F25` | El enganche nombra `02·F4` y `02·F8` entre las parecidas, sale con 0 y tarda entre 1,5 y 2,1 s; la tabla traduce las 257 reglas con los mismos números que la librería | Aprobado | EV-01, EV-02 | Ninguno |
| CP-002 | CA-02 | Alta | `tests_parecidas.py` (2 pruebas) | `--regla F25` da un aviso con `02·F4`; con una regla preparada en un repositorio de prueba, un aviso; sin nada preparado, ninguno | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Media | `tests_parecidas.py` (2 pruebas) | Con la búsqueda apagada, el subcomando y el enganche dicen que no pudieron buscar y no nombran ninguna regla | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 3 casos en el plan, 3 acá.

**Qué salió distinto de lo esperado:** con el texto entero de cada regla, `02·F4` no salía entre las seis primeras de `02·F25`, porque casi todos los pares quedaban entre 0,85 y 0,91; con el título y la exigencia sale primera. Y abrir el modelo tardaba de 2 a 6 s, más de lo que permite el RNF-01: se cambió a la tabla de palabras en una base de datos, con aprobación del usuario el 2026-10-05.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Umbral y texto que se compara | Puesto de `02·F4` para `02·F25` y parecidas por regla con 0,80 a 0,85, sobre tres textos distintos | Con 0,85 cada regla tiene en promedio tres parecidas; ver el comentario de `UMBRAL` |

## 4. Defectos encontrados

Ninguno en esta fase.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |
| RNF-01 | CP-001 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 4 de 4 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 3 de 3 | Sí |

Corren también sin fallas las pruebas de reglas (140) y las del enganche de reglas relacionadas (14).

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los tres criterios y el requisito de tiempo tienen sus casos ejecutados y aprobados.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/validadores/parecidas.py`, `relacionadas.py`, `tests_parecidas.py` |
| EV-02 | Enganche y mediciones | `adaptadores/claude-code/hook_relacionadas.py`; `historico-chat/scripts/2026-10-05/` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-05 | 3 | 0 | Primera ejecución |
