"""`EP-025·HU-033` · Cimiento llena los análisis sin guiones sueltos.

Sale del análisis 3 del pendiente 133, acuerdo 1. Cada análisis se llenaba con
un guion escrito para él, y ya había 49. Lo que siempre es igual lo hace
Cimiento al prender el análisis (`llenar_encabezado`); lo que redacta el agente
lo guarda un comando fijo, sección por sección (`poner_seccion`, que usa
`manage.py analisis seccion`).
"""
import io
import os
import re

RUTA = "«RUTA-ESTANDAR»"
SIGUIENTE = "`analisis-«N+1»`.md"
COPIA_HALLAZGO = re.compile(r"> Copia del hallazgo[^\n]*\n\n«copia del hallazgo»")
COPIA_PENDIENTE = re.compile(r"> Copia del pendiente[^\n]*\n\n«copia del pendiente»")

# El enlace del «De dónde sale» que nombra un hallazgo: `[… H-3 · título](ruta.md)`.
_ENLACE_HALLAZGO = re.compile(r"\[[^\]]*?\b(H-\d+) ·[^\]]*\]\(([^)#]+\.md)\)")
_TITULO = re.compile(r"^(#{2,6}) (.+?)[ \t]*$", re.M)


def _leer(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return f.read()


def hallazgo_del_pendiente(carpeta):
    """El texto del primer hallazgo que nombra el «De dónde sale» del pendiente, o `""`."""
    pendiente = os.path.join(carpeta, "pendiente.md")
    if not os.path.isfile(pendiente):
        return ""
    fila = next((l for l in _leer(pendiente).splitlines() if "De dónde sale" in l), "")
    m = _ENLACE_HALLAZGO.search(fila)
    if not m:
        return ""
    resumen = os.path.normpath(os.path.join(carpeta, m.group(2)))
    if not os.path.isfile(resumen):
        return ""
    texto = _leer(resumen)
    inicio = re.search(r"^### %s ·[^\n]*$" % re.escape(m.group(1)), texto, re.M)
    if not inicio:
        return ""
    resto = texto[inicio.start():]
    fin = re.search(r"\n(?=### |---\n|## )", resto[1:])
    return (resto[:fin.start() + 1] if fin else resto).strip()


def texto_del_pendiente(carpeta):
    """El pendiente sin su título, o `""`."""
    pendiente = os.path.join(carpeta, "pendiente.md")
    if not os.path.isfile(pendiente):
        return ""
    partes = _leer(pendiente).split("\n", 1)
    return partes[1].strip() if len(partes) > 1 else ""


def llenar_encabezado(texto, carpeta, numero, estandar):
    """El análisis con lo que siempre es igual ya puesto. Lo que no encuentra
    queda con su marca, para el agente."""
    ruta = os.path.relpath(estandar, carpeta).replace(os.sep, "/")
    texto = texto.replace(RUTA, ruta).replace(SIGUIENTE, "`analisis-%d.md`" % (numero + 1))
    pendiente = texto_del_pendiente(carpeta)
    if pendiente:
        texto = COPIA_PENDIENTE.sub(lambda _m: pendiente, texto, count=1)
    # Desde el análisis 2, el hallazgo que lo abre es nuevo y todavía no está en el pendiente.
    hallazgo = hallazgo_del_pendiente(carpeta) if numero == 1 else ""
    if hallazgo:
        texto = COPIA_HALLAZGO.sub(lambda _m: hallazgo, texto, count=1)
    return texto


class SeccionInexistente(ValueError):
    """La sección pedida no está en el análisis."""


def secciones(texto):
    return [m.group(2) for m in _TITULO.finditer(texto)]


def poner_seccion(texto, seccion, cuerpo):
    """`(texto nuevo, cuerpo anterior)`: el cuerpo de la sección cuyo título empieza
    por `seccion` queda reemplazado, hasta el título siguiente del mismo nivel o
    mayor, o la línea `---`."""
    buscada = seccion.strip().lower()
    titulos = list(_TITULO.finditer(texto))
    elegido = next((m for m in titulos if m.group(2).lower().startswith(buscada)), None)
    if not elegido:
        raise SeccionInexistente("no hay una sección «%s»; las que hay son: %s"
                                 % (seccion, "; ".join(secciones(texto))))
    nivel = len(elegido.group(1))
    inicio = elegido.end()
    fin = len(texto)
    for m in titulos:
        if m.start() > elegido.start() and len(m.group(1)) <= nivel:
            fin = m.start()
            break
    raya = re.search(r"^---$", texto[inicio:fin], re.M)
    if raya:
        fin = inicio + raya.start()
    anterior = texto[inicio:fin].strip("\n")
    nuevo = texto[:inicio] + "\n\n" + cuerpo.strip("\n") + "\n\n" + texto[fin:]
    return nuevo, anterior
