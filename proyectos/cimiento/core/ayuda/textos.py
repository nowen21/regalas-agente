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
    "documento.ruta": _campo("¿Qué ruta?", "Dónde queda el documento dentro del estándar. Empieza por base/ y termina en .md.",
                             "base/17-guia-de-pantallas.md"),
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
    "documento": _pantalla("Leer un documento del estándar y proponer un cambio.",
                           "Se corrige una palabra de una regla y se guarda: queda como propuesta en «Propuestas por aprobar»."),
    "git": _pantalla("Guardar en git lo que cambió en Cimiento, separado por sesión, y subirlo si se quiere.",
                     "Al terminar una tarea, se escribe el asunto y la idea, y se pulsa el botón de la sesión."),
    "estandar": _pantalla("Ver todos los documentos del estándar y buscar en ellos.",
                          "Se busca «F8» para encontrar la regla y los documentos que la nombran."),
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
