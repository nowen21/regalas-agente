# -*- coding: utf-8 -*-
"""Clasifica las reglas vigentes según **cuándo** se pueden hacer cumplir.

    python clasificar-reglas-por-accion.py

Paso 1 del pedido del 2026-09-16: que las reglas determinen cómo actúa el
agente, identificando la aplicable **antes** de ejecutar cada acción. Eso solo
es posible para las reglas que se pueden comprobar sobre la acción misma —la
herramienta y sus argumentos— en el enganche `PreToolUse`.

**No clasifica desde cero.** `validadores/reglas-validables.md` ya decide, regla
por regla, si un programa puede comprobarla **sobre el repositorio**. Este eje
es otro: **sobre la acción, antes de que ocurra**. Se apoya en aquel registro y
no lo reemplaza (`20·M12`).

Escribe `validadores/reglas-antes-de-la-accion.md` y comprueba que las 248
vigentes queden en una sola clase cada una.
"""
import io
import os
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(RAIZ, "validadores"))

import metareglas  # noqa: E402

# A · Sobre la acción, antes de ejecutarla. `PreToolUse` ve la herramienta y sus
# argumentos, y puede detener la acción. Cada una con lo que la dispara.
A = {
    "N1": "cualquier herramienta que cambie estado (Write, Edit, Bash que no sea de lectura) cuando el último mensaje del usuario no trae palabra que la autorice. Parcial: un «sí» a una pregunta del agente también autoriza (`C24`)",
    "C28": "el mismo disparador que `N1`: acción que cambia estado sin palabra de `palabras-clave.md` en el pedido",
    "N2": "Bash con `git commit` o `git push` sin «Suba» o «Hágalo» en el pedido",
    "N3": "`--no-verify`, `commit -n`, `core.hooksPath`, o contenido que marca una prueba como omitida",
    "N4": "Bash con `DROP`, `TRUNCATE`, `DELETE` sin `WHERE`, o una migración contra un entorno real",
    "N5": "el disparador de `N4` sobre muchos registros sin `dry-run` previo",
    "N7": "el disparador de `N4` sin respaldo hecho antes (`respaldo.py`)",
    "S11": "el disparador de `N4` contra el almacén productivo: cada escritura, aparte",
    "S12": "el disparador de `S11` cuando la escritura es un borrado lógico",
    "N6": "contenido de Write o Edit, o un comando, que trae una credencial (patrones de `secretos.py`)",
    "N8": "envío hacia afuera: WebFetch con cuerpo, `curl` o `Invoke-WebRequest` con datos, subida de un archivo, herramienta MCP que publica contenido",
    "C19": "Write o Edit dentro del almacén de memoria de la herramienta (`~/.claude/projects/*/memory/`)",
    "S9": "Write o Edit, o redirección en Bash, hacia una ruta fuera del proyecto que el usuario no autorizó exacta",
    "S10": "`killall`, `pkill`, `taskkill /IM`, `Stop-Process -Name`: terminar procesos por nombre o patrón",
    "S18": "Write de un guion fuera de `historico-chat/scripts/AAAA-MM-DD/`",
    "S19": "Write en `historico-chat/memory/` con una clave adentro. Parcial: el dato personal no se detecta sin leer",
    "F8": "Write o Edit sobre un archivo que no está en la tabla del plan aprobado de la fase en curso",
    "F11": "Write o Edit fuera del módulo que declaró la fase en curso. Parcial: exige que la fase lo declare",
    "G5": "`push --force`, `rebase` o `commit --amend` sobre historia ya publicada",
    "G7": "`git commit` sin que el mensaje anterior del agente haya mostrado el mensaje y los archivos. Parcial",
    "G10": "`git commit` cuyo mensaje trae marca de la herramienta. Hoy lo detiene `commit-msg`; antes, lo detendría la acción",
    "T4": "comando de pruebas o cambio de configuración que apunta a datos reales",
    "DP8": "comando de despliegue o de ejecución contra producción",
    "C16": "Edit sobre un archivo que cambió en disco desde la última lectura. La herramienta ya lo cubre en parte",
}

# B · Sobre el texto de la respuesta. Ocurren en lo que el agente escribe, y
# ningún enganche frena una respuesta antes de mostrarla: se miden después.
B = {"C5", "C8", "C20", "ID7", "ID8", "ID9", "ID10"}

# D · Sobre el repositorio o el código, al guardar o en integración. Tienen
# validador, o está clasificado como validable en `reglas-validables.md`.
D = {
    "G2", "G3", "G4", "G6", "G9", "D1", "D2", "D3", "EST1", "EST2",
    "E1", "E5", "R1", "R2", "S3", "S4", "S5", "Q3", "Q6", "T3", "T5",
    "DEP2", "DEP3", "DEP4", "CFG2", "F0", "F2", "F4", "F12", "F13", "F14",
    "F17", "F18", "F21", "F22", "F23", "F24", "F26", "C18", "C27",
    "DOC1", "DOC3", "DOC7", "DOC8", "DOC10", "DOC11", "DOC12", "DOC13",
    "DOC14", "DOC15", "DOC16", "DOC17", "DOC19", "DOC20", "DOC21", "DOC22",
    "DOC23", "CQ1", "IM2", "IM5", "DP1", "DP2", "DP4", "DP6", "DP7",
    "OB1", "OB3", "OB4", "M3", "M4", "M5", "M7", "M9", "M10", "M14",
    "M15", "M16", "M17", "M18",
}

