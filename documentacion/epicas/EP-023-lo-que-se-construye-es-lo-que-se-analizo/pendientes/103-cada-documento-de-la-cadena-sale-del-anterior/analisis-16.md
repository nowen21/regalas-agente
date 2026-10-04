# Análisis 16: el commit rechaza lo que un análisis aprobado mandó hacer de una

> Este análisis se redacta aplicando estas reglas.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../../../../../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](../../../../../base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Viene del [análisis 15](analisis-15.md), aprobado el 2026-10-03. Trata el H-20, que apareció al guardar el commit de los análisis 14 y 15.

---

## Recomendaciones

| Recomendación | Cómo se aplica en este análisis |
|---|---|
| R-16 | Lo que falló en el control del commit se corrige de una aquí |
| R-17 | Las respuestas se miden contra `00·ID9` |
| Las demás | No aplican: no se crean reglas y no hay plan en ejecución |

---

## Hallazgo

### H-20 · El commit rechaza lo que un análisis aprobado mandó hacer de una

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-03, el control del commit rechazó 12 archivos que las filas «de una» de los análisis 14 y 15 del pendiente 103 mandaron hacer: solo acepta esas filas mientras el análisis está prendido, y los dos ya estaban aprobados. |
| Por qué importa | Lo que un análisis manda hacer de una no se puede guardar después de aprobarlo, y aprobarlo es el paso anterior al commit. |

## Pendiente

Versión 7, del análisis 15: [pendiente](pendiente.md), tal como estaba al empezar este análisis.

---

## Conversación

> La escribe el enganche en tiempo real, turno por turno, desde la transcripción de la sesión. No se escribe a mano.

### 582 · Usuario, 2026-10-03 23:37:24
> Analicemos: el pendiente 103

**Agente**, 2026-10-03 23:40:34
<!-- agente: 873b3347-b4a5-4e1e-8d04-81211bd258b8 -->

Abro el análisis 16. Primero anoto el hallazgo del commit rechazado en el resumen de la sesión, porque apareció cuando no había ningún análisis prendido.

Ahora lleno el análisis 16 con su fila «de una».

Ahora el código: una función que lee las rutas «de una» de cualquier análisis, y el control del commit que la usa.

Pasan las 49 pruebas. Ahora la versión 8 del pendiente, la 53.1.2, y una revisión del commit antes de guardarlo.

El control del commit ya pasa con todo adentro, en la versión 53.1.2. Pasan las 49 pruebas del control del commit, del freno y de la integración continua.

Falta tu «Apruebo el análisis» para el análisis 16. En ese mismo turno hago el commit completo y lo subo, como lo pediste.

### 583 · Usuario, 2026-10-03 23:41:03
> Pregunta: qué pasó nos quedamos en el ciclo creando análisis? hay solucionar eso ya me está desgastando demaciado, analice todos los análisis del pendiente 103 para ver por qué se están generando tantos análisis

**Agente**, 2026-10-03 23:41:41
<!-- agente: 1b254285-5d7b-4a7d-a221-bcf68871e23e -->

Reviso de dónde salió cada uno de los 16 análisis.

Sí, quedamos atrapados en un ciclo. De los 16 análisis, solo 3 trajeron trabajo nuevo de verdad: el 8 (el freno), el 10 (los planes leen lo acordado) y el 13 (los proyectos reportan pendientes). Los otros 13 nacieron de cuatro causas:

1. **El pendiente construye las herramientas con las que se trabaja.** Cuando falla el freno, el validador o el control del commit, se detiene el trabajo y la regla obliga a abrir otro análisis. Pasó en los análisis 2, 14, 15 y 16.
2. **Antes de la versión 52.1.0, todo hallazgo abría un análisis**, por pequeño que fuera. Así nacieron los análisis 3 a 7 y el 9.
3. **El plan no encuentra qué pruebas leen lo que cambia.** Pasó en los análisis 11 y 12, y hoy otra vez en la fase C de la HU-003.
4. **Sin un análisis prendido, el freno no deja corregir nada.** Los análisis 15 y 16 existen solo para destrabar la escritura.

Propongo cuatro cambios:
1. **«Corrija»:** que corregir una herramienta del proceso que bloquea trabajo legítimo se haga con esa palabra, sin abrir un análisis. Lo que se corrija queda anotado en el resumen de la sesión.
2. **Al escribir el plan:** que un programa busque qué pruebas importan cada archivo que cambia y las ponga en la sección 2.1.
3. **El freno:** que ignore el texto de los heredocs, que es donde estaba el `>=`.
4. **Cerrar el pendiente 103 con el análisis 16:** lo que aparezca después va a un pendiente nuevo, «las herramientas del proceso».

¿Están de acuerdo?

### 584 · Usuario, 2026-10-03 23:42:26
> 00 id9

**Agente**, 2026-10-03 23:42:38
<!-- agente: 96eff2d8-6a97-4f63-ad08-330bed00bfe6 -->

Solo 3 de los 16 análisis trajeron trabajo nuevo. Los otros 13 los abrieron fallas de las propias herramientas, o un freno que no deja corregir nada sin un análisis prendido.

Propuesta:
1. Que «Corrija» arregle una herramienta del proceso sin abrir un análisis.
2. Que un programa diga qué pruebas toca cada plan.
3. Que el freno ignore lo que va dentro de un heredoc.
4. Que el pendiente 103 se cierre con el análisis 16.

¿Están de acuerdo?

### 585 · Usuario, 2026-10-03 23:43:16
> pregunta: se crearon análisis por crear?

**Agente**, 2026-10-03 23:43:29
<!-- agente: 7b2609f7-484a-465b-90b9-48c6674f8097 -->

No se crearon por crear. Pero sí sobran varios, y unos los causé yo:

- **Los análisis 3 a 7 y el 9** salieron de la regla que había antes: todo hallazgo, por pequeño que fuera, abría un análisis. Se cumplió tal cual. Hoy esa regla ya no lo exige.
- **Los análisis 11 y 12** salieron de errores míos: escribí planes sin buscar qué pruebas tocaban lo que cambiaba.
- **Los análisis 15 y 16** los pedí yo solo para que el freno me dejara corregir. No había nada que analizar.
- **El 2 y el 14** salieron de fallas en las herramientas que yo mismo construí.

De 16 análisis, solo 4 eran necesarios: el 1, el 8, el 10 y el 13.

### 586 · Usuario, 2026-10-03 23:44:23
> pregunta: si no eran necesarios por qué los hizo crear?

**Agente**, 2026-10-03 23:44:35
<!-- agente: c4f023a6-b7cf-4c3b-ac1f-31c9e31944da -->

Porque seguí la regla al pie de la letra y no les avisé a tiempo que estaba produciendo más trabajo del que resolvía.

- **Los análisis 3 a 7 y el 9:** la regla decía que todo hallazgo abría un análisis. Debí decirles que, para correcciones tan pequeñas, era desproporcionado. Lo dijimos tarde, en la versión 52.1.0.
- **Los análisis 15 y 16:** vi que el freno solo deja escribir con un análisis prendido, y elegí pedirles abrir uno en lugar de decirles que el problema era el freno. Fue el camino más fácil para mí, y les costó a ustedes.
- **Los análisis 11, 12, 14 y 2:** salieron de errores míos en planes y herramientas. Se habrían evitado revisando mejor antes.

Lo que había que hacer era proponer la salida desde la primera vez: que «Corrija» deje arreglar una herramienta sin abrir un análisis. Es el primer punto de la propuesta que está pendiente.

### 587 · Usuario, 2026-10-03 23:46:18
> pregunta:pero entonces ya no se van a crear más?

**Agente**, 2026-10-03 23:46:27
<!-- agente: 0ca7273f-5ebe-4610-8494-15e722ff1ab1 -->

Todavía se pueden crear. Hoy el freno solo deja corregir algo con un análisis prendido, así que cada falla de una herramienta vuelve a pedir uno.

Dejan de crearse sin necesidad si se aprueban los cuatro puntos de la propuesta:
1. «Corrija» arregla una herramienta sin abrir un análisis.
2. Un programa dice qué pruebas toca el plan.
3. El freno ignora lo que va dentro de un heredoc.
4. El pendiente 103 se cierra.

Desde ahí, solo se abriría un análisis cuando aparezca trabajo nuevo de verdad, como pasó con el 8, el 10 y el 13.

### 588 · Usuario, 2026-10-03 23:46:54
> pregunta qué sigue?

**Agente**, 2026-10-03 23:47:05
<!-- agente: 316d2ea7-287b-43e2-a39f-0a20fc9f4218 -->

Sigue aprobar o ajustar los cuatro puntos. Con «Apruebo» los anoto en el análisis 16, que ya está prendido, y los hago ahí mismo. Después se aprueba el análisis y se hace el commit completo con la subida.

### 589 · Usuario, 2026-10-03 23:47:15
> Apruebo

**Agente**, 2026-10-03 23:58:04
<!-- agente: 9c44a2d8-c914-4186-8d0c-47122c657868 -->

Busco cómo saben los enganches cuál fue la palabra del último mensaje.

Anoto el acuerdo y las filas en el análisis 16; después hago los cuatro cambios.

Ahora el código. Primero «Corrija»: el estado en `analisis_en_curso.py` y el enganche que lo anota.

Ahora el freno: que deje pasar «Corrija» y que ignore el texto de los heredocs.

Ahora `plan_vs_hecho.py`: que el `estado-fase.md` solo no cuente como tocar la fase, y el aviso de pruebas que el plan no declara.

El aviso funciona: en el plan de la fase C de la HU-003 habría encontrado la prueba que se olvidó. Ahora las pruebas de los cuatro cambios.

Pasan las 74 pruebas. Falta la excepción en `02·F8`, las copias por tarea y la versión.

Las copias por tarea no cambiaron, porque solo copian el cuerpo de la regla. Corro `pruebas.py` completo, ya que cambiaron el freno y los enganches.

Los cuatro cambios quedaron hechos, en la versión 53.2.0:

1. **«Corrija»:** corrige `validadores/` y `adaptadores/` en esa respuesta, sin abrir un análisis. Lo dice `02·F8` como excepción.
2. **`validar.py plan`:** avisa qué pruebas leen lo que cambia el plan y el plan no declara. En la fase C de la HU-003 habría encontrado la prueba que se olvidó.
3. **El freno:** ya no lee como escritura el texto de un heredoc.
4. **El commit:** la anotación del hash en el estado de una fase ya no cuenta como tocar esa fase.

Pasan las 571 pruebas de `pruebas.py` y las 74 de los cambios. Al análisis 16 no le falta nada.

Falta tu «Apruebo el análisis». Con eso se cierra el pendiente 103, y después hago el commit completo y lo subo.

### 590 · Usuario, 2026-10-03 23:58:57
> hágalo: haga de una todos esos cambios no deje nada pendiente

> acá termina la conversación

---

## Lo acordado

1. El control del commit acepta también las rutas «de una» de todo análisis que entra en el mismo commit, prendido o aprobado: el análisis y lo que mandó hacer se guardan juntos. Se corrige de una (turno 582).
2. Salir del ciclo de análisis: de los 16 análisis del pendiente, solo el 1, el 8, el 10 y el 13 trajeron trabajo nuevo. Se hacen de una cuatro cosas: con «Corrija», el agente corrige una herramienta del proceso (`validadores/`, `adaptadores/`) que bloquea el trabajo sin abrir análisis, y lo anota en el resumen; un programa avisa qué pruebas leen los archivos que el plan cambia y el plan no declara; el freno no lee como escritura lo que va dentro de un heredoc, y el commit no cuenta como tocada una fase solo porque se anotó su hash. El pendiente 103 cierra con este análisis: lo que aparezca después va a un pendiente nuevo (turnos 583 a 589).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `02·F8` (lo que entra al commit está en el plan o lo autoriza algo) y `20·M10` (versionar). No choca ninguna.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| `validadores/plan_vs_hecho.py` | Acepta las rutas «de una» solo del análisis prendido (análisis 14, acuerdo 5) |
| `validadores/freno.py` | `_de_una` lee el análisis prendido; no hay una función que lea un análisis cualquiera |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| Análisis 14, acuerdo 5 | El freno y el control del commit usan la misma lista; aquí la del commit se amplía a los análisis que entran con él |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | PARCHE, 53.1.2: el commit deja de rechazar lo que un análisis aprobado mandó hacer |
| Normas y leyes | Ninguna |
| Herramientas | Ninguna condiciona lo acordado |

### Dónde más puede pasar

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Un análisis aprobado en una sesión y guardado en otra | Cualquier proyecto | El commit lo rechaza | Punto 1: basta con que el análisis entre en el mismo commit |
| Un archivo «de una» que se guarda sin su análisis | Cualquier proyecto | Se rechaza | No hace falta cubrirlo: así el commit no se lleva lo que nadie mandó |

---

## Propuesta final: hallazgo y pendiente V8, épica y HU

### Hallazgo V8. El commit rechaza lo que un análisis aprobado mandó hacer de una

| Campo | Valor |
|---|---|
| Qué pasó | El control del commit solo aceptaba las filas «de una» del análisis prendido. |
| Por qué importa | Lo que se manda hacer de una no se podía guardar después de aprobar el análisis. |

### Pendiente V8. Lo que se construye se aparta de lo aprobado

| Campo | Valor |
|---|---|
| De dónde sale | Lo de la versión 7, más el H-20 de la sesión del 2026-10-01 |
| El problema | Lo de la versión 7, más: el control del commit no aceptaba lo que un análisis aprobado mandó hacer de una |
| Por qué importa | Sin cambio |

### Épica y HU que salen del análisis

Ninguna nueva: se hace de una en este análisis.

## Lecciones aprendidas

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | Una autorización que vale solo mientras el análisis está prendido se acaba antes del commit, que viene después de aprobar | Falló | S-290 | complementa R-16 |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Pasar el pendiente a su versión siguiente | `13·DOC26` | Este análisis, de una y sin fase: `documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/pendiente.md`, hecho el 2026-10-03 |
| 2 | Que el control del commit acepte las rutas «de una» de todo análisis que entra en el mismo commit, con su prueba, y su entrada en `CHANGELOG.md` y `VERSION` | 1 | Este análisis, de una y sin fase: `validadores/plan_vs_hecho.py`, `validadores/freno.py`, `validadores/tests/test_nada_fuera_del_plan.py`, `CHANGELOG.md`, `VERSION`, hecho el 2026-10-03 |
| 3 | Que «Corrija» deje corregir las herramientas del proceso sin abrir análisis: el enganche lo anota al recibir el mensaje, el freno deja escribir `validadores/` y `adaptadores/` en esa respuesta, y `02·F8` lo dice como excepción, con su prueba, las copias por tarea y su entrada en `CHANGELOG.md` | 2 | Este análisis, de una y sin fase: `validadores/analisis_en_curso.py`, `adaptadores/claude-code/hook_analisis.py`, `validadores/freno.py`, `validadores/tests/test_el_freno.py`, `base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md`, `base/reglas-por-tarea/trabajar-cadena-1.md`, `base/reglas-por-tarea/trabajar-cadena-2.md`, `base/reglas-por-tarea/escribir-documento-1.md`, `base/reglas-por-tarea/escribir-documento-2.md`, `base/reglas-por-tarea/cambiar-codigo-1.md`, `base/reglas-por-tarea/cambiar-codigo-2.md`, `base/reglas-por-tarea/cambiar-codigo-3.md`, `base/reglas-por-tarea/cambiar-codigo-4.md`, `base/reglas-por-tarea/README.md`, `base/mapa-de-tareas.md`, hecho el 2026-10-03 |
| 4 | Que `validar.py plan` avise qué pruebas leen los archivos que el plan cambia y el plan no declara, con su prueba | 2 | Este análisis, de una y sin fase: `validadores/plan_vs_hecho.py`, `validadores/validar.py`, `validadores/tests/test_nada_fuera_del_plan.py`, hecho el 2026-10-03 |
| 5 | Que el freno no lea como escritura lo que va dentro de un heredoc, con su prueba | 2 | Este análisis, de una y sin fase: `validadores/freno.py`, `validadores/tests/test_el_freno.py`, hecho el 2026-10-03 |
| 6 | Que el commit no cuente como tocada una fase solo porque entra su `estado-fase.md`, con su prueba | 2 | Este análisis, de una y sin fase: `validadores/plan_vs_hecho.py`, `validadores/tests/test_nada_fuera_del_plan.py`, hecho el 2026-10-03 |

## Lo que aporta al análisis principal

**Resultado:** aclara.

**Lo que suma al análisis principal:** Lo que un análisis manda hacer de una se guarda en el mismo commit que el análisis.
