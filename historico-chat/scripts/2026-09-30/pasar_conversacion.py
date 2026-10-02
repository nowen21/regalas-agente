"""Pasa la conversación de la sesión al análisis que está prendido.

Lee `historico-chat/.estado/analisis-en-curso.txt`. Si no existe o está vacío,
no hay análisis prendido y no hace nada. Si existe, trae tres líneas:

    analisis=<ruta del análisis, desde la raíz>
    transcripcion=<ruta de la transcripción de la sesión, desde la raíz>
    desde=<primer turno del usuario que le pertenece al análisis>

Copia los turnos desde ese número hasta el último, entre la nota de la sección
«## Conversación» y la línea «> acá termina la conversación». Lo demás del
análisis no se toca.

Es el paso intermedio hacia la herramienta general (punto 29 del análisis 1 y
análisis 2 del pendiente 103): ya no tiene la ruta de un análisis escrita
adentro. Todavía no maneja la pausa.
"""
import re
import sys
import time
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
ESTADO = RAIZ / "historico-chat" / ".estado" / "analisis-en-curso.txt"
FIN = "\n> acá termina la conversación\n"


def leer_estado():
    if not ESTADO.exists():
        return None
    datos = {}
    for linea in ESTADO.read_text(encoding="utf-8").splitlines():
        if "=" in linea:
            clave, valor = linea.split("=", 1)
            datos[clave.strip()] = valor.strip()
    if not {"analisis", "transcripcion", "desde"} <= datos.keys():
        return None
    return RAIZ / datos["analisis"], RAIZ / datos["transcripcion"], int(datos["desde"])


def esperar(transcripcion, segundos=5.0):
    """Espera a que hook_historico.py termine de escribir; corren a la vez."""
    antes = transcripcion.stat().st_mtime
    limite = time.time() + segundos
    while time.time() < limite:
        time.sleep(0.25)
        if transcripcion.stat().st_mtime != antes:
            time.sleep(0.5)
            return


def conversacion(transcripcion, desde, carpeta):
    texto = transcripcion.read_text(encoding="utf-8")
    m = re.search(rf"^### {desde} · Usuario", texto, flags=re.M)
    if not m:
        return ""
    cuerpo = texto[m.start():].rstrip() + "\n"
    # la transcripción separa el turno de su hora con raya larga; el análisis
    # es un documento que sigue 00·ID8, así que ahí va una coma
    cuerpo = re.sub(r"^(### \d+ · Usuario|\*\*Agente\*\*) — ", r"\1, ", cuerpo, flags=re.M)
    # las marcas que la herramienta le pone al mensaje del usuario (texto
    # pegado, archivo abierto en el editor) no son palabras del usuario
    cuerpo = re.sub(r"</?pasted_content[^>]*>", "", cuerpo)
    cuerpo = re.sub(r"<ide_opened_file>.*?</ide_opened_file>", "", cuerpo, flags=re.S)
    cuerpo = re.sub(r"^> *\n(?=> *\n)", "", cuerpo, flags=re.M)
    subir = "../" * len(carpeta.relative_to(RAIZ).parts)

    # los enlaces del chat son relativos a la raíz; el que no existe ahí pero
    # sí junto al análisis se deja como está
    def ajustar(e):
        ruta = e.group(1)
        archivo = ruta.split("#")[0]
        if not (RAIZ / archivo).exists() and (carpeta / archivo).exists():
            return e.group(0)
        return "](" + subir + ruta + ")"

    return re.sub(r"\]\((?!https?:|#|\.\./)([^)]+)\)", ajustar, cuerpo)


def pasar(analisis, transcripcion, desde):
    texto = analisis.read_text(encoding="utf-8")
    inicio = texto.index("## Conversación")
    inicio = texto.index("\n\n", texto.index("\n> ", inicio) + 1) + 2
    fin = texto.rindex(FIN) + 1
    nuevo = texto[:inicio] + conversacion(transcripcion, desde, analisis.parent) + "\n" + texto[fin:]
    if nuevo != texto:
        analisis.write_text(nuevo, encoding="utf-8")


if __name__ == "__main__":
    if "--enganche" in sys.argv:
        sys.stdin.read()
    estado = leer_estado()
    if estado is None:
        sys.exit(0)
    analisis, transcripcion, desde = estado
    try:
        if "--enganche" in sys.argv:
            esperar(transcripcion)
        pasar(analisis, transcripcion, desde)
        # apagar: si el análisis ya tiene la marca de aprobado y la respuesta a
        # ese turno ya entró, se borra el estado para que no entre nada más
        texto = transcripcion.read_text(encoding="utf-8")
        ultimo_usuario = texto.rfind("\n### ")
        if ("> **Aprobado**" in analisis.read_text(encoding="utf-8")
                and texto.find("\n**Agente**", ultimo_usuario) != -1):
            ESTADO.unlink()
    except (OSError, ValueError) as error:
        # un enganche no debe frenar la sesión: avisa y sigue
        print(f"{analisis.name} no se actualizó: {error}", file=sys.stderr)
