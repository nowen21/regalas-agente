# -*- coding: utf-8 -*-
"""Qué reglas vigentes se parecen a la que se va a escribir.

**Es lo que la ficha de `F-005` llama lo difícil:** *«escribir la regla es lo
fácil; lo que cuesta es que no repita ni contradiga a otra»*. Con 248 reglas
vigentes, nadie las tiene todas en la cabeza.

**Y hay que decir qué NO hace esto.** No detecta contradicciones: dos reglas se
contradicen por lo que significan, y eso no se saca contando palabras. Lo que
hace es **poner al lado las que hablan de lo mismo**, para que quien escribe las
mire antes de guardar. La decisión sigue siendo de una persona.

Llamarlo «detector de contradicciones» sería peor que no tenerlo: quien confía
en un detector deja de mirar, y las que se le escapan pasan sin que nadie las
revise.
"""
import re
import unicodedata

from . import catalogo

# Palabras que aparecen en todas las reglas y no distinguen ninguna. Sin
# quitarlas, todo se parece a todo.
VACIAS = frozenset(u"""
a al ante antes cada como con contra cuando de del desde donde dos e el ella
ello en entre es esa ese eso esta este esto hasta la las le les lo los mas me
mi ni no nunca o para pero por porque que quien se segun ser si sin sobre solo
son su sus te tiene toda todas todo todos tras un una uno y ya
regla reglas debe puede hace hacer queda quedar deja dejar dice decir va van
""".split())

# Cuántas palabras significativas tienen que compartir para que valga la pena
# mirarlas. Con menos, la lista se llena de coincidencias sin sentido.
MINIMO_EN_COMUN = 2


def _palabras(texto):
    plano = unicodedata.normalize("NFKD", (texto or "").lower())
    plano = u"".join(c for c in plano if not unicodedata.combining(c))
    return set(p for p in re.findall(u"[a-z]{3,}", plano) if p not in VACIAS)


def parecidas_a(raiz, titulo, prefijo="", cuantas=5):
    """Las reglas vigentes que más palabras comparten con ese título.

    Devuelve `[(regla, en_comun)]`, de más a menos. **Las del mismo capítulo
    pesan más**: dos reglas del mismo capítulo que hablan de lo mismo son el
    caso que de verdad hay que mirar.
    """
    del_titulo = _palabras(titulo)
    if not del_titulo:
        return []

    puntuadas = []
    for una in catalogo.vigentes(raiz):
        comunes = del_titulo & _palabras(una.titulo)
        if len(comunes) < MINIMO_EN_COMUN:
            continue
        peso = len(comunes) + (1 if prefijo and una.prefijo == prefijo else 0)
        puntuadas.append((peso, una, sorted(comunes)))

    puntuadas.sort(key=lambda uno: (-uno[0], uno[1].id))
    return [(una, comunes) for _, una, comunes in puntuadas[:cuantas]]


def aviso(encontradas):
    """La frase que acompaña la lista, con lo que esto no puede decir."""
    if not encontradas:
        return (u"Ninguna regla vigente se parece por sus palabras. **No quiere "
                u"decir que no haya una que la contradiga:** contar palabras no "
                u"encuentra contradicciones.")
    return (u"Estas %d hablan de lo mismo. **Míralas antes de guardar:** esto "
            u"no dice si se contradicen, solo que se parecen."
            % len(encontradas))
