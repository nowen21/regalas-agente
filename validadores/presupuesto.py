# -*- coding: utf-8 -*-
"""Cuánto consumió la sesión. **Mide, no detiene** — como `brevedad`.

**Qué mide.** Fichas (tokens) de entrada, de salida y leídas de caché, sumadas
sobre los turnos de una sesión. El número existe para que «esta sesión salió
cara» deje de ser una impresión: viene de la brecha que el análisis contra
`notas/estructura.md` (§3.2 Presupuesto) dejó escrita — sin visibilidad del
gasto, cada sesión es una factura sorpresa.

**Qué no hace.** No corta la sesión ni decide cuánto es mucho: el límite duro
lo pone la herramienta. Con `umbral` avisa; sin él, solo informa.

**El tramo** (`EP-005 · HU-014`). Al cierre el total llega cuando ya se pagó.
Durante la sesión se avisa **una vez por cada tramo** que el consumo cruza,
y el tramo por defecto salió de medir ocho sesiones reales el 2026-08-20
(de 144 mil a 12,7 millones de fichas sin caché): un millón avisa de cero a
doce veces según el tamaño, y ninguna sesión corta lo cruza. Sin estado
compartido: el cruce se decide comparando el total con y sin el último turno.

**Por qué acá y no en el adaptador.** Sumar y comparar es agnóstico; **leer**
la transcripción de una herramienta concreta no. La lectura vive en
`adaptadores/claude-code/hook_presupuesto.py`; esto sirve con cualquiera.
"""
import comun

# Fichas de entrada más salida, sin caché, entre un aviso y el siguiente.
TRAMO = 1_000_000


def resumen(consumos):
    """Totales de una sesión.

    `consumos`: iterable de `{"entrada": int, "salida": int, "cache": int}`,
    uno por turno. Las llaves que falten cuentan como 0.
    """
    total = {"turnos": 0, "entrada": 0, "salida": 0, "cache": 0}
    for c in consumos:
        total["turnos"] += 1
        for llave in ("entrada", "salida", "cache"):
            total[llave] += int(c.get(llave, 0) or 0)
    total["total"] = total["entrada"] + total["salida"]
    return total


def excedido(totales, umbral):
    """True si el consumo (entrada + salida, sin caché) pasó el umbral."""
    return bool(umbral) and totales["total"] > int(umbral)


def tramo(total, umbral):
    """En qué tramo cae `total`: 0 hasta el primer umbral, 1 hasta el segundo..."""
    return int(total) // int(umbral) if umbral else 0


def cruzo_tramo(consumos, umbral=TRAMO):
    """`(cruzó, tramo actual, totales)`: si el último turno cambió de tramo.

    Se compara el total con el último turno contra el total sin él. Un umbral
    de 0 apaga el aviso, y una lista vacía no cruza nada.
    """
    consumos = list(consumos)
    con = resumen(consumos)
    if not umbral or not consumos:
        return False, 0, con
    sin = resumen(consumos[:-1])
    actual = tramo(con["total"], umbral)
    return actual > tramo(sin["total"], umbral), actual, con


def aviso_de_tramo(totales, numero, umbral=TRAMO):
    """El aviso de mitad de sesión: qué tramo se cruzó y cuánto va."""
    return ("[LA SESIÓN CRUZÓ EL TRAMO %d DE CONSUMO]\n"
            "Lleva %s fichas de entrada y salida (sin caché), en %d turno(s); "
            "cada tramo son %s. No detiene nada: es para decidir si se sigue, "
            "se compacta o se cierra." % (
                numero, f"{totales['total']:,}", totales["turnos"],
                f"{int(umbral):,}"))


def como_texto(totales, umbral=0):
    """El resumen en una línea legible, con el aviso si el umbral se pasó."""
    linea = ("Consumo de la sesión: %d turno(s) · %s fichas de entrada · "
             "%s de salida · %s leídas de caché" % (
                 totales["turnos"], f"{totales['entrada']:,}",
                 f"{totales['salida']:,}", f"{totales['cache']:,}"))
    if excedido(totales, umbral):
        linea += ("\nAVISO: el consumo (%s) pasó el umbral (%s). No detiene "
                  "nada: es un número para mirar." % (
                      f"{totales['total']:,}", f"{int(umbral):,}"))
    return linea


if __name__ == "__main__":
    comun.no_es_punto_de_entrada("presupuesto")
