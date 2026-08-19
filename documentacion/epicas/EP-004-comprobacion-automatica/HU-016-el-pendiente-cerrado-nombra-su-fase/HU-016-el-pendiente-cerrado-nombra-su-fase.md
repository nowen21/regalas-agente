# HU-016 — Comprobar que el pendiente cerrado nombra su fase

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-016 |
| **Épica / Feature** | [EP-004 Comprobación automática de lo que no admite discusión](../epica.md) |
| **Módulo / Componente** | Programas de comprobación |
| **Tipo** | Técnica |
| **Prioridad** | Should |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Backlog |

---

## 2. Narrativa

- **Como** quien mantiene el estándar
- **Quiero** que un programa avise cuando un pendiente no nombra la historia donde vive —al abrirlo— ni la fase donde se construyó —al cerrarlo—
- **Para** que nada del backlog quede suelto ni se construya saltándose la cadena, sin depender de que alguien se acuerde

> **El identificador de esta historia se quedó corto y no se cambia.** Nació diciendo «el pendiente cerrado», y desde el 2026-08-17 cubre también al abierto. Renombrar la carpeta rompería todo lo que la cita — que es exactamente el defecto del [pendientes/hecho/cerrar-un-pendiente-arrastra-sus-citas.md](../../../../pendientes/hecho/cerrar-un-pendiente-arrastra-sus-citas.md). El nombre queda; el alcance lo dicen las `RN` y los `CA`.

---

## 3. Contexto y descripción

El backlog dice qué falta. Durante meses se ejecutó leyéndolo como si fuera el plan: se editaba el código, se subía la versión y se marcaba hecho. Sin fase no hay plan de pruebas, y sin plan de pruebas nadie escribe qué había que comprobar.

El 2026-08-16 eso costó un defecto real. Se cerró un pendiente que cambiaba cómo las plantillas citan las reglas; la única prueba que importaba era instalar en un proyecto y hacer clic en el enlace, y no la corrió nadie. El defecto lo encontró el proyecto que lo sufrió, no el estándar que lo produjo.

De ahí nació [`02·F23`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), que exige bajar el pendiente a historia y construirlo como fase. Hoy la regla existe y **nada la comprueba**: es exactamente la situación que [`20·M9`](«RUTA-ESTANDAR»/base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md) describe — una regla validable que nadie valida es una regla que no se cumple.

Falta una pieza antes del programa: hoy el pendiente cerrado **no declara en un sitio fijo** cuál fue su fase. Unos lo cuentan en prosa, otros no lo dicen. Sin un sitio fijo no hay qué leer.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Un pendiente marcado hecho nombra la historia de usuario y la fase donde se construyó |
| RN-02 | La referencia se escribe en un campo fijo del pendiente, no en prosa libre |
| RN-03 | La fase nombrada tiene que existir en el árbol de épicas |
| RN-04 | El pendiente que solo pedía decidir algo o leer no abre fase, y lo declara en el mismo campo |
| RN-05 | Lo cerrado antes de que naciera la regla no se reabre; se reporta aparte y no hace fallar la corrida |
| RN-06 | **Todo pendiente nombra su historia de usuario desde que se abre**, no solo al cerrarse |
| RN-07 | La historia nombrada tiene que existir en el árbol de épicas |
| RN-08 | El pendiente que no es un ítem sino un tema lo declara en el mismo campo, y cada uno de sus puntos nombra la suya adentro |

**Por qué la exigencia se corrió hacia atrás.** La historia nació pidiendo el campo **al cerrar**, porque el defecto que la originó fue un cierre sin fase. Al enrutar el backlog el 2026-08-17 se vio que eso llega tarde: un pendiente que se abre sin historia se construye sin historia, y el campo del cierre se llena entonces con la fase que ya se hizo — que es documentar el salto, no impedirlo. El usuario lo dijo en una línea: *«todos los pendientes deben estar dentro de una HU, nada puede estar suelto»*.

