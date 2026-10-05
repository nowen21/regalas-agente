# Resultado de Pruebas · Fase `A-EP-004-HU-026-el-validador-avisa-la-funcion-repetida`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-004-HU-026-el-validador-avisa-la-funcion-repetida` |
| **HU** | [HU-026](../HU-026-una-funcion-que-ya-existe-se-avisa-al-crearla.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), versión 1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-04 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Repositorio del estándar en la máquina local, rama `main`, sobre el commit `29a30ad` más los cambios sin guardar, versión 54.1.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 5 | 5 | 5 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Media | `tests_repetidas.py`, las pruebas de `calidad` en `tests.py`, y `calidad` viejo contra el nuevo sobre tres proyectos | `Funciones` separa las dos formas; `calidad` da lo mismo que antes: 13, 188 y 2 avisos | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | `tests_repetidas.py` (2 pruebas) | La copia con otros nombres se avisa en Python y en PHP, como aviso y citando `07·Q4`; ocho copias dan siete avisos que nombran la primera | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Alta | `tests_repetidas.py` (2 pruebas) | El mismo nombre con otro cuerpo y las funciones de una línea no se avisan | Aprobado | EV-01 | Ninguno |
| CP-004 | CA-04 | Alta | `tests_repetidas.py` (1 prueba) | Con `--preparados` se avisa solo la nueva, nombrando la que ya estaba; sin nada nuevo, nada | Aprobado | EV-01 | Ninguno |
| CP-005 | CA-05, RNF-01 | Media | `tests_repetidas.py` (2 pruebas) y `validar.py repetidas` parado en agro-system | Revisa solo el proyecto dado: los 45 avisos de agro-system son suyos; sobre Cimiento tarda 3,5 s | Aprobado | EV-02 | Ninguno |

**Correspondencia con el plan:** 5 casos en el plan, 5 acá.

**Qué salió distinto de lo esperado:** comparar cada par con `difflib` tardaba más de diez minutos en agro-system (3.910 funciones); con un índice de trozos de cinco fichas quedó en diez segundos. Y el umbral medido fue 0,80, no 0,90: con 0,90 se perdía `raiz_pedida`, el caso del pendiente 117.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Umbral y tamaño mínimo | Avisos de Cimiento y agro-system con 0,95, 0,90, 0,85 y 0,80, y lectura de la franja entre 0,80 y 0,90 | Entre 0,80 y 0,90 son copias casi exactas; ver el comentario de `UMBRAL` |

## 4. Defectos encontrados

Ninguno en esta fase.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |
| CA-04 | CP-004 | Aprobado | Sí |
| CA-05 | CP-005 | Aprobado | Sí |
| RNF-01 | CP-005 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 6 de 6 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 5 de 5 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los cinco criterios y el requisito de tiempo tienen sus casos ejecutados y aprobados.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/validadores/codigo.py`, `calidad.py`, `repetidas.py`, `tests_repetidas.py` |
| EV-02 | Subcomando | `proyectos/cimiento/core/herramientas/validar.py` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-04 | 5 | 0 | Primera ejecución |
