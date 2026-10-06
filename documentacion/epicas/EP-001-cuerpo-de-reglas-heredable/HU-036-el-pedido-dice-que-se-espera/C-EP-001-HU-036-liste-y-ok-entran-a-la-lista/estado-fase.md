# Estado de fase · Fase C-EP-001-HU-036-liste-y-ok-entran-a-la-lista (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `C-EP-001-HU-036-liste-y-ok-entran-a-la-lista` |
| **Módulo** | Cuerpo de reglas |
| **Planteamiento / Épica / HU** | [EP-001](../../epica.md) / [HU-036](../HU-036-el-pedido-dice-que-se-espera.md) / decisión del usuario del 2026-10-06, en la sesión [la palabra clave que dice qué hacer](../../../../../historico-chat/resumenes/2026-08-31/la-palabra-clave-que-dice-que-hacer.md) |
| **Última actualización** | 2026-10-06 |

## 1. En qué estación va

**Estación actual:** 12, commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ Leídos el anexo, `C28`, `recuperar.py` y la fase B |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ El usuario decidió que el cambio lleva cadena |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-001 ya existe |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ HU-036 ya existe |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ La HU y su anexo son la especificación |
| 6 | Diseñador | diseño coherente | ☑ Las filas se leen del anexo, sin tocar código |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ «apruebo» del usuario, el 2026-10-06 |
| 8 | Implementador | implementado + pruebas verdes | ☑ Las 4 tareas, 3 de 3 pruebas en verde |
| 9 | Verificador | trazabilidad sin faltantes | ☑ `validar.py fases` sin fallas |
| 10 | Crítico | sin hallazgos graves | ☑ El freno detuvo un intento fuera de plan; quedó en el resultado |
| 11 | Cierre documental + señales | docs y señales al día | ☑ Resultado, funcionalidad, HU y bitácora |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

**La fase arranca con el cambio ya subido.** El anexo, el sello de `C28`, el registro y la versión quedaron en el commit `634b28a`, antes de que la fase existiera. Lo que le falta a esta fase son las pruebas y los índices, no el cambio. El plan de trabajo lo declara en su ORIGEN.

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | Cumple |
| **CA cumplidos** | 2 de 2 |
| **CA en «No»** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | `resultado_pruebas.md` |

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Hecha | `core/herramientas/tests_liste_y_ok.py`, 3 casos |
| T-02 | Hecha | La celda dice «Nada: es el acuse de recibo de una explicación» |
| T-03 | Hecha | CP-003, en verde |
| T-04 | Hecha | Índices de la HU: su README y la tabla de fases. Va con la apertura, no con la ejecución del plan |

**Hechas:** 4 de 4. **Bloqueadas:** ninguna.

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Qué | Decisión |
|---|---|
| Si el cambio lleva cadena | Sí, como fase `C` de esta HU, decidido por el usuario el 2026-10-06 |
| La pregunta entre `¿?` | Descartada en la sesión del 2026-08-31, con su motivo escrito en el plan |
| La celda de `OK` | Cambiada al aprobar el plan: dice que no autoriza nada |

## 3. Pendiente / preguntas abiertas

Ninguna. Falta el commit de la fase, que se pide aparte.

## 4. Si se bloqueó

No aplica.
