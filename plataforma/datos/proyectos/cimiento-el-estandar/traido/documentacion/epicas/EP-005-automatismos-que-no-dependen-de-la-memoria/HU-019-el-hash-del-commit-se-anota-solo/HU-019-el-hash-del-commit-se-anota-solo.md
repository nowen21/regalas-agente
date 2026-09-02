# HU-019 — Que el hash del commit se anote solo, y que se sepa a cuántas fases alcanza

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-019 |
| **Épica / Feature** | [EP-005 Automatismos que no dependen de la memoria](../epica.md) |
| **Módulo / Componente** | Enganches |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | En curso |

---

## 2. Narrativa

- **Como** quien pregunta cuánto trabajo queda colgando
- **Quiero** que la casilla del commit se marque sola al hacer el commit
- **Para** que el número de fases abiertas diga las que de verdad lo están

---

## 3. Contexto y descripción

**La estación 12 del ciclo es «commit», y el commit ocurre después de que el agente termina de escribir.** En ese momento ya reportó, el usuario aprueba, se commitea — **y nadie vuelve al `estado-fase.md` a marcar la casilla**.

No es descuido: es la forma del ciclo. **La última estación es la única que se cumple fuera del momento en que se escribe el documento que la registra.**

**Solo el 2026-08-27 se marcó a mano cinco veces**, y cada una costó un commit aparte.

### Lo medido antes de diseñar, que cambia el alcance

> Sobre los 140 `estado-fase.md` del árbol, antes de crear la carpeta de esta historia.

| Qué | Cuántas |
|---|---|
| Estación 12 **marcada** | 11 |
| Estación 12 **sin marcar** | 23 |
| **Sin la fila de la estación 12** | **106** |

**Tres de cada cuatro fases no tienen dónde marcar.** Un programa que ponga el hash no tendría en qué escribirlo, y **actuaría solo sobre las que ya estaban bien**.

**Y de las 23 sin marcar, 22 son solo la marca:** su documento de cierre ya está en git, comprobado contra el historial. **Una sola es trabajo de verdad.** Contarlas juntas da 23 «fases sin commitear» donde hay una.

### 3.1 Reglas de negocio

| ID | Regla | De dónde baja |
|---|---|---|
| RN-01 | Al hacer un commit, la fase que ese commit cierra **recibe su hash sin que nadie lo escriba** | El pendiente 87 |
| RN-02 | Solo se escribe donde **hay dónde**: una fase sin la fila de la estación 12 no se toca | `S-066`: son 106 de 140 |
| RN-03 | Se escribe **solo si la casilla está vacía**. Un hash ya puesto no se pisa | Un automatismo que reescribe borra el rastro de qué commit fue |
| RN-04 | Una fase cuyo cierre **no está en git** no se marca | Marcarla dir��a que se commiteó algo que no se commiteó |
| RN-05 | El conteo distingue **«falta la marca»** de **«falta el trabajo»**, y los dice aparte | Son 22 y 1: juntarlos da 23 donde hay uno |
| RN-06 | Las fases **sin la fila** se cuentan aparte y se nombran | `04·R4`: no se puede afirmar sobre lo que no tiene campo |
| RN-07 | Si el enganche falla, **el commit no se pierde ni se deshace** | Un automatismo que rompe un commit se desinstala el mismo día |

### 3.2 Supuestos

- Git ofrece un enganche que corre **después** del commit, cuando el hash ya existe. Hoy el instalador escribe `commit-msg`, `pre-commit` y `pre-push`; **este haría falta agregarlo**.

### 3.3 Fuera de alcance

- **Rellenar las 106 fases sin la fila.** Se cuentan y se nombran; reescribir 106 documentos viejos es otro trabajo.
- **Marcar las 22 pendientes de hoy.** Esta historia hace que no vuelva a pasar; ponerlas al día se decide aparte, con el número a la vista.
- **Que la estación 12 deje de ser casilla.** Es la salida 2 del pendiente, y cambia el ciclo: decisión del usuario.

---

## 4. Criterios de aceptación

### CA-01 — El hash se escribe solo al commitear

```gherkin
Dado que un commit incluye el cierre de una fase
Y esa fase tiene su fila de estación 12 vacía
Cuando termina el commit
Entonces la casilla queda marcada con el hash de ese commit
```

**Cómo validarlo:**
1. En un repositorio de prueba, crear una fase con su fila de estación 12 vacía.
2. Commitear su documento de cierre.
3. Abrir el `estado-fase.md`. Resultado esperado: la casilla trae el hash del commit que se acaba de hacer.
- **Aprobado cuando:** nadie escribió el hash a mano.

### CA-02 — No se pisa un hash ya puesto

```gherkin
Dado que la casilla ya tiene un hash
Cuando se vuelve a commitear el mismo cierre
Entonces la casilla no cambia
```

**Cómo validarlo:**
1. Marcar la casilla con un hash cualquiera.
2. Commitear otra vez el cierre.
3. Comparar. Resultado esperado: **idéntico**.
- **Aprobado cuando:** el primer hash sobrevive.

