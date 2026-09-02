# -*- coding: utf-8 -*-
"""Las pantallas de proyectos: la lista, uno solo, y las confirmaciones.

Son `P-01` y `P-02` del diseño aprobado, en su forma mínima: muestran,
conectan y administran. Lo demás que esas pantallas prometen -entrar a un
documento, abrir una fase, pedir el expediente- llega en las versiones
siguientes.

**Una lista vacía dice que está vacía.** Una pantalla en blanco se lee como un
error de la plataforma, y no lo es.

**Ningún cambio de estado ocurre sin confirmación** (`00·N1`). Y la
confirmación dice **qué va a pasar y qué no**: que al desconectar la
documentación se queda, y que al reconectar vuelve. Sin eso el usuario no
confirma, adivina.
"""
from django.shortcuts import get_object_or_404, redirect, render

from . import core
from .models import Proyecto

# Cada cambio, con lo que la pantalla tiene que decir antes de hacerlo.
CONFIRMACIONES = {
    "desconectar": {
        "titulo": "Desconectar el proyecto",
        "que_pasa": "Deja de aparecer entre los proyectos conectados.",
        "que_no_pasa": [
            "Su documentación se queda guardada en la plataforma.",
            "Nada de la carpeta de su código se toca.",
            "Se puede volver a conectar después, y vuelve con lo que tenía.",
        ],
        "boton": "Sí, desconectar",
    },
    "renombrar": {
        "titulo": "Renombrar el proyecto",
        "que_pasa": "Pasa a llamarse como usted diga.",
        "que_no_pasa": [
            "Su carpeta de documentación no se mueve.",
            "Nada de la carpeta de su código se toca.",
        ],
        "boton": "Sí, renombrar",
    },
    "corregir-ruta": {
        "titulo": "Corregir dónde vive su código",
        "que_pasa": "El proyecto pasa a apuntar a la carpeta que usted diga.",
        "que_no_pasa": [
            "Su documentación no se mueve: sigue en la plataforma.",
            "Ninguna de las dos carpetas se toca: ni la vieja ni la nueva.",
            "No se copia ni se mueve código de un lado al otro.",
        ],
        "boton": "Sí, corregir la ruta",
    },
    "corregir-version": {
        "titulo": "Corregir la versión de reglas",
        "que_pasa": "Se vuelve a leer del CLAUDE.md del proyecto y se comprueba.",
        "que_no_pasa": [
            "No se escribe nada dentro del proyecto: solo se lee.",
            "Si la versión que declara no existe, se deja la que tenía.",
        ],
        "boton": "Sí, corregir",
    },
}


def lista(request):
    """`P-01` · los proyectos conectados, los desconectados, y el formulario."""
    return render(request, "proyectos/lista.html", {
        "proyectos": Proyecto.objects.filter(desconectado=""),
        "desconectados": Proyecto.objects.exclude(desconectado=""),
    })


def conectar(request):
    """Recibe el nombre y la ruta. Rechaza o conecta, y dice cuál de las dos.

    Si esa carpeta ya la tuvo un proyecto desconectado, **avisa antes**: va a
    volver con la documentación que dejó, y eso puede no ser lo que el usuario
    quería.
    """
    if request.method != "POST":
        return redirect("proyectos-lista")

    nombre = (request.POST.get("nombre") or "").strip()
    ruta = (request.POST.get("ruta") or "").strip()
    if not nombre or not ruta:
        return _lista_con_error(request, "Hacen falta el nombre y la ruta.",
                                nombre, ruta)

    dormido = core.desconectado_en(ruta)
    if dormido and not request.POST.get("confirmado"):
        return render(request, "proyectos/confirmar.html", {
            "titulo": "Este proyecto ya estuvo conectado",
            "proyecto": dormido,
            "que_pasa": "Vuelve el proyecto «%s», con la documentación que "
                        "dejó cuando se desconectó el %s."
                        % (dormido.nombre, dormido.desconectado),
            "que_no_pasa": [
                "No se crea un proyecto nuevo: vuelve el mismo.",
                "Si quería empezar de cero con esa carpeta, esto no es lo que "
                "busca.",
            ],
            "boton": "Sí, volver a conectarlo",
            "accion": "conectar",
            "campos": {"nombre": nombre, "ruta": ruta},
        })

    try:
        proyecto, avisos = core.conectar(
            nombre, ruta, quien="el usuario",
            sesion=(request.POST.get("sesion") or "").strip())
    except (core.RutaQueNoExiste, core.RutaYaRegistrada,
            core.VersionQueNoExiste) as rechazo:
        return _lista_con_error(request, str(rechazo), nombre, ruta)

    return render(request, "proyectos/uno.html", {
        "seccion": "ficha",
        "proyecto": proyecto,
        "avisos": avisos,
        "recien_conectado": True,
    })


