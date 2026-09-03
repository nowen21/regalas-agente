# Inventario de funcionalidades — Cimiento   ·   `[CAPA 3]`

**Para qué sirve este documento.** Es el alcance completo, ítem por ítem: todo lo que la plataforma debe tener, esté construido o no. Aprobado por el usuario, es la puerta de las épicas ([`02·F26`](../../base/02-flujo-de-trabajo/reglas/F26-el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-epicas.md)).

> **Escrito desde la propuesta, no desde lo que hoy existe.** Sale de los 32 requisitos de [cvds/analisis-requisitos/README.md](README.md). Todas las fichas dicen «Definida» y «Sin verificar»: lo que se escribe es el alcance acordado, no el estado del código.

**Estado: APROBADO** (2026-08-24, por Ing. José Dúmar Jiménez Ruíz). Con esta aprobación se abre la puerta de las épicas.

## Las tres clases

| Clase | Qué significa |
|---|---|
| **Obligatoria** | Sin esto el producto no sirve para lo que se hizo |
| **Complementaria** | Suma valor, pero el producto arranca sin ella |
| **Futura** | Se sabe que se quiere, y se decidió que no ahora |

## Resumen

Una línea por funcionalidad, para verlas todas juntas. El detalle de cada una está en su ficha, más abajo.

| ID | Funcionalidad | Clase | Parte del sistema | Prioridad | Estado | Verificado |
|---|---|---|---|---|---|---|
| F-001 | Conectar un proyecto | Obligatoria | Proyectos | Alta | Construida | Verificada |
| F-002 | Avisar cuando la ruta de un proyecto se pierde | Obligatoria | Proyectos | Alta | Construida | Verificada |
| F-003 | Ver el estado de un proyecto sin entrar a él | Obligatoria | Proyectos | Alta | Construida | Verificada |
| F-004 | Configurar qué rige en cada proyecto | Complementaria | Proyectos | Media | Construida | Verificada |
| F-005 | Escribir, cambiar y derogar reglas | Obligatoria | Reglas | Alta | Construida | Verificada |
| F-006 | Asignar el identificador sin reutilizar ninguno | Obligatoria | Reglas | Alta | Construida | Verificada |
| F-007 | Aplicar el checklist a una regla y guardar su sello | Complementaria | Reglas | Media | Construida | Verificada |
| F-008 | Publicar una versión del cuerpo de reglas | Obligatoria | Reglas | Alta | Construida | Verificada |
| F-009 | Entregarle las reglas al agente al abrir sesión | Obligatoria | Reglas | Alta | Construida | Verificada |
| F-010 | Avisar a un proyecto que quedó atrás | Complementaria | Reglas | Media | Construida | Verificada |
| F-011 | Crear épicas, historias y fases con su molde | Obligatoria | Ciclo de vida | Alta | Construida | Verificada |
| F-012 | Ver en qué estación va cada fase | Obligatoria | Ciclo de vida | Alta | Construida | Verificada |
| F-013 | Impedir avanzar sin la puerta cumplida | Obligatoria | Ciclo de vida | Alta | Construida | Verificada |
| F-014 | Llenar los documentos del ciclo desde la plataforma | Obligatoria | Ciclo de vida | Alta | Construida | Verificada |
| F-015 | Registrar una aprobación con su firma | Obligatoria | Aprobaciones | Alta | Construida | Verificada |
| F-016 | Ver qué está aprobado y qué está en borrador | Obligatoria | Aprobaciones | Alta | Construida | Verificada |
| F-017 | Caducar la aprobación cuando el texto cambia | Obligatoria | Aprobaciones | Alta | Construida | Verificada |
| F-018 | Registrar cada acción que se hace | Obligatoria | Auditoría | Alta | Construida | Verificada |
| F-019 | Consultar lo registrado | Complementaria | Auditoría | Media | Construida | Verificada |
| F-020 | Comprobar sola lo que las reglas exigen | Obligatoria | Comprobaciones | Alta | Construida | Verificada |
| F-021 | Declarar sin verificar lo que no tiene prueba | Obligatoria | Comprobaciones | Alta | Construida | Verificada |
| F-022 | Comprobar que lo nuevo no rompió lo anterior | Obligatoria | Comprobaciones | Alta | Construida | Verificada |
| F-023 | Guardar lo aprendido y devolverlo después | Obligatoria | Memoria | Alta | Construida | Verificada |
| F-024 | Consultar y corregir lo guardado | Complementaria | Memoria | Media | Construida | Verificada |
| F-025 | Armar el expediente de un proyecto | Obligatoria | Expediente | Alta | Construida | Verificada |
| F-026 | Generar el entregable de ofimática | Obligatoria | Expediente | Alta | Construida | Verificada |
| F-027 | Traer un proyecto que ya existe | Obligatoria | Importación | Alta | Construida | Verificada |
| F-028 | Reportar qué de lo traído no sigue ningún molde | Complementaria | Importación | Media | Construida | Verificada |
| F-029 | Avisar lo que se desvía | Complementaria | Avisos | Media | Construida | Verificada |
| F-030 | Reportar cómo va cada proyecto | Complementaria | Avisos | Media | Construida | Verificada |
| F-031 | Tapar toda credencial antes de escribirla | Obligatoria | Seguridad | Alta | Construida | Verificada |
| F-032 | Medir el tiempo que se gasta revisando | Futura | Medición | Baja | Construida | Verificada |
| F-033 | Guardar las conversaciones donde se pueda buscar | Complementaria | Medición | Media | Construida | Verificada |
| F-034 | Decir qué correcciones se repiten | Complementaria | Medición | Media | Construida | Verificada |
| F-035 | Administrar un proyecto ya conectado | Obligatoria | Proyectos | Alta | Construida | Verificada |
| F-036 | Entrar con cuenta y contraseña | Obligatoria | Acceso | Alta | Construida | Verificada |
| F-037 | Separar lo que cada grupo puede hacer | Obligatoria | Acceso | Alta | Construida | Verificada |

**Cuenta:** 23 obligatorias, 11 complementarias y 1 futura, de 35. **Las 35 construidas, y las 35 con veredicto.**

> **De dónde salen esas dos columnas.** No se escriben a mano: las deriva la plataforma, y se preguntan con `python manage.py estado_funcionalidades <proyecto>`. **Construida** quiere decir que hay una fase que la construye; **verificada**, que esa fase cerró con veredicto *Cumple*.
>
> **Verificada no quiere decir que alguien de afuera la comprobó.** Quiere decir que la fase que la construyó corrió sus pruebas y las declaró en verde. Es lo que el estándar entiende por verificar, y no es lo mismo que una auditoría ajena.
>
> Esta columna estuvo en «sin verificar» para las 35 hasta el 2026-09-02, por escribirse a mano mientras la plataforma ya sabía la respuesta.

