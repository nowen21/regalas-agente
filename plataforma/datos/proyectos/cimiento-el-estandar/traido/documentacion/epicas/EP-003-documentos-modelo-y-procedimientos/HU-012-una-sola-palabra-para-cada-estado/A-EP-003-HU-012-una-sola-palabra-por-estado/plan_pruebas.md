# Plan de Pruebas — Fase `A-EP-003-HU-012-una-sola-palabra-por-estado`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba cada criterio de aceptación**, con qué datos y en qué ambiente, y cuándo se da por aprobado. Lo que se pide vive en la [HU-012](../HU-012-una-sola-palabra-para-cada-estado.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que «terminado» quedó escrito de una sola forma, definido en un solo sitio, sin que ningún documento cambiara de significado al normalizarlo.

### 1.2 Alcance

**Entra:** [`base/glosario.md`](../../../../../base/glosario.md), los cuatro moldes del ciclo de vida, las 114 historias, la comprobación nueva en `validadores/fases.py` y sus pruebas, más `VERSION` y `CHANGELOG`.

**No entra:** qué significa cada estado, traducir el vocabulario al español, y los estados de documentos que no son del ciclo de vida.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [HU-012](../HU-012-una-sola-palabra-para-cada-estado.md) | Los cuatro criterios y sus pasos |
| [plan_trabajo.md](plan_trabajo.md) | La línea base medida, el mapa de las 51 y las decisiones |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| El glosario | Que defina los tres conjuntos, y que no queden dos palabras para un concepto |
| Los cuatro moldes | Que citen el glosario y no listen |
| Las 114 historias | Que usen el vocabulario, **y que ninguna haya cambiado de sentido** |
| La comprobación nueva | Que avise el estado inventado, que no corrija, y que salga por `validar` |
| `VERSION` y `CHANGELOG` | Que suban juntos |

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

**Unitario** para la comprobación, sobre árboles de mentira. **De sistema** para el glosario, los moldes y las 114: se leen y se comparan contra la foto previa.

### 3.2 Tipos de prueba

| Tipo | Por qué |
|---|---|
| Funcional | Los cuatro criterios se comprueban leyendo archivos y corriendo comandos |
| **De equivalencia** | El corazón de `CA-02`: el cambio debe preservar el sentido, no solo la forma |
| De no regresión | La suite entera, y que la cuenta de completas no se mueva |
| De sabotaje | Que las pruebas cacen lo que dicen cazar |

### 3.3 Técnicas de diseño de casos

**Partición** entre estado válido y estado fuera del vocabulario. **Bordes**: sin campo `Estado`, con texto después de la palabra, y con la palabra en negrita — que es la forma en que aparecen dos de las 51.

### 3.4 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-002, CP-003 | Que nada cambie de sentido es lo único irreversible de esta fase |
| Alta | CP-001, CP-004, CP-005 | El vocabulario único y que la guardia funcione |
| Media | CP-006, CP-007 | Bordes y versionado |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

`python validadores/pruebas.py` **entera**, y **con el conteo a la vista**: `Ran 0 tests` sale con el mismo `OK` que una corrida buena, y eso ya pasó una vez en esta sesión.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- Los dos planes, aprobados.
- **T-04 hecha:** la foto de las 114 con su estado actual. Sin ella, `CA-02` no se puede comprobar.

### 4.2 Criterios de salida

- Los siete casos ejecutados, con su resultado escrito.
- Los cuatro criterios en verde.
- **La cuenta de historias completas, idéntica antes y después.**
- La suite completa en verde, con conteo distinto de cero.

### 4.3 Criterios de suspensión y reanudación

Se suspende si `CP-002` encuentra que alguna de las 51 no tiene mapa evidente: eso deja de ser mecánica y pasa a ser criterio, y vuelve al usuario.

---

## 5. Matriz de trazabilidad

| CA / RNF | Caso | Tipo |
|---|---|---|
| CA-01 — el glosario define, una vez | CP-001 | Camino feliz |
| CA-02 — las 114 usan el vocabulario | CP-002 | Equivalencia |
| CA-02 — ninguna cambió de sentido | CP-003 | Que **no** pase |
| CA-03 — el estado inventado se avisa | CP-004 | Validación |
| CA-03 — y no se corrige, y sale por `validar` | CP-005 | Que **no** pase |
| Transversal — límites | CP-006 | Bordes |
| CA-04 — la versión sube | CP-007 | Funcional |

---

## 6. Casos de prueba

### CP-001 — El vocabulario vive en un solo sitio

