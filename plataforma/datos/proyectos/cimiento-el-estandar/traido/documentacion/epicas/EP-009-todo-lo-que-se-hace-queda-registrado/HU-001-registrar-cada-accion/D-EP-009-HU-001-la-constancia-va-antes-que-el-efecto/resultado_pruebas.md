# Resultado de Pruebas — Fase D-EP-009-HU-001: la constancia va antes que el efecto   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el `estado-fase.md` para pasar la puerta de verificación, y la fuente de la sección "qué se probó" del `funcionalidad_implementada.md`. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar: se aprobó antes y así se queda.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `D-EP-009-HU-001-la-constancia-va-antes-que-el-efecto` |
| **HU** | [HU-001 Registrar cada acción](../HU-001-registrar-cada-accion.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md), aprobado el 2026-08-25 |
| **Ciclo** | 2. El 1 encontró un hueco en `CP-007`, se corrigió y se corrió completo otra vez |
| **Fecha de ejecución** | 2026-08-25 |
| **Ejecutado por** | El agente, en la máquina del usuario |
| **Ambiente y versión** | Windows 11, Python 3.11.9, Django 5.2.11. Sobre `plataforma/`, sin commit todavía |

---

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 7 | 7 | 6 | 1 | 0 | 0 |
| 2 | 7 | 7 | 7 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

**Qué pasó entre los dos ciclos.** `CP-007` falló en el ciclo 1, y falló bien: encontró que `almacen.guardar` se podía llamar directo y el archivo cambiaba sin dejar registro. Con ese camino abierto, `CA-01` no se cumplía. Corregirlo obligaba a tocar `plataforma/nucleo/almacen/`, que el plan aprobado no declaraba, así que **la fase se detuvo y se pidió el visto bueno** (`02·F8`). El usuario autorizó ampliar el plan el 2026-08-25, sobre dos opciones escritas con su costo. La ampliación quedó anotada en la sección 2.1 del [plan de trabajo](plan_trabajo.md).

**Las 37 comprobaciones automáticas pasaron a la primera, y eso no se dio por bueno.** Se saboteó el código a propósito, cuatro veces, para ver si las pruebas cazaban cada falla. Las cuatro veces fallaron las pruebas correctas. Sin ese paso, "todo en verde" no habría dicho nada.

---

## 2. Ejecución caso por caso

### CP-001 · La acción queda registrada con sus seis datos

**El problema que resuelve:** un registro al que le falta un dato no sirve para rastrear nada. Si no dice quién, no responde; si no dice cuándo, no ubica.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Registrar una acción completa: conectar `rni-back`, por el usuario, en la sesión `5f06ce4e` | Devuelve el comprobante con las siete columnas | Las siete: cuándo, quién, qué se hizo, sobre qué, qué cambió, proyecto, sesión |
| 2 | Buscar esa acción en el índice | Está, con su proyecto y su sesión | `proyecto = rni-back`, `sesión = 5f06ce4e` |
| 3 | Registrar una acción **sin** proyecto: publicar una versión de reglas | Se registra igual, con el campo vacío | `proyecto = ""`, y quedó en el índice |
| 4 | Abrir el archivo del registro con `cat` | Se lee sin la plataforma | Salió la tabla completa, con su cabecera |
| 5 | Borrar el índice del registro y rehacerlo desde el texto | Vuelven todas las filas | `Índice de auditoría rehecho: 3 acción(es).` |

**Cómo se verificó que la pareja cumple:** el paso 3 es el que decide que la fase se puede construir antes que la B: si una acción sin proyecto se rechazara, habría que esperar al módulo de proyectos. El paso 5 prueba que el registro es texto y no base de datos: se borró el índice entero y volvió completo.

### CP-002 · Editar o borrar no se puede, y el intento queda

