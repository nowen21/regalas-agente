# Resultado de Pruebas — Fase B-EP-008-HU-001: se conecta un proyecto   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el `estado-fase.md` para pasar la puerta de verificación, y la fuente de la sección "qué se probó" del `funcionalidad_implementada.md`. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar: se aprobó antes y así se queda.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `B-EP-008-HU-001-se-conecta-un-proyecto` |
| **HU** | [HU-001 Conectar un proyecto](../HU-001-conectar-un-proyecto.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md), aprobado el 2026-08-25 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-25 |
| **Ejecutado por** | El agente, en la máquina del usuario |
| **Ambiente y versión** | Windows 11, Python 3.11.9, Django 5.2.11. Sobre `plataforma/`, sin commit todavía |

---

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 9 | 9 | 9 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

**62 comprobaciones automáticas**, las 34 que ya existían más 28 de esta fase. El plan exigía validarlas con sabotaje, y se hizo: cinco veces se rompió el código a propósito, y las cinco fallaron las pruebas correctas.

**Una prueba de la fase A hubo que corregirla.** La ruta `/` pasó a ser la lista de proyectos, y la comprobación de «la plataforma está viva» apuntaba ahí. Se movió a `/esta-viva/` y la prueba se actualizó: **la comprobación sigue haciendo falta**, porque dice si la plataforma responde sin depender de que haya proyectos conectados.

---

## 2. Ejecución caso por caso

### CP-001 · Un proyecto queda conectado

**El problema que resuelve:** si el registro no guarda lo que identifica al proyecto, la lista no sirve para nada y hay que ir a mirar carpeta por carpeta, que es lo que la plataforma vino a evitar.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Crear una carpeta de mentira con un `codigo.py`, un `CLAUDE.md` que declare la versión `34.1.0`, y su control de versiones | Queda el proyecto de prueba | Quedó, y la prueba lo borra al terminar |
| 2 | Conectarla con el nombre `Mi Proyecto Ñandú` | Queda registrada con nombre, ruta, versión y fecha | Los cuatro, y ningún aviso |
| 3 | Mirar el identificador que le tocó | Sirve como nombre de carpeta en cualquier sistema | `mi-proyecto-nandu`: sin espacios, sin acentos, sin mayúsculas |
| 4 | Preguntar por su estado | Responde `sin empezar` | `sin empezar` |
| 5 | Buscar su ficha en el disco y abrirla | Existe, y se lee sin la plataforma | `datos/proyectos/mi-proyecto-nandu/proyecto.md`, con su nombre y su ruta |
| 6 | Conectar **otro** proyecto con el mismo nombre | No se pisan | Identificadores distintos, dos proyectos en la lista |
| 7 | Borrar el índice entero y rehacerlo desde las fichas | Vuelven los dos | `2 proyecto(s)`, con sus nombres |

**Cómo se verificó que la pareja cumple:** el paso 3 es el que evita un problema que se descubre tarde. Un nombre con eñe o con espacios usado tal cual como carpeta funciona en una máquina y falla en otra. El paso 6 cubre el caso que rompe un identificador derivado del nombre: dos proyectos que se llaman igual. Y el 7 prueba que la ficha es la fuente y el índice se rehace, igual que en el resto de la plataforma.

### CP-002 · La ruta que no existe se rechaza, y se dice cuál era

**El problema que resuelve:** un proyecto que apunta a la nada ocupa un renglón en la lista y no sirve para nada. Y si el rechazo no dice qué ruta se buscó, el error de tecleo hay que adivinarlo.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Intentar conectar una ruta inventada | Revienta con `RutaQueNoExiste` | Reventó |
| 2 | Leer lo que dice el rechazo | **Trae la ruta que se buscó** | La trae completa |
| 3 | Contar los proyectos | Sigue en cero | Cero |
| 4 | Mirar si quedó algo escrito en la carpeta de datos | Nada, ni un archivo | Igual que antes: sin cambios |
| 5 | Contar los registros de auditoría | Cero: no hubo acción que registrar | Cero |

**Cómo se verificó que la pareja cumple:** los pasos 4 y 5 son los que decidieron el veredicto, no el 1. Un rechazo que igual dejó archivos escritos es peor que no rechazar, porque deja basura que nadie sabe de dónde salió. Y el paso 2 es lo que hace útil el rechazo: sin la ruta, el usuario tiene que comparar a ojo lo que escribió con lo que quería escribir.

### CP-003 · La ruta ya registrada dice qué proyecto la tiene