> **`F-033`, `F-034` y `F-035` entraron el 2026-08-25**, después de aprobado el inventario. Quedan anotadas en la sección 14.1 de [README.md](README.md), con quién las aprobó. La cuenta cambió de 32 a 35 por eso, y no por un error de conteo.

## La columna «Verificado» ya no se mantiene a mano

**Desde el 2026-09-01 el estado de una funcionalidad se deriva de la fase que la construyó**, siguiendo la cadena que ya está escrita: el inventario, la §13 de la especificación de su módulo, la fase, y el veredicto que esa fase declaró. Se pide así:

```
python manage.py estado_funcionalidades <identificador>
```

**Lo que dicen las fichas de abajo es lo que se escribió el día que se aprobó el inventario**, y no se actualiza a mano: mantener a mano un dato que se puede derivar termina en dos verdades, y la escrita es la que nadie mira. Al 2026-09-01: **14 verificadas de 35**, y son exactamente las construidas.

**Sin verificar no es lo mismo que no cumple.** Una es que nadie comprobó; la otra, que se comprobó y salió mal.

## Qué dice la columna «Depende de», y qué no dice

**Dice qué tiene que existir para que la funcionalidad sirva. No dice en qué orden hay que construir.** Son dos cosas distintas y confundirlas hace leer el plan al revés.

Lo que una ficha nombra ahí puede llegar por dos caminos: construído en la plataforma, o **traído por la importación**, que incorpora los documentos y las fases que un proyecto ya tiene escritos. El segundo camino existe desde la versión 1.

Dos funcionalidades cerradas y andando lo demuestran:

| Ficha | Dice depender de | Se construyó sin ella porque |
|---|---|---|
| `F-027` · versión 1 | `F-011` | Trae las fases que el proyecto ya tiene, en vez de crearlas |
| `F-025` · versión 2 | `F-014` | Arma el expediente con los documentos traídos, sin llenarlos ahí |

**Y la columna tiene un ciclo, encontrado el 2026-09-01.** Tres funcionalidades de la versión 3 se esperan entre sí:

```
F-008 (publicar una version) -> F-022 (comprobar que no rompio) -> F-020 (comprobar lo exigido) -> F-008
```

**Leído como orden de construcción, ninguna de las tres se puede empezar.** Leído como lo que la columna de verdad dice, se resuelve solo: `F-020` necesita que **exista** un cuerpo de reglas contra el cual comprobar, y existe desde el primer día, escrito en `base/`. No necesita que la plataforma lo publique.

Es el mismo malentendido de arriba, en su forma más clara: **una cadena de necesidades puede tener vueltas sin que nada esté mal; una cadena de construcción, no.**

**Para saber si algo está bloqueado no basta esta columna:** hay que preguntarse si lo que necesita ya lo trae la importación. El reparto por versiones vive en [cvds/implementacion/README.md](../implementacion/README.md) §2, y ahí está escrito por qué ninguna versión se movió por esto.

## Las funcionalidades, una por una

### Conectar un proyecto

| Campo | Valor |
|---|---|
| **Identificador** | `F-001` |
| **De qué se trata** | Registrar un proyecto en la plataforma: su nombre y dónde vive su código |
| **Para qué sirve** | Es lo primero: sin proyectos conectados no hay nada que administrar |
| **Parte del sistema** | Proyectos |
| **Quién la usa** | El usuario |
| **Qué recibe** | El nombre y la ruta del código |
| **Qué entrega** | El proyecto registrado, listo para recibir documentación y reglas |
| **Reglas que debe respetar** | `RN-2` registrar no toca el código del proyecto |
| **Depende de** | Ninguna |
| **Terminada cuando** | `CA-1` un proyecto queda registrado y aparece en la lista · `CA-2` una ruta que no existe no se registra, y se dice por qué · `CA-3` registrar dos veces la misma ruta avisa cuál proyecto ya la tiene |
| **Qué necesita construirse** | Pantalla, lógica y almacenamiento |
| **Prioridad** | Alta |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | Un proyecto sin control de versiones se puede registrar, pero se advierte: su código no tiene respaldo |

### Avisar cuando la ruta de un proyecto se pierde

| Campo | Valor |
|---|---|
| **Identificador** | `F-002` |
| **De qué se trata** | Detectar que la carpeta de un proyecto ya no está donde estaba, y decirlo |
| **Para qué sirve** | Que la plataforma no muestre como vivo un proyecto que se movió o se borró |
| **Parte del sistema** | Proyectos |
| **Quién la usa** | El usuario, sin hacer nada |
| **Qué recibe** | La ruta registrada de cada proyecto |
| **Qué entrega** | El aviso de cuál se perdió, con la ruta que buscó |
| **Reglas que debe respetar** | `RN-4` no se afirma sobre lo que no se leyó |
| **Depende de** | F-001 |
| **Terminada cuando** | `CA-1` una ruta que dejó de existir queda avisada · `CA-2` la documentación de ese proyecto se sigue viendo · `CA-3` volver a apuntar la ruta quita el aviso |
| **Qué necesita construirse** | Lógica y pantalla |
| **Prioridad** | Alta |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | Perder la ruta no puede borrar nada: la documentación vive en la plataforma, no allá |

### Ver el estado de un proyecto sin entrar a él

| Campo | Valor |
|---|---|
| **Identificador** | `F-003` |
| **De qué se trata** | Mostrar en qué va un proyecto: qué etapas tiene escritas, qué fases están abiertas y qué falta aprobar |
| **Para qué sirve** | Es el motivo de la plataforma: hoy hay que entrar a cada proyecto para saberlo |
| **Parte del sistema** | Proyectos |
| **Quién la usa** | El usuario |
| **Qué recibe** | Lo que la plataforma guardó de ese proyecto |
| **Qué entrega** | Su estado en pantalla, de un vistazo |
| **Reglas que debe respetar** | `RN-5` lo que no tiene prueba corrida se muestra como sin verificar |
| **Depende de** | F-001 |
| **Terminada cuando** | `CA-1` se ve el estado sin abrir la carpeta del proyecto · `CA-2` un proyecto sin trabajo abierto lo dice, y no muestra una pantalla vacía · `CA-3` lo que está sin aprobar se distingue de lo aprobado |
| **Qué necesita construirse** | Pantalla y lógica |
| **Prioridad** | Alta |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | Mostrar de más cansa: primero lo que decide algo, el detalle después |

### Configurar qué rige en cada proyecto

