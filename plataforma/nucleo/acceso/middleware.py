# -*- coding: utf-8 -*-
"""Ninguna pantalla responde sin haber entrado — `RN-1` de Acceso.

**Va acá y no como decorador en cada vista, y es la decisión que importa.** Un
decorador hay que acordarse de ponerlo: la vista número trece que alguien
escriba dentro de seis meses va a nacer abierta, y nadie lo va a notar porque
funcionar, funciona. Con esto **una vista nueva nace protegida**, y abrirla al
público exige escribirlo a propósito en una lista corta que se lee de un vistazo.

**La lista de lo que no exige entrar es esa lista.** Hoy tiene dos cosas: la
pantalla de entrar y la de salir. Cualquier otra cosa que se agregue se ve.
"""
from django.conf import settings
from django.contrib.auth.views import redirect_to_login

# Lo que responde sin haber entrado. **Cada renglón de acá es una decisión.**
ABIERTAS = ("/entrar/", "/salir/")


def sin_entrar(camino):
    """¿Ese camino responde sin haber entrado?

    Los estáticos también: son la hoja de estilos de la propia pantalla de
    entrar, y sin ellos esa pantalla se ve rota.
    """
    return camino in ABIERTAS or camino.startswith(str(settings.STATIC_URL))


class ExigirHaberEntrado(object):
    """Manda al formulario de entrar a quien no haya entrado."""

    def __init__(self, siguiente):
        self.siguiente = siguiente

    def __call__(self, peticion):
        if sin_entrar(peticion.path) or peticion.user.is_authenticated:
            return self.siguiente(peticion)
        # Se recuerda a dónde iba: volver a la portada le haría buscar otra vez
        # lo que ya había encontrado.
        return redirect_to_login(peticion.get_full_path(),
                                 settings.LOGIN_URL and "/entrar/")
