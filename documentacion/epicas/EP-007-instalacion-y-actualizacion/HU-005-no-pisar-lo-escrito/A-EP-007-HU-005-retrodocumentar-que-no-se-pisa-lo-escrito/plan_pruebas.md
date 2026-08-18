# Plan de Pruebas — Fase A-EP-007-HU-005-retrodocumentar-que-no-se-pisa-lo-escrito   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-007-HU-005 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-007-HU-005-retrodocumentar-que-no-se-pisa-lo-escrito` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/planes/pruebas.md)).

**Condición de arranque, no negociable.** Todo va sobre **copias temporales**. No se instala ni se actualiza ningún proyecto vivo.

**Si el CA-01 falla, la fase se detiene.** Que el instalador pise lo que alguien escribió es un defecto grave en producción: se reporta y se espera decisión.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| No destrucción | Que un archivo modificado a mano conserve su contenido | Copia temporal | Sí |
| El caso que más duele | Que el `CLAUDE.md` del proyecto, con texto propio, sobreviva | Copia temporal | Sí |
| Inventario | Qué se reemplaza y qué se conserva | Copia temporal | No |
| Registro | Que quede dicho qué se actualizó | Copia temporal | Parcial |

**Por qué se prueba con el `CLAUDE.md` del proyecto.** Es el archivo que **mezcla lo heredado con lo propio**, y donde pisar sería más grave.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Integridad | ☑ | El CA-01: el contenido escrito se conserva |
| Trazabilidad | ☑ | El CA-02: lo reemplazado queda dicho |
| Límites | ☑ | Un archivo heredado modificado a mano, que es el caso ambiguo |
| Seguridad | ☑ | Que nada se escriba fuera de la copia |

### 3.3 Técnicas de diseño de casos

