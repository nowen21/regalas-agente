# -*- coding: utf-8 -*-
"""Reescribe nucleo/proyectos/core.py con lo que agrega la fase H."""
import io

p = "nucleo/proyectos/core.py"
t = io.open(p, encoding="utf-8").read()

# --- El encabezado del módulo cuenta también lo de la fase H ---
t = t.replace('''Vacío y falso no son lo mismo: un número inventado apagaría el aviso de
desfase, y no declarar nada solo dice que ese proyecto todavía no adoptó el
estándar. Decidido con el usuario el 2026-08-25.
"""''',
'''Vacío y falso no son lo mismo: un número inventado apagaría el aviso de
desfase, y no declarar nada solo dice que ese proyecto todavía no adoptó el
estándar. Decidido con el usuario el 2026-08-25.

**Desde la fase H, conectar tiene reversa.** Se puede desconectar, renombrar y
corregir la versión declarada, y **nada de eso borra ni mueve nada**:
desconectar deja la documentación donde está, y renombrar deja la carpeta donde
está. Un proyecto desconectado **libera su ruta**, y volver a conectar esa
carpeta lo **reactiva** en vez de crear uno nuevo: crear uno nuevo dejaría la
documentación del anterior sin dueño.
"""''')

# --- La ficha gana el campo de desconexión ---
t = t.replace('''def _texto_de_la_ficha(nombre, ruta, version, conectado):
    return (
        "# %s\\n\\n"
        "| Campo | Valor |\\n"
        "|---|---|\\n"
        "| Nombre | %s |\\n"
        "| Ruta del código | %s |\\n"
        "| Versión de reglas adoptada | %s |\\n"
        "| Fecha de conexión | %s |\\n\\n"
        "La ruta viva y el estado no se guardan acá: se calculan al mirarlos.\\n"
        % (nombre, nombre, ruta, version or "ninguna todavía", conectado))''',
'''def _texto_de_la_ficha(nombre, ruta, version, conectado, desconectado=""):
    """El texto de la ficha. Es la fuente; el índice se rehace desde acá.

    El campo de desconexión va en la ficha y no solo en el índice: si viviera
    solo en la base, rehacer el índice resucitaría al proyecto desconectado.
    """
    return (
        "# %s\\n\\n"
        "| Campo | Valor |\\n"
        "|---|---|\\n"
        "| Nombre | %s |\\n"
        "| Ruta del código | %s |\\n"
        "| Versión de reglas adoptada | %s |\\n"
        "| Fecha de conexión | %s |\\n"
        "| Fecha de desconexión | %s |\\n\\n"
        "La ruta viva y el estado no se guardan acá: se calculan al mirarlos.\\n"
        % (nombre, nombre, ruta, version or "ninguna todavía", conectado,
           desconectado or "sigue conectado"))''')

# --- Conectar: la ruta tomada solo cuenta si el proyecto sigue conectado ---
t = t.replace('''    normal = ruta_normalizada(pedida)
    ya = Proyecto.objects.filter(ruta_normalizada=normal).first()
    if ya:
        raise RutaYaRegistrada(
            "Esa carpeta ya está registrada por el proyecto «%s»." % ya.nombre)''',
'''    normal = ruta_normalizada(pedida)
    ya = Proyecto.objects.filter(ruta_normalizada=normal,
                                 desconectado="").first()
    if ya:
        raise RutaYaRegistrada(
            "Esa carpeta ya está registrada por el proyecto «%s»." % ya.nombre)

    # Un desconectado liberó su ruta, pero su documentación se quedó. Volver a
    # conectar esa carpeta lo **reactiva**: crear uno nuevo dejaría lo suyo sin
    # dueño. Decidido con el usuario el 2026-08-25.
    dormido = Proyecto.objects.filter(ruta_normalizada=normal).first()
    if dormido:
        return reconectar(dormido, quien=quien, sesion=sesion)''')

