# -*- coding: utf-8 -*-
"""La única pantalla que no exige haber entrado: la de entrar.

**No se dice cuál de los dos datos estuvo mal.** Responder «esa cuenta no
existe» le confirma a cualquiera qué cuentas hay, que es la mitad del trabajo de
quien esté probando. El mensaje es uno solo para los dos casos.

**Entrar lleva a donde se iba, no a la portada.** Quien pidió una pantalla y fue
mandado a entrar espera volver a esa pantalla; devolverlo al inicio le hace
buscar otra vez lo que ya había encontrado.
"""
from django.contrib.auth import views as de_django


class Entrar(de_django.LoginView):
    template_name = "acceso/entrar.html"
    redirect_authenticated_user = True

    def form_invalid(self, formulario):
        """El mismo mensaje para los dos casos."""
        formulario.errors.clear()
        formulario.add_error(
            None,
            "La cuenta o la contraseña no son correctas. No se dice cuál de "
            "las dos: decirlo confirmaría qué cuentas existen.")
        return super().form_invalid(formulario)


class Salir(de_django.LogoutView):
    pass
