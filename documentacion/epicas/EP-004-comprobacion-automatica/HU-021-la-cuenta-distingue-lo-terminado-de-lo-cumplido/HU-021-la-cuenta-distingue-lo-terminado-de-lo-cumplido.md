# HU-021 — Que la cuenta distinga lo terminado de lo cumplido

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-021 |
| **Épica / Feature** | [EP-004 Comprobación automática de lo que no admite discusión](../epica.md) |
| **Módulo / Componente** | Programas de comprobación |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien decide en qué trabajar
- **Quiero** que «cuántas historias faltan» no cuente como hecha una fase que no cumplió
- **Para** no elegir el próximo trabajo mirando un número que se ve mejor de lo que es

---

## 3. Contexto y descripción

**Diecinueve fases cerradas dicen «No cumple», y las diecinueve cuentan como completas.** De las 84 historias que el inventario da por hechas, **casi una de cada cuatro descansa en una fase que no cumplió su criterio**.

**Es la tercera forma del mismo defecto en dos días**, y las dos anteriores se arreglaron:

| Cuándo | Qué contaba mal | Cómo se arregló |
|---|---|---|
| Hasta la `35.0.0` | El número se copiaba a mano y se desfasaba | Se quitó la copia (`S-049`) |
| Hasta el 2026-08-27 | Contaba archivos presentes: un molde en blanco pasaba por terminado | Se llenaron los cuatro (`S-053`) |
| **Hoy** | Cuenta fases cerradas **sin mirar su veredicto** | Esta historia |

**Cada arreglo dejó el conteo más honesto y siguió midiendo la cosa de al lado.**

### La causa no es descuido: los moldes se contradicen

| Molde | Qué vocabulario ofrece para el veredicto |
|---|---|
| [`09-resultado-pruebas.md`](../../../../plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md) §6 | `Cumple / No cumple`, y dice **«no hay estado intermedio»** |
| [`11-funcionalidad-implementada.md`](../../../../plantillas/ciclo-vida-proyectos/11-funcionalidad-implementada.md) | `Cumple / Cumple con observaciones` |

**El molde del cierre no tiene forma de decir «No cumple».** Por eso las 19 fases lo escriben en prosa, arriba del todo, antes de la identificación: **tuvieron que inventarse un sitio**. Y lo que se inventa cada uno, ningún programa lo lee.

**Y hay una contradicción más de fondo:** el molde de resultados dice **«la fase no cierra con un CA en No»**, mientras 19 fases cerradas lo hacen — con precedente, declarándolo, y siendo lo correcto. **La regla escrita no describe lo que se hace, y lo que se hace es lo razonable.**

### El dato existe, y está en el documento correcto

| Documento | Traen veredicto legible | No lo traen |
|---|---|---|
| `resultado_pruebas.md` | **103 de 128** | 25 |
| `funcionalidad_implementada.md` | 55 de 125 | **70** |

**El veredicto vive donde tiene que vivir**: en el resultado de pruebas, que es quien lo produce. Lo que falta es que **el conteo lo mire** y que los 25 restantes lo declaren.

### 3.1 Reglas de negocio

| ID | Regla | De dónde baja |
|---|---|---|
| RN-01 | El conteo distingue **terminada** de **cumplida**, y dice las dos | Hallazgo del 2026-08-27; `S-054` |
| RN-02 | El veredicto se lee del `resultado_pruebas.md`, que es quien lo produce | Ahí está en 103 de 128; en el cierre, en 55 de 125 |
| RN-03 | El vocabulario del veredicto es uno solo: `Cumple` / `No cumple` | El molde de resultados ya lo dice; el del cierre ofrece otro |
| RN-04 | El molde del cierre gana forma de declarar «No cumple» | Hoy no la tiene, y por eso 19 lo escriben en prosa |
| RN-05 | Una fase **sí puede cerrar** con «No cumple», y el molde deja de decir lo contrario | Hay 19 cerradas así, con precedente y siendo lo correcto: cerrar no es aprobar |
| RN-06 | Una fase sin veredicto legible **se cuenta aparte**, no se reparte entre las otras dos | `S-038`: lo que no se puede leer se cuenta aparte |
| RN-07 | El programa avisa, no corrige | `EP-004 §10.2` y `DA-06` |

### 3.2 Supuestos

- El veredicto de una fase es el que decide si su criterio quedó cumplido. Una historia con varias fases se resuelve en `CA-02`.

### 3.3 Fuera de alcance

- **Arreglar las 19 fases que no cumplen.** Esta historia las hace visibles; resolverlas es trabajo de cada una.
- **Rellenar el veredicto de los 25 resultados que no lo traen.** Se cuentan aparte, y quien los cierre lo pondrá.
- **Los veredictos de épicas o planes.** Solo fases.

