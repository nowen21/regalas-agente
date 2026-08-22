# Resultado de Pruebas — Fase A-EP-004-HU-011-la-comprobacion-del-molde-se-puede-correr

**Para qué sirve este documento.** Registra qué se ejecutó y con qué resultado. Los casos viven en el [plan_pruebas.md](plan_pruebas.md), que no se toca al ejecutar.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-004-HU-011-la-comprobacion-del-molde-se-puede-correr` |
| **HU** | [HU-011 Molde de las reglas](../HU-011-molde-de-las-reglas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-22 |
| **Ejecutado por** | El agente, por la orden del usuario de resolver el [pendiente 59](../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md) |
| **Ambiente** | El repositorio del estándar en `main`, versión 31.6.0 |

### 0.1 La duda que la detenía, y qué encontró la corrida

**¿Un subcomando con dos modos, o dos subcomandos?** **Uno con dos modos**, y ya estaba construido así: `validar.py metareglas` en seco y `metareglas --catalogo <proyecto>` para el catálogo propio. Es la decisión 38 del pendiente 59, que el propio pendiente marcaba como «se contesta mirando el programa, no decidiendo».

**Pero uno de los cinco casos no pasaba, y ese sí había que construirlo:** el `CP-002` exige que un **identificador repetido** se reporte, y nadie lo miraba.

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos |
|---|---:|---:|---:|---:|
| 1 | 6 | 6 | 6 | 0 |

## 2. Ejecución caso por caso

| Caso | Qué comprueba | Resultado |
|---|---|---|
| CP-001 · el programa corre y no termina en silencio | `validar.py metareglas` imprime y, corrido a mano, muere diciendo por dónde va | ✅ Aprobado |
| CP-002 · el identificador repetido y el de prefijo ajeno se reportan | **el que faltaba** | ✅ Aprobado tras construirlo: cinco casos nuevos en `test_el_identificador_no_se_repite.py` |
| CP-003 · la dependencia inexistente y la que manda sobre una blindada | fila 14 y 15 | ✅ Aprobado: hoy mismo reportó las tres reglas que declaraban extender una blindada |
| CP-004 · la regla sin bloque de checklist se reporta | fila 20 | ✅ Aprobado: llegó a contar 129 sin bloque, y hoy son cero |
| CP-005 · la regla que nombra un lenguaje se reporta | fila 5 | ✅ Aprobado: la lista de tecnologías vive en el propio programa |
| CP-006 · la regla propia sin respaldo se reporta | `--catalogo`, el segundo modo | ✅ Aprobado |

## 3. Lo que se construyó

**La detección del identificador repetido**, dentro de la fila 6 de `metareglas.py`. Reporta en las **dos** reglas en conflicto y nombra las dos rutas: quien lo lea no tiene que buscar la otra a mano.

**Y las derogadas cuentan.** `20·M11` prohíbe reutilizar el ID de una regla derogada, y ese es justo el caso donde alguien lo repetiría sin querer, porque la regla vieja ya no se lee. Hay un caso dedicado.

## 4. Defectos encontrados

**Uno, y era el motivo de la fase:** el identificador único dependía de que nadie se equivocara. Se contó a mano el mismo día —249 identificadores, 249 distintos— y esa fue la señal: el orden estaba bien **por costumbre, no por comprobación**. Ahora hay un caso que corre sobre el cuerpo real y sale en cero.

## 5. Veredicto de la fase

**Cumple.** Seis casos de seis.

| Criterio | Veredicto |
|---|---|
| CA-01 · la comprobación del molde se puede correr | ✅ Cumple |
| CA-02 · el identificador único deja de depender de que nadie se equivoque | ✅ Cumple |
| CA-03 · el catálogo del proyecto se comprueba con el mismo subcomando | ✅ Cumple |
