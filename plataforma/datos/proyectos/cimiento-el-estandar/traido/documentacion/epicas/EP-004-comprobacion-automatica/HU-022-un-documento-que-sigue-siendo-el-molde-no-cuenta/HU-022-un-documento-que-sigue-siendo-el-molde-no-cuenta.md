# HU-022 — Que un documento que sigue siendo el molde no cuente como escrito

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-022 |
| **Épica / Feature** | [EP-004 Comprobación automática de lo que no admite discusión](../epica.md) |
| **Módulo / Componente** | Programas de comprobación |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | En curso |

---

## 2. Narrativa

- **Como** quien decide en qué trabajar
- **Quiero** que una fase recién abierta no cuente como terminada
- **Para** que abrir trabajo no haga subir el número que dice cuánto se ha hecho

---

## 3. Contexto y descripción

**El inventario cuenta que los cinco documentos de una fase existan. El andamio los crea vacíos de entrada.** Así que **una fase recién abierta, sin una línea escrita, ya cuenta como terminada** — y el número que dice cuánto falta se vuelve optimista sin que nadie mienta a propósito.

**Cobró cuatro veces el 2026-08-27**, y las cuatro están medidas:

| Cuándo | Qué pasó |
|---|---|
| Al buscar fases con criterios en rojo | Cuatro figuraban cerradas y su cierre era el molde en blanco, con 31 marcadores cada uno |
| Al crear la `HU-021` para arreglar el conteo | **La historia contaba como terminada** antes de escribir una línea |
| Al crear su fase `B` | Volvió a meter esa historia entre las mudas, y **movió la base de una medición en curso** |
| Al crear su fase `C` | La sacó de «terminadas»: `57 cumplen` pasó a `56` sin que nadie tocara nada |

**Es la cuarta forma del mismo defecto**, y las tres anteriores ya se arreglaron: el número se copiaba a mano (`S-049`), contaba fases cerradas sin mirar su veredicto (`S-055`), y leía solo los encabezados que ya reconocía (`S-058`). **Cada arreglo lo dejó más honesto y siguió midiendo la cosa de al lado.**

**Y el sesgo va siempre en la misma dirección: optimista.** Abrir trabajo hace que el avance se vea mejor.

### La medida: cuáles marcadores, no cuántos

`S-053` propuso contar los marcadores del molde que quedaron sin reemplazar — `«…»` y `AAAA-MM-DD` — y afirmó que separaba sin falsos positivos. **Sobre los 664 documentos del árbol no separa:** este repositorio usa comillas angulares en prosa todo el tiempo, así que un documento largo y bien escrito acumula más marcadores que un molde corto. En la primera corrida dio 38, **y tres eran de una fase escrita, cerrada y publicada media hora antes** (`S-059`).

**Lo que sí separa es cruzar cada documento con su plantilla.** `«Cumple»` es prosa; `«2-4 líneas en lenguaje claro»` está en el molde y solo ahí.

| Documentos de fase | Cuántos |
|---|---|
| Sin ningún marcador del molde | 577 |
| Con uno o dos | 80 |
| **Con tres o más — siguen siendo el molde** | **7** |

Los siete, verificados uno por uno: **cinco `plan_pruebas.md`** con 36 marcadores —`B-EP-002-HU-003`, `B-EP-002-HU-004`, `B-EP-004-HU-011`, `B-EP-004-HU-012`, `B-EP-005-HU-002`— y **dos `estado-fase.md`** con 16 —`A-EP-007-HU-009` y `A-EP-004-HU-021`—.

**Los cinco primeros son fases construidas con su código y sus pruebas, cuyo plan de pruebas nunca se escribió.** No es papeleo perdido: es que nadie sabe con qué casos se comprobaron.

### 3.1 Reglas de negocio