NOMBRES = {
    "A": "Sobre la acción, antes de ejecutarla",
    "B": "Sobre el texto de la respuesta",
    "C": "Criterio: ningún programa la decide",
    "D": "Sobre el repositorio, al guardar",
}


def main():
    vigentes = [r for r in metareglas.reglas() if not r.derogada]
    ids = {r.id for r in vigentes}

    for nombre, grupo in (("A", set(A)), ("B", B), ("D", D)):
        sobran = grupo - ids
        if sobran:
            sys.exit(f"{nombre} nombra reglas que no existen o están derogadas: {sorted(sobran)}")
    choques = (set(A) & B) | (set(A) & D) | (B & D)
    if choques:
        sys.exit(f"reglas en dos clases a la vez: {sorted(choques)}")

    clase = {}
    for r in vigentes:
        clase[r.id] = ("A" if r.id in A else "B" if r.id in B
                       else "D" if r.id in D else "C")

    orden = lambda r: (r.capitulo, r.linea)
    lineas = [
        "# Qué reglas se pueden hacer cumplir antes de la acción",
        "",
        "Clasificación de las **248 reglas vigentes** según **cuándo** se pueden "
        "comprobar. Fecha: **2026-09-16**. Es el paso 1 del pedido de que las "
        "reglas determinen cómo actúa el agente, identificando la aplicable "
        "**antes** de ejecutar cada acción.",
        "",
        "**No reemplaza a [validadores/reglas-validables.md](reglas-validables.md).** "
        "Aquel decide si un programa puede comprobar una regla **sobre el "
        "repositorio**. Este eje es otro: **sobre la acción, antes de que "
        "ocurra**, que es lo único que el enganche `PreToolUse` de Claude Code "
        "puede ver y detener.",
        "",
        "Lo generó [historico-chat/scripts/2026-09-16/clasificar-reglas-por-accion.py]"
        "(../historico-chat/scripts/2026-09-16/clasificar-reglas-por-accion.py), "
        "que además comprueba que ninguna regla quede en dos clases ni sin clase.",
        "",
        "## Conteo",
        "",
        "| Clase | Qué significa | Cuántas |",
        "|---|---|---|",
    ]
    explica = {
        "A": "`PreToolUse` ve la herramienta y sus argumentos, y puede **detener** la acción",
        "B": "ocurren en lo que el agente escribe; ningún enganche frena la respuesta antes de mostrarla, así que se **miden después**",
        "C": "decidir si se cumplió es leer: dos personas pueden discutirlo",
        "D": "se comprueban sobre el código o los documentos; los corre el enganche de git o la integración",
    }
    for c in "ABDC":
        n = sum(1 for v in clase.values() if v == c)
        lineas.append(f"| **{c}** · {NOMBRES[c]} | {explica[c]} | {n} |")
    lineas += ["", f"**Total: {len(vigentes)}.**", ""]

    lineas += [
        "## A · Sobre la acción, antes de ejecutarla",
        "",
        "Son las que el enganche `PreToolUse` puede hacer cumplir. Las marcadas "
        "**parcial** tienen una mitad que exige leer: esa mitad no se bloquea.",
        "",
        "| Regla | Qué dice | Qué acción la dispara |",
        "|---|---|---|",
    ]
    for r in sorted((r for r in vigentes if clase[r.id] == "A"), key=orden):
        titulo = r.titulo.split("`")[0].strip()
        lineas.append(f"| `{r.capitulo}·{r.id}` | {titulo} | {A[r.id]} |")
    lineas.append("")

    for c in "BDC":
        lineas += [f"## {c} · {NOMBRES[c]}", "", "| Regla | Qué dice |", "|---|---|"]
        for r in sorted((r for r in vigentes if clase[r.id] == c), key=orden):
            titulo = r.titulo.split("`")[0].strip()
            lineas.append(f"| `{r.capitulo}·{r.id}` | {titulo} |")
        lineas.append("")

    destino = os.path.join(RAIZ, "validadores", "reglas-antes-de-la-accion.md")
    io.open(destino, "w", encoding="utf-8", newline="").write("\n".join(lineas))
    cuenta = {c: sum(1 for v in clase.values() if v == c) for c in "ABCD"}
    print(f"{len(vigentes)} vigentes -> A {cuenta['A']} · B {cuenta['B']} · "
          f"C {cuenta['C']} · D {cuenta['D']}")


if __name__ == "__main__":
    main()
