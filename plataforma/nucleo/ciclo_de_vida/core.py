# -*- coding: utf-8 -*-
"""Qué le falta a un documento del ciclo. **Solo lee; no escribe nada.**

Se calcula al pedirlo, leyendo el archivo. Guardar la lista crearía una segunda
verdad que envejece en cuanto alguien edite el documento por fuera, que es lo
que `DA-01` viene a evitar.

**Escribir es de la otra historia.** Acá se cuenta y se ubica; llenar el hueco
llega con la `HU-002`. Se separaron porque fallan distinto: contar mal da un
número equivocado, escribir mal daña un documento.
"""
import io
import os

from django.conf import settings

from nucleo.auditoria.core import con_constancia
from nucleo.importacion.models import Traido
from nucleo.seguridad import claves
from . import escritura, huecos, moldes


def _carpeta_de_plantillas():
    """Dónde vive `plantillas/` del estándar."""
    declarada = getattr(settings, "CARPETA_PLANTILLAS", None)
    if declarada:
        return str(declarada)
    return os.path.join(str(settings.RAIZ.parent), "plantillas")


def _texto_de(traido):
    """El texto guardado de un documento, o `""` si no se puede leer."""
    ruta = os.path.join(str(settings.CARPETA_DATOS),
                        traido.guardado_en.replace("/", os.sep))
    try:
        with io.open(ruta, encoding="utf-8", errors="replace") as abierto:
            return abierto.read()
    except OSError:
        return ""


def que_le_falta(proyecto, origen):
    """Qué molde sigue un documento y qué huecos le faltan.

    Devuelve `None` si ese documento no está traído. Si está, devuelve siempre
    las tres listas, aunque estén vacías: un documento sin huecos **lo dice**,
    en vez de responder con una lista vacía que no se sabe interpretar.
    """
    try:
        traido = Traido.objects.get(proyecto=proyecto, origen=origen)
    except Traido.DoesNotExist:
        return None
    return de_un_texto(_texto_de(traido), traido.tipo, traido.origen)


def de_un_texto(texto, tipo, relativa=""):
    """Lo mismo, sobre un texto que ya se tiene. Es lo que se puede probar.

    Se parte en dos para que la comprobación no necesite base de datos ni
    archivos: lo que decide es el texto y el tipo, no de dónde salieron.
    """
    sin_tipo = not tipo
    porque_no = moldes.por_que_no_tiene_molde(tipo)
    ruta_molde = moldes.molde_de(tipo, relativa)

    del_molde = ()
    if ruta_molde:
        del_molde = huecos.marcas_del_molde(
            moldes.texto_del_molde(_carpeta_de_plantillas(), tipo, relativa))

    hallados = huecos.encontrar(texto, del_molde)
    ciertos = huecos.por_clase(hallados, huecos.CIERTO)
    posibles = huecos.por_clase(hallados, huecos.POSIBLE)
    instalacion = huecos.por_clase(hallados, huecos.INSTALACION)

    return {
        "tipo": tipo,
        "molde": ruta_molde,
        # Las tres razones por las que puede no haber molde, separadas. Un tipo
        # desconocido se arregla enseñándoselo a Importación; un tipo sin molde,
        # escribiendo el molde. Confundirlos esconde el que sí tiene arreglo.
        "sin_tipo": sin_tipo,
        "sin_molde": porque_no,
        "molde_perdido": bool(ruta_molde) and not del_molde and not sin_tipo,
        "ciertos": ciertos,
        "posibles": posibles,
        "instalacion": instalacion,
        # La cuenta que manda. Es la del usuario, y es la misma que da el módulo
        # Expediente: las dos cuentan `«…»`.
        "cuantos": len(ciertos),
        "completo": not ciertos,
    }


def de_un_proyecto(proyecto):
    """Lo que le falta a cada documento de un proyecto, de más a menos.

    Los que no tienen ningún hueco cierto no salen: la lista es de trabajo por
    hacer, y un documento completo no es trabajo.
    """
    salida = []
    for traido in Traido.objects.filter(proyecto=proyecto):
        falta = de_un_texto(_texto_de(traido), traido.tipo, traido.origen)
        if falta["cuantos"]:
            falta["origen"] = traido.origen
            salida.append(falta)
    salida.sort(key=lambda uno: (-uno["cuantos"], uno["origen"]))
    return salida


def ruta_original(proyecto, origen):
    """Dónde vive de verdad ese documento, en el proyecto del usuario.

    **No es la copia de `datos/`.** Se decidió el 2026-09-01 escribir en el
    original: la copia se rehace al importar, así que lo escrito ahí se
    perdería, y el proyecto quedaría igual, que es no hacer nada.
    """
    from nucleo.proyectos.models import Proyecto
    try:
        registrado = Proyecto.objects.get(identificador=proyecto)
    except Proyecto.DoesNotExist:
        return ""
    return os.path.join(registrado.ruta_codigo,
                        origen.replace("/", os.sep))


