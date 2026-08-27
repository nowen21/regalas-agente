
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
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Salió de un caso real: se aprobaron tres documentos y al día siguiente el cambio de producto los dejó sin valor |

### Registrar cada acción que se hace

| Campo | Valor |
|---|---|
| **Identificador** | `F-018` |
| **De qué se trata** | Guardar qué se hizo sobre proyectos, documentos y reglas: quién, cuándo y sobre qué |
| **Para qué sirve** | Poder rastrear cualquier cambio hasta quién lo hizo |
| **Parte del sistema** | Auditoría |
| **Quién la usa** | El sistema solo, cada vez que algo cambia |
| **Qué recibe** | La acción que se acaba de ejecutar |
| **Qué entrega** | El registro guardado |
| **Reglas que debe respetar** | `RN-9` nada de lo registrado incluye credenciales |
| **Depende de** | F-001 |
| **Terminada cuando** | `CA-1` toda acción que cambia algo queda registrada · `CA-2` el registro dice quién, cuándo y sobre qué · `CA-3` lo registrado no se puede editar |
| **Qué necesita construirse** | Lógica y almacenamiento |
| **Prioridad** | Alta |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Registrar cada mensaje de la sesión pesa mucho y sirve poco. Qué se registra exactamente es la duda 2 del análisis |

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
| **Estado** | Definida |
| **Verificado** | Sin verificar |
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
| **Estado** | Definida |
| **Verificado** | Sin verificar |
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
| **Estado** | Definida |
| **Verificado** | Sin verificar |
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
| **Estado** | Definida |
| **Verificado** | Sin verificar |
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
| **Estado** | Definida |
| **Verificado** | Sin verificar |
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
| **Estado** | Definida |
| **Verificado** | Sin verificar |
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
| **Estado** | Definida |
| **Verificado** | Sin verificar |
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
| **Estado** | Definida |
| **Verificado** | Sin verificar |
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
| **Estado** | Definida |
| **Verificado** | Sin verificar |
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
| **Estado** | Definida |
| **Verificado** | Sin verificar |
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
| **Estado** | Definida |
| **Verificado** | Sin verificar |
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
| **Estado** | Definida |
| **Verificado** | Sin verificar |
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
| **Estado** | Definida |
| **Verificado** | Sin verificar |
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
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | La medición inicial debió tomarse antes de empezar y no se tomó: sin ella pierde la mitad del valor |

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
