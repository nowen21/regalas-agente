# -*- coding: utf-8 -*-
"""Agrega a nucleo/proyectos/core.py lo que construye la fase C."""
import io

p = "nucleo/proyectos/core.py"
t = io.open(p, encoding="utf-8").read()

# --- El aviso de la ruta perdida dice qué ruta se buscó ---
viejo = '''def avisos_de(ruta, version_declarada):
    """Lo que hay que decirle al usuario, sin impedirle conectar."""
    dichos = []'''
nuevo = '''def avisos_de(ruta, version_declarada):
    """Lo que hay que decirle al usuario, sin impedirle conectar."""
    dichos = []
    if not os.path.isdir(str(ruta)):
        # **El aviso nombra la ruta**, no solo dice que falló (`RN-2` de la
        # historia). Sin ella el usuario no puede ver si fue un renombre, un
        # movimiento, o un disco que no está montado.
        dichos.append(
            "La carpeta de su código ya no está donde estaba. Se buscó en "
            "«%s». Su documentación sigue guardada acá." % ruta)
        return dichos'''
assert viejo in t
t = t.replace(viejo, nuevo, 1)

# --- Corregir la ruta ---
viejo = '''def corregir_version(proyecto, quien="el usuario", sesion=""):'''
nuevo = '''def corregir_ruta(proyecto, ruta_nueva, quien="el usuario", sesion=""):
    """Vuelve a apuntar el proyecto a otra carpeta. Devuelve el proyecto.

    **La ruta nueva se comprueba igual que al conectar**: que exista, y que no
    la tenga ya otro proyecto. Corregir no puede ser una puerta de atrás para
    lo que conectar rechaza.

    **Y se relee la versión de reglas de la carpeta nueva.** La carpeta cambió,
    así que lo que declara puede ser otra cosa; dejar la vieja sería afirmar
    sobre lo que no se leyó.
    """
    from .models import Proyecto

    pedida = str(ruta_nueva or "").strip()
    if not os.path.isdir(pedida):
        raise RutaQueNoExiste(
            "No existe la carpeta «%s». Se deja la ruta que tenía." % pedida)

    normal = ruta_normalizada(pedida)
    ya = Proyecto.objects.filter(ruta_normalizada=normal,
                                 desconectado="").exclude(pk=proyecto.pk).first()
    if ya:
        raise RutaYaRegistrada(
            "Esa carpeta ya está registrada por el proyecto «%s». Se deja la "
            "ruta que tenía." % ya.nombre)

    version = reglas.declarada_por(pedida)
    if not reglas.existe(version):
        raise VersionQueNoExiste(
            "La carpeta nueva declara la versión %s del estándar, y esa "
            "versión nunca se publicó. Se deja la ruta que tenía." % version)

    vieja = proyecto.ruta_codigo
    _reescribir_ficha(proyecto, ruta=pedida, version=version,
                      que_se_hizo="corregir la ruta de un proyecto",
                      que_cambio="de «%s» a «%s»" % (vieja, pedida),
                      quien=quien, sesion=sesion)
    return _indexar(proyecto.identificador, proyecto.nombre, pedida, version,
                    proyecto.conectado, desconectado=proyecto.desconectado)


def corregir_version(proyecto, quien="el usuario", sesion=""):'''
assert viejo in t
t = t.replace(viejo, nuevo, 1)

# --- _reescribir_ficha aprende a cambiar la ruta ---
viejo = '''def _reescribir_ficha(proyecto, que_se_hizo, que_cambio, quien, sesion,
                      nombre=None, version=None, desconectado=None):'''
nuevo = '''def _reescribir_ficha(proyecto, que_se_hizo, que_cambio, quien, sesion,
                      nombre=None, version=None, desconectado=None, ruta=None):'''
assert viejo in t
t = t.replace(viejo, nuevo, 1)

viejo = '''    texto = _texto_de_la_ficha(
        proyecto.nombre if nombre is None else nombre,
        proyecto.ruta_codigo,'''
nuevo = '''    texto = _texto_de_la_ficha(
        proyecto.nombre if nombre is None else nombre,
        proyecto.ruta_codigo if ruta is None else ruta,'''
assert viejo in t
t = t.replace(viejo, nuevo, 1)

# --- El encabezado del módulo cuenta lo de la fase C ---
viejo = '''carpeta lo **reactiva** en vez de crear uno nuevo: crear uno nuevo dejaría la
documentación del anterior sin dueño.
"""'''
nuevo = '''carpeta lo **reactiva** en vez de crear uno nuevo: crear uno nuevo dejaría la
documentación del anterior sin dueño.

**Desde la fase C, la ruta que se pierde se avisa y se corrige.** El aviso dice
**qué ruta se buscó**, y corregirla comprueba lo mismo que al conectar. Perder
la ruta no pierde nada: la documentación vive en la plataforma, no allá.
"""'''
assert viejo in t
t = t.replace(viejo, nuevo, 1)

io.open(p, "w", encoding="utf-8", newline="\n").write(t)
print("core ok")
