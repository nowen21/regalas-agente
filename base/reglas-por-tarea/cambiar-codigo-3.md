# Reglas de la tarea `cambiar-codigo`, parte 3 de 4

Lo escribe `validadores/mapa_tareas.py` desde las reglas de `base/`: no se edita a mano. Son las reglas que [base/mapa-de-tareas.md](../mapa-de-tareas.md) pone bajo esta tarea, completas. Las que llevan *opt-in* rigen solo si el proyecto encendió su capítulo en el punto 5.1 de su `CLAUDE.md`.

## IM2 · El registro tiene tres estados y solo uno es editable
El registro pasa por **borrador**, que se edita; **materializado**, que ya no; y **anulado**, que revierte el efecto **conservando la fila**. Nada se borra para corregirlo: se anula y se rehace.
```
INCORRECTO: la factura salió mal, se edita el registro ya emitido
CORRECTO:   se anula la emitida —queda su fila— y se emite otra
```

Fuente: [15·IM2](../15-registros-inmutables.md#im2--el-registro-tiene-tres-estados-y-solo-uno-es-editable)

## IM3 · La anulación revierte todo o no revierte nada
Anular comprueba primero que el estado lo permita, y después revierte **en una sola transacción** todos los efectos que el registro produjo — movimientos, saldos, derivados — junto con la marca de anulado. Si algo de la reversión falla, no queda nada a medias ([`05·E6`](../05-errores-y-logging.md#e6--lo-que-toca-varios-registros-va-en-transacción)).
```
INCORRECTO: se marca anulado, se revierte el movimiento y falla el saldo
            → el registro dice anulado y el saldo dice que no
CORRECTO:   o se revierten los tres y la marca, o no se revierte ninguno
```

Fuente: [15·IM3](../15-registros-inmutables.md#im3--la-anulación-revierte-todo-o-no-revierte-nada)

## IM7 · Al anular se avisa a quien tenía el dato calculado
La anulación **avisa** a los demás módulos para que descarten lo que tenían derivado de ese registro: totales, resúmenes, lo que se hubiera guardado calculado (extiende [`15·IM3`](../15-registros-inmutables.md#im3--la-anulación-revierte-todo-o-no-revierte-nada)).
```
INCORRECTO: la factura se anula y el total del mes la sigue contando
CORRECTO:   al anularla, lo que la había sumado se entera y se rehace
```

Fuente: [15·IM7](../15-registros-inmutables.md#im7--al-anular-se-avisa-a-quien-tenía-el-dato-calculado)

## IM4 · Las consultas agregadoras excluyen los anulados
Toda consulta que sume/cuente/promedie **excluye** los anulados. Idealmente por **defecto** en el modelo/consulta, no confiando en que cada consulta lo recuerde.
```
INCORRECTO: un reporte que suma incluyendo anulados "y que el usuario tenga cuidado"
CORRECTO:   la consulta excluye anulados por defecto
```

Fuente: [15·IM4](../15-registros-inmutables.md#im4--las-consultas-agregadoras-excluyen-los-anulados)

## IM5 · Permiso propio para anular
Anular pesa más que crear o editar: **permiso separado** del de eliminar, para roles con responsabilidad ([`04·S1`](../04-seguridad.md#s1--autorización-en-cada-acción-sensible)). En la UI, los materializados ofrecen "Anular" (motivo obligatorio) en vez de "Eliminar"; los anulados quedan visibles, marcados y con su motivo.

Fuente: [15·IM5](../15-registros-inmutables.md#im5--permiso-propio-para-anular)

## IM6 · Anular deja escrito quién, cuándo y por qué
La anulación guarda **quién la hizo, cuándo, y el motivo** — un motivo con sustancia, no una palabra. Sin eso la fila conservada dice que algo se revirtió y no dice nada más (extiende [`15·IM2`](../15-registros-inmutables.md#im2--el-registro-tiene-tres-estados-y-solo-uno-es-editable)).
```
INCORRECTO: motivo: «error»
CORRECTO:   motivo: «se emitió al cliente equivocado; se rehace con el 4021»
```

Fuente: [15·IM6](../15-registros-inmutables.md#im6--anular-deja-escrito-quién-cuándo-y-por-qué)

## CQ2 · Cumple por construcción y déjalo trazable
Traduce cada control del marco a una **decisión concreta** (esquema, validación, permiso, cifrado, log, retención) y verifícalo junto con la trazabilidad especificación→implementación ([`13·DOC3`](../13-documentacion/reglas/DOC3-verifica-la-trazabilidad-especificacion-implementacion-antes-de-cerrar.md)). Si un requisito **no se puede cumplir**, avísalo — no lo omitas en silencio.
```
INCORRECTO: implementar y dar por hecho que "cumple"
CORRECTO:   mapear cada requisito del marco a un control real + evidencia en la trazabilidad
```

Fuente: [16·CQ2](../16-cumplimiento-y-calidad.md#cq2--cumple-por-construcción-y-déjalo-trazable)

## CQ3 · Seguridad de software por defecto (OWASP)
Toma **OWASP** (ASVS + Top 10) como línea base de controles de código seguro. Es la instancia concreta de la seguridad de `04`: inyección, autenticación, control de acceso, exposición de datos, configuración segura.
```
INCORRECTO: revisar la seguridad "a ojo", con lo que cada quien recuerde
CORRECTO:   recorrer los controles de OWASP y decir cuáles aplican y dónde quedan
```

Fuente: [16·CQ3](../16-cumplimiento-y-calidad.md#cq3--seguridad-de-software-por-defecto-owasp)

## CQ4 · Atributos de calidad como checklist (ISO/IEC 25010)
Evalúa y prioriza contra los atributos de **ISO/IEC 25010**: funcionalidad, fiabilidad, seguridad, usabilidad, eficiencia de desempeño, mantenibilidad, compatibilidad, portabilidad. Sirve para decidir qué mejorar y para justificar trade-offs.
```
INCORRECTO: "está listo" sin mirar mantenibilidad ni fiabilidad
CORRECTO:   revisar el cambio contra los atributos de 25010 y nombrar los trade-offs
```

Fuente: [16·CQ4](../16-cumplimiento-y-calidad.md#cq4--atributos-de-calidad-como-checklist-isoiec-25010)

## I1 · Toda vista resuelve sus tres estados
Ninguna pantalla queda en blanco ni muestra un error crudo. Los tres se definen siempre:
- **Vacío** → un mensaje claro y, si aplica, la acción que lo llena.
- **Cargando** → un indicador, no una pantalla congelada.
- **Error** → un mensaje entendible y accionable, **nunca** una traza ([`05·E3`](../05-errores-y-logging.md#e3--mensajes-en-dos-niveles-usuario-y-diagnóstico)).
```
INCORRECTO: la tabla aparece vacía sin explicar si no hay datos o si falló la carga
CORRECTO:   estado vacío ("no hay registros"), estado cargando, y estado de error diferenciados
```

Fuente: [17·I1](../17-interfaz.md#i1--toda-vista-resuelve-sus-tres-estados)

## I2 · Feedback de validación claro
Cuando el usuario se equivoca en un formulario, se le dice **qué campo** y **qué falta**, en su idioma ([`01·C8`](../01-conducta.md#c8--habla-el-idioma-del-proyecto)), antes o al enviar. No se rechaza en silencio ni con un mensaje genérico.
```
INCORRECTO: "Error al guardar" sin decir qué campo está mal
CORRECTO:   "El correo no es válido" junto al campo correspondiente
```

Fuente: [17·I2](../17-interfaz.md#i2--feedback-de-validación-claro)

## I3 · Accesibilidad mínima
La interfaz cumple el **mínimo de accesibilidad**: esta lista cerrada, entera y no a medias.
- Campos con **etiqueta** asociada; imágenes con texto alternativo.
- **Contraste** suficiente entre texto y fondo.
- Navegable por **teclado**, con el **foco visible**.
- Ninguna información transmitida **solo** por color.
```
INCORRECTO: la pantalla tiene etiquetas impecables y se entrega como accesible,
            con el texto en gris claro sobre blanco y el estado de cada fila
            indicado solo con un punto de color
CORRECTO:   los cuatro puntos de la lista, comprobados juntos antes de entregar
```

Fuente: [17·I3](../17-interfaz.md#i3--accesibilidad-mínima)

## I4 · Texto para el usuario, no jerga
Lo que el usuario lee se entiende sin ser del oficio: **claro, directo, que hasta un niño lo entienda**. Sin siglas internas, sin códigos de sistema, sin jerga técnica. (Es el mismo estándar de [`00·ID7`](../00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md) llevado a la pantalla del producto; lo que se suma acá es que no asomen siglas ni códigos internos.)
```
INCORRECTO: "Error 422: constraint violation en FK proyecto_id"
CORRECTO:   "No se pudo guardar: primero elegí un proyecto"
```

Fuente: [17·I4](../17-interfaz.md#i4--texto-para-el-usuario-no-jerga)

## I5 · Consistencia con el sistema de diseño
Usar los componentes y patrones que el proyecto ya tiene (el sistema de diseño lo declara la capa 3) antes de inventar unos nuevos. Una pantalla nueva se parece a las demás: mismos componentes, misma ubicación de las acciones, mismos estados.
```
INCORRECTO: la pantalla nueva trae su propio botón, su propio modal y las
            acciones a la izquierda, porque «quedaba mejor»
CORRECTO:   los componentes que ya existen, y las acciones donde el usuario
            ya sabe buscarlas
```

Fuente: [17·I5](../17-interfaz.md#i5--consistencia-con-el-sistema-de-diseño)

## I6 · Funciona en los tamaños de pantalla que el proyecto soporta
La interfaz se ve y funciona en los tamaños de pantalla que el proyecto soporta (declarados en capa 3). El contenido ancho (tablas, diagramas) no rompe el layout: se desplaza en su propio contenedor.
```
INCORRECTO: una tabla de doce columnas que empuja el layout y saca una barra
            de desplazamiento a la página entera
CORRECTO:   la tabla se desplaza dentro de su contenedor; la página no
```

Fuente: [17·I6](../17-interfaz.md#i6--funciona-en-los-tamaños-de-pantalla-que-el-proyecto-soporta)

## DP1 · El despliegue es un artefacto versionado, no una serie de clics
Todo lo que lleva el código a un entorno vive en el repo como **texto revisable**: pipeline de CI/CD, manifiestos de infraestructura, scripts. Nada de configurar a mano en una consola (click-ops) sin dejar rastro: lo que no está versionado no es reproducible ni auditable, y se pierde cuando cambia la persona.
```
INCORRECTO: la cola de mensajes se crea a mano en la consola de la nube y «queda
            anotado» en un chat; nadie puede volver a crearla igual
CORRECTO:   el recurso se declara en el manifiesto versionado y se aplica desde ahí
```

Fuente: [18·DP1](../18-despliegue-e-infraestructura.md#dp1--el-despliegue-es-un-artefacto-versionado-no-una-serie-de-clics)

## DP2 · Infraestructura como código
La infraestructura (contenedor, red, servicios, recursos de nube) se declara en archivos versionados y se aplica desde ahí, no se crea a mano. Un entorno nuevo se levanta corriendo la declaración, no siguiendo un instructivo. El **estado real** debe poder reconstruirse del código.
```
INCORRECTO: el servidor nuevo se configura siguiendo un instructivo de doce pasos
CORRECTO:   se corre la declaración versionada y el entorno queda igual al anterior
```

Fuente: [18·DP2](../18-despliegue-e-infraestructura.md#dp2--infraestructura-como-código)

## DP3 · Build una vez, promover el mismo artefacto
Se compila/empaqueta **una sola vez** y ese mismo artefacto inmutable (imagen, paquete) pasa por los entornos (pruebas → staging → producción). No se recompila por entorno: lo que se probó es exactamente lo que se despliega. La versión del artefacto es rastreable al commit.
```
INCORRECTO: se vuelve a compilar «para producción» con otra bandera: lo que llega
            no es lo que se probó
CORRECTO:   la misma imagen que pasó las pruebas se promueve, etiquetada con su commit
```

Fuente: [18·DP3](../18-despliegue-e-infraestructura.md#dp3--build-una-vez-promover-el-mismo-artefacto)

## DP4 · Config por entorno, fuera del artefacto
El artefacto es **agnóstico del entorno**; la configuración y los secretos se inyectan al desplegar, no se hornean adentro (`11`, [`04·S4`](../04-seguridad.md#s4--guarda-los-secretos-fuera-del-código-y-rota-el-que-se-expuso)). Así la misma imagen corre en cualquier entorno cambiando solo su config, y un secreto no viaja dentro del build.
```
INCORRECTO: la clave de producción va dentro de la imagen «para que no se olvide»
CORRECTO:   la imagen lee la clave del entorno al arrancar; la misma imagen corre en
            pruebas y en producción cambiando solo su configuración
```

Fuente: [18·DP4](../18-despliegue-e-infraestructura.md#dp4--config-por-entorno-fuera-del-artefacto)

## DP5 · Release reversible, con plan de vuelta
Toda estrategia de release define **cómo se revierte** antes de aplicarse: volver a la versión anterior del artefacto, revertir la migración ([`03·D2`](../03-datos.md#d2--cada-cambio-de-esquema-es-una-migración-reversible)), restaurar datos. Preferir releases graduales (canario/azul-verde) cuando el riesgo lo amerite. Un release sin rollback pensado no está listo.
```
INCORRECTO: se despliega y «si algo falla, vemos»
CORRECTO:   antes de aplicar está escrito cómo se vuelve a la versión anterior,
            con la migración inversa y el respaldo
```

Fuente: [18·DP5](../18-despliegue-e-infraestructura.md#dp5--release-reversible-con-plan-de-vuelta)

## DP7 · La app expone su salud
El servicio ofrece un punto de **readiness/health** (¿está vivo?, ¿listo para recibir tráfico?) para que el pipeline y el orquestador decidan sin adivinar si el release quedó bien. Migraciones y arranque no dejan el servicio a medias: o queda sano, o el release falla y se revierte.
```
INCORRECTO: el orquestador enruta tráfico a una instancia que todavía está migrando
CORRECTO:   el punto de readiness responde «no listo» hasta que la migración termina
```

Fuente: [18·DP7](../18-despliegue-e-infraestructura.md#dp7--la-app-expone-su-salud)

## OB1 · Logs estructurados y correlacionables
Los logs se emiten como **datos** (clave-valor o JSON), no como texto libre: nivel, marca de tiempo y un **identificador de correlación** para seguir una operación de punta a punta. Nunca llevan secretos ni datos sensibles ([`05·E5`](../05-errores-y-logging.md#e5--nunca-registres-secretos-ni-datos-sensibles), [`00·N6`](../00-nucleo-blindado.md#n6--una-credencial-no-se-escribe-no-se-registra-y-no-se-guarda-blindada)).
```
INCORRECTO: imprimir «error procesando pedido» con el pedido entero, en texto libre
CORRECTO:   un registro con nivel, hora, identificador de correlación y el id del
            pedido; nada del cliente
```

Fuente: [19·OB1](../19-observabilidad-y-operacion.md#ob1--logs-estructurados-y-correlacionables)

## OB2 · Se mide lo que le duele al usuario
La instrumentación cubre las **señales doradas** del servicio: latencia, tráfico, errores y saturación. Las trazas permiten seguir una petición por los componentes que atraviesa. Se mide el **síntoma que sufre el usuario** (una página que no carga), no solo recursos internos (CPU) que no dicen si el sistema sirve.
```
INCORRECTO: el tablero muestra la CPU al 40 % mientras los usuarios ven páginas en blanco
CORRECTO:   se mide la latencia y la tasa de error que sufre el usuario, y de ahí salen
            las alertas
```

Fuente: [19·OB2](../19-observabilidad-y-operacion.md#ob2--se-mide-lo-que-le-duele-al-usuario)

## OB3 · SLO y alertas como código, sobre síntomas
Los objetivos de servicio (SLO) y las alertas se declaran **versionados**, no a mano en un tablero. Una alerta se dispara por un **síntoma que exige acción humana**, no por ruido que nadie atiende, y apunta a su runbook ([`19·OB4`](../19-observabilidad-y-operacion.md#ob4--runbooks-para-lo-que-se-opera)).
```
INCORRECTO: una alerta por cada pico de CPU, que todos aprenden a silenciar
CORRECTO:   una alerta cuando el error del usuario supera el umbral, versionada y con
            su runbook
```

Fuente: [19·OB3](../19-observabilidad-y-operacion.md#ob3--slo-y-alertas-como-código-sobre-síntomas)

## AU1 · Lo que el proceso hace se separa de dónde lo hace
La **secuencia de negocio** —qué pasos se dan y en qué orden— vive aparte de **cómo se alcanza cada elemento** de la pantalla. Cuando el sistema del otro lado cambia de aspecto, se toca solo el segundo.
```
INCORRECTO: la secuencia lleva incrustada la posición del botón, y mover
            el botón obliga a reescribir el proceso entero
CORRECTO:   la secuencia dice «confirmar», y en otro sitio está cómo se
            alcanza «confirmar» hoy
```

Fuente: [21·AU1](../21-automatizacion-de-procesos.md#au1--lo-que-el-proceso-hace-se-separa-de-dónde-lo-hace)

## AU2 · El elemento se alcanza por lo que es, no por dónde está
Cada elemento con el que el proceso interactúa se identifica por **algo que lo describa** —su nombre, su etiqueta, su papel en la pantalla—, nunca por su posición ni por una coordenada. La posición cambia con la resolución, el idioma y la versión; lo que el elemento *es*, no.
```
INCORRECTO: hacer clic en la coordenada 340, 512
CORRECTO:   hacer clic en el elemento cuyo nombre es «Guardar»
```

Fuente: [21·AU2](../21-automatizacion-de-procesos.md#au2--el-elemento-se-alcanza-por-lo-que-es-no-por-dónde-está)

## AU3 · El trabajo se toma de una cola y cada ítem se cierra solo
El proceso no recorre una lista en memoria: **toma un ítem de una cola, lo termina y lo marca**, uno por uno. Así se sabe qué se hizo y qué no cuando algo se corta a la mitad, y otro puede seguir desde ahí.
```
INCORRECTO: se leen las 400 facturas al empezar y se procesan en un bucle;
            se corta en la 180 y nadie sabe cuáles quedaron hechas
CORRECTO:   cada factura es un ítem de la cola, y su estado dice si se hizo
```

Fuente: [21·AU3](../21-automatizacion-de-procesos.md#au3--el-trabajo-se-toma-de-una-cola-y-cada-ítem-se-cierra-solo)

## AU4 · El fallo del negocio y el fallo del sistema no se tratan igual
El ítem que **no debía procesarse** —le falta un dato, no cumple una condición— se aparta con su motivo y el proceso sigue. El fallo **del sistema** —la pantalla no cargó, se cayó la sesión— se reintenta, y si insiste se detiene. Confundirlos reintenta eternamente lo que nunca iba a funcionar.
```
INCORRECTO: la factura sin cliente hace fallar el proceso entero
CORRECTO:   esa factura se aparta con su motivo y las otras 399 siguen
```

Fuente: [21·AU4](../21-automatizacion-de-procesos.md#au4--el-fallo-del-negocio-y-el-fallo-del-sistema-no-se-tratan-igual)

## AU5 · El proceso no guarda con qué entra a ningún sistema
Las credenciales con las que el proceso entra a los sistemas se piden a un **almacén seguro en el momento de usarlas**, y no viven en su configuración, en su código ni en sus registros. Un proceso automático corre sin nadie mirando: si deja una clave escrita, la deja escrita para siempre.
```
INCORRECTO: la clave del sistema va en la configuración del proceso
CORRECTO:   el proceso la pide al almacén cuando la necesita y no la conserva
```

Fuente: [21·AU5](../21-automatizacion-de-procesos.md#au5--el-proceso-no-guarda-con-qué-entra-a-ningún-sistema)

## AU6 · Se prueba contra un entorno que no es el de verdad
El proceso se prueba contra **sistemas de prueba y datos inventados**, nunca contra los productivos. Lo que el entorno de prueba no puede reproducir se comprueba a mano y **queda escrito qué se comprobó así**.
```
INCORRECTO: se prueba «con cuidado» contra el sistema real, en horario de poco uso
CORRECTO:   se prueba contra el de prueba, y lo que solo existe en el real
            se verifica a mano y se anota
```

Fuente: [21·AU6](../21-automatizacion-de-procesos.md#au6--se-prueba-contra-un-entorno-que-no-es-el-de-verdad)

## AU8 · Una corrida que no se mira no está terminada
Cada corrida deja **cuántos ítems entraron, cuántos se completaron, cuántos se apartaron y por qué**, en un sitio que alguien mire. Un proceso que corre solo y falla en silencio deja de hacer su trabajo sin que nadie se entere, a veces por meses.
```
INCORRECTO: el proceso corre cada noche y nadie sabe que hace tres semanas
            aparta el 90 % de los ítems
CORRECTO:   el resumen de cada corrida queda a la vista, con lo apartado y su motivo
```

Fuente: [21·AU8](../21-automatizacion-de-procesos.md#au8--una-corrida-que-no-se-mira-no-está-terminada)

## IA1 · Todo modelo en marcha está en un inventario antes de recibir tráfico
El inventario dice **qué modelos hay corriendo**, y de cada uno: qué decide, quién lo puso, con qué datos aprendió y desde cuándo. Un modelo que no está en el inventario no se despliega.
```
INCORRECTO: el modelo entró con la funcionalidad; qué hay corriendo se
            averigua leyendo el código de cada servicio
CORRECTO:   el modelo está en el inventario antes de recibir su primera
            petición, con qué decide y de qué datos aprendió
```

Fuente: [22·IA1](../22-sistemas-que-aprenden-de-datos.md#ia1--todo-modelo-en-marcha-está-en-un-inventario-antes-de-recibir-tráfico)

## IA4 · Que el modelo sugiera y que el modelo ejecute se aprueban por separado
Pasar de **proponer** a **hacer** es una autorización nueva, aunque el modelo sea el mismo y acierte igual. Mientras sugiere, una persona filtra el error; cuando ejecuta, el error ya ocurrió.
```
INCORRECTO: el modelo venía sugiriendo bien seis meses, así que se le
            conecta la ejecución directa
CORRECTO:   ejecutar directo se autoriza aparte, con quién lo autorizó y
            qué pasa cuando se equivoque
```

Fuente: [22·IA4](../22-sistemas-que-aprenden-de-datos.md#ia4--que-el-modelo-sugiera-y-que-el-modelo-ejecute-se-aprueban-por-separado)

## IA6 · El modelo en marcha se vigila por si sigue acertando, no solo por si responde
La vigilancia de [`19`](../19-observabilidad-y-operacion.md) dice si el servicio está en pie. Acá se agrega **si las respuestas siguen sirviendo**: un modelo se desvía sin lanzar un solo error, porque cambió la realidad y no el código.
```
INCORRECTO: el tablero muestra disponibilidad y tiempo de respuesta, y
            de ahí se concluye que el modelo está bien
CORRECTO:   además se mide si acierta como el día que se aprobó, y hay un
            umbral con un aviso a la persona a cargo
```

Fuente: [22·IA6](../22-sistemas-que-aprenden-de-datos.md#ia6--el-modelo-en-marcha-se-vigila-por-si-sigue-acertando-no-solo-por-si-responde)

## ID1 · Trabaja con criterio de desarrollador senior
Resuelve cada decisión técnica dentro de lo pedido con el criterio del oficio, pragmático y meticuloso, y no con lo mínimo que funciona. Qué entra en lo pedido lo dice [`01·C30`](../01-conducta.md#c30--no-agregues-lo-que-no-se-pidió).
```
INCORRECTO: entregar lo mínimo que pasa y llamarlo terminado
CORRECTO:   entregar lo pedido como lo firmaría un senior del oficio, y decir qué
            quedó fuera
```

Fuente: [00·ID1](../00-identidad-y-rol/reglas/ID1-trabaja-con-criterio-de-desarrollador-senior.md#id1--trabaja-con-criterio-de-desarrollador-senior)

## ID3 · No des por entregado lo que no está terminado
No des por entregado un cambio hasta que cumpla su especificación ([`02·F2`](../02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md)), sus pruebas corran en verde ([`08·T5`](../08-pruebas.md#t5--ejecuta-y-reporta)), no rompa lo existente ([`02·F7`](../02-flujo-de-trabajo/reglas/F7-no-cierres-una-fase-con-trazabilidad-incompleta.md)) y deje rastro escrito para la próxima sesión ([`13·DOC1`](../13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)). Si falta una de las cuatro, reporta qué falta — no cierres.
```
INCORRECTO: "listo" con las pruebas escritas pero sin correr, y la doc para después
CORRECTO:   "listo" = especificación cumplida + pruebas verdes 9/9 + nada roto + rastro escrito
```

Fuente: [00·ID3](../00-identidad-y-rol/reglas/ID3-no-des-por-entregado-lo-que-no-esta-terminado.md#id3--no-des-por-entregado-lo-que-no-está-terminado)

## F19 · Implementa literal el criterio de aceptación
La implementación hace **literal** lo que dice el CA aprobado: ni más, ni menos, ni "más seguro por si acaso" (extiende [`02·F18`](../02-flujo-de-trabajo/reglas/F18-deriva-el-plan-de-los-ca-aprobados-no-de-la-proactividad.md) · deroga [`02·F4.5`](../02-flujo-de-trabajo/reglas/F4.5-implementa-literal-el-ca-y-propon-lo-que-sobre.md)). La redacción del CA es la especificación funcional: el agente no la interpreta libremente ni la endurece por su cuenta.
```
INCORRECTO: el CA pide un listado de clientes, y se le agrega una exportación
            a hoja de cálculo «porque todo listado la trae»
CORRECTO:   se implementa el listado que el CA dice, tal cual
```

Fuente: [02·F19](../02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md#f19--implementa-literal-el-criterio-de-aceptación)

## F2 · Sin especificación acordada no hay código
Ningún desarrollo, refactor o migración sin una **especificación acordada** que lo respalde —alcance, reglas de negocio, datos, pruebas, permisos—. Si no existe, el agente **no toca código**: ofrece redactar el borrador y lo hace aprobar primero. Sin especificación, el código es opinión del agente.
```
INCORRECTO: "hacé que el módulo permita X" → escribo código directo
CORRECTO:   busco X en la especificación → si no está: "no está en la especificación; ¿lo agrego a la fase Y
            o es dominio nuevo?" → aprueban → actualizo especificación → implemento + pruebas
```

Fuente: [02·F2](../02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md#f2--sin-especificación-acordada-no-hay-código)