| Campo | Valor |
|---|---|
| **Identificador** | `F-004` |
| **De qué se trata** | Elegir por proyecto qué reglas opcionales rigen y qué moldes usa |
| **Para qué sirve** | Que un proyecto pequeño no cargue con lo que solo necesita uno grande |
| **Parte del sistema** | Proyectos |
| **Quién la usa** | El usuario |
| **Qué recibe** | La elección de reglas y moldes |
| **Qué entrega** | La configuración guardada, que el agente recibe al abrir |
| **Reglas que debe respetar** | Lo obligatorio no se puede apagar |
| **Depende de** | F-001, F-005 |
| **Terminada cuando** | `CA-1` una regla opcional se activa y desactiva por proyecto · `CA-2` una obligatoria no se puede desactivar, y se dice por qué · `CA-3` el agente recibe lo configurado allí, no lo de otro proyecto |
| **Qué necesita construirse** | Pantalla, lógica y almacenamiento |
| **Prioridad** | Media |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | Cada opción que se agrega es una forma más de que dos proyectos no se parezcan |

### Escribir, cambiar y derogar reglas

| Campo | Valor |
|---|---|
| **Identificador** | `F-005` |
| **De qué se trata** | Administrar las reglas desde la plataforma: escribirlas, corregirlas y quitarles vigencia |
| **Para qué sirve** | Que el cuerpo de reglas se mantenga sin editar archivos a mano |
| **Parte del sistema** | Reglas |
| **Quién la usa** | El usuario |
| **Qué recibe** | El texto de la regla y a qué capítulo pertenece |
| **Qué entrega** | La regla guardada, con su identificador y pendiente de publicar |
| **Reglas que debe respetar** | `RN-6` nada se borra: se deroga |
| **Depende de** | F-006 |
| **Terminada cuando** | `CA-1` una regla nueva queda guardada con su identificador · `CA-2` derogar deja la regla legible y marcada · `CA-3` una regla que contradice a otra vigente muestra el choque antes de guardar |
| **Qué necesita construirse** | Pantalla, lógica y almacenamiento |
| **Prioridad** | Alta |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | Escribir la regla es lo fácil; lo que cuesta es que no repita ni contradiga a otra |

### Asignar el identificador sin reutilizar ninguno

| Campo | Valor |
|---|---|
| **Identificador** | `F-006` |
| **De qué se trata** | Dar a cada regla su número, tomando el siguiente libre y sin reasignar los que quedaron sueltos |
| **Para qué sirve** | Que una cita escrita hace un año siga apuntando a lo mismo |
| **Parte del sistema** | Reglas |
| **Quién la usa** | El sistema solo, al crear una regla |
| **Qué recibe** | El capítulo al que entra la regla |
| **Qué entrega** | El identificador asignado |
| **Reglas que debe respetar** | `RN-6` el número de una regla derogada no se le da a otra |
| **Depende de** | Ninguna |
| **Terminada cuando** | `CA-1` una regla nueva recibe el siguiente número libre · `CA-2` el número de una derogada no se reasigna · `CA-3` no se puede guardar una regla con un identificador ya usado |
| **Qué necesita construirse** | Lógica y almacenamiento |
| **Prioridad** | Alta |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | Es de las pocas cosas que se pueden comprobar solas, y conviene que lo haga |

### Aplicar el checklist a una regla y guardar su sello

| Campo | Valor |
|---|---|
| **Identificador** | `F-007` |
| **De qué se trata** | Correr la lista de comprobación sobre una regla y guardar el resultado junto a ella |
| **Para qué sirve** | Que se sepa contra qué versión se revisó y cuándo, sin volver a revisarla entera |
| **Parte del sistema** | Reglas |
| **Quién la usa** | El usuario, con el agente |
| **Qué recibe** | La regla y la lista de comprobación vigente |
| **Qué entrega** | El sello: qué filas pasaron, cuáles no aplican, y contra qué versión |
| **Reglas que debe respetar** | `RN-8` si la regla se edita, el sello queda anulado |
| **Depende de** | F-005 |
| **Terminada cuando** | `CA-1` una regla queda con su sello y su fecha · `CA-2` editar la regla anula el sello y lo dice · `CA-3` una fila que no aplica queda escrita con su motivo |
| **Qué necesita construirse** | Pantalla, lógica y almacenamiento |
| **Prioridad** | Media |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | Buena parte de las filas pide criterio: la plataforma acompaña, no decide |

### Publicar una versión del cuerpo de reglas

| Campo | Valor |
|---|---|
| **Identificador** | `F-008` |
| **De qué se trata** | Cerrar los cambios pendientes en una versión, con su número, su fecha y qué cambió |
| **Para qué sirve** | Que los proyectos sepan qué rige y desde cuándo |
| **Parte del sistema** | Reglas |
| **Quién la usa** | El usuario |
| **Qué recibe** | Las reglas cambiadas desde la última publicación |
| **Qué entrega** | La versión publicada, con qué cambió y si obliga a rehacer algo |
| **Reglas que debe respetar** | `RN-1` lo que cambió queda escrito, no dicho |
| **Depende de** | F-005, F-022 |
| **Terminada cuando** | `CA-1` se publica con su número, su fecha y qué cambió · `CA-2` sin registro de qué cambió no se publica · `CA-3` si rompe algo que servía, no se publica hasta corregirlo |
| **Qué necesita construirse** | Pantalla, lógica y almacenamiento |
| **Prioridad** | Alta |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | Publicar es lo que vuelve real un cambio: antes de eso, nada rige |

### Entregarle las reglas al agente al abrir sesión

| Campo | Valor |
|---|---|
| **Identificador** | `F-009` |
| **De qué se trata** | Que al abrir sesión en cualquier proyecto, el agente reciba las reglas que rigen ahí |
| **Para qué sirve** | Es lo que hace que la plataforma gobierne, y no solo guarde |
| **Parte del sistema** | Reglas |
| **Quién la usa** | El agente, sin que nadie lo pida |
| **Qué recibe** | Qué proyecto abre, y qué versión adoptó |
| **Qué entrega** | Las reglas vigentes para ese proyecto, y el aviso de qué versión rige |
| **Reglas que debe respetar** | `RN-7` si la plataforma no responde, la fuente en texto sigue siendo legible |
| **Depende de** | F-001, F-008 |
| **Terminada cuando** | `CA-1` al abrir, el agente tiene las reglas sin pedirlas · `CA-2` entregarlas no demora la apertura más de dos segundos · `CA-3` si la plataforma no está disponible, se avisa y se trabaja leyendo la fuente |
| **Qué necesita construirse** | Tarea que corre sola al abrir, y lógica |
| **Prioridad** | Alta |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | Que el agente las reciba no garantiza que las obedezca: eso lo cubre F-020 |

### Avisar a un proyecto que quedó atrás

