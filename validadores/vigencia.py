# -*- coding: utf-8 -*-
"""`EP-001·HU-007·CA-04` · Qué reglas llevan más tiempo sin que nadie las mire.

**Una regla equivocada se comporta exactamente igual que una correcta.** No se
rompe nada: sigue ahí, sigue pasando su checklist de forma, y el agente la
sigue obedeciendo. Mientras tanto cambia la herramienta que nombraba, cambia la
práctica que daba por buena, o el problema que venía a evitar deja de ocurrir.

**El sello que ya trae cada regla no cubre esto.** Dice *«vale mientras el
texto de arriba no cambie»*: protege contra que cambie **la regla**, no contra
que cambie **el mundo**.

## Dos fechas distintas, y confundirlas era el defecto

| Fecha | Qué dice | Quién la pone |
|---|---|---|
| La del sello | Se le aplicó el molde: título, ejemplo, una sola exigencia | Quien escribe la regla |
| **La de vigencia** | Alguien volvió a preguntarse si la regla sigue sirviendo | Quien la revisa |

Una regla puede tener el sello de ayer y llevar un año sin que nadie se
pregunte si todavía hace falta.

## Por qué no hay umbral

**Un umbral inventado produce una alarma que se aprende a ignorar**, y ese es
el defecto más caro de este repositorio. Acá se ordena y se muestra; cada
cuánto conviene revisar se decide **después de mirar la lista**, no antes.

Por eso `validar()` **nunca falla**: informa.

## Sin fecha de vigencia se ordena por la del sello, no por la de `git`

**El primer intento ordenó por el último commit que tocó el archivo, y salió
inservible:** la limpieza tipográfica del mismo día había tocado las 245
reglas, así que todas parecían recién escritas. Una fecha que se mueve cuando
se cambia una raya por un guion no mide cuándo alguien miró la regla.

**La fecha del sello sí lo mide**, y ya estaba escrita en todas: es el día que
alguien se sentó a revisar esa regla contra el molde. No es lo mismo que
revisarla contra la realidad —por eso este módulo existe—, pero es la última
vez que un humano la leyó entera, y eso es exactamente lo que hace falta para
ordenar la fila.
"""
import os
import re

import comun
from comun import AVISO, Hallazgo, RAIZ, Hallazgo as _H, relativo

# La línea que se agrega al sello cuando alguien revisa la regla de fondo.
# **Es opcional y arranca ausente en todas**: agregar doscientas líneas a mano
# habría sido el trabajo, no el resultado. Lo que la lista muestra desde el
# primer día es cuáles no la tienen.
_VIGENCIA = re.compile(r"(?m)^>?\s*Revisada contra la realidad el (\d{4}-\d{2}-\d{2})")

_SELLO_FECHA = re.compile(r"Aplicado el \[checklist.*?el \*\*(\d{4}-\d{2}-\d{2})\*\*")

MOLDE = "> Revisada contra la realidad el AAAA-MM-DD."


def revisada(regla):
    """`AAAA-MM-DD` de la última revisión de fondo, o `""` si nunca."""
    m = _VIGENCIA.search(regla.texto or "")
    return m.group(1) if m else ""


def fecha_del_sello(regla):
    """`AAAA-MM-DD` del día que se le aplicó el checklist, o `""`."""
    m = _SELLO_FECHA.search(regla.texto or "")
    return m.group(1) if m else ""


def _hallazgos_por_regla(raiz):
    """`{id: cuántos}` incumplimientos que hoy produce cada regla.

    **Una regla vieja que falla todo el tiempo se revisa primero.** Y una
    regla vieja que no ha fallado nunca hay que mirarla por el motivo
    contrario: puede que ya nadie la esté aplicando.
    """
    import metareglas
    cuenta = {}
    for h in metareglas.validar(raiz):
        for m in re.finditer(r"`([A-Z]{1,3}\d+(?:\.\d+)?)`", h.mensaje):
            cuenta[m.group(1)] = cuenta.get(m.group(1), 0) + 1
    return cuenta


def listado(raiz=None):
    """`[(regla, revisada, fecha del sello, hallazgos)]`, de la más vieja a la más nueva.

    Ordena por la fecha de vigencia si la hay, y si no por la del sello:
    las que **nunca** se revisaron encabezan la lista, que es donde tienen que
    estar.
    """
    raiz = raiz or RAIZ
    import metareglas
    fallas = _hallazgos_por_regla(raiz)
    salida = []
    for regla in metareglas.reglas(raiz):
        salida.append((regla, revisada(regla),
                       fecha_del_sello(regla),
                       fallas.get(regla.id, 0)))
    # Sin fecha de vigencia va primero; entre las que no la tienen, la del
    # sello más viejo. Un `""` ordena antes que cualquier fecha, que es
    # justamente lo que se quiere.
    return sorted(salida, key=lambda x: (x[1] or "", x[2] or ""))


def validar(raiz=None):
    """Un aviso por las reglas que nadie ha revisado de fondo. **Nunca falla.**

    Se emite **uno solo**, no uno por regla: doscientos avisos idénticos
    entierran los hallazgos que sí piden acción, y el hábito de saltárselos se
    lleva por delante a los demás.
    """
    datos = listado(raiz)
    sin_revisar = [d for d in datos if not d[1]]
    if not sin_revisar:
        return []
    viejas = ", ".join("`%s`" % d[0].id for d in sin_revisar[:5])
    return [Hallazgo(
        AVISO, os.path.join(raiz or RAIZ, "base"), 0,
        f"{len(sin_revisar)} de {len(datos)} reglas no dicen cuándo se "
        f"revisó **si siguen sirviendo** — el sello responde por la forma, no "
        f"por si el problema que evitan todavía existe. Las del "
        f"sello más antiguo: {viejas}. La lista completa: "
        f"`python validadores/vigencia.py`")]


def linea_resumen(raiz=None):
    """Cuántas tienen fecha de vigencia y cuántas no."""
    datos = listado(raiz)
    con = len([d for d in datos if d[1]])
    return "Reglas revisadas contra la realidad: %d de %d" % (con, len(datos))


def main():
    import argparse
    comun.preparar_salida()
    p = argparse.ArgumentParser(
        description="Lista las reglas por cuánto llevan sin que nadie se "
                    "pregunte si siguen sirviendo. No hay umbral: se mira la "
                    "lista y después se decide cada cuánto revisar.")
    p.add_argument("--raiz", default=RAIZ)
    p.add_argument("--cuantas", type=int, default=25,
                   help="cuántas reglas listar, de la más vieja a la más nueva")
    a = p.parse_args()

    datos = listado(a.raiz)
    sin = len([d for d in datos if not d[1]])
    print("== Vigencia de las reglas ==\n")
    print("%d reglas · %d sin revisar de fondo · %d con fecha\n"
          % (len(datos), sin, len(datos) - sin))
    print("Las tres preguntas de la revisión están en "
          "`base/20-meta-reglas/revision-de-vigencia.md`.\n")
    print("%-8s %-12s %-12s %s" % ("REGLA", "REVISADA", "SELLO DE", "FALLA HOY"))
    for regla, rev, sello, fallas in datos[:a.cuantas]:
        print("%-8s %-12s %-12s %s" % (regla.id, rev or "nunca",
                                       sello or "sin sello",
                                       fallas if fallas else ""))
    if len(datos) > a.cuantas:
        print("\n... y %d más. Se listan con --cuantas."
              % (len(datos) - a.cuantas))
    print("\nQuien revise una regla le agrega esta línea a su sello:")
    print("  %s" % MOLDE)
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
