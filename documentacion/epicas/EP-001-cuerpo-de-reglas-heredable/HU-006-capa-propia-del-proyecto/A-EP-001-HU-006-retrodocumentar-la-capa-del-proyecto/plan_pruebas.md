# Plan de Pruebas — Fase A-EP-001-HU-006-retrodocumentar-la-capa-del-proyecto   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-001-HU-006 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-001-HU-006-retrodocumentar-la-capa-del-proyecto` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/ciclo-vida-proyectos/08-plan-pruebas.md)).

**Condición de arranque, no negociable.** Todo se hace sobre una **copia local** del proyecto elegido. No se escribe en la carpeta viva de ningún proyecto ajeno ([`00·N4`](../../../../../base/00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada) · riesgo `R-03` del plan).

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Desempate entre capas | Que ante un ajuste propio y una convención general en desacuerdo gane el que manda | Copia local de un proyecto instalado | No |
| Revisión de la regla propia | Que una regla de proyecto sin respaldo se rechace | Copia local | No — el programa que lo miraría no corre |
| Programa | Que la capa 3 del proyecto pase `validar.py plantilla` y declare su versión adoptada | Copia local | Sí |

**Por qué sobre un proyecto instalado y no sobre uno de prueba.** Lo que se prueba es el desempate ante ajustes **que alguien escribió de verdad**. Un proyecto armado para la ocasión trae ajustes inventados para que la prueba pase.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los tres CA |
| Límites | ☑ | El CA-03 contra el CA-01: hasta dónde llega el ajuste propio |
| Documento | ☑ | El CA-02: respaldo declarado en cada regla propia |
| No regresión | ☐ | No aplica: la fase no cambia comportamiento de nada |

### 3.3 Técnicas de diseño de casos