| Campo | Valor |
|---|---|
| **Identificador** | `F-010` |
| **De qué se trata** | Decirle a un proyecto que la versión que adoptó ya no es la última, y qué cambió desde entonces |
| **Para qué sirve** | Que nadie siga una versión vieja sin saberlo |
| **Parte del sistema** | Reglas |
| **Quién la usa** | Quien trabaje en ese proyecto |
| **Qué recibe** | La versión adoptada y la publicada |
| **Qué entrega** | El aviso, empezando por lo que obliga a rehacer algo |
| **Reglas que debe respetar** | `RN-2` avisar no es actualizar |
| **Depende de** | F-008, F-009 |
| **Terminada cuando** | `CA-1` con versión anterior, avisa y dice qué cambió · `CA-2` con la misma, no molesta · `CA-3` con un número que no existe, lo dice en vez de concluir que va adelantado |
| **Qué necesita construirse** | Tarea que corre sola al abrir, y lógica |
| **Prioridad** | Media |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | Un aviso que aparece siempre se vuelve ruido y se ignora |

### Crear épicas, historias y fases con su molde

| Campo | Valor |
|---|---|
| **Identificador** | `F-011` |
| **De qué se trata** | Abrir cada unidad de trabajo desde la plataforma, con su documento ya formado |
| **Para qué sirve** | Que nadie cree carpetas y archivos a mano, ni se salte un documento |
| **Parte del sistema** | Ciclo de vida |
| **Quién la usa** | El usuario, con el agente |
| **Qué recibe** | Qué se abre, en qué proyecto y de qué historia depende |
| **Qué entrega** | La unidad creada, con sus documentos y su nombre |
| **Reglas que debe respetar** | El nombre de una fase dice a qué historia pertenece |
| **Depende de** | F-001 |
| **Terminada cuando** | `CA-1` se abre una fase y quedan sus documentos con el molde · `CA-2` una fase sin historia no se puede abrir · `CA-3` el nombre sale del identificador, no se escribe a mano |
| **Qué necesita construirse** | Pantalla, lógica y almacenamiento |
| **Prioridad** | Alta |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | Es donde más se nota si los moldes son pesados: se llenan en cada fase |

### Ver en qué estación va cada fase

| Campo | Valor |
|---|---|
| **Identificador** | `F-012` |
| **De qué se trata** | Mostrar el avance de una fase: qué estaciones pasó, cuál sigue y qué puerta falta |
| **Para qué sirve** | Que el estado no dependa de que alguien lo recuerde |
| **Parte del sistema** | Ciclo de vida |
| **Quién la usa** | El usuario |
| **Qué recibe** | Lo que la fase tiene escrito |
| **Qué entrega** | La estación actual y la puerta pendiente |
| **Reglas que debe respetar** | `RN-5` el estado lo fija lo escrito, no la opinión |
| **Depende de** | F-011 |
| **Terminada cuando** | `CA-1` se ve la estación actual de cualquier fase · `CA-2` se ve qué falta para pasar a la siguiente · `CA-3` una fase detenida dice desde cuándo |
| **Qué necesita construirse** | Pantalla y lógica |
| **Prioridad** | Alta |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | Sirve para ver todas las fases a la vez: una sola se ve mirando su documento |

### Impedir avanzar sin la puerta cumplida

| Campo | Valor |
|---|---|
| **Identificador** | `F-013` |
| **De qué se trata** | No dejar pasar a la estación siguiente mientras falte lo que esa puerta exige |
| **Para qué sirve** | Que las puertas se cumplan sin depender de que alguien las recuerde |
| **Parte del sistema** | Ciclo de vida |
| **Quién la usa** | El usuario, con el agente |
| **Qué recibe** | La fase y lo que lleva escrito |
| **Qué entrega** | El paso concedido, o el rechazo diciendo qué falta |
| **Reglas que debe respetar** | `RN-5` sin prueba corrida no se cierra |
| **Depende de** | F-012 |
| **Terminada cuando** | `CA-1` una fase sin plan aprobado no pasa a ejecución · `CA-2` una fase sin veredicto no se cierra · `CA-3` el rechazo dice cuál puerta falta, no solo que falta |
| **Qué necesita construirse** | Lógica |
| **Prioridad** | Alta |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | Una puerta que estorba se termina saltando: cada una tiene que justificarse |

### Llenar los documentos del ciclo desde la plataforma

| Campo | Valor |
|---|---|
| **Identificador** | `F-014` |
| **De qué se trata** | Escribir y editar los documentos de cada etapa dentro de la plataforma, con su molde |
| **Para qué sirve** | Que documentar sea parte del trabajo y no una tarea aparte |
| **Parte del sistema** | Ciclo de vida |
| **Quién la usa** | El usuario y el agente |
| **Qué recibe** | El documento y lo que se escribe en él |
| **Qué entrega** | El documento guardado, con lo que le falta por llenar |
| **Reglas que debe respetar** | `RN-1` se guarda donde no se borra · `RN-7` la fuente es texto |
| **Depende de** | F-011 |
| **Terminada cuando** | `CA-1` se escribe un documento sin salir de la plataforma · `CA-2` se ve cuántos espacios le faltan por llenar · `CA-3` lo guardado queda como texto legible sin la plataforma |
| **Qué necesita construirse** | Pantalla, lógica y almacenamiento |
| **Prioridad** | Alta |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | Si escribir ahí es más incómodo que en un editor, nadie lo va a usar |

### Registrar una aprobación con su firma

| Campo | Valor |
|---|---|
| **Identificador** | `F-015` |
| **De qué se trata** | Guardar que alguien aprobó un documento: quién, cuándo y sobre qué texto exacto |
| **Para qué sirve** | Que se pueda demostrar meses después qué se autorizó |
| **Parte del sistema** | Aprobaciones |
| **Quién la usa** | El usuario |
| **Qué recibe** | El documento y la decisión de aprobarlo |
| **Qué entrega** | La aprobación registrada, atada al texto que se aprobó |
| **Reglas que debe respetar** | `RN-8` se aprueba un texto, no un documento en abstracto |
| **Depende de** | F-014 |
| **Terminada cuando** | `CA-1` queda registrado quién aprobó, cuándo y sobre qué texto · `CA-2` la aprobación se puede consultar meses después · `CA-3` no se puede aprobar un documento que no existe |
| **Qué necesita construirse** | Pantalla, lógica y almacenamiento |
| **Prioridad** | Alta |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | Es la pieza que hoy no existe, y de la que se sostiene todo el gobierno |

### Ver qué está aprobado y qué está en borrador

| Campo | Valor |
|---|---|
| **Identificador** | `F-016` |
| **De qué se trata** | Mostrar el estado de aprobación de cada documento, en cualquier proyecto |
| **Para qué sirve** | Saber sobre qué se puede construir, y qué todavía puede cambiar |
| **Parte del sistema** | Aprobaciones |
| **Quién la usa** | El usuario |
| **Qué recibe** | Los documentos y sus aprobaciones |
| **Qué entrega** | Qué está firmado y qué no, con su fecha |
| **Reglas que debe respetar** | `RN-5` no se muestra como aprobado lo que no lo está |
| **Depende de** | F-015 |
| **Terminada cuando** | `CA-1` se distingue lo aprobado de lo que está en borrador · `CA-2` se ve desde cuándo · `CA-3` un documento sin aprobación aparece así, no vacío |
| **Qué necesita construirse** | Pantalla y lógica |
| **Prioridad** | Alta |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | Dicho con palabras, no solo con color: quien no distingue colores tiene que poder saberlo |