def huecos_del_original(proyecto, origen):
    """Lo que le falta al archivo del proyecto, no a la copia.

    Devuelve `(ruta, huella, falta)`. La huella es la de ahora: se guarda para
    comprobar, al escribir, que nadie más lo tocó mientras tanto.

    **Se mira el original y no la copia** porque es donde se va a escribir. Si
    los dos se separaron, el que manda es el del proyecto.
    """
    try:
        traido = Traido.objects.get(proyecto=proyecto, origen=origen)
    except Traido.DoesNotExist:
        return "", "", None
    ruta = ruta_original(proyecto, origen)
    if not ruta or not os.path.exists(ruta):
        return ruta, "", None
    texto = escritura.leer_tal_cual(ruta)
    return ruta, escritura.huella(texto), de_un_texto(texto, traido.tipo,
                                                      traido.origen)


def llenar(proyecto, origen, numero, con, quien="el usuario",
           huella_de_cuando_se_leyo=""):
    """Llena el hueco número `numero` de un documento. Devuelve qué le queda.

    `numero` cuenta desde uno, y **solo sobre los huecos ciertos**: son los que
    se le preguntan al usuario. Los posibles y los de instalación no se llenan
    por acá.

    Levanta `escritura.SeMovio` si el documento cambió donde iba el hueco, y
    `escritura.CambioAjeno` si alguien más escribió desde que se leyó. En los
    dos casos **no se escribe nada**.
    """
    ruta, huella_ahora, falta = huecos_del_original(proyecto, origen)
    if falta is None:
        return None
    ciertos = falta["ciertos"]
    if numero < 1 or numero > len(ciertos):
        raise ValueError(
            "Ese documento tiene %d espacio(s) por llenar; se pidió el %d."
            % (len(ciertos), numero))

    esperada = huella_de_cuando_se_leyo or huella_ahora
    hueco = ciertos[numero - 1]

    # **Se tapa lo que se teclea.** Este es el camino por el que una persona
    # escribe algo nuevo, y ahí es donde se le puede escapar una clave pegada.
    # Lo importado no pasa por acá y no se toca: taparlo alteraría documentos
    # que ya existían, sin vuelta atrás (`RN-1` y `RN-3` del módulo Seguridad).
    con, tapadas = claves.tapar(con)

    # La constancia va **antes** del efecto, como en el resto de la plataforma:
    # un cambio sin registro es un cambio que nadie puede auditar (`DA-08`).
    con_constancia(
        lambda comprobante: escritura.llenar_el_hueco(ruta, hueco, con,
                                                      esperada),
        que_se_hizo="llenar un espacio de un documento del ciclo",
        sobre_que=origen, quien=quien, proyecto=proyecto,
        que_cambio="linea %d: %s" % (hueco["linea"], hueco["marca"]))

    _poner_al_dia_la_copia(proyecto, origen, ruta)
    _, _, quedan = huecos_del_original(proyecto, origen)
    # Cuántas se taparon va de vuelta: tapar en silencio deja al usuario
    # creyendo que escribió otra cosa.
    quedan["tapadas"] = tapadas
    return quedan


def _poner_al_dia_la_copia(proyecto, origen, ruta):
    """Deja la copia de `datos/` igual que el original que se acaba de escribir.

    Sin esto, la cuenta seguiría mostrando el hueco que ya se llenó, porque la
    cuenta de un proyecto entero se calcula sobre lo traído.

    **Se copia tal cual**, con sus finales de línea, y de un golpe: la copia se
    rehace al importar, pero mientras tanto tiene que decir la verdad.
    """
    try:
        traido = Traido.objects.get(proyecto=proyecto, origen=origen)
    except Traido.DoesNotExist:
        return
    destino = os.path.join(str(settings.CARPETA_DATOS),
                           traido.guardado_en.replace("/", os.sep))
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    escritura.guardar_de_un_golpe(destino, escritura.leer_tal_cual(ruta))


def para_la_consola(texto):
    """El texto sin lo que la consola no pueda escribir.

    **La consola de Windows no habla el alfabeto entero.** Un documento del
    ciclo trae emojis en sus tablas de estaciones, y mostrarlos revienta el
    programa con un error de codificación en vez de mostrar el hueco.

    Se vio corriendo la orden sobre un documento real: se cayó al llegar a un
    renglón con una marca de aprobación. Perder un signo al mostrarlo no cuesta
    nada; no poder ver el hueco, sí.
    """
    import sys
    como_escribe = getattr(sys.stdout, "encoding", None) or "utf-8"
    return (texto or "").encode(como_escribe, "replace").decode(como_escribe)
