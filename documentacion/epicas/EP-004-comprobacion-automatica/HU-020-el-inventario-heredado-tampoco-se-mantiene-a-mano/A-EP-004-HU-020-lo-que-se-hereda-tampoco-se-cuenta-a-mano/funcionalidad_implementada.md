# Funcionalidad implementada — Fase `A-EP-004-HU-020-lo-que-se-hereda-tampoco-se-cuenta-a-mano` (módulo Programas de comprobación)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-004-HU-020-lo-que-se-hereda-tampoco-se-cuenta-a-mano` |
| **Módulo** | Programas de comprobación |
| **Especificación del módulo** | No hay documento aparte. La historia hace de especificación, declarado en el [plan_trabajo.md](plan_trabajo.md) §0. **Cuarta fase que lo declara** |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-26 |
| **HU / CA cubiertas** | [HU-020](../HU-020-el-inventario-heredado-tampoco-se-mantiene-a-mano.md): `CA-01`, `CA-02`, `CA-03`, `CA-04` y su transversal. Los cuatro |
| **Fecha de cierre** | 2026-08-26 |
| **Versión del estándar al cerrar** | `34.2.0` — el número, no un puntero. Por qué importa, en §5 |
| **Commit** | Por anotar al guardar |

---

## 1. Qué se implementó — resumen

**Lo que el estándar arregló para sí mismo llegó a quien lo hereda.** La fase anterior le quitó al inventario del estándar la cuenta escrita a mano. Quedaban dos mitades sin cubrir, y las dos se cerraron acá.

**La plantilla dejó de enseñar el defecto.** Ya no pide llenar tres campos ni mantener una tabla de una fila por historia: remite al comando que las calcula, con su `--raiz` para correrlo desde un proyecto.

**Y la comprobación dejó de mirar una sola ruta.** Busca el inventario en el primer nivel de `pendientes/` y de `documentacion/`, que es donde el estándar dice que vive, y lo reconoce **por su forma, no por su nombre**.

**El estándar subió a la versión `34.2.0`**, porque cambiar una plantilla lo exige (`20·M10`).

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem de la historia | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| `RN-01` la plantilla no trae campos de cuenta | documento | [plantillas/inventario-hu.md](../../../../../plantillas/inventario-hu.md) | ✅ | CP-003 |
| `RN-02` tampoco la tabla ni los pasos para llenarla | documento | La misma | ✅ | CP-003 |
| `RN-03` dice el comando, con su `--raiz` | documento | La misma, sección «Cómo se pregunta cuánto falta» | ✅ | CP-004 |
| `RN-04` la comprobación busca donde el proyecto lo tenga | servicio | `CARPETAS_DEL_INVENTARIO` y `_donde_puede_estar_el_inventario` en [validadores/fases.py](../../../../../validadores/fases.py) | ✅ | CP-001, CP-002 |
| `RN-05` lo no derivable se conserva | documento | La plantilla, secciones de proceso | ✅ | CP-003 |
| `RN-06` versionar | documento | [VERSION](../../../../../VERSION) y [CHANGELOG.md](../../../../../CHANGELOG.md) | ✅ | CP-007 |
| `RNF-01` no recorre el proyecto entero | servicio | El primer nivel de dos carpetas | ✅ | CP-005: **2 carpetas contra 541** |
| `RNF-02` un inventario en `pendientes/` sigue igual | servicio | La misma función | ✅ | CP-006 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Evidencia |
|---|---|---|---|
| T-01 | Declarar en qué carpetas se busca, con su porqué | ✅ hecha | El comentario de `CARPETAS_DEL_INVENTARIO` |
| T-02 | Que la comprobación busque ahí | ✅ hecha | CP-001 |
| T-03 | Que el aviso nombre la ruta real | ✅ hecha | CP-001 paso 4 |
| T-04 | Casos para el inventario fuera de `pendientes/` | ✅ hecha | 5 pruebas nuevas |
| T-05 | Que las de la `HU-019` sigan pasando sin tocarlas | ✅ hecha, **con una salvedad** | §4.4 del resultado |
| T-06 | Listar las secciones antes de tocar | ✅ hecha | CP-003 |
| T-07 | Quitar los tres campos | ✅ hecha | CP-003 |
| T-08 | Quitar la tabla y los seis pasos | ✅ hecha | CP-003 |
| T-09 | Escribir el comando, verificado corriéndolo | ✅ hecha | CP-004, y `DEF-02` |
| T-10 | Reescribir la guía sin la tabla | ✅ hecha | CP-003 |
| T-11 | Listar las secciones otra vez | ✅ hecha | CP-003 |
| T-12 | Subir `VERSION` | ✅ hecha | CP-007 |
| T-13 | Escribir la entrada del `CHANGELOG` | ✅ hecha | CP-007 |
| T-14 | Correr `validar.py versionado` | ✅ hecha | CP-007 |
| T-15 | Medir el recorrido | ✅ hecha | CP-005 |
| T-16 | Sabotear | ✅ hecha | Siete sabotajes |