### Caducar la aprobación cuando el texto cambia

| Campo | Valor |
|---|---|
| **Identificador** | `F-017` |
| **De qué se trata** | Detectar que un documento aprobado cambió, y quitarle la aprobación |
| **Para qué sirve** | Que nadie dé por aprobado un texto que nadie leyó así |
| **Parte del sistema** | Aprobaciones |
| **Quién la usa** | El usuario, sin hacer nada |
| **Qué recibe** | El documento aprobado y el texto que se guarda ahora |
| **Qué entrega** | La aprobación caducada, con qué cambió desde que se firmó |
| **Reglas que debe respetar** | `RN-8` lo aprobado se congela |
| **Depende de** | F-015 |
| **Terminada cuando** | `CA-1` editar un documento aprobado le quita la aprobación · `CA-2` se ve qué cambió respecto de lo aprobado · `CA-3` la aprobación anterior no se borra: queda como historia |
| **Qué necesita construirse** | Lógica y almacenamiento |
| **Prioridad** | Alta |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | Salió de un caso real: se aprobaron tres documentos y al día siguiente el cambio de producto los dejó sin valor |

### Registrar cada acción que se hace

| Campo | Valor |
|---|---|
| **Identificador** | `F-018` |
| **De qué se trata** | Guardar qué se hizo sobre proyectos, documentos y reglas, y lo que cada sesión dejó escrito: quién, cuándo y sobre qué |
| **Para qué sirve** | Poder rastrear cualquier cambio hasta quién lo hizo |
| **Parte del sistema** | Auditoría |
| **Quién la usa** | El sistema solo, cada vez que algo cambia |
| **Qué recibe** | La acción que se acaba de ejecutar, y el resumen y las decisiones que la sesión escribió |
| **Qué entrega** | El registro guardado |
| **Reglas que debe respetar** | `RN-9` nada de lo registrado incluye credenciales |
| **Depende de** | F-001 |
| **Terminada cuando** | `CA-1` toda acción que cambia algo queda registrada · `CA-2` el registro dice quién, cuándo y sobre qué · `CA-3` lo registrado no se puede editar · `CA-4` lo que la sesión dejó escrito queda enlazado desde el registro · `CA-5` la conversación completa no entra |
| **Qué necesita construirse** | Lógica y almacenamiento |
| **Prioridad** | Alta |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | Registrar cada mensaje pesa mucho, se llena de ruido y arrastra credenciales. La transcripción se guarda aparte, como hasta hoy, y la auditoría enlaza el resumen |

### Consultar lo registrado

| Campo | Valor |
|---|---|
| **Identificador** | `F-019` |
| **De qué se trata** | Buscar en la auditoría por proyecto, por fecha y por tipo de acción |
| **Para qué sirve** | Un registro que no se puede consultar es un archivo que nadie abre |
| **Parte del sistema** | Auditoría |
| **Quién la usa** | El usuario |
| **Qué recibe** | Los filtros de la búsqueda |
| **Qué entrega** | Lo registrado que coincide, de lo más reciente a lo más viejo |
| **Reglas que debe respetar** | `RN-4` si no hay coincidencias, se dice |
| **Depende de** | F-018 |
| **Terminada cuando** | `CA-1` se filtra por proyecto, fecha y tipo de acción · `CA-2` sin coincidencias se dice que no hay · `CA-3` responde en menos de un segundo con un año de registros |
| **Qué necesita construirse** | Pantalla y lógica |
| **Prioridad** | Media |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | Sin esta, la auditoría existe pero no sirve |

### Comprobar sola lo que las reglas exigen

| Campo | Valor |
|---|---|
| **Identificador** | `F-020` |
| **De qué se trata** | Programas que leen lo escrito y dicen si cumple las reglas, sin corregir nada |
| **Para qué sirve** | Que el cumplimiento no dependa de que el agente se acuerde |
| **Parte del sistema** | Comprobaciones |
| **Quién la usa** | El usuario, y el agente antes de entregar |
| **Qué recibe** | Los documentos y el código del proyecto, y qué regla comprobar |
| **Qué entrega** | Qué cumple, qué no, y en qué archivo y línea |
| **Reglas que debe respetar** | `RN-4` no se afirma sobre lo que no se leyó |
| **Depende de** | F-008 |
| **Terminada cuando** | `CA-1` un documento que cumple pasa · `CA-2` uno que no cumple es rechazado con el archivo y la línea · `CA-3` apuntada a algo que no le corresponde, lo dice en vez de dar veredicto |
| **Qué necesita construirse** | Lógica |
| **Prioridad** | Alta |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | Una comprobación que reprueba de más se apaga a la semana, y entonces no queda nada vigilando |

### Declarar sin verificar lo que no tiene prueba

| Campo | Valor |
|---|---|
| **Identificador** | `F-021` |
| **De qué se trata** | Que el estado de una funcionalidad lo fije la prueba corrida, no la lectura |
| **Para qué sirve** | Que no se entregue como terminado lo que nadie comprobó |
| **Parte del sistema** | Comprobaciones |
| **Quién la usa** | El usuario, al leer qué está hecho de verdad |
| **Qué recibe** | El cierre de una unidad de trabajo, con sus pruebas y su evidencia |
| **Qué entrega** | El veredicto por criterio: cumple, no cumple o sin verificar |
| **Reglas que debe respetar** | `RN-5` la prueba corrida manda sobre la lectura |
| **Depende de** | F-020 |
| **Terminada cuando** | `CA-1` con prueba y evidencia queda verificado · `CA-2` sin prueba queda «sin verificar» y no se puede cerrar · `CA-3` con prueba fallida queda «no cumple», con lo que falló |
| **Qué necesita construirse** | Lógica |
| **Prioridad** | Alta |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | «Sin verificar» tiene que ser una respuesta aceptable, o se falsean las pruebas para poder cerrar |

### Comprobar que lo nuevo no rompió lo anterior

| Campo | Valor |
|---|---|
| **Identificador** | `F-022` |
| **De qué se trata** | Antes de publicar, volver a correr lo que ya funcionaba |
| **Para qué sirve** | Que la plataforma pueda crecer sin que cada cosa nueva se lleve por delante lo anterior |
| **Parte del sistema** | Comprobaciones |
| **Quién la usa** | El usuario, al publicar |
| **Qué recibe** | La versión que se va a publicar |
| **Qué entrega** | Qué sigue sirviendo, qué se rompió, y qué obliga a rehacer algo |
| **Reglas que debe respetar** | `RN-5` lo dice la prueba corrida, no la lectura |
| **Depende de** | F-020 |
| **Terminada cuando** | `CA-1` una versión que rompe algo no se publica · `CA-2` una que obliga a rehacer algo lo declara · `CA-3` una que no rompe nada pasa sin trabajo manual |
| **Qué necesita construirse** | Lógica |
| **Prioridad** | Alta |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | Solo puede comprobar lo que tenga prueba: lo que nunca se probó no se sabe si se rompió |