| ID | Regla | De dónde baja |
|---|---|---|
| RN-01 | Un documento cuyos marcadores **siguen siendo los de su plantilla** no cuenta como escrito | `S-053`, y la medida corregida en `S-059` |
| RN-02 | La comparación es **contra la plantilla**, no contra un umbral de cuántos marcadores hay | `S-059`: contar síntomas mide el estilo de la casa |
| RN-03 | Una fase con un documento sin llenar **no está terminada** | Es la misma regla que ya se aplica a un documento que falta |
| RN-04 | El programa **dice cuáles**, no solo cuántos | `S-040`: un registro que dice cuántos sin decir cuáles no demuestra nada |
| RN-05 | El programa **avisa, no corrige** | `EP-004 §10.2` y `DA-06` |
| RN-06 | El umbral y la lista de plantillas se leen del repositorio, **no de una lista en el código** | Es lo que se hizo con el vocabulario de estados (`S-049`) |

### 3.2 Supuestos

- Las plantillas de `plantillas/ciclo-vida-proyectos/` son la fuente de qué es un marcador del molde. Si una plantilla cambia sus marcadores, la comparación se ajusta sola.

### 3.3 Fuera de alcance

- **Llenar los siete documentos.** Esta historia los hace visibles; escribirlos es trabajo de cada fase.
- **Que el andamio deje de crear los cinco documentos de entrada.** Es la salida 2 del [pendiente 88](../../../../pendientes/hecho/el-molde-sin-llenar-no-cuenta-como-escrito.md), y **el usuario la dejó fuera a propósito**: cambia cómo se abre una fase, y eso es hábito, no defecto.
- **Los documentos que no son de fase** — épicas, historias, planteamiento. Solo los cinco de una fase.

---

## 4. Criterios de aceptación

### CA-01 — Una fase con un documento sin llenar no cuenta terminada

```gherkin
Dado un árbol con una historia cuya fase tiene sus cinco documentos
Y uno de ellos conserva los marcadores de su plantilla
Cuando se cuenta
Entonces esa historia figura entre las que no están terminadas
Y no aparece entre las terminadas
```

**Cómo validarlo:**
1. Armar un árbol con una historia de una fase, con los cinco documentos escritos.
2. Contar. Resultado esperado: figura terminada.
3. Reemplazar uno de los cinco por la plantilla sin llenar.
4. Contar otra vez. Resultado esperado: **sale de las terminadas** y entra en las que no lo están.
- **Aprobado cuando:** el mismo árbol cambia de cuenta según el documento esté escrito o sea el molde.

### CA-02 — La comparación es contra la plantilla, no contra un umbral

```gherkin
Dado un documento largo y bien escrito que usa comillas angulares en su prosa
Cuando se comprueba si sigue siendo el molde
Entonces no se lo señala, por muchas comillas que tenga
```

**Cómo validarlo:**
1. Tomar un documento real de una fase cerrada, con más de diez marcadores de prosa.
2. Comprobarlo. Resultado esperado: **no se señala**.
3. Comprobar el `plan_pruebas.md` de `B-EP-004-HU-011`, que es la plantilla sin llenar.
4. Resultado esperado: **se señala**, y dice cuáles marcadores son del molde.
- **Aprobado cuando:** ningún documento escrito se señala, y los siete que son el molde sí.

**Este es el criterio que importa.** Un umbral por cantidad ya se probó y falla: señaló tres documentos escritos el mismo día en que se escribieron (`S-059`).

### CA-03 — El aviso dice cuáles, con su documento

```gherkin
Dado que hay documentos que siguen siendo el molde
Cuando se corre la comprobación de fases
Entonces el aviso nombra la fase y el documento de cada uno
Y no solo cuántos hay
```

**Cómo validarlo:**
1. Correr `python validadores/validar.py fases` desde la raíz.
2. Leer los avisos. Resultado esperado: uno por documento, con la fase y el nombre del archivo.
3. Contar los avisos contra la cuenta que da la línea. Resultado esperado: coinciden.
- **Aprobado cuando:** se puede ir a arreglar cada uno sin volver a medir.

### CA-04 — Las plantillas se leen del repositorio

```gherkin
Dado que una plantilla cambia sus marcadores
Cuando se vuelve a comprobar
Entonces la comparación usa los marcadores nuevos
Y nadie tuvo que tocar el código
```

