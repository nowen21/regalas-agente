# -*- coding: utf-8 -*-
"""Traer a la plataforma la documentación que un proyecto ya tiene escrita.

**Traer copia, nunca mueve ni modifica.** Si algo sale mal, el proyecto de
origen queda exactamente como estaba. Es `RN-1` de la especificación, y es la
promesa más importante de este módulo: es el que más archivos ajenos lee.

**Primero se mira, después se trae.** `mirar` recorre y cuenta sin escribir
nada; `traer` escribe. La pantalla muestra lo que `mirar` devolvió y pide
confirmación, porque traer cambia el estado y mueve cientos de documentos de
una vez (`00·N1`).

**Si falla a mitad, no queda nada de esa pasada.** Media importación es peor
que ninguna: nadie sabe qué falta ni por dónde seguir.

**Un documento se identifica por su ruta dentro del proyecto**, no por su
contenido. Por eso traer dos veces no duplica, y un documento que se editó
entra con su versión nueva sin crear otro (`RN-3`).

**Cada traída deja su reporte escrito.** Antes de la fase F, el registro de
auditoría decía «994 reconocidos, 1 sin reconocer»: **cuántos, no cuáles**.
Para saber cuál era había que traer el proyecto entero otra vez. Ahora queda un
documento con su fecha, y el registro lo enlaza en vez de repetir la lista: dos
copias de lo mismo se separan.

**El reporte se escribe siempre**, también cuando no quedó nada afuera. Su
ausencia no distinguiría entre «salió limpio» y «no se corrió».
"""
import io
import os

from django.utils import timezone

from nucleo.almacen import core as almacen
from nucleo.auditoria import core as auditoria
from . import moldes


class NoSePudoTraer(Exception):
    """Falló la traída. No queda nada de esa pasada."""


class Hallazgo(object):
    """Lo que se encontró al mirar, sin haber escrito nada todavía."""

    def __init__(self, proyecto):
        self.proyecto = proyecto
        self.reconocidos = []      # (ruta relativa, tipo)
        self.sin_reconocer = []    # rutas relativas
        self.carpetas_del_ciclo = []

    @property
    def por_tipo(self):
        """Cuántos de cada tipo. Es lo que se le muestra al usuario.

        **El recuento, no la lista entera.** Un número por tipo se lee; mil
        líneas se confirman sin mirar, y entonces la confirmación deja de
        proteger.
        """
        cuenta = {}
        for _, tipo in self.reconocidos:
            cuenta[tipo] = cuenta.get(tipo, 0) + 1
        return sorted(cuenta.items())

    @property
    def cuantos(self):
        return len(self.reconocidos)

    @property
    def todo_reconocido(self):
        return not self.sin_reconocer

    @property
    def hay_documentacion(self):
        return bool(self.carpetas_del_ciclo)

    @property
    def carpetas_que_no_se_miraron(self):
        """Las que existen en este proyecto, con el porqué. Nunca en silencio."""
        if not self.proyecto.ruta_viva:
            return []
        return [(nombre, porque)
                for nombre, porque in moldes.CARPETAS_QUE_NO_SE_MIRAN
                if os.path.isdir(os.path.join(self.proyecto.ruta_codigo, nombre))]


def mirar(proyecto):
    """Recorre la documentación del proyecto y cuenta. **No escribe nada.**"""
    hallazgo = Hallazgo(proyecto)
    if not proyecto.ruta_viva:
        return hallazgo

    # Se recorren **las dos** carpetas del ciclo: la de épicas, historias y
    # fases, y la de las siete etapas. Que la segunda faltara era el hueco de
    # la fase E, y se saltaba en silencio.
    for carpeta in moldes.CARPETAS_DEL_CICLO:
        ciclo = os.path.join(proyecto.ruta_codigo, carpeta)
        if not os.path.isdir(ciclo):
            continue
        hallazgo.carpetas_del_ciclo.append(ciclo)

        for raiz, _, archivos in os.walk(ciclo):
            for nombre in sorted(archivos):
                if not nombre.endswith(".md"):
                    continue
                relativa = os.path.relpath(
                    os.path.join(raiz, nombre),
                    proyecto.ruta_codigo).replace(os.sep, "/")
                tipo = moldes.tipo_de(nombre, relativa)
                if tipo:
                    hallazgo.reconocidos.append((relativa, tipo))
                else:
                    hallazgo.sin_reconocer.append(relativa)
    return hallazgo