- **Contenido, no presencia** — la prueba modifica un archivo a mano **antes** de actualizar y compara el contenido después. Existir y conservar el contenido no es lo mismo, y lo que se pierde es el contenido.
- **El archivo mezclado** — arriba. Es el que distingue "no borra nada" de "no borra los archivos que él no puso".
- **El caso ambiguo también se prueba** — un archivo **heredado** que el proyecto modificó a mano: ahí es donde conservar y actualizar se contradicen, y el resultado tiene que decir qué hace el instalador.
- **El registro se lee, no se supone** — el CA-02 se cierra viendo si el registro dice **archivo por archivo** qué reemplazó, no si el registro existe.
- **Lo que se encuentre mal se para y se reporta** — el riesgo `R-01`: corregir un instalador que pisa merece su propio plan, no un arreglo al vuelo.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/pruebas.py` entera y la puesta al día sobre copias temporales.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-005 | [CA-01](../HU-005-no-pisar-lo-escrito.md#ca-01--lo-que-la-persona-escribió-se-conserva) | [CP-001](#cp-001--el-archivo-modificado-a-mano-conserva-su-contenido), [CP-002](#cp-002--el-claudemd-del-proyecto-con-texto-propio-sobrevive) | Integridad | Crítica | Sí | ☐ |
| HU-005 | [CA-02](../HU-005-no-pisar-lo-escrito.md#ca-02--lo-que-sí-se-reemplaza-queda-dicho) | [CP-003](#cp-003--qué-se-reemplaza-y-qué-se-conserva), [CP-004](#cp-004--el-registro-dice-qué-se-actualizó) | Trazabilidad | Alta | Parcial | ☐ |
| HU-005 | RNF — que actualizar sea seguro | [CP-001](#cp-001--el-archivo-modificado-a-mano-conserva-su-contenido) | Integridad | Crítica | Sí | ☐ |

**Cobertura:** 2 de 2 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — El archivo modificado a mano conserva su contenido

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-01 y RNF |
| **Tipo** | Integridad |
| **Prioridad** | Crítica |
| **Precondiciones** | Copia temporal de un proyecto ya instalado |
| **Datos de entrada** | Varios archivos modificados a mano, con contenido reconocible |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Modificar a mano varios archivos del proyecto | Quedan con contenido reconocible |
| 2 | Anotar el contenido de cada uno | Queda la línea base |
| 3 | Correr la puesta al día | Termina |
| 4 | Comparar el contenido de cada archivo contra la línea base | Idéntico, byte por byte |
| 5 | Probar con un archivo **heredado** modificado a mano | Se anota qué hace: es el caso ambiguo |
| 6 | Comprobar que no se escribió fuera de la copia | Nada afuera |

**Resultado esperado final:** actualizar es seguro, o queda dicho exactamente dónde no lo es.

> **El paso 5 es el caso difícil.** En un archivo heredado que el proyecto tocó, conservar y actualizar se contradicen: lo que importa es que el instalador tenga una respuesta y que quede escrita.

---

### CP-002 — El `CLAUDE.md` del proyecto, con texto propio, sobrevive

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-01 |
| **Tipo** | Integridad |
| **Prioridad** | Crítica |
| **Precondiciones** | Copia temporal con su `CLAUDE.md` instalado |
| **Datos de entrada** | El `CLAUDE.md` con texto propio del proyecto agregado |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Agregar texto propio al `CLAUDE.md` del proyecto | Queda mezclado con lo heredado |
| 2 | Anotar el archivo entero | Queda la línea base |
| 3 | Correr la puesta al día | Termina |
| 4 | Comprobar que el texto propio **sigue ahí** | Sigue, completo |
| 5 | Comprobar qué pasó con la parte heredada | Se anota: actualizada o intacta |
| 6 | Comprobar que el archivo no quedó duplicado ni partido | Ninguna de las dos |

**Resultado esperado final:** el archivo que mezcla lo propio con lo heredado es el que prueba de verdad el CA-01.

---

### CP-003 — Qué se reemplaza y qué se conserva

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-02 |
| **Tipo** | Trazabilidad |
| **Prioridad** | Alta |
| **Precondiciones** | Copia temporal, con su árbol anotado |
| **Datos de entrada** | Una puesta al día completa |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Anotar el árbol y el contenido antes | Queda la línea base |
| 2 | Correr la puesta al día | Termina |
| 3 | Comparar y listar qué archivos cambiaron | Queda la lista real |
| 4 | Separarlos en heredados y propios del proyecto | Dos grupos |
| 5 | Comprobar que ningún propio está en la lista de cambiados | Ninguno |

**Resultado esperado final:** se sabe exactamente qué toca una puesta al día, medido y no supuesto.

---

### CP-004 — El registro dice qué se actualizó

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-02 |
| **Tipo** | Trazabilidad |
| **Prioridad** | Alta |
| **Precondiciones** | El CP-003 corrido, con su lista real de archivos cambiados |
| **Datos de entrada** | El registro de la versión que el instalador escribe |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer el registro después de la puesta al día | Existe, con su entrada |
| 2 | Comprobar si dice **archivo por archivo** qué reemplazó | Se anota si lo dice o no |
| 3 | Comparar lo que dice contra la lista real del CP-003 | Coinciden, o se anota la diferencia |
| 4 | Anotar los defectos conocidos de este registro | Atados a los pendientes [44](../../../../../pendientes/hecho/el-registro-no-se-escribe-si-no-cambia-la-huella.md) y [46](../../../../../pendientes/hecho/el-registro-se-escribe-antes-de-contarse.md) |
| 5 | Escribir el veredicto del CA-02 con lo medido | Cumplido, a medias o no |

**Resultado esperado final:** el CA-02 queda establecido con la lista real al lado del registro, no con una lectura del registro sola.

> **El registro puede mentir** (riesgo `R-03`): tiene dos pendientes abiertos. Se prueba igual y se anota — es la evidencia que esos pendientes necesitan.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que la puesta al día pise contenido escrito (riesgo `R-01`) | **Se para, se reporta al usuario y no se sigue** hasta que se decida |
| **Crítica** | Que la corrida se haga sobre un proyecto vivo (riesgo `R-02`) | Inmediato. Copia temporal, siempre |
| **Alta** | Que el texto propio del `CLAUDE.md` se pierda | Inmediato. Es el caso que más duele |
| **Media** | Que el registro no diga archivo por archivo qué reemplazó | Se anota: el CA-02 queda a medias, con la lista real como evidencia |
| **Media** | Que el registro mienta por los pendientes 44 y 46 (riesgo `R-03`) | Se prueba igual y se anota |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 2 CA y los RNF con caso |
| Casos ejecutados | 4 de 4 |
| Proyectos vivos actualizados | **0** |
| Archivos propios del proyecto alterados | **0** |
| Diferencias entre el registro y la lista real de cambios | Todas anotadas |
| Archivos escritos fuera de la copia | **0** |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
