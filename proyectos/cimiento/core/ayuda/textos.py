"""Los textos de la ayuda en cada campo y en cada pantalla, en un solo lugar (`EP-025·HU-018`).

Se escriben para que los entienda cualquiera (`00·ID7`): palabras de todos los
días, frases cortas, tercera persona para lo que se explica e infinitivo para lo
que se hace (`00·ID10`).

CAMPOS: la ayuda del «?» junto a una etiqueta.
    titulo    la pregunta que responde el globo.
    secciones lista de (encabezado, texto o lista de textos).
    consejo   frase final opcional, en el recuadro amarillo.

PANTALLAS: la ayuda de los botones debajo del título de una pantalla.
    para_que   texto, ejemplo y por_que (los dos últimos opcionales).
    donde_mas  texto y pantallas: nombre, detalle y ruta en el menú.
    como_encaja mapa: pasos antes, aquí y después.
"""
from core.proyectos.ajustes import CAPITULOS_OPT_IN

CAMPOS = {
    "configuracion.rutas_en_avisos": {
        "titulo": "¿Cómo salen las rutas en los avisos?",
        "secciones": [
            ("Las opciones", ["Relativas: desde la carpeta del proyecto, por ejemplo base/02-flujo/F8.md.",
                              "Completas: con la unidad y todas las carpetas, por ejemplo C:/proyecto/base/02-flujo/F8.md."]),
        ],
        "consejo": "Vacío, vale el de fábrica: relativas. Cada proyecto puede poner el suyo en «Proyectos» → «Editar».",
    },
    "configuracion.limite_enganche": {
        "titulo": "¿Qué es el límite por enganche?",
        "secciones": [
            ("¿Qué es?", "Cuántos tokens puede agregar un enganche en un mensaje antes de que Cimiento avise."),
            ("Ejemplo", "Con 2.000, si el enganche de las reglas agrega 3.500 tokens, el mensaje siguiente lo avisa."),
        ],
        "consejo": "El aviso no detiene nada: sirve para decidir qué achicar o pasar a un programa.",
    },
    "configuracion.limite_archivo": {
        "titulo": "¿Qué es el límite por archivo?",
        "secciones": [
            ("¿Qué es?", "Cuántos tokens puede ocupar un archivo cuando el agente lo lee, antes de que Cimiento avise."),
            ("Ejemplo", "Con 10.000, leer un análisis de 14.000 tokens queda avisado en el mensaje siguiente."),
        ],
    },
    "suspension.tipo": {
        "titulo": "¿Qué se puede suspender?",
        "secciones": [
            ("Las opciones", ["Una regla: deja de frenar solo esa regla en este proyecto.",
                              "El freno entero: deja pasar todo lo que frena, menos el núcleo."]),
        ],
        "consejo": "El núcleo del estándar y el histórico no se suspenden nunca: protegen los datos y las claves.",
    },
    "suspension.nombre": {
        "titulo": "¿Qué regla se escribe?",
        "secciones": [
            ("¿Qué es?", "El código de la regla, tal como sale en el aviso del freno."),
            ("Ejemplo", "02·F8"),
        ],
        "consejo": "Si se suspende el freno entero, este campo no se llena.",
    },
    "suspension.motivo": {
        "titulo": "¿Por qué se pide el motivo?",
        "secciones": [
            ("¿Qué es?", "La razón de dejar pasar algo que el freno detendría. Queda guardada con quién suspendió y cuándo."),
            ("Ejemplo", "Corregir el andamio, que no está en el plan de ninguna fase abierta."),
        ],
    },
    "suspension.vence": {
        "titulo": "¿Hasta cuándo dura?",
        "secciones": [
            ("¿Qué es?", "El día y la hora en que la suspensión deja de valer sola."),
            ("Límite", "A lo sumo 30 días desde hoy."),
        ],
        "consejo": "Se puede terminar antes con «Levantar».",
    },
    # `EP-028·HU-004` · Las dos preguntas del tipo de versión (`20·M10`).
    "version.obliga": {
        "titulo": "¿Algún proyecto tiene que cambiar algo?",
        "secciones": [
            ("¿Qué se pregunta?", "Si un proyecto que hoy cumple el estándar tiene que hacer algo nuevo para seguir cumpliéndolo."),
            ("Ejemplos de «Sí»", ["Una regla nueva que todos deben cumplir.", "Un capítulo que deja de ser opcional."]),
            ("Ejemplos de «No»", ["Una guía o una plantilla nueva.", "Corregir la redacción de una regla."]),
        ],
        "consejo": "«Sí» da una versión MAYOR, y la segunda pregunta ya no hace falta.",
    },
    "version.agrega": {
        "titulo": "¿Agrega algo nuevo que se puede usar si se quiere?",
        "secciones": [
            ("¿Qué se pregunta?", "Si el cambio trae algo nuevo que un proyecto puede aprovechar, sin estar obligado."),
            ("Ejemplos de «Sí»", ["Una guía, una plantilla o un recuerdo nuevo.", "Una regla opcional."]),
            ("Ejemplos de «No»", ["Corregir o aclarar un texto que ya existía.", "Agregar un enlace."]),
        ],
        "consejo": "«Sí» da una versión MENOR; «No», un PARCHE.",
    },
}

