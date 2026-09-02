# Resultado de Pruebas — Fase `A-EP-007-HU-009-el-instalador-deja-puestas-las-rutas-largas`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó, con qué resultado, y si cada criterio de aceptación quedó cumplido**. Lo que se iba a probar está en el [plan_pruebas.md](plan_pruebas.md); lo que quedó construido, en el [funcionalidad_implementada.md](funcionalidad_implementada.md).

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-007-HU-009-el-instalador-deja-puestas-las-rutas-largas` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-26 |
| **Ciclo** | 2. El ciclo 1 destapó dos defectos, los dos en la forma de probar |

---

## 2. Veredicto

**Cumple.**

| Métrica | Meta | Real |
|---|---|---|
| Casos ejecutados | 6 de 6 | 6 de 6 |
| Criterios en verde | 3 de 3 | 3 de 3 |
| **Cambios en la configuración global** | **0** | **0**, comprobado al terminar |
| Clases de EP-007 que hubo que tocar | **0** | **0** |
| Sabotajes cazados | Todos | 7 de 7, **en el ciclo 2** |
| Fallas en la suite completa | 0 | 0, sobre **402 pruebas** |

---

## 3. Resultado por caso

| Caso | Qué comprueba | Resultado |
|---|---|---|
| CP-001 | Instalar deja el ajuste puesto | ✅ |
| CP-002 | Un `false` puesto a propósito no se pisa | ✅ |
| CP-003 | El modo que muestra no escribe, y nada fuera del repositorio cambia | ✅ |
| CP-004 | Correrlo dos veces no repite trabajo | ✅ |
| CP-005 | Lo de antes no se rompió | ✅ |
| CP-006 | Quien clone y no instale sabe qué hacer | ✅ |

### CP-001, CP-002 y CP-004 — El instalador

| Situación previa | Qué hace | Qué queda |
|---|---|---|
| Sin el ajuste | Lo pone, y lo dice entre sus pasos | `true` |
| Ya en `true` | Dice «ya estaba puesto» | `true` |
| En `false` puesto a mano | Dice `OMITIDO` y **no lo toca** | `false` |

### CP-003 — Nada fuera del repositorio

El modo que muestra nombra el paso y **no escribe**. Y la configuración global de quien corre la suite quedó idéntica, comprobado antes y después de las dos corridas.

**Se agregó un paso que el plan no traía**, y lo pidió un sabotaje: preguntar por el valor **local** del repositorio. Ver §4.2.

### CP-005 — Lo de antes no se rompió

Las clases de `EP-007` pasan **sin tocarlas**. La suite completa: **402 pruebas, OK**, con el conteo a la vista.

### CP-006 — Quien clone y no instale

El documento de despliegue gana su §3.1. Dice el error tal como aparece, el comando del repositorio, el comando global marcado como opcional, y **por qué el instalador no pudo hacerlo por uno**: la configuración no viaja al clonar.

**Ese último punto es el que evita que se lea como un fallo del instalador.**

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Los sabotajes

Siete, restaurados **con copia**.

| # | Qué se rompió | Ciclo 1 | Ciclo 2 |
|---|---|---|---|
| 1 | El instalador no pone el ajuste | Cazado (4) | Cazado (5) |
| 2 | Pisa un `false` puesto a mano | Cazado | Cazado |
| 3 | El modo que muestra también escribe | Cazado | Cazado |
| 4 | Toca la configuración **global** | Cazado, **por las pruebas equivocadas** | Cazado, **por la suya** |
| 5 | No dice que lo puso | Cazado | Cazado |
| 6 | El documento no dice por qué no viaja | Cazado, **contaminado** | Cazado, limpio |
| 7 | El documento no dice el comando global | Cazado, contaminado | Cazado, limpio |

### 4.2 Los dos defectos del ciclo 1, y los dos son de la forma de probar

**El guion dejaba un rastro fuera del repositorio.** El sabotaje 4 escribe en la configuración **global** de la máquina — tiene que hacerlo, porque comprueba que el instalador *no* la toque. El guion limpiaba al final, así que los sabotajes 5, 6 y 7 corrieron con la global puesta. **Sus fallas se leían como «cazado» y eran del rastro anterior.**

Se descubrió leyendo por qué un sabotaje **de documentación** hacía fallar pruebas **de código**. Es `S-035` un nivel más arriba: allá el rastro era un archivo y `git status` lo mostraba; **acá queda fuera del repositorio, donde nada lo vigila.**

**Y la prueba que existe justo para el sabotaje 4 no lo cazó.** Comparaba el valor global antes y después dentro de sí misma: si otra prueba ya lo había dejado puesto, antes y después coinciden y pasa. Se cambió por preguntar el valor **local** del repositorio — si el instalador escribiera afuera, ahí no habría nada. **Eso no depende del orden en que corran las pruebas**, y lo anterior sí.

Queda `S-051`.

### 4.3 Rastros

**Ninguno, y se comprobó explícitamente.** El guion anota la configuración global al empezar, la restaura después de **cada** sabotaje, y vuelve a comprobarla al terminar: quedó como estaba, sin poner.

### 4.4 Ninguna prueba usa credenciales

Ni reales ni inventadas (`00·N6`).

### 4.5 Un aviso que existía antes de esta fase

La corrida deja un `ResourceWarning` en `_ProyectoDePrueba`, la base compartida de las pruebas de `EP-007`: abre el registro de proyectos sin cerrarlo, en su línea 2640. **Es anterior a esta fase y no se tocó** — es código compartido, y arreglarlo de paso sería tocar lo que el plan no declara. Se reporta en el cierre §6.

---

## 5. Trazabilidad criterio a evidencia

| CA / RNF | Evidencia | Estado |
|---|---|---|
| CA-01 — instalar deja el ajuste | CP-001, CP-004 | ✅ |
| CA-02 — un `false` no se pisa | CP-002 | ✅ |
| CA-03 — quien clone sabe qué hacer | CP-006 | ✅ |
| RNF-01 — nada fuera del repositorio | CP-003, con el valor local | ✅ |
| RNF-02 — sus pasos lo dicen | CP-001 paso 4 | ✅ |
| Transversal · no regresión | CP-005 | ✅ |

---

## 6. Veredicto final

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple**, en el ciclo 2 |
| **CA cumplidos** | 3 de 3 |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno |
| **Suite** | `python validadores/pruebas.py`: **402 pruebas, OK** |

### Defectos encontrados y corregidos

| ID | Qué era | Cómo se cazó | Estado |
|---|---|---|---|
| DEF-01 | El guion de sabotaje dejaba la configuración global puesta entre sabotajes, y contaminaba los siguientes | Leyendo por qué un sabotaje de documentación rompía pruebas de código | Corregido: limpia tras cada uno. `S-051` |
| DEF-02 | La prueba del sabotaje 4 comparaba el global contra sí mismo, y pasaba si otra prueba ya lo había cambiado | El mismo sabotaje, que la esquivaba | Corregido: pregunta por el valor local. `S-051` |

**Los dos son de la forma de probar, no del instalador.** El código quedó bien al primer intento; lo que estaba mal era cómo se comprobaba.

---

## 7. Lo que este resultado NO dice

- **No dice que el problema quedó resuelto para todos.** Quien clone y no instale se tropieza igual: **la configuración no viaja**. Lo que hay para esa persona es el texto del documento de despliegue.
- **No dice que el ajuste funcione**, porque eso no se probó acá y no hacía falta: está comprobado en la realidad, guardando 1005 archivos con 59 rutas sobre el tope. Fabricar el caso extremo probaría a git, no al instalador.
- **No cubre acortar la convención de carpetas**, que se midió y no alcanza.