**El problema que resuelve:** dos proyectos apuntando al mismo código son dos verdades sobre lo mismo, y al cambiar una queda la otra vieja.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Conectar una carpeta con el nombre `El Primero` | Queda registrada | Quedó |
| 2 | Intentar conectar **la misma carpeta** con el nombre `El Segundo` | Revienta con `RutaYaRegistrada` | Reventó |
| 3 | Leer lo que dice el rechazo | Nombra **cuál** proyecto la tiene | `Esa carpeta ya está registrada por el proyecto «El Primero»` |
| 4 | Contar los proyectos | Sigue en uno | Uno |
| 5 | Intentar otra vez con **la misma carpeta escrita distinto**: en mayúsculas, o con la barra final | Rechaza igual | Rechazó |

**Cómo se verificó que la pareja cumple:** el paso 5 es el que decide. Comparar rutas como texto crudo deja pasar el duplicado en cuanto alguien escribe la misma carpeta de otra manera, que en Windows es todo el tiempo. Y el paso 3 es la diferencia entre un rechazo útil y uno que obliga a buscar a mano cuál de los proyectos ya tenía esa ruta.

### CP-004 · Una versión de reglas que no existe se rechaza

**El problema que resuelve:** un número inventado **mayor** que el real apaga el aviso de desfase en vez de dispararlo. El proyecto se queda atrás y nadie se entera.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Crear un proyecto cuyo `CLAUDE.md` declare la versión `999.0.0` | Queda el caso | Quedó |
| 2 | Intentar conectarlo | Revienta con `VersionQueNoExiste` | Reventó |
| 3 | Leer lo que dice | Nombra el número que se rechazó | Nombra `999.0.0` |
| 4 | Contar los proyectos | Cero | Cero |
| 5 | Comprobar contra qué se validó | Contra las versiones **publicadas en el registro de cambios**, no contra la vigente | `existe('34.1.0')` da verdadero, `existe('999.0.0')` da falso |

**Cómo se verificó que la pareja cumple:** el paso 5 es el que importa y es el que se hereda del pendiente 82. Comparar solo con la versión vigente dejaría pasar cualquier número mayor, que es justo el caso peligroso. Comprobar contra el registro de cambios pregunta otra cosa: si ese número **existió alguna vez**.

### CP-005 · La carpeta sin control de versiones se conecta, con advertencia

**El problema que resuelve:** si la advertencia se convierte en rechazo, la plataforma deja fuera a los proyectos que más falta le hacen.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Crear un proyecto **sin** control de versiones | Queda el caso | Quedó |
| 2 | Conectarlo | **Se registra** | Se registró |
| 3 | Leer los avisos que devolvió | Dice que su código no tiene respaldo | Lo dice |

**Cómo se verificó que la pareja cumple:** el paso 2 es el que decide, y decide por lo que **no** pasa: no rechaza. El 3 comprueba que la advertencia existe, porque conectar en silencio sería el otro error.

### CP-006 · Conectar deja su registro en la auditoría

**El problema que resuelve:** la fase D construyó la auditoría y la probó contra sí misma. Esta es la primera acción de verdad que tiene que pasar por ahí, y es donde se ve si sirve.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Contar los registros | Queda el número de partida | El de antes |
| 2 | Conectar un proyecto, diciendo quién y en qué sesión | Sube exactamente en uno | Subió en uno |
| 3 | Leer el registro que quedó | Trae qué se hizo, el proyecto, quién y la sesión | `conectar un proyecto`, con el identificador, `el agente` y `5f06ce4e` |
| 4 | Dejar el registro sin poder escribirse, y conectar otro | La acción se detiene | Reventó con `RegistroNoSePudoEscribir` |
| 5 | Contar los proyectos y buscar la carpeta que se iba a crear | **Ninguno quedó conectado, y la carpeta no existe** | Cero proyectos, sin carpeta |

**Cómo se verificó que la pareja cumple:** los pasos 4 y 5 son los que decidieron el veredicto. El 2 y el 3 prueban que el registro se escribe, pero eso no dice nada sobre el orden. Bloqueando la auditoría se ve lo que de verdad importa: sin constancia, el proyecto **no queda conectado**. La fase D lo prometió y acá se comprueba con una acción real.

### CP-007 · Se ve la lista y se entra a un proyecto