### Guardar lo aprendido y devolverlo después

| Campo | Valor |
|---|---|
| **Identificador** | `F-023` |
| **De qué se trata** | Que lo que se decide, se corrige o se descubre quede guardado, y la sesión siguiente lo reciba |
| **Para qué sirve** | Que el agente no arranque en blanco, y que la corrección no se repita |
| **Parte del sistema** | Memoria |
| **Quién la usa** | El agente al abrir; el usuario cuando quiere consultar |
| **Qué recibe** | Lo que la sesión dejó: decisiones, correcciones y hallazgos |
| **Qué entrega** | Lo guardado, con su fecha y de qué proyecto salió |
| **Reglas que debe respetar** | `RN-1` vive donde no se borra · `RN-9` nada guardado incluye credenciales |
| **Depende de** | F-001 |
| **Terminada cuando** | `CA-1` lo guardado en una sesión se recupera en la siguiente · `CA-2` lo de un proyecto no se mezcla con el de otro · `CA-3` si no hay nada guardado del tema, se dice en vez de inventar |
| **Qué necesita construirse** | Lógica y almacenamiento |
| **Prioridad** | Alta |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | Es la mitad del problema original: sin esto, cada sesión vuelve a empezar |

### Consultar y corregir lo guardado

| Campo | Valor |
|---|---|
| **Identificador** | `F-024` |
| **De qué se trata** | Ver la memoria, buscar en ella, corregir lo que dejó de ser cierto y darlo de baja |
| **Para qué sirve** | Que lo que el agente recuerda no sea invisible ni intocable para el usuario |
| **Parte del sistema** | Memoria |
| **Quién la usa** | El usuario |
| **Qué recibe** | La búsqueda o la corrección |
| **Qué entrega** | Lo guardado, corregido o dado de baja, sin borrar la historia |
| **Reglas que debe respetar** | `RN-6` lo que deja de valer se marca, no se borra |
| **Depende de** | F-023 |
| **Terminada cuando** | `CA-1` se busca por palabra y por proyecto · `CA-2` corregir deja constancia de qué decía antes · `CA-3` dar de baja no lo borra: lo deja fuera de lo que se le entrega al agente |
| **Qué necesita construirse** | Pantalla, lógica y almacenamiento |
| **Prioridad** | Media |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | Es un problema de confianza antes que de comodidad: hoy solo el agente ve lo que recuerda |

### Armar el expediente de un proyecto

| Campo | Valor |
|---|---|
| **Identificador** | `F-025` |
| **De qué se trata** | Juntar todos los documentos de un proyecto en el orden del ciclo, cuando se pida |
| **Para qué sirve** | Es lo que hoy cuesta un día: armarlo documento por documento |
| **Parte del sistema** | Expediente |
| **Quién la usa** | El usuario |
| **Qué recibe** | Qué proyecto, y qué alcance: todo o hasta cierta fase |
| **Qué entrega** | El expediente armado, con lo que falta señalado |
| **Reglas que debe respetar** | `RN-5` lo que está sin verificar se entrega diciendo que lo está |
| **Depende de** | F-014 |
| **Terminada cuando** | `CA-1` se arma el expediente completo de un proyecto · `CA-2` los documentos que faltan se listan, y no se inventan · `CA-3` los que tienen espacios sin llenar se marcan antes de entregar |
| **Qué necesita construirse** | Pantalla y lógica |
| **Prioridad** | Alta |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | Qué recibe un cliente, y si eso incluye la auditoría y la memoria, es la duda 5 del análisis |

### Generar el entregable de ofimática

| Campo | Valor |
|---|---|
| **Identificador** | `F-026` |
| **De qué se trata** | Convertir el expediente en un archivo de ofimática, generado desde la fuente en texto |
| **Para qué sirve** | Entregar en el formato que el cliente espera sin mantener dos versiones del mismo texto |
| **Parte del sistema** | Expediente |
| **Quién la usa** | El usuario, y quien reciba el proyecto |
| **Qué recibe** | El expediente armado |
| **Qué entrega** | El archivo generado, nunca escrito a mano |
| **Reglas que debe respetar** | `RN-7` la fuente es el texto: la salida no se edita |
| **Depende de** | F-025 |
| **Terminada cuando** | `CA-1` un expediente completo se genera con todas sus secciones · `CA-2` uno con espacios sin llenar avisa antes de generar · `CA-3` generar dos veces da el mismo resultado |
| **Qué necesita construirse** | Lógica |
| **Prioridad** | Alta |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | Las listas dentro de una celda tienen que salir como listas, no con la etiqueta a la vista |

### Traer un proyecto que ya existe

| Campo | Valor |
|---|---|
| **Identificador** | `F-027` |
| **De qué se trata** | Incorporar a la plataforma un proyecto con la documentación que ya tenga escrita |
| **Para qué sirve** | Que empezar a gobernar un proyecto no obligue a rehacer su historia |
| **Parte del sistema** | Importación |
| **Quién la usa** | El usuario |
| **Qué recibe** | El proyecto y dónde está su documentación |
| **Qué entrega** | Lo que tenía, adentro de la plataforma, con su forma reconocida |
| **Reglas que debe respetar** | `RN-2` traer no modifica el proyecto de origen |
| **Depende de** | F-001, F-011 |
| **Terminada cuando** | `CA-1` los documentos que siguen un molde conocido quedan adentro, con su tipo · `CA-2` el proyecto de origen queda intacto · `CA-3` traer dos veces no duplica |
| **Qué necesita construirse** | Pantalla y lógica |
| **Prioridad** | Alta |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | Es lo que hace usable la plataforma desde el primer día: sin esto arranca vacía |

### Reportar qué de lo traído no sigue ningún molde

| Campo | Valor |
|---|---|
| **Identificador** | `F-028` |
| **De qué se trata** | Decir qué documentos no se reconocieron al traer un proyecto, y por qué |
| **Para qué sirve** | Que nada se pierda en silencio ni se transforme a la fuerza |
| **Parte del sistema** | Importación |
| **Quién la usa** | El usuario |
| **Qué recibe** | Lo que quedó sin reconocer |
| **Qué entrega** | La lista, con dónde está cada uno |
| **Reglas que debe respetar** | `RN-4` no se afirma sobre lo que no se leyó |
| **Depende de** | F-027 |
| **Terminada cuando** | `CA-1` lo no reconocido queda listado con su ruta · `CA-2` nada se transforma sin que el usuario lo diga · `CA-3` si todo se reconoció, se dice |
| **Qué necesita construirse** | Pantalla y lógica |
| **Prioridad** | Media |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | Lo que no se reconoce suele ser lo más valioso: las notas que nadie escribió con molde |

