# Reglas de la tarea `cambiar-codigo`, parte 2 de 4

Lo escribe `validadores/mapa_tareas.py` desde las reglas de `base/`: no se edita a mano. Son las reglas que [base/mapa-de-tareas.md](../mapa-de-tareas.md) pone bajo esta tarea, completas. Las que llevan *opt-in* rigen solo si el proyecto encendió su capítulo en el punto 5.1 de su `CLAUDE.md`.

## E6 · Lo que toca varios registros va en transacción
La operación que deja **varios registros consistentes entre sí** se hace en una transacción: todo o nada. Si falla a la mitad, no queda la mitad (extiende [`05·E2`](../05-errores-y-logging.md#e2--valida-al-entrar-y-aborta-temprano)).
```
INCORRECTO: se descuenta del inventario y falla al escribir el movimiento
            → el inventario quedó mal y nadie lo sabe
CORRECTO:   las dos escrituras van juntas; si una falla, ninguna queda
```

Fuente: [05·E6](../05-errores-y-logging.md#e6--lo-que-toca-varios-registros-va-en-transacción)

## E3 · Mensajes en dos niveles: usuario y diagnóstico
- **Al usuario:** claro, en su idioma, **accionable** ("Ese correo ya está registrado"), sin jerga ni internos.
- **Al log:** el detalle completo (excepción, contexto, id de correlación).
- **Nunca** trazas/consultas/rutas al usuario (es fuga de info — [`04·S8`](../04-seguridad.md#s8--no-filtres-información-en-errores)).
```
INCORRECTO: al usuario: "SQLSTATE[23000]... INSERT INTO..."
CORRECTO:   al usuario: "Ese registro ya existe."  ·  al log: la excepción completa
```

Fuente: [05·E3](../05-errores-y-logging.md#e3--mensajes-en-dos-niveles-usuario-y-diagnóstico)

## E4 · Loguea con niveles y con propósito
Cada registro lleva su nivel —**error** lo que pide atención, **warning** lo anómalo ya manejado, **info** el hito, **debug** el detalle, apagado en producción— y el contexto que lo hace rastreable: identificadores de entidad, usuario, correlación. Loguear de más entierra la señal.
```
INCORRECTO: log.error("error")
CORRECTO:   log.error("Falló causar factura", { factura_id, usuario_id, causa })
```

Fuente: [05·E4](../05-errores-y-logging.md#e4--loguea-con-niveles-y-con-propósito)

## E5 · Nunca registres secretos ni datos sensibles
Blindado en [`00·N6`](../00-nucleo-blindado.md#n6--una-credencial-no-se-escribe-no-se-registra-y-no-se-guarda-blindada). Los logs no llevan contraseñas, tokens, ni más datos personales de los necesarios. Enmascara o excluye. Trata el log como potencialmente público.
```
INCORRECTO: log.info("Login", { email, password })
CORRECTO:   log.info("Login", { usuario_id })
```

Fuente: [05·E5](../05-errores-y-logging.md#e5--nunca-registres-secretos-ni-datos-sensibles)

## R1 · Evita consultas en bucle (N+1)
No ejecutes una consulta por cada elemento de una lista. Carga las relaciones por adelantado (**eager loading**). Prefiere un join o un `IN (...)` a N consultas.
```
INCORRECTO: for (factura in facturas) { imprimir(factura.cliente.nombre) }  // 1 + N
CORRECTO:   cargar facturas con su cliente por adelantado → 1-2 consultas
```

Fuente: [06·R1](../06-rendimiento.md#r1--evita-consultas-en-bucle-n1)

## R2 · Nunca cargues conjuntos sin límite
- Toda lista para el usuario va **paginada**.
- Procesa grandes volúmenes **por lotes** (chunking), no todo en memoria.
- Trae **solo las columnas necesarias**, no `SELECT *` para tres campos.
```
INCORRECTO: cargar 200.000 registros en la vista y renderizarlos todos
CORRECTO:   paginar (25-50 por página) y consultar solo lo visible
```

Fuente: [06·R2](../06-rendimiento.md#r2--nunca-cargues-conjuntos-sin-límite)

## R3 · Índices en lo que se filtra y ordena
Las columnas por las que se filtra, une u ordena seguido llevan **índice** (FKs, fechas, estados, búsqueda). Uno de más frena las escrituras; uno de menos vuelve la consulta un escaneo completo. Indexa según el patrón real, no "por si acaso".
```
INCORRECTO: filtrar por fecha sin índice en una tabla grande → escaneo completo
CORRECTO:   índice en la columna de fecha del filtro
```

Fuente: [06·R3](../06-rendimiento.md#r3--índices-en-lo-que-se-filtra-y-ordena)

## R4 · Cachea lo caro y estable, con invalidación clara
Cachea lo **caro** que **cambia poco** (catálogos, agregados pesados, consultas frecuentes idénticas). Define **cuándo se invalida** desde el diseño: sin eso, la caché sirve datos viejos. Invalídala en el evento que cambia el dato de origen.
```
INCORRECTO: cachear un saldo y no invalidarlo nunca
CORRECTO:   cachearlo e invalidarlo en el evento que lo modifica
```

Fuente: [06·R4](../06-rendimiento.md#r4--cachea-lo-caro-y-estable-con-invalidación-clara)

## R5 · Trabajo pesado fuera del ciclo de petición
Lo que tarda (correos, reportes grandes, servicios externos lentos, procesamiento masivo) va a **segundo plano / cola**, no bloquea la respuesta.
```
INCORRECTO: enviar 5.000 correos dentro de la petición → timeout
CORRECTO:   encolar → responder de inmediato → procesar aparte
```

Fuente: [06·R5](../06-rendimiento.md#r5--trabajo-pesado-fuera-del-ciclo-de-petición)

## R6 · Mide antes de optimizar
Ante lentitud, **mide** (profiler, tiempos, conteo de consultas) para hallar el cuello real, no optimices por corazonada. No sacrifiques legibilidad por micro-optimizaciones sin impacto medible (`07`). Las ineficiencias de arriba (N+1, sin paginar, sin índice) son evidentes y se evitan desde el diseño.
```
INCORRECTO: reescribir "porque parece lento", sin medir, y romper legibilidad
CORRECTO:   medir → localizar el cuello → optimizar ahí → volver a medir
```

Fuente: [06·R6](../06-rendimiento.md#r6--mide-antes-de-optimizar)

## Q1 · Escribe como el código que lo rodea
El código nuevo imita al vecino: mismas convenciones, mismos nombres, mismo idioma ([`01·C8`](../01-conducta.md#c8--habla-el-idioma-del-proyecto)). No metas un paradigma ajeno sin acordarlo. La consistencia vale más que la preferencia personal.
```
INCORRECTO: el archivo nuevo trae un estilo distinto al del módulo
CORRECTO:   se mimetiza con el código vecino
```

Fuente: [07·Q1](../07-calidad-de-codigo.md#q1--escribe-como-el-código-que-lo-rodea)

## Q2 · Nombres que dicen la intención
Nombres descriptivos por lo que representan o hacen, no por su tipo ni abreviados. Evita genéricos (`data`, `temp`, `proceso`). Funciones con verbo; booleanos como afirmación (`estaActivo`, `tienePermiso`). Un buen nombre ahorra un comentario.
```
INCORRECTO: function proc(d) { ... }
CORRECTO:   function calcularSaldoDisponible(cuenta) { ... }
```

Fuente: [07·Q2](../07-calidad-de-codigo.md#q2--nombres-que-dicen-la-intención)

## Q3 · Funciones pequeñas, una responsabilidad
Cada función hace **una cosa**, a un solo nivel de abstracción. Si necesita comentarios que separan bloques, esos bloques son funciones. Usa retornos tempranos en vez de pirámides de `if`.
```
INCORRECTO: una función de 200 líneas que valida, calcula, guarda y notifica
CORRECTO:   una que orquesta validar(), calcular(), guardar(), notificar()
```

Fuente: [07·Q3](../07-calidad-de-codigo.md#q3--funciones-pequeñas-una-responsabilidad)

## Q4 · No repitas (DRY), pero no abstraigas de más
Lógica de negocio duplicada se extrae a un punto único. **Pero** no abstraigas prematuro: dos usos parecidos no siempre son el mismo concepto. Duplicar una vez y esperar el patrón es válido.
```
INCORRECTO: la misma regla copiada en tres lados → se corrige en dos y se olvida el tercero
CORRECTO:   la regla en un servicio; los tres lo llaman
```

Fuente: [07·Q4](../07-calidad-de-codigo.md#q4--no-repitas-dry-pero-no-abstraigas-de-más)

## Q5 · Comenta el porqué, no el qué
El código dice **qué**; el comentario, **por qué** (una decisión no obvia, un workaround). No comentes lo que el código ya dice. Las decisiones de diseño van a la documentación (`13`), no a un comentario que nadie relee.
```
INCORRECTO: i = i + 1 // incrementa i
CORRECTO:   // reintenta 3 veces porque el servicio externo falla intermitente
```

Fuente: [07·Q5](../07-calidad-de-codigo.md#q5--comenta-el-porqué-no-el-qué)

## Q6 · Linter y formateador automáticos
El estilo lo resuelve una **herramienta**, no el criterio manual. Entrega el código formateado y sin advertencias del linter. No desactives reglas para "que pase" ([`00·N3`](../00-nucleo-blindado.md#n3--no-romper-cosas-para-pasar-un-obstáculo-blindada)); si una estorba, ajusta la config, no la silencies caso por caso.
```
INCORRECTO: el linter marca una regla molesta y se silencia con un comentario
            en cada uno de los doce sitios donde aparece
CORRECTO:   se decide si la regla aplica al proyecto; si no, se apaga en la
            config, una vez y a la vista de todos
```

Fuente: [07·Q6](../07-calidad-de-codigo.md#q6--linter-y-formateador-automáticos)

## Q7 · Deja el código mejor, pero en tu alcance
Corregir algo pequeño y cercano está bien; mejorar de paso lo que no es de la tarea sale del alcance ([`01·C3`](../01-conducta.md#c3--quédate-en-tu-tarea)) e infla el diff. Si algo cercano merece mejora, **dilo y déjalo para su tarea**.

Fuente: [07·Q7](../07-calidad-de-codigo.md#q7--deja-el-código-mejor-pero-en-tu-alcance)

## T1 · Todo cambio con lógica lleva prueba
Toda funcionalidad o corrección con lógica se acompaña de pruebas, y su plan se aprueba junto con el plan de trabajo ([`02·F4`](../02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)).

Fuente: [08·T1](../08-pruebas.md#t1--todo-cambio-con-lógica-lleva-prueba)

## T2 · Prueba el comportamiento, no la implementación
Verifica **lo que el sistema hace** (la validación rechaza el input, el cálculo da el resultado, el usuario ve el mensaje), no los detalles internos. Una prueba atada a la implementación se rompe con cada refactor. Cubre: caso feliz, límites, errores, permisos, validaciones.
```
INCORRECTO: la prueba verifica que se llamó a tal método interno en tal orden
CORRECTO:   dado el input X, la respuesta/efecto es Y
```

Fuente: [08·T2](../08-pruebas.md#t2--prueba-el-comportamiento-no-la-implementación)

## T3 · Aisladas, deterministas, repetibles
- **Independiente:** corre sola y en cualquier orden, sin depender de otra.
- **Determinista:** mismo input → mismo resultado. Nada de **flaky** por reloj, azar, red o carreras (fija fechas, semillas, usa dobles).
- Aísla dependencias externas (terceros, correo, pagos) con dobles; no golpees sistemas reales.
```
INCORRECTO: prueba que depende de la fecha de hoy y falla el día 31
CORRECTO:   fijar la fecha para que el resultado sea estable
```

Fuente: [08·T3](../08-pruebas.md#t3--aisladas-deterministas-repetibles)

## T4 · Protege los datos reales al probar
Las pruebas corren contra un entorno **efímero y aislado**, creado y destruido por ejecución, nunca contra datos reales, y el agente no reapunta la configuración a datos reales aunque se lo sugieran. Lo que ese entorno no reproduce se verifica a mano y queda escrito, sin relajar el aislamiento (depende de [`00·N4`](../00-nucleo-blindado.md#n4--nada-destructivo-sobre-datos-reales-sin-autorización-de-esa-operación-blindada)).
```
INCORRECTO: «para que la prueba tenga datos de verdad» se apunta la suite a la base de producción
CORRECTO:   la suite levanta su base efímera; lo que no se pueda reproducir se verifica a mano y queda escrito
```

Fuente: [08·T4](../08-pruebas.md#t4--protege-los-datos-reales-al-probar)

## T5 · Ejecuta y reporta
Las pruebas se **corren**, no solo se escriben ([`02·F5`](../02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)). Reporta el conteo. Si fallan: diagnostica, corrige, vuelve a correr. Nunca silencies/saltes/borres una para que pase ([`00·N3`](../00-nucleo-blindado.md#n3--no-romper-cosas-para-pasar-un-obstáculo-blindada)).
```
INCORRECTO: implementar + escribir pruebas + "listo"
CORRECTO:   implementar + escribir + EJECUTAR + "Verdes 4/4"
```

Fuente: [08·T5](../08-pruebas.md#t5--ejecuta-y-reporta)

## T6 · Cobertura con criterio, no por porcentaje
Prioriza la **lógica de negocio, las reglas y los caminos de error** — lo que duele si se rompe. No persigas un número con pruebas triviales (getters, "el framework funciona"). Una regla que vive en la app ([`03·D5`](../03-datos.md#d5--con-la-bd-desplegada-la-validación-nueva-va-en-la-app)) **debe** tener prueba dedicada.
```
INCORRECTO: pruebas que suben el porcentaje verificando un getter
CORRECTO:   pruebas sobre reglas, límites y errores que importan
```

Fuente: [08·T6](../08-pruebas.md#t6--cobertura-con-criterio-no-por-porcentaje)

## T7 · Los casos se derivan con método, no se eligen a ojo
Los casos de la lógica que calcula o decide salen de un método, no de la intuición: los **valores de frontera**, uno de **cada grupo que se comporta igual**, las **combinaciones** cuando varias condiciones se cruzan, y lo **inválido**. En lo crítico va la matriz; en el resto, al menos límites y errores.
```
INCORRECTO: tres casos que se le ocurrieron a quien escribió el código
CORRECTO:   los límites, un caso por grupo, las combinaciones que se cruzan,
            y lo que no debería aceptarse
```

Fuente: [08·T7](../08-pruebas.md#t7--los-casos-se-derivan-con-método-no-se-eligen-a-ojo)

## T8 · El resultado esperado no sale del código que se está probando
El valor que la prueba espera se confirma desde **fuentes independientes que coinciden** —la especificación, un cálculo hecho aparte—, **nunca leyendo lo que el código produce hoy**. Dos fuentes; tres si hay dinero, seguridad o consecuencias legales (extiende [`08·T7`](../08-pruebas.md#t7--los-casos-se-derivan-con-método-no-se-eligen-a-ojo)).
```
INCORRECTO: se corre la función, sale 1 240, y se escribe que el esperado es 1 240
CORRECTO:   se calcula aparte a partir de la especificación, da 1 260, y se
            descubre que el código estaba mal
```

Fuente: [08·T8](../08-pruebas.md#t8--el-resultado-esperado-no-sale-del-código-que-se-está-probando)

## G6 · Las pruebas y el linter corren solos en cada cambio propuesto
La suite y el linter corren en un **entorno reproducible que no depende de que alguien se acuerde**, sobre cada cambio propuesto, y la rama principal no admite lo que no está en verde.
```
INCORRECTO: «las corrí en mi máquina y pasaban» → se integra
CORRECTO:   corren solas sobre el cambio propuesto, y si algo falla no entra
```

Fuente: [09·G6](../09-git.md#g6--las-pruebas-y-el-linter-corren-solos-en-cada-cambio-propuesto)

## DEP1 · Agregar una dependencia es una decisión
Antes de sumar una librería: ¿la necesito o lo resuelvo con lo que ya tengo? ¿Está **mantenida** y es confiable? ¿Su **licencia** es compatible? ¿Cuánto **peso** y cuántas transitivas arrastra? Es una decisión funcional: el agente la **propone**, no la mete por su cuenta ([`01·C4`](../01-conducta.md#c4--no-decidas-por-tu-cuenta)).
```
INCORRECTO: sumar una librería pesada para formatear una fecha en un solo lugar
CORRECTO:   resolverlo con la utilidad estándar
```

Fuente: [10·DEP1](../10-dependencias.md#dep1--agregar-una-dependencia-es-una-decisión)

## DEP2 · Versiones fijadas y reproducibles
Fija versiones con el **lockfile** del ecosistema y **versiónalo**: todos (y producción) instalan lo mismo. No dependas de "la última" flotante. Actualiza **deliberado**, revisando cambios.
```
INCORRECTO: no versionar el lockfile → cada máquina instala versiones distintas
CORRECTO:   versionarlo → instalación idéntica en todos lados
```

Fuente: [10·DEP2](../10-dependencias.md#dep2--versiones-fijadas-y-reproducibles)

## DEP3 · Audita vulnerabilidades y mantén al día
Revisa las **vulnerabilidades conocidas** de las dependencias con la herramienta del ecosistema y no dejes ninguna sin resolver; quedarse muy atrás vuelve caro e inseguro actualizar después (deroga [`04·S7`](../04-seguridad.md#s7--dependencias-sin-vulnerabilidades-conocidas----derogada-en-23170--ver-10dep3): desde la 23.17.0 esta regla es la dueña del tema).
```
INCORRECTO: la auditoría reporta una vulnerabilidad alta y se anota «para la
            próxima», porque actualizar rompe dos pruebas
CORRECTO:   se arreglan las dos pruebas y se actualiza; si de verdad no se
            puede, queda escrito qué la mitiga y hasta cuándo
```

Fuente: [10·DEP3](../10-dependencias.md#dep3--audita-vulnerabilidades-y-mantén-al-día)

## DEP5 · Aísla la dependencia que puede cambiar
Una dependencia central y sustituible (cliente de pago, proveedor de correo) se **encapsula** detrás de una interfaz propia, en vez de esparcir llamadas directas. Cambiar de proveedor toca un punto, no cien. No lo sobre-apliques a utilidades estables y ubicuas.
```
INCORRECTO: el cliente del proveedor de correo llamado desde quince sitios;
            cambiar de proveedor toca los quince
CORRECTO:   un envío propio por delante; cambiar de proveedor toca ese
```

Fuente: [10·DEP5](../10-dependencias.md#dep5--aísla-la-dependencia-que-puede-cambiar)

## CFG1 · La configuración vive fuera del código
Lo que cambia entre entornos (credenciales, URLs, claves, flags de entorno) se lee de la **configuración de entorno**. El mismo código corre en todos lados; cambia la config que recibe. Secretos, nunca en el código ([`00·N6`](../00-nucleo-blindado.md#n6--una-credencial-no-se-escribe-no-se-registra-y-no-se-guarda-blindada), [`04·S4`](../04-seguridad.md#s4--guarda-los-secretos-fuera-del-código-y-rota-el-que-se-expuso)).
```
INCORRECTO: la URL del servicio de pago en el código con un if por entorno
CORRECTO:   leerla de la configuración; cada entorno trae la suya
```

Fuente: [11·CFG1](../11-configuracion-entornos.md#cfg1--la-configuración-vive-fuera-del-código)

## CFG2 · El entorno real no se versiona; sí una plantilla
El archivo con valores reales está **ignorado** ([`09·G3`](../09-git.md#g3--deja-fuera-del-control-de-versiones-los-secretos-y-lo-generado)). Se versiona una **plantilla de ejemplo** con todas las variables **sin valores**, y se documenta qué es cada una y cuáles son obligatorias.
```
INCORRECTO: versionar el archivo de entorno con las claves reales
CORRECTO:   versionar la plantilla vacía; el real queda en cada entorno
```

Fuente: [11·CFG2](../11-configuracion-entornos.md#cfg2--el-entorno-real-no-se-versiona-sí-una-plantilla)

## CFG3 · Los entornos se parecen lo suficiente para que probar signifique algo
El entorno donde se prueba corre **las mismas versiones y la misma configuración estructural** que el de producción. Sin eso, «funciona en mi máquina» no dice nada, y lo que no se puede reproducir se cubre con comprobaciones manuales escritas ([`08·T4`](../08-pruebas.md#t4--protege-los-datos-reales-al-probar)).
```
INCORRECTO: se prueba contra una versión distinta del motor «porque es lo que hay»
CORRECTO:   se iguala la versión, o se anota qué queda sin probar y cómo se comprueba
```

Fuente: [11·CFG3](../11-configuracion-entornos.md#cfg3--los-entornos-se-parecen-lo-suficiente-para-que-probar-signifique-algo)

## CFG4 · Cambios de comportamiento tras banderas
Funcionalidad que conviene activar/desactivar sin desplegar (en progreso, arriesgada, de un cliente) va tras una **bandera** (feature flag): permite apagar rápido sin revertir código. Limpia las banderas obsoletas — una eterna es deuda.
```
INCORRECTO: la bandera se enciende al liberar y nadie la quita; dos años después
            nadie sabe si el código de abajo se ejecuta
CORRECTO:   la bandera nace con la fecha en que se retira, y al retirarla se borra
            también la rama que ya no se usa
```

Fuente: [11·CFG4](../11-configuracion-entornos.md#cfg4--cambios-de-comportamiento-tras-banderas)

## PR1 · Recolecta solo lo necesario (minimización)
No pidas ni guardes datos personales que la función no necesita. Cada dato guardado es riesgo y responsabilidad. Prefiere el dato menos sensible que resuelva el problema.
```
INCORRECTO: guardar documento y dirección "por si acaso"
CORRECTO:   guardar solo lo que la función usa de verdad
```

Fuente: [12·PR1](../12-privacidad-datos.md#pr1--recolecta-solo-lo-necesario-minimización)

## PR2 · Úsalos solo para lo que se recolectaron
Los datos se usan para el propósito con que se obtuvieron. No los reutilices para otro fin (analítica, marketing, terceros) sin base legítima y consentimiento. No los envíes a servicios externos sin autorización ([`00·N6`](../00-nucleo-blindado.md#n6--una-credencial-no-se-escribe-no-se-registra-y-no-se-guarda-blindada)).
```
INCORRECTO: los correos se pidieron para avisar del pedido y se usan para una
            campaña, porque «ya los tenemos»
CORRECTO:   para la campaña se pide consentimiento aparte, y quien no lo da
            sigue recibiendo el aviso del pedido
```

Fuente: [12·PR2](../12-privacidad-datos.md#pr2--úsalos-solo-para-lo-que-se-recolectaron)

## PR3 · Protégelos en reposo y en tránsito
**El dato personal se trata como sensible aunque nadie lo haya clasificado así**: le aplican las mismas protecciones que el capítulo [`04`](../04-seguridad.md) exige para lo sensible —cifrado en tránsito, almacenamiento restringido, acceso por permiso—, sin esperar a que el proyecto lo declare.

Fuente: [12·PR3](../12-privacidad-datos.md#pr3--protégelos-en-reposo-y-en-tránsito)

## PR4 · No los expongas en logs, errores ni mensajes
Lo que se muestra en pantalla también expone: un mensaje a otro usuario no filtra datos de terceros, y un reporte o una pantalla solo los enseña a quien tiene derecho. En logs y errores rige [`05·E5`](../05-errores-y-logging.md#e5--nunca-registres-secretos-ni-datos-sensibles) (depende de `05·E5`).
```
INCORRECTO: el reporte de incidencias muestra el teléfono del denunciante a
            cualquiera que abra la pantalla, porque «ya está en la base»
CORRECTO:   el reporte muestra el dato solo a quien tiene derecho a verlo; al
            resto le llega el caso sin el dato de contacto
```

Fuente: [12·PR4](../12-privacidad-datos.md#pr4--no-los-expongas-en-logs-errores-ni-mensajes)

## PR5 · Define cuánto se conservan y qué pasa después
Define **cuánto tiempo** se conservan; no indefinido "porque sí". Prevé **borrado o anonimización** cuando ya no se necesitan o la persona lo pide. Si el registro tiene valor legal/contable que impide borrarlo (`15`), **anonimiza** los datos personales conservando el registro. Documenta la decisión.
```
INCORRECTO: conservar para siempre los datos de cuentas inactivas
CORRECTO:   retención definida + borrado/anonimización al cumplirse el plazo
```

Fuente: [12·PR5](../12-privacidad-datos.md#pr5--define-cuánto-se-conservan-y-qué-pasa-después)

## EST1 · Organiza el código nuevo por módulo, en ubicación predecible
Cada elemento nuevo (modelo, componente, servicio, prueba, vista) vive en una ubicación **predecible** según su módulo y tipo. Todo el módulo en un lugar, no disperso.
Así: se localiza cualquier archivo por convención; borrar un módulo es borrar una carpeta; un dev nuevo abre la carpeta y ve el dominio de un vistazo.
```
INCORRECTO: archivos de un módulo dispersos por carpetas globales según tipo
CORRECTO:   el módulo agrupado en una ubicación predecible
```

Fuente: [14·EST1](../14-estructura-codigo.md#est1--organiza-el-código-nuevo-por-módulo-en-ubicación-predecible)

## EST2 · Nomenclatura consistente
**Una sola convención por tipo de elemento** —tablas, columnas, clases, archivos, permisos—, aplicada igual en todos: eso hace que el nombre se **adivine** sin buscarlo. Cortos, con significado por contexto, sin repetir lo que la ubicación ya dice.
```
INCORRECTO: booleano "es_socio_principal_del_grupo_familiar"
CORRECTO:   "es_principal" — el contexto de la tabla ya aclara

INCORRECTO: dejar autogenerar el índice en una tabla de nombre largo → excede el límite
CORRECTO:   pasar un nombre corto y explícito
```

Fuente: [14·EST2](../14-estructura-codigo.md#est2--nomenclatura-consistente)

## EST3 · Respeta el legacy — la convención es para lo nuevo
Las convenciones aplican a lo **nuevo**. El código existente que no las sigue **no se renombra ni se mueve** solo para ordenar: sale del alcance ([`01·C3`](../01-conducta.md#c3--quédate-en-tu-tarea)). Migrar legacy es tarea **propia y acordada**, no efecto colateral.
```
INCORRECTO: mover y renombrar legacy "de paso" mientras hago otra cosa
CORRECTO:   crear lo nuevo con la convención; dejar el legacy intacto salvo tarea explícita
```

Fuente: [14·EST3](../14-estructura-codigo.md#est3--respeta-el-legacy--la-convención-es-para-lo-nuevo)

## IM1 · Un registro materializado es inmutable
Cuando un registro ya surtió efecto (movimiento contable generado, pago aplicado, saldo afectado, documento emitido), **no se edita ni se borra físico**. La única operación válida es **anular con motivo y trazabilidad**. En borrador (aún no materializado) sí se edita.
```
INCORRECTO: editar un documento materializado con un update, sin revertir su efecto
CORRECTO:   anularlo (con motivo, revirtiendo el efecto en transacción) y preservar la fila
```

Fuente: [15·IM1](../15-registros-inmutables.md#im1--un-registro-materializado-es-inmutable)

## IM2 · El registro tiene tres estados y solo uno es editable
El registro pasa por **borrador**, que se edita; **materializado**, que ya no; y **anulado**, que revierte el efecto **conservando la fila**. Nada se borra para corregirlo: se anula y se rehace.
```
INCORRECTO: la factura salió mal, se edita el registro ya emitido
CORRECTO:   se anula la emitida —queda su fila— y se emite otra
```

Fuente: [15·IM2](../15-registros-inmutables.md#im2--el-registro-tiene-tres-estados-y-solo-uno-es-editable)
