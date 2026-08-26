# -*- coding: utf-8 -*-
"""Qué documento es cada archivo, y cuáles ni se miran.

**Se reconoce por el nombre y la ubicación, no por el contenido.** El estándar
fija cómo se llama cada documento del ciclo de vida, así que el nombre **es** la
forma. Adivinar leyendo el texto es más frágil y más caro, y adivinar mal
ensucia lo que sí sirve.

**Solo se recorre la documentación del ciclo de vida.** Se decidió con el
usuario el 2026-08-25, después de contar sobre el repositorio del estándar:
dentro de `documentacion/` se reconoce el 99,7% de 969 archivos; fuera de ahí,
casi nada, porque `base/`, `plantillas/`, `historico-chat/` y `pendientes/` no
son documentación del ciclo. Recorrer todo dejaba un reporte de 540 líneas
donde los tres casos reales se perdían.

**Lo que no se mira igual se dice.** `CARPETAS_QUE_NO_SE_MIRAN` existe para que
el reporte lo nombre: saltarse carpetas sin decirlo es perder en silencio con
otro nombre (`RN-4`).
"""
import re

# Dónde vive la documentación del ciclo de vida dentro de un proyecto.
CARPETA_DEL_CICLO = "documentacion"

# Lo que no se mira, y por qué. El reporte lo mueestra tal cual.
CARPETAS_QUE_NO_SE_MIRAN = [
    ("base", "el cuerpo de reglas que el proyecto adopta, no su documentación"),
    ("plantillas", "los moldes del estándar, no documentos del proyecto"),
    ("historico-chat", "las conversaciones, que se guardan aparte"),
    ("pendientes", "el backlog, que no es documentación del ciclo"),
    ("validadores", "programas, no documentos"),
    ("skills", "procedimientos del agente, no del proyecto"),
    ("notas", "razonamientos de diseño, no documentos del ciclo"),
    ("prompts", "lo que el usuario pidió, con sus palabras"),
]

# Cada documento del ciclo, por el nombre exacto de su archivo.
POR_NOMBRE = {
    "epica.md": "épica",
    "plan_trabajo.md": "plan de trabajo",
    "plan_pruebas.md": "plan de pruebas",
    "resultado_pruebas.md": "resultado de pruebas",
    "funcionalidad_implementada.md": "funcionalidad implementada",
    "estado-fase.md": "estado de fase",
    "spec.md": "especificación de módulo",
    "senales.md": "señales",
    "README.md": "índice",
}

# Los que se reconocen por su forma de nombre, no por el nombre exacto.
POR_FORMA = [
    # `HU-001-lo-que-sea.md`
    (re.compile(r"^HU-\d+.*\.md$"), "historia de usuario"),
    # `resultado_pruebas_2.md`: el segundo ciclo de pruebas de una fase.
    (re.compile(r"^resultado_pruebas_\d+\.md$"), "resultado de pruebas"),
    # `2026-08-14-15.0.0.md`: un registro de adopción de versión.
    (re.compile(r"^\d{4}-\d{2}-\d{2}-\d+\.\d+\.\d+\.md$"),
     "registro de versión"),
]


def tipo_de(nombre):
    """El tipo del documento, o "" si no sigue ningún molde conocido.

    Los tres del final de `POR_FORMA` salieron de contar sobre el repositorio
    real: eran los únicos tres archivos de `documentacion/` sin reconocer, y
    resultaron ser moldes que faltaban en la lista, no casos raros.
    """
    if nombre in POR_NOMBRE:
        return POR_NOMBRE[nombre]
    for forma, tipo in POR_FORMA:
        if forma.match(nombre):
            return tipo
    return ""