Seis de los treinta abiertos no tenían historia que los recibiera, y hubo que crearla: [EP-001 · HU-011](../../EP-001-cuerpo-de-reglas-heredable/HU-011-buscar-antes-de-preguntar/HU-011-buscar-antes-de-preguntar.md), [EP-001 · HU-012](../../EP-001-cuerpo-de-reglas-heredable/HU-012-inventario-de-acciones-y-riesgo/HU-012-inventario-de-acciones-y-riesgo.md), [EP-001 · HU-013](../../EP-001-cuerpo-de-reglas-heredable/HU-013-capitulos-opt-in-de-dominio/HU-013-capitulos-opt-in-de-dominio.md), [EP-005 · HU-011](../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-011-donde-termina-el-estandar/HU-011-donde-termina-el-estandar.md), [EP-005 · HU-012](../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-012-hacer-cumplir-lo-que-solo-se-recuerda/HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md) y [EP-007 · HU-008](../../EP-007-instalacion-y-actualizacion/HU-008-el-proyecto-reporta-al-estandar/HU-008-el-proyecto-reporta-al-estandar.md). Ese es el número que mide el hueco: seis pendientes que se habrían construido sin nadie que dijera cuándo estaban aceptados.

### 3.2 Supuestos

- El backlog seguirá viviendo en archivos de texto, uno por ítem, con su índice.

### 3.3 Fuera de alcance

- Juzgar si lo que la fase construyó corresponde a lo que el pendiente pedía. Eso es criterio y lo lee una persona.
- Comprobar que la fase esté bien hecha. De eso ya se ocupan las comprobaciones de trazabilidad.

---

## 4. Criterios de aceptación

### CA-01 — Un pendiente cerrado sin fase se reporta

```gherkin
Dado que un pendiente está marcado como hecho
Cuando no nombra la historia de usuario ni la fase donde se construyó
Entonces la comprobación lo reporta con su archivo
Y la corrida termina con error
```

**Cómo validarlo:**

1. Marcar como hecho un pendiente de prueba, dejando vacío el campo de la fase.
2. Correr la comprobación de coherencia. Resultado esperado: reporta ese pendiente y nombra el campo que le falta.
3. Escribir la fase en el campo y volver a correr. Resultado esperado: no reporta nada.
- **Aprobado cuando:** el pendiente sin fase se reporta y el que la tiene no.

### CA-02 — Una fase que no existe se reporta

```gherkin
Dado que un pendiente cerrado nombra su fase
Cuando esa fase no existe en el árbol de épicas
Entonces la comprobación lo reporta y nombra el identificador que no resolvió
```

**Cómo validarlo:**

1. En un pendiente cerrado de prueba, escribir un identificador de fase inventado.
2. Correr la comprobación. Resultado esperado: reporta que la fase no existe, con el identificador escrito.
3. Cambiarlo por una fase que sí existe y volver a correr. Resultado esperado: no reporta nada.
- **Aprobado cuando:** la fase inventada se reporta y la real no.

### CA-03 — El pendiente que no era desarrollo no se reporta

```gherkin
Dado que un pendiente cerrado declara que solo pedía decidir algo
Cuando se corre la comprobación
Entonces no se reporta nada
```

**Cómo validarlo:**

1. Cerrar un pendiente de prueba escribiendo en el campo de la fase que no era desarrollo, con el motivo.
2. Correr la comprobación. Resultado esperado: no lo reporta.
3. Borrar el motivo dejando el campo vacío y volver a correr. Resultado esperado: lo reporta, porque un campo vacío no es una declaración.
- **Aprobado cuando:** la excepción declarada pasa y el campo vacío no.

### CA-04 — Lo cerrado antes de la regla se separa

```gherkin
Dado que hay pendientes cerrados antes de que naciera la regla
Cuando se corre la comprobación
Entonces se listan aparte como aviso
Y la corrida no falla por ellos
```

**Cómo validarlo:**

1. Correr la comprobación sobre el backlog tal como está hoy.
2. Mirar la salida. Resultado esperado: los cerrados viejos salen como aviso, no como falla, y se dice desde qué versión rige la exigencia.
3. Marcar hecho un pendiente nuevo sin fase y correr otra vez. Resultado esperado: ese sí sale como falla.
- **Aprobado cuando:** lo viejo avisa y lo nuevo falla.