def uno(request, identificador):
    """`P-02` · un proyecto: su ruta, su versión, qué le falta y qué se le puede hacer."""
    proyecto = get_object_or_404(Proyecto, identificador=identificador)
    return render(request, "proyectos/uno.html", {
        "seccion": "ficha",
        "proyecto": proyecto,
        "avisos": _avisos_de(proyecto),
        "estado": proyecto.detalle_del_estado,
    })


def cambiar(request, identificador, que):
    """Pregunta antes, y solo entonces cambia. Es la puerta de `00·N1`."""
    proyecto = get_object_or_404(Proyecto, identificador=identificador)
    if que not in CONFIRMACIONES:
        return redirect("proyectos-uno", identificador=identificador)

    confirmacion = CONFIRMACIONES[que]
    if not request.POST.get("confirmado"):
        return render(request, "proyectos/confirmar.html", dict(
            confirmacion,
            proyecto=proyecto,
            accion=que,
            pide_nombre=(que == "renombrar"),
            pide_ruta=(que == "corregir-ruta"),
            campos={}))

    quien, sesion = "el usuario", (request.POST.get("sesion") or "").strip()
    try:
        if que == "desconectar":
            core.desconectar(proyecto, quien=quien, sesion=sesion)
            return redirect("proyectos-lista")
        if que == "renombrar":
            proyecto = core.renombrar(
                proyecto, request.POST.get("nombre"), quien=quien,
                sesion=sesion)
        elif que == "corregir-ruta":
            proyecto = core.corregir_ruta(
                proyecto, request.POST.get("ruta"), quien=quien,
                sesion=sesion)
        else:
            proyecto = core.corregir_version(proyecto, quien=quien,
                                             sesion=sesion)
    except (core.NombreVacio, core.VersionQueNoExiste,
            core.RutaQueNoExiste, core.RutaYaRegistrada) as rechazo:
        return render(request, "proyectos/uno.html", {
        "seccion": "ficha",
            "proyecto": proyecto,
            "avisos": _avisos_de(proyecto),
            "error": str(rechazo),
        })

    return render(request, "proyectos/uno.html", {
        "seccion": "ficha",
        "proyecto": proyecto,
        "avisos": _avisos_de(proyecto),
        "hecho": confirmacion["titulo"] + ": listo.",
    })


def _avisos_de(proyecto):
    if not proyecto.esta_conectado:
        return ["Este proyecto está desconectado desde el %s. Su documentación "
                "sigue guardada acá, y vuelve si se conecta otra vez."
                % proyecto.desconectado]
    return core.avisos_de(proyecto.ruta_codigo, proyecto.version_reglas)


def _lista_con_error(request, error, nombre, ruta):
    return render(request, "proyectos/lista.html", {
        "proyectos": Proyecto.objects.filter(desconectado=""),
        "desconectados": Proyecto.objects.exclude(desconectado=""),
        "error": error,
        "nombre": nombre,
        "ruta": ruta,
    })
