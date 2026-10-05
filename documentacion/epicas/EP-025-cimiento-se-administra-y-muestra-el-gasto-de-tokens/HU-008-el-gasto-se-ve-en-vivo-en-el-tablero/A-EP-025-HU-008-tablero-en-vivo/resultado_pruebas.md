# Resultado de Pruebas · Fase `A-EP-025-HU-008-tablero-en-vivo`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-008-tablero-en-vivo` |
| **HU** | [HU-008](../HU-008-el-gasto-se-ve-en-vivo-en-el-tablero.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), versión 1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-05 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Máquina local, rama `main`, sobre el commit `29a30ad` más los cambios sin guardar; base de pruebas y base real en MariaDB 11.4.9; versión 54.2.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno. Del CP-001 queda un paso para el usuario: mirar las gráficas en el navegador.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `ElTableroSuma` (2 pruebas), `LaPaginaMuestraElGasto` (3) y la página contra la base real | Totales, proyectos, sesiones, enganches y archivos con los números de la muestra; siete días con hoy al final; la cuenta de consulta ve «1.210» y «5.000» y los datos de las gráficas; sin cuenta, manda a entrar. Contra la base real: 200 en 1,24 segundos, con 12 proyectos | Aprobado | EV-01, EV-02 | Ninguno |
| CP-002 | CA-02 | Media | `SeFiltra` (3 pruebas) | Un proyecto: 1 llamada; 7 días: 2, 30 días: 3; `dias=99`, `dias=abc`, `proyecto=x` y `proyecto=9999` se ignoran | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Alta | `SeActualizaSolo` (3 pruebas) y la parte que se recarga contra la base real | Una llamada nueva aparece en la siguiente recarga; la página pide `/gasto/datos/` cada 10 segundos con sus filtros; abrir la página guarda lo del `.jsonl` y recargar no lo repite. Con el gasto real: 0,02 s (hoy), 0,2 s (7 días) y 0,28 s (30 días, 9369 llamadas) | Aprobado | EV-01, EV-02 | Ninguno |

**Correspondencia con el plan:** 3 casos en el plan, 3 acá.

**Qué salió distinto de lo esperado:** el paso 4 del CP-001 pide ver las gráficas. Claude no tiene navegador: se comprobó que la página trae los datos de las gráficas y ApexCharts, no que se dibujen.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | La página y la parte que se recarga con el gasto real | Cliente de Django con una cuenta temporal, dentro de una transacción que se deshace | Los tiempos del CP-003; la cuenta no quedó |
| 2 | Que lo de las HU-001 a HU-007 siga andando | `manage.py test core.consumo core.proyectos core.niveles core.cuentas core.inicio` | Todas pasan |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |
| RNF-01 | CP-003 | 0,28 s con 30 días de gasto real | Sí |
| RNF-02 | CP-001 | Sin cuenta manda a entrar | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 3 de 3 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 3 de 3 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los tres criterios pasan en la base de pruebas, y contra la base real la página abre y se recarga rápido.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/consumo/tests_tablero.py` (11 pruebas) |
| EV-02 | Base real | Los tiempos de la sección 2 |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-05 | 3 | 0 | Primera ejecución |
