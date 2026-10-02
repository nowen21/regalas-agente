# Reglas de la tarea `escribir-documento`, parte 2 de 2

Lo escribe `validadores/mapa_tareas.py` desde las reglas de `base/`: no se edita a mano. Son las reglas que [base/mapa-de-tareas.md](../mapa-de-tareas.md) pone bajo esta tarea, completas. Las que llevan *opt-in* rigen solo si el proyecto encendió su capítulo en el punto 5.1 de su `CLAUDE.md`.

## F27 · Cada punto dice de qué punto del anterior sale
Cada punto de un documento de la cadena lleva «Sale de» con el punto del documento anterior: el pendiente, su hallazgo; la conclusión del análisis, su turno; el criterio de la HU, su punto de «Lo que se tiene que hacer». Lo que no tiene origen no entra (extiende [`02·F18`](../02-flujo-de-trabajo/reglas/F18-deriva-el-plan-de-los-ca-aprobados-no-de-la-proactividad.md)).
```
INCORRECTO: la HU trae un CA-04 sin «Sale de», porque «se veía necesario»
CORRECTO:   el CA-04 dice «Sale de: análisis 6, punto 2», y ese punto existe
            en «Lo que se tiene que hacer» del análisis 6
```

Fuente: [02·F27](../02-flujo-de-trabajo/reglas/F27-cada-punto-dice-de-que-punto-del-anterior-sale.md#f27--cada-punto-dice-de-qué-punto-del-anterior-sale)

## F28 · El cambio se aplica donde nace y baja en orden
Si cambia la necesidad, el cambio se escribe primero en el documento donde nace, aunque sea el planteamiento, y baja en orden por la épica, la HU, la especificación y el plan. Ningún documento de abajo cambia antes que el de arriba (extiende [`02·F0`](../02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md)).
```
INCORRECTO: el usuario cambia lo que necesita y se corrige el plan; la HU
            sigue diciendo lo de antes
CORRECTO:   se corrige la HU, después la especificación y al final el plan
```

Fuente: [02·F28](../02-flujo-de-trabajo/reglas/F28-el-cambio-se-aplica-donde-nace-y-baja-en-orden.md#f28--el-cambio-se-aplica-donde-nace-y-baja-en-orden)

## F8 · Edita solo los archivos que el plan aprobado declara
Se editan únicamente los archivos de la tabla del plan aprobado ([`02·F14`](../02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md), pregunta 9). Descubrir a mitad que hace falta otro **detiene la ejecución**: se pausa, se reporta, se propone ampliar el plan y se espera el OK. Que el cambio sea obvio no autoriza; la aprobación sí ([`base.md`](../02-flujo-de-trabajo/base.md)).
```
INCORRECTO: durante la ejecución el agente descubre que también hay que editar el
            archivo Y → lo edita en el mismo commit "porque era necesario"
CORRECTO:   descubre Y → PAUSA + reporta + propone ampliar el plan → usuario
            aprueba (o difiere Y a otra fase) → sigue con el plan actualizado
```

Fuente: [02·F8](../02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md#f8--edita-solo-los-archivos-que-el-plan-aprobado-declara)

## DOC1 · Persiste el trabajo de cada unidad completada
Al cerrar una unidad, deja en documentación versionada **qué se planeó**, **qué se probó** —incluidas las verificaciones manuales que el entorno automático no cubre ([`08·T4`](../08-pruebas.md#t4--protege-los-datos-reales-al-probar))— y **qué quedó**: cómo usarlo, puntos de entrada, enlaces al código. El chat no sustituye los archivos.
```
INCORRECTO: implementar, mostrar todo en el chat y cerrar
CORRECTO:   implementar + persistir plan, pruebas y resultado
```

Fuente: [13·DOC1](../13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md#doc1--persiste-el-trabajo-de-cada-unidad-completada)

## DOC10 · Registra en el catálogo del proyecto toda regla propia
Toda regla que solo vale para este proyecto se escribe en su catálogo, cuya ruta declara la capa 3, numerada `P1`, `P2` y así, para poder citarla; cada `P` que nace o se endurece deja su señal ([`DOC5`](../13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)). La que se promueve a `base/` conserva solo su matiz y enlaza a la regla base.
```
INCORRECTO: el usuario dice "de aquí en adelante siempre X" · se aplica · nada
            queda escrito · la próxima sesión no lo sabe
CORRECTO:   se aplica + se crea la `P` en el catálogo + se registra su señal
```

Fuente: [13·DOC10](../13-documentacion/reglas/DOC10-registra-en-el-catalogo-del-proyecto-toda-regla-propia.md#doc10--registra-en-el-catálogo-del-proyecto-toda-regla-propia)

## DOC13 · Registra cada módulo nuevo en el catálogo de módulos
Un módulo nuevo —dominio funcional propio, con su prefijo de rutas o su especificación separada— se registra en el catálogo de módulos **antes de cerrar** la unidad que lo creó, con lo que pide [`plantillas/catalogo-modulos.md`](../../plantillas/catalogo-modulos.md). No cuentan la fase de un módulo que ya existe, el arreglo interno ni el componente hijo.
```
INCORRECTO: se crea un módulo · las sesiones siguientes asumen que el proyecto
            "solo tiene X e Y" porque el nuevo no está en el catálogo
CORRECTO:   al cerrar la unidad que lo creó, su entrada queda en el catálogo
```

Fuente: [13·DOC13](../13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md#doc13--registra-cada-módulo-nuevo-en-el-catálogo-de-módulos)

## DOC14 · Enlaza cada `.md` con ruta legible y destino relativo
Toda referencia de un `.md` a otro `.md` del proyecto es un enlace de dos partes: como **texto**, la ruta completa desde la raíz —para saber dónde vive sin abrirlo—; como **destino**, la ruta relativa desde el archivo actual.
```
INCORRECTO: [plan_trabajo.md](../otra/carpeta/plan_trabajo.md)
            — el texto no dice dónde vive
INCORRECTO: `documentacion/area/unidad/plan_trabajo.md`
            — dice dónde vive pero no se puede abrir
CORRECTO:   [documentacion/area/unidad/plan_trabajo.md](../area/unidad/plan_trabajo.md)
```

Fuente: [13·DOC14](../13-documentacion/reglas/DOC14-enlaza-cada-md-con-ruta-legible-y-destino-relativo.md#doc14--enlaza-cada-md-con-ruta-legible-y-destino-relativo)

## DOC17 · Mantén un `README.md` en cada nivel del árbol de trabajo
Ninguna carpeta del árbol de épicas, HU y fases ([`02·F12`](../02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md), punto 13) queda muda: cada una tiene un `README.md` que lista **su contenido inmediato**, no el árbol entero, con una frase de qué es cada cosa. Se actualiza en el mismo cambio que crea, mueve o cierra algo.
```
INCORRECTO: la carpeta de la épica tiene ocho HU dentro y ningún índice ·
            hay que abrirlas una por una para saber qué hay
CORRECTO:   su README lista las ocho, cada una con su título y su estado
```

Fuente: [13·DOC17](../13-documentacion/reglas/DOC17-manten-un-readme-en-cada-nivel-del-arbol-de-trabajo.md#doc17--mantén-un-readmemd-en-cada-nivel-del-árbol-de-trabajo)

## DOC19 · Marca con `«…»` los espacios por llenar de un documento modelo
Todo espacio que quien usa un modelo tiene que reemplazar se marca `«…»`, la misma marca en todos los modelos del proyecto. Se marca lo que llena quien usa el modelo: la sintaxis de un comando que se copia y se pega la llena quien lo corre, y no es un espacio por llenar.
```
INCORRECTO: un modelo marca sus huecos con [texto], otro con <texto> y un
            tercero con XXX · el corchete además es la sintaxis del enlace,
            así que no se sabe cuál hueco es hueco
CORRECTO:   los tres marcan «texto», que no es sintaxis de nada más
```

Fuente: [13·DOC19](../13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md#doc19--marca-con--los-espacios-por-llenar-de-un-documento-modelo)

## DOC2 · Documenta las decisiones no obvias y su porqué
Escribe lo que el código no dice: reglas de negocio, por qué se eligió X y no Y, convenciones del módulo, y dónde se aplica cada una —con enlace al archivo. No documentes cómo funciona el código línea por línea, ni lo que se ve leyéndolo.
```
INCORRECTO: comentar el porqué en el código y confiar en que lo relean
CORRECTO:   registrar la decisión y su motivo en la doc, enlazando al código
```

Fuente: [13·DOC2](../13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md#doc2--documenta-las-decisiones-no-obvias-y-su-porqué)

## DOC20 · No entregues como terminado un documento que todavía trae marcas
Un documento que salió de un modelo y conserva una sola marca `«…»` sin reemplazar no está terminado y no se presenta como tal: se completa, o se dice qué falta y dónde (depende de [`DOC19`](../13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md)). Vale para todo documento que alguien vaya a leer como trabajo cerrado.
```
INCORRECTO: se entrega el plan de trabajo con «estimación» en tres tareas y
            se avisa "después lo completo"
CORRECTO:   se completan las tres, o se entrega diciendo que faltan esas tres
            y que el documento todavía no está terminado
```

Fuente: [13·DOC20](../13-documentacion/reglas/DOC20-no-entregues-como-terminado-un-documento-con-marcas.md#doc20--no-entregues-como-terminado-un-documento-que-todavía-trae-marcas)

## DOC21 · Escribe `N/A` en la sección del modelo que no aplica
La sección de un modelo que no le aplica al caso se escribe `N/A`: no se deja con su marca ni se borra (depende de [`DOC19`](../13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md)). Dejarla con la marca la vuelve un hueco sin llenar; borrarla hace creer que el modelo nunca la pidió, y quien revise no sabrá si se leyó y no aplicaba o si nadie la miró.
```
INCORRECTO: la especificación no tiene interfaz, así que se borra la sección
            de interfaz · el que revisa no sabe si no aplicaba o si se olvidó
CORRECTO:   la sección se queda con su título y adentro dice N/A
```

Fuente: [13·DOC21](../13-documentacion/reglas/DOC21-escribe-n-a-en-la-seccion-que-no-aplica.md#doc21--escribe-na-en-la-sección-del-modelo-que-no-aplica)

## DOC22 · Escribe en su propio documento lo que cada sesión dejó
Cada sesión deja su resumen en un documento aparte de la transcripción, escrito con el modelo del estándar y llenado **en el momento en que aparece cada hallazgo**, no al cerrar. Cada hallazgo dice si quedó resuelto o abierto, dónde quedó, qué trabajo dispara y con qué pregunta se retoma.
```
INCORRECTO: la sesión produjo cinco aprendizajes y nueve pendientes, y para
            encontrarlos hay que releer la conversación entera
CORRECTO:   su resumen los lista, cada uno con su estado y con la pregunta
            que quedó viva
```

Fuente: [13·DOC22](../13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md#doc22--escribe-en-su-propio-documento-lo-que-cada-sesión-dejó)

## DOC23 · Escribe el glosario de los términos del proyecto
Todo proyecto mantiene el glosario de las palabras de su negocio: cada término en una línea, entendible por quien no conoce el dominio, y actualizado en el mismo cambio que introduce el término.
Dónde vive lo declara la capa 3; el modelo es el glosario del propio estándar ([`base/glosario.md`](../glosario.md)).
```
INCORRECTO: dos documentos del mismo proyecto llaman "cliente" a cosas distintas
            y nadie lo nota hasta que el código ya está escrito
CORRECTO:   "cliente" definido en una línea en el glosario del proyecto, y los
            dos documentos usándolo igual
```

Fuente: [13·DOC23](../13-documentacion/reglas/DOC23-escribe-el-glosario-de-los-terminos-del-proyecto.md#doc23--escribe-el-glosario-de-los-términos-del-proyecto)

## DOC24 · Cierra el análisis en su mismo archivo
Un análisis individual cierra al final de su mismo archivo, con sus conclusiones, sus lecciones y lo que se tiene que hacer, y desde que se aprueba no se reescribe: lo que aparezca después abre el análisis siguiente (deroga [`13·DOC8`](../13-documentacion/reglas/DOC8-cierra-todo-analisis-con-su-tabla-de-decisiones.md)).
```
INCORRECTO: el análisis se cierra en otro archivo con su tabla de decisiones,
            y meses después alguien le corrige una conclusión al original
CORRECTO:   las conclusiones van al final del mismo análisis; aprobado, queda
            como está, y el hallazgo nuevo abre analisis-2.md
```

Fuente: [13·DOC24](../13-documentacion/reglas/DOC24-cierra-el-analisis-en-su-mismo-archivo.md#doc24--cierra-el-análisis-en-su-mismo-archivo)

## DOC25 · Reescribe el análisis principal con su lista de cambios
El análisis principal del proyecto o del módulo dice siempre lo que se va a construir hoy: cuando un análisis individual cambia algo, se reescribe y suma a su lista de cambios la fecha y el enlace a ese análisis (deroga [`13·DOC8`](../13-documentacion/reglas/DOC8-cierra-todo-analisis-con-su-tabla-de-decisiones.md)).
```
INCORRECTO: el principal dice «la clase con suma», un análisis individual
            agregó sus propiedades y el principal quedó congelado
CORRECTO:   el principal dice «la clase con suma y sus propiedades» y su
            lista de cambios enlaza el análisis que lo cambió
```

Fuente: [13·DOC25](../13-documentacion/reglas/DOC25-reescribe-el-analisis-principal-con-su-lista-de-cambios.md#doc25--reescribe-el-análisis-principal-con-su-lista-de-cambios)

## DOC4 · Documenta lo que producción necesita
Los pasos de despliegue —cambios de esquema, datos base, permisos, comandos posteriores— se documentan **auto-suficientes y ejecutables**: quien despliega lo hace leyendo el entregable, sin volver a mirar el código.
```
INCORRECTO: "aplicar las migraciones y listo" · el orden y los datos base se
            averiguan leyendo el código
CORRECTO:   la secuencia exacta, con cada comando, su orden y qué verificar
            después de cada uno
```

Fuente: [13·DOC4](../13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md#doc4--documenta-lo-que-producción-necesita)

## DOC5 · Registra como señal lo que no se recupera del código — *opt-in*
Lo que no se reconstruye leyendo el código —una decisión y su motivo, un error resuelto, un supuesto, una alternativa descartada— se registra como **señal**: qué pasó · por qué · dónde · qué se aprendió, con su tipo y a quién sirve. La revertida no se borra: se marca reemplazada y enlaza a la nueva.
```
INCORRECTO: "elegimos X y no Y porque Z" queda solo en el chat → se pierde al compactar
CORRECTO:   se registra como señal de tipo decisión, con qué / por qué / dónde / qué se aprendió
```

Fuente: [13·DOC5](../13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md#doc5--registra-como-señal-lo-que-no-se-recupera-del-código--opt-in)

## DOC7 · Registra el cruce en los dos documentos que se referencian
Cuando el documento de un módulo consume a otro, el que referencia declara **qué consume y por qué**, y el referenciado registra la recepción en su historial cruzado: fecha, de dónde vino, qué cambió. Los dos lados o ninguno. La mención de paso no cuenta: es analogía, no dependencia.
```
INCORRECTO: el documento de A dice "ver B para más" · B no se entera
CORRECTO:   A declara qué consume de B y por qué · B lo registra en su historial cruzado
```

Fuente: [13·DOC7](../13-documentacion/reglas/DOC7-registra-el-cruce-en-los-dos-documentos-que-se-referencian.md#doc7--registra-el-cruce-en-los-dos-documentos-que-se-referencian)