### CA-05 — Un pendiente abierto sin historia se reporta

```gherkin
Dado que un pendiente está abierto
Cuando su ficha no nombra la historia de usuario donde vive
Entonces la comprobación lo reporta con su archivo
Y la corrida termina con error
```

**Cómo validarlo:**

1. Correr la comprobación sobre el backlog tal como está hoy. Resultado esperado: no reporta ninguno, porque los treinta y tres se enrutaron el 2026-08-17.
2. Abrir un pendiente de prueba sin la fila `Historia de usuario` en su ficha.
3. Correr otra vez. Resultado esperado: lo reporta y dice qué fila le falta y dónde escribirla.
4. Escribir la fila con una historia que exista y volver a correr. Resultado esperado: no reporta nada.
- **Aprobado cuando:** el pendiente sin historia se reporta y el que la tiene no. Es el CA que hace que este trabajo no se deshaga solo: sin él, el próximo pendiente nace suelto y nadie se entera.

### CA-06 — La historia nombrada existe

```gherkin
Dado que un pendiente nombra su historia de usuario
Cuando esa historia no existe en el árbol de épicas
Entonces la comprobación lo reporta y nombra la que no resolvió
```

**Cómo validarlo:**

1. En un pendiente de prueba, escribir una historia inventada — por ejemplo `EP-009 · HU-042`.
2. Correr la comprobación. Resultado esperado: reporta que no existe, con el identificador escrito.
3. Cambiarla por una real y volver a correr. Resultado esperado: no reporta nada.
- **Aprobado cuando:** la inventada se reporta y la real no. Sin esto, la fila se puede llenar con cualquier cosa y el campo pasa a ser decoración.

### CA-07 — El tema declarado no se reporta

```gherkin
Dado que un pendiente declara en su ficha que no es un ítem sino un tema
Cuando se corre la comprobación
Entonces no se reporta
```

**Cómo validarlo:**

1. Correr la comprobación sobre el backlog de hoy. Resultado esperado: no reporta el [01](../../../../pendientes/hecho/validadores-de-codigo-de-proyecto.md), el [09](../../../../pendientes/hecho/autonomia-sin-ia.md), el [10](../../../../pendientes/10-ideas.md) ni el [33](../../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md), que son los cuatro temas.
2. Borrarle la declaración a uno de ellos, dejando la fila vacía. Correr. Resultado esperado: lo reporta, porque una fila vacía no es una declaración.
- **Aprobado cuando:** los cuatro temas pasan con su declaración y ninguno pasa con la fila vacía.

### Criterios de aceptación transversales

- [ ] **Límites** — un backlog vacío, un pendiente sin encabezado y un índice desactualizado tienen comportamiento definido.
- [ ] **No regresión** — las comprobaciones que ya corrían sobre `pendientes/` siguen dando lo mismo.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Determinismo** | El mismo backlog da el mismo resultado, corra desde donde corra |
| RNF-02 | **Rendimiento** | Recorrer el backlog completo sin que la espera desanime a correrlo |
| RNF-03 | **Claridad** | El mensaje dice qué falta y dónde escribirlo, no solo que algo está mal |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica, la salida es texto en la terminal.
- **Documento funcional:** [documentacion/epicas/EP-004-comprobacion-automatica/epica.md](../epica.md).
- **Regla que comprueba:** [`02·F23`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md).
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [x] Fijar en la plantilla del pendiente el campo donde va la historia y la fase. **Va primero: sin él no hay qué leer.** — quedó como la fila `Historia de usuario` de la ficha de cabecera, escrita en los 33 archivos el 2026-08-17.
- [x] Enrutar los 33 pendientes a su historia, y crear las seis que no existían — hecho el 2026-08-17.
- [ ] Recorrer el backlog y separar lo abierto de lo cerrado.
- [ ] Comprobar que cada **abierto** trae la fila, y que la historia que nombra existe (`CA-05`, `CA-06`).
- [ ] Dejar pasar al que declara que es un tema, y no al que deja la fila vacía (`CA-07`).
- [ ] Comprobar que cada cerrado trae el campo, y que la fase que nombra existe.
- [ ] Separar por versión lo cerrado antes de que la regla existiera.
- [ ] Escribir las pruebas de lo que NO se debe reportar: lo viejo y lo que declaró no ser desarrollo.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-004-HU-016-el-pendiente-cerrado-declara-su-fase](A-EP-004-HU-016-el-pendiente-cerrado-declara-su-fase/README.md) | CA-01, CA-02, CA-03 y CA-04 | Abierta 2026-08-17, con su plan de trabajo escrito y sin aprobar |
| [B-EP-004-HU-016-todo-pendiente-abierto-nombra-su-historia](B-EP-004-HU-016-todo-pendiente-abierto-nombra-su-historia/README.md) | CA-05, CA-06 y CA-07 | Abierta 2026-08-17, con sus dos planes escritos y sin aprobar. **Sin dudas abiertas** |