**Cómo validarlo:**
1. Buscar en `validadores/` una lista de marcadores escrita a mano. Resultado esperado: no hay.
2. Agregar un marcador a una plantilla en un árbol de prueba.
3. Comprobar un documento que lo tenga. Resultado esperado: se señala.
- **Aprobado cuando:** agregar un marcador a una plantilla no obliga a tocar un validador.

### CA-05 — El programa avisa y no corrige

```gherkin
Dado un documento que sigue siendo el molde
Cuando se corre la comprobación
Entonces el documento queda exactamente como estaba
```

**Cómo validarlo:**
1. Anotar el contenido de un documento sin llenar.
2. Correr la comprobación.
3. Comparar. Resultado esperado: idéntico, byte por byte.
- **Aprobado cuando:** la comprobación no escribe en ningún documento.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | Leer las plantillas se hace **una vez**, no una por documento |
| RNF-02 | **Claridad** | El aviso dice qué marcador quedó, no solo que hay marcadores |

---

## 6. Diseño y referencias

- **Dónde se cuenta:** `inventario` y `por_veredicto` en `validadores/fases.py`.
- **De dónde salen los marcadores del molde:** las plantillas de [`plantillas/ciclo-vida-proyectos/`](../../../../plantillas/ciclo-vida-proyectos/).
- **La medida que no sirve y la que sí:** los dos guiones en [historico-chat/scripts/2026-08-27/](../../../../historico-chat/scripts/2026-08-27/), guardados los dos.

---

## 7. Tareas técnicas derivadas

- [ ] «Backend» Leer los marcadores de cada plantilla, una sola vez.
- [ ] «Backend» Decir si un documento conserva tres o más de los suyos.
- [ ] «Backend» Que una fase con un documento así no cuente terminada.
- [ ] «Backend» Un aviso por documento, con la fase y el archivo.
- [ ] «Pruebas» Los cinco criterios, y el caso de la prosa con comillas.
- [ ] «Documentación» Entrada en el `CHANGELOG` y subir `VERSION`.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| Por abrir | CA-01 a CA-05 | (vacío) | | | | Propuesta |

**La línea base, medida antes de abrir ninguna carpeta:** `117 en total · 32 sin terminar · 85 terminadas, de las cuales 64 cumplen, 16 no cumplen y 5 no dicen si cumplen`. **Se anota acá porque abrir la fase la mueve**, y eso ya confundió una medición.

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Que la comprobación señale documentos escritos | **Ya pasó** con el umbral por cantidad. `CA-02` lo cubre con el caso de la prosa |
| Riesgo | Que las «sin terminar» suban y se lea como retroceso | No es retroceso: son siete documentos que nunca se escribieron. La entrada del `CHANGELOG` lo dirá |
| Riesgo | Que abrir la fase mueva la medición | Está medida antes, y anotada en el §8 |
| Dependencia | Las plantillas tienen que conservar sus marcadores | `CA-04`: se leen de ellas, así que un cambio se refleja solo |

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

- [ ] Código implementado y revisado
- [ ] Pruebas unitarias escritas y en verde
- [ ] Criterios de aceptación validados
- [ ] Requisitos no funcionales validados
- [ ] Documentación técnica y de usuario actualizada
- [ ] Desplegada en ambiente de pruebas — no aplica
- [ ] Aceptada por el Product Owner

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | ☑ | No depende de nada abierto |
| **N**egociable | ☑ | El umbral de tres se puede discutir sin tocar el objetivo |
| **V**aliosa | ☑ | Es la última de las cuatro formas en que el número mintió, y la única que sigue viva |
| **E**stimable | ☑ | Una función, un aviso y sus pruebas |
| **S**mall (pequeña) | ☑ | Una sola fase |
| **T**esteable | ☑ | Los cinco criterios se comprueban con árboles de prueba y contra el árbol real |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-27 | Agente, con el usuario | Creación de la HU. Sale del [pendiente 88](../../../../pendientes/hecho/el-molde-sin-llenar-no-cuenta-como-escrito.md), con las salidas 1 y 3 aprobadas y la 2 dejada fuera por el usuario |
