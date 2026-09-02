# Plan de Pruebas — Fase `A-EP-004-HU-020-lo-que-se-hereda-tampoco-se-cuenta-a-mano`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba cada criterio de aceptación**, con qué datos y en qué ambiente, y cuándo se da por aprobado. Lo que se pide vive en la [HU-020](../HU-020-el-inventario-heredado-tampoco-se-mantiene-a-mano.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que lo que el estándar arregló para sí mismo llega a quien lo hereda: que la plantilla del inventario deje de pedir una cuenta a mano, y que la comprobación la vigile donde el proyecto la tenga.

### 1.2 Alcance

**Entra:** [`plantillas/inventario-hu.md`](../../../../../plantillas/inventario-hu.md), `cuenta_escrita_a_mano` en `validadores/fases.py`, sus pruebas, y el par `VERSION` + `CHANGELOG`.

**No entra:** los inventarios ya escritos en proyectos existentes, las demás plantillas, y cómo se cuenta una historia completa.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [HU-020](../HU-020-el-inventario-heredado-tampoco-se-mantiene-a-mano.md) | Los cuatro criterios y sus pasos |
| [plan_trabajo.md](plan_trabajo.md) | Tareas, línea base medida y decisiones |
| La fase [`A` de la HU-019](../../HU-019-inventario-que-no-se-mantiene-a-mano/A-EP-004-HU-019-el-inventario-no-guarda-la-cuenta/resultado_pruebas.md) | Lo que ya se probó puertas adentro, y que no se repite |

---

## 2. Elementos a probar

| Elemento | Ubicación | Qué se prueba de él |
|---|---|---|
| La plantilla del inventario | `plantillas/inventario-hu.md` | Que no pida cuenta ni tabla, que enseñe el comando, y que conserve lo no derivable |
| La comprobación generalizada | `cuenta_escrita_a_mano` en `validadores/fases.py` | Que encuentre el inventario en varias carpetas, que no recorra el proyecto entero, y que siga sin corregir |
| El versionado | `VERSION` y `CHANGELOG.md` | Que suban juntos y que el validador los acepte |

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

**Unitario** para la comprobación, sobre proyectos de mentira en carpeta temporal. **De sistema** para la plantilla: se lee, y el comando que enseña se copia y se corre.

### 3.2 Tipos de prueba

| Tipo | Por qué se incluye |
|---|---|
| Funcional | Los cuatro criterios son observables leyendo archivos y corriendo comandos |
| De no regresión | **Las siete pruebas de la `HU-019` tienen que seguir pasando sin tocarlas.** Es lo que dice que un inventario en `pendientes/` no se rompió |
| De rendimiento | Que buscar no abra el proyecto entero |
| De sabotaje | Que las pruebas cacen lo que dicen cazar |

### 3.3 Técnicas de diseño de casos

**Partición** entre «el inventario está en `pendientes/`» y «está en `documentacion/`». **Caso borde** con un archivo que trae los rótulos **fuera** de las carpetas declaradas: dice si el alcance de la búsqueda es el que se declaró, y no otro por accidente.

### 3.4 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-001, CP-002 | Son el criterio central: que la guardia llegue a los proyectos |
| Alta | CP-003, CP-004, CP-006 | Que no se pierda lo que la plantilla enseña, y que lo de antes no se rompa |
| Media | CP-005, CP-007 | El alcance de la búsqueda y el versionado |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

`python validadores/pruebas.py` **entera**, no solo las clases tocadas. En la fase anterior, un cambio en un validador dejó una prueba fallando en otro archivo, y correr solo lo tocado no lo habría mostrado.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- Los dos planes, aprobados.
- **T-02 hecha antes de T-09**: el comando que la plantilla va a enseñar se corre antes de escribirlo.

### 4.2 Criterios de salida

- Los siete casos ejecutados, con su resultado escrito.
- Los cuatro criterios en verde, con evidencia.
- La suite completa en verde, **y con un conteo distinto de cero**.
- Los sabotajes corridos y cazados.