def traer(proyecto, quien="el usuario", sesion=""):
    """Trae lo reconocido. Devuelve el hallazgo, con cuántos entraron y cuántos ya estaban.

    Deja la constancia **antes** de escribir, y si algo falla a mitad borra lo
    de esta pasada.
    """
    from .models import Traido

    hallazgo = mirar(proyecto)

    # **Traer sin que entre nada también es una traída**, y también deja su
    # registro y su reporte. Antes se salía por acá sin escribir ninguno de
    # los dos, y ese era justo el caso donde más falta hacen: alguien trae un
    # proyecto, no entra nada, y no queda constancia de que se intentó ni de
    # por qué no entró. Lo encontró `CP-008` de la fase F.
    donde_el_reporte = _donde_va_el_reporte(proyecto)
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
        sesion=sesion)

    nuevos, ya_estaban, escritos, anotados = 0, 0, [], []
    try:
        for relativa, tipo in hallazgo.reconocidos:
            origen = os.path.join(proyecto.ruta_codigo,
                                  relativa.replace("/", os.sep))
            # `newline=""` es lo que impide que Python traduzca los saltos
            # de línea de Windows a los de Unix al leer. Sin eso, traer un
            # documento escrito en Windows lo **transformaba en silencio**, que
            # es justo lo que `CA-5` prohíbe. Lo encontró `CP-002`.
            with io.open(origen, encoding="utf-8", errors="replace",
                         newline="") as abierto:
                texto = abierto.read()

            destino = _donde_queda(proyecto, relativa)
            existia = Traido.objects.filter(proyecto=proyecto.identificador,
                                            origen=relativa).first()
            _escribir(destino, texto)
            escritos.append(destino)

            if existia:
                ya_estaban += 1
                # Se actualiza, no se duplica: es el mismo documento con otra
                # versión. Lo identifica su ruta de origen, no su contenido.
                Traido.objects.filter(pk=existia.pk).update(
                    tipo=tipo, guardado_en=destino)
            else:
                nuevos += 1
                anotado = Traido.objects.create(
                    proyecto=proyecto.identificador, origen=relativa,
                    tipo=tipo, guardado_en=destino)
                anotados.append(anotado.pk)
    except Exception as falla:
        _deshacer(escritos, anotados)
        raise NoSePudoTraer(
            "No se pudo traer la documentación: %s. No quedó nada de esta "
            "pasada, y el proyecto de origen está intacto." % falla)

    _escribir(donde_el_reporte, _texto_del_reporte(proyecto, hallazgo, nuevos,
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
        cuantos = len(hallazgo.sin_reconocer)
        lineas += [
            "%s **no entró** y **no se transformó**: quedó donde estaba, tal "
            "como estaba. Adivinar su forma sería peor que no traerlo, porque "
            "ensuciaría lo que sí sirve."
            % ("Este archivo" if cuantos == 1
               else "Estos %d archivos" % cuantos),
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
    return "\n".join(lineas)


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


def _donde_queda(proyecto, relativa):
    """Dónde vive dentro de la plataforma un documento traído."""
    return "proyectos/%s/traido/%s" % (proyecto.identificador, relativa)


def _escribir(nombre, texto):
    """Escribe sin pasar por el comprobante, y por una razón que hay que decir.

    Traer es **una sola** acción del usuario que produce cientos de escrituras.
    La constancia se deja una vez, antes de empezar, con el recuento de lo que
    va a entrar. Pedir un comprobante por archivo llenaría el registro de mil
    líneas y escondería las acciones que sí hay que poder encontrar.
    """
    destino = almacen._ruta_real(nombre)
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with io.open(destino, "w", encoding="utf-8", newline="") as archivo:
        archivo.write(texto)


def _deshacer(escritos, anotados):
    """Borra lo que esta pasada alcanzó a dejar. Nunca toca el origen.

    **Hay que borrar las dos cosas: los archivos y sus filas del índice.**
    Borrar solo los archivos dejaba el índice diciendo que había documentos
    traídos que ya no existían, que es media importación con otra cara. Lo
    encontró `CP-007`.
    """
    from .models import Traido
    for nombre in escritos:
        try:
            os.remove(almacen._ruta_real(nombre))
        except OSError:
            pass
    if anotados:
        Traido.objects.filter(pk__in=anotados).delete()


def reconstruir_indice():
    """Rehace el índice de lo traído leyendo la carpeta `traido/` de cada proyecto."""
    from .models import Traido
    from nucleo.proyectos.models import Proyecto

    Traido.objects.all().delete()
    cuantos = 0
    for proyecto in Proyecto.objects.all():
        raiz = os.path.join(str(almacen.carpeta_datos()), "proyectos",
                            proyecto.identificador, "traido")
        if not os.path.isdir(raiz):
            continue
        for carpeta, _, archivos in os.walk(raiz):
            for nombre in sorted(archivos):
                completa = os.path.join(carpeta, nombre)
                relativa = os.path.relpath(completa, raiz).replace(os.sep, "/")
                Traido.objects.create(
                    proyecto=proyecto.identificador,
                    origen=relativa,
                    tipo=moldes.tipo_de(nombre, relativa),
                    guardado_en=_donde_queda(proyecto, relativa))
                cuantos += 1
    return cuantos
