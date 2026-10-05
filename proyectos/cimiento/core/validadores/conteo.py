"""`EP-004·HU-009` · Por cuál regla se incumple más.

Una regla que produce cien hallazgos por semana casi nunca es un equipo
descuidado: es una regla mal escrita, o una que hace falta automatizar. Sin el
número, esa conversación es opinión contra opinión.

**Se guarda solo el identificador y cuántas veces.** Nunca el texto del hallazgo
ni la ruta: en un mensaje de incumplimiento viaja lo revisado, y ahí puede ir
una clave o un dato personal (`00·N6`, `12·PR4`).

**Vive en `metricas/`, fuera del control de versiones**: es generado (`09·G3`).
Una línea por corrida, con su fecha, su versión y su recuento.

No es un validador: no comprueba nada, cuenta lo que los demás encontraron.
"""
import io
import json
import os

from ..comun import Proyecto
from ..comun.archivos import Archivos
from ..comun.consola import conteo_por_regla

REGISTRO = os.path.join("metricas", "conteo-por-regla.jsonl")


class ConteoPorRegla:
    """El registro de corridas de un proyecto."""

    def __init__(self, proyecto, archivos=None):
        self.proyecto = proyecto if isinstance(proyecto, Proyecto) else Proyecto(proyecto)
        self.archivos = archivos or Archivos()

    @property
    def registro(self):
        return os.path.join(self.proyecto.raiz, *REGISTRO.split(os.sep))

    def version(self):
        """La versión del estándar en el momento de la corrida, o `""`."""
        ruta = os.path.join(self.proyecto.raiz, "VERSION")
        if not os.path.isfile(ruta):
            return ""
        return (self.archivos.leer(ruta).strip().splitlines() or [""])[0].strip()

    def anotar(self, hallazgos, cuando="", version=""):
        """Agrega la línea de esta corrida y devuelve lo que anotó.

        `cuando` y `version` se reciben en vez de mirarse acá: una función que
        lee el reloj no se puede probar dos veces con el mismo resultado.
        """
        hallazgos = list(hallazgos)
        fila = {"cuando": cuando, "version": version or self.version(),
                "conteo": conteo_por_regla(hallazgos), "total": len(hallazgos)}
        os.makedirs(os.path.dirname(self.registro), exist_ok=True)
        with io.open(self.registro, "a", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(fila, ensure_ascii=False, sort_keys=True) + "\n")
        return fila

    def corridas(self):
        """Lo anotado, de la más vieja a la más nueva. Una línea rota se salta:
        no se lleva el registro entero."""
        if not os.path.isfile(self.registro):
            return []
        salida = []
        for linea in self.archivos.leer(self.registro).splitlines():
            if linea.strip():
                try:
                    salida.append(json.loads(linea.strip()))
                except ValueError:
                    continue
        return salida

    def comparar(self):
        """Qué cambió entre las dos últimas corridas: `[(regla, antes, ahora)]`."""
        hechas = self.corridas()
        if len(hechas) < 2:
            return []
        antes, ahora = hechas[-2]["conteo"], hechas[-1]["conteo"]
        return [(r, antes.get(r, 0), ahora.get(r, 0)) for r in sorted(set(antes) | set(ahora))
                if antes.get(r, 0) != ahora.get(r, 0)]

    def lineas(self, hallazgos):
        """Lo que se imprime al terminar la corrida: el conteo y qué cambió."""
        cuenta = conteo_por_regla(hallazgos)
        if not cuenta:
            return ["Ningún hallazgo que contar."]
        orden = sorted(cuenta.items(), key=lambda kv: (-kv[1], kv[0]))
        salida = ["Hallazgos por regla (%d en total):" % sum(cuenta.values())]
        salida += ["  %-12s %d" % (regla, cuantos) for regla, cuantos in orden[:10]]
        if len(orden) > 10:
            salida.append("  (y %d regla(s) más con menos hallazgos)" % (len(orden) - 10))
        cambios = self.comparar()
        if cambios:
            salida.append("Cambió desde la corrida anterior:")
            # La flecha es la salida de siempre: quien la lea la reconoce así.
            salida += ["  %-12s %d → %d  (%s)" % (regla, antes, ahora, "baja" if ahora < antes else "sube")
                       for regla, antes, ahora in cambios[:10]]
        return salida
