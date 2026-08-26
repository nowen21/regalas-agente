# HU-012 — Una sola palabra para cada estado

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-012 |
| **Épica / Feature** | [EP-003 Documentos modelo y procedimientos guiados](../epica.md) |
| **Módulo / Componente** | Documentos modelo |
| **Tipo** | Técnica |
| **Prioridad** | Should |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Terminada |
---

## 2. Narrativa

- **Como** quien lee o escribe un documento del ciclo de vida
- **Quiero** que «terminado» se escriba siempre igual
- **Para** poder saber si algo está cerrado sin interpretar, y para que un programa pueda comprobarlo

---

## 3. Contexto y descripción

**Tres palabras distintas para «terminado», y una lista que se contradice consigo misma.** Leído línea por línea el 2026-08-26:

| Molde | Qué estado define | Vocabulario | Palabra para «terminado» |
|---|---|---|---|
| [`03-epica.md`](../../../../plantillas/ciclo-vida-proyectos/03-epica.md) ·21 | El de una **épica** | Propuesta / Aprobada / En curso / Completada / Cancelada | `Completada` |
| [`01-planteamiento.md`](../../../../plantillas/ciclo-vida-proyectos/01-planteamiento.md) ·93 | El de una **épica**, otra vez | Propuesta / Aprobada / En curso / Completada | `Completada` |
| [`04-HU.md`](../../../../plantillas/ciclo-vida-proyectos/04-HU.md) ·20 | El de una **historia** | Backlog / Ready / En curso / En QA / Done | `Done` |
| [`10-estado-fase.md`](../../../../plantillas/ciclo-vida-proyectos/10-estado-fase.md) ·60 | El de una **tarea** | Pendiente / En curso / Hecha / Bloqueada | `Hecha` |

**Que épica, historia y tarea tengan conjuntos distintos es correcto**: una épica se cancela y una tarea se bloquea, y una historia ninguna de las dos. Lo que no lo es: que **el mismo concepto se escriba de tres formas**, y que el estado de una épica esté definido **dos veces con listas distintas** — `01-planteamiento` no trae `Cancelada` y `03-epica` sí.

**Y el resultado se ve en el árbol.** De las 114 historias, **51 se salen del vocabulario de su propio molde**: cinco palabras distintas significan cerrado —`Done`, `Cumplida`, `Cerrada`, `Hecha`, `Terminada`— y hay un estado usado 19 veces que ningún molde define: `En implementación`.

**No es descuido, y por eso regañar no lo arregla.** Quien escribe una historia justo después de una épica escribe «Completada» con toda lógica: acaba de leerlo en el molde de al lado. **El estándar enseñó tres palabras para la misma cosa**, y después las encontró repartidas.

**El sitio del arreglo ya existe.** El [glosario](../../../../base/glosario.md) dice de sí mismo que sirve *«para que dos documentos no llamen distinto a la misma cosa»*. Tiene 95 entradas y **no cubre los estados**, que es justamente donde el problema apareció.

**Y esto es lo que traba lo siguiente.** Hoy ningún programa puede saber si una historia está cerrada sin una lista de sinónimos que envejece. Sin una sola palabra, no hay comprobación posible — y el 2026-08-26 se afirmó cuatro veces que una historia estaba abierta cuando decía `Done`, sin que nada lo cazara.

### 3.1 Reglas de negocio

| ID | Regla | De dónde baja |
|---|---|---|
| RN-01 | El glosario define los estados, y es el único sitio donde se definen | El propósito escrito del glosario |
| RN-02 | Los moldes del ciclo de vida citan el glosario en vez de llevar cada uno su lista | Cuatro listas, y una de ellas definida dos veces sin coincidir |
| RN-03 | Un estado por concepto: si dos palabras significan lo mismo, sobra una | `S-048` y lo medido |
| RN-04 | `En implementación` pasa a ser `En curso`, que ya existe y significa lo mismo | Decisión del usuario, 2026-08-26 |
| RN-05 | Los documentos existentes se normalizan, incluidos los de fases cerradas | Decisión del usuario. El campo es un índice, no el registro de lo que pasó. **Al traducir son 111 de 115, no 51**: `Backlog` solo son 54 |
| RN-06 | Un programa comprueba que el estado esté en el vocabulario, y **avisa** | `EP-004 §10.2`: reporta y no corrige |
| RN-07 | Épica, historia y fase pueden tener **conjuntos** distintos, pero la palabra de un concepto compartido es una sola | Una épica se cancela y una historia no; «terminado» es lo mismo en las tres |
| RN-08 | El vocabulario se escribe **en español** | `01·C20` lo exige, y el glosario es justamente el documento que lleva la lista de lo que se queda en otro idioma y por qué. Escribir ahí `Backlog` sin razón sería incumplir en el archivo donde más se nota |

### 3.2 Supuestos

- El vocabulario de [`04-HU.md`](../../../../plantillas/ciclo-vida-proyectos/04-HU.md) sirve de base **en su forma**, no en sus palabras: tres de las cinco están en inglés y hay que traducirlas (`RN-08`).
- Cambiar `Terminada` por `Done` en una historia cerrada **no cambia ningún hecho**: dice lo mismo con la palabra acordada.