# `EP-026·HU-009` · Un globo por capítulo opt-in, todos con el mismo molde.
for _capitulo, _tema in CAPITULOS_OPT_IN.items():
    CAMPOS["configuracion.opt_in_%s" % _capitulo] = {
        "titulo": "¿Qué es el patrón opt-in %s?" % _capitulo,
        "secciones": [
            ("¿Qué es?", "Las reglas del capítulo %s, de %s. Rigen en el proyecto solo si está en «Sí»." % (_capitulo, _tema)),
            ("Ejemplo", "Con «Sí», un mensaje que pide algo de ese tema trae sus reglas; con «No», no las trae."),
        ],
        "consejo": "Vacío, vale el de la configuración de Cimiento, y si tampoco tiene, el de fábrica: «No». "
                   "La vista previa del estándar muestra cuáles tiene prendidos cada proyecto.",
    }

PANTALLAS = {
    "configuracion": {
        "para_que": {
            "texto": "Fijar el valor común de cada ajuste para todos los proyectos que no tienen el suyo.",
            "ejemplo": "Se quiere ver las rutas completas en todos los proyectos: se elige «Completas» aquí, "
                       "y solo el proyecto que dijo otra cosa en su edición la conserva.",
            "por_que": "Cambiar aquí cambia todos los proyectos sin valor propio, y su copia en .agente/configuracion.md.",
        },
        "donde_mas": {
            "texto": "Estos ajustes también se ven y se cambian en otras pantallas:",
            "pantallas": [
                {"nombre": "Editar un proyecto", "detalle": "pone el valor que manda solo para ese proyecto",
                 "ruta": ["Proyectos", "Editar"]},
                {"nombre": "Gasto", "detalle": "usa los límites para avisar lo que pesa demasiado",
                 "ruta": ["Gasto"]},
            ],
        },
        "como_encaja": {
            "mapa": [
                {"tipo": "antes", "titulo": "Lo de fábrica", "pasos": ["Valores de Cimiento"]},
                {"tipo": "aqui", "titulo": "La base común", "pantalla": "Configuración",
                 "pasos": ["Rutas en los avisos", "Límites de tokens"]},
                {"tipo": "despues", "titulo": "Lo que manda en cada proyecto", "pasos": [
                    "Valor propio del proyecto", "Suspensiones"]},
            ],
        },
    },
    "suspensiones": {
        "para_que": {
            "texto": "Dejar de frenar una regla, o el freno entero, en un proyecto, por un tiempo y con su motivo.",
            "ejemplo": "El freno detiene una corrección legítima que no está en el plan. Se suspende 02·F8 por un día "
                       "con el motivo, se hace la corrección y se levanta la suspensión.",
            "por_que": "Es la salida prevista ante un bloqueo: así nadie toca archivos a mano para pasar el freno.",
        },
        "como_encaja": {
            "mapa": [
                {"tipo": "antes", "titulo": "Lo que pasa primero", "pasos": ["El freno detiene", "Su aviso dice cómo salir"]},
                {"tipo": "aqui", "titulo": "Suspender", "pantalla": "Suspensiones",
                 "pasos": ["Qué se suspende", "Motivo", "Vencimiento"]},
                {"tipo": "despues", "titulo": "Después", "pasos": ["La acción pasa", "Levantar o dejar vencer"]},
            ],
        },
    },
}


