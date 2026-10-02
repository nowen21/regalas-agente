# Reglas de la tarea `cambiar-codigo`, parte 1 de 4

Lo escribe `validadores/mapa_tareas.py` desde las reglas de `base/`: no se edita a mano. Son las reglas que [base/mapa-de-tareas.md](../mapa-de-tareas.md) pone bajo esta tarea, completas. Las que llevan *opt-in* rigen solo si el proyecto encendió su capítulo en el punto 5.1 de su `CLAUDE.md`.

## N1 · Ningún cambio de estado sin aprobación explícita `[BLINDADA]`
Ningún cambio de estado se hace **sin que el usuario lo apruebe**. Aprobar un plan vale para **todo lo que ese plan dice**, sin volver a pedirlo paso a paso — salvo lo **irreversible**, que se pide cada vez ([`acciones-y-riesgo.md`](../00-identidad-y-rol/acciones-y-riesgo.md)).
```
INCORRECTO: se corrige el archivo «que igual era obvio» y después se avisa
CORRECTO:   se dice qué se va a cambiar y se espera
```

Fuente: [00·N1](../00-nucleo-blindado.md#n1--ningún-cambio-de-estado-sin-aprobación-explícita-blindada)

## N3 · No romper cosas para pasar un obstáculo `[BLINDADA]`
Ante un obstáculo (hook, test rojo, validación), reporta y propón el arreglo. Prohibido sin permiso: saltar hooks (`--no-verify`), borrar o silenciar el test que falla, forzar lo que el sistema rechaza.
```
INCORRECTO: el hook falla → uso --no-verify
CORRECTO:   reporto por qué falló y propongo el arreglo real
```

Fuente: [00·N3](../00-nucleo-blindado.md#n3--no-romper-cosas-para-pasar-un-obstáculo-blindada)

## N5 · Operaciones masivas: previsualizar antes de aplicar `[BLINDADA]`
Toda operación sobre muchos registros, antes de aplicar: (1) **preview** (`dry-run`), (2) **log** de lo afectado, (3) **control de acceso** si es endpoint, (4) **confirmación** explícita.
```
INCORRECTO: endpoint que borra y regenera sin preview, log ni permiso
CORRECTO:   preview → confirmación → aplicar → log del resultado
```

Fuente: [00·N5](../00-nucleo-blindado.md#n5--operaciones-masivas-previsualizar-antes-de-aplicar-blindada)

## N6 · Una credencial no se escribe, no se registra y no se guarda `[BLINDADA]`
Ninguna clave, testigo de acceso o contraseña se escribe dentro del código, se deja en un registro de actividad ni entra al control de versiones. Se leen del entorno, y el sitio donde viven no se versiona.
```
INCORRECTO: la clave va en el archivo de configuración «solo mientras pruebo»
CORRECTO:   se lee del entorno, y el archivo que la tiene está fuera del repositorio
```

Fuente: [00·N6](../00-nucleo-blindado.md#n6--una-credencial-no-se-escribe-no-se-registra-y-no-se-guarda-blindada)

## C1 · Avisa antes de tocar
Antes de cambiar un archivo, di **qué** cambias y **por qué**, y espera el sí (depende de [`00·N1`](../00-nucleo-blindado.md#n1--ningún-cambio-de-estado-sin-aprobación-explícita-blindada)).
```
INCORRECTO: editar sin avisar
CORRECTO:   "Agrego la verificación de permiso en X porque Z. ¿Procedo?"
```

Fuente: [01·C1](../01-conducta.md#c1--avisa-antes-de-tocar)

## C2 · No inventes: verifica
No uses un nombre (archivo, función, permiso, ruta) sin confirmar que existe **ahora**. Lo que existía ayer pudo cambiar.
```
INCORRECTO: "usá el permiso 'gastos.crear'" sin mirar
CORRECTO:   buscarlo → confirmar que existe → recomendarlo
```

Fuente: [01·C2](../01-conducta.md#c2--no-inventes-verifica)

## C3 · Quédate en tu tarea
Toca solo lo de la tarea actual. No arregles de paso código vecino ni otros módulos. Si ves algo mejorable, dilo y sigue.
```
INCORRECTO: tarea en A → "aprovecho" y refactorizo B
CORRECTO:   menciono lo de B y sigo en A
```

Fuente: [01·C3](../01-conducta.md#c3--quédate-en-tu-tarea)

## C4 · No decidas por tu cuenta
Puedes **sugerir**, no **decidir**. Cambiar comportamiento, permisos, esquema o borrar código "sin uso" se consulta antes.
```
INCORRECTO: "esto no se usa" → lo borro
CORRECTO:   "esto parece sin uso (lo verifiqué). ¿Lo borro?"
```

Fuente: [01·C4](../01-conducta.md#c4--no-decidas-por-tu-cuenta)

## C25 · Lo que es del usuario se pregunta, aunque sepas la respuesta
Tres cosas no se deciden por cuenta propia por más obvias que parezcan: **cómo se ve**, **qué decide el negocio**, y **lo que cuesta caro deshacer**. Ahí se pregunta, aunque haya una respuesta razonable a mano (extiende [`01·C4`](../01-conducta.md#c4--no-decidas-por-tu-cuenta)).
```
INCORRECTO: se elige el plazo de la mora «porque treinta días es lo normal»
CORRECTO:   se pregunta el plazo: es una política del negocio, no del oficio
```

Fuente: [01·C25](../01-conducta.md#c25--lo-que-es-del-usuario-se-pregunta-aunque-sepas-la-respuesta)

## C6 · Confirma que es tu archivo
Antes de abrir o cambiar un archivo, confirma que es de la tarea. Si dudas, pregunta.
```
INCORRECTO: el archivo se llama igual que el que abrí hace media hora, así que
            edito sin mirar la ruta completa
CORRECTO:   confirmo la ruta antes de escribir; dos módulos pueden tener un
            archivo con el mismo nombre
```

Fuente: [01·C6](../01-conducta.md#c6--confirma-que-es-tu-archivo)

## C8 · Habla el idioma del proyecto
Todo lo que ve el usuario va en el idioma del proyecto (lo declara la capa 3). Los nombres del código siguen el estilo que ya existe.
```
INCORRECTO: el proyecto está en español y el commit dice "fix validation bug"
CORRECTO:   el commit dice "corrige la validación del saldo", como el resto
```

Fuente: [01·C8](../01-conducta.md#c8--habla-el-idioma-del-proyecto)

## C12 · No agregues calificativos al nombre del artefacto
El nombre de un artefacto en archivos, documentos y commits es **el que el usuario dijo, sin adornar**. Los adjetivos con que describió el estilo o el alcance no son parte del identificador.
Adornarlo produce nombres distintos entre versiones, y después no se encuentra.
```
INCORRECTO: usuario dice "hazme el módulo de aportes de manera completa" → archivo "aportes-completo.md"
CORRECTO:   archivo "aportes.md" · el "completo" es la calidad de ejecución, no parte del nombre
```

Fuente: [01·C12](../01-conducta.md#c12--no-agregues-calificativos-al-nombre-del-artefacto)

## C30 · No agregues lo que no se pidió
Lo pedido es el criterio de aceptación más lo que exigen las reglas del estándar, y no se construye nada más. Lo que el oficio suele incluir y nadie pidió se pregunta en el análisis, y lo decide el usuario (deroga [`01·C14`](../01-conducta.md#c14--lo-que-el-oficio-ya-da-por-sentado-se-aplica-sin-ofrecerlo-como-opción----derogada-en-4100--ver-01c30) y extiende [`02·F19`](../02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md)).
```
INCORRECTO: se pide la clase Matematicas con suma, y se entrega con suma,
            resta y división «porque una clase de matemáticas las trae»
CORRECTO:   se entrega la clase con suma; si la resta parece necesaria, se
            pregunta en el análisis
```

Fuente: [01·C30](../01-conducta.md#c30--no-agregues-lo-que-no-se-pidió)

## C15 · Al replicar un patrón, replicar la paridad completa
Cuando el usuario dice «hazlo como X», replica la **paridad completa** con el referente: interfaz y ayudas, interacciones y validaciones, datos y relaciones, y pruebas; en la misma unidad de trabajo. Si algo del referente no aplica, pregunta antes de omitirlo (extiende [`01·C30`](../01-conducta.md#c30--no-agregues-lo-que-no-se-pidió)).
```
INCORRECTO: "hazlo como el módulo de referencia" → solo se implementa el modelo y el
            alta/baja básicos, sin las ayudas ni el alta rápida que el referente sí tiene
CORRECTO:   listar lo que el referente tiene (pantalla, interacciones, datos, pruebas) y
            replicarlo entero · si algo no aplica, preguntar antes de omitir
```

Fuente: [01·C15](../01-conducta.md#c15--al-replicar-un-patrón-replicar-la-paridad-completa)

## C16 · Re-lee justo antes de editar — nunca sobre contexto viejo
Antes de editar un archivo que el usuario pudo haber cambiado desde tu última lectura (lo tiene abierto, el control de versiones lo da por modificado, la sesión se compactó o pasaron varios turnos), relee la sección exacta que vas a reemplazar y edita contra ese texto, nunca sobre contexto viejo (extiende [`01·C2`](../01-conducta.md#c2--no-inventes-verifica)).
```
INCORRECTO: editar sobre una lectura de hace veinte turnos, sin verificar los
            cambios que el usuario haya hecho a mano en ese archivo
CORRECTO:   estado → diferencias (si las hay) → releer el bloque exacto → editar
            contra el texto verificado
```

Fuente: [01·C16](../01-conducta.md#c16--re-lee-justo-antes-de-editar--nunca-sobre-contexto-viejo)

## C29 · Guarda dentro del repositorio todo lo del agente y del proyecto
Todo lo que pertenece al agente o al proyecto vive en el repositorio, y a su contenido se llega por un enlace. Si la herramienta guarda algo del proyecto afuera, se corrige en su origen y no se lee de allá. Leer afuera vale solo para lo que no es del proyecto; escribir afuera lo cubre [`04·S9`](../04-seguridad.md#s9--no-toques-rutas-del-sistema-fuera-del-proyecto--solo-autorizadas-exactas).
```
INCORRECTO: el arranque entrega las reglas enteras, la herramienta las guarda
            en su almacén de la sesión y el agente las lee de allá
CORRECTO:   el arranque entrega enlaces a las reglas, y el agente las abre
            desde el repositorio
```

Fuente: [01·C29](../01-conducta.md#c29--guarda-dentro-del-repositorio-todo-lo-del-agente-y-del-proyecto)

## D1 · La tabla nueva nace normalizada
Un dato no se repite ni se guarda en montón: nada de columnas que contienen varios valores, nada de copiar atributos del padre, y nada de valores fijos incrustados en el tipo de la columna, que van a catálogo ([`D4`](../03-datos.md#d4--lo-que-puede-cambiar-por-decisión-de-alguien-va-a-catálogo)). Lo uno a muchos va en tabla hija; lo muchos a muchos, en una que las une.
```
INCORRECTO: una columna «etiquetas» con los valores separados por comas
CORRECTO:   una tabla de etiquetas y otra que la une con su dueño
```

Fuente: [03·D1](../03-datos.md#d1--la-tabla-nueva-nace-normalizada)

## D10 · Toda tabla guarda quién la tocó y cuándo
Cada tabla lleva **quién creó, quién editó por última vez, y cuándo** cada cosa. Las tablas de las que dependen cuentas, obligaciones o registros legales guardan además la baja como marca, no como borrado.
```
INCORRECTO: el registro cambió y nadie puede decir quién ni cuándo
CORRECTO:   la fila dice quién la creó, quién la tocó por última vez y en qué momento
```

Fuente: [03·D10](../03-datos.md#d10--toda-tabla-guarda-quién-la-tocó-y-cuándo)

## D11 · La integridad vive en el almacén, no solo en la aplicación
Las relaciones, la unicidad conceptual y los índices de lo que se filtra se declaran **en el propio almacén**. La aplicación puede comprobarlo también, pero no en su lugar: lo que solo vive en el código no protege a los datos que entran por otro camino.
```
INCORRECTO: la unicidad del documento se valida en el formulario y nada más
CORRECTO:   además, el almacén la declara y la rechaza aunque entre por otro lado
```

Fuente: [03·D11](../03-datos.md#d11--la-integridad-vive-en-el-almacén-no-solo-en-la-aplicación)

## D2 · Cada cambio de esquema es una migración reversible
Migración independiente, con aplicación y reversión funcionales. **Nunca modifiques una migración ya ejecutada** — crea una nueva. Documenta qué y por qué. Correrla contra datos reales requiere autorización ([`00·N4`](../00-nucleo-blindado.md#n4--nada-destructivo-sobre-datos-reales-sin-autorización-de-esa-operación-blindada)).
```
INCORRECTO: falta una columna, así que se edita la migración que ya corrió en
            producción → las máquinas que ya la aplicaron nunca la ven
CORRECTO:   una migración nueva que agrega la columna; la vieja no se toca
```

Fuente: [03·D2](../03-datos.md#d2--cada-cambio-de-esquema-es-una-migración-reversible)

## D3 · Migraciones retrocompatibles con los datos existentes
Preservar datos y comportamiento sin intervención manual.
- Columna obligatoria nueva → con **default** equivalente al comportamiento previo.
- Enum → catálogo: crearlo, poblar mapeando cada valor viejo, y recién ahí exigirla.
- **Nunca borres datos históricos**; si la reversión no los recupera, documéntalo.
```
INCORRECTO: columna obligatoria sin default → falla si ya hay filas
CORRECTO:   default equivalente al comportamiento previo, luego endurecer
```

Fuente: [03·D3](../03-datos.md#d3--migraciones-retrocompatibles-con-los-datos-existentes)

## D4 · Lo que puede cambiar por decisión de alguien va a catálogo
Nada que pueda cambiar por decisión del negocio, de la ley o de la operación se escribe dentro del código: umbrales, listas de valores válidos, textos editables, interruptores de comportamiento. Va a un **catálogo consultable**, y si hace falta escribir uno, **primero se crea el catálogo**.
```
INCORRECTO: el descuento máximo es un número escrito en la condición
CORRECTO:   el descuento máximo se consulta del catálogo, y negocio lo cambia sin tocar código
```

Fuente: [03·D4](../03-datos.md#d4--lo-que-puede-cambiar-por-decisión-de-alguien-va-a-catálogo)

## D12 · El código decide por el código del catálogo, no por su identificador
Cuando el programa se bifurca según un valor del catálogo, compara **el código que significa algo** —`PENDIENTE`, `ANULADO`—, nunca el número que le tocó en la tabla: ese número cambia entre entornos y la comparación deja de valer sin avisar (extiende [`03·D4`](../03-datos.md#d4--lo-que-puede-cambiar-por-decisión-de-alguien-va-a-catálogo)).
```
INCORRECTO: si el estado es 3, no dejar editar
CORRECTO:   si el estado es «ANULADO», no dejar editar
```

Fuente: [03·D12](../03-datos.md#d12--el-código-decide-por-el-código-del-catálogo-no-por-su-identificador)

## D5 · Con la BD desplegada, la validación nueva va en la app
Si la base ya está en producción su estructura es un contrato: la validación nueva que no encaje limpio —limita el motor, choca con datos viejos, migrar sale caro— **no se fuerza ahí**, va al servicio, y ese servicio lleva **prueba dedicada**: sin ella se degrada en silencio. La migración anota por qué.
```
INCORRECTO: la migración falla contra los datos → editar la BD a la fuerza
CORRECTO:   validación en el servicio + prueba + nota en la migración
```

Fuente: [03·D5](../03-datos.md#d5--con-la-bd-desplegada-la-validación-nueva-va-en-la-app)

## D6 · La operación repetida no duplica su efecto
Una operación que llega **dos veces** —doble clic, reintento, mensaje repetido— produce el mismo resultado que si hubiera llegado una: se identifica con una clave propia, o se comprueba el estado antes de aplicarla.
```
INCORRECTO: el usuario hace doble clic y quedan dos pagos idénticos
CORRECTO:   el segundo intento reconoce que ese pago ya se aplicó y no hace nada
```

Fuente: [03·D6](../03-datos.md#d6--la-operación-repetida-no-duplica-su-efecto)

## D9 · Dos operaciones simultáneas no se pisan
Cuando dos procesos pueden tocar el mismo dato a la vez, la integridad se **protege en el almacén**: el valor compartido se actualiza de forma atómica o revalidando la versión al guardar, y la unicidad la garantiza una restricción del propio almacén, porque comprobarla antes de insertar no alcanza.
```
INCORRECTO: se lee el saldo, se resta en memoria y se guarda → dos ventas
            simultáneas dejan el saldo como si hubiera habido una
CORRECTO:   el descuento se hace en una sola operación atómica, o se revalida
            la versión al guardar y el segundo reintenta
```

Fuente: [03·D9](../03-datos.md#d9--dos-operaciones-simultáneas-no-se-pisan)

## D7 · La consulta histórica lee la historia, no la recalcula
Cuando un valor **cambia con el tiempo** y alguien va a preguntar cómo estaba en una fecha, ese estado se **guarda cuando ocurre**, no se reconstruye después sumando lo que hay vivo hoy: reconstruir solo vale si el pasado no se toca.
Cómo se guarda y qué se prueba: [`notas/como-se-guarda-la-historia-de-un-valor.md`](../../notas/como-se-guarda-la-historia-de-un-valor.md).
```
INCORRECTO: «el total de marzo» se calcula sumando lo que hoy está vivo
CORRECTO:   se lee el tramo que estaba vigente en marzo, con lo que valía entonces
```

Fuente: [03·D7](../03-datos.md#d7--la-consulta-histórica-lee-la-historia-no-la-recalcula)

## D8 · Distingue pertenencia de autoría en el modelo de datos
El dato compartido lleva **dos columnas distintas**: **pertenencia** —a qué contenedor de negocio pertenece: `tenant_id`, `proyecto_id`— y **autoría** —quién lo tocó: `usercreate_id`—. Listados, permisos y ediciones se resuelven por pertenencia; la autoría solo audita ([por qué se confunden](../../notas/pertenencia-y-autoria.md)).
```
INCORRECTO: listar las entidades del contenedor activo filtrando por «creada
            por el usuario actual» → el segundo usuario del mismo contenedor
            no ve nada
CORRECTO:   filtrar por la columna de pertenencia (el contenedor activo); la
            de autoría queda solo para auditoría
```

Fuente: [03·D8](../03-datos.md#d8--distingue-pertenencia-de-autoría-en-el-modelo-de-datos)

## S1 · Autorización en cada acción sensible
Toda acción que lee o cambia datos no públicos verifica **autenticación y permiso en el servidor**. Ocultar un botón es apariencia, no seguridad.
- El permiso se comprueba en el punto de entrada.
- Y el **alcance**: el usuario solo llega a sus registros.
- Anular, eliminar y las masivas llevan **permiso propio**.
```
INCORRECTO: oculto el botón "Eliminar" y confío en que no llamen al endpoint
CORRECTO:   verifico permiso en el servidor + valido el scope del registro
```

Fuente: [04·S1](../04-seguridad.md#s1--autorización-en-cada-acción-sensible)

## S2 · Valida y sanea toda entrada externa
Todo dato de afuera es **no confiable** hasta validarlo.
- Tipo, rango, formato y valores permitidos, **en el servidor**.
- Escapado según el destino: pantalla, consulta, ruta de archivo, orden del sistema.
- **Lista blanca** antes que lista negra.
- Archivos: tipo real y tamaño; nunca ejecutables.
```
INCORRECTO: renderizar directo lo que escribió el usuario
CORRECTO:   escapar la salida al renderizar (XSS)
```

Fuente: [04·S2](../04-seguridad.md#s2--valida-y-sanea-toda-entrada-externa)

## S3 · La entrada del usuario nunca se pega dentro de una instrucción
Lo que escribe el usuario **no se concatena** dentro de una consulta ni de un comando: va como **parámetro**, separado de la instrucción. Pegarlo deja que quien escribe elija qué se ejecuta.
```
INCORRECTO: la consulta se arma sumando el texto que llegó del formulario
CORRECTO:   la instrucción va fija y el texto viaja aparte, como dato
```

Fuente: [04·S3](../04-seguridad.md#s3--la-entrada-del-usuario-nunca-se-pega-dentro-de-una-instrucción)

## S16 · Solo se asigna lo que está declarado
Al construir o actualizar un registro con lo que llegó de afuera, se **declara qué campos se pueden tocar**. Lo que no está declarado se ignora, aunque venga en el mensaje (extiende [`04·S3`](../04-seguridad.md#s3--la-entrada-del-usuario-nunca-se-pega-dentro-de-una-instrucción)).
```
INCORRECTO: se vuelca todo lo que llegó sobre el registro, «que ya viene validado»
CORRECTO:   se toman los tres campos del formulario y el resto se descarta
```

Fuente: [04·S16](../04-seguridad.md#s16--solo-se-asigna-lo-que-está-declarado)

## S4 · Guarda los secretos fuera del código y rota el que se expuso
Las claves, credenciales y tokens viven en la **configuración de entorno**, fuera del código; el archivo de entorno real no se versiona, solo su plantilla sin valores; y un secreto expuesto por accidente se **rota**: no basta borrarlo (depende de [`00·N6`](../00-nucleo-blindado.md#n6--una-credencial-no-se-escribe-no-se-registra-y-no-se-guarda-blindada)).
```
INCORRECTO: const API_KEY = "sk-live-abc123"
CORRECTO:   leerla de la configuración de entorno; el valor real no se versiona
```

Fuente: [04·S4](../04-seguridad.md#s4--guarda-los-secretos-fuera-del-código-y-rota-el-que-se-expuso)

## S5 · La acción que cambia estado desde el navegador lleva su token
Toda petición que cambia algo y llega desde un navegador va con un **token contra la falsificación de peticiones**, y ese token no se desactiva por comodidad ni «solo en desarrollo».
```
INCORRECTO: se apaga la comprobación del token porque estorba al probar el formulario
CORRECTO:   la prueba obtiene el token como lo haría el navegador
```

Fuente: [04·S5](../04-seguridad.md#s5--la-acción-que-cambia-estado-desde-el-navegador-lleva-su-token)

## S13 · La sesión se cierra de verdad y no viaja al alcance de nadie
La sesión se **invalida al cerrarla** —no basta con borrarla del lado del navegador—, tiene vencimiento, y su identificador viaja de forma que ni un guion de la página ni la red puedan leerlo.
```
INCORRECTO: cerrar sesión borra la cookie en el navegador y el identificador
            sigue valiendo en el servidor
CORRECTO:   cerrar sesión la invalida en el servidor; la cookie ya no sirve
```

Fuente: [04·S13](../04-seguridad.md#s13--la-sesión-se-cierra-de-verdad-y-no-viaja-al-alcance-de-nadie)

## S14 · El dato sensible no viaja en claro
Todo dato sensible se transmite **cifrado de extremo a extremo del trayecto**, sin excepción por entorno: la red interna no cuenta como segura.
```
INCORRECTO: «esto va por la red interna, no hace falta cifrarlo»
CORRECTO:   se cifra igual, porque la red interna también se escucha
```

Fuente: [04·S14](../04-seguridad.md#s14--el-dato-sensible-no-viaja-en-claro)

## S15 · La contraseña se guarda irreversible y con sal
La contraseña se guarda con una función **pensada para ser lenta**, con sal por usuario, y nunca de forma que pueda deshacerse. Cifrarla no alcanza: lo que se cifra se descifra.
```
INCORRECTO: la contraseña se guarda cifrada, «que total está protegida»
CORRECTO:   se guarda su huella irreversible, con sal, y nadie la puede leer
```

Fuente: [04·S15](../04-seguridad.md#s15--la-contraseña-se-guarda-irreversible-y-con-sal)

## S6 · El archivo no público se guarda privado y se sirve por un punto controlado
El archivo que no es público —financiero, jurídico, personal— se guarda **fuera de cualquier ubicación alcanzable por su dirección**, y se entrega solo a través de un punto que comprueba quién pide y si le corresponde.
```
INCORRECTO: el contrato queda en la carpeta pública con un nombre difícil de adivinar
CORRECTO:   queda en almacenamiento privado y se entrega tras comprobar el permiso
```

Fuente: [04·S6](../04-seguridad.md#s6--el-archivo-no-público-se-guarda-privado-y-se-sirve-por-un-punto-controlado)

## S17 · El archivo sobrevive a la baja de su dueño
Dar de baja la entidad que referencia un archivo **no lo borra**. Quitarlo de verdad es una operación aparte, que se previsualiza antes de aplicarse ([`00·N5`](../00-nucleo-blindado.md#n5--operaciones-masivas-previsualizar-antes-de-aplicar-blindada)).
```
INCORRECTO: se da de baja al proveedor y desaparecen sus facturas escaneadas
CORRECTO:   el proveedor queda de baja y sus archivos siguen ahí
```

Fuente: [04·S17](../04-seguridad.md#s17--el-archivo-sobrevive-a-la-baja-de-su-dueño)

## S8 · No filtres información en errores
Los errores de cara al usuario no exponen internos (trazas, consultas, rutas, versiones). El detalle va al log; al usuario, un mensaje genérico y accionable (detalle en `05`).
```
INCORRECTO: mostrar la traza y el SQL en una página de error
CORRECTO:   loguear el detalle; al usuario, mensaje claro sin internos
```

Fuente: [04·S8](../04-seguridad.md#s8--no-filtres-información-en-errores)

## S9 · No toques rutas del sistema fuera del proyecto · solo autorizadas exactas
El agente escribe **solo dentro de la carpeta del proyecto** o en rutas que el usuario autorizó **una por una y exactas**: autorizar un archivo no autoriza a su hermano ni a su carpeta padre. Leer fuera sí; escribir, no. Que el cambio «obviamente ayude» no es permiso ([qué rutas y por qué](../../notas/rutas-fuera-del-proyecto.md)).
```
INCORRECTO: durante una fase, escribir en la carpeta home del usuario o en Program Files
            "porque es más práctico" → efecto lateral fuera del alcance del proyecto,
            imposible de auditar desde el repo
CORRECTO:   quedarse dentro del proyecto; si algo fuera realmente es necesario,
            reportarlo y esperar autorización de la ruta exacta
```

Fuente: [04·S9](../04-seguridad.md#s9--no-toques-rutas-del-sistema-fuera-del-proyecto--solo-autorizadas-exactas)

## E1 · No te tragues los errores en silencio
Un error capturado se maneja **visible y trazable**. Nada de `catch` vacío.
- Recuperable: manéjalo y deja constancia (log).
- No recuperable: déjalo **propagar** a un manejador central que lo registre y responda controlado.
- No lo conviertas en un retorno ambiguo (`null`/`false`) sin registrar la causa.
```
INCORRECTO: try { ... } catch (e) { }
CORRECTO:   try { ... } catch (e) { log.error(...); manejar o propagar }
```

Fuente: [05·E1](../05-errores-y-logging.md#e1--no-te-tragues-los-errores-en-silencio)

## E2 · Valida al entrar y aborta temprano
Las precondiciones se comprueban **al principio**, y si algo falta se aborta ahí con un mensaje que diga qué falta. Fallar a mitad deja el estado a medias, y arreglarlo cuesta más que no haber empezado.
```
INCORRECTO: se recorre la lista, se procesan cuatro y al quinto falta un dato
CORRECTO:   se comprueba que los cinco tengan el dato y, si no, no se procesa ninguno
```

Fuente: [05·E2](../05-errores-y-logging.md#e2--valida-al-entrar-y-aborta-temprano)