# --- Las funciones nuevas, antes de _identificador_libre ---
t = t.replace('''def _identificador_libre(nombre):''',
'''def desconectado_en(ruta):
    """El proyecto desconectado que tenía esa ruta, o None.

    Sirve para que la pantalla avise **antes de confirmar** que ahí hay una
    historia guardada: si el usuario quería empezar de cero con esa carpeta,
    reactivar le devolvería lo viejo sin haberlo pedido.
    """
    from .models import Proyecto
    if not os.path.isdir(str(ruta)):
        return None
    return Proyecto.objects.filter(
        ruta_normalizada=ruta_normalizada(ruta)).exclude(
            desconectado="").first()


def desconectar(proyecto, quien="el usuario", sesion=""):
    """Saca el proyecto de la lista. **No borra su documentación.**

    Escribe la fecha en su ficha, que es la fuente. Devuelve el proyecto.
    """
    cuando = timezone.localtime().date().isoformat()
    _reescribir_ficha(proyecto, desconectado=cuando,
                      que_se_hizo="desconectar un proyecto",
                      que_cambio="su documentación se queda en la plataforma",
                      quien=quien, sesion=sesion)
    return _indexar(proyecto.identificador, proyecto.nombre,
                    proyecto.ruta_codigo, proyecto.version_reglas,
                    proyecto.conectado, desconectado=cuando)


def reconectar(proyecto, quien="el usuario", sesion=""):
    """Vuelve a conectar un desconectado, con lo que tenía. Devuelve el par
    del `conectar` normal: el proyecto y sus avisos."""
    _reescribir_ficha(proyecto, desconectado="",
                      que_se_hizo="volver a conectar un proyecto",
                      que_cambio="vuelve con la documentación que ya tenía",
                      quien=quien, sesion=sesion)
    vuelto = _indexar(proyecto.identificador, proyecto.nombre,
                      proyecto.ruta_codigo, proyecto.version_reglas,
                      proyecto.conectado, desconectado="")
    return vuelto, avisos_de(vuelto.ruta_codigo, vuelto.version_reglas)


def renombrar(proyecto, nombre_nuevo, quien="el usuario", sesion=""):
    """Le cambia el nombre. **El identificador no cambia, así que su carpeta
    de documentación se queda donde está.**"""
    nombre_nuevo = (nombre_nuevo or "").strip()
    if not nombre_nuevo:
        raise NombreVacio("Un proyecto tiene que llamarse de alguna manera.")
    viejo = proyecto.nombre
    _reescribir_ficha(proyecto, nombre=nombre_nuevo,
                      que_se_hizo="renombrar un proyecto",
                      que_cambio="de «%s» a «%s»" % (viejo, nombre_nuevo),
                      quien=quien, sesion=sesion)
    return _indexar(proyecto.identificador, nombre_nuevo,
                    proyecto.ruta_codigo, proyecto.version_reglas,
                    proyecto.conectado, desconectado=proyecto.desconectado)


def corregir_version(proyecto, quien="el usuario", sesion=""):
    """Vuelve a leer del proyecto qué versión declara, y la comprueba.

    No se pide escrita, por lo mismo que al conectar: teclearla es la forma de
    que quede un número que no existe.
    """
    if not os.path.isdir(proyecto.ruta_codigo):
        raise RutaQueNoExiste(
            "No existe la carpeta «%s», así que no hay de dónde leer la "
            "versión." % proyecto.ruta_codigo)

    version = reglas.declarada_por(proyecto.ruta_codigo)
    if not reglas.existe(version):
        raise VersionQueNoExiste(
            "El proyecto declara la versión %s del estándar, y esa versión "
            "nunca se publicó. Se deja la que tenía." % version)

    viejo = proyecto.version_reglas
    _reescribir_ficha(proyecto, version=version,
                      que_se_hizo="corregir la versión de reglas declarada",
                      que_cambio="de «%s» a «%s»" % (viejo or "ninguna",
                                                     version or "ninguna"),
                      quien=quien, sesion=sesion)
    return _indexar(proyecto.identificador, proyecto.nombre,
                    proyecto.ruta_codigo, version, proyecto.conectado,
                    desconectado=proyecto.desconectado)


def _reescribir_ficha(proyecto, que_se_hizo, que_cambio, quien, sesion,
                      nombre=None, version=None, desconectado=None):
    """Vuelve a escribir la ficha con el cambio, dejando la constancia antes.

    **Reescribe la ficha entera, nunca la carpeta.** Lo que hay dentro de la
    carpeta de documentación de ese proyecto no se toca.
    """
    texto = _texto_de_la_ficha(
        proyecto.nombre if nombre is None else nombre,
        proyecto.ruta_codigo,
        proyecto.version_reglas if version is None else version,
        proyecto.conectado,
        proyecto.desconectado if desconectado is None else desconectado)
    auditoria.con_constancia(
        lambda comprobante: almacen.guardar(
            _ficha(proyecto.identificador), texto, comprobante),
        que_se_hizo=que_se_hizo,
        sobre_que=_ficha(proyecto.identificador),
        quien=quien,
        que_cambio=que_cambio,
        proyecto=proyecto.identificador,
        sesion=sesion)


def _identificador_libre(nombre):''')

# --- La excepción nueva ---
t = t.replace('''class VersionQueNoExiste(Exception):
    """El proyecto declara una versión de reglas que nunca se publicó."""''',
'''class VersionQueNoExiste(Exception):
    """El proyecto declara una versión de reglas que nunca se publicó."""


class NombreVacio(Exception):
    """Se intentó dejar un proyecto sin nombre."""''')

# --- Indexar aprende el campo nuevo ---
t = t.replace('''def _indexar(identificador, nombre, ruta, version, conectado):
    from .models import Proyecto
    proyecto, _ = Proyecto.objects.update_or_create(
        identificador=identificador,
        defaults={
            "nombre": nombre,
            "ruta_codigo": ruta,
            "ruta_normalizada": ruta_normalizada(ruta),
            "version_reglas": version,
            "conectado": conectado,
        })
    return proyecto''',
'''def _indexar(identificador, nombre, ruta, version, conectado,
             desconectado=""):
    from .models import Proyecto
    proyecto, _ = Proyecto.objects.update_or_create(
        identificador=identificador,
        defaults={
            "nombre": nombre,
            "ruta_codigo": ruta,
            "ruta_normalizada": ruta_normalizada(ruta),
            "version_reglas": version,
            "conectado": conectado,
            "desconectado": desconectado,
        })
    return proyecto''')

# --- Rehacer el índice lee el campo nuevo ---
t = t.replace('''        version = campos.get("Versión de reglas adoptada", "")
        _indexar(identificador,
                 campos.get("Nombre", identificador),
                 campos.get("Ruta del código", ""),
                 "" if version == "ninguna todavía" else version,
                 campos.get("Fecha de conexión", ""))
        cuantos += 1''',
'''        version = campos.get("Versión de reglas adoptada", "")
        # Una ficha de antes de la fase H no trae este campo, y se lee como un
        # proyecto conectado. Por eso no hubo que migrar nada.
        fuera = campos.get("Fecha de desconexión", "")
        _indexar(identificador,
                 campos.get("Nombre", identificador),
                 campos.get("Ruta del código", ""),
                 "" if version == "ninguna todavía" else version,
                 campos.get("Fecha de conexión", ""),
                 desconectado="" if fuera == "sigue conectado" else fuera)
        cuantos += 1''')

io.open(p, "w", encoding="utf-8", newline="\n").write(t)
print("core ok")
