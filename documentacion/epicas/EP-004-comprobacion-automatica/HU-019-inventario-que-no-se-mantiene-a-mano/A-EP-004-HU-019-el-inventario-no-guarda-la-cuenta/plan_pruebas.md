# Plan de Pruebas — Fase `A-EP-004-HU-019-el-inventario-no-guarda-la-cuenta`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba cada criterio de aceptación** de la fase, con qué datos y en qué ambiente, y cuándo se da por aprobado. Lo que se pide vive en la [HU-019](../HU-019-inventario-que-no-se-mantiene-a-mano.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó y con qué resultado, en el `resultado_pruebas.md`.

---

## 1. Introducción

### 1.1 Propósito

Comprobar que el inventario de historias deja de guardar una cuenta que el árbol ya sabe, que lo que solo él sabía sigue estando, y que si alguien repone la cuenta a mano, se dice.

### 1.2 Alcance

**Entra:** el pendiente [48](../../../../../pendientes/48-inventario-hu.md), la comprobación nueva en `validadores/fases.py` y la prueba que la cubre en `validadores/pruebas.py`.

**No entra:** cómo se cuenta una historia completa, que es de la [HU-017](../../HU-017-inventario-de-hu-sin-fase/HU-017-inventario-de-hu-sin-fase.md) y no se toca. Tampoco otros pendientes que traigan números a mano.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [HU-019](../HU-019-inventario-que-no-se-mantiene-a-mano.md) | Los tres criterios y sus pasos de validación |
| [plan_trabajo.md](plan_trabajo.md) | Las tareas, la línea base medida y las decisiones |
| [EP-004](../../epica.md) §10.2 | Que el programa reporte y no corrija |

---

## 2. Elementos a probar

| Elemento | Ubicación | Qué se prueba de él |
|---|---|---|
| El pendiente del inventario | `pendientes/48-inventario-hu.md` | Que no guarde la cuenta, que remita al comando, y que conserve su narrativa |
| La comprobación nueva | `validar` en `validadores/fases.py` | Que reporte el campo repuesto, y que no toque el archivo |
| La cuenta que ya existía | `inventario` en `validadores/fases.py` | Que siga dando lo mismo: esta fase no la cambia |

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

**Unitario** para la comprobación nueva, sobre un árbol de mentira en carpeta temporal. **De sistema** para el pendiente real, leyéndolo y corriendo el comando que nombra.

### 3.2 Tipos de prueba

| Tipo | Por qué se incluye |
|---|---|
| Funcional | Los tres criterios son observables leyendo un archivo y corriendo un comando |
| De no regresión | La cuenta y los demás avisos de `fases` tienen que seguir iguales |
| De sabotaje | Comprobar que las pruebas cazan lo que dicen cazar, y no pasan en verde por casualidad |

### 3.3 Técnicas de diseño de casos

**Partición de equivalencia** entre «el pendiente trae la cuenta» y «no la trae». **Caso borde** con el archivo que trae números **dentro de su narrativa** pero no como campo: es el que distingue una comprobación útil de uno que marca cualquier cifra.

### 3.4 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-001, CP-002 | Son el criterio central: que la cuenta no esté dos veces |
| Alta | CP-003, CP-004 | Que no se pierda lo que solo el pendiente sabía |
| Media | CP-005, CP-006 | Que el aviso no se vuelva ruido, y que nada más se haya movido |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Se corre `python validadores/pruebas.py`, que es la suite que esta fase toca. **Y se corre entera al final**, no solo las clases tocadas: en esta misma sesión un cambio en un validador dejó una prueba fallando en otro archivo, y correr solo lo tocado no lo habría mostrado.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- El plan de trabajo y este plan, aprobados.
- La lista de T-01 hecha: qué de las 74 filas está solo ahí. **Sin eso no se quita la tabla.**

### 4.2 Criterios de salida

- Los seis casos ejecutados, con su resultado escrito.
- Los tres criterios de aceptación en verde, con su evidencia.
- La suite completa en verde. **Incluida la falla que hoy existe**, que es justamente la que esta fase resuelve.
- Los sabotajes corridos, y cazados todos.

### 4.3 Criterios de suspensión y reanudación

Se suspende si T-01 encuentra que la tabla guarda trabajo que no está en ninguna otra parte y no hay dónde ponerlo: eso cambia el alcance y vuelve al usuario antes de quitar nada.

---

## 5. Matriz de trazabilidad

| CA / RNF | Caso que lo cubre | Tipo |
|---|---|---|
| CA-01 — responde sin guardar la respuesta | CP-001 | Camino feliz |
| CA-02 — reponer un número se reporta | CP-002, CP-005 | Validación y borde |
| CA-02 — y no se corrige solo | CP-003 | Que **no** pase |
| CA-03 — la narrativa sobrevive | CP-004 | Camino feliz |
| RNF-01 — dice de dónde sale la cuenta | CP-001 paso 4 | Funcional |
| RNF-02 — no agrega un recorrido nuevo | CP-006 | No regresión |