### Avisar lo que se desvía

| Campo | Valor |
|---|---|
| **Identificador** | `F-029` |
| **De qué se trata** | Decirle al usuario lo que se salió de lo acordado: deuda vencida, historia sin fase, respaldo sin probar |
| **Para qué sirve** | Que enterarse no dependa de ir a mirar |
| **Parte del sistema** | Avisos |
| **Quién la usa** | El usuario |
| **Qué recibe** | Lo que la plataforma ya tiene guardado |
| **Qué entrega** | Los avisos, ordenados por lo que más duele |
| **Reglas que debe respetar** | `RN-4` un aviso dice qué lo disparó |
| **Depende de** | F-003, F-018 |
| **Terminada cuando** | `CA-1` una deuda vencida se avisa · `CA-2` cada aviso dice qué lo disparó y dónde mirar · `CA-3` un aviso atendido no vuelve a aparecer |
| **Qué necesita construirse** | Lógica y pantalla |
| **Prioridad** | Media |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | Demasiados avisos se vuelven ruido, y el ruido se ignora completo |

### Reportar cómo va cada proyecto

| Campo | Valor |
|---|---|
| **Identificador** | `F-030` |
| **De qué se trata** | Mostrar el avance, la deuda y el cumplimiento de cada proyecto, y compararlos |
| **Para qué sirve** | Decidir dónde poner el tiempo con datos, y no con impresión |
| **Parte del sistema** | Avisos |
| **Quién la usa** | El usuario |
| **Qué recibe** | Lo guardado de todos los proyectos |
| **Qué entrega** | El reporte, con la misma medida para todos |
| **Reglas que debe respetar** | `RN-5` lo que no está verificado se reporta así |
| **Depende de** | F-003 |
| **Terminada cuando** | `CA-1` se ve el avance de cada proyecto con la misma medida · `CA-2` se ve la deuda declarada y la vencida · `CA-3` un proyecto sin datos aparece así, no en cero |
| **Qué necesita construirse** | Pantalla y lógica |
| **Prioridad** | Media |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | Comparar proyectos distintos con la misma medida engaña si no se dice qué mide |

### Tapar toda credencial antes de escribirla

| Campo | Valor |
|---|---|
| **Identificador** | `F-031` |
| **De qué se trata** | Que ninguna clave quede escrita en un documento, en el registro ni en la base |
| **Para qué sirve** | Que una clave pegada en una conversación no quede para siempre |
| **Parte del sistema** | Seguridad |
| **Quién la usa** | El usuario, sin hacer nada |
| **Qué recibe** | El texto que se va a guardar, antes de guardarlo |
| **Qué entrega** | El mismo texto con la clave tapada, y el nombre de la variable intacto |
| **Reglas que debe respetar** | `RN-9` una credencial no se escribe, no se registra y no se guarda |
| **Depende de** | F-018 |
| **Terminada cuando** | `CA-1` una clave entre comillas queda tapada · `CA-2` una tecleada sin comillas también · `CA-3` una palabra que solo parece clave queda intacta |
| **Qué necesita construirse** | Lógica |
| **Prioridad** | Alta |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | Es el único daño de esta lista que no se puede deshacer |

### Medir el tiempo que se gasta revisando

| Campo | Valor |
|---|---|
| **Identificador** | `F-032` |
| **De qué se trata** | Registrar cuánto tiempo dedica el usuario a revisar lo entregado, y compararlo en el tiempo |
| **Para qué sirve** | Saber si el proyecto cumplió su objetivo, en vez de suponerlo |
| **Parte del sistema** | Medición |
| **Quién la usa** | El usuario |
| **Qué recibe** | Lo que dura cada revisión, y cuántas correcciones se repiten |
| **Qué entrega** | La comparación entre el antes y el después |
| **Reglas que debe respetar** | Medir no puede costar más que lo que ahorra |
| **Depende de** | F-018, F-030 |
| **Terminada cuando** | `CA-1` hay una medición inicial contra la cual comparar · `CA-2` medir no obliga al usuario a anotar nada a mano |
| **Qué necesita construirse** | Lógica |
| **Prioridad** | Baja |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | La medición inicial debió tomarse antes de empezar y no se tomó: sin ella pierde la mitad del valor |

### Guardar las conversaciones donde se pueda buscar

| Campo | Valor |
|---|---|
| **Identificador** | `F-033` |
| **De qué se trata** | Que las conversaciones que ya se escriben entren a la plataforma y se puedan buscar sin abrir archivo por archivo |
| **Para qué sirve** | Es la fuente de `F-034`: sin poder buscar en ellas, no hay nada que contar |
| **Parte del sistema** | Medición |
| **Quién la usa** | El sistema solo, cada vez que una sesión escribe |
| **Qué recibe** | El mensaje del usuario y la respuesta del agente, tal como quedaron escritos |
| **Qué entrega** | La conversación indexada, con su fecha y su sesión |
| **Reglas que debe respetar** | `RN-9` nada guardado incluye credenciales. Ya se cumple: lo que se escribe viene tapado desde el enganche del histórico |
| **Depende de** | F-001 |
| **Terminada cuando** | `CA-1` lo que una sesión conversó se encuentra buscando una palabra suya · `CA-2` el texto sigue siendo la fuente, y el índice se puede borrar y rehacer · `CA-3` ninguna credencial aparece en lo indexado |
| **Qué necesita construirse** | Lógica y almacenamiento |
| **Prioridad** | Media |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | **No es la auditoría.** La auditoría guarda qué se hizo; esto guarda qué se conversó, y `RN-4` de ese módulo sigue diciendo que la conversación no entra allá |

### Decir qué correcciones se repiten

| Campo | Valor |
|---|---|
| **Identificador** | `F-034` |
| **De qué se trata** | Contar qué le tocó repetir al usuario, y mostrarlo ordenado de lo más repetido a lo menos |
| **Para qué sirve** | Una corrección que se repite no es un descuido del usuario: es una regla que falta, y hoy ese patrón se pierde |
| **Parte del sistema** | Medición |
| **Quién la usa** | El usuario |
| **Qué recibe** | El período que se quiere mirar |
| **Qué entrega** | Las correcciones más repetidas, cada una con cuántas veces y en qué sesiones |
| **Reglas que debe respetar** | Mostrar el patrón, nunca decidir la regla: eso lo sigue decidiendo el usuario por la cadena |
| **Depende de** | F-033 |
| **Terminada cuando** | `CA-1` se pide un período y salen las correcciones más repetidas · `CA-2` cada una dice cuántas veces y en qué sesiones · `CA-3` dos formas distintas de decir lo mismo cuentan como una · `CA-4` si no hay nada repetido, se dice, en vez de rellenar |
| **Qué necesita construirse** | Pantalla y lógica |
| **Prioridad** | Media |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | **`CA-3` es lo difícil.** Agrupar frases parecidas no es contar palabras iguales, y hacerlo sin depender de nada instalado aparte es la parte que puede no salir. Le da además a `F-032` la fuente que le faltaba: hoy dice que recibe cuántas correcciones se repiten, y nada las cuenta |

