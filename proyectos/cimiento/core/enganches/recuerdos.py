"""Los recuerdos del agente viven en el repositorio, no en la herramienta (`01·C19`).

Claude Code guarda lo que el agente debe recordar en una carpeta propia, fuera
del proyecto (`~/.claude/projects/<ruta-con-guiones>/memory/`). Ahí no se ve en
git, no se revisa, no se versiona ni viaja a otra máquina. Esta clase deja esa
carpeta **vacía**: cada recuerdo se **mueve** a `historico-chat/memory/`.

Mover y no copiar: dos copias del mismo recuerdo terminan diciendo cosas
distintas, y manda la que nadie puede leer.

**Nada se borra.** Si el nombre ya está ocupado, el que llega entra como
`<nombre>-local.md` y decide el usuario.

**El almacén puede estar enlazado** al repositorio (un *junction* o un enlace
simbólico): ahí la norma ya está cumplida, y mover sería mover cada archivo
sobre sí mismo. Por eso todo pregunta primero si las dos rutas son el mismo
sitio en disco, no si se escriben igual.

No confundir con la memoria por señales (`13·DOC5`): aquella guarda lo que el
**proyecto** aprendió; esta, cómo quiere el usuario que el **agente** trabaje.
"""
import os
import re
import shutil

CARPETA = os.path.join("historico-chat", "memory")
INDICE = "memory.md"

# Claude Code nombra la carpeta del proyecto cambiando por `-` todo lo que no
# sea letra o dígito ASCII, acentos incluidos: c:\Ing. Jose\ia\agente da
# c--Ing--Jose-ia-agente.
_NO_ALFANUM = re.compile(r"[^A-Za-z0-9]")

# Sufijo del recuerdo que llega con un nombre ocupado: no se pisa nada.
_SUFIJO = "-local"