**Los tres criterios están cubiertos, y el que más importa —que el programa no corrija— tiene su propio caso.**

---

## 6. Casos de prueba

### CP-001 — El pendiente remite al comando y el comando responde

| Campo | Valor |
|---|---|
| **HU / CA** | HU-019 / CA-01, RNF-01 |
| **Tipo** | Funcional — camino feliz |
| **Prioridad** | Crítica |
| **Precondiciones** | La fase construida; el pendiente ya editado |
| **Datos de entrada** | El repositorio real |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir `pendientes/48-inventario-hu.md` | Se lee completo, sin la tabla de historias |
| 2 | Buscar en el archivo el rótulo «Total de HU» | No aparece |
| 3 | Buscar los rótulos «Completas» e «Incompletas» como campo con número | No aparecen |
| 4 | Leer el encabezado y copiar el comando que nombra | Está escrito de forma que se copia y se pega sin editarlo |
| 5 | Correr ese comando desde la raíz del repositorio | Termina con una línea que dice cuántas historias hay, cuántas completas y cuántas incompletas |

**Resultado esperado final:** el pendiente no guarda ninguno de los tres números, y el comando que nombra los devuelve.
**Postcondiciones:** ninguna. Leer y contar no cambian nada.

---

### CP-002 — Reponer un total a mano se reporta

| Campo | Valor |
|---|---|
| **HU / CA** | HU-019 / CA-02 |
| **Tipo** | Funcional — validación |
| **Prioridad** | Crítica |
| **Precondiciones** | Un árbol de mentira en carpeta temporal, con su pendiente sin cuenta |
| **Datos de entrada** | La fila `| **Total de HU** | 99 |` agregada al encabezado |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr la comprobación sobre el árbol de mentira sin la fila | No reporta nada sobre ese archivo |
| 2 | Agregar la fila con el total escrito | El archivo queda con la fila |
| 3 | Correr la comprobación otra vez | Reporta, nombrando el archivo y el campo que sobra |
| 4 | Leer el texto del aviso | Dice de dónde sale la cuenta, para que quien lo lea sepa qué hacer |
| 5 | Quitar la fila y correr una vez más | Vuelve a no reportar nada sobre ese archivo |

**Resultado esperado final:** el aviso aparece solo cuando la fila está.
**Postcondiciones:** la carpeta temporal se borra al terminar.

---

### CP-003 — La comprobación reporta y no corrige

| Campo | Valor |
|---|---|
| **HU / CA** | HU-019 / CA-02, `RN-04` |
| **Tipo** | Funcional — que **no** pase |
| **Prioridad** | Crítica |
| **Precondiciones** | El árbol de mentira con la fila del total puesta |
| **Datos de entrada** | El mismo de CP-002 |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Guardar el contenido exacto del pendiente de mentira, en bytes | Queda una copia para comparar |
| 2 | Correr la comprobación | Reporta el campo que sobra |
| 3 | Volver a leer el pendiente de mentira, en bytes | Es **idéntico** al del paso 1 |
| 4 | Comprobar que no se creó ningún archivo nuevo en esa carpeta | La carpeta tiene los mismos archivos que antes |

**Resultado esperado final:** el archivo no cambió ni un byte.
**Se compara en bytes y no como texto a propósito:** comparar como texto dejaría pasar un cambio de fin de línea, que es exactamente el defecto que se coló en la fase E de la plataforma.

---

### CP-004 — La narrativa fechada y la condición de cierre sobreviven

| Campo | Valor |
|---|---|
| **HU / CA** | HU-019 / CA-03 |
| **Tipo** | Funcional — camino feliz |
| **Prioridad** | Alta |
| **Precondiciones** | Copia del pendiente tomada **antes** de editarlo |
| **Datos de entrada** | El pendiente antes y después |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Contar en la copia previa los párrafos de narrativa fechada | Da 11, que es lo medido en el plan §2 |
| 2 | Contar los mismos párrafos en el pendiente ya editado | Da 11 |
| 3 | Comparar uno por uno su texto y su fecha | Coinciden, sin recortes |
| 4 | Buscar la condición de cierre en el pendiente editado | Sigue diciendo que cierra cuando no quede ninguna historia incompleta |
| 5 | Revisar la lista que dejó T-01 | Todo lo que estaba solo en la tabla quedó escrito en alguna parte del pendiente |

**Resultado esperado final:** no se perdió ningún párrafo fechado ni la condición de cierre.

---