### 4.3 Criterios de suspensión y reanudación

Se suspende si T-06 encuentra que la plantilla enseña algo no derivable que no cabe en la versión nueva: eso cambia el alcance y vuelve al usuario antes de quitar nada.

---

## 5. Matriz de trazabilidad

| CA / RNF | Caso que lo cubre | Tipo |
|---|---|---|
| CA-01 — la plantilla no pide mantener una cuenta | CP-003, CP-004 | Camino feliz |
| CA-02 — la comprobación busca donde el proyecto tenga | CP-001, CP-002 | Camino feliz y partición |
| CA-02 — y sigue sin corregir | CP-002 paso 5 | Que **no** pase |
| CA-03 — lo no derivable se conserva | CP-003 | Camino feliz |
| CA-04 — la versión sube | CP-007 | Funcional |
| RNF-01 — no recorre el proyecto entero | CP-005 | Rendimiento y borde |
| RNF-02 — un inventario en `pendientes/` sigue igual | CP-006 | No regresión |

---

## 6. Casos de prueba

### CP-001 — El inventario en `documentacion/` se vigila

| Campo | Valor |
|---|---|
| **HU / CA** | HU-020 / CA-02 |
| **Tipo** | Funcional — camino feliz |
| **Prioridad** | Crítica |
| **Precondiciones** | Un proyecto de mentira con `documentacion/epicas/` y una historia con su fase |
| **Datos de entrada** | `documentacion/inventario-hu.md` con `| **Total de HU** | 99 |` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Armar el proyecto de mentira sin ningún inventario | La comprobación no reporta nada |
| 2 | Escribir el inventario en `documentacion/` con el total a mano | El archivo queda en su sitio |
| 3 | Correr la comprobación sobre ese proyecto | Reporta un aviso |
| 4 | Leer la ruta que nombra el aviso | Es `documentacion/inventario-hu.md`, la real, no una fija |
| 5 | Quitarle la fila y correr otra vez | No reporta nada |

**Resultado esperado final:** el aviso aparece y desaparece siguiendo al archivo real.

---

### CP-002 — La misma vigilancia en otra carpeta, y sin corregir

| Campo | Valor |
|---|---|
| **HU / CA** | HU-020 / CA-02, `RN-04` de la HU-019 |
| **Tipo** | Funcional — partición, y que **no** pase |
| **Prioridad** | Crítica |
| **Precondiciones** | El proyecto de mentira de CP-001 |
| **Datos de entrada** | El mismo inventario, movido a otra de las carpetas declaradas |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Mover el inventario a la otra carpeta declarada | Queda un solo inventario, en sitio distinto |
| 2 | Correr la comprobación | Reporta, con la ruta nueva |
| 3 | Guardar el contenido del archivo en bytes | Queda la copia para comparar |
| 4 | Correr la comprobación otra vez | Reporta lo mismo |
| 5 | Volver a leer el archivo en bytes | **Idéntico** al del paso 3 |
| 6 | Contar los archivos de esa carpeta | Los mismos: no se creó ninguno |

**Resultado esperado final:** vigila en las dos ubicaciones y no toca nada.
**Se compara en bytes**, no como texto: comparar como texto dejaría pasar un cambio de fin de línea.

---

### CP-003 — La plantilla conserva lo que no es derivable

| Campo | Valor |
|---|---|
| **HU / CA** | HU-020 / CA-01, CA-03 |
| **Tipo** | Funcional — camino feliz |
| **Prioridad** | Alta |
| **Precondiciones** | Lista de secciones tomada **antes** de tocar la plantilla |
| **Datos de entrada** | La plantilla antes y después |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Listar las secciones de la plantilla antes del cambio | Queda la lista de referencia |
| 2 | Buscar en la plantilla ya cambiada los rótulos «Total de HU», «Completas» e «Incompletas» como campo | No aparecen |
| 3 | Buscar la tabla con columnas `Épica`, `HU`, `Fase` y los cinco documentos | No aparece |
| 4 | Buscar la guía del orden en que se escriben los documentos | Sigue estando |
| 5 | Buscar la distinción entre construcción y retrodocumentación | Sigue estando |
| 6 | Buscar dónde dice que el inventario vive donde el proyecto lleve su backlog | Sigue estando |