**Por qué importa:** el hash dice **qué commit cerró la fase**. Reescribirlo con el último la haría apuntar a una corrección de una coma.

### CA-03 — Una fase sin la fila no se toca

```gherkin
Dado un `estado-fase.md` sin la fila de la estación 12
Cuando se commitea su cierre
Entonces el documento queda exactamente igual
```

**Cómo validarlo:**
1. Un `estado-fase.md` sin tabla de estaciones.
2. Commitear su cierre.
3. Comparar byte por byte. Resultado esperado: idéntico.
- **Aprobado cuando:** no se inventa una fila donde no hay tabla.

**Este es el criterio que decide si sirve.** Son **106 de 140**: un programa que les invente estructura haría más daño que el problema que corrige.

### CA-04 — El conteo separa «falta la marca» de «falta el trabajo»

```gherkin
Dado un árbol con fases sin marcar
Cuando se cuenta
Entonces se dice cuántas están cerradas de hecho
Y cuántas de verdad no se han commiteado
Y cuántas no tienen dónde marcar
```

**Cómo validarlo:**
1. Correr la comprobación sobre el árbol real.
2. Leer las tres cuentas. Resultado esperado: las tres, con nombres.
3. Sumarlas contra el total de fases. Resultado esperado: cuadran.
- **Aprobado cuando:** se puede ir a arreglar cada grupo sin volver a medir.

### CA-05 — Si el enganche falla, el commit no se pierde

```gherkin
Dado que el enganche revienta por cualquier motivo
Cuando se commitea
Entonces el commit queda hecho igual
```

**Cómo validarlo:**
1. Romper el enganche a propósito.
2. Commitear.
3. Comprobar `git log`. Resultado esperado: el commit está.
- **Aprobado cuando:** ningún fallo del enganche deshace ni bloquea un commit.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **No estorbar** | Corre en cada commit: no puede recorrer el árbol entero |
| RNF-02 | **Claridad** | Lo que escribe se entiende sin documentación: el hash, y nada más |

---

## 6. Diseño y referencias

- **Dónde vive la lógica:** `validadores/estacion_commit.py`, agnóstico de la herramienta.
- **Dónde se dispara:** un enganche de git que corre **después** del commit.
- **El molde de la tabla:** [`10-estado-fase.md`](../../../../plantillas/ciclo-vida-proyectos/10-estado-fase.md).
- **El precedente:** los tres enganches de git que el instalador ya escribe en `.githooks/`.

---

## 7. Tareas técnicas derivadas

- [ ] «Backend» Encontrar la fase que un commit cierra, por los archivos que toca.
- [ ] «Backend» Escribir el hash solo si hay fila y está vacía.
- [ ] «Backend» El enganche, que nunca deshace ni bloquea un commit.
- [ ] «Backend» El conteo con sus tres grupos, y sus nombres.
- [ ] «Documentación» Que el instalador lo escriba, como los otros tres.
- [ ] «Pruebas» Los cinco criterios, con el caso de las 106 sin fila.
- [ ] «Documentación» Entrada en el `CHANGELOG` y subir `VERSION`.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| Por abrir | CA-01 a CA-05 | (vacío) | | | | Propuesta |

**La línea base, medida antes de abrir la carpeta:** `120 en total · 32 sin terminar · 88 terminadas, de las cuales 69 cumplen, 14 no cumplen y 5 no dicen si cumplen`. Y sobre las estaciones: **11 marcadas, 23 sin marcar, 106 sin la fila**.

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Que el enganche escriba donde no hay estructura | `CA-03`, y son 106 de 140 |
| Riesgo | Que pise un hash ya puesto | `CA-02`. El hash dice qué commit cerró la fase |
| Riesgo | Que un fallo del enganche rompa un commit | `CA-05` y `RNF-02` |
| Riesgo | Que se lea como que el problema quedó resuelto para todas | El conteo del `CA-04` dice **sobre cuántas** actúa |
| Dependencia | Hace falta un enganche de git que hoy no se instala | Se agrega, como los otros tres |

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
| **I**ndependiente | ☑ | El canal de enganches de git ya existe |
| **N**egociable | ☑ | Qué se escribe exactamente se puede discutir sin tocar el objetivo |
| **V**aliosa | ☑ | Se marcó a mano cinco veces en un día, y cada vez costó un commit |
| **E**stimable | ☑ | Un enganche, una función, un conteo y sus pruebas |
| **S**mall (pequeña) | ☑ | Una sola fase |
| **T**esteable | ☑ | Los cinco criterios, con repositorios de prueba de verdad |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-27 | Agente, con el usuario | Creación de la HU. Baja del [pendiente 87](../../../../pendientes/hecho/el-hash-del-commit-se-anota-solo.md) con las salidas **1 y 3**; la **2** queda fuera. Al medir apareció que **106 de 140 fases no tienen dónde marcar** (`S-066`), y eso entró como `CA-03` y `CA-04` |
