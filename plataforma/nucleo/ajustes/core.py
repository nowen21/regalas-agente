# -*- coding: utf-8 -*-
"""Pedirle un ajuste a la plataforma, y sembrar los de fábrica.

**Nunca revienta por un ajuste que falte.** Si alguien borra una fila, el
programa sigue con el valor de fábrica que trae escrito el propio llamado. Una
pantalla que se cae porque falta un texto es peor que una que muestra el texto
de siempre.
"""
from nucleo.ajustes.models import Ajuste, EtapaDelCiclo

# Los ajustes que la plataforma trae puestos. Cada uno dice para qué sirve, y
# eso es lo que se lee en `/admin/` al ir a cambiarlo.
DE_FABRICA = (
    ("aviso.es_el_estandar", Ajuste.TEXTO,
     "El aviso que sale en la ficha del proyecto que ES el estándar, en vez de "
     "reclamarle qué versión sigue.",
     "Esta carpeta es el estándar mismo, no un proyecto que lo hereda. Por eso "
     "no declara qué versión sigue: la versión que es está en su archivo "
     "VERSION{version}. No hay nada que corregir."),

    ("aviso.sin_version", Ajuste.TEXTO,
     "El aviso para un proyecto que no ha declarado qué versión del estándar "
     "sigue. Sale en su ficha.",
     "Este proyecto todavía no ha indicado qué versión del estándar está "
     "utilizando. Aunque el sistema puede conectarse y funcionar normalmente, "
     "no será posible identificar si está desactualizado hasta que esta "
     "información se registre en su archivo CLAUDE.md. Para corregirlo, abra "
     "el archivo CLAUDE.md que está en la carpeta del proyecto y escriba en él "
     "la versión del estándar que sigue; si no sabe cuál es, la versión "
     "vigente aparece en el archivo VERSION del estándar."),

    ("aviso.ruta_perdida", Ajuste.TEXTO,
     "El aviso cuando la carpeta del código ya no está donde estaba. Lleva la "
     "ruta buscada, que es lo que permite ver si fue un renombre o un disco "
     "sin montar.",
     "La carpeta de su código ya no está donde estaba. Se buscó en «{ruta}». "
     "Su documentación sigue guardada acá."),

    ("aviso.sin_control_de_versiones", Ajuste.TEXTO,
     "El aviso cuando la carpeta del proyecto no está bajo control de "
     "versiones.",
     "La carpeta de este proyecto no está bajo control de versiones: su código "
     "no tiene respaldo."),

    ("proposito.ficha_del_proyecto", Ajuste.TEXTO,
     "El párrafo que abre la ficha de un proyecto y dice para qué sirve esa "
     "pantalla.",
     "Acá se puede consultar el estado del proyecto sin necesidad de abrir su "
     "carpeta."),

    ("avisos.dias_para_dar_por_vencida", Ajuste.NUMERO,
     "Cuántos días sin moverse hacen que un trabajo se dé por vencido, en el "
     "tablero. El estándar nunca le puso fecha a una deuda: este número se "
     "puso acá, y por eso se puede cambiar.",
     "30"),
)

LAS_SIETE_DE_FABRICA = (
    (1, "planificacion", "Planear",
     "¿Vale la pena hacerlo, y con qué recursos?",
     "El acta que abre el proyecto y el estudio de si es viable"),
    (2, "analisis-requisitos", "Analizar",
     "¿Qué tiene que hacer exactamente?",
     "La lista de todo lo que el sistema debe hacer, una por una"),
    (3, "diseno", "Diseñar",
     "¿Cómo va a estar hecho por dentro?",
     "El modelo de datos, las pantallas y las decisiones de arquitectura"),
    (4, "implementacion", "Construir",
     "¿En qué orden se construye, y qué entra en cada versión?",
     "El plan de versiones y qué funcionalidad cubre cada una"),
    (5, "pruebas", "Probar",
     "¿Funciona de verdad, y cómo se comprueba?",
     "Qué se probó, con qué casos y qué salió"),
    (6, "despliegue", "Entregar",
     "¿Cómo se instala, cómo se opera y qué se entregó?",
     "El manual técnico, las notas de versión y el acta de entrega"),
    (7, "mantenimiento", "Mantener",
     "¿Qué hay que hacerle después, y quién?",
     "El plan de mantenimiento y la bitácora de lo que pase"),
)


def texto(clave, por_defecto=""):
    """El texto de ese ajuste. El de fábrica si no está o si algo falla.

    **Se lee al pedirlo, sin caché.** Alguien lo cambia en `/admin/` y la
    siguiente pantalla ya lo muestra: un caché obligaría a reiniciar, y eso es
    volver a depender de quien sabe reiniciar.
    """
    try:
        return Ajuste.objects.get(clave=clave).valor
    except Exception:
        return por_defecto


def numero(clave, por_defecto=0):
    """El ajuste como número entero. El de fábrica si no está o no es un número."""
    try:
        return int(str(texto(clave, por_defecto)).strip())
    except (TypeError, ValueError):
        return por_defecto


def de_fabrica(clave):
    """Con qué valor vino ese ajuste, según la tabla de acá."""
    for una, _tipo, _para, valor in DE_FABRICA:
        if una == clave:
            return valor
    return ""


def poner_al_dia():
    """Siembra lo que falte. Se puede correr muchas veces.

    **No pisa lo que alguien haya cambiado**: solo crea lo que no está. Volver a
    ponerlo de fábrica es borrar la fila y correr esto otra vez.
    """
    puestos = 0
    for clave, tipo, para_que, valor in DE_FABRICA:
        _, nuevo = Ajuste.objects.get_or_create(
            clave=clave,
            defaults={"valor": valor, "tipo": tipo, "para_que": para_que,
                      "de_fabrica": valor})
        puestos += 1 if nuevo else 0
    etapas = 0
    for orden, carpeta, nombre, pregunta, queda in LAS_SIETE_DE_FABRICA:
        _, nueva = EtapaDelCiclo.objects.get_or_create(
            carpeta=carpeta,
            defaults={"orden": orden, "nombre": nombre, "pregunta": pregunta,
                      "queda": queda})
        etapas += 1 if nueva else 0
    return {"ajustes": puestos, "etapas": etapas}


def las_etapas():
    """Las etapas del ciclo, en su orden. Las de fábrica si la tabla está vacía."""
    hay = list(EtapaDelCiclo.objects.all())
    if hay:
        return [{"carpeta": una.carpeta, "nombre": una.nombre,
                 "pregunta": una.pregunta, "queda": una.queda} for una in hay]
    return [{"carpeta": carpeta, "nombre": nombre, "pregunta": pregunta,
             "queda": queda}
            for _o, carpeta, nombre, pregunta, queda in LAS_SIETE_DE_FABRICA]
