"""Cuánto consumió la sesión. **Mide, no detiene**, como `brevedad`.

Suma fichas (tokens) de entrada, de salida y leídas de caché sobre los turnos
de una sesión, para que «esta sesión salió cara» deje de ser una impresión
(`notas/estructura.md`, §3.2 Presupuesto). No corta la sesión ni decide cuánto
es mucho: el límite duro lo pone la herramienta. Con `umbral` avisa; sin él,
solo informa.

**El tramo** (`EP-005·HU-014`). Al cierre el total llega cuando ya se pagó, así
que durante la sesión se avisa **una vez por cada tramo** cruzado. El millón por
defecto salió de medir ocho sesiones reales el 2026-08-20: avisa de cero a doce
veces según el tamaño, y ninguna sesión corta lo cruza. Sin estado compartido:
el cruce se decide comparando el total con y sin el último turno.

Sumar y comparar es agnóstico; **leer** la transcripción de una herramienta
concreta no, y vive en el adaptador.
"""

# Fichas de entrada más salida, sin caché, entre un aviso y el siguiente.
TRAMO = 1_000_000


class Presupuesto:
    """Todo es estático: recibe consumos y devuelve números o texto."""

    TRAMO = TRAMO

    @staticmethod
    def resumen(consumos):
        """Totales de una sesión. `consumos`: `{"entrada", "salida", "cache"}`
        por turno; las llaves que falten cuentan como 0."""
        total = {"turnos": 0, "entrada": 0, "salida": 0, "cache": 0}
        for c in consumos:
            total["turnos"] += 1
            for llave in ("entrada", "salida", "cache"):
                total[llave] += int(c.get(llave, 0) or 0)
        total["total"] = total["entrada"] + total["salida"]
        return total

    @staticmethod
    def excedido(totales, umbral):
        """`True` si el consumo (entrada + salida, sin caché) pasó el umbral."""
        return bool(umbral) and totales["total"] > int(umbral)

    @staticmethod
    def tramo(total, umbral):
        """En qué tramo cae `total`: 0 hasta el primer umbral, 1 hasta el segundo..."""
        return int(total) // int(umbral) if umbral else 0

    @classmethod
    def cruzo_tramo(cls, consumos, umbral=TRAMO):
        """`(cruzó, tramo actual, totales)`: si el último turno cambió de tramo.
        Un umbral de 0 apaga el aviso, y una lista vacía no cruza nada."""
        consumos = list(consumos)
        con = cls.resumen(consumos)
        if not umbral or not consumos:
            return False, 0, con
        sin = cls.resumen(consumos[:-1])
        actual = cls.tramo(con["total"], umbral)
        return actual > cls.tramo(sin["total"], umbral), actual, con

    @staticmethod
    def aviso_de_tramo(totales, numero, umbral=TRAMO):
        """El aviso de mitad de sesión: qué tramo se cruzó y cuánto va."""
        return ("[LA SESIÓN CRUZÓ EL TRAMO %d DE CONSUMO]\n"
                "Lleva %s fichas de entrada y salida (sin caché), en %d turno(s); "
                "cada tramo son %s. No detiene nada: es para decidir si se sigue, "
                "se compacta o se cierra." % (
                    numero, f"{totales['total']:,}", totales["turnos"], f"{int(umbral):,}"))

    @staticmethod
    def pasados_del_limite(piezas, limite):
        """`EP-025·HU-009` · `[(nombre, mayor estimación, veces)]` de lo que pasó `limite`.

        `piezas`: `(nombre, tokens)` de cada enganche o archivo del turno. Un
        nombre que pasa varias veces sale una, con su mayor estimación. Justo en
        el límite no pasa.
        """
        pasados = {}
        for nombre, tokens in piezas:
            if tokens > limite:
                mayor, veces = pasados.get(nombre, (0, 0))
                pasados[nombre] = (max(mayor, tokens), veces + 1)
        return sorted(((n, m, v) for n, (m, v) in pasados.items()), key=lambda fila: -fila[1])

    @staticmethod
    def aviso_de_limites(enganches, archivos, limite_enganche, limite_archivo):
        """El aviso del turno anterior, o "" si nada pasó su límite."""
        if not enganches and not archivos:
            return ""

        from ..consumo.formato import miles

        def veces(n):
            return f" ({n} veces)" if n > 1 else ""

        lineas = ["[EN EL TURNO ANTERIOR, ALGO PASÓ SU LÍMITE DE TOKENS]"]
        lineas += [f"- El enganche «{nombre}» agregó unos {miles(tokens)} tokens{veces(n)}; "
                   f"el límite del proyecto es {miles(limite_enganche)}." for nombre, tokens, n in enganches]
        lineas += [f"- Leer «{ruta}» ocupó unos {miles(tokens)} tokens{veces(n)}; "
                   f"el límite del proyecto es {miles(limite_archivo)}." for ruta, tokens, n in archivos]
        lineas.append("Son estimaciones. No detiene nada: es para decidir si se achica, se parte "
                      "o se pasa a un programa. Los límites se cambian en Cimiento, en «Proyectos».")
        return "\n".join(lineas)

    @classmethod
    def como_texto(cls, totales, umbral=0):
        """El resumen en una línea legible, con el aviso si el umbral se pasó."""
        linea = ("Consumo de la sesión: %d turno(s) · %s fichas de entrada · "
                 "%s de salida · %s leídas de caché" % (
                     totales["turnos"], f"{totales['entrada']:,}",
                     f"{totales['salida']:,}", f"{totales['cache']:,}"))
        if cls.excedido(totales, umbral):
            linea += ("\nAVISO: el consumo (%s) pasó el umbral (%s). No detiene "
                      "nada: es un número para mirar." % (f"{totales['total']:,}", f"{int(umbral):,}"))
        return linea


def aviso_de_limites(ruta, raiz, estandar=None):
    """`EP-025·HU-009` · Lo que en el turno anterior pasó el límite del proyecto, o "".

    Vivía en `hook_presupuesto.py`; pasó a `core/` con la `EP-025·HU-013`
    (análisis 2 del pendiente 119, punto 6), y lee los límites de los ajustes.
    """
    from ..consumo.lector import LectorDeClaudeCode, estimar_tokens
    from .niveles import LimitesDelProyecto

    turno = LectorDeClaudeCode(ruta).turno_anterior()
    limite_enganche, limite_archivo = LimitesDelProyecto(raiz, estandar).limites()
    enganches = Presupuesto.pasados_del_limite(
        ((e.nombre, estimar_tokens(e.caracteres)) for e in turno.enganches), limite_enganche)
    archivos = Presupuesto.pasados_del_limite(
        ((a.ruta, estimar_tokens(a.caracteres)) for a in turno.archivos), limite_archivo)
    return Presupuesto.aviso_de_limites(enganches, archivos, limite_enganche, limite_archivo)
