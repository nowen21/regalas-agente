# -*- coding: utf-8 -*-
"""Escribe en cada regla del capitulo 00 quien la hace cumplir.

Es la tarea T-12 de la fase `A-EP-005-HU-012`. **No decide nada**: el texto de
cada declaracion esta escrito abajo, una por regla, y el guion solo lo pone en
el sitio que el molde fijo — despues del ejemplo y antes del checklist.

Se hizo con un guion y no a mano por una razon medida: dieciocho reglas
repartidas en diez archivos, con la misma linea en el mismo sitio, es donde una
edicion a mano deja una distinta de las otras sin que nadie lo note.

Es idempotente: la regla que ya tiene su declaracion no se toca.
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

NUCLEO = os.path.join(RAIZ, "base", "00-nucleo-blindado.md")
REGLAS = os.path.join(RAIZ, "base", "00-identidad-y-rol", "reglas")

Q = u"**Quién la hace cumplir:** "
N = u"**Nadie la hace cumplir:** "

DECLARACIONES = {
 "N1": N + u"ningún programa ve si el usuario aprobó: la aprobación ocurre "
       u"en el chat y no queda en ningún archivo. Lo construido es el anexo de "
       u"acciones y `validadores/acciones.py`, que dice **cuál** acción exige "
       u"aprobación propia; que se haya pedido, no.",
 "N2": N + u"un programa no distingue el commit que el usuario pidió del que el "
       u"agente hizo por su cuenta. Los dos se ven igual en el repositorio, y el "
       u"pedido vive en el chat.",
 "N3": N + u"reconocer que algo se rompió **para pasar un obstáculo** exige "
       u"entender qué se buscaba con el cambio. Un programa ve la prueba "
       u"desactivada; no ve si fue para salir del paso.",
 "N4": N + u"los datos reales viven fuera del repositorio, y la operación "
       u"destructiva pasa donde ningún validador la ve. Lo comprobable es lo que "
       u"queda escrito después, no la autorización de antes.",
 "N5": N + u"la previsualización ocurre **en la operación**, no en un archivo. "
       u"Un programa podría contar que el código tenga la palabra, y eso no dice "
       u"si de verdad se previsualizó antes de aplicar.",
 "N6": Q + u"`validadores/enmascarar.py`, que tapa la clave antes de que la "
       u"transcripción la guarde, y corre solo en cada turno; y "
       u"`validadores/secretos.py`, que caza la credencial incrustada en el "
       u"código cuando se le pide.",
 "N7": Q + u"`validadores/respaldo.py`, que hace la copia antes de la operación "
       u"y la detiene si no se puede. **Su límite va escrito en su propia "
       u"salida:** un borrado a mano o por interfaz no lo ve nadie.",
 "N8": N + u"lo que sale del proyecto sale por una herramienta de red, y no deja "
       u"rastro en el repositorio. Lo único que un programa alcanza a ver es lo "
       u"que **entra**, y eso ya lo marca `validadores/externo.py` para `01·C27`.",
 "N9": N + u"reconocer que un intento es el mismo que el usuario rechazó, dicho "
       u"de otra forma, es leer. Comparar cadenas daría por reintento cualquier "
       u"trabajo parecido, y dejaría pasar el mismo con otras palabras.",
 "ID1": N + u"qué cuenta como criterio de desarrollador con experiencia lo "
        u"discute una persona. Lo que un programa ve son los resultados sueltos "
        u"(una prueba, un enlace roto), y ninguno de ellos es la postura.",
 "ID3": N + u"**en conjunto**, que es lo que la regla exige. Sus cuatro "
        u"condiciones sí se validan por separado (la suite, el plan contra lo "
        u"hecho, la documentación del cierre); lo que ningún programa junta es "
        u"decidir si el trabajo está terminado.",
 "ID4": N + u"que el agente haya recorrido el ciclo entero se ve en lo que "
        u"entregó, y cada tramo tiene su propia regla con su propio validador. "
        u"El ciclo completo como exigencia única no lo cuenta ninguno.",
 "ID5": N + u"el borde del rol se cruza en lo que el agente **dice**, no en un "
        u"archivo. Un programa que buscara palabras se saltaría el caso real: "
        u"opinar de lo que no le toca con el vocabulario correcto.",
 "ID6": N + u"qué rol pide la etapa es una lectura de la etapa. Un programa que "
        u"lo dedujera del nombre de la fase estaría inventando criterio, y "
        u"acertaría justo en los casos en que no hacía falta.",
 "ID7": N + u"que un texto se entienda sin saber del tema lo decide quien no "
        u"sabe del tema. Contar palabras raras daría por clara una explicación "
        u"sencilla y equivocada.",
 "ID8": Q + u"`validadores/marcas.py`, que el enganche `.githooks/pre-commit` "
        u"corre como trinquete: rechaza el commit que **suma** marcas nuevas. Y "
        u"`adaptadores/claude-code/hook_redaccion.py`, que las cuenta sobre lo "
        u"que el agente acaba de escribir.",
 "ID9": Q + u"`validadores/brevedad.py`, que mide cuánto ocupa cada respuesta, "
        u"y `adaptadores/claude-code/hook_redaccion.py`, que lo dice al cerrar el "
        u"turno. **Mide y no detiene:** cuando el enganche corre, el texto ya "
        u"salió.",
 "ID10": Q + u"`validadores/redaccion.py`, que cuenta el trato directo sobre lo "
         u"que el agente acaba de escribir, y "
         u"`adaptadores/claude-code/hook_redaccion.py`, que lo deja a la vista al "
         u"cerrar el turno. La variedad del idioma no se cuenta: se lee.",
}


def _archivo_de(rid):
    if rid.startswith("N"):
        return NUCLEO
    for n in os.listdir(REGLAS):
        if n.startswith(rid + "-"):
            return os.path.join(REGLAS, n)
    raise ValueError("no se encontro el archivo de %s" % rid)


def _poner(texto, rid, declaracion):
    """El texto con la declaracion puesta, o el mismo texto si ya estaba."""
    cabeza = re.search(r"(?m)^##\s+%s\s+·" % re.escape(rid), texto)
    if not cabeza:
        raise ValueError("no se encontro el encabezado de %s" % rid)
    siguiente = re.search(r"(?m)^##\s+[A-Z]", texto[cabeza.end():])
    fin = cabeza.end() + (siguiente.start() if siguiente else
                          len(texto) - cabeza.end())
    tramo = texto[cabeza.start():fin]

    if u"la hace cumplir:**" in tramo:
        return texto, False

    checklist = re.search(r"(?m)^###\s+Checklist", tramo)
    if not checklist:
        raise ValueError("%s no tiene checklist: no se sabe donde poner" % rid)
    raya = None
    for m in re.finditer(r"(?m)^---\s*$", tramo[:checklist.start()]):
        raya = m
    if not raya:
        raise ValueError("%s no tiene la raya antes del checklist" % rid)

    nuevo = (tramo[:raya.start()] + declaracion + u"\n\n" + tramo[raya.start():])
    return texto[:cabeza.start()] + nuevo + texto[fin:], True


def main():
    puestas, ya = 0, 0
    for rid in sorted(DECLARACIONES, key=lambda r: (r[0], len(r), r)):
        ruta = _archivo_de(rid)
        with io.open(ruta, encoding="utf-8") as f:
            texto = f.read()
        texto, cambio = _poner(texto, rid, DECLARACIONES[rid])
        if cambio:
            with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
                f.write(texto)
            puestas += 1
            print("  %-5s %s" % (rid, os.path.relpath(ruta, RAIZ)))
        else:
            ya += 1
    print("\n%d declaraciones puestas, %d ya estaban." % (puestas, ya))
    return 0


if __name__ == "__main__":
    sys.exit(main())
