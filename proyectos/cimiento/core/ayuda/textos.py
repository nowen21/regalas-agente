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
