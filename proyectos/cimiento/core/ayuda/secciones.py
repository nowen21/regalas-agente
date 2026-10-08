"""Las secciones del manual, en el orden en que se usa Cimiento, y la pantalla de cada una."""

# (sección, título, vistas de Django que la muestran)
SECCIONES = [
    ("primeros-pasos", "Primeros pasos", ()),
    ("palabras", "Palabras que conviene conocer", ()),
    ("entrar", "Entrar a Cimiento", ("cuentas:entrar",)),
    ("inicio", "Inicio", ("inicio:inicio",)),
    ("proyectos", "Proyectos", ("proyectos:lista",)),
    ("registrar", "Registrar o editar un proyecto", ("proyectos:registrar", "proyectos:editar")),
    ("reglas", "Las reglas de un proyecto", ("niveles:reglas", "niveles:historial")),
    ("configuracion", "Configuración", ("proyectos:configuracion",)),
    ("suspensiones", "Suspensiones", ("proyectos:suspensiones",)),
    ("gasto", "Gasto de tokens", ("consumo:tablero",)),
    ("historia", "Historia de los cambios", ("historia:lista", "historia:versiones")),
    ("estandar", "El estándar y la memoria", ("estandar:lista", "estandar:documento", "estandar:nuevo",
                                              "estandar:memoria", "estandar:recuerdo", "estandar:recuerdo_nuevo",
                                              "estandar:reglas_del_proyecto",
                                              "estandar:propuestas", "estandar:git",
                                              "estandar:reportes", "estandar:vista_previa")),
]

TITULOS = {s: t for s, t, _ in SECCIONES}
_POR_VISTA = {v: s for s, _, vistas in SECCIONES for v in vistas}

# Rutas con nombre que no son pantallas: no llevan sección.
NO_SON_PANTALLAS = {"cuentas:salir", "consumo:franja", "consumo:pestana", "consumo:aviso", "consumo:eventos",
                    "proyectos:levantar", "historia:deshacer", "estandar:quitar", "estandar:aprobar", "estandar:rechazar",
                    "estandar:resolver_reporte",
                    "ayuda:manual", "ayuda:pantalla", "ayuda:panel"}


def seccion_de(vista):
    """La sección del manual que explica la pantalla de esa vista; sin una propia, «Primeros pasos»."""
    return _POR_VISTA.get(vista or "", "primeros-pasos")


def tiene_seccion(vista):
    return vista in _POR_VISTA