**El problema que resuelve:** una pantalla en blanco se lee como un error de la plataforma. Y sin pantalla, todo lo anterior existe pero no se puede usar.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Pedir la lista **sin ningún proyecto conectado** | Dice que está vacía, en vez de quedar en blanco | `Todavía no hay ningún proyecto conectado` |
| 2 | Conectar dos proyectos y pedir la lista | Salen los dos, con su estado | Salieron, con `sin empezar` |
| 3 | Entrar a uno de ellos | Trae su ruta y su versión | Los trae |
| 4 | Conectar uno **desde la pantalla**, con el formulario | Queda conectado y lo dice | `Quedó conectado`, y hay un proyecto más |
| 5 | Intentar conectar una ruta inventada desde la pantalla | Muestra el rechazo, y **no pierde lo que el usuario escribió** | Muestra `No existe la carpeta`, y el nombre `Fantasma` sigue en el formulario |
| 6 | Entrar a un proyecto que no declara versión | Se ve el aviso | Se ve |
| 7 | Levantar el servidor de verdad y pedir las dos páginas | Responden | Las dos, con el proyecto real conectado |

**Cómo se verificó que la pareja cumple:** el paso 5 es el que decide si la pantalla sirve o estorba. Un formulario que borra lo escrito al fallar obliga a teclearlo todo de nuevo, y el error suele estar en un solo carácter. El paso 1 cubre el caso que casi nunca se prueba, que es el del primer día: la lista vacía.

### CP-008 · El proyecto sin estándar instalado se conecta, con aviso

**El problema que resuelve:** si la plataforma solo administra proyectos que ya adoptaron el estándar, no administra los proyectos del usuario: administra un subconjunto que además es el que menos ayuda necesita.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Crear un proyecto **sin** `CLAUDE.md` | Queda el caso | Quedó |
| 2 | Conectarlo | **Se registra**, con la versión vacía | Se registró, `version_reglas` vacía |
| 3 | Leer los avisos | Dice que todavía no declara ninguna versión | Lo dice |
| 4 | Repetirlo con un `CLAUDE.md` que **existe pero no declara versión** | Mismo resultado | Igual: se conecta, con su aviso |
| 5 | En la misma prueba, conectar el que no declara nada **y** el que declara `999.0.0` | El primero entra, el segundo se rechaza | Entró uno, el otro reventó. Un proyecto en la lista |
| 6 | Entrar a su pantalla | El aviso se ve | Se ve |

**Cómo se verificó que la pareja cumple:** el paso 5 es el que protege la diferencia entre **vacío y falso**, y es la que se pierde sola. Los dos casos entran por el mismo camino en el código, y si alguien los junta, uno de los dos queda mal sin que nadie lo note: o se empiezan a aceptar versiones inventadas, o se empiezan a rechazar proyectos sin estándar. Que la prueba haga los dos en la misma corrida es lo que lo impide.

### CP-009 · Que NO pase: que conectar toque la carpeta del proyecto

**El problema que resuelve:** la plataforma administra carpetas ajenas. Escribir donde no debe es el error que nadie perdona, y el que además se descubre tarde.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Retratar la carpeta del proyecto: cada archivo, con su contenido y su fecha | Queda el punto de comparación | Quedó |
| 2 | Conectarlo | Se registra | Se registró |
| 3 | Retratar la carpeta otra vez y comparar la lista de archivos | Ninguno se creó ni se borró | Idéntica |
| 4 | Comparar archivo por archivo el contenido y la fecha | Ninguno cambió | Ninguno |
| 5 | Repetir con un proyecto que se **rechaza** por versión inventada | Tampoco se toca | Retrato idéntico |
| 6 | Comprobar que la ficha quedó en los datos de la plataforma, y **no** en la carpeta del proyecto | Está en `datos/`, no allá | `datos/proyectos/uno/proyecto.md` sí; `proyecto.md` en el proyecto, no |
| 7 | Con el repositorio real conectado, contar sus archivos antes y después | El mismo número | 13518 antes, 13518 después |

**Cómo se verificó que la pareja cumple:** el paso 4 es el que decide, no el 3. La lista de archivos puede ser idéntica y el contenido de uno haber cambiado. El paso 5 cubre el camino que se olvida: rechazar y haber escrito igual. Y el 6 comprueba lo simétrico, que lo que sí se escribió esté donde tiene que estar.

