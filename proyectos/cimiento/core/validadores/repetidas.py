"""`07·Q4` · No repetir lógica: avisa la función que hace lo mismo que otra.

**Compara lo que hace, no cómo se llama** (análisis 1 del pendiente 116,
acuerdo 4). Cada cuerpo se normaliza antes de comparar: sin comentarios, cada
texto entre comillas vale lo mismo, cada número también, y cada nombre propio se
cambia por su orden de aparición. Así `_leer(ruta)` y `leer_archivo(camino)`
escritas igual salen iguales, y dos `validar()` que hacen cosas distintas no.

**Avisa y no frena** (acuerdo 4): `Q4` misma dice que duplicar una vez y esperar
el patrón es válido. Decidir si es el mismo concepto es de quien escribe.

El umbral y el tamaño mínimo se midieron sobre Cimiento y agro-system el
2026-10-04 (fase `A-EP-004-HU-026`): ver `UMBRAL` y `MINIMO`.
"""
import os
import re
from collections import Counter, defaultdict

from ..comun import AVISO, Git, Hallazgo
from .codigo import Funciones, RecorridoDeCodigo, ValidadorDeCodigo

_COMENTARIO = re.compile(r"#[^\n]*|//[^\n]*|/\*.*?\*/", re.S)
_TEXTO = re.compile(r"\"\"\".*?\"\"\"|'''.*?'''|\"(?:\\.|[^\"\\\n])*\"|'(?:\\.|[^'\\\n])*'", re.S)
_FICHA = re.compile(r"[A-Za-z_$]\w*|\d+(?:\.\d+)?|\S")

# Palabras del lenguaje: se conservan, porque dicen qué hace la función.
_RESERVADAS = frozenset("""
    and as assert async await break class continue def del elif else except finally for from global if
    import in is lambda nonlocal not or pass raise return try while with yield None True False self
    function var let const new this null true false echo array foreach switch case default do throw
    catch instanceof public private protected static void typeof undefined isset empty unset list
""".split())

# Medidos el 2026-10-04 sobre Cimiento (555 funciones) y agro-system (3.910):
# con 0,90 se pierde `raiz_pedida`, el caso del pendiente 117, cuyas copias
# difieren en un renglón (83 %); entre 0,80 y 0,90 lo demás también son copias
# casi exactas, y bajo 0,80 aparecen funciones que solo comparten la forma. Con
# menos de 40 fichas, las de una o dos líneas salen iguales sin ser la misma lógica.
UMBRAL = 0.80
MINIMO = 40
TEJA = 5
# Un trozo que aparece en muchas funciones es forma del lenguaje, no lógica
# propia: no sirve para encontrar copias y vuelve lenta la búsqueda.
COMUN = 40


class Firma:
    """El cuerpo de una función reducido a lo que hace."""

    def __init__(self, donde, nombre, linea, cuerpo):
        self.donde, self.nombre, self.linea = donde, nombre, linea
        self.fichas = self.normalizar(cuerpo)
        self._tejas = None

    @staticmethod
    def normalizar(cuerpo):
        cuerpo = _TEXTO.sub(" S ", _COMENTARIO.sub(" ", cuerpo))
        nombres, salida = {}, []
        for f in _FICHA.findall(cuerpo):
            if f[0].isdigit():
                salida.append("N")
            elif (f[0].isalpha() or f[0] in "_$") and f not in _RESERVADAS and f != "S":
                salida.append("v%d" % nombres.setdefault(f, len(nombres)))
            else:
                salida.append(f)
        return tuple(salida)

    @property
    def tejas(self):
        """Los trozos de `TEJA` fichas seguidas: dos funciones que hacen lo mismo
        comparten casi todos los suyos."""
        if self._tejas is None:
            self._tejas = {hash(self.fichas[i:i + TEJA]) for i in range(max(len(self.fichas) - TEJA + 1, 1))}
        return self._tejas

    def parecido(self, otra):
        """De 0 a 1: los trozos que comparten sobre todos los que tienen las dos."""
        if self.fichas == otra.fichas:
            return 1.0
        comunes = len(self.tejas & otra.tejas)
        return comunes / float(len(self.tejas | otra.tejas) or 1)

    def __str__(self):
        return "`%s` (%s:%d)" % (self.nombre or "función anónima", self.donde, self.linea)


