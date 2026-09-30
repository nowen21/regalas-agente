import io

R = "C:\\Ing. Jose\\ia\\agente\\"


def cambiar(rel, pares):
    p = R + rel
    crudo = io.open(p, encoding="utf-8", newline="").read()
    crlf = "\r\n" in crudo
    s = crudo.replace("\r\n", "\n")
    for v, n in pares:
        assert v in s, (rel, v[:70])
        s = s.replace(v, n, 1)
    if crlf:
        s = s.replace("\n", "\r\n")
    io.open(p, "w", encoding="utf-8", newline="").write(s)


cambiar("validadores\\comun.py", [(
    'EXCLUIDAS = {".git", "__pycache__", ".venv", "venv", "node_modules", "vendor"}',
    '''EXCLUIDAS = {".git", "__pycache__", ".venv", "venv", "node_modules", "vendor",
             # `base/reglas-por-tarea/` son copias de las reglas de `base/`,
             # que escribe `mapa_tareas.py` (`EP-005·HU-023`). Recorridas, los
             # validadores las contarían como reglas repetidas; su coincidencia
             # con las de verdad la comprueba `validar.py tareas`.
             "reglas-por-tarea"}''')])

cambiar("validadores\\mapa_tareas.py", [
    ('''218.000. Viven en `reglas-por-tarea/`, en la raíz y no en `base/`: son copias,
y dentro de `base/` los validadores las contarían como reglas repetidas.''',
     '''218.000. Viven en `base/reglas-por-tarea/`, y los recorridos de los
validadores saltan esa carpeta (`comun.EXCLUIDAS`): son copias, y los
contarían como reglas repetidas.'''),
    ('POR_TAREA = "reglas-por-tarea"', 'POR_TAREA = "base/reglas-por-tarea"'),
    ('"[reglas-por-tarea/](../reglas-por-tarea/README.md).",',
     '"[base/reglas-por-tarea/](reglas-por-tarea/README.md).",'),
    ('"[base/mapa-de-tareas.md](../base/mapa-de-tareas.md) pone "',
     '"[base/mapa-de-tareas.md](../mapa-de-tareas.md) pone "'),
    ('    carpeta = os.path.join(raiz, POR_TAREA)\n    salida, filas = {}, []',
     '    carpeta = os.path.join(raiz, *POR_TAREA.split("/"))\n    salida, filas = {}, []'),
    ('''    raiz = raiz or RAIZ
    carpeta = os.path.join(raiz, POR_TAREA)
    if os.path.isfile''', '''    raiz = raiz or RAIZ
    carpeta = os.path.join(raiz, *POR_TAREA.split("/"))
    if os.path.isfile'''),
    ('''    carpeta = os.path.join(raiz, POR_TAREA)
    esperados = armar_por_tarea(raiz)
    for nombre, texto in esperados.items():''', '''    carpeta = os.path.join(raiz, *POR_TAREA.split("/"))
    esperados = armar_por_tarea(raiz)
    for nombre, texto in esperados.items():'''),
    ('''    carpeta = os.path.join(raiz, POR_TAREA)
    os.makedirs(carpeta, exist_ok=True)''', '''    carpeta = os.path.join(raiz, *POR_TAREA.split("/"))
    os.makedirs(carpeta, exist_ok=True)'''),
])

cambiar("validadores\\leidas.py", [
    ('carpeta = _normal(os.path.join(estandar or RAIZ, mapa_tareas.POR_TAREA))',
     'carpeta = _normal(os.path.join(estandar or RAIZ, *mapa_tareas.POR_TAREA.split("/")))'),
])

cambiar("adaptadores\\claude-code\\hook_antes.py", [
    ('''def leido(datos, proyecto):
    entrada = datos.get("tool_input") or {}
    leidas.anotar(proyecto, datos.get("session_id"), entrada.get("file_path") or "")
    return 0''',
     '''def leido(datos, proyecto):
    """Anota la lectura solo si fue entera: una lectura con `offset` o `limit`
    trae un pedazo, y contarla dejaba pasar la acción sin haber leído la regla."""
    entrada = datos.get("tool_input") or {}
    if entrada.get("offset") or entrada.get("limit"):
        return 0
    leidas.anotar(proyecto, datos.get("session_id"), entrada.get("file_path") or "")
    return 0'''),
])

cambiar("base\\tareas.md", [(
    '[reglas-por-tarea/](../reglas-por-tarea/README.md)',
    '[base/reglas-por-tarea/](reglas-por-tarea/README.md)')])
print("ok")