| Campo | Valor |
|---|---|
| **HU / CA** | HU-012 / CA-01 |
| **Tipo** | Funcional — camino feliz |
| **Prioridad** | Alta |
| **Precondiciones** | El cambio aplicado |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir el glosario y buscar los estados | Están, con los tres conjuntos y qué significa cada uno |
| 2 | Listar las palabras de los tres conjuntos y buscar sinónimos entre ellas | No hay dos palabras para el mismo concepto |
| 3 | Buscar «terminado» en los tres conjuntos | Es **la misma palabra** en los tres |
| 4 | Abrir los cuatro moldes y buscar una lista de estados escrita ahí | Ninguno la lista; los cuatro remiten al glosario |
| 5 | Comprobar que la lista de la épica ya no esté escrita dos veces | Aparece una sola vez, en el glosario |

**Resultado esperado final:** un solo sitio define, y los cuatro citan.

---

### CP-002 — Las 114 usan el vocabulario, y el cambio es de sinónimo

| Campo | Valor |
|---|---|
| **HU / CA** | HU-012 / CA-02 |
| **Tipo** | Equivalencia |
| **Prioridad** | Crítica |
| **Precondiciones** | La foto de T-04 guardada **antes** de tocar nada |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer las 114 después del cambio | Las 114 usan una palabra del glosario |
| 2 | Comparar par por par contra la foto | Cada cambio va de sinónimo a palabra acordada |
| 3 | Revisar los cambios uno por uno contra el mapa del plan §2.1 | Ninguno se salió del mapa declarado |
| 4 | Buscar historias cuyo estado no cambió | Son las 63 que ya cumplían, ni una más ni una menos |
| 5 | Comprobar el texto que seguía a la palabra | Se conservó entero: fechas, criterios verificados, todo |

**Resultado esperado final:** 114 dentro del vocabulario, y cada cambio explicable por el mapa.

---

### CP-003 — Ninguna historia cambió de sentido

| Campo | Valor |
|---|---|
| **HU / CA** | HU-012 / CA-02, `B-01` |
| **Tipo** | Que **no** pase |
| **Prioridad** | Crítica |
| **Precondiciones** | La cuenta del árbol anotada antes del cambio |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Anotar la línea del inventario antes del cambio | Queda el número de referencia |
| 2 | Aplicar el cambio y correr `validar.py fases` | La línea da **exactamente lo mismo** |
| 3 | Clasificar los 114 estados de antes en abierto/cerrado, y los de después | Las dos clasificaciones coinciden historia por historia |
| 4 | Buscar alguna que pasara de abierta a cerrada o al revés | **Ninguna** |

**Resultado esperado final:** el sentido se preservó, y hay dos formas independientes de decirlo.
**Por qué el paso 2 y el 3 son distintos:** la cuenta del árbol mira documentos presentes, no el campo `Estado`. Que coincida dice que no se rompió nada; el paso 3 es el que mira el campo, que es lo que esta fase toca. **Uno solo no alcanza.**

---

### CP-004 — El estado inventado se avisa

| Campo | Valor |
|---|---|
| **HU / CA** | HU-012 / CA-03 |
| **Tipo** | Validación |
| **Prioridad** | Alta |
| **Precondiciones** | Árbol de mentira con una historia |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Poner en la historia un estado válido y correr | No reporta nada |
| 2 | Cambiarlo por `Casi lista` y correr | Reporta, nombrando el archivo |
| 3 | Leer el aviso | Dice qué estado escribió **y cuáles valen** |
| 4 | Devolverlo a uno válido y correr | No reporta nada |

**Resultado esperado final:** el aviso sigue al estado, y dice qué hacer.

---

### CP-005 — Reporta, no corrige, y sale por `validar`

| Campo | Valor |
|---|---|
| **HU / CA** | HU-012 / CA-03, `RN-06` |
| **Tipo** | Que **no** pase |
| **Prioridad** | Alta |
| **Precondiciones** | El árbol de mentira con el estado inventado |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Guardar el archivo en **bytes** | Queda la copia |
| 2 | Correr la comprobación | Reporta |
| 3 | Volver a leerlo en bytes | **Idéntico** |
| 4 | Correr `validar` completo, no la función suelta | El aviso **también sale por ahí** |
| 5 | Comprobar que el vocabulario que usa sale del glosario, no de una lista en el código | Cambiar el glosario cambia qué acepta |

**Resultado esperado final:** no corrige, sale por el punto de entrada de verdad, y el vocabulario no vive en dos sitios.
**El paso 4 existe porque en la fase anterior faltaba**: descolgar una comprobación de `validar` dejaba todas sus pruebas en verde (`S-043`). **El paso 5 es el que impide que vuelvan las dos copias**, que es el problema entero de esta fase.

---

### CP-006 — Los bordes

