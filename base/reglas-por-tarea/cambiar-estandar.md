# Reglas de la tarea `cambiar-estandar`

Lo escribe `validadores/mapa_tareas.py` desde las reglas de `base/`: no se edita a mano. Son las reglas que [base/mapa-de-tareas.md](../mapa-de-tareas.md) pone bajo esta tarea, completas. Las que llevan *opt-in* rigen solo si el proyecto encendió su capítulo en el punto 5.1 de su `CLAUDE.md`.

## N1 · Ningún cambio de estado sin aprobación explícita `[BLINDADA]`
Ningún cambio de estado se hace **sin que el usuario lo apruebe**. Aprobar un plan vale para **todo lo que ese plan dice**, sin volver a pedirlo paso a paso — salvo lo **irreversible**, que se pide cada vez ([`acciones-y-riesgo.md`](../00-identidad-y-rol/acciones-y-riesgo.md)).
```
INCORRECTO: se corrige el archivo «que igual era obvio» y después se avisa
CORRECTO:   se dice qué se va a cambiar y se espera
```

Fuente: [00·N1](../00-nucleo-blindado.md#n1--ningún-cambio-de-estado-sin-aprobación-explícita-blindada)

## C1 · Avisa antes de tocar
Antes de cambiar un archivo, di **qué** cambias y **por qué**, y espera el sí (depende de [`00·N1`](../00-nucleo-blindado.md#n1--ningún-cambio-de-estado-sin-aprobación-explícita-blindada)).
```
INCORRECTO: editar sin avisar
CORRECTO:   "Agrego la verificación de permiso en X porque Z. ¿Procedo?"
```

Fuente: [01·C1](../01-conducta.md#c1--avisa-antes-de-tocar)

## C10 · Lo que el usuario pide dos veces se propone como regla
Además de hacer lo pedido, se mira si el pedido trae **un criterio que valga para la próxima vez**. Si lo trae, se **propone escribirlo como regla antes de cerrar la tarea**, mostrando el cambio exacto para que se pueda revisar y no haya que creer en la palabra. No aplica al pedido puntual que no deja patrón.
```
INCORRECTO: se corrige el nombre de la columna y se sigue; a la semana se
            vuelve a corregir lo mismo en otra tabla
CORRECTO:   se corrige, y se propone la convención escrita, con el cambio a la vista
```

Fuente: [01·C10](../01-conducta.md#c10--lo-que-el-usuario-pide-dos-veces-se-propone-como-regla)

## C26 · La regla que serviría en otra empresa va a la base común
Antes de escribir una regla se decide **dónde vive**, con una sola pregunta: *«¿tendría sentido en otra empresa, con otro lenguaje y otro negocio?»*. Si sí, va a la base común y **no se duplica** en el proyecto; si no, es del proyecto y se queda ahí (extiende [`01·C10`](../01-conducta.md#c10--lo-que-el-usuario-pide-dos-veces-se-propone-como-regla)).
```
INCORRECTO: «toda fase tiene su historia madre» se escribe en el catálogo
            del proyecto, donde solo lo ve ese proyecto
CORRECTO:   esa va a la base común; la que dice qué identificador aprueba
            se queda en el proyecto
```

Fuente: [01·C26](../01-conducta.md#c26--la-regla-que-serviría-en-otra-empresa-va-a-la-base-común)

## DOC10 · Registra en el catálogo del proyecto toda regla propia
Toda regla que solo vale para este proyecto se escribe en su catálogo, cuya ruta declara la capa 3, numerada `P1`, `P2` y así, para poder citarla; cada `P` que nace o se endurece deja su señal ([`DOC5`](../13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)). La que se promueve a `base/` conserva solo su matiz y enlaza a la regla base.
```
INCORRECTO: el usuario dice "de aquí en adelante siempre X" · se aplica · nada
            queda escrito · la próxima sesión no lo sabe
CORRECTO:   se aplica + se crea la `P` en el catálogo + se registra su señal
```

Fuente: [13·DOC10](../13-documentacion/reglas/DOC10-registra-en-el-catalogo-del-proyecto-toda-regla-propia.md#doc10--registra-en-el-catálogo-del-proyecto-toda-regla-propia)

## M1 · La jerarquía tiene cuatro niveles y un solo orden
Un nivel **nunca** contradice al de arriba. La capa 3 puede ajustar una convención; ninguna capa toca el núcleo. Los cuatro niveles y qué ajusta cada uno: [`base.md`](../20-meta-reglas/base.md).
```
INCORRECTO: el proyecto declara "aquí sí se puede hacer push sin pedir" (ajusta 00·N2)
CORRECTO:   el proyecto declara "los commits van en inglés" (ajusta 09·G2)
```

Fuente: [20·M1](../20-meta-reglas/reglas/M1-la-jerarquia-tiene-cuatro-niveles-y-un-solo-orden.md#m1--la-jerarquía-tiene-cuatro-niveles-y-un-solo-orden)

## M10 · Todo cambio de regla se versiona y se registra
Cambiar `base/` o `plantillas/` obliga, **en el mismo movimiento**, a sumar entrada en `CHANGELOG.md` con su tipo y a subir `VERSION`. Los tipos, qué más hay que revisar y la retroactividad: [`base.md`](../20-meta-reglas/base.md).
```
INCORRECTO: se afina la redacción de una regla y el CHANGELOG queda "para después"
CORRECTO:   el cambio, su entrada en el CHANGELOG y la subida de VERSION van en el mismo movimiento
```

Fuente: [20·M10](../20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md#m10--todo-cambio-de-regla-se-versiona-y-se-registra)

## M11 · Las reglas no se borran: se derogan
Una regla que deja de regir se **marca** `[DEROGADA en X.Y.Z → ver ID]`, no se elimina: se conserva su texto debajo de la marca y su ID **no se reutiliza**. Por qué: [`base.md`](../20-meta-reglas/base.md).
```
INCORRECTO: la regla ya no rige → se borra del capítulo
CORRECTO:   se marca [DEROGADA en X.Y.Z → ver ID] y se conserva su texto debajo
```

Fuente: [20·M11](../20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md#m11--las-reglas-no-se-borran-se-derogan)

## M12 · Antes de crear una regla, buscar — la duplicación es el defecto más caro
Antes de escribir una regla nueva, **buscar por concepto** en `base/` y leer entero el capítulo dueño. Si ya existe se afina; si casi existe se extiende; crear es lo último. El orden completo de búsqueda y de decisión: [`base.md`](../20-meta-reglas/base.md).
```
INCORRECTO: se escribe una regla nueva sin abrir el capítulo dueño, y termina diciendo lo que ya decía otra
CORRECTO:   se busca por concepto → ya existe → se afina la que está
```

Fuente: [20·M12](../20-meta-reglas/reglas/M12-antes-de-crear-una-regla-buscar-la-duplicacion-es-el-defecto-mas-caro.md#m12--antes-de-crear-una-regla-buscar--la-duplicación-es-el-defecto-más-caro)

## M13 · Lo que no es regla del estándar tiene su propio sitio
Antes de escribir en `base/`, verificar que ahí es donde va: solo la regla que aplica a **cualquier** proyecto. Dónde va todo lo demás: [`base.md`](../20-meta-reglas/base.md).
```
INCORRECTO: la convención de un equipo entra en base/ como si aplicara a cualquier proyecto
CORRECTO:   entra en el catálogo de ese proyecto; base/ solo lleva lo universal
```

Fuente: [20·M13](../20-meta-reglas/reglas/M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md#m13--lo-que-no-es-regla-del-estándar-tiene-su-propio-sitio)

## M14 · Ninguna regla nace fuera del procedimiento
Toda regla nueva —y toda reescritura que cambie **qué exige** una existente— recorre los nueve pasos del procedimiento de este capítulo, cuyo cierre es su [checklist](../20-meta-reglas/checklist.md) en **CUMPLE**. Sin ese cierre la regla no se publica: se corrige o se retira.
```
INCORRECTO: la regla se escribe, se lee bien, y entra al capítulo
CORRECTO:   se escribe, se responde su checklist, y entra solo si da CUMPLE
```

Fuente: [20·M14](../20-meta-reglas/reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md#m14--ninguna-regla-nace-fuera-del-procedimiento)

## M15 · Toda cita a otra regla lleva su enlace
Citar una regla por su ID no basta: la cita se escribe como enlace al sitio exacto donde vive esa regla — el archivo, y el ancla de su encabezado si comparte archivo con otras (extiende [`M4`](../20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md), que fija el ID y la forma `NN·ID`). Una cita que obliga a salir a buscar es una dependencia que nadie comprueba.
```
INCORRECTO: No se saltan (`00` · N3).
CORRECTO:   No se saltan ([`00·N3`](../00-nucleo-blindado.md#n3--no-romper-cosas-para-pasar-un-obstáculo-blindada)).
```

Fuente: [20·M15](../20-meta-reglas/reglas/M15-toda-cita-a-otra-regla-lleva-su-enlace.md#m15--toda-cita-a-otra-regla-lleva-su-enlace)

## M16 · Toda regla de proyecto nombra la regla de base que concreta
Cada regla del catálogo de un proyecto ([`13·DOC10`](../13-documentacion/reglas/DOC10-registra-en-el-catalogo-del-proyecto-toda-regla-propia.md)) declara, con su enlace ([`M15`](../20-meta-reglas/reglas/M15-toda-cita-a-otra-regla-lleva-su-enlace.md)), la regla de `base/` cuyo criterio concreta o endurece (extiende [`M1`](../20-meta-reglas/reglas/M1-la-jerarquia-tiene-cuatro-niveles-y-un-solo-orden.md)). Si ninguna la cubre, la de base se escribe primero; hasta entonces la de proyecto no se publica.
```
INCORRECTO: P4 · El catálogo se cachea 10 minutos · Por qué: lo acordó el equipo
CORRECTO:   P4 · El catálogo se cachea 10 minutos · Respaldo 06·R4: fija aquí el tiempo
```

Fuente: [20·M16](../20-meta-reglas/reglas/M16-toda-regla-de-proyecto-nombra-la-regla-de-base-que-concreta.md#m16--toda-regla-de-proyecto-nombra-la-regla-de-base-que-concreta)

## M17 · La entrada del registro abre en castellano llano
La entrada de `CHANGELOG.md` abre con **qué cambió y por qué**, en dos frases que se entienden sin conocer el proyecto: sin identificador de regla, sin ruta y sin las palabras de la casa (extiende [`20·M10`](../20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)).
El detalle va debajo, con sus enlaces, para quien los necesite.
```
INCORRECTO: **MENOR** — la fila 12 del checklist pide ejemplo en `plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md`
CORRECTO:   Al anotar que una prueba pasó ahora hay que decir con qué se probó.
            Antes se anotaba solo «aprobado», y así nadie podía repetirla.
```

Fuente: [20·M17](../20-meta-reglas/reglas/M17-la-entrada-del-registro-abre-en-castellano-llano.md#m17--la-entrada-del-registro-abre-en-castellano-llano)

## M18 · Lo compartido se lee un instante antes de escribirlo
Todo archivo que otra sesión puede estar tocando —`VERSION`, el registro de cambios, un índice, una numeración— se **relee en el momento de escribirlo**, nunca desde lo que se leyó al abrir (extiende [`20·M10`](../20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)). Decidirlo antes es apostar a que nadie más guarde primero.
```
INCORRECTO: a media sesión se sube VERSION a 10.0.0 y se sigue trabajando dos horas
CORRECTO:   el número se lee de lo guardado y se sube en el mismo movimiento
```

Fuente: [20·M18](../20-meta-reglas/reglas/M18-lo-compartido-se-lee-un-instante-antes-de-escribirlo.md#m18--lo-compartido-se-lee-un-instante-antes-de-escribirlo)

## M19 · La regla se automatiza cuando ya se cumple a mano
Antes de construir el programa que comprueba una regla (extiende [`20·M9`](../20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md)), se deja escrito si hoy se cumple a mano, cuántas veces se incumplió y por qué, y cuántas falsas alarmas daría. Si se incumple porque está mal escrita, se corrige la regla; si lo único que falla es acordarse, se automatiza ya.
```
INCORRECTO: la regla se incumple seis veces porque exige dos cosas; se le construye
            el validador tal cual, y ahora falla sola en cada commit
CORRECTO:   se mira por qué se incumplió → estaba mal escrita → se parte en dos, y el
            validador se construye sobre la regla corregida
```

Fuente: [20·M19](../20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md#m19--la-regla-se-automatiza-cuando-ya-se-cumple-a-mano)

## M2 · Un tema, un capítulo, un dueño
Cada dominio tiene **un** archivo `NN-nombre.md` y ese archivo es la **fuente única** de su tema. Si una regla de otro capítulo necesita hablar del mismo tema, **enlaza**, no repite. El preámbulo del `00` comparte número con el núcleo porque lo anexa: no es otro capítulo ni otro dueño.
```
INCORRECTO: la regla de índices se escribe en el capítulo de datos y otra vez en el de rendimiento
CORRECTO:   vive en el de rendimiento; el de datos la enlaza
```

Fuente: [20·M2](../20-meta-reglas/reglas/M2-un-tema-un-capitulo-un-dueno.md#m2--un-tema-un-capítulo-un-dueño)

## M20 · Antes de publicar una versión se barre lo que se pidió dos veces
Antes de publicar una versión se relee el tramo cerrado (resúmenes, pendientes y señales) y lo que el usuario pidió **dos veces o más** se escribe en el barrido de candidatas, con su salida: cubierta, regla nueva, afinar una, o no es regla (extiende [`01·C10`](../01-conducta.md#c10--lo-que-el-usuario-pide-dos-veces-se-propone-como-regla)). Molde: [`plantillas/candidatas-a-regla.md`](../../plantillas/candidatas-a-regla.md).
```
INCORRECTO: el criterio se pidió en tres sesiones, nadie lo notó en el momento,
            y a la cuarta el usuario lo corrige otra vez
CORRECTO:   al cerrar la versión se barre el tramo, sale la candidata con las
            tres veces que se pidió, y el usuario decide si se escribe
```

Fuente: [20·M20](../20-meta-reglas/reglas/M20-antes-de-publicar-una-version-se-barre-lo-que-se-pidio-dos-veces.md#m20--antes-de-publicar-una-versión-se-barre-lo-que-se-pidió-dos-veces)

## M3 · La base es agnóstica: sin stack y sin dominio
Una regla de capa 1 o 2 sirve a **cualquier** proyecto: no nombra lenguaje, framework, motor de base de datos, nube, sector ni cliente. Lo concreto se declara en capa 3 y la regla lo referencia como concepto.
Si una regla no se puede escribir sin nombrar una tecnología, **no es regla de la base**: es capa 3.
```
INCORRECTO: "usar pytest con cobertura mínima de 80%"
CORRECTO:   "toda unidad entregada lleva pruebas automáticas; el marco y el
             umbral los declara el proyecto (.agente/stack.md)"
```

Fuente: [20·M3](../20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md#m3--la-base-es-agnóstica-sin-stack-y-sin-dominio)

## M4 · Cada regla tiene un identificador único, estable y prefijado
Formato `<PREFIJO><n>`: prefijo de letras del capítulo más consecutivo. El prefijo es **exclusivo** de un capítulo. **El ID no cambia nunca** — ni al reescribir la regla, ni al moverla, ni al cambiarle el título. Cómo se cita y por qué no cambia: [`base.md`](../20-meta-reglas/base.md).
```
INCORRECTO: se borra la R3 y se corre la R4 a R3 "para dejarlo ordenado"
CORRECTO:   el hueco se queda; la regla nueva toma el siguiente consecutivo libre
```

Fuente: [20·M4](../20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md#m4--cada-regla-tiene-un-identificador-único-estable-y-prefijado)

## M5 · Toda regla se escribe en el mismo formato
Toda regla se escribe con el mismo molde: encabezado `## <PREFIJO><n> · <título imperativo>` con su marca si lleva, cuerpo de una a cuatro líneas en presente e imperativo, y ejemplo. El molde con sus cinco reglas de formato: [`base.md`](../20-meta-reglas/base.md); parte por parte: [`estructura-regla.md`](../20-meta-reglas/estructura-regla.md).
```
INCORRECTO: <el error concreto que se ve en la práctica>
CORRECTO:   <qué se hace en su lugar>
```

Fuente: [20·M5](../20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md#m5--toda-regla-se-escribe-en-el-mismo-formato)

## M6 · Ante un conflicto, el desempate es este y en este orden
Ante un choque entre dos reglas, el desempate se resuelve por el [orden del anexo](../20-meta-reglas/desempate.md), de arriba abajo, parando en el primero que aplique. Está prohibido elegir en silencio o inventar un tercer camino: si sigue empatado es un defecto del estándar, así que se **pausa**, se reporta y se arregla la regla.
```
INCORRECTO: dos reglas se contradicen → elijo la que me deja avanzar y sigo
CORRECTO:   reporto "01·C3 y 02·F7 chocan en este caso" y espero la decisión
```

Fuente: [20·M6](../20-meta-reglas/reglas/M6-ante-un-conflicto-el-desempate-es-este-y-en-este-orden.md#m6--ante-un-conflicto-el-desempate-es-este-y-en-este-orden)

## M7 · Las dependencias entre reglas se declaran, y solo hay tres
Una regla que se apoya en otra lo declara **en su cuerpo, entre paréntesis**, con una de tres formas: `extiende ID` · `depende de ID` · `deroga ID`. No hay una cuarta. Qué significa cada una y sus dos prohibiciones: [`base.md`](../20-meta-reglas/base.md).
```
INCORRECTO: la regla cierra con un párrafo en prosa que "se relaciona con" media docena de reglas
CORRECTO:   (extiende 09·G6), en el cuerpo y entre paréntesis
```

Fuente: [20·M7](../20-meta-reglas/reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md#m7--las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres)

## M8 · La excepción se escribe dentro de la regla que la admite
Una excepción no vive en otro documento ni en el chat: es **parte del texto de la regla**, y declara tres cosas — **condición** (cuándo aplica), **límite** (hasta dónde) y **quién la autoriza**. Qué no es excepción y qué hacer ante una no escrita: [`base.md`](../20-meta-reglas/base.md).
```
INCORRECTO: "el test tarda mucho, esta vez lo salto y sigo"
CORRECTO:   reporto el costo, propongo el arreglo y espero; si se acepta un
            criterio nuevo, entra escrito en la regla
```

Fuente: [20·M8](../20-meta-reglas/reglas/M8-la-excepcion-se-escribe-dentro-de-la-regla-que-la-admite.md#m8--la-excepción-se-escribe-dentro-de-la-regla-que-la-admite)

## M9 · Toda regla declara si es validable
Al escribir la regla, responder **¿puede un script decir sí/no sin opinar?** y registrar la respuesta en `validadores/reglas-validables.md`. Qué se sigue de cada respuesta: [`base.md`](../20-meta-reglas/base.md).
```
INCORRECTO: la regla se escribe y nadie decide si un script puede comprobarla
CORRECTO:   se responde al escribirla y queda registrada en validadores/reglas-validables.md
```

Fuente: [20·M9](../20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md#m9--toda-regla-declara-si-es-validable)