**El problema que resuelve:** un registro que se puede cambiar después no demuestra nada. Es la diferencia entre una constancia y una nota.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Registrar una acción, tomar la fila del índice y cambiarle un campo | Al guardar, rechaza | `SoloSeAgrega: Lo registrado no se edita.` |
| 2 | Leer esa fila otra vez | Sigue diciendo lo de antes | `que_se_hizo = "una acción"`, sin cambiar |
| 3 | Intentar borrar la fila, y después borrar el conjunto entero | Rechaza las dos veces | `SoloSeAgrega` en ambas |
| 4 | Intentar actualizar en bloque | Rechaza | `SoloSeAgrega` |
| 5 | Llamar a `editar()` y a `borrar()` del registro | Rechazan, y el intento queda escrito | `LoRegistradoNoSeToca`, y en el texto: `intento de editar el registro / nada: se rechazó` |
| 6 | Registrar otra acción y comparar el archivo contra el de antes | El texto nuevo empieza exactamente con el viejo | Empieza igual: nada se reescribió |

**Cómo se verificó que la pareja cumple:** el paso 2 es el que decide, no el 1. Que la operación reviente no prueba que el dato no cambió: se comprueba leyéndolo después. El paso 6 prueba lo mismo sobre el texto, que es la fuente: solo se agregó al final. Y el 5 es el que cumple la segunda mitad del criterio, que pide que **el intento quede registrado**, no solo que se rechace.

### CP-003 · Con el registro bloqueado, nada cambia

**El problema que resuelve:** si el cambio se hace y después falla el registro, queda un cambio del que nadie sabe. Es el caso que hace inútil una auditoría.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Dejar el registro sin poder escribirse, poniendo un archivo donde va la carpeta | La escritura va a fallar | Bloqueado |
| 2 | Pedir que se registre una acción | Revienta con `RegistroNoSePudoEscribir` | Reventó |
| 3 | Pedir un cambio con `con_constancia`, con una acción que anota si se ejecutó | Revienta, y la acción **no deja huella** | Reventó, y la huella quedó vacía |
| 4 | Buscar el archivo que esa acción iba a escribir | No existe | No existe |
| 5 | Desbloquear y repetir el cambio | Ahora sí se ejecuta, y el registro queda | El archivo quedó escrito y hay 1 registro |
| 6 | Espiar el orden real: envolver la escritura del registro y anotar cuándo ocurre | Primero la constancia, después el efecto | `["constancia", "efecto"]` |

**Cómo se verificó que la pareja cumple:** el paso 6 es el que decide, y es el que faltaba en la primera versión de esta prueba. Los pasos 3 y 4 muestran que ante la falla nada cambia, pero eso también pasaría con un código que ejecuta primero y revierte después. Espiar el orden es lo único que distingue *"la constancia va antes"* de *"al final quedaron las dos cosas"*. El paso 1 usa un archivo en vez de quitar permisos porque en Windows quitarle la escritura a una carpeta no impide crear archivos dentro: lo que se prueba es el comportamiento ante la falla, no la forma de provocarla.

### CP-004 · La clave queda tapada, con comillas y sin ellas

**El problema que resuelve:** lo que se guarda hoy se publica mañana. Una clave escrita en el registro queda en el control de versiones para siempre.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Registrar una acción cuyo campo traiga `password: "inventada123"` | La clave no aparece; el nombre de la variable sí | En el texto: `password: "«enmascarado»"` |
| 2 | Registrar otra con `API_KEY=inventada456`, sin comillas | Tapada también | `API_KEY=«enmascarado»` |
| 3 | Poner la clave en un campo distinto: `secret=inventada789` en «qué cambió» | Tapada igual | No aparece en el texto |
| 4 | Buscar esas claves en el índice, no solo en el texto | Tampoco están | No están |

**Cómo se verificó que la pareja cumple:** el paso 2 es el que importa, porque es el que fallaba antes del pendiente 84: la clave sin comillas es la que una persona teclea. El paso 4 cubre el descuido de tapar al escribir y guardar en claro al indexar. **Las tres claves son inventadas**, y eso es parte de lo que se está probando: probar el tapado con una clave real sería el mismo daño que se quiere evitar.

### CP-005 · Lo que solo parece clave se deja legible

**El problema que resuelve:** tapar de más vuelve el registro ilegible, y entonces nadie lo lee. Un registro que nadie lee no sirve más que uno que no existe.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Registrar una acción con `clave: tu-clave` y con `changeme` | Ninguno se tapa | Los dos quedaron legibles |
| 2 | Comprobarlo también fuera de la plataforma, contra el módulo del estándar | El molde no se toca | `clave: tu-clave` intacto, `0` tapadas |