| Campo | Valor |
|---|---|
| **HU / CA** | HU-012 / transversal de límites |
| **Tipo** | Bordes |
| **Prioridad** | Media |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Una historia **sin** campo `Estado` | Se reporta que falta, y no revienta |
| 2 | Un estado válido **con texto detrás**: `Done — cerrada el 2026-08-14` | No se reporta: la palabra es válida |
| 3 | Un estado válido **en negrita**: `**Done**` | No se reporta |
| 4 | Un estado válido con otra caja: `done` | Se decide y se declara: o se acepta, o se reporta diciendo que va con mayúscula |
| 5 | Una historia con el campo vacío | Se reporta, y no se confunde con «sin campo» |

**Resultado esperado final:** ningún borde revienta, y cada uno tiene comportamiento escrito.
**El paso 3 no es hipotético:** dos de las 51 traen la palabra en negrita, y son de esta misma sesión.

---

### CP-007 — La versión subió y lo dice

| Campo | Valor |
|---|---|
| **HU / CA** | HU-012 / CA-04 |
| **Tipo** | Funcional |
| **Prioridad** | Media |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer `VERSION` | Subió respecto de lo anotado antes |
| 2 | Leer la primera entrada del `CHANGELOG` | Es de esa versión, con su clase |
| 3 | Leer qué dice | Nombra el glosario, los moldes y la comprobación |
| 4 | Buscar si dice que los documentos de un proyecto se migran | Dice que **no**: el aviso informa |
| 5 | Correr `validar.py versionado` | Sin incumplimientos |

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes

La máquina de quien trabaja, con la biblioteca estándar.

### 7.2 Datos de prueba

Árboles de mentira en carpeta temporal, creados y borrados por la prueba. **Ningún documento real se edita para probar.**

### 7.3 Usuarios de prueba

No aplica. **Ninguna prueba usa credenciales** (`00·N6`).

### 7.4 Qué NO reproduce el entorno de pruebas  ·  `08·T4`

Los árboles de mentira tienen una o dos historias, no 114. **Por eso `CP-002` y `CP-003` corren contra el árbol real**: son los únicos que ven el volumen y la variedad de redacciones de verdad.

---

## 8. Herramientas

| Herramienta | Para qué |
|---|---|
| `unittest`, de la biblioteca estándar | La suite |
| Un guion de sabotaje | Romper cada pieza a propósito |
| Un guion que toma la foto de las 114 | `CP-002` y `CP-003` no se pueden hacer a ojo |

**El guion de sabotaje se restaura con copia**, declara y limpia sus rastros, y **se cae si su corrida final reporta cero pruebas**.

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué la define |
|---|---|
| Crítica | Una historia cambió de sentido, o la comprobación corrige un archivo |
| Alta | El vocabulario quedó escrito también en el código |
| Media | Un borde revienta |
| Baja | Redacción del aviso o del `CHANGELOG` |

### 9.2 Flujo del defecto

Se anota en el `resultado_pruebas.md`, se arregla, y **se vuelve a correr el caso completo**.

### 9.3 Contenido mínimo de un reporte

Qué se esperaba, qué pasó, con qué datos, y en qué archivo y línea.

### 9.4 Registro

En el `resultado_pruebas.md` de esta fase.

---

## 10. Cronograma

Un solo tramo. La suite completa al final.

---

## 11. Roles y responsabilidades

Una sola persona cumple los roles. El agente construye y corre; el usuario aprueba.

---

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Meta |
|---|---|
| Casos ejecutados | 7 de 7 |
| Criterios en verde | 4 de 4 |
| Historias dentro del vocabulario | 114 de 114 |
| **Historias que cambiaron de sentido** | **0** |
| Diferencia en la cuenta de completas | **0** |
| Sabotajes cazados | Todos |
| Fallas en la suite completa | 0, con conteo distinto de cero |

### 12.2 Dónde se miden

En el `resultado_pruebas.md`, con la salida pegada.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Que un sabotaje pase en verde | Se corre el escenario y se mira el estado final: puede ser que el sabotaje no saboteara. Pasó tres veces en esta sesión, con dos diagnósticos distintos |
| Que comparar 114 pares se haga a ojo | Lo hace un guion, y su salida se pega en el resultado |
| Que la comprobación quede escrita pero descolgada | `CP-005` paso 4 la busca por `validar` |
| Que el vocabulario acabe duplicado en el código | `CP-005` paso 5: cambiar el glosario tiene que cambiar qué acepta |

---

## 14. Control de versiones

| Versión | Fecha | Cambio |
|---|---|---|
| 1 | 2026-08-26 | Redacción inicial, junto con el plan de trabajo |

---

## 15. Aprobación

| Rol | Estado |
|---|---|
| Usuario | Pendiente. **No se toca nada hasta que este plan y el de trabajo estén aprobados** (`02·F4`) |
