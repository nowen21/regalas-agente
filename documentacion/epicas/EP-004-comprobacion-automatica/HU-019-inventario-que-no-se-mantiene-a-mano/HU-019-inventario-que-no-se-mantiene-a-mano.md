# HU-019 — Que el inventario de historias deje de mantenerse a mano

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-019 |
| **Épica / Feature** | [EP-004 Comprobación automática de lo que no admite discusión](../epica.md) |
| **Módulo / Componente** | Programas de comprobación |
| **Tipo** | Técnica |
| **Prioridad** | Should |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Terminada. Los tres criterios y su transversal, verificados el 2026-08-26 |
---

## 2. Narrativa

- **Como** quien mantiene el estándar
- **Quiero** que el inventario de historias no tenga números propios que alguien deba corregir
- **Para** que la respuesta a «cuánto falta» no pueda quedar vieja sin que nadie se entere

---

## 3. Contexto y descripción

**El número ya se calcula solo.** Desde la [HU-017](../HU-017-inventario-de-hu-sin-fase/HU-017-inventario-de-hu-sin-fase.md), `validar.py fases` termina diciendo `HU: 112 en total · 69 completas · 43 incompletas`. Sale del árbol, así que no puede mentir.

**Y aparte hay una segunda copia, escrita a mano.** El pendiente [48](../../../../pendientes/48-inventario-hu.md) guarda esos mismos tres números en su encabezado, más una tabla con una fila por historia y seis casillas por fila. Eso lo mantiene una persona.

**Las dos copias se separaron tres veces.** El 2026-08-17 la cifra escrita llevaba dos de retraso. El 2026-08-26 dice 78 historias donde el árbol tiene 112: las cuatro épicas de la plataforma quedaron enteras por fuera. Entre una y otra hubo diecinueve cambios en las épicas y ninguna vuelta al pendiente.

**No es descuido, y por eso corregirlo no lo arregla.** Escribir hoy las 112 filas correctas solo mueve la fecha del próximo desfase: el pendiente 48 existe **precisamente** porque una cuenta a mano se desactualiza el día que alguien cierra algo y no vuelve ahí.

**La salida no es que un programa la escriba.** `EP-004 §10.2` y [`DA-06`](../../../../cvds/diseno/decisiones-de-arquitectura.md) dicen que los programas de comprobación reportan y no corrigen. La salida es **que no haya segunda copia**: el pendiente enlaza lo que el árbol ya sabe, en vez de repetirlo. Es lo mismo que se decidió en `S-040` para el registro de auditoría, y por la misma razón: dos copias de un dato se separan con el tiempo.

**Lo que sí se conserva.** El pendiente lleva una narrativa de **por qué** cambió cada número: «68 a 74: seis historias nuevas al enrutar el backlog, que no son trabajo nuevo sino trabajo que ya existía y no tenía a quién rendirle cuentas». Eso no está en el árbol y no se recupera contando. Se queda.

### 3.1 Reglas de negocio

| ID | Regla | De dónde baja |
|---|---|---|
| RN-01 | El pendiente del inventario no guarda el total, las completas ni las incompletas. Remite al comando que los calcula | Hallazgo H-27 del 2026-08-26 |
| RN-02 | Tampoco guarda la tabla de una fila por historia: `validar.py fases` ya dice qué le falta a cada una | `S-040`: quien resume algo con detalle enlaza el detalle |
| RN-03 | La narrativa de por qué cambiaron los números se conserva íntegra | No es derivable del árbol; contarla otra vez no la recupera |
| RN-04 | Ningún programa de comprobación escribe el pendiente | `EP-004 §10.2` y `DA-06` |
| RN-05 | Queda una comprobación que impida que la segunda copia vuelva | Sin ella, el próximo que edite el pendiente puede reponer los números sin saber por qué no van |

### 3.2 Supuestos

- `validar.py fases` seguirá terminando con la línea del inventario, que es lo que la [HU-017](../HU-017-inventario-de-hu-sin-fase/HU-017-inventario-de-hu-sin-fase.md) dejó construido.
- El pendiente 48 sigue siendo el sitio donde se responde «cuánto falta».

### 3.3 Fuera de alcance

