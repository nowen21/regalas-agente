# -*- coding: utf-8 -*-
"""`EP-027·HU-002` · Las reglas del texto pasan a sus tablas, y el texto se arma desde ellas.

- `pasar_documento` lee cada regla de un documento con `molde.leer` y la guarda
  en su fila, con su capítulo, sus tareas y sus dependencias.
- Las notas con fecha del sello («Corregida el...», «Partida el...») pasan a la
  historia de su regla, con su fecha, y salen del sello (análisis 1 del
  pendiente 136, acuerdo 1). El agente no recibe el sello: lo que le llega no
  cambia.
- `armar_documento` vuelve a escribir el texto del documento desde las tablas.

Pasar de nuevo no duplica: actualiza la fila de cada código y no repite notas.
"""
import datetime
import os
import re

from django.db import transaction

from core.historia.models import CAMBIAR, Cambio
from core.historia.registro import anotar

from . import molde
from .models import (FALTA_EL_PROGRAMA, NO_VALIDABLE, SIN_DECLARAR, VALIDABLE, Capitulo, Dependencia, Documento,
                     Regla, ReglaTarea, Tarea)
from .presentar import es_cabeza, leer_titulo

VALIDABLES = "validadores/reglas-validables.md"
QUIEN_NOTA = "nota del sello"
_CAPITULO = re.compile(r"^base/((\d\d)-[^/]+?)(?:\.md)?(?:/|$)")
_NOTA = re.compile(r"^\*\*[^*\n]{0,80}\b(?:el|del) (\d{4}-\d{2}-\d{2})")
_CODIGO = re.compile(r"\b([A-Z]{1,4}\d+(?:\.\d+)?)\b")


# --- «Validable», desde su registro ----------------------------------------

def validables(texto):
    """`{código: (valor, programa)}` de `validadores/reglas-validables.md`.
    Una regla que el registro nombra en dos listas se queda con la primera de
    estas: «Ya son validadores», «Validables, faltan», «No validables»: la prosa
    de una lista nombra reglas de otra («F8 salió de esta lista»)."""
    seccion, salida = None, {}
    hallado = {VALIDABLE: {}, FALTA_EL_PROGRAMA: {}, NO_VALIDABLE: {}}
    for linea in (texto or "").replace("\r\n", "\n").split("\n"):
        if linea.startswith("## "):
            seccion = (VALIDABLE if "Ya son validadores" in linea else FALTA_EL_PROGRAMA
                       if "Validables, faltan" in linea else NO_VALIDABLE if "No validables" in linea else None)
            continue
        if seccion in (VALIDABLE, FALTA_EL_PROGRAMA) and linea.startswith("|") and not linea.startswith("|---"):
            celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
            if celdas[0] == "Regla":
                continue
            programa = re.sub(r"[`*]|\[([^\]]*)\]\([^)]*\)", r"\1", celdas[1]).strip() if seccion == VALIDABLE else ""
            for codigo in _CODIGO.findall(re.sub(r"\]\([^)]*\)", "]", celdas[0])):
                hallado[seccion].setdefault(codigo, programa)
        elif seccion == NO_VALIDABLE and linea.startswith("- "):
            for codigo in _CODIGO.findall(re.sub(r"\]\([^)]*\)", "]", linea)):
                hallado[NO_VALIDABLE].setdefault(codigo, "")
    for valor in (NO_VALIDABLE, FALTA_EL_PROGRAMA, VALIDABLE):
        for codigo, programa in hallado[valor].items():
            salida[codigo] = (valor, programa)
    return salida


def leer_validables(raiz):
    ruta = os.path.join(raiz, *VALIDABLES.split("/"))
    if not os.path.isfile(ruta):
        return {}
    with open(ruta, encoding="utf-8") as archivo:
        return validables(archivo.read())


# --- Del texto a las tablas ------------------------------------------------

def capitulo_de(documento):
    """El capítulo de un documento de `base/`, creado si falta. None si no es de un capítulo."""
    m = _CAPITULO.match(documento.ruta)
    if not m:
        return None
    capitulo, _ = Capitulo.objects.get_or_create(clave=m.group(1), defaults={"numero": m.group(2),
                                                                            "nombre": m.group(1)})
    if es_cabeza(documento.ruta):
        nombre = leer_titulo(documento.contenido)[0] or capitulo.nombre
        if (capitulo.nombre, capitulo.documento_id) != (nombre, documento.pk):
            capitulo.nombre, capitulo.documento = nombre, documento
            capitulo.save()
    return capitulo