# `EP-028·HU-005` · La ayuda de los formularios que nacieron después de la EP-025·HU-018.
def _campo(titulo, que, ejemplo=None, consejo=None):
    secciones = [("¿Qué es?", que)]
    if ejemplo:
        secciones.append(("Ejemplo", ejemplo))
    return {"titulo": titulo, "secciones": secciones, **({"consejo": consejo} if consejo else {})}


CAMPOS.update({
    "entrar.usuario": _campo("¿Qué usuario?", "El nombre de la cuenta con que se entra a Cimiento.",
                             consejo="Si no se tiene cuenta, la crea quien administra Cimiento."),
    "entrar.clave": _campo("¿Qué contraseña?", "La contraseña de esa cuenta. Se escribe sin que se vea."),
    "gasto.proyecto": _campo("¿De qué proyecto?", "El proyecto cuyo gasto de tokens se quiere ver; «Todos» los suma.",
                             "Escoger «scilit» para ver solo lo que gastó ese proyecto."),
    "gasto.dias": _campo("¿Qué período?", "Cuántos días hacia atrás se cuentan.", "«7 días» muestra la última semana."),
    # `EP-028·HU-007`, fase B · La ayuda de la franja y de las cinco pestañas del gasto.
    "gasto.total": _campo("¿Qué es el total del período?",
                          "Todos los tokens del período: los que entran, los que se escriben y se releen de caché, "
                          "y los que responde el modelo. Debajo, cuánto subió o bajó frente al tramo anterior, "
                          "cortado a la misma hora.", "Con «7 días», se compara con los 7 días de antes."),
    "gasto.llamadas": _campo("¿Qué son las llamadas?",
                             "Cuántas veces se le pidió algo al modelo. Un solo mensaje del usuario hace varias "
                             "llamadas: una por cada paso que da el agente."),
    "gasto.cache": _campo("¿Qué es lo releído de caché?",
                          "La parte del total que el modelo ya tenía guardada y volvió a leer. Es lo más barato.",
                          "Un 90 % quiere decir que casi todo lo que entra ya estaba guardado.",
                          "Si baja de golpe, algo está cambiando el comienzo de cada mensaje."),
    "gasto.contexto_maximo": _campo("¿Qué es el contexto más grande?",
                                    "La llamada que más tokens tuvo a la vista a la vez en el período.",
                                    consejo="Si se acerca al límite del modelo, la conversación se resume y se pierde detalle."),
    "gasto.por_dia": _campo("¿Qué muestra la gráfica por día?",
                            "Los tokens de cada día, apilados por tipo: entrada nueva, escrita en caché, "
                            "releída de caché y salida.", "Una barra muy alta muestra el día que más se gastó."),
    "gasto.por_tipo": _campo("¿Qué muestra la gráfica por tipo?",
                             "Cómo se reparte el total del período entre los cuatro tipos de token."),
    "gasto.candidatos": _campo("¿Qué es un candidato a automatizar?",
                               "Algo que se repite y gasta tokens cada vez: un archivo que se lee 3 veces o más, "
                               "un comando que se corre 3 veces o más, o un enganche que agrega texto en casi "
                               "todos los mensajes. Si lo hiciera un programa, ese gasto se ahorraría.",
                               "Un archivo leído 6 veces: con una lectura bastaría."),
    "gasto.veces": _campo("¿Qué son las veces?", "Cuántas veces pasó en el período."),
    "gasto.se_ahorrarian": _campo("¿Qué se ahorraría?",
                                  "Los tokens que dejarían de gastarse si un programa hiciera esto. Es un cálculo "
                                  "aproximado.", "Un archivo leído 4 veces ahorraría las 3 lecturas de más."),
    "gasto.gasta_hoy": _campo("¿Qué gasta hoy?", "Los tokens que esto gastó en el período, sumadas todas las veces."),
    "gasto.donde": _campo("¿Dónde se gasta más?",
                          "Las partes que más tokens gastaron, con su porcentaje del total.",
                          consejo="La pestaña «Dónde se gasta» deja agrupar de otras maneras."),
    "gasto.agrupar": _campo("¿Cómo se agrupa?",
                            "Escoge por qué se reparte el gasto: proyecto, palabra clave del mensaje, trabajo, "
                            "modelo o agente auxiliar.", "«Palabra clave» muestra cuánto gastan los «Hágalo» frente a las «pregunta»."),
    "gasto.porcentaje": _campo("¿Qué es el % del total?", "La parte del gasto del período que se llevó esta fila."),
    "gasto.tokens": _campo("¿Qué son los tokens?",
                           "Los pedacitos de texto que el modelo lee y escribe; por ellos se paga. Aquí van "
                           "todos sumados: entrada, caché y salida.", "Una palabra en español son más o menos 2 tokens."),
    "gasto.enganches": _campo("¿Qué son los enganches?",
                              "Los programas que corren solos en ciertos momentos (al enviar un mensaje, antes de "
                              "una acción) y le agregan texto al agente, como las reglas de cada mensaje. La cifra "
                              "es lo que agregaron en el período, estimado."),
    "gasto.archivos": _campo("¿Qué son los archivos leídos?",
                             "Lo que entró al contexto porque el agente leyó un archivo, estimado."),
    "gasto.otras_herramientas": _campo("¿Qué son las otras herramientas?",
                                       "Lo que entró al contexto por la respuesta de un comando, una búsqueda u otra "
                                       "herramienta que no es leer un archivo, estimado."),
    "gasto.limite_enganche": _campo("¿Qué es el límite por enganche?",
                                    "Cuántos tokens puede agregar un enganche en un mensaje antes de que Cimiento avise.",
                                    consejo="El límite se cambia en «Configuración», o en cada proyecto."),
    "gasto.limite_archivo": _campo("¿Qué es el límite por archivo?",
                                   "Cuántos tokens puede ocupar un archivo al leerlo antes de que Cimiento avise.",
                                   consejo="El límite se cambia en «Configuración», o en cada proyecto."),
    "gasto.promedio": _campo("¿Qué es el promedio?", "Lo que ocupó, en tokens, una vez cualquiera."),
    "gasto.maximo": _campo("¿Qué es el máximo?", "La vez que más tokens ocupó. Se compara con el límite."),
    "gasto.total_fila": _campo("¿Qué es el total?", "Todos los tokens que ocupó en el período, sumadas todas las veces."),
    "gasto.por_herramienta": _campo("¿Qué muestra por herramienta?",
                                    "Cada herramienta que usó el agente (leer, buscar, correr un comando...) con "
                                    "cuántas veces la usó y cuánto ocupó su respuesta."),
    "gasto.resultado": _campo("¿Qué es el resultado?", "Los tokens que ocupó la respuesta de la herramienta, estimados."),
    "gasto.enganche_gasta": _campo("¿Qué enganches gastan tokens?",
                                   "Los que agregan texto al agente: ese texto se paga en cada mensaje."),
    "gasto.enganche_no_gasta": _campo("¿Qué enganches no gastan tokens?",
                                      "Los que corren y no le agregan nada al agente, como el que guarda el histórico.",
                                      consejo="Pasar trabajo a un enganche de estos es lo que ahorra."),
    "gasto.corrio": _campo("¿Cuántas veces corrió?", "Las veces que el enganche se ejecutó en el período."),
    "gasto.tokens_agregados": _campo("¿Qué tokens agregó?", "Todo lo que el enganche le agregó al agente en el período, estimado."),
    "gasto.sesiones": _campo("¿Qué son las sesiones?", "Las conversaciones con el agente, de la más reciente a la más vieja."),
    "gasto.sesion": _campo("¿Qué es la sesión?", "Los primeros caracteres del código de la conversación, para reconocerla."),
    "gasto.ultima_llamada": _campo("¿Qué es la última llamada?", "El día y la hora en que esa sesión gastó por última vez."),
    "gasto.mensajes": _campo("¿Qué son los mensajes?", "Lo último que el usuario le escribió al agente, con lo que gastó cada mensaje."),
    "gasto.palabra": _campo("¿Qué palabra clave?", "La palabra con que empezó el mensaje, la que dice qué hacer.",
                            "«Hágalo», «pregunta», «corrija»"),
    "gasto.trabajo": _campo("¿Qué trabajo?",
                            "La fase o el análisis en que se estaba. Sale, en este orden, del análisis que estaba "
                            "prendido, de los archivos y órdenes que tocó la respuesta, o del mensaje anterior de la "
                            "misma conversación («sigue la conversación»). Si nada de eso da una fase o un análisis, "
                            "el trabajo es la conversación misma, con el título que le puso Claude Code.",
                            "Un «Apruebo» después de trabajar en una fase queda en esa fase; un «Buenos días» al "
                            "comenzar queda en «Conversación «Buenos días»».",
                            "Mucho gasto en «Conversación ...» es trabajo hecho por fuera de una fase o un análisis."),
    "documento.ruta": _campo("¿Qué ruta?", "Dónde queda el documento dentro del estándar. Empieza por base/ y termina en .md.",
                             "base/17-guia-de-pantallas.md"),
    "reglas_del_proyecto.texto": _campo("¿Qué texto?",
                                        "Todas las reglas propias del proyecto. Cada una abre con su código y su "
                                        "título, como «### P1 · Título», y puede ir bajo una sección «## Nombre». "
                                        "Al guardar, cada regla pasa a su fila; la que se quita del texto queda "
                                        "apartada, no se borra.",
                                        "### P3 · Todo monto se guarda en centavos"),
    "documento.relaciones": _campo("¿Qué son las relaciones?",
                                   "Las otras reglas que tienen que ver con esta, en tres grupos: de cuáles depende "
                                   "(lo que la regla declara con «extiende», «depende de» o «deroga»), cuáles nombra "
                                   "en su texto y cuáles la nombran a ella.",
                                   "F1 depende de F2: para cumplir F1 también se cumple F2."),
    "documento.texto": _campo("¿Qué texto?", "El contenido completo del documento, como queda después del cambio.",
                              consejo="El cambio no se guarda de una vez: queda como propuesta para aprobar."),
    "git.asunto": _campo("¿Qué asunto?", "Una línea que dice qué cambió, como la verá quien lea la historia de git.",
                         "feat(cimiento): el menú se arma por tareas"),
    "git.idea": _campo("¿Qué idea del usuario?", "Lo que pidió el usuario, con sus palabras. Va primero en el commit."),
    "git.hecho": _campo("¿Qué hizo el agente?", "Lo que se hizo para cumplir esa idea. Va después en el commit."),
    "git.subir": _campo("¿Subir también?", "Marcado, después de guardar el cambio en git lo sube al repositorio remoto.",
                        consejo="Sin marcar, el cambio queda guardado solo en esta máquina."),
    "estandar.buscar": _campo("¿Qué buscar?", "Una palabra o un código de regla; se busca en las rutas y en el texto.",
                              "«F8» o «propuesta»"),
    "recuerdo.nombre": _campo("¿Qué nombre?", "El nombre del recuerdo, en minúsculas y con guiones, terminado en .md.",
                              "aprobar-antes-de-commit.md"),
    "recuerdo.texto": _campo("¿Qué texto?", "Lo que el agente debe recordar: qué se pide, por qué y cómo se aplica."),
    "reporte.proyecto": _campo("¿Qué proyecto reporta?", "El proyecto donde se encontró lo que está mal en el estándar."),
    "reporte.titulo": _campo("¿Qué pasa?", "En una línea, lo que está mal.", "«02·F8 frena lo que el plan sí autoriza»"),
    "reporte.regla": _campo("¿Qué regla?", "El código de la regla que toca, si hay una.", "02·F8"),
    "reporte.texto": _campo("¿Qué detalle?", "Cómo pasó y qué se esperaba, para que se pueda corregir."),
    "reporte.version": _campo("¿En qué versión se corrigió?",
                              "La versión del estándar que trae la corrección. El proyecto se entera al abrir su sesión siguiente."),
    "reporte.motivo": _campo("¿Por qué se descarta?", "La razón para no corregir nada. El proyecto la ve."),
    "vista_previa.proyecto": _campo("¿Para qué proyecto?", "Las reglas cambian según los capítulos que el proyecto tiene prendidos."),
    "vista_previa.mensaje": _campo("¿Qué mensaje?", "Lo que se le escribiría al agente, con su palabra clave al comienzo.",
                                   "«Hágalo: corrija el plan de la fase»"),
    "historia.tabla": _campo("¿Qué se cambió?", "Muestra solo los cambios de ese tipo de dato.", "«Propuesta» o «Ajuste de un proyecto»"),
    "historia.accion": _campo("¿Qué acción?", "Muestra solo lo que se creó, se cambió o se quitó."),
    "versiones.proyecto": _campo("¿De quién?", "Las versiones del estándar o las de un proyecto: cada uno lleva la suya."),
    "nivel.regla": _campo("¿Qué nivel?", "Qué hace el agente con esta regla en este proyecto.",
                          consejo="«Frena» detiene la acción; «avisa» la deja pasar con un aviso; «apagada» la ignora."),
    "proyecto.nombre": _campo("¿Qué nombre?", "Como se reconoce el proyecto en Cimiento.", "scilit"),
    "proyecto.ruta": _campo("¿Qué ruta?", "La carpeta del proyecto en esta máquina.", r"C:\DesarrollosClaude\personales\scilit"),
    "proyecto.activo": _campo("¿Activo?", "Si se sigue trabajando en él. Uno inactivo conserva su historia, pero no aparece en las listas."),
    "propuesta.rechazo": _campo("¿Por qué no se aprueba?", "La razón para rechazar la propuesta. Queda guardada con ella.",
                                "«El texto repite lo que ya dice otra regla»"),
})


