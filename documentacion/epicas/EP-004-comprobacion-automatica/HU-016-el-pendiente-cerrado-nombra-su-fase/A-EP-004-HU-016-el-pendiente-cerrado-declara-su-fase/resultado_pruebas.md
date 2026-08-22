# Resultado de Pruebas — Fase A-EP-004-HU-016-el-pendiente-cerrado-declara-su-fase

**Para qué sirve este documento.** Registra qué se ejecutó y con qué resultado. Los casos viven en el [plan_pruebas.md](plan_pruebas.md), que no se toca al ejecutar.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-004-HU-016-el-pendiente-cerrado-declara-su-fase` |
| **HU** | [HU-016 El pendiente cerrado nombra su fase](../HU-016-el-pendiente-cerrado-nombra-su-fase.md) |
| **Ciclo** | 1 · **Fecha** 2026-08-22 |
| **Ejecutado por** | El agente, por la orden del usuario de resolver el [pendiente 59](../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md) |

### 0.1 Las dos dudas que la detenían

| Duda | Decisión, del pendiente 59 |
|---|---|
| ¿desde cuándo se exige? | **Desde el 2026-08-16**, que es cuando nació la exigencia. Lo cerrado antes no se reabre, igual que `20·M10` con cualquier norma nueva (decisión 26) |
| ¿dónde se declara? | **Una fila fija en la ficha de cabecera**, no una sección: una sección se olvida sin dejar rastro, una fila se ve vacía (decisión 27) |

## 1. Resumen

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos |
|---|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 |

## 2. Caso por caso

| Caso | Qué comprueba | Resultado |
|---|---|---|
| CP-001 · el cerrado sin fase se reporta, el que la nombra no | el corazón del CA | ✅ Aprobado, como **aviso**: ya no rompe nada, solo cortó su rastro |
| CP-002 · la fase inventada se reporta | nombrar una fase que no existe es peor que no nombrar ninguna | ✅ Aprobado: se busca la carpeta en `documentacion/epicas/` |
| CP-003 · el cerrado por decisión no se reporta | no hubo desarrollo, no hay fase que nombrar | ✅ Aprobado |
| CP-004 · lo cerrado antes del corte queda de su lado | la norma no se aplica hacia atrás | ✅ Aprobado, y también lo que no declara fecha |

## 3. Lo que la primera corrida midió

**24 pendientes cerrados desde el 2026-08-16 no dicen en qué fase se hicieron.** Esa es la deuda real, y ahora se puede ver corriendo `validar.py pendientes` en vez de abriendo 35 archivos.

**No se rellenaron acá, y es a propósito.** Averiguar la fase de cada uno exige leer su historia y su commit; hacerlo a las corridas es el camino directo a escribir una fase que no fue. Cada uno lo gana cuando alguien lo toque, y mientras tanto el aviso lo recuerda.

**Y por qué los que no declaran fecha quedan fuera:** los pendientes viejos no la traen, así que exigirles la fase sería aplicar hacia atrás una norma nueva. Treinta avisos que nunca se van apagan la comprobación entera, que es el patrón que este repositorio ya vio cuatro veces.

## 4. Veredicto

**Cumple.** Cuatro casos de cuatro, más ocho automatizados en [`test_pendientes_historia.py`](../../../../../validadores/tests/test_pendientes_historia.py).
