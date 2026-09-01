# -*- coding: utf-8 -*-
"""Convierte el expediente en un archivo, y lo deja guardado.

**Se genera desde el texto, y nunca al contrario** (`DA-09`). Lo que se pierde
está declarado y no es poco: quien recibe el entregable no puede devolver
correcciones escritas encima, tiene que pedirlas. Se aceptó a cambio de no
mantener un segundo original para siempre.

**Dos corridas dan el mismo archivo.** No se escribe la fecha de generación
adentro: una fecha haría distintos dos archivos idénticos, y entonces `CA-03` no
se podría comprobar más que de palabra. Cuándo se generó queda en la auditoría,
que es donde vive esa pregunta.

**Con documentos a medio llenar se avisa y no se impide.** La decisión de
entregar algo incompleto es del usuario; el programa la informa, no la toma.
"""
from nucleo.almacen import core as almacen
from nucleo.auditoria import core as auditoria
from . import core, marcado

# La envoltura del archivo. Sin nada que salga a la red: ni fuentes, ni hojas
# de estilo, ni guiones. Un entregable que necesita internet para verse bien no
# es un entregable.
_ENVOLTURA = u"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8"/>
<title>%(titulo)s</title>
<style>
body { font-family: Georgia, serif; max-width: 46em; margin: 2em auto;
       padding: 0 1em; line-height: 1.5; color: #222; }
h1, h2, h3, h4 { font-family: Arial, sans-serif; line-height: 1.25; }
table { border-collapse: collapse; width: 100%%; margin: 1em 0; }
th, td { border: 1px solid #bbb; padding: .4em .6em; text-align: left;
         vertical-align: top; }
th { background: #f0f0f0; }
td ul, th ul { margin: 0; padding-left: 1.2em; }
pre { background: #f6f6f6; padding: .8em; overflow-x: auto; }
code { font-family: Consolas, monospace; }
blockquote { border-left: 3px solid #bbb; margin-left: 0; padding-left: 1em;
             color: #444; }
.documento { border-top: 2px solid #888; margin-top: 3em; padding-top: 1em; }
.ruta { color: #666; font-size: .85em; font-family: Consolas, monospace; }
.aviso { background: #fff6d8; border: 1px solid #e0c46a; padding: .8em 1em; }
</style>
</head>
<body>
%(cuerpo)s
</body>
</html>
"""


def nombre_del_archivo(proyecto):
    """Dónde queda guardado el entregable de ese proyecto."""
    return "proyectos/%s/entregable/expediente.html" % proyecto


def _indice(expediente):
    """La tabla de contenido, que el expediente arma por su cuenta."""
    renglones = []
    for grupo in expediente["grupos"]:
        renglones.append(u"<li>%s <em>(%d)</em><ul>%s</ul></li>" % (
            marcado.escapar(grupo["grupo"]), len(grupo["documentos"]),
            "".join(u'<li><a href="#d%d">%s</a></li>'
                    % (documento.id, marcado.escapar(documento.origen))
                    for documento in grupo["documentos"])))
    return u"<h2>Contenido</h2><ul>%s</ul>" % "".join(renglones)


def _lo_que_falta(expediente):
    """Lo que falta y lo incompleto, **dentro del entregable**.

    Va en el archivo y no solo en la consola a propósito: quien lo recibe tiene
    que ver lo mismo que vio quien lo generó. Un entregable que se ve completo
    y no lo está es peor que uno que dice qué le falta.
    """
    if not expediente["falta"] and not expediente["incompletos"]:
        return u""
    partes = [u'<div class="aviso"><p><strong>Este expediente no está '
              u'completo.</strong> Lo que sigue es lo que le falta, dicho '
              u'antes de que nadie lo lea de más.</p>']
    if expediente["falta"]:
        partes.append(u"<p>Documentos que el ciclo espera y no están: %d.</p><ul>%s</ul>"
                      % (len(expediente["falta"]),
                         "".join(u"<li>%s: %s</li>"
                                 % (marcado.escapar(f["donde"]),
                                    marcado.escapar(f["que"]))
                                 for f in expediente["falta"][:40])))
    if expediente["incompletos"]:
        partes.append(u"<p>Documentos con espacios sin llenar: %d.</p><ul>%s</ul>"
                      % (len(expediente["incompletos"]),
                         "".join(u"<li>%s (%d)</li>"
                                 % (marcado.escapar(d["origen"]), d["huecos"])
                                 for d in expediente["incompletos"][:40])))
    partes.append(u"</div>")
    return "".join(partes)


def armar_el_texto(proyecto, expediente):
    """El archivo entero, como texto. **No escribe nada**: así se puede comparar."""
    cuerpo = [u"<h1>Expediente de %s</h1>" % marcado.escapar(proyecto),
              _lo_que_falta(expediente),
              _indice(expediente)]

    for grupo in expediente["grupos"]:
        cuerpo.append(u"<h2>%s</h2>" % marcado.escapar(grupo["grupo"]))
        for documento in grupo["documentos"]:
            cuerpo.append(
                u'<div class="documento" id="d%d">'
                u'<p class="ruta">%s</p>%s</div>'
                % (documento.id, marcado.escapar(documento.origen),
                   marcado.a_marcado(core._texto_de(documento))))

    return _ENVOLTURA % {"titulo": marcado.escapar(u"Expediente de %s" % proyecto),
                         "cuerpo": "\n".join(cuerpo)}


def generar(proyecto, hasta=None, quien="el usuario"):
    """Genera el entregable y lo guarda. `(nombre, avisos)`.

    `avisos` dice qué está incompleto. **No impide generar**: la decisión de
    entregar es del usuario.
    """
    expediente = core.armar(proyecto, hasta)
    if not expediente["grupos"]:
        return ("", [u"Ese proyecto no tiene documentos traídos: "
                     u"no hay qué generar."])

    avisos = []
    if expediente["falta"]:
        avisos.append(u"Faltan %d documento(s) que el ciclo espera."
                      % len(expediente["falta"]))
    if expediente["incompletos"]:
        avisos.append(u"Hay %d documento(s) con espacios sin llenar."
                      % len(expediente["incompletos"]))

    texto = armar_el_texto(proyecto, expediente)
    nombre = nombre_del_archivo(proyecto)
    auditoria.con_constancia(
        lambda comprobante: almacen.guardar(nombre, texto, comprobante),
        que_se_hizo="generar el entregable del expediente",
        sobre_que=nombre, quien=quien,
        que_cambio="%d documento(s)" % core.cuantos_documentos(expediente),
        proyecto=proyecto)
    return (nombre, avisos)