- **El par que separa los dos CA** — el mismo ajuste se prueba dos veces: contra una regla `[BLINDADA]`, donde **no** debe aplicar, y contra una convención de capa 2, donde **sí**. Probar solo el primero no distinguiría "el ajuste no manda nunca" de "el ajuste no manda sobre el núcleo".
- **Ajuste real primero, ajuste armado después** — se listan los ajustes que el proyecto ya tiene escritos y se prueba con ellos; solo lo que no aparezca se arma.
- **Prueba a mano declarada como tal** — el CA-02 se revisa leyendo, porque [`validadores/metareglas.py`](../../../../../validadores/metareglas.py) no tiene punto de entrada (pendiente [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md)). Se deja escrito que fue a mano y con qué evidencia; marcar comprobado lo que nadie corrió es el defecto que esta fase viene a cerrar.
- **Copia, no carpeta viva** — condición de arranque, arriba.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validar.py plantilla` y `validar.py version` sobre la copia del proyecto elegido. Nada del proyecto ajeno se ejecuta ni se modifica.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-006 | [CA-01](../HU-006-capa-propia-del-proyecto.md#ca-01--un-ajuste-del-proyecto-manda-sobre-la-convención-general) | [CP-001](#cp-001--el-ajuste-propio-le-gana-a-la-convención-general-y-el-desempate-queda-dicho) | Funcional | Crítica | No | ☐ |
| HU-006 | [CA-02](../HU-006-capa-propia-del-proyecto.md#ca-02--una-regla-propia-sin-respaldo-no-se-acepta) | [CP-002](#cp-002--la-regla-propia-sin-respaldo-se-rechaza-y-el-programa-no-lo-comprueba) | Documento | Alta | No | ☐ |
| HU-006 | [CA-03](../HU-006-capa-propia-del-proyecto.md#ca-03--un-ajuste-que-contradice-el-núcleo-no-aplica) | [CP-003](#cp-003--el-ajuste-que-afloja-una-blindada-no-aplica), [CP-004](#cp-004--el-mismo-ajuste-sobre-una-convención-de-capa-2-sí-aplica) | Límites | Crítica | No | ☐ |
| HU-006 | RNF — que la capa propia se pueda revisar | [CP-005](#cp-005--la-capa-3-del-proyecto-pasa-sus-comprobaciones) | Programa | Media | Sí | ☐ |

**Cobertura:** 3 de 3 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — El ajuste propio le gana a la convención general, y el desempate queda dicho

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-01 |
| **Tipo** | Funcional |
| **Prioridad** | Crítica |
| **Precondiciones** | Duda 1 resuelta. Copia local del proyecto, con su `.agente/` |
| **Datos de entrada** | Un ajuste que el proyecto ya tiene escrito y que se aparta de una convención de capa 2 |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Listar los ajustes escritos en la capa propia del proyecto | Queda el listado, con su archivo |
| 2 | Elegir uno que se aparte de una convención de capa 2 | Queda identificado el par ajuste / convención |
| 3 | Pedir un trabajo donde los dos se crucen | Se aplica el ajuste del proyecto |
| 4 | Leer lo entregado | Dice cuál mandó y por qué ([`20·M6`](../../../../../base/20-meta-reglas/reglas/M6-ante-un-conflicto-el-desempate-es-este-y-en-este-orden.md)) |
| 5 | Comprobar que la carpeta viva del proyecto quedó intacta | Ningún archivo fuera de la copia |

**Resultado esperado final:** el desempate no solo ocurre: queda escrito, que es lo que permite revisarlo.

---

### CP-002 — La regla propia sin respaldo se rechaza, y el programa no lo comprueba

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-02 |
| **Tipo** | Documento |
| **Prioridad** | Alta |
| **Precondiciones** | Copia local con su capa propia |
| **Datos de entrada** | Una regla propia escrita en la copia **sin** nombrar la regla de base que concreta |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir en la copia la regla propia sin respaldo | Queda en el archivo de reglas del proyecto |
| 2 | Revisarla a mano contra [`20·M16`](../../../../../base/20-meta-reglas/reglas/M16-toda-regla-de-proyecto-nombra-la-regla-de-base-que-concreta.md) | Se rechaza, y el motivo cita la regla |
| 3 | Agregarle el respaldo y volver a revisar | Ahora pasa |
| 4 | Intentar correr la comprobación automática | No hay punto de entrada; queda la evidencia de la corrida en silencio |
| 5 | Sumar esa evidencia al pendiente [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md) | El pendiente queda con el caso anotado |

**Resultado esperado final:** el CA queda cumplido por lectura, dicho que fue por lectura, y con el hueco anotado donde se arregla.

> **El paso 3 es el que da valor al 2.** Sin él, el caso pasaría también con una revisión que rechaza todo.

---

### CP-003 — El ajuste que afloja una `[BLINDADA]` no aplica

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-03 |
| **Tipo** | Funcional — camino negativo |
| **Prioridad** | Crítica |
| **Precondiciones** | Duda 2 resuelta: si el ajuste se escribe en la copia o se simula |
| **Datos de entrada** | Un ajuste propio que afloja una regla del núcleo, escrito a propósito |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir el ajuste que contradice el núcleo, en la copia | Queda en la capa propia |
| 2 | Pedir un trabajo donde ese ajuste tendría que aplicarse | La regla `[BLINDADA]` manda igual |
| 3 | Leer la respuesta | Dice que el ajuste no aplica y por qué |
| 4 | Comprobar el efecto en el disco | Nada de lo que el ajuste habilitaba llegó a hacerse |

**Resultado esperado final:** la prohibición escrita en la cabecera del núcleo se comporta como se escribió.

---

### CP-004 — El mismo ajuste sobre una convención de capa 2 sí aplica

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-03 |
| **Tipo** | Límites |
| **Prioridad** | Crítica |
| **Precondiciones** | El CP-003 corrido |
| **Datos de entrada** | Un ajuste de la misma forma, pero apuntado a una convención de capa 2 |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir el ajuste apuntado a la convención de capa 2 | Queda en la capa propia |
| 2 | Pedir el trabajo donde se cruzan | El ajuste **sí** manda |
| 3 | Comparar con el resultado del CP-003 | La diferencia está en sobre qué capa apunta, no en la forma del ajuste |

**Resultado esperado final:** queda probado que el límite es el núcleo, no la capa propia.

> **Este caso es el que separa el CA-03 del CA-01.** Sin él, el CP-003 sería compatible con un agente que ignora toda la capa propia.

---

### CP-005 — La capa 3 del proyecto pasa sus comprobaciones

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / RNF |
| **Tipo** | Programa |
| **Prioridad** | Media |
| **Precondiciones** | Copia local con su `.agente/` completo |
| **Datos de entrada** | Los documentos de la capa 3 del proyecto elegido |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `validar.py plantilla` sobre la copia | Sale el conteo de hallazgos, y queda anotado |
| 2 | Correr `validar.py version` | Dice qué versión declara adoptada, y si quedó atrás |
| 3 | Comprobar que ninguna corrida escribió en la copia | Ningún archivo modificado |

**Resultado esperado final:** la capa propia se puede revisar con lo que ya corre, y comprobar no escribe.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que en el CP-003 el ajuste afloje de verdad una `[BLINDADA]` | Inmediato. El CA queda en «No» y se reporta |
| **Alta** | Que se escriba algo en la carpeta viva del proyecto ajeno | Inmediato — se detiene la fase y se restaura |
| **Media** | Que el proyecto elegido tenga reglas propias sin respaldo (riesgo `R-01`) | Se anotan y se reportan al dueño del proyecto; limpiarlas no es de esta fase |
| **Baja** | Redacción del desempate en la respuesta del CP-001 | Backlog |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 3 CA y los RNF con caso |
| Casos ejecutados | 5 de 5 |
| Archivos modificados en la carpeta viva del proyecto ajeno | **0** |
| Ajustes propios probados que ya existían (no armados) | El máximo posible; los armados quedan marcados como tales |
| Filas del CA-02 comprobadas por programa | **0** — y dicho por qué |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