def _pantalla(texto, ejemplo):
    return {"para_que": {"texto": texto, "ejemplo": ejemplo}}


PANTALLAS.update({
    "gasto": _pantalla("Ver cuántos tokens se gastan, en qué proyecto y en qué, en vivo.",
                       "Se escoge un proyecto y «7 días» para ver qué enganche gastó más la última semana."),
    "documento": _pantalla("Leer una regla o un documento del estándar, ver con qué reglas se relaciona y, quien administra, cambiar su texto.",
                           "Se abre F8, se lee su ejemplo y, en «Relaciones», se pulsa la regla de la que depende para leerla."),
    "git": _pantalla("Guardar en git lo que cambió en Cimiento, separado por sesión, y subirlo si se quiere.",
                     "Al terminar una tarea, se escribe el asunto y la idea, y se pulsa el botón de la sesión."),
    "reglas_del_proyecto": _pantalla("Leer las reglas que solo valen para un proyecto y, quien administra, cambiarlas.",
                                     "Se abre AgroSystem, se despliega P3 y se lee qué exige."),
    "estandar": _pantalla("Ver las reglas del estándar por capítulo, con su código y su nombre, y buscar en ellas.",
                          "Se abre el capítulo «02 · Flujo de trabajo» y se pulsa «F8» para leer la regla."),
    "recuerdo": _pantalla("Leer o proponer un recuerdo de la memoria del agente.",
                          "Se escribe cómo quiere el usuario que se trabaje; queda como propuesta para aprobar."),
    "reportes": _pantalla("Atender lo que los proyectos encontraron mal en el estándar.",
                          "Un proyecto reporta que una regla frena de más; se corrige la regla y aquí se marca con la versión que la corrigió."),
    "vista_previa": _pantalla("Ver qué reglas le llegarían al agente con un mensaje, antes de escribirlo.",
                              "Se escoge el proyecto, se escribe «Hágalo: corrija el plan» y se ven las reglas de esa tarea."),
    "propuestas": _pantalla("Aprobar o rechazar lo que propone el agente para el estándar o la memoria.",
                            "Se lee «Qué cambia», se responden las dos preguntas de versión y se pulsa «Aprobar»."),
    "historia": _pantalla("Ver quién cambió qué, cuándo y por qué, y deshacerlo si hace falta.",
                          "Se filtra por «Propuesta» para ver qué se aprobó hoy."),
    "versiones": _pantalla("Ver las versiones del estándar y las de cada proyecto, con su tipo y su motivo.",
                           "Se escoge «Estándar» para ver qué subió MAYOR y por qué."),
    "reglas": _pantalla("Decidir qué hace el agente con cada regla en este proyecto.",
                        "Una regla que estorba se pone en «avisa» en vez de «frena»."),
    "proyecto": _pantalla("Registrar un proyecto o cambiar sus datos y su configuración propia.",
                          "Se registra la carpeta de un proyecto nuevo y se prenden los capítulos opt-in que necesita."),
})