### CP-005 — Un número dentro de la narrativa no se marca

| Campo | Valor |
|---|---|
| **HU / CA** | HU-019 / CA-02 |
| **Tipo** | Funcional — caso borde |
| **Prioridad** | Media |
| **Precondiciones** | Árbol de mentira con un pendiente sin campos de cuenta |
| **Datos de entrada** | Un párrafo que dice «68 a 74 total: seis historias nuevas al enrutar el backlog» |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir ese párrafo en el pendiente de mentira | El archivo tiene cifras, pero ninguna como campo |
| 2 | Correr la comprobación | No reporta nada |

**Resultado esperado final:** las cifras de la narrativa no disparan el aviso.
**Por qué existe este caso:** una comprobación que marcara cualquier número volvería el aviso ruido, y un aviso que se aprende a ignorar es peor que no tenerlo.

---

### CP-006 — Nada más se movió

| Campo | Valor |
|---|---|
| **HU / CA** | HU-019 / RNF-02 y no regresión |
| **Tipo** | No regresión |
| **Prioridad** | Media |
| **Precondiciones** | La fase construida |
| **Datos de entrada** | El repositorio real |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Anotar la línea del inventario antes del cambio | Queda el número de referencia |
| 2 | Correr `validar.py fases` después del cambio | La línea del inventario da lo mismo |
| 3 | Comparar la cantidad de avisos de fases, aparte del nuevo | No aparecen ni desaparecen avisos que no sean el de esta fase |
| 4 | Correr la suite completa | Verde, incluida la falla que existía antes de esta fase |

**Resultado esperado final:** lo único que cambió es lo que esta fase se propuso cambiar.

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes

La máquina de quien trabaja, con la biblioteca estándar del lenguaje. No hace falta instalar nada, que es lo que pide `EP-004 §10.2`.

### 7.2 Datos de prueba

Árboles de mentira en carpeta temporal, creados y borrados por la propia prueba. **El pendiente real no se edita para probar**, y ninguna prueba deja archivos fuera de su carpeta temporal.

### 7.3 Usuarios de prueba

No aplica: no hay autenticación. **Ninguna prueba usa credenciales**, ni de mentira (`00·N6`).

### 7.4 Qué NO reproduce el entorno de pruebas  ·  `08·T4`

El árbol de mentira tiene unas pocas historias, no 113. **Por eso `CP-006` corre contra el árbol real**: es el único que comprueba el comportamiento con el volumen de verdad.

---

## 8. Herramientas

| Herramienta | Para qué |
|---|---|
| `unittest`, de la biblioteca estándar | La suite de `validadores/pruebas.py` |
| Un guion de sabotaje | Romper a propósito cada pieza y ver si la prueba la caza |

**El sabotaje se restaura con copia, nunca con el control de versiones**, y el guion declara y limpia lo que deje fuera del archivo saboteado. Las dos cosas se aprendieron rompiéndolas en esta misma sesión.

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué la define |
|---|---|
| Crítica | La comprobación **corrige** el archivo, o la cuenta cambia de valor |
| Alta | Un párrafo de narrativa se perdió al quitar la tabla |
| Media | El aviso aparece sobre cifras de la narrativa |
| Baja | Redacción del aviso |

### 9.2 Flujo del defecto

Se anota en el `resultado_pruebas.md` con su identificador, se arregla, y **se vuelve a correr el caso completo**, no solo el paso que falló.

### 9.3 Contenido mínimo de un reporte

Qué se esperaba, qué pasó, con qué datos, y en qué archivo y línea.

### 9.4 Registro

En el `resultado_pruebas.md` de esta fase.

---

## 10. Cronograma

Un solo tramo de trabajo. Las pruebas se corren a medida que las tareas cierran, y la suite completa al final.

---

## 11. Roles y responsabilidades

Una sola persona cumple los roles. El agente construye y corre; el usuario aprueba.

---

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Meta |
|---|---|
| Casos ejecutados | 6 de 6 |
| Criterios en verde | 3 de 3 |
| Sabotajes cazados | Todos |
| Fallas en la suite completa | 0 |

### 12.2 Dónde se miden

En el `resultado_pruebas.md`, con la salida de las corridas pegada.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Que un sabotaje pase en verde y se lea como «falta una prueba» | Se corre el escenario y se mira el estado final: puede ser que el sabotaje no saboteó. Distinguirlo costó dos diagnósticos opuestos en esta sesión |
| Que `CP-003` pase porque la comprobación no corrió, no porque no corrija | El caso empieza comprobando que **sí** reportó, y solo después mira que el archivo no cambió |
| Que probar deje rastros en el repositorio | Todo va a carpeta temporal, y el guion de sabotaje declara qué deja fuera y lo limpia |

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
