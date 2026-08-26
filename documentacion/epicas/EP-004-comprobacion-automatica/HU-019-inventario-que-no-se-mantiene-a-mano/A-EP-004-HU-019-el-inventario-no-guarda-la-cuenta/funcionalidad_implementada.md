# Funcionalidad implementada — Fase `A-EP-004-HU-019-el-inventario-no-guarda-la-cuenta` (módulo Programas de comprobación)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-004-HU-019-el-inventario-no-guarda-la-cuenta` |
| **Módulo** | Programas de comprobación |
| **Especificación del módulo** | No hay documento aparte. La historia hace de especificación, y se declaró en el [plan_trabajo.md](plan_trabajo.md) §0 con su porqué |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-26 |
| **HU / CA cubiertas** | [HU-019](../HU-019-inventario-que-no-se-mantiene-a-mano.md): `CA-01`, `CA-02`, `CA-03` y su transversal. Los tres |
| **Fecha de cierre** | 2026-08-26 |
| **Versión del estándar al cerrar** | La que declara [VERSION](../../../../../VERSION) |
| **Commit** | `ce2246b` |

---

## 1. Qué se implementó — resumen

**El inventario de historias dejó de guardar una cuenta que el árbol ya sabe.** El pendiente [48](../../../../../pendientes/48-inventario-hu.md) tenía tres números y una tabla de 74 filas, mantenidos a mano. Ahora remite al comando que los calcula.

**Y quedó una comprobación para que la copia no vuelva.** `validar.py fases` avisa si el pendiente guarda alguno de los tres campos. **Avisa, no falla, y no corrige**: el programa reporta (`EP-004 §10.2`).

**Lo que solo el pendiente sabía se conservó entero:** los 11 párrafos que explican por qué cambió cada número, idénticos letra por letra, y la condición de cierre.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem de la historia | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| `RN-01` el pendiente no guarda los tres números | documento | [pendientes/48-inventario-hu.md](../../../../../pendientes/48-inventario-hu.md), encabezado | ✅ | CP-001 |
| `RN-02` tampoco la tabla de una fila por historia | documento | El mismo, sección «Qué le falta a cada HU» | ✅ | CP-001 |
| `RN-03` la narrativa se conserva íntegra | documento | El mismo, los 11 párrafos | ✅ | CP-004 |
| `RN-04` ningún programa escribe el pendiente | servicio | `cuenta_escrita_a_mano` en [validadores/fases.py](../../../../../validadores/fases.py) | ✅ | CP-003 |
| `RN-05` queda una comprobación que impida que vuelva | servicio | La misma, colgada de `validar` | ✅ | CP-002, y el sabotaje 4 |
| `RNF-01` dice de dónde sale la cuenta | documento | El encabezado, con el comando copiable | ✅ | CP-001 |
| `RNF-02` no agrega un recorrido nuevo | servicio | La función hace un `isfile` y una lectura | ✅ | T-10 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-01 | Comparar las 74 filas contra el árbol | ✅ hecha | Su resultado, en §2.3 | CP-004 paso 5 |
| T-02 | Quitar los tres campos con su número | ✅ hecha | El encabezado del pendiente | CP-001 |
| T-03 | Escribir el comando que da la cuenta | ✅ hecha | El mismo encabezado | CP-001 |
| T-04 | Comprobar que el pendiente no traiga la cuenta | ✅ hecha | `cuenta_escrita_a_mano` | CP-002 |
| T-05 | Redactar el aviso | ✅ hecha | La misma función | CP-002 paso 4 |
| T-06 | Reemplazar la prueba que comparaba las dos copias | ✅ hecha | `InventarioDeHU`, en `pruebas.py` | La suite |
| T-07 | Contar los párrafos antes y después | ✅ hecha | 11 y 11 | CP-004 |
| T-08 | Quitar la tabla | ✅ hecha | El pendiente, 148 líneas a 83 | CP-004 |
| T-09 | Comprobar que la condición de cierre sigue | ✅ hecha | La sección «Cómo se sabe que cerró» | CP-004 |
| T-10 | Verificar que no hay recorrido nuevo | ✅ hecha | Leyendo la función | §2.1 |
| T-11 | Sabotear y ver si las pruebas cazan | ✅ hecha | Seis sabotajes | §4.1 del resultado |

**Correspondencia con el plan:** 11 tareas en el plan, 11 acá.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno. **Y uno que el plan no declaraba se dejó sin tocar a propósito**: la plantilla `inventario-hu.md`, que sigue describiendo la tabla. Se reporta en §6 en vez de editarla por iniciativa.

**Esfuerzo real contra estimado:** el plan estimó 10 h. El trabajo salió más rápido, y lo que costó fue el ciclo 2 de sabotajes, que no estaba previsto porque los sabotajes se planearon como verificación y resultaron ser los que encontraron los dos defectos.

### 2.3 Lo que dijo T-01, que era la única duda abierta

La tabla se podía quitar sin perder nada, y se comprobó antes de quitarla:

| Qué se buscó | Resultado |
|---|---|
| Filas que nombran una historia que no está en el árbol | **Ninguna** |
| Filas cuyo enlace no resuelve | **Ninguno** |
| Historias del árbol que la tabla no nombraba | **39** |
| Filas con alguna casilla equivocada | **26 de 74** |
| Filas que daban por **completa** una historia que no lo estaba | **4** |

Y las seis columnas eran «tiene fase» más los cinco documentos: **todo derivable del árbol**. Nada era propio del pendiente.

**Las 4 filas optimistas son el dato que más pesa.** Un inventario atrasado se nota; uno que dice «hecho» donde no lo está **esconde trabajo**, y esa es la dirección que hace daño.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Qué | Resultado |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | Cumple, en el ciclo 2 |
| **Suites ejecutadas** | `python validadores/pruebas.py`: **373 de 373 verdes** |
| **Defectos abiertos que se aceptaron** | Ninguno. `DEF-01` y `DEF-02` corregidos y verificados |

**Verificaciones manuales** (`08·T4`):

| # | Qué se verificó | Resultado |
|---|---|---|
| 1 | Que las pruebas cacen lo que dicen cazar | Seis sabotajes; **dos pasaron en verde en el ciclo 1** |
| 2 | Que los dos verdes no fueran lo mismo | No lo eran: uno no saboteaba, el otro sí y la prueba era floja |
| 3 | Que la narrativa no se perdiera | 11 párrafos, idénticos letra por letra |
| 4 | Que el programa no toque el archivo | Comparado en bytes |
| 5 | Que nada más se moviera | 54 avisos antes y 54 después |
| 6 | Que las pruebas no dejaran rastros | Todo en carpeta temporal |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Para saber cuánto falta, desde la raíz del repositorio:

```
python validadores/validar.py fases
```

Lista cada historia sin fase y cada fase a la que le falta un documento, y termina con la cuenta.

- **Desde el código:** `fases.inventario(proyecto)` da la terna, y `fases.linea_inventario(proyecto)` la línea escrita.
- **La comprobación nueva:** `fases.cuenta_escrita_a_mano(proyecto)`, que sale sola por `validar`.

---

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal |
|---|---|---|
| Quitar la copia en vez de generarla | Un generador dejaría dos copias con alguien teniendo que acordarse de correrlo: el mismo fallo, más lento. `EP-004 §10.2` lo permitiría, y aun así no | El comentario junto a `cuenta_escrita_a_mano` |
| Avisa, no falla | Un pendiente con un número de más no rompe nada, y detener el commit por eso es como se terminan desactivando los enganches | El docstring de la función |
| Se busca el campo con su rótulo, no cualquier cifra | La narrativa tiene números —«68 a 74»— y marcarlos volvería el aviso ruido, que es como se aprende a ignorarlo | `CP-005`, que existe solo para eso |
| La comprobación vive en `fases.py` y no en un validador nuevo | La cuenta la calcula `fases`; un archivo aparte recorrería el árbol otra vez para decir lo mismo | `RNF-02` |
| Una prueba que busca el aviso **por `validar`**, no por la función | Es la única que dice que alguien la llama. Sin ella, descolgarla dejaba las otras seis en verde | `S-043` |
| El guion de sabotaje se cae si la suite corre cero pruebas | `Ran 0 tests` sale con el mismo `OK` que una corrida buena | `S-044` |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino |
|---|---|---|
| La plantilla [`inventario-hu.md`](../../../../../plantillas/inventario-hu.md) sigue describiendo la tabla que acá se quitó | No previsto. Apareció al reescribir el pendiente | **Un proyecto que herede el estándar arma su inventario a mano, con el defecto que este repositorio acaba de dejar atrás.** No se tocó porque el plan no la declara (`02·F8`), y cambiar `plantillas/` suma entrada en el `CHANGELOG` y sube `VERSION` (`20·M10`). Se decide con el usuario |
| Las 43 historias incompletas siguen incompletas | Fuera de alcance declarado | Es trabajo, no marcas. El pendiente 48 sigue abierto hasta que lleguen a cero |
| Otros pendientes podrían guardar números a mano | Fuera de alcance declarado | Si los hay, salen de un barrido aparte |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] La épica [EP-004](../../epica.md): la `HU-019` entró en su tabla de historias y en la de fases.
- [x] El [README](../README.md) de la carpeta de la historia.
- [x] Las señales `S-043` y `S-044`, en [documentacion/senales.md](../../../../senales.md).
- [x] Catálogo de módulos: sin cambios. `fases.py` ya estaba registrado.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

- **Migraciones a correr:** ninguna. No hay base de datos.
- **Qué cambia para quien ya tenía el repositorio:** al correr `validar.py fases` verá un aviso nuevo si su inventario guarda la cuenta, y el pendiente 48 ya sin la tabla.
- **Reversión:** se descarta el commit de la fase. La tabla que se quitó sigue en el historial.
