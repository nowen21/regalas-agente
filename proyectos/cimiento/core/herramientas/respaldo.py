"""`09·15` · Hace el respaldo antes de correr lo que no se puede deshacer.

`00·N7` exige comprobar que hay de dónde volver antes de una operación
irreversible sobre datos reales, y una regla del núcleo no debería depender de
que alguien se acuerde.

**El límite, dicho antes que nada.** «Operación irreversible» en general no se
puede detectar sin criterio: un borrado escrito a mano, un guion propio o una
llamada a una interfaz que borra del otro lado no los ve este programa. Cubre
el subconjunto nombrado, los comandos que se le pasan, y lo dice cada vez que
corre: **un respaldo parcial que se anuncia como total es peor que no
tenerlo**, porque genera confianza donde no la hay.

**No adivina el comando.** Sin `Respaldo de datos` declarado en
`.agente/stack.md` no corre nada y lo dice: adivinar cómo se respalda una base
ajena sería equivocarse justo antes de lo irreversible.

**Invocarlo es la autorización** de `00·N4`: nadie escribe el comando
destructivo dentro de este envoltorio sin querer. Lo que agrega no es permiso:
es la red.
"""
import os
import re
import subprocess
import sys

if __name__ == "__main__" and not __package__:
    # Corrido por su ruta: se arma el paquete para que las importaciones
    # relativas encuentren a `core`.
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    __package__ = "core.herramientas"

from ..comun import Archivos, Proyecto  # noqa: E402
from ..comun.consola import preparar_salida  # noqa: E402

STACK = os.path.join(".agente", "stack.md")

# Fila de la tabla de comandos: `| Acción | `comando` |`
_FILA = re.compile(r"(?m)^\|\s*\**(.+?)\**\s*\|\s*`(.+?)`\s*\|")

# Lo que se toma como marcador de «sin llenar» en las plantillas.
_SIN_LLENAR = ("«", "…")


class Respaldo:
    """El respaldo que un proyecto declara, y correrlo antes de lo irreversible."""

    def __init__(self, raiz=None):
        self.raiz = raiz or Proyecto.estandar()

    def comandos(self):
        """`{acción en minúsculas: comando}` de lo que el proyecto declaró."""
        archivo = os.path.join(self.raiz, *STACK.split(os.sep))
        if not os.path.isfile(archivo):
            return {}
        salida = {}
        for m in _FILA.finditer(Archivos().leer(archivo)):
            accion, cmd = m.group(1).strip().lower(), m.group(2).strip()
            if any(x in cmd for x in _SIN_LLENAR):
                continue                    # marcador sin llenar: no es un comando
            salida[accion] = cmd
        return salida

    def comando_de_respaldo(self):
        """El comando declarado para respaldar, o `""` si no lo hay."""
        return self.comandos().get("respaldo de datos", "")

    def respaldar(self, fecha, escribir=False):
        """Corre el respaldo declarado. `(ok, mensaje)`.

        **No inventa el comando**: sin declaración devuelve `(False, …)` y quien
        llama decide, que en este programa siempre es *no seguir*. `fecha` se
        recibe por compatibilidad: el comando declarado decide el nombre.
        """
        cmd = self.comando_de_respaldo()
        if not cmd:
            return False, (
                "el proyecto no declara «Respaldo de datos» en `%s`: no se hace el "
                "respaldo y **no se corre la operación**. Declararlo es de quien "
                "conoce el almacén, no de este programa" % STACK.replace(os.sep, "/"))
        if not escribir:
            return True, "se correría: %s" % cmd
        r = subprocess.run(cmd, shell=True, cwd=self.raiz, capture_output=True,
                           text=True, encoding="utf-8", errors="replace")
        if r.returncode != 0:
            return False, ("el respaldo falló (%s) — **no se corre la operación**: "
                           "%s" % (cmd, (r.stderr or r.stdout).strip()[:200]))
        return True, "respaldo hecho con: %s" % cmd


def main(argv=None):
    """Se pide a mano. Correrlo **es** la autorización de `00·N4`."""
    import argparse
    import datetime

    # El viejo no la preparaba: con la salida en un tubo, Windows escribía en su
    # página de códigos y «operación» llegaba partida a quien la leía.
    preparar_salida()
    p = argparse.ArgumentParser(
        description="Respalda y después corre la operación que se le pase. "
                    "Sin respaldo declarado no corre nada.")
    p.add_argument("operacion", nargs=argparse.REMAINDER,
                   help="el comando destructivo, tal cual se escribiría")
    p.add_argument("--raiz", default=os.getcwd())
    p.add_argument("--aplicar", action="store_true",
                   help="corre de verdad; sin esto solo dice qué haría")
    a = p.parse_args(argv)

    if not a.operacion:
        print("respaldo: falta la operación que se va a correr.")
        print("Uso: python validadores/respaldo.py --aplicar -- <comando>")
        return 2

    print("Cubre solo lo que se le pase por aquí. **Un borrado escrito a mano, "
          "un guion propio o un borrado por interfaz no los ve nadie** — eso "
          "sigue siendo criterio del agente (`00·N7`).\n")

    ok, mensaje = Respaldo(a.raiz).respaldar(datetime.datetime.now().strftime("%Y-%m-%d"), a.aplicar)
    print("  respaldo: %s" % mensaje)
    if not ok:
        return 1

    cmd = " ".join(x for x in a.operacion if x != "--")
    if not a.aplicar:
        print("  operación: se correría: %s  (simulado; agrega --aplicar)" % cmd)
        return 0

    print("  operación: %s" % cmd)
    sys.stdout.flush()                      # que el aviso salga antes que la operación
    return subprocess.run(cmd, shell=True, cwd=a.raiz).returncode


if __name__ == "__main__":
    sys.exit(main())