**Sobre el paso 7 hay algo que anotar.** El primer conteo sobre el repositorio real dio 13616 antes y 13618 después, y **no fue una violación**: la carpeta de datos de la plataforma vive dentro de ese repositorio, porque el proyecto conectado es el que la contiene. Los dos archivos nuevos eran la ficha y el registro de auditoría, los dos en `datos/`. Descontando `plataforma/`, el conteo es 13518 en los dos lados. Queda escrito porque un conteo sin ese descuento parecería decir lo contrario.

**Tabla de casos ejecutados:**

| Caso | Qué exige | Prioridad | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | `CA-01` | Crítica | 2026-08-25 | `Mi Proyecto Ñandú` quedó como `mi-proyecto-nandu`, con su ficha en `datos/proyectos/mi-proyecto-nandu/proyecto.md` y estado `sin empezar` | Aprobado | EV-01, EV-03 | — |
| CP-002 | `CA-02` | Crítica | 2026-08-25 | Una ruta inventada dio `RutaQueNoExiste` con la ruta adentro; la carpeta de datos quedó igual y sin registros | Aprobado | EV-01 | — |
| CP-003 | `CA-03` | Crítica | 2026-08-25 | La segunda conexión dio `Esa carpeta ya está registrada por el proyecto «El Primero»`, también con la ruta escrita en mayúsculas | Aprobado | EV-01, EV-03 | — |
| CP-004 | `RN-3` de la especificación | Crítica | 2026-08-25 | Un `CLAUDE.md` con `999.0.0` fue rechazado; `existe('34.1.0')` da verdadero y `existe('999.0.0')` falso | Aprobado | EV-01 | — |
| CP-005 | Transversal | Alta | 2026-08-25 | Una carpeta sin control de versiones quedó conectada, con el aviso de que su código no tiene respaldo | Aprobado | EV-01 | — |
| CP-006 | `RN-3` de la HU | Crítica | 2026-08-25 | Conectar dejó un registro con `conectar un proyecto`, el identificador, `el agente` y la sesión. Con la auditoría bloqueada, cero proyectos y sin carpeta | Aprobado | EV-01, EV-03 | — |
| CP-007 | Las dos pantallas | Alta | 2026-08-25 | La lista vacía dice que lo está; con dos proyectos los muestra; el formulario conecta y, al rechazar, conserva lo escrito. Servidas de verdad en el puerto 8742 | Aprobado | EV-01, EV-04 | — |
| CP-008 | La decisión del 2026-08-25 | Alta | 2026-08-25 | Un proyecto sin `CLAUDE.md` quedó conectado con la versión vacía y su aviso; en la misma prueba, el que declara `999.0.0` fue rechazado | Aprobado | EV-01, EV-03 | — |
| CP-009 | `CA-04` | Crítica | 2026-08-25 | Retrato archivo por archivo idéntico antes y después, también al rechazar. Sobre el repositorio real: 13518 y 13518 | Aprobado | EV-01, EV-03 | — |

**Correspondencia con el plan:** 9 casos en el plan, 9 acá. Ninguno de más, ninguno de menos.

**Qué salió distinto de lo esperado:** nada falló. Lo que hubo fueron dos cosas que anotar: la prueba de la fase A que hubo que mover de ruta, y el conteo del repositorio real que a primera vista parecía acusar un cambio.

---

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que las pruebas cacen lo que dicen cazar | Cinco sabotajes: quitar la comprobación de ruta, la de duplicado, la de versión inventada, confundir vacío con falso, y escribir la ficha dentro del proyecto | Las cinco veces fallaron las pruebas correctas: 3, 2, 3, 4 y 2 fallas |
| 2 | Que la plataforma sirva las dos pantallas de verdad | Se levantó en el puerto 8742 y se pidieron las dos páginas | Las dos respondieron, con el proyecto real |
| 3 | Que conectar el repositorio real no lo toque | Conteo de archivos antes y después, descontando `plataforma/` | 13518 y 13518 |
| 4 | Que la ficha y el registro se lean sin la plataforma | `cat` sobre los dos archivos | Los dos legibles |
| 5 | Que los dos índices se rehagan desde el texto | `reconstruir_proyectos` y `reconstruir_auditoria` | 1 proyecto y 1 acción recuperados |
| 6 | Que los datos de prueba no quedaran | Se borraron y se rehicieron los índices | `0 proyecto(s)` y `0 acción(es)` |

**Una advertencia que salió de acá.** El primer guion de sabotaje restauraba los archivos con el control de versiones, y estos todavía no están versionados: uno quedó saboteado y solo se notó al final, cuando la corrida limpia salió en rojo. La evidencia se rehizo restaurando con copias. **Un guion de sabotaje que no restaura bien deja el código roto y las pruebas mintiendo en la dirección contraria.**