def separar_notas(sello):
    """`(sello sin las notas con fecha, [(fecha, nota)])`."""
    quedan, notas = [], []
    for parrafo in (sello or "").split("\n\n"):
        m = _NOTA.match(parrafo)
        if m:
            notas.append((m.group(1), parrafo.strip()))
        else:
            quedan.append(parrafo)
    return "\n\n".join(quedan), notas


def _notas_a_la_historia(regla, notas):
    tabla = "estandar.regla"
    for fecha, texto in notas:
        if Cambio.objects.filter(tabla=tabla, fila=str(regla.pk), quien=QUIEN_NOTA, motivo=texto).exists():
            continue
        cambio = anotar(tabla, regla.pk, CAMBIAR)
        if cambio is None:
            continue
        cuando = datetime.datetime.combine(datetime.date.fromisoformat(fecha), datetime.time(12, 0),
                                           tzinfo=datetime.timezone.utc)
        Cambio.objects.filter(pk=cambio.pk).update(quien=QUIEN_NOTA, motivo=texto, fecha=cuando)


def _casillas_a_fila(casillas, sello):
    incorrecto, correcto = molde.par_del_ejemplo(casillas["ejemplo"])
    condicion, limite, autoriza = molde.partes_de_la_excepcion(casillas["excepcion"])
    resultado, version, fecha, observacion = molde.sello_de(sello)
    return {
        "titulo": casillas["titulo"], "marca": casillas["marca"], "marca_texto": casillas["marca_texto"],
        "exigencia": casillas["exigencia"], "excepcion": casillas["excepcion"],
        "excepcion_condicion": condicion, "excepcion_limite": limite, "excepcion_autoriza": autoriza,
        "ejemplo": casillas["ejemplo"], "ejemplo_incorrecto": incorrecto, "ejemplo_correcto": correcto,
        "notas": casillas["notas"], "quien_cumple": casillas["quien_cumple"],
        "autoriza_escribir": casillas["autoriza_escribir"], "raya": casillas["raya"], "sello": sello,
        "sello_resultado": resultado, "sello_version": version,
        "sello_fecha": datetime.date.fromisoformat(fecha) if fecha else None, "sello_observacion": observacion,
    }


def _guardar(regla, datos):
    cambio = [k for k, v in datos.items() if getattr(regla, k) != v]
    for k, v in datos.items():
        setattr(regla, k, v)
    if regla.pk is None or cambio:
        regla.full_clean()
        regla.save()


def _tareas(regla, nombres):
    actuales = [a.tarea.nombre for a in regla.aplica.select_related("tarea")]
    if actuales == nombres:
        return
    regla.aplica.all().delete()
    for orden, nombre in enumerate(nombres):
        ReglaTarea.objects.create(regla=regla, tarea=Tarea.objects.get_or_create(nombre=nombre)[0], orden=orden)


def _dependencias(regla, casillas):
    esperadas = {(tipo, codigo) for tipo, _, codigo in
                 molde.dependencias(casillas["exigencia"], casillas["excepcion"], casillas["notas"])
                 if codigo != regla.codigo}
    actuales = {(d.tipo, d.codigo): d for d in regla.dependencias.all()}
    for clave, dependencia in actuales.items():
        if clave not in esperadas:
            dependencia.delete()
    for tipo, codigo in esperadas - set(actuales):
        Dependencia.objects.create(regla=regla, tipo=tipo, codigo=codigo)