- **Cambiar cómo se cuenta.** Qué es una historia completa lo define la `HU-017` y no se toca.
- **Corregir las 34 filas que faltan.** No se corrigen: se quitan, junto con las otras 78.
- **Marcar la estación del commit**, que es el pendiente [87](../../../../pendientes/87-la-estacion-del-commit-casi-nunca-se-marca.md) y otro problema.
- **Que un programa escriba el pendiente.** Está prohibido por `RN-04`, y por eso ni siquiera es una alternativa diferida.
- **Los demás pendientes con números a mano.** Si los hay, salen de un barrido aparte.

---

## 4. Criterios de aceptación

### CA-01 — El pendiente responde «cuánto falta» sin guardar la respuesta

```gherkin
Dado que el árbol tiene 112 historias, 69 completas y 43 incompletas
Cuando alguien abre el pendiente del inventario para saber cuánto falta
Entonces encuentra el comando que lo calcula, y no un número escrito
Y ese comando, al correrse, responde con la cuenta del árbol de ese momento
```

**Cómo validarlo:**
1. Abrir [pendientes/48-inventario-hu.md](../../../../pendientes/48-inventario-hu.md) en cualquier editor de texto.
2. Buscar en todo el archivo las palabras «Total de HU», «Completas» e «Incompletas» como campos con un número al lado. Resultado esperado: no aparecen.
3. Leer el encabezado. Resultado esperado: dice con qué comando se obtiene la cuenta, escrito de forma que se pueda copiar y pegar.
4. Correr ese comando en una terminal, desde la raíz del repositorio. Resultado esperado: termina con una línea que dice cuántas historias hay en total, cuántas completas y cuántas incompletas.
- **Aprobado cuando:** el pendiente no contiene ninguno de los tres números, y el comando que nombra devuelve los tres al correrse.

### CA-02 — Reponer un número a mano no pasa desapercibido

```gherkin
Dado que el pendiente ya no guarda la cuenta
Cuando alguien vuelve a escribir un total fijo en su encabezado
Entonces la comprobación lo reporta, diciendo qué campo sobra y por qué
Y el pendiente queda igual: la comprobación no lo corrige
```

**Cómo validarlo:**
1. Hacer una copia de trabajo del pendiente y agregarle al encabezado una fila con un total escrito a mano, por ejemplo `| **Total de HU** | 99 |`.
2. Correr la comprobación de fases sobre el repositorio. Resultado esperado: reporta esa fila, nombrando el archivo, y explica que la cuenta sale del árbol.
3. Volver a abrir el pendiente. Resultado esperado: la fila que se agregó sigue ahí, sin cambios. El programa reportó y no corrigió (`RN-04`).
4. Quitar la fila y correr otra vez. Resultado esperado: no reporta nada sobre ese archivo.
- **Aprobado cuando:** el reporte aparece con la fila puesta, desaparece al quitarla, y en ningún caso el archivo cambió solo.

### CA-03 — La narrativa de por qué cambiaron los números sobrevive

```gherkin
Dado que el pendiente explicaba que «68 a 74» fueron seis historias nuevas al
  enrutar el backlog, y no trabajo nuevo
Cuando se le quitan los números y la tabla
Entonces esa explicación sigue estando, completa y legible
Y sigue estando la condición de cierre: que las incompletas lleguen a cero
```

**Cómo validarlo:**
1. Antes de cambiar nada, guardar aparte una copia del pendiente y contar cuántos párrafos de explicación histórica tiene, fechados.
2. Aplicar el cambio.
3. Abrir el pendiente y contar otra vez esos párrafos. Resultado esperado: está el mismo número, con las mismas fechas y el mismo texto.
4. Buscar la condición de cierre. Resultado esperado: sigue diciendo que el pendiente cierra cuando no quede ninguna historia incompleta.
- **Aprobado cuando:** ningún párrafo fechado se perdió, y la condición de cierre sigue escrita.

### Criterios de aceptación transversales

- [x] **No regresión** — lo existente sigue funcionando; la suite relacionada queda verde (`08`, `02·F5`). En particular, la prueba que hoy compara las dos copias deja de tener objeto y **se reemplaza**, no se borra: pasa a comprobar `CA-02`.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Trazabilidad** | El pendiente dice de dónde sale la cuenta, para que quien lo lea pueda obtenerla sin preguntar |
| RNF-02 | **Rendimiento** | La comprobación de `CA-02` no agrega un recorrido nuevo: se apoya en el que ya hace `fases` (`EP-004 §10.2`) |

