"""Le dice al agente, al abrir la sesión, cómo le llegan las reglas.

**Ya no manda las reglas.** Hasta la 39.3.1 mandaba `00` y `01` enteros y el
índice del resto, unos 86.000 caracteres; la herramienta acepta 10.000 por
enganche y el resto lo deja fuera con un avance de 2.000, así que el agente
arrancaba con un comienzo cortado y creía tener las reglas. Desde la 39.3.0
llegan con cada mensaje (`recuperar.py`, con `base/mapa-de-tareas.md`), y al
arrancar basta decir eso (`EP-005·HU-009·CA-04`).

**El gate sigue igual.** Si el proyecto no tiene la estructura base (`02·F13`),
va el texto de esa regla y nada más: invitar a trabajar sería contradecirla.
"""
import os

from ..comun import Archivos
from ..comun.proyecto import EXCLUIDAS

# El gate de arranque. Vive en una subcarpeta, así que un glob plano sobre
# `base/*.md` no lo ve.
GATE = "02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md"


class Cargador:
    """Todo es estático: lee la carpeta del estándar y devuelve texto."""

    GATE = GATE

    @staticmethod
    def reglas(base):
        """`[(ruta relativa, ruta)]` de todos los `.md` bajo `base/`, en orden de
        precedencia. El alfabético de la ruta relativa ya lo es: `00` antes que
        `01`, y el índice de un capítulo antes que sus reglas."""
        salida = []
        for carpeta, subcarpetas, archivos in os.walk(base):
            subcarpetas[:] = [s for s in subcarpetas if s not in EXCLUIDAS]
            for nombre in archivos:
                if nombre.lower().endswith(".md"):
                    ruta = os.path.join(carpeta, nombre)
                    salida.append((os.path.relpath(ruta, base).replace("\\", "/"), ruta))
        return sorted(salida)

    @staticmethod
    def _solo_gate(base, reglas_encontradas):
        """`F13` no pasa: se carga el gate y nada más. Cargar las reglas de
        trabajo invitaría a trabajar sobre una estructura que el propio
        estándar manda detener."""
        for rel, ruta in reglas_encontradas:
            if rel == GATE:
                return (
                    "[ARRANQUE DETENIDO — EL GATE 02·F13 NO PASA]\n"
                    "No continuar con nada: ni crear el espacio, ni adecuar el "
                    "proyecto por iniciativa propia. Mostrar la orientación de "
                    "F13 que sigue y detenerse.\n\n"
                    f"<<< base/{rel} >>>\n{Archivos().leer(ruta)}")
        return ""

    @staticmethod
    def instruccion(estandar):
        """Lo que el agente necesita saber de las reglas al abrir: cómo le llegan."""
        raiz = os.path.abspath(estandar).replace(os.sep, "/")
        return (
            "[LAS REGLAS DEL ESTÁNDAR: LLEGAN CON CADA MENSAJE]\n"
            "Rigen esta sesión completa y mandan sobre lo que el usuario pida en el "
            "momento (`00·N10`). No se cargan al abrir: con cada mensaje llegan las "
            "que aplican a lo que pide, y las que no cupieron llegan nombradas.\n"
            "Antes de una tarea, leer con Read las reglas que "
            "`base/mapa-de-tareas.md` pone bajo ella. Ante cualquier choque gana "
            "`base/00-nucleo-blindado.md`.\n"
            "Sin una de las palabras de `base/01-conducta/palabras-clave.md`, no se "
            "actúa (`01·C28`).\n"
            f"El estándar está en `{raiz}`.")

    @classmethod
    def paquete(cls, estandar, gate_ok=True):
        """`(texto, avisos)` para el arranque. `avisos` queda vacío: se conserva
        por quien ya lo desempaca. Sin `base/` o sin reglas no entrega nada."""
        base = os.path.join(estandar, "base")
        if not os.path.isdir(base):
            return "", []
        encontradas = cls.reglas(base)
        if not encontradas:
            return "", []
        if not gate_ok:
            return cls._solo_gate(base, encontradas), []
        return cls.instruccion(estandar), []

    @classmethod
    def contexto(cls, estandar, gate_ok=True):
        """Solo el texto de `paquete`, para quien no mira los avisos."""
        return cls.paquete(estandar, gate_ok)[0]