**Resultado esperado final:** se fue lo derivable y se quedó lo que solo la plantilla enseña.

---

### CP-004 — El comando que la plantilla enseña funciona al copiarlo

| Campo | Valor |
|---|---|
| **HU / CA** | HU-020 / CA-01, `RN-03` |
| **Tipo** | Funcional — camino feliz |
| **Prioridad** | Alta |
| **Precondiciones** | La plantilla ya cambiada, y un proyecto de mentira con una historia |
| **Datos de entrada** | El comando, copiado **literal** de la plantilla |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer el comando en la plantilla | Trae `--raiz` |
| 2 | Copiarlo tal cual, sin editar nada más que la ruta | Queda una orden ejecutable |
| 3 | Correrla contra el proyecto de mentira | Lista qué le falta a la historia |
| 4 | Leer la última línea de la salida | Dice cuántas historias hay, cuántas completas y cuántas incompletas |

**Resultado esperado final:** quien copie el comando de la plantilla obtiene la cuenta, no un error.
**Por qué este caso existe:** un comando escrito sin haberlo corrido deja a quien lo copia con un error en la mano, y la plantilla es justamente lo que la gente copia.

---

### CP-005 — La búsqueda tiene el alcance que se declaró

| Campo | Valor |
|---|---|
| **HU / CA** | HU-020 / RNF-01 |
| **Tipo** | Rendimiento y caso borde |
| **Prioridad** | Media |
| **Precondiciones** | Proyecto de mentira con carpetas fuera de las declaradas |
| **Datos de entrada** | Un archivo con los rótulos, en una carpeta **no** declarada |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Poner un archivo con `| **Total de HU** | 99 |` en una carpeta no declarada | El archivo existe |
| 2 | Correr la comprobación | **No** lo reporta |
| 3 | Contar cuántas carpetas abre la comprobación al correr | Son las declaradas, no todo el árbol |

**Resultado esperado final:** el alcance es el declarado.
**Este caso corta en los dos sentidos:** si algún día el alcance se amplía sin querer, el paso 2 lo dice; si se necesita ampliarlo a propósito, este caso es el que hay que cambiar, y eso obliga a decidirlo en vez de que ocurra solo.

---

### CP-006 — Lo de antes no se rompió

| Campo | Valor |
|---|---|
| **HU / CA** | HU-020 / RNF-02 y no regresión |
| **Tipo** | No regresión |
| **Prioridad** | Alta |
| **Precondiciones** | La comprobación ya generalizada |
| **Datos de entrada** | Las siete pruebas de la `HU-019`, **sin tocarlas** |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr las pruebas de `InventarioDeHU` sin haberlas modificado | Todas en verde |
| 2 | Correr `validar.py fases` sobre el estándar | Sigue sin reportar nada del pendiente 48 |
| 3 | Comparar la cantidad de avisos con la de antes del cambio | La misma |
| 4 | Correr la suite completa | En verde, **y con un conteo distinto de cero** |

**Resultado esperado final:** un inventario en `pendientes/` se comporta igual que antes.
**El paso 4 comprueba dos cosas, no una:** que no haya fallas **y que haya corrido algo**. `Ran 0 tests` sale con el mismo `OK` que una corrida buena, y eso ya pasó una vez en la fase anterior.

---

### CP-007 — La versión subió y lo dice