---

## 4. Defectos encontrados

Ninguno.

**Defectos abiertos que se aceptan y por qué:** ninguno.

---

## 5. Veredicto por criterio de aceptación

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| `CA-01` un proyecto queda registrado | CP-001 | Con sus cuatro datos, su identificador seguro y su carpeta | Sí |
| `CA-02` una ruta que no existe no se registra | CP-002 | Rechaza, dice qué ruta se buscó, y no deja nada escrito | Sí |
| `CA-03` registrar dos veces la misma ruta avisa | CP-003 | Dice cuál proyecto la tiene, también escrita distinto | Sí |
| `CA-04` registrar no toca el código | CP-009 | Retrato idéntico archivo por archivo, y al rechazar también | Sí |
| Transversal: la acción queda en la auditoría | CP-006 | Un registro por conexión, y sin constancia no hay conexión | Sí |
| Transversal: sin control de versiones se advierte | CP-005 | Se conecta, con su aviso | Sí |
| `RN-3` la versión declarada debe existir | CP-004 | Contra las publicadas, no contra la vigente | Sí |
| La decisión del 2026-08-25 sobre proyectos sin estándar | CP-008 | Se conectan, con su aviso, sin confundirse con los que declaran falso | Sí |
| Las dos pantallas muestran y dejan conectar | CP-007 | Servidas de verdad, incluida la lista vacía | Sí |

**Los que no cumplen:** ninguno.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Los nueve casos con veredicto escrito | Plan de pruebas §7 | 9 | 9 | Sí |
| Ningún caso en **No cumple** sin corregir | Plan de pruebas §7 | 0 | 0 | Sí |
| Las pruebas validadas con sabotaje | Plan de pruebas §7 | Todas las promesas | 5 sabotajes, 5 cazados | Sí |
| Ninguna carpeta real del usuario usada como conejillo | Plan de pruebas §7 | 0 | 0. Los proyectos de prueba se crean y se borran solos | Sí |

**Lo que no se cumplió:** nada quedó corto.

**Sobre el repositorio real.** Se conectó, y eso no lo vuelve un conejillo: conectar no lo toca, y es lo que `CP-009` comprobó contando sus archivos. Es además la prueba que la especificación del módulo pedía, en su §2: *"el propio repositorio será el primer proyecto que se conecte, y esa es la prueba real de este módulo"*.

---

## 6. Veredicto de la fase

**Concepto:** **Cumple**.

**Justificación:** los cuatro criterios de aceptación de la historia quedaron probados, cada uno por el paso que de verdad los decide: la comparación archivo por archivo para `CA-04`, la ruta escrita de dos maneras para `CA-03`, y la carpeta de datos intacta para `CA-02`. Las 62 comprobaciones automáticas se validaron con cinco sabotajes. El repositorio del propio estándar quedó conectado como primer proyecto real, que es la prueba que la especificación pedía.

**Qué falta para que cumpla:** nada.

**Lo que la fase deja sin resolver, y no es un incumplimiento:** conectar todavía no tiene reversa. Salió al ver la primera pantalla funcionando, no está en el alcance de esta fase, y quedó pedido por la cadena completa: [pendientes/86-conectar-un-proyecto-no-tiene-reversa.md](../../../../../pendientes/86-conectar-un-proyecto-no-tiene-reversa.md) y la [HU-004](../../HU-004-administrar-un-proyecto-conectado/HU-004-administrar-un-proyecto-conectado.md), que es la fase H.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Salida de las 62 comprobaciones automáticas, con versiones | [evidencias/EV-01-pruebas-automaticas.txt](evidencias/EV-01-pruebas-automaticas.txt) |
| EV-02 | Los cinco sabotajes, y qué prueba cazó cada uno | [evidencias/EV-02-las-pruebas-cazan-el-sabotaje.txt](evidencias/EV-02-las-pruebas-cazan-el-sabotaje.txt) |
| EV-03 | Corrida real: el repositorio del estándar conectado, con el conteo de archivos | [evidencias/EV-03-corrida-real.txt](evidencias/EV-03-corrida-real.txt) |
| EV-04 | Las dos pantallas, tal como las sirvió el servidor | [evidencias/EV-04-las-dos-pantallas.txt](evidencias/EV-04-las-dos-pantallas.txt) |

---

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-08-25 | 9 | 0 | Primera ejecución |
