# -*- coding: utf-8 -*-
"""Cierra el hueco de la fase E: `cvds/` entra a lo que se trae."""
import io

# --- moldes.py ---
p = "nucleo/importacion/moldes.py"
t = io.open(p, encoding="utf-8").read()

t = t.replace('''donde los tres casos reales se perdían.''',
'''donde los tres casos reales se perdían.

**Las etapas del ciclo también son documentación del ciclo, y se estaban
quedando afuera.** La fase E recorría solo `documentacion/`, y las siete etapas
viven en `cvds/`. Peor: `cvds/` no estaba ni en la lista de lo que se declara
como no mirado, así que se saltaba **en silencio**. Se descubrió en la fase G,
que fue la primera que necesitó leerlas para calcular el estado de un proyecto.
Desde entonces se recorren las dos carpetas.''', 1)

t = t.replace('''# Dónde vive la documentación del ciclo de vida dentro de un proyecto.
CARPETA_DEL_CICLO = "documentacion"''',
'''# Dónde vive la documentación del ciclo de vida dentro de un proyecto. Son dos:
# los documentos de las épicas, historias y fases van en una, y los de las siete
# etapas del ciclo en la otra.
CARPETAS_DEL_CICLO = ("documentacion", "cvds")''')

t = t.replace('''    "README.md": "índice",
}''',
'''    "README.md": "índice",
    # Los documentos de las etapas del ciclo, que viven en `cvds/`.
    "inventario-funcionalidades.md": "inventario de funcionalidades",
    "estudio-factibilidad.md": "estudio de factibilidad",
    "acta-de-constitucion.md": "acta de constitución",
    "modelo-de-datos.md": "modelo de datos",
    "decisiones-de-arquitectura.md": "decisiones de arquitectura",
    "diseno-de-interfaz.md": "diseño de interfaz",
    "contrato-de-la-interfaz.md": "contrato de la interfaz",
}

# Las siete etapas del ciclo de vida. El documento de cada una es el `README.md`
# de su carpeta, y por eso su tipo depende de dónde está y no solo del nombre.
ETAPAS = ("planificacion", "analisis-requisitos", "diseno", "implementacion",
          "pruebas", "despliegue", "mantenimiento")''')

viejo = '''def tipo_de(nombre):
    """El tipo del documento, o "" si no sigue ningún molde conocido.

    Los tres del final de `POR_FORMA` salieron de contar sobre el repositorio
    real: eran los únicos tres archivos de `documentacion/` sin reconocer, y
    resultaron ser moldes que faltaban en la lista, no casos raros.
    """
    if nombre in POR_NOMBRE:'''
nuevo = '''def tipo_de(nombre, relativa=""):
    """El tipo del documento, o "" si no sigue ningún molde conocido.

    `relativa` es su ruta dentro del proyecto, y hace falta para una sola cosa:
    **el `README.md` de una carpeta de etapa es el documento de esa etapa**, no
    un índice cualquiera. El nombre solo no alcanza para distinguirlos.

    Los tres del final de `POR_FORMA` salieron de contar sobre el repositorio
    real: eran los únicos tres archivos de `documentacion/` sin reconocer, y
    resultaron ser moldes que faltaban en la lista, no casos raros.
    """
    if nombre == "README.md" and relativa:
        partes = relativa.replace("\\\\", "/").split("/")
        if len(partes) >= 2 and partes[-2] in ETAPAS:
            return "etapa del ciclo de vida"
    if nombre in POR_NOMBRE:'''
assert viejo in t, "no se encontró tipo_de"
t = t.replace(viejo, nuevo, 1)
io.open(p, "w", encoding="utf-8", newline="\n").write(t)
print("moldes ok")

# --- core.py ---
p = "nucleo/importacion/core.py"
t = io.open(p, encoding="utf-8").read()

t = t.replace('''        self.sin_reconocer = []    # rutas relativas
        self.carpeta_del_ciclo = ""''',
'''        self.sin_reconocer = []    # rutas relativas
        self.carpetas_del_ciclo = []''')

t = t.replace('''    @property
    def hay_documentacion(self):
        return bool(self.carpeta_del_ciclo)''',
'''    @property
    def hay_documentacion(self):
        return bool(self.carpetas_del_ciclo)''')

viejo = '''    hallazgo = Hallazgo(proyecto)
    if not proyecto.ruta_viva:
        return hallazgo

    ciclo = os.path.join(proyecto.ruta_codigo, moldes.CARPETA_DEL_CICLO)
    if not os.path.isdir(ciclo):
        return hallazgo
    hallazgo.carpeta_del_ciclo = ciclo

    for raiz, _, archivos in os.walk(ciclo):
        for nombre in sorted(archivos):
            if not nombre.endswith(".md"):
                continue
            relativa = os.path.relpath(os.path.join(raiz, nombre),
                                       proyecto.ruta_codigo).replace(os.sep, "/")
            tipo = moldes.tipo_de(nombre)
            if tipo:
                hallazgo.reconocidos.append((relativa, tipo))
            else:
                hallazgo.sin_reconocer.append(relativa)
    return hallazgo'''
nuevo = '''    hallazgo = Hallazgo(proyecto)
    if not proyecto.ruta_viva:
        return hallazgo

    # Se recorren **las dos** carpetas del ciclo: la de épicas, historias y
    # fases, y la de las siete etapas. Que la segunda faltara era el hueco de
    # la fase E, y se saltaba en silencio.
    for carpeta in moldes.CARPETAS_DEL_CICLO:
        ciclo = os.path.join(proyecto.ruta_codigo, carpeta)
        if not os.path.isdir(ciclo):
            continue
        hallazgo.carpetas_del_ciclo.append(ciclo)

        for raiz, _, archivos in os.walk(ciclo):
            for nombre in sorted(archivos):
                if not nombre.endswith(".md"):
                    continue
                relativa = os.path.relpath(
                    os.path.join(raiz, nombre),
                    proyecto.ruta_codigo).replace(os.sep, "/")
                tipo = moldes.tipo_de(nombre, relativa)
                if tipo:
                    hallazgo.reconocidos.append((relativa, tipo))
                else:
                    hallazgo.sin_reconocer.append(relativa)
    return hallazgo'''
assert viejo in t, "no se encontró mirar"
t = t.replace(viejo, nuevo, 1)

t = t.replace('''                    tipo=moldes.tipo_de(nombre),''',
              '''                    tipo=moldes.tipo_de(nombre, relativa),''')

io.open(p, "w", encoding="utf-8", newline="\n").write(t)
print("core ok")