| Campo | Valor |
|---|---|
| **HU / CA** | HU-020 / CA-04 |
| **Tipo** | Funcional |
| **Prioridad** | Media |
| **Precondiciones** | El cambio de plantilla aplicado |
| **Datos de entrada** | `VERSION` y `CHANGELOG.md` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer `VERSION` | Dice `34.2.0`: subió la parte **menor** |
| 2 | Leer la primera entrada del `CHANGELOG` | Es de esa versión, marcada **MENOR** |
| 3 | Leer qué dice esa entrada | Nombra la plantilla y la comprobación, y dice qué verá un proyecto que ya tenía el estándar |
| 4 | Buscar si la entrada dice que el inventario existente se migra | Dice que **no**: el aviso informa y arreglarlo es decisión del proyecto |
| 5 | Correr `validar.py versionado` | Sin incumplimientos |

**Resultado esperado final:** el par sube junto y el validador lo acepta.

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes

La máquina de quien trabaja, con la biblioteca estándar del lenguaje.

### 7.2 Datos de prueba

Proyectos de mentira en carpeta temporal, creados y borrados por la propia prueba. **Ni la plantilla ni el pendiente real se editan para probar.**

### 7.3 Usuarios de prueba

No aplica. **Ninguna prueba usa credenciales**, ni reales ni inventadas (`00·N6`).

### 7.4 Qué NO reproduce el entorno de pruebas  ·  `08·T4`

Los proyectos de mentira tienen una o dos historias, no cientos. **Por eso `CP-005` cuenta carpetas abiertas en vez de medir segundos**: el tiempo en un árbol de tres carpetas no dice nada del tiempo en uno de mil, y el conteo sí.

---

## 8. Herramientas

| Herramienta | Para qué |
|---|---|
| `unittest`, de la biblioteca estándar | La suite |
| Un guion de sabotaje | Romper cada pieza a propósito |

**El guion se restaura con copia**, declara y limpia lo que deje fuera del archivo saboteado, y **se cae con error si su corrida final reporta cero pruebas** — las tres cosas se aprendieron rompiéndolas.

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué la define |
|---|---|
| Crítica | La comprobación **corrige** un archivo, o no ve un inventario que sí está |
| Alta | La plantilla perdió algo que enseñaba y no es derivable |
| Media | La búsqueda se salió del alcance declarado |
| Baja | Redacción del aviso o de la entrada del `CHANGELOG` |

### 9.2 Flujo del defecto

Se anota en el `resultado_pruebas.md`, se arregla, y **se vuelve a correr el caso completo**.

### 9.3 Contenido mínimo de un reporte

Qué se esperaba, qué pasó, con qué datos, y en qué archivo y línea.

### 9.4 Registro

En el `resultado_pruebas.md` de esta fase.

---

## 10. Cronograma

Un solo tramo. Las pruebas se corren a medida que las tareas cierran, y la suite completa al final.

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
| Sabotajes cazados | Todos |
| Pruebas de la `HU-019` que hubo que tocar | **0** |
| Fallas en la suite completa | 0, con conteo distinto de cero |

### 12.2 Dónde se miden

En el `resultado_pruebas.md`, con la salida de las corridas pegada.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Que un sabotaje pase en verde | Se corre el escenario y se mira el estado final: puede ser que el sabotaje no saboteó. En la fase anterior pasó dos veces, con diagnósticos opuestos |
| Que la comprobación quede escrita pero descolgada de la corrida | Hay una prueba que la busca **a través de `validar`**, no llamándola. Es lo que la fase anterior aprendió (`S-043`), y acá se hereda |
| Que probar deje rastros | Todo en carpeta temporal, y el guion declara qué deja fuera |

---

## 14. Control de versiones

| Versión | Fecha | Cambio |
|---|---|---|
| 1 | 2026-08-26 | Redacción inicial, junto con el plan de trabajo |

---

## 15. Aprobación

| Rol | Estado |
|---|---|
| Usuario | Pendiente. **No se toca código hasta que este plan y el de trabajo estén aprobados** (`02·F4`) |