**Cómo se verificó que la pareja cumple:** son los dos moldes que el estándar declara que **no** se tapan. Sin este caso, un enmascarador que tapara todo pasaría `CP-004` con nota perfecta y dejaría el registro inservible.

### CP-006 · El enlace a la sesión está, y vacío cuando no la hay

**El problema que resuelve:** la acción dice qué se hizo; el porqué está en lo que la sesión escribió. Sin el enlace, la auditoría responde una pregunta y no la otra.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Registrar una acción dentro de una sesión, con su identificador | El registro lo trae completo | `5f06ce4e-64bf-41e5-b58e-87959b32bf62` |
| 2 | Registrar una acción fuera de toda sesión | El enlace queda vacío, no faltante | `""` |
| 3 | Crear un archivo de histórico llamado `2026-08-25-sesion.md` con su marca de sesión adentro | Queda el punto de partida | Quedó |
| 4 | Registrar una acción con ese identificador, y después **renombrar** el archivo a `2026-08-25-la-auditoria.md` | El renombre es lo normal: el archivo nace sin tema y lo recibe después | Renombrado |
| 5 | Buscar el archivo por el identificador que guardó el registro | Lo encuentra, con el nombre nuevo | Encontró `2026-08-25-la-auditoria.md` |

**Cómo se verificó que la pareja cumple:** el paso 4 es el que decide, y no estaba en la primera versión del plan. Se agregó al resolver la duda 2: el agente había propuesto guardar el nombre del archivo, y el propio código del histórico explicaba por qué eso no sirve. Sin el renombre, este caso habría pasado en verde con la implementación equivocada, y el enlace se habría roto la primera vez que una sesión recibiera su tema.

### CP-007 · Que NO pase: que algo cambie sin quedar registrado

**El problema que resuelve:** si existe un camino que escribe sin pasar por la auditoría, los otros seis casos pueden estar todos en verde y la auditoría no servir. Es el caso que mira el conjunto, no la parte.

**Cómo se hizo la prueba, paso a paso, en el ciclo 1:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Contar los registros | Queda el número de partida | 0 |
| 2 | Guardar un documento por el camino correcto, con `con_constancia` | Sube a 1 | 1 |
| 3 | Guardar otro llamando a `almacen.guardar` directo | Debería no poderse, o dejar su registro | **Escribió, y los registros siguieron en 1** |
| 4 | Comprobar si el archivo quedó | No debería estar | `b.md quedó escrito: True` |

**Veredicto del ciclo 1: No cumple.** Un archivo cambió sin registro. Con ese camino abierto, `CA-01` tampoco se cumplía.

**Qué se hizo con eso.** Corregirlo obligaba a tocar `plataforma/nucleo/almacen/`, fuera de lo que el plan declaraba, así que la fase se detuvo y se presentaron dos opciones: cerrarlo ahora ampliando el plan, o declararlo como deuda para la fase B. El usuario autorizó cerrarlo el 2026-08-25. La razón que inclinó la balanza: hoy no hay un solo llamador de `almacen.guardar` fuera de las pruebas, y con la fase B encima ya serían varios.

**Cómo quedó.** `almacen.guardar` ahora exige el comprobante que emite la auditoría al registrar la acción, y ese comprobante **solo vale para el archivo sobre el que se registró**.

**Cómo se hizo la prueba, paso a paso, en el ciclo 2:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Contar los registros | Punto de partida | 0 |
| 2 | Guardar por el camino correcto | Sube a 1 | 1 |
| 3 | Guardar llamando a `almacen.guardar` sin constancia | Rechaza | `SinConstancia: «b.md» se iba a escribir sin constancia` |
| 4 | Comprobar si el archivo quedó, y si el conteo cambió | No, y no | `b.md quedó escrito: False` · registros: 1 |
| 5 | Registrar una acción sobre `a.md` y usar **ese** comprobante para escribir `c.md` | Rechaza: es de otro archivo | `SinConstancia: La constancia es de «a.md», no de «c.md»` |
| 6 | Comprobar si `c.md` quedó | No | `c.md quedó escrito: False` |
| 7 | Ejecutar las tres acciones que la plataforma sabe hacer, por el camino correcto, y contar | Un registro por cada una | 3 registros nuevos, 3 acciones |