---

## 4. Criterios de aceptación

### CA-01 — La cuenta dice las dos cosas

```gherkin
Dado que hay historias cuyas fases cerraron con «No cumple»
Cuando se corre la comprobación de fases
Entonces la línea del inventario distingue las terminadas de las que cumplen
Y quien la lee sabe cuál es cuál sin interpretar
```

**Cómo validarlo:**
1. Correr `python validadores/validar.py fases` desde la raíz.
2. Leer la última línea. Resultado esperado: además del total y las incompletas, dice **cuántas cumplen** y **cuántas terminaron sin cumplir**.
3. Sumar los números de la línea. Resultado esperado: cuadran con el total, sin que sobre ni falte ninguna.
4. Comparar «las que cumplen» contra el conteo de fases con veredicto `Cumple`. Resultado esperado: coinciden.
- **Aprobado cuando:** la línea dice las dos cosas y los números cuadran.

### CA-02 — Una historia con una fase que no cumple no se cuenta cumplida

```gherkin
Dado un árbol con una historia de dos fases, una que cumple y otra que no
Cuando se cuenta
Entonces esa historia figura como terminada pero no como cumplida
Y si las dos cumplen, figura en las dos
```

**Cómo validarlo:**
1. Armar un árbol de prueba con una historia de dos fases, las dos con sus cinco documentos.
2. Poner en una `Concepto: Cumple` y en la otra `Concepto: No cumple`.
3. Contar. Resultado esperado: la historia cuenta terminada y **no** cuenta cumplida.
4. Cambiar la segunda a `Cumple` y contar otra vez. Resultado esperado: ahora cuenta en las dos.
- **Aprobado cuando:** basta una fase que no cumpla para que la historia no cuente cumplida.

### CA-03 — Lo que no se puede leer se cuenta aparte

```gherkin
Dado un árbol con una fase cuyo resultado no declara veredicto
Cuando se cuenta
Entonces esa historia no se suma ni a las que cumplen ni a las que no
Y la línea dice cuántas quedaron sin poder leerse
```

**Cómo validarlo:**
1. Armar un árbol con una historia cuya fase tenga los cinco documentos pero **sin** veredicto en su resultado.
2. Contar. Resultado esperado: la línea trae una tercera cuenta, de las que no se pudieron leer, con esa historia dentro.
3. Comprobar que **no** aparece entre las que cumplen ni entre las que no. Resultado esperado: no está en ninguna de las dos.
4. Ponerle el veredicto y contar otra vez. Resultado esperado: sale de la tercera cuenta y entra donde corresponda.
- **Aprobado cuando:** ninguna historia sin veredicto legible se reparte entre las otras dos cuentas.

### CA-04 — El molde del cierre puede decir «No cumple»

```gherkin
Dado que hoy el molde ofrece «Cumple / Cumple con observaciones»
Cuando alguien cierra una fase que no cumplió
Entonces encuentra dónde declararlo, con el mismo vocabulario del resultado
Y el molde ya no dice que una fase no cierra con un criterio en rojo
```

**Cómo validarlo:**
1. Abrir el molde del cierre y buscar el campo del veredicto. Resultado esperado: ofrece `Cumple` o `No cumple`, y ninguna tercera opción.
2. Abrir el molde del resultado y comparar el vocabulario. Resultado esperado: es el mismo, palabra por palabra.
3. Buscar en los dos moldes la frase que dice que una fase no cierra con un criterio en rojo. Resultado esperado: ya no está, o dice que cierra **declarándolo**.
4. Comprobar que el campo del cierre está donde un programa lo encuentre, no en prosa suelta. Resultado esperado: es un campo, con su rótulo.
- **Aprobado cuando:** los dos moldes usan el mismo vocabulario y el cierre tiene dónde decir «No cumple».

### CA-05 — La versión sube, porque cambiaron los moldes

**Cómo validarlo:**
1. Anotar `VERSION` antes del cambio.
2. Aplicar el cambio y leerlo. Resultado esperado: subió.
3. Leer la entrada del `CHANGELOG`. Resultado esperado: dice que el número de historias completas **va a cambiar de significado**, y qué verá quien ya tenía el estándar.
4. Correr `validar.py versionado`. Resultado esperado: sin incumplimientos.
- **Aprobado cuando:** el par sube junto y la entrada avisa del cambio de significado.

### Criterios de aceptación transversales

