# Plan de Pruebas — Fase A-EP-003-HU-002-retrodocumentar-los-modelos-del-encargo   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-003-HU-002 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-003-HU-002-retrodocumentar-los-modelos-del-encargo` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/ciclo-vida-proyectos/08-plan-pruebas.md)).

**Los modelos no se corrigen acá.** Lo que les falte se propone: son `plantillas/` y suben versión ([`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)).

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Unitario sobre el árbol | Que toda HU nombre su épica y toda épica liste sus HU | Lectura de `documentacion/epicas/` | Sí |
| Revisión de criterios | Que cada CA diga cómo se valida y cuándo se aprueba | Este repositorio | No |
| Negativa | Que un encargo llenado a medias salga reportado | Copias en carpeta temporal | Sí |

**Sobre qué se prueba el encadenamiento.** Sobre las **HU reales** del árbol, no sobre una épica armada para la ocasión: las reales traen los casos raros que un ejemplo inventado no tiene.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los tres CA |
| Negativa | ☑ | El CA-03: el hueco tiene que salir reportado |
| Documento | ☑ | La forma de los criterios de aceptación |
| No regresión | ☑ | La suite que ya existe, contra su número anotado antes |

### 3.3 Técnicas de diseño de casos

- **Encadenamiento en los dos sentidos** — de la HU hacia la épica y de la épica hacia sus HU. Con un solo sentido, una HU huérfana o una épica que se olvidó de listar una historia pasarían sin verse.
- **El par a medias / completo** — el CA-03 no se cierra viendo que el validador existe: se cierra comprobando que **reporta cuando falta** y **calla cuando está completo**.
- **Muestra elegida por dificultad** — las tres HU del CA-02 se eligen por tener criterios difíciles de comprobar, no por ser las más prolijas.
- **La carencia se documenta, no se tapa** — el estándar no tiene planteamiento propio (pendiente [56](../../../../../pendientes/56-el-estandar-no-tiene-planteamiento.md)). Escribirlo leyendo el repositorio saldría describiendo la solución en vez del problema, y apagaría el aviso sin arreglar nada. Queda dicho.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validar.py plantilla` y `trazabilidad` sobre este repositorio, más `validadores/pruebas.py` entera.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-002 | [CA-01](../HU-002-modelos-del-encargo.md#ca-01--los-tres-modelos-existen-y-se-encadenan) | [CP-001](#cp-001--toda-hu-nombra-su-épica-y-toda-épica-lista-sus-hu) | Funcional | Alta | Sí | ☐ |
| HU-002 | [CA-02](../HU-002-modelos-del-encargo.md#ca-02--la-historia-trae-criterios-que-se-pueden-comprobar) | [CP-002](#cp-002--cada-criterio-dice-cómo-se-valida-y-cuándo-se-aprueba) | Documento | Alta | No | ☐ |
| HU-002 | [CA-03](../HU-002-modelos-del-encargo.md#ca-03--un-encargo-llenado-a-medias-se-nota) | [CP-003](#cp-003--el-encargo-a-medias-sale-reportado-y-el-completo-pasa) | Negativa | Crítica | Sí | ☐ |
| HU-002 | RNF — que el modelo se entienda sin explicación | [CP-004](#cp-004--el-planteamiento-que-le-falta-a-esta-casa-queda-dicho) | Documento | Media | No | ☐ |

**Cobertura:** 3 de 3 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — Toda HU nombra su épica, y toda épica lista sus HU

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-01 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Ninguna: la prueba lee el árbol y no escribe |
| **Datos de entrada** | Todas las HU y todas las épicas del repositorio |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Contar cuántas HU y cuántas épicas hay | Queda el número, con la fecha de la cuenta |
| 2 | Por cada HU, comprobar que nombra su épica con enlace | Ninguna huérfana |
| 3 | Por cada épica, comprobar que lista sus HU | Ninguna historia sin listar |
| 4 | Cruzar las dos direcciones | Los dos conjuntos coinciden |
| 5 | Listar las que fallen, con su archivo | Se anotan; corregirlas es trabajo de la fase de cada HU |

**Resultado esperado final:** la cadena planteamiento → épica → historia se puede recorrer en los dos sentidos.

> **El paso 4 es el que sirve.** Que cada HU nombre una épica no impide que una épica se haya olvidado de listar una historia.

---

### CP-002 — Cada criterio dice cómo se valida y cuándo se aprueba

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-02 |
| **Tipo** | Documento |
| **Prioridad** | Alta |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | Tres HU elegidas **por tener criterios difíciles de comprobar** |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Tomar las tres HU y sus criterios | Quedan a la vista, con cuántos criterios son |
| 2 | Por cada criterio, responder con qué se comprobaría | Hay una respuesta concreta, no "se revisa" |
| 3 | Por cada criterio, responder cuándo se da por aprobado | Hay una condición observable |
| 4 | Anotar el criterio que no permita responder | Queda como hallazgo, sin reescribir la HU |

**Resultado esperado final:** un criterio de aceptación se puede llevar a un caso de prueba sin preguntarle a quien lo escribió.

---

### CP-003 — El encargo a medias sale reportado, y el completo pasa

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-03 |
| **Tipo** | Negativa |
| **Prioridad** | Crítica |
| **Precondiciones** | Carpeta temporal |
| **Datos de entrada** | Una copia de cada modelo llenada a medias, y otra completa |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Llenar a medias una copia de los tres modelos, dejando la marca de hueco | Quedan los tres |
| 2 | Correr `validar.py plantilla` sobre ellos | Los tres salen reportados, y el mensaje dice qué falta |
| 3 | Completar las copias y volver a correr | Ninguna sale reportada |
| 4 | Comprobar que la corrida no escribió nada | Ningún archivo modificado |
| 5 | Borrar la carpeta temporal | No queda rastro |

**Resultado esperado final:** el hueco se nota, y lo completo no molesta.

> **El paso 3 es el que da valor al 2.** Sin él, el caso pasaría con un validador que reporta siempre.

---

### CP-004 — El planteamiento que le falta a esta casa queda dicho

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / RNF |
| **Tipo** | Documento |
| **Prioridad** | Media |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | El aviso que hoy da el revisor sobre el planteamiento faltante |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Comprobar que el estándar no tiene su planteamiento | No lo tiene, y el aviso sale |
| 2 | Dejar escrito por qué no se redacta acá | Porque saldría describiendo la solución en vez del problema |
| 3 | Atarlo al pendiente [56](../../../../../pendientes/56-el-estandar-no-tiene-planteamiento.md) | Queda citable desde la fase que lo resuelva |
| 4 | Comprobar que el aviso **no** se silenció | Sigue saliendo |

**Resultado esperado final:** la falta queda documentada sin apagar el aviso que la señala.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que un encargo a medias pase sin reporte | Inmediato. El CA-03 queda en «No» |
| **Alta** | Que varias HU viejas fallen el encadenamiento (riesgo `R-01`) | Se listan y se anotan. Corregirlas es trabajo de la fase de cada HU |
| **Media** | Que un criterio de aceptación no se pueda llevar a un caso | Se anota como hallazgo, sin reescribir la HU |
| **Media** | Que la especificación crezca describiendo los modelos en vez de exigirles (riesgo `R-02`) | El incremento dice qué se exige y enlaza el modelo, no lo copia |
| **Baja** | Que otra sesión esté tocando la especificación del módulo | Se relee justo antes de escribir |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 3 CA y los RNF con caso |
| Casos ejecutados | 4 de 4 |
| HU sin épica o épicas sin listar sus HU | Las que salgan, todas listadas con su archivo |
| Modelos de `plantillas/` modificados en esta fase | **0** — lo que falte se propone |
| Avisos silenciados | **0** |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