---

## 6. Diseño y referencias

- **Documento funcional:** el pendiente [48](../../../../pendientes/48-inventario-hu.md), que es lo que se cambia.
- **De dónde sale la cuenta:** `inventario` y `linea_inventario` en `validadores/fases.py`, construidos por la [HU-017](../HU-017-inventario-de-hu-sin-fase/HU-017-inventario-de-hu-sin-fase.md).
- **La prueba que cambia de objeto:** `InventarioDeHU.test_la_cuenta_del_programa_coincide_con_la_del_inventario_escrito`, en `validadores/pruebas.py`.
- **Modelo de datos afectado:** ninguno. No hay base de datos en los programas de comprobación.

---

## 7. Tareas técnicas derivadas

- [ ] «Documentación» Reescribir el encabezado del pendiente 48 para que remita al comando en vez de guardar la cuenta.
- [ ] «Documentación» Quitar la tabla de una fila por historia, conservando la narrativa fechada.
- [ ] «Backend» Comprobar en `fases.py` que el pendiente no traiga la cuenta escrita, y reportarlo sin corregir.
- [ ] «Pruebas» Reemplazar la prueba que compara las dos copias por la que comprueba `CA-02`.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| [`A-EP-004-HU-019-el-inventario-no-guarda-la-cuenta`](A-EP-004-HU-019-el-inventario-no-guarda-la-cuenta/) | CA-01, CA-02, CA-03 | (vacío) | [plan_trabajo](A-EP-004-HU-019-el-inventario-no-guarda-la-cuenta/plan_trabajo.md) | [plan_pruebas](A-EP-004-HU-019-el-inventario-no-guarda-la-cuenta/plan_pruebas.md) | [resultado](A-EP-004-HU-019-el-inventario-no-guarda-la-cuenta/resultado_pruebas.md) · cumple | Cerrada |

Los tres criterios van juntos en una fase porque **no se pueden comprobar por separado**: quitar la cuenta sin dejar la comprobación deja el pendiente listo para que alguien la reponga, y dejar la comprobación sin quitar la cuenta la haría fallar contra el propio archivo.

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | La [HU-017](../HU-017-inventario-de-hu-sin-fase/HU-017-inventario-de-hu-sin-fase.md), que es la que calcula la cuenta. Ya está cumplida | Bajo |
| Riesgo | Que quitar la tabla se lleve por delante trabajo anotado ahí y en ninguna otra parte | Antes de quitarla se compara fila por fila contra el árbol, y lo que solo esté en la tabla se conserva |
| Riesgo | Que la comprobación de `CA-02` reporte pendientes que legítimamente traen números de otra cosa | Se limita al pendiente del inventario y a los campos de la cuenta, no a cualquier número |

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
- [x] Pruebas unitarias e integración pasando — 373 de 373
- [ ] Code review aprobado — lo hace el usuario al aprobar la fase
- [x] Todos los criterios de aceptación verificados
- [x] Requisitos no funcionales validados
- [x] Documentación técnica y de usuario actualizada
- [ ] Desplegada en ambiente de pruebas — no aplica: son programas que se corren a mano
- [ ] Aceptada por el Product Owner

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | ☑ | Solo depende de la HU-017, que ya está cumplida |
| **N**egociable | ☑ | Qué se conserva del pendiente y qué se quita se puede discutir sin tocar el objetivo |
| **V**aliosa | ☑ | Hoy el único número que dice cuánto falta va 34 atrás |
| **E**stimable | ☑ | Un archivo de texto, una comprobación y una prueba |
| **S**mall (pequeña) | ☑ | Una sola fase |
| **T**esteable | ☑ | Los tres criterios se comprueban leyendo el archivo y corriendo un comando |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-26 | Agente, con el usuario | Creación de la HU. Sale del hallazgo H-27 y del pendiente 48 |
| 2026-08-26 | Agente | Cerrada la fase `A`. Los tres criterios cumplidos; dos defectos encontrados por los sabotajes y corregidos (`S-043`, `S-044`) |