**Las dos mitades de la misma pieza.** La `A` mira el pendiente **cerrado** y la `B` el **abierto**; escriben funciones distintas de `validadores/pendientes.py` y ninguna espera a la otra. La `A` está detenida por dos dudas y la `B` no tiene ninguna — **una de esas dos dudas la contestó el enrutamiento del 2026-08-17**: dónde se declara es la fila `Historia de usuario` de la ficha, medida en 33 archivos.

**Qué construye la `A`.** `02·F23` existe y nadie comprueba que el pendiente cerrado diga en qué fase se hizo: hay 17 cerrados y 12 lo nombran, cada uno a su manera. El trabajo fino son las tres excepciones.

**Qué documento responde qué**, para no buscar en el que no es:

| Pregunta | Documento |
|---|---|
| Qué se pide y cuándo se da por aceptado | Esta HU |
| Qué se va a hacer, en qué orden y sobre qué archivos | `plan_trabajo.md` de la fase |
| Con qué casos se comprueba cada CA | `plan_pruebas.md` de la fase |
| Qué se ejecutó, con qué resultado, y si el CA quedó cumplido | `resultado_pruebas.md` de la fase |
| En qué estación va y qué la tiene detenida | `estado-fase.md` de la fase |
| Qué quedó hecho al final | `funcionalidad_implementada.md` de la fase |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | Fijar el campo en la plantilla del pendiente. Sin sitio fijo el programa no tiene qué leer | Alto |
| Dependencia | [HU-003](../HU-003-formato-del-hallazgo/), porque los hallazgos salen con la forma ya definida | Medio |
| Riesgo | Que los cerrados viejos llenen la salida de ruido y nadie la mire | Salen como aviso y separados, con la versión desde la que rige |
| Riesgo | Que el campo se llene con un identificador que parezca fase y no lo sea | Se comprueba contra el árbol de épicas, no contra el texto |

---

## 10. Definition of Ready (DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [ ] Dependencias identificadas y desbloqueadas — falta fijar el campo en la plantilla del pendiente

## 11. Definition of Done (DoD)

- [ ] El pendiente cerrado sin fase se reporta
- [ ] La fase que no existe se reporta
- [ ] La excepción declarada no se reporta
- [ ] Lo cerrado antes de la regla sale como aviso y no hace fallar la corrida
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Parcial | Necesita que la plantilla del pendiente declare dónde va la fase |
| **N**egociable | Sí | Se puede discutir si lo viejo avisa o se ignora |
| **V**aliosa | Sí | La regla deja de depender de que alguien se acuerde |
| **E**stimable | Sí | El alcance lo fija el tamaño del backlog |
| **S**mall (pequeña) | Sí | Son dos comprobaciones sobre archivos de texto |
| **T**esteable | Sí | Se prueba cerrando pendientes de mentira mal a propósito |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-16 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde el hallazgo H-1 de la sesión «un pendiente no es un plan» |
| 2026-08-17 | Ing. José Dúmar Jiménez Ruíz | La exigencia se corre del cierre a la apertura: `RN-06` a `RN-08` y `CA-05` a `CA-07`. Sale de que el usuario pidió que ningún pendiente quede suelto, y de que al enrutarlos seis no tenían historia |