**Correspondencia con el plan:** 16 tareas en el plan, 16 acá. **Ninguna sin hacer.**

**La salvedad de T-05.** La meta era tocar **cero** pruebas de la fase anterior y fue **una**, por un `ResourceWarning`: abría un archivo sin cerrarlo. Se envolvió en `with`; lo que comprueba y su veredicto son los mismos.

**Archivos tocados que el plan no declaraba** (`02·F8`): **uno, con el plan ampliado y autorizado.** El cierre de la fase anterior quedó afirmando algo falso por culpa de esta fase; se paró, se reportó al usuario, y con su permiso se corrigió. **El orden importa**: no se editó primero para pedir perdón después. Ver §6.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Qué | Resultado |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | Cumple, en el ciclo 2 |
| **Suites ejecutadas** | `python validadores/pruebas.py`: **381 de 381 verdes** |
| **Defectos** | Los tres corregidos. `DEF-03` estaba fuera de lo declarado: se paró, se reportó, y se corrigió con el plan ampliado |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

**Desde un proyecto**, para saber cuánto falta:

```
python "<ruta-al-estandar>/validadores/validar.py" fases --raiz .
```

**Las comillas no sobran:** la ruta al estándar puede tener espacios, y sin ellas la terminal parte la orden. Se descubrió corriéndolo.

- **Desde el código:** `fases.cuenta_escrita_a_mano(proyecto)`, que sale sola por `validar`.
- **Dónde busca:** el primer nivel de `pendientes/` y de `documentacion/`, declarado en `CARPETAS_DEL_INVENTARIO`.

---

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal |
|---|---|---|
| El inventario se reconoce por su **forma**, no por su nombre | El nombre lo elige cada proyecto; la plantilla no lo fija. Lo constante es el defecto | `test_el_nombre_del_archivo_no_decide_nada` |
| Solo el **primer nivel** de dos carpetas | Un proyecto de mil documentos pagaría el recorrido en cada corrida para vigilar un archivo. Medido: 2 carpetas contra 541 | `CP-005` |
| Hay una prueba que **fija el alcance** | Si se amplía sin querer, lo dice; si hay que ampliarlo, hay que cambiarla, y eso obliga a decidirlo en vez de que ocurra solo | `test_fuera_de_las_carpetas_declaradas_no_se_busca` |
| **Dos comprobaciones con dos formas**, no una más laxa | En un inventario real el defecto es un número; en una plantilla, el hueco `«N»`. Aflojar la primera volvería el aviso ruido, porque la narrativa tiene cifras | `S-046` |
| El comando va **entre comillas** en la plantilla | La ruta al estándar puede tener espacios | `DEF-02` |
| La versión al cerrar se escribe con su **número**, no apuntando a `VERSION` | Es una **foto**, no una cuenta. Un puntero la falsifica el día que la fuente cambia — que fue hoy | `S-047` |
| **MENOR** | Ningún proyecto al día queda obligado a nada: lo que aparece es un aviso, y los avisos no detienen | La entrada del `CHANGELOG` |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino |
|---|---|---|
| ~~El cierre de la fase anterior dice «la versión que declara `VERSION`» en vez de su número~~ **Corregido** | No previsto. Lo destapó subir la versión en esta fase | Se paró, se reportó y **el usuario autorizó ampliar el plan** con ese archivo, que es lo que `02·F8` pide. El cierre dice ahora `34.1.0`, con la nota de por qué cambió. `S-047` |
| Los inventarios ya escritos en proyectos existentes | Fuera de alcance declarado | Se avisan; arreglarlos es decisión de cada proyecto, y así lo dice el `CHANGELOG` |
| Otras plantillas podrían enseñar a mantener a mano algo derivable | No previsto | Sale de un barrido aparte, si el usuario lo quiere |
| **Cuatro fases seguidas declararon no llevar especificación aparte** | Acumulado | Ya no es un caso suelto: es la regla que falta. La [EP-001 · HU-010](../../../EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/HU-010-cuando-no-aplica-la-especificacion.md) lleva abierta esperando escribirla |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] La épica [EP-004](../../epica.md): la `HU-020` en su tabla de historias y en la de fases.
- [x] El [README](../README.md) de la carpeta de la historia.
- [x] Las señales `S-045`, `S-046` y `S-047`.
- [x] `VERSION` y `CHANGELOG.md`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

- **Migraciones a correr:** ninguna.
- **Qué cambia para quien ya tenía el estándar:** un aviso nuevo si su inventario guarda la cuenta, y la plantilla sin tabla la próxima vez que arme uno. **Su inventario no se toca ni se migra.**
- **Reversión:** se descarta el commit. **Con una salvedad:** si la versión ya se publicó, bajar `VERSION` no deshace que un proyecto la haya visto. La reversión sería una versión nueva que restituye, no un borrado.