def pasar_documento(documento, validable=None):
    """Guarda en las tablas cada regla del texto de `documento`. Devuelve sus reglas en orden."""
    texto = (documento.contenido or "").replace("\r\n", "\n")
    capitulo = capitulo_de(documento)
    reglas = []
    for orden, (inicio, fin, codigo) in enumerate(molde.partir(texto)):
        casillas = molde.leer(texto[inicio:fin])
        sello, notas = separar_notas(casillas["sello"])
        regla = Regla.objects.filter(codigo=codigo, proyecto__isnull=True).first() or Regla(codigo=codigo)
        datos = _casillas_a_fila(casillas, sello)
        datos.update(capitulo=capitulo, documento=documento, orden=orden)
        if validable is not None:
            datos["validable"], datos["validador"] = validable.get(codigo, (SIN_DECLARAR, ""))
        _guardar(regla, datos)
        _tareas(regla, molde.tareas(casillas["aplica_a"]))
        _dependencias(regla, casillas)
        _notas_a_la_historia(regla, notas)
        reglas.append(regla)
    _apartar_las_que_salieron(documento, reglas)
    if capitulo and reglas and not capitulo.prefijo:
        capitulo.prefijo = re.match(r"[A-Z]+", reglas[0].codigo).group(0)
        capitulo.save()
    return reglas


def _apartar_las_que_salieron(documento, reglas):
    """La regla que salió del texto no se borra (`20·M11`): queda sin documento."""
    for regla in Regla.objects.filter(documento=documento).exclude(pk__in=[r.pk for r in reglas]):
        regla.documento = None
        regla.save()


def enlazar_dependencias():
    """Une cada dependencia con la regla de destino, por su código."""
    por_codigo = dict(Regla.objects.filter(proyecto__isnull=True).values_list("codigo", "pk"))
    for dependencia in Dependencia.objects.filter(regla__proyecto__isnull=True):
        destino = por_codigo.get(dependencia.codigo)
        if dependencia.destino_id != destino:
            dependencia.destino_id = destino
            dependencia.save()


# --- De las tablas al texto -------------------------------------------------

def casillas_de(regla):
    """Las casillas de `molde.armar`, desde la fila."""
    return {
        "codigo": regla.codigo, "titulo": regla.titulo, "marca_texto": regla.marca_texto,
        "exigencia": regla.exigencia, "excepcion": regla.excepcion, "ejemplo": regla.ejemplo,
        "notas": regla.notas, "quien_cumple": regla.quien_cumple,
        "aplica_a": ", ".join(a.tarea.nombre for a in regla.aplica.select_related("tarea")),
        "autoriza_escribir": regla.autoriza_escribir, "raya": regla.raya, "sello": regla.sello,
    }


def texto_armado(documento):
    """El texto del documento con cada regla escrita desde su fila."""
    texto = (documento.contenido or "").replace("\r\n", "\n")
    filas = {r.codigo: r for r in Regla.objects.filter(documento=documento, proyecto__isnull=True)}
    for inicio, fin, codigo in reversed(molde.partir(texto)):
        if codigo in filas:
            texto = texto[:inicio] + molde.armar(casillas_de(filas[codigo])) + texto[fin:]
    return texto


def armar_documento(documento):
    """Guarda el texto armado desde las tablas, si cambió. Devuelve si cambió."""
    texto = texto_armado(documento)
    if texto == (documento.contenido or "").replace("\r\n", "\n"):
        return False
    documento.contenido = texto
    documento.save()
    return True


def pasar_todo(raiz):
    """Pasa todo el estándar a las tablas y arma de nuevo cada documento.
    Devuelve `(reglas, documentos que cambiaron)`. Todo o nada."""
    validable = leer_validables(raiz)
    with transaction.atomic():
        documentos = list(Documento.objects.filter(ruta__startswith="base/")
                          .exclude(ruta__startswith="base/reglas-por-tarea/").order_by("ruta"))
        total = 0
        for documento in documentos:
            total += len(pasar_documento(documento, validable))
        enlazar_dependencias()
        cambiados = [d.ruta for d in documentos if armar_documento(d)]
    return total, cambiados


# --- EP-027·HU-003 · Todo cambio de un documento pasa por las tablas ---------

def es_de_reglas(documento):
    return documento.ruta.startswith("base/") and not documento.ruta.startswith("base/reglas-por-tarea/")


def pasar_y_armar(documento):
    """Lo que se guardó en el texto pasa a las tablas, y el texto se guarda armado desde ellas."""
    if not es_de_reglas(documento):
        return
    pasar_documento(documento)
    enlazar_dependencias()
    armar_documento(documento)


def soltar_reglas(documento):
    """Antes de quitar un documento: sus reglas quedan sin documento, no se borran (`20·M11`)."""
    for regla in Regla.objects.filter(documento=documento):
        regla.documento = None
        regla.save()