class FuncionesRepetidas(ValidadorDeCodigo):
    """Avisa cada par de funciones que hacen lo mismo. Con `solo_preparados`, solo
    las nuevas del commit que repiten una que ya estaba."""

    nombre = "repetidas"
    regla = "07·Q4"
    descripcion = "funciones que repiten lo que hace otra"

    def __init__(self, proyecto, archivos=None, solo_preparados=False):
        super().__init__(proyecto, archivos)
        self.solo_preparados = solo_preparados

    def firmas(self, textos):
        """`[Firma]` de las funciones con tamaño suficiente, de `[(donde, texto)]`."""
        salida = []
        for donde, texto in textos:
            for nombre, linea, cuerpo, _ in Funciones.de(texto):
                firma = Firma(donde, nombre, linea, cuerpo)
                if len(firma.fichas) >= MINIMO:
                    salida.append(firma)
        return salida

    def validar(self):
        textos = list(RecorridoDeCodigo(self.proyecto, self.archivos).archivos())
        if self.solo_preparados:
            return self._preparados(textos)
        return self.comparar(self.firmas(textos))

    def comparar(self, firmas, nuevas=None):
        """Los avisos de los pares sobre el umbral. Con `nuevas`, solo los pares en
        que una es nueva y la otra no.

        No se compara cada par: un índice de trozos da los candidatos, y solo a
        esos se les mide el parecido."""
        indice = defaultdict(list)
        for i, f in enumerate(firmas):
            for teja in f.tejas:
                indice[teja].append(i)
        compartidas = Counter()
        for miembros in indice.values():
            if 1 < len(miembros) <= COMUN:
                for x in range(len(miembros)):
                    for y in range(x + 1, len(miembros)):
                        compartidas[(miembros[x], miembros[y])] += 1
        pares = []
        for (i, j), n in compartidas.items():
            a, b = firmas[i], firmas[j]
            if n < UMBRAL * min(len(a.tejas), len(b.tejas)):
                continue
            if nuevas is not None and (id(a) in nuevas) == (id(b) in nuevas):
                continue
            p = a.parecido(b)
            if p >= UMBRAL:
                pares.append((i, j, p))
        return self._agrupar(firmas, pares, nuevas)

    def _agrupar(self, firmas, pares, nuevas):
        """Un aviso por copia, no por par: ocho copias de lo mismo son siete avisos
        que nombran la primera, no veintiocho."""
        grupo = list(range(len(firmas)))

        def raiz(x):
            while grupo[x] != x:
                grupo[x] = grupo[grupo[x]]
                x = grupo[x]
            return x

        mejor = {}
        for i, j, p in pares:
            grupo[raiz(i)] = raiz(j)
            for k in (i, j):
                mejor[k] = max(mejor.get(k, 0.0), p)
        miembros = defaultdict(list)
        for k in mejor:
            miembros[raiz(k)].append(k)
        hallazgos = []
        for indices in miembros.values():
            orden = sorted(indices, key=lambda k: (id(firmas[k]) in (nuevas or ()), firmas[k].donde, firmas[k].linea))
            primera = firmas[orden[0]]
            for k in orden[1:]:
                if nuevas is None or id(firmas[k]) in nuevas:
                    hallazgos.append(self._aviso(firmas[k], primera, mejor[k], len(orden) - 1))
        return sorted(hallazgos, key=lambda h: (h.archivo, h.linea))

    def _preparados(self, textos):
        """Las funciones del commit que no estaban en `HEAD`, contra todas las demás."""
        firmas = self.firmas(textos)
        nuevas = set()
        for repo in self.proyecto.repositorios():
            git, prefijo = Git(repo), self.proyecto.prefijo_de(repo)
            for relativa in git.preparados():
                donde = prefijo + relativa
                if not RecorridoDeCodigo(self.proyecto).es_codigo(relativa):
                    continue
                antes = {f.fichas for f in self.firmas([(donde, git.correr("show", "HEAD:" + relativa))])}
                nuevas |= {id(f) for f in firmas if f.donde == donde and f.fichas not in antes}
        return self.comparar(firmas, nuevas) if nuevas else []

    def _aviso(self, copia, primera, parecido, copias):
        otras = " y %d copia(s) más" % (copias - 1) if copias > 1 else ""
        return Hallazgo(AVISO, self.proyecto.ruta(copia.donde) if not os.path.isabs(copia.donde) else copia.donde,
                        copia.linea, "la función %s hace lo mismo que %s%s (parecido %d %%) — %s: si es la misma "
                        "lógica, que viva en un solo lugar" % (copia, primera, otras, round(parecido * 100), self.regla),
                        regla=self.regla)
