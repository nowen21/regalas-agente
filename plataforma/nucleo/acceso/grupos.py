# -*- coding: utf-8 -*-
"""Los dos grupos y lo que cada uno puede hacer — `F-037`.

**Dos grupos y no cuatro.** El análisis define cuatro actores; solo dos entran a
la plataforma. «Un proyecto administrado» no es una persona ni un programa que
entre —es una carpeta que se observa—, y «quien recibe un proyecto» tiene
escrito que **no puede entrar**. Construir cuatro grupos habría sido construir
de más, y dos de ellos no los habría usado nadie.

**Lo que separa a los dos es qué obliga a otros.** El agente escribe documentos,
abre fases y comprueba: todo eso es su trabajo. Lo que no hace es **aprobar,
publicar una versión, derogar una regla ni administrar cuentas**, porque las
cuatro obligan a alguien más — y `00·N1` pide que eso lo autorice una persona.

**Un agente que se aprobara a sí mismo volvería la aprobación un trámite.** Esa
es la frase entera; lo demás es cómo se escribe en Django.

**Los permisos son de la plataforma, no de una tabla.** No hay modelo `Aprobar`;
lo que hay es una acción. Por eso se declaran como permisos sueltos colgados de
un modelo cualquiera de la plataforma, que es la forma en que Django deja
declarar permisos que no son «crear, ver, cambiar, borrar» de algo.
"""
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

USUARIO = "usuario"
AGENTE = "agente"

# Lo que solo el usuario puede hacer. Cada uno con la frase que explica por qué
# no lo puede el agente: el rechazo la usa, y así el motivo vive en un solo sitio.
SOLO_DEL_USUARIO = (
    ("aprobar_documento", "Aprobar un documento",
     "aprobar es de una persona (`00·N1`): un agente que aprueba lo que él "
     "mismo construyó vuelve la aprobación un trámite"),
    ("publicar_version", "Publicar una versión de las reglas",
     "publicar obliga a todos los proyectos que heredan, y eso lo decide quien "
     "responde por ellos"),
    ("derogar_regla", "Derogar una regla",
     "derogar cambia lo que se le exige a otros proyectos"),
    ("administrar_cuentas", "Administrar cuentas",
     "quien se da permisos a sí mismo no tiene permisos"),
)

# Lo que los dos pueden. Se declara, en vez de darse por hecho: un permiso que
# no está escrito es un permiso que nadie sabe si existe.
DE_LOS_DOS = (
    ("escribir_documentos", "Escribir documentos y abrir fases"),
    ("ver_todo", "Ver cualquier pantalla"),
)

_POR_QUE = {clave: porque for clave, _nombre, porque in SOLO_DEL_USUARIO}


def por_que_no(clave):
    """Por qué el agente no puede hacer eso. `""` si no es de los restringidos."""
    return _POR_QUE.get(clave, "")


def _donde_cuelgan():
    """El modelo del que cuelgan estos permisos.

    Django exige colgar cada permiso de un modelo. Estas acciones no son de
    ningún modelo —aprobar no es «cambiar una fila»—, así que cuelgan del de
    Proyecto, que es el que representa aquello sobre lo que se actúa.
    """
    from nucleo.proyectos.models import Proyecto
    return ContentType.objects.get_for_model(Proyecto)


def poner_al_dia():
    """Crea los dos grupos con sus permisos. Se puede correr muchas veces.

    Devuelve `{"usuario": [...], "agente": [...]}` con lo que quedó.
    """
    tipo = _donde_cuelgan()
    todos = {}
    for clave, nombre, _porque in SOLO_DEL_USUARIO:
        todos[clave] = Permission.objects.get_or_create(
            codename=clave, content_type=tipo, defaults={"name": nombre})[0]
    for clave, nombre in DE_LOS_DOS:
        todos[clave] = Permission.objects.get_or_create(
            codename=clave, content_type=tipo, defaults={"name": nombre})[0]

    del_usuario = Group.objects.get_or_create(name=USUARIO)[0]
    del_agente = Group.objects.get_or_create(name=AGENTE)[0]

    # El usuario, todo. **Nada le está vedado**, dice el análisis.
    del_usuario.permissions.set(todos.values())
    # El agente, solo lo que no obliga a otros.
    del_agente.permissions.set([todos[clave] for clave, _n in DE_LOS_DOS])

    return {USUARIO: sorted(todos), AGENTE: sorted(c for c, _n in DE_LOS_DOS)}


def con_prefijo(clave):
    """La clave como Django la pide al preguntar: `app.permiso`."""
    return "proyectos.%s" % clave