# --- EP-027·HU-006 · Las reglas de cada proyecto, en la misma tabla ----------

ARCHIVO_DEL_PROYECTO = ".agente/reglas-proyecto.md"


class CodigoRepetido(ValueError):
    """Dos reglas del proyecto con el mismo código: no pasa ninguna (RN-08 de la épica, errores)."""
_GRUPO = re.compile(r"^## (?![A-Z]+\d+(?:\.\d+)? · )(.+?)\s*$")


def _grupos(texto, nivel):
    """`{posición del encabezado de la regla: grupo}`: la sección `##` donde va
    cada regla escrita en `###`. «Reglas», a secas, no es grupo."""
    if nivel != 3:
        return {}
    salida, actual, pos, dentro = {}, "", 0, False
    for linea in texto.split("\n"):
        if linea.lstrip().startswith(("```", "~~~")):
            dentro = not dentro
        m = _GRUPO.match(linea) if not dentro else None
        if m:
            nombre = re.sub(r"\s*·?\s*`[^`]*`\s*$", "", m.group(1)).strip()
            actual = "" if nombre.lower() == "reglas" else nombre
        salida[pos] = actual
        pos += len(linea) + 1
    return salida


def pasar_reglas_del_proyecto(proyecto, texto):
    """Guarda en la tabla, con su proyecto, cada regla del texto de sus reglas. Devuelve sus reglas en orden."""
    texto = (texto or "").replace("\r\n", "\n")
    nivel = molde.nivel_de(texto)
    grupos = _grupos(texto, nivel)
    bloques = molde.partir(texto, nivel)
    codigos = [codigo for _, _, codigo in bloques]
    repetidos = sorted({c for c in codigos if codigos.count(c) > 1})
    if repetidos:
        raise CodigoRepetido("%s tiene códigos repetidos: %s. El código no se cambia por su cuenta (20·M4): "
                             "lo decide el proyecto" % (proyecto, ", ".join(repetidos)))
    reglas = []
    for orden, (inicio, fin, codigo) in enumerate(bloques):
        casillas = molde.leer(texto[inicio:fin])
        sello, notas = separar_notas(casillas["sello"])
        regla = Regla.objects.filter(codigo=codigo, proyecto=proyecto).first() or Regla(codigo=codigo,
                                                                                        proyecto=proyecto)
        datos = _casillas_a_fila(casillas, sello)
        datos.update(orden=orden, grupo=grupos.get(inicio, ""), apartada=False)
        _guardar(regla, datos)
        _tareas(regla, molde.tareas(casillas["aplica_a"]))
        _dependencias(regla, casillas)
        _notas_a_la_historia(regla, notas)
        reglas.append(regla)
    for regla in Regla.objects.filter(proyecto=proyecto, apartada=False).exclude(pk__in=[r.pk for r in reglas]):
        regla.apartada = True
        regla.save()
    return reglas


def texto_del_proyecto(proyecto):
    """Las reglas del proyecto armadas desde la tabla, por grupo, como se cambian en la pantalla."""
    partes, grupo = ["# Reglas propias de %s" % proyecto.nombre], None
    for regla in Regla.objects.filter(proyecto=proyecto, apartada=False).order_by("orden", "pk"):
        if regla.grupo != grupo:
            grupo = regla.grupo
            partes.append("## %s" % (grupo or "Reglas"))
        partes.append(molde.armar(casillas_de(regla), nivel=3))
    return "\n\n".join(partes) + "\n"


def guardar_reglas_del_proyecto(proyecto, texto):
    """Lo que se cambió en la pantalla pasa a la tabla. La regla que salió del texto
    queda apartada: nada se borra (`20·M11`). Devuelve las reglas del texto."""
    with transaction.atomic():
        reglas = pasar_reglas_del_proyecto(proyecto, texto)
    return reglas


def archivo_a_la_historia(proyecto, texto):
    """El archivo de reglas entero queda en la historia del proyecto antes de borrarlo."""
    from core.historia.models import CAMBIAR as _CAMBIAR

    return anotar("proyectos.proyecto", proyecto.pk, _CAMBIAR, antes={ARCHIVO_DEL_PROYECTO: texto},
                  despues={ARCHIVO_DEL_PROYECTO: "en la tabla de reglas de Cimiento"})