### 3.3 Fuera de alcance

- **Cambiar qué significa cada estado.** Se unifica cómo se escribe, no qué quiere decir.
- **Los estados de documentos que no son del ciclo de vida** (pendientes, señales, decisiones de arquitectura). Si también divergen, sale de un barrido aparte.
- **La regla de no citar como abierto lo que está cerrado.** Depende de esta y va después.
- **Los estados de otros documentos del proyecto** que no sean épica, historia o tarea. Si también divergen, sale de un barrido aparte.


### 3.4 El vocabulario, acordado el 2026-08-26

**Mismo concepto, misma palabra.** Que los conjuntos difieran es correcto; que «terminado» se diga de tres formas, no.

| Concepto | Palabra | La usan |
|---|---|---|
| Todavía no empezó | **Pendiente** | épica · historia · tarea |
| Propuesta, sin aprobar | **Propuesta** | épica |
| Aprobada, sin empezar | **Aprobada** | épica |
| Escrita y lista para construir | **Lista** | historia |
| Se está construyendo | **En curso** | épica · historia · tarea |
| Construida, probándose | **En prueba** | historia |
| Terminada | **Terminada** | épica · historia · tarea |
| Detenida por algo de afuera | **Bloqueada** | tarea |
| Se decidió no hacerla | **Cancelada** | épica |

Los tres conjuntos quedan:

- **Épica:** Propuesta · Aprobada · En curso · Terminada · Cancelada
- **Historia:** Pendiente · Lista · En curso · En prueba · Terminada
- **Tarea:** Pendiente · En curso · Terminada · Bloqueada

**«Terminada» y no «Cerrada»**, aunque seis historias usen `Cerrada` hoy: `cerrada` ya significa otra cosa en el estándar — es como se marca una **estación** de fase. Reusarla mezclaría dos vocabularios.

---

## 4. Criterios de aceptación

### CA-01 — El glosario define los estados, una vez

```gherkin
Dado que hoy cada molde trae su propia lista de estados
Cuando alguien quiere saber cómo se escribe «terminado»
Entonces lo encuentra en el glosario, con su fila y su definición
Y no encuentra dos palabras distintas para el mismo concepto
```

**Cómo validarlo:**
1. Abrir [base/glosario.md](../../../../base/glosario.md).
2. Buscar la entrada de los estados. Resultado esperado: existe, y lista cada estado con qué significa.
3. Comprobar que ninguna palabra de la lista signifique lo mismo que otra. Resultado esperado: no hay sinónimos.
4. Buscar en los cuatro moldes del ciclo de vida si alguno define su propia lista de estados. Resultado esperado: ninguno la define; todos remiten al glosario.
- **Aprobado cuando:** hay un solo sitio donde los estados están definidos, y los moldes apuntan ahí.

### CA-02 — Los 114 documentos usan el vocabulario

```gherkin
Dado que 51 historias se salían del vocabulario de su molde
Cuando se normalizan
Entonces las 114 usan una palabra de la lista del glosario
Y ninguna cambió de significado al hacerlo
```

**Cómo validarlo:**
1. Antes de tocar nada, guardar la lista de las 114 historias con el estado que declara cada una.
2. Aplicar el cambio.
3. Volver a leer las 114. Resultado esperado: todas usan una palabra del glosario.
4. Comparar la lista de antes con la de después, par por par. Resultado esperado: cada cambio es de sinónimo a palabra acordada — `Terminada` a `Done`, `En implementación` a `En curso` — y ninguna historia pasó de abierta a cerrada ni al revés.
5. Contar cuántas historias contaba el árbol como completas antes y después. Resultado esperado: el mismo número.
- **Aprobado cuando:** las 114 están dentro del vocabulario y **ningún estado cambió de sentido**.

### CA-03 — Escribir un estado inventado se avisa

```gherkin
Dado que el vocabulario está definido en un solo sitio
Cuando un documento declara un estado que no está en la lista
Entonces la comprobación lo reporta, diciendo cuál escribió y cuáles valen
Y el documento queda igual: no se corrige solo
```

**Cómo validarlo:**
1. En una copia de trabajo, poner en una historia un estado inventado, por ejemplo `Casi lista`.
2. Correr la comprobación de fases. Resultado esperado: reporta ese archivo, nombra el estado escrito, y dice cuáles son los válidos.
3. Volver a abrir el archivo. Resultado esperado: sigue diciendo `Casi lista`. El programa reportó y no corrigió.
4. Devolverlo a un estado válido y correr otra vez. Resultado esperado: no reporta nada sobre ese archivo.
- **Aprobado cuando:** el aviso aparece con el estado inventado, dice qué se puede escribir, y en ningún caso el archivo cambió solo.

### CA-04 — La versión sube, porque cambiaron los moldes