### Administrar un proyecto ya conectado

| Campo | Valor |
|---|---|
| **Identificador** | `F-035` |
| **De qué se trata** | Desconectar un proyecto, renombrarlo y corregir la versión de reglas que declara |
| **Para qué sirve** | Que conectar tenga reversa. Sin esto, un proyecto conectado con el nombre o la ruta equivocados queda así para siempre |
| **Parte del sistema** | Proyectos |
| **Quién la usa** | El usuario |
| **Qué recibe** | Qué proyecto, y qué se le cambia |
| **Qué entrega** | El proyecto cambiado, o fuera de la lista si se desconectó. Su documentación se queda |
| **Reglas que debe respetar** | `RN-2` ningún cambio de estado sin aprobación: las tres piden confirmación · `RN-9` la acción queda en la auditoría |
| **Depende de** | F-001 |
| **Terminada cuando** | `CA-1` desconectar saca el proyecto de la lista y **no borra su documentación** · `CA-2` renombrar cambia el nombre y **no mueve su carpeta** · `CA-3` corregir la versión declarada la vuelve a comprobar contra las publicadas · `CA-4` las tres piden confirmación y quedan en la auditoría |
| **Qué necesita construirse** | Pantalla, lógica y almacenamiento |
| **Prioridad** | Alta |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | **Ya estaba decidida sin estar pedida.** La especificación del módulo dice desde el 2026-08-25 cómo se comporta desconectar, en su §7 y su §12, y ninguna funcionalidad lo pedía: ninguna fase lo iba a construir. Desconectar **no borra**, y esa decisión ya está tomada |

### Entrar con cuenta y contraseña

| Campo | Valor |
|---|---|
| **Identificador** | `F-036` |
| **De qué se trata** | Que la plataforma pida cuenta y contraseña, y que ninguna pantalla responda sin haber entrado |
| **Para qué sirve** | Que se sepa quién hizo cada cosa, y que no entre cualquiera que alcance el puerto |
| **Parte del sistema** | Acceso |
| **Quién la usa** | El usuario y el agente |
| **Qué recibe** | La cuenta y la contraseña |
| **Qué entrega** | La sesión abierta, o el rechazo |
| **Reglas que debe respetar** | `RN-2` la contraseña se guarda cifrada y nunca en claro · `RN-7` un intento fallido no dice cuál de los dos datos estuvo mal |
| **Depende de** | F-001 |
| **Terminada cuando** | `CA-1` ninguna pantalla responde sin haber entrado · `CA-2` entrar lleva a donde se iba, no a la portada · `CA-3` un intento fallido no dice cuál dato estuvo mal |
| **Qué necesita construirse** | Pantalla, lógica y almacenamiento |
| **Prioridad** | Alta |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | **Estaba definida y aplazada, no descartada.** La sección 6 del análisis ya decía qué puede hacer cada actor; el diseño lo aplazó «mientras haya un solo usuario» y advirtió que con dos es una falla. El usuario levantó el aplazamiento el 2026-09-02 |

### Separar lo que cada grupo puede hacer

| Campo | Valor |
|---|---|
| **Identificador** | `F-037` |
| **De qué se trata** | Dos grupos, `usuario` y `agente`, con lo que cada uno puede hacer |
| **Para qué sirve** | Que la aprobación siga siendo de una persona, y no un trámite que el agente se dé a sí mismo |
| **Parte del sistema** | Acceso |
| **Quién la usa** | El usuario |
| **Qué recibe** | La cuenta que pide hacer algo |
| **Qué entrega** | El permiso, o el rechazo diciendo qué permiso falta |
| **Reglas que debe respetar** | `RN-4` el agente no aprueba, no publica versiones, no deroga reglas y no administra cuentas · `RN-5` una orden solo acepta una cuenta que exista |
| **Depende de** | F-036 |
| **Terminada cuando** | `CA-1` el agente no puede aprobar, publicar ni derogar · `CA-2` el rechazo dice qué permiso falta · `CA-3` una orden con una cuenta que no existe se rechaza |
| **Qué necesita construirse** | Lógica |
| **Prioridad** | Alta |
| **Estado** | Construida |
| **Verificado** | Verificada |
| **Lo que hay que tener en cuenta** | **De los cuatro actores del análisis, solo dos son cuentas.** Un proyecto administrado no es una persona que entre, y quien recibe un proyecto tiene prohibido entrar. Construir cuatro grupos habría sido construir de más |

## Lo que todavía no se sabe si entra

| # | Funcionalidad candidata | De qué se trata | Estado |
|---|---|---|---|
| C-1 | Buscar por parecido en la memoria | Encontrar lo guardado aunque se nombre distinto | **Por confirmar** (P-1) |
| C-2 | Roles y permisos | Que más de una persona use la plataforma con distintos alcances | **Por confirmar** (P-2) |
| C-3 | Que la plataforma escriba en el repositorio del proyecto | Dejarle allá una copia generada de su documentación al entregar | **Por confirmar** (P-3) |
| C-4 | Alimentar la memoria con lo que el usuario estudia por fuera | Que lo aprendido en otro lado entre al sistema | **Por confirmar** (P-4) |

## Preguntas: las contesta el usuario

- **P-1 · ¿Entra C-1?** Buscar por parecido pide una dependencia de terceros, y eso choca con correr sin instalar nada. Propuesta: no entra mientras esa restricción siga vigente.
- **P-2 · ¿Entra C-2?** Hoy hay un solo usuario. Sumar roles trae permisos, credenciales y responsabilidad sobre datos ajenos. Propuesta: queda como futura hasta que alguien más la use.
- **P-3 · ¿Entra C-3?** Un proyecto entregado a un cliente se queda sin su historia si nada se le deja. Propuesta: entra, pero como salida generada, nunca como fuente.
- **P-4 · ¿Entra C-4?** Es la idea que el usuario ya tenía anotada. Propuesta: futura, hasta que la memoria del trabajo esté verificada.

## Qué pasa cuando esto se apruebe

1. El planteamiento se revisa para que diga esto, y no lo que alguien hubiera supuesto antes.
2. El trabajo se parte en bloques a partir de esta lista, y cada bloque dice qué funcionalidades cubre por su identificador.
3. Cada «Terminada cuando» se vuelve el criterio de aceptación de su historia, y de ahí salen las pruebas.
4. Cada prueba que salga bien llena su casilla de «Verificado». Ahí, y solo ahí, se sabe qué está hecho.
5. La lista se va volviendo el manual del producto, sin volver a escribirla.
