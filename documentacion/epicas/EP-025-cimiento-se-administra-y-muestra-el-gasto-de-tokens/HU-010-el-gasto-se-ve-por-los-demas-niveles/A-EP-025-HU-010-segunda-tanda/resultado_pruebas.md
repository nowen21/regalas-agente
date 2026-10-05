# Resultado de Pruebas · Fase `A-EP-025-HU-010-segunda-tanda`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-010-segunda-tanda` |
| **HU** | [HU-010](../HU-010-el-gasto-se-ve-por-los-demas-niveles.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), versión 1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-05 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Máquina local, rama `main`, sobre el commit `29a30ad` más los cambios sin guardar; base de pruebas y base real en MariaDB 11.4.9; versión 54.2.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `ElTrabajoSaleDeLasRutas` (2), `LaPalabraClaveEsLaDeLaLista` (1) y `ElGastoQuedaPorMensajePalabraYTrabajo` (4) | «Hágalo» con la fase, «Analicemos» con «análisis 2 del pendiente 119» y un mensaje sin palabra ni trabajo; cada llamada con su mensaje; el texto no queda en la base; un turno leído en dos veces sigue con su mensaje; leer otra vez no duplica | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Media | `ElGastoQuedaPorHerramientaYAgente` (3) | Edit, Bash y Read con el tamaño de su resultado; el auxiliar con «Explore» y sin mensaje, y su tarea no cuenta como mensaje; la telemetría guarda Bash con 300 y une la llamada al mensaje «p-2» | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Media | `ElTableroMuestraLosSieteNiveles` (2) y la base real | Palabra, trabajo, modelo, tipo de token, herramienta, contexto y mensajes con los números de la muestra; la página trae las ocho secciones. Con el gasto real: 0,33 s (hoy), 0,35 s (7 días), 0,58 s (30 días) | Aprobado | EV-01, EV-02 | Ninguno |

**Correspondencia con el plan:** 3 casos en el plan, 3 acá.

**Qué salió distinto de lo esperado:** la prueba de la HU-006 que exigía no leer `subagents/` pasó a exigir que se lean, como pide esta HU.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Los niveles nuevos con el gasto real | Migración `0003`; se borró el avance de lectura y se corrió `leer_consumo` (1 min 38 s) | 2988 mensajes, 13 160 usos de herramientas, 880 llamadas de auxiliares (general-purpose 738, Explore 112, claude-code-guide 30); 1851 mensajes sin palabra clave, casi todos de antes de `01·C28` |
| 2 | Que lo de las HU-006 a HU-009 siga andando | `manage.py test core.consumo core.proyectos` y `core.enganches.tests_limites` | Todas pasan |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |
| RNF-01 | CP-003 | 0,58 s con 30 días de gasto real | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 3 de 3 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 3 de 3 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los tres criterios pasan en la base de pruebas, y con el gasto real los niveles se llenan y el tablero responde en menos de un segundo.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/consumo/tests_segunda_tanda.py` (12 pruebas) |
| EV-02 | Base real | Los conteos y tiempos de las secciones 2 y 3 |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-05 | 3 | 0 | Primera ejecución |