```gherkin
Dado que «20·M10» exige versionar todo cambio de «base/» o «plantillas/»
Cuando el glosario y los cuatro moldes cambian
Entonces «VERSION» sube y el «CHANGELOG» gana su entrada
Y la entrada dice qué tiene que hacer un proyecto que ya tenía el estándar
```

**Cómo validarlo:**
1. Anotar `VERSION` antes del cambio.
2. Aplicar el cambio.
3. Leer `VERSION`. Resultado esperado: subió.
4. Leer la primera entrada del `CHANGELOG`. Resultado esperado: dice qué cambia para un proyecto que ya tenía el estándar, y si tiene que hacer algo.
5. Correr `validar.py versionado`. Resultado esperado: sin incumplimientos.
- **Aprobado cuando:** el par sube junto y el validador lo acepta.

### Criterios de aceptación transversales

- [x] **No regresión** — lo existente sigue funcionando y la suite queda verde (`08`, `02·F5`).
- [x] **Límites** — está definido qué pasa con un documento sin campo de estado, y con uno cuyo estado trae texto adicional después de la palabra.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Claridad** | Quien escribe un documento sabe qué poner leyendo solo su molde, sin abrir los otros tres |
| RNF-02 | **Trazabilidad** | El cambio queda versionado, y cada documento normalizado se puede comparar contra lo que decía |

---

## 6. Diseño y referencias

- **Dónde se define:** [base/glosario.md](../../../../base/glosario.md), que hoy tiene 95 entradas y ninguna de estados.
- **Los cuatro moldes:** `01-planteamiento`, `03-epica`, `04-HU` y `10-estado-fase`, en [plantillas/ciclo-vida-proyectos/](../../../../plantillas/ciclo-vida-proyectos/).
- **Dónde va la comprobación:** `validadores/fases.py`, que ya recorre las historias.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] «Documentación» Definir los estados en el glosario, con qué significa cada uno.
- [ ] «Documentación» Que los cuatro moldes citen el glosario en vez de listar.
- [ ] «Documentación» Normalizar los 51 documentos, guardando el antes para comparar.
- [ ] «Backend» Comprobar que el estado esté en el vocabulario, y avisar.
- [ ] «Pruebas» Casos del vocabulario, del estado inventado y de los bordes.
- [ ] «Documentación» Entrada en el `CHANGELOG` y subir `VERSION`.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| [`A-EP-003-HU-012-una-sola-palabra-por-estado`](A-EP-003-HU-012-una-sola-palabra-por-estado/) | CA-01, CA-02, CA-03, CA-04 | (vacío) | [plan_trabajo](A-EP-003-HU-012-una-sola-palabra-por-estado/plan_trabajo.md) | [plan_pruebas](A-EP-003-HU-012-una-sola-palabra-por-estado/plan_pruebas.md) | [resultado](A-EP-003-HU-012-una-sola-palabra-por-estado/resultado_pruebas.md) · cumple | Terminada |

Van juntos porque **normalizar sin definir deja el mismo problema con otras palabras**, y **definir sin comprobar deja que vuelva**. `CA-04` es la condición para que el cambio de moldes exista según `20·M10`.

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Que normalizar cambie el sentido de un estado sin que nadie lo note | `CA-02` compara par por par, y cuenta las completas antes y después. Si el número se mueve, algo cambió de sentido |
| Riesgo | Que un estado traiga texto útil después de la palabra, como `Cumplida — los tres CA verificados` | Se conserva: se normaliza **la palabra**, no la frase. Es un borde declarado en el transversal |
| Riesgo | Que tocar documentos de fases cerradas se lea como reabrirlas | No se reabren: el campo es un índice, no el registro de lo que pasó. Queda dicho en el cierre y en el `CHANGELOG` |
| Riesgo | Que el vocabulario en inglés choque con `01·C8` | Declarado fuera de alcance a propósito. Mezclarlo volvería este cambio mucho más grande, y hoy el problema es que sean tres palabras, no en qué idioma |

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
- [x] Pruebas unitarias e integración pasando — 396 de 396
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
| **N**egociable | ☑ | Qué palabra gana para cada concepto se puede discutir sin tocar el objetivo |
| **V**aliosa | ☑ | Es lo que traba poder comprobar por programa si algo está cerrado |
| **E**stimable | ☑ | Un glosario, cuatro moldes, 51 documentos y una comprobación |
| **S**mall (pequeña) | ☑ | Una sola fase, aunque toque muchos archivos: el cambio es mecánico |
| **T**esteable | ☑ | Los cuatro criterios se comprueban leyendo archivos y corriendo comandos |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-26 | Agente, con el usuario | Creación de la HU. Sale de medir por qué se pudo afirmar cuatro veces que una historia cerrada estaba abierta (`S-048`) |
| 2026-08-26 | Agente y usuario | El alcance creció: se decidió **traducir** el vocabulario, y pasó de 51 documentos a 111 |
| 2026-08-26 | Agente | Cerrada la fase `A`. Los cuatro criterios cumplidos; tres defectos, los tres corregidos (`S-049`, `S-050`) |