**Cómo se verificó que la pareja cumple:** el paso 5 es el que decide, más que el 3. Rechazar cuando no hay constancia solo cubre el olvido total; el descuido probable es reutilizar el comprobante que uno tiene a mano para escribir otra cosa, y ese es el que el paso 5 cierra. Los pasos 4 y 6 comprueban el archivo, no solo la excepción: reventar y haber escrito igual es una falla que el error solo taparía.

**Lo que este caso no promete, y está escrito en el código:** la constancia no es una barrera contra alguien que quiera saltársela a propósito. En este lenguaje el objeto se puede construir a mano. Lo que se logra es que escribir sin constancia sea un acto deliberado y visible, en vez de un olvido que nadie nota.

**Tabla de casos ejecutados:**

| Caso | Qué exige | Prioridad | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | `CA-01` | Crítica | 2026-08-25 | Se registró `conectar un proyecto` sobre `rni-back` en la sesión `5f06ce4e`: las siete columnas quedaron, y una acción sin proyecto también | Aprobado | EV-01, EV-03 | — |
| CP-002 | `CA-02` | Crítica | 2026-08-25 | Cambiar la fila y guardarla dio `SoloSeAgrega`, y al releerla seguía diciendo `una acción`. `editar()` dejó la línea `intento de editar el registro / nada: se rechazó` | Aprobado | EV-01, EV-03 | — |
| CP-003 | `CA-03` | Crítica | 2026-08-25 | Con el registro bloqueado, `con_constancia` reventó y la acción no dejó huella; `cambiado.md` no existe. Espiando el orden salió `["constancia", "efecto"]` | Aprobado | EV-01 | — |
| CP-004 | `CA-05` | Crítica | 2026-08-25 | `password: "inventada123"`, `API_KEY=inventada456` y `secret=inventada789` quedaron como `«enmascarado»`, en el texto y en el índice | Aprobado | EV-01, EV-03 | — |
| CP-005 | `CA-05` | Alta | 2026-08-25 | `clave: tu-clave` y `changeme` quedaron legibles, `0` tapadas | Aprobado | EV-01 | — |
| CP-006 | `CA-04` | Alta | 2026-08-25 | Se renombró `2026-08-25-sesion.md` a `2026-08-25-la-auditoria.md` y el identificador guardado siguió encontrando el archivo | Aprobado | EV-01 | — |
| CP-007 | Que NO pase | Crítica | 2026-08-25 | Ciclo 1: `almacen.guardar` directo escribió `b.md` sin registro. Ciclo 2: rechaza con `SinConstancia`, y una constancia de `a.md` tampoco sirve para `c.md` | Aprobado en el ciclo 2 | EV-04 | DEF-01, corregido |

**Correspondencia con el plan:** 7 casos en el plan, 7 acá. Ninguno de más, ninguno de menos.

**Qué salió distinto de lo esperado:** `CP-007` en el ciclo 1, que es el defecto `DEF-01`. Todo lo demás pasó a la primera.

---

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que las pruebas cacen las fallas que dicen cazar | Se saboteó el código cuatro veces, una por cada cosa que la fase promete | Las cuatro veces fallaron las pruebas correctas: 2, 4, 1 y 4 fallas |
| 2 | Que el registro se lea sin la plataforma | `cat datos/auditoria/2026-08.md` | Salió la tabla completa, legible |
| 3 | Que el índice del registro se rehaga desde el texto | `python manage.py reconstruir_auditoria` | `Índice de auditoría rehecho: 3 acción(es).` |
| 4 | Que el enmascarador del estándar se importe de verdad | Se llamó desde la plataforma antes de escribir una línea de la fase | Tapó las dos formas de clave, dejó el molde |
| 5 | Que los datos de mentira no quedaran | Se borraron y se rehicieron los dos índices | `0 acción(es)` y `0 archivo(s)` |

---