- [x] **No regresión** — la cuenta de totales e incompletas sigue dando lo mismo, y la suite queda verde.
- [x] **Límites** — están definidos: una historia sin fases, una fase sin resultado, y un veredicto escrito en otra forma.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Claridad** | La línea se entiende sin leer la documentación: dice qué es cada número |
| RNF-02 | **Rendimiento** | Leer el veredicto no agrega un recorrido nuevo del árbol |

---

## 6. Diseño y referencias

- **Dónde se cuenta:** `inventario` y `linea_inventario` en `validadores/fases.py`.
- **De dónde sale el veredicto:** el §6 del `resultado_pruebas.md` de cada fase.
- **Los dos moldes que se contradicen:** [`09`](../../../../plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md) y [`11`](../../../../plantillas/ciclo-vida-proyectos/11-funcionalidad-implementada.md).

---

## 7. Tareas técnicas derivadas

- [ ] «Backend» Leer el veredicto de cada fase desde su resultado.
- [ ] «Backend» Contar terminadas, cumplidas y sin veredicto legible.
- [ ] «Documentación» Que el molde del cierre pueda decir «No cumple», con el mismo vocabulario.
- [ ] «Documentación» Quitar de los moldes la frase que dice que una fase no cierra con un rojo.
- [ ] «Pruebas» Casos de las tres cuentas y de los bordes.
- [ ] «Documentación» Entrada en el `CHANGELOG` y subir `VERSION`.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| [`A-EP-004-HU-021-la-cuenta-mira-el-veredicto`](A-EP-004-HU-021-la-cuenta-mira-el-veredicto/) | CA-01 a CA-05 | (vacío) | [plan_trabajo](A-EP-004-HU-021-la-cuenta-mira-el-veredicto/plan_trabajo.md) | [plan_pruebas](A-EP-004-HU-021-la-cuenta-mira-el-veredicto/plan_pruebas.md) | [resultado](A-EP-004-HU-021-la-cuenta-mira-el-veredicto/resultado_pruebas.md) · cumple | Terminada |
| [`D-EP-004-HU-021-las-dos-formas-que-quedaban-sin-leerse`](D-EP-004-HU-021-las-dos-formas-que-quedaban-sin-leerse/) | La tercera cuenta | fase `C` | [plan_trabajo](D-EP-004-HU-021-las-dos-formas-que-quedaban-sin-leerse/plan_trabajo.md) | [plan_pruebas](D-EP-004-HU-021-las-dos-formas-que-quedaban-sin-leerse/plan_pruebas.md) | [resultado](D-EP-004-HU-021-las-dos-formas-que-quedaban-sin-leerse/resultado_pruebas.md) · cumple | Terminada |

Van juntos porque **contar sin arreglar el molde deja 70 cierres sin dónde declarar el veredicto**, y arreglar el molde sin contar no cambia ningún número.

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Que el número de completas **baje mucho de golpe** y se lea como un retroceso | No es retroceso: es la primera medición honesta. La entrada del `CHANGELOG` lo dice, y `CA-05` lo exige |
| Riesgo | Que las 25 fases sin veredicto legible se repartan entre las otras dos cuentas | `CA-03`. Es `S-038`: lo que no se puede leer se cuenta aparte |
| Riesgo | Que el veredicto esté escrito de formas distintas y el programa lea mal | `RN-03` fija el vocabulario, y los bordes tienen su caso |

---

## 10. Definition of Ready (DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Diseño / mockup disponible — no aplica: no hay interfaz
- [x] Dependencias identificadas y desbloqueadas
- [x] Estimada por el equipo
- [x] Cumple criterios INVEST

## 11. Definition of Done (DoD)

- [x] Código implementado y en rama principal
- [x] Pruebas unitarias e integración pasando — 417 de 417
- [ ] Code review aprobado — lo hace el usuario al aprobar la fase
- [x] Todos los criterios de aceptación verificados
- [x] Requisitos no funcionales validados
- [x] Documentación técnica y de usuario actualizada
- [ ] Desplegada en ambiente de pruebas — no aplica
- [ ] Aceptada por el Product Owner

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | ☑ | No depende de nada abierto |
| **N**egociable | ☑ | Cómo se muestra la línea se puede discutir sin tocar el objetivo |
| **V**aliosa | ☑ | Es el número con que se decide qué hacer, y hoy está mal en un 23% |
| **E**stimable | ☑ | Una función, dos moldes y sus pruebas |
| **S**mall (pequeña) | ☑ | Una sola fase |
| **T**esteable | ☑ | Los cinco criterios se comprueban con árboles de prueba y corriendo el comando |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-27 | Agente, con el usuario | Creación de la HU. Sale de `S-054`, al ver que cerrar cinco fases con «No cumple» bajó el número de incompletas en cinco |
