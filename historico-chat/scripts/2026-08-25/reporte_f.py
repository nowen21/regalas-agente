# -*- coding: utf-8 -*-
"""Agrega a nucleo/importacion/core.py el reporte de la fase F."""
import io

p = "nucleo/importacion/core.py"
t = io.open(p, encoding="utf-8").read()

# --- El encabezado cuenta lo de la fase F ---
t = t.replace('''**Un documento se identifica por su ruta dentro del proyecto**, no por su
contenido. Por eso traer dos veces no duplica, y un documento que se editó
entra con su versión nueva sin crear otro (`RN-3`).
"""''',
'''**Un documento se identifica por su ruta dentro del proyecto**, no por su
contenido. Por eso traer dos veces no duplica, y un documento que se editó
entra con su versión nueva sin crear otro (`RN-3`).

**Cada traída deja su reporte escrito.** Antes de la fase F, el registro de
auditoría decía «994 reconocidos, 1 sin reconocer»: **cuántos, no cuáles**.
Para saber cuál era había que traer el proyecto entero otra vez. Ahora queda un
documento con su fecha, y el registro lo enlaza en vez de repetir la lista: dos
copias de lo mismo se separan.

**El reporte se escribe siempre**, también cuando no quedó nada afuera. Su
ausencia no distinguiría entre «salió limpio» y «no se corrió».
"""''')

# --- Escribir el reporte, dentro de traer ---
viejo = '''    auditoria.registrar(
        que_se_hizo="traer la documentación de un proyecto",
        sobre_que="proyectos/%s/traido" % proyecto.identificador,
        quien=quien,
        que_cambio="%d documento(s) reconocido(s), %d sin reconocer"
                   % (hallazgo.cuantos, len(hallazgo.sin_reconocer)),
        proyecto=proyecto.identificador,
        sesion=sesion)'''
nuevo = '''    donde_el_reporte = _donde_va_el_reporte(proyecto)
    auditoria.registrar(
        que_se_hizo="traer la documentación de un proyecto",
        sobre_que="proyectos/%s/traido" % proyecto.identificador,
        quien=quien,
        # **El registro enlaza el reporte; no repite la lista.** Un proyecto
        # que siga el estándar a medias puede dejar cientos de rutas sin
        # reconocer, y el registro quedaría ilegible justo cuando más falta
        # hace. Y la auditoría guarda la acción, no el contenido.
        que_cambio="%d documento(s) reconocido(s), %d sin reconocer. "
                   "El detalle, en %s"
                   % (hallazgo.cuantos, len(hallazgo.sin_reconocer),
                      donde_el_reporte),
        proyecto=proyecto.identificador,
        sesion=sesion)'''
assert viejo in t, "no se encontró el registro de auditoría"
t = t.replace(viejo, nuevo, 1)

# --- Escribirlo al terminar, antes de devolver ---
viejo = '''    return hallazgo, nuevos, ya_estaban


def _donde_queda(proyecto, relativa):'''
nuevo = '''    _escribir(donde_el_reporte, _texto_del_reporte(proyecto, hallazgo, nuevos,
                                                  ya_estaban))
    return hallazgo, nuevos, ya_estaban


def _donde_va_el_reporte(proyecto):
    """Un reporte por traída, con su fecha y su hora en el nombre.

    **No se sobrescribe uno solo.** Poder comparar dos traídas es la mitad del
    valor: muestra qué se corrigió entre una y otra.
    """
    cuando = timezone.localtime().strftime("%Y-%m-%d-%H%M%S")
    return "proyectos/%s/reportes/%s-lo-que-no-entro.md" % (
        proyecto.identificador, cuando)


def _texto_del_reporte(proyecto, hallazgo, nuevos, ya_estaban):
    """El reporte de una traída, en texto que se lee sin la plataforma."""
    cuando = timezone.localtime().strftime("%Y-%m-%d a las %H:%M")
    lineas = [
        "# Qué no entró al traer «%s»" % proyecto.nombre,
        "",
        "**Traído el %s.** De la carpeta `%s`." % (cuando, proyecto.ruta_codigo),
        "",
        "| Qué | Cuántos |",
        "|---|---|",
        "| Documentos que entraron | %d |" % hallazgo.cuantos,
        "| De esos, nuevos | %d |" % nuevos,
        "| De esos, que ya estaban y quedaron al día | %d |" % ya_estaban,
        "| **Que NO entraron** | **%d** |" % len(hallazgo.sin_reconocer),
        "",
        "## Lo que no siguió ningún molde conocido",
        "",
    ]
    if hallazgo.todo_reconocido:
        lineas += [
            "**Nada quedó afuera.** Todo lo que hay en la documentación de "
            "este proyecto sigue un molde que la plataforma conoce.",
            "",
            "Este reporte se escribe igual cuando no hay nada que reportar: su "
            "ausencia no distinguiría entre «salió limpio» y «no se corrió».",
        ]
    else:
        lineas += [
            "Estos %d archivos **no entraron**, y **no se transformaron**: "
            "quedaron donde estaban, tal como estaban. Adivinar su forma sería "
            "peor que no traerlos, porque ensuciaría lo que sí sirve."
            % len(hallazgo.sin_reconocer),
            "",
        ]
        lineas += ["- `%s`" % ruta for ruta in hallazgo.sin_reconocer]

    lineas += ["", "## Qué carpetas no se miraron, y por qué", ""]
    carpetas = hallazgo.carpetas_que_no_se_miraron
    if carpetas:
        lineas += [
            "Traer recorre solo la documentación del ciclo de vida. Estas "
            "carpetas del proyecto existen y **no se abrieron**:",
            "",
            "| Carpeta | Por qué no se mira |",
            "|---|---|",
        ]
        lineas += ["| `%s/` | %s |" % (nombre, porque)
                   for nombre, porque in carpetas]
    else:
        lineas.append("Este proyecto no tiene ninguna de las carpetas que "
                      "traer se salta.")
    lineas.append("")
    return "\\n".join(lineas)


def reportes_de(proyecto):
    """Los reportes de ese proyecto, del más nuevo al más viejo.

    Devuelve pares `(cuándo, ruta)`. Se leen del disco y no de un índice: el
    reporte es texto, y el texto es la fuente.
    """
    carpeta = os.path.join(str(almacen.carpeta_datos()), "proyectos",
                           proyecto.identificador, "reportes")
    if not os.path.isdir(carpeta):
        return []
    hallados = []
    for nombre in sorted(os.listdir(carpeta), reverse=True):
        if not nombre.endswith(".md"):
            continue
        cuando = nombre.split("-lo-que-no-entro")[0]
        hallados.append((cuando, "proyectos/%s/reportes/%s"
                         % (proyecto.identificador, nombre)))
    return hallados


def leer_reporte(nombre):
    """El texto de un reporte guardado, o "" si no está."""
    return almacen.leer(nombre) or ""


def _donde_queda(proyecto, relativa):'''
assert viejo in t, "no se encontró el final de traer"
t = t.replace(viejo, nuevo, 1)

t = t.replace('''import io
import os

from nucleo.almacen import core as almacen''',
'''import io
import os

from django.utils import timezone

from nucleo.almacen import core as almacen''')

io.open(p, "w", encoding="utf-8", newline="\n").write(t)
print("core ok")
