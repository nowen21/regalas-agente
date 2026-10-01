"""Mantiene al día el análisis 1 del pendiente 103 con la conversación del 2026-09-30.

Copia los turnos de la transcripción del día dentro de analisis-1.md, entre el
encabezado y la línea «acá es donde continua el primer análisis». Lo que va de
esa línea hacia abajo (conclusiones, lecciones, lo que se tiene que hacer) lo
escribe el usuario y no se toca.

Corre solo después de cada mensaje y de cada respuesta (enganche en
.claude/settings.json), para que el análisis quede en tiempo real. Espera a que
hook_historico.py termine de escribir la transcripción, porque los dos corren a
la vez.
"""
import re
import sys
import time
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
ORIGEN = RAIZ / "pendientes" / "103-cada-documento-de-la-cadena-sale-del-anterior.md"
TRANSCRIPCION = RAIZ / "historico-chat" / "2026-09-30-sesion.md"
DESTINO = RAIZ / "historico-chat" / "resumenes" / "2026-09-30" / ORIGEN.stem
ANALISIS = DESTINO / "analisis-1.md"
SUBIR = "../../../../"
PRIMER_TURNO = "### 2 · Usuario"
MARCA = "> acá es donde continua el primer análisis"


def esperar_transcripcion(segundos=5.0):
    """Espera a que la transcripción cambie y quede quieta, o hasta el límite."""
    if not TRANSCRIPCION.exists():
        return
    antes = TRANSCRIPCION.stat().st_mtime
    limite = time.time() + segundos
    while time.time() < limite:
        time.sleep(0.25)
        if TRANSCRIPCION.stat().st_mtime != antes:
            time.sleep(0.5)
            return


def conversacion():
    trans = TRANSCRIPCION.read_text(encoding="utf-8")
    cuerpo = trans[trans.index(PRIMER_TURNO):].rstrip() + "\n"
    # los enlaces del chat son relativos a la raíz del repositorio; el que no
    # existe ahí pero sí junto al análisis se deja como está
    def ajustar(m):
        ruta = m.group(1)
        archivo = ruta.split("#")[0]
        if not (RAIZ / archivo).exists() and (DESTINO / archivo).exists():
            return m.group(0)
        return "](" + SUBIR + ruta + ")"
    return re.sub(r"\]\((?!https?:|#|\.\./)([^)]+)\)", ajustar, cuerpo)


def sincronizar():
    texto = ANALISIS.read_text(encoding="utf-8")
    inicio = texto.index(PRIMER_TURNO)
    # la última: la conversación también puede citar la línea de la marca
    fin = texto.rindex("\n" + MARCA + "\n") + 1
    nuevo = texto[:inicio] + conversacion() + "\n" + texto[fin:]
    if nuevo != texto:
        ANALISIS.write_text(nuevo, encoding="utf-8")


if __name__ == "__main__":
    if "--enganche" in sys.argv:
        sys.stdin.read()
        esperar_transcripcion()
    try:
        sincronizar()
    except (OSError, ValueError) as error:
        # un enganche no debe frenar la sesión: avisa y sigue
        print(f"analisis-1.md no se actualizó: {error}", file=sys.stderr)