## 4. Defectos encontrados

| ID | Título | Caso que lo destapó | Severidad | Estado | Dónde quedó registrado |
|---|---|---|---|---|---|
| DEF-01 | `almacen.guardar` escribía sin dejar constancia, y con ese camino abierto `CA-01` no se cumplía | CP-007, ciclo 1 | Crítica | Corregido y verificado en el ciclo 2 | Sección 2.1 del [plan de trabajo](plan_trabajo.md), como ampliación autorizada. Evidencia en EV-04 |

**Defectos abiertos que se aceptan y por qué:** ninguno.

---

## 5. Veredicto por criterio de aceptación

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| `CA-01` toda acción que cambia algo queda registrada | CP-001, CP-007 | Se registra con sus siete datos, y ya no hay camino que escriba sin constancia | Sí |
| `CA-02` lo registrado no se puede editar ni borrar | CP-002 | Rechaza en la fila, en el conjunto y en bloque; el intento queda escrito | Sí |
| `CA-03` sin constancia no hay efecto | CP-003 | Con el registro bloqueado nada cambió, y el orden real es constancia y después efecto | Sí |
| `CA-04` la acción de una sesión queda enlazada | CP-006 | El identificador aguanta el renombre del archivo | Sí |
| `CA-05` ninguna credencial entra al registro | CP-004, CP-005 | Las dos formas de clave tapadas; los moldes intactos | Sí |
| `RNF-12` toda acción dice quién, cuándo y sobre qué | CP-001 | Las siete columnas | Sí |
| `RNF-05` ninguna credencial escrita | CP-004 | Ni en el texto ni en el índice | Sí |
| El registro es texto: se lee sin la plataforma | CP-001 paso 4 | `cat` mostró la tabla | Sí |

**Los que no cumplen:** ninguno.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Los siete casos con veredicto escrito | Plan de pruebas §7 | 7 | 7 | Sí |
| Ningún caso en **No cumple** sin corregir | Plan de pruebas §7 | 0 | 0. `CP-007` falló y se corrigió antes de cerrar | Sí |
| Ninguna credencial real usada en las pruebas | Plan de pruebas §7 | 0 | 0. Todas inventadas | Sí |
| Si un caso falla, se corre el ciclo completo | Plan de pruebas §3.5 | Ciclo entero | Se corrieron los 7 otra vez, no solo el que falló | Sí |

**Lo que no se cumplió:** nada quedó corto.

---

## 6. Veredicto de la fase

**Concepto:** **Cumple**.

**Justificación:** los cinco criterios de aceptación de la historia quedaron probados, cada uno por el paso que de verdad los decide y no por el que era más fácil de escribir. El único defecto, `DEF-01`, lo encontró el caso que existía para eso, se detuvo la fase para pedir el visto bueno en vez de ampliar el plan por iniciativa, y se corrigió con el ciclo completo repetido. Las 37 comprobaciones automáticas se validaron saboteando el código cuatro veces.

**Qué falta para que cumpla:** nada.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Salida de las 37 comprobaciones automáticas, con versiones | [evidencias/EV-01-pruebas-automaticas.txt](evidencias/EV-01-pruebas-automaticas.txt) |
| EV-02 | Los cuatro sabotajes, y qué prueba cazó cada uno | [evidencias/EV-02-las-pruebas-cazan-el-sabotaje.txt](evidencias/EV-02-las-pruebas-cazan-el-sabotaje.txt) |
| EV-03 | Corrida real: registro, intento de edición, el texto y su reconstrucción | [evidencias/EV-03-corrida-real.txt](evidencias/EV-03-corrida-real.txt) |
| EV-04 | `CP-007` después de cerrar el camino, con los dos rechazos | [evidencias/EV-04-la-puerta-de-atras-cerrada.txt](evidencias/EV-04-la-puerta-de-atras-cerrada.txt) |

---

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-08-25 | 6 | 1 | Primera ejecución. `CP-007` encontró que `almacen.guardar` escribía sin constancia |
| 2 | 2026-08-25 | 7 | 0 | El plan se amplió con autorización del usuario, y `almacen.guardar` pasó a exigir el comprobante de la acción |