class Recuerdos:
    """La memoria del agente de un proyecto: dónde la deja la herramienta y
    dónde tiene que vivir. `casa` es la carpeta personal (las pruebas la cambian)."""

    def __init__(self, proyecto, casa=None):
        self.proyecto = os.path.abspath(proyecto)
        self.casa = casa

    def carpeta_local(self):
        """Dónde guarda la herramienta la memoria de este proyecto."""
        slug = _NO_ALFANUM.sub("-", self.proyecto)
        return os.path.join(self.casa or os.path.expanduser("~"),
                            ".claude", "projects", slug, "memory")

    def carpeta_repo(self):
        """Dónde debe vivir: `historico-chat/memory/` del proyecto."""
        return os.path.join(self.proyecto, *CARPETA.split(os.sep))

    def ruta_indice(self):
        return os.path.join(self.carpeta_repo(), INDICE)

    def indice_presente(self):
        """¿Ya hay índice? Sin distinguir mayúsculas: en Windows `MEMORY.md` (el
        de la herramienta) y `memory.md` son el mismo archivo, y preguntar por el
        nombre exacto haría que el instalador lo escribiera encima."""
        carpeta = self.carpeta_repo()
        if not os.path.isdir(carpeta):
            return False
        return INDICE.lower() in {n.lower() for n in os.listdir(carpeta)}

    @staticmethod
    def es_el_mismo(uno, otro):
        """¿Las dos rutas son el **mismo** sitio en disco? Un *junction* o un
        enlace hace que dos rutas distintas apunten al mismo lugar."""
        try:
            if os.path.exists(uno) and os.path.exists(otro):
                return os.path.samefile(uno, otro)
        except OSError:
            pass
        return (os.path.normcase(os.path.realpath(uno))
                == os.path.normcase(os.path.realpath(otro)))

    def enlazada(self):
        """¿El almacén de la herramienta **es** la carpeta del repositorio? Entonces
        `01·C19` ya está cumplido y no hay nada que mover."""
        return self.es_el_mismo(self.carpeta_local(), self.carpeta_repo())

    def sueltos(self):
        """Los archivos que quedaron en la carpeta de la herramienta. Vacío es como
        tiene que estar siempre; con el almacén enlazado también."""
        local = self.carpeta_local()
        if not os.path.isdir(local) or self.enlazada():
            return []
        return [os.path.join(local, n) for n in sorted(os.listdir(local))
                if os.path.isfile(os.path.join(local, n))]

    @staticmethod
    def libre(carpeta, nombre):
        """Un nombre que no choque con nada de `carpeta`, sin distinguir
        mayúsculas: mover `MEMORY.md` sobre `memory.md` borraba el índice."""
        ocupados = {n.lower() for n in os.listdir(carpeta)} if os.path.isdir(carpeta) else set()
        if nombre.lower() not in ocupados:
            return nombre
        base, ext = os.path.splitext(nombre)
        candidato = f"{base}{_SUFIJO}{ext}"
        n = 2
        while candidato.lower() in ocupados:
            candidato = f"{base}{_SUFIJO}-{n}{ext}"
            n += 1
        return candidato

    def migrar(self, aplicar=True):
        """Vacía la carpeta de la herramienta hacia `historico-chat/memory/`.
        Devuelve `[(nombre_de_origen, nombre_de_destino)]`.

        **Aquí no se borra nada, nunca.** La versión que borraba el archivo del
        almacén cuando era idéntico a uno del repositorio destruyó memoria real:
        con el almacén enlazado, los dos eran el mismo archivo.
        """
        pendientes = self.sueltos()
        if not pendientes:
            return []
        destino_carpeta = self.carpeta_repo()
        movidos = []
        for origen in pendientes:
            nombre = os.path.basename(origen)
            # Cinturón, además del de `sueltos`: mover un archivo sobre sí mismo
            # es la forma de perderlo.
            if self.es_el_mismo(origen, os.path.join(destino_carpeta, nombre)):
                continue
            nuevo = self.libre(destino_carpeta, nombre)
            movidos.append((nombre, nuevo))
            if aplicar:
                os.makedirs(destino_carpeta, exist_ok=True)
                shutil.move(origen, os.path.join(destino_carpeta, nuevo))
        return movidos

    @staticmethod
    def pasos(movidos):
        """Los movimientos, dichos en una línea cada uno."""
        salida = []
        ruta = CARPETA.replace(os.sep, "/")
        for nombre, destino in movidos:
            if destino == nombre:
                salida.append(f"mover `{nombre}` a `{ruta}/`")
            else:
                salida.append(f"mover `{nombre}` a `{ruta}/{destino}` "
                              f"— el nombre ya estaba ocupado; revisar cuál manda")
        return salida

    def contexto(self, tope=None):
        """El índice de la memoria, para inyectarlo al abrir la sesión: la
        herramienta solo carga sola lo que guarda ella, y ahí ya no hay nada.

        **Con `tope`, en caracteres, cabe siempre** (`EP-005 · HU-009 · CA-04`):
        si no cabe entero van solo las filas, y si tampoco, las primeras que
        quepan con la ruta del índice. Nunca se corta una fila a la mitad.
        """
        archivo = self.ruta_indice()
        if not os.path.isfile(archivo):
            return ""
        try:
            with open(archivo, encoding="utf-8", errors="replace") as f:
                texto = f.read()
        except OSError:
            return ""

        ruta = CARPETA.replace(os.sep, "/")
        cabeza = ("[MEMORIA DEL AGENTE — ÍNDICE, OBLIGATORIA]\n"
                  "Es cómo pide el usuario que se trabaje en este proyecto, y rige "
                  "esta sesión completa. Antes de tocar un tema que aparezca abajo, "
                  "leer con Read el archivo del recuerdo: el índice dice de qué "
                  "trata, no qué exige.\n"
                  f"Un recuerdo nuevo se escribe en `{ruta}/`, nunca en el almacén de "
                  "la herramienta (`01·C19`).\n\n")
        entero = f"{cabeza}<<< {ruta}/{INDICE} >>>\n{texto}"
        if tope is None or len(entero) <= tope:
            return entero

        filas = [l for l in texto.splitlines() if l.startswith(("| [", "- ["))]
        return self._hasta_caber(cabeza, filas, f"{ruta}/{INDICE}", tope)

    @staticmethod
    def _hasta_caber(cabeza, filas, indice, tope):
        """Las filas que caben en `tope`, y la ruta donde está el índice entero."""
        for cuantas in range(len(filas), -1, -1):
            if cuantas == len(filas):
                pie = f"El índice completo, con cómo se usa, está en `{indice}`."
            else:
                pie = f"Se listan {cuantas} de {len(filas)} recuerdos; el resto, en `{indice}`."
            salida = cabeza + pie + "\n\n" + "\n".join(filas[:cuantas])
            if len(salida.rstrip()) <= tope:
                return salida.rstrip()
        return ""

    def revisar(self):
        """¿La carpeta de la herramienta está vacía? `(cumple, detalle)`."""
        quedaron = self.sueltos()
        if not quedaron:
            return True, ""
        nombres = ", ".join(os.path.basename(r) for r in quedaron[:4])
        if len(quedaron) > 4:
            nombres += f" y {len(quedaron) - 4} más"
        local = self.carpeta_local().replace(os.sep, "/")
        return False, (f"quedaron {len(quedaron)} archivo(s) en la memoria local de "
                       f"la herramienta ({nombres}) — `{local}`; la memoria va en "
                       f"`{CARPETA.replace(os.sep, '/')}/` (`01·C19`)")
