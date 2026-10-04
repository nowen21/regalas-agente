# -*- coding: utf-8 -*-
"""El aviso de resuelto sale solo con la prueba en el proyecto aprobada, y con
«Comprobado» lleno por Cimiento (análisis 1 del pendiente 110, acuerdo 7)."""
import io
import os

P = os.path.join(os.path.dirname(__file__), "..", "..", "..", "validadores", "aviso_resuelto.py")
t = io.open(P, encoding="utf-8").read()

viejo = t[t.index('PLANTILLA = """'):t.index('def _destino(')]
nuevo = '''PLANTILLA = """# Aviso: el estándar resolvió el pendiente que este proyecto reportó

Lo escribió `validadores/aviso_resuelto.py` el {fecha}. No se edita.

| | |
|---|---|
| **Pendiente del estándar** | `{pendiente}` |
| **Versión que trae la corrección** | {version} |

## Cómo lo comprobó Cimiento

Cimiento reprodujo el caso en una copia de este proyecto, en el escenario donde se presentó, y comprobó que la corrección funciona antes de avisar (`02·F29`).

{prueba}

## Qué hacer con esto

Actualizar el estándar en este proyecto y seguir con el trabajo. El pendiente de seguimiento de esta carpeta queda cerrado.

**Comprobado:** {fecha}
"""

# `02·F29` · Lo que Cimiento comprobó en el proyecto que reportó, antes de avisar.
PRUEBA = "prueba-en-el-proyecto.md"
_RESULTADO = re.compile(r"^\\*\\*Resultado:\\*\\*\\s*(pasa|falla)\\s*$", re.M)


def anotar_prueba(carpeta, fecha, escenario, casos):
    """Escribe `prueba-en-el-proyecto.md` en la carpeta del reporte.

    `casos`: `[(qué se probó, cómo, pasó)]`. Pasa solo si pasan todos."""
    paso = bool(casos) and all(c[2] for c in casos)
    filas = "\\n".join("| %s | %s | %s |" % (q, c, "Pasa" if p else "Falla") for q, c, p in casos)
    texto = ("# Prueba en el proyecto que reportó\\n\\n"
             "Hecha por Cimiento el %s, en %s (`02·F29`).\\n\\n"
             "| Qué se probó | Cómo | Resultado |\\n|---|---|---|\\n%s\\n\\n"
             "**Resultado:** %s\\n" % (fecha, escenario, filas, "pasa" if paso else "falla"))
    with open(os.path.join(carpeta, PRUEBA), "w", encoding="utf-8", newline="\\n") as f:
        f.write(texto)
    return paso


def prueba_paso(carpeta):
    """Si Cimiento ya comprobó la corrección en el proyecto y pasó."""
    m = _RESULTADO.search(comun.leer(os.path.join(carpeta, PRUEBA)))
    return bool(m) and m.group(1) == "pasa"


def _tabla_de_la_prueba(carpeta):
    texto = comun.leer(os.path.join(carpeta, PRUEBA))
    m = re.search(r"(?ms)^\\| Qué se probó.*?(?=^\\*\\*Resultado)", texto)
    return m.group(0).strip() if m else ""


'''
t = t.replace(viejo, nuevo)

a = '''        destino, porque = seguimiento_de(carpeta)
        if not destino:
            sin_entregar.append((carpeta, porque))
            continue'''
b = '''        if not prueba_paso(carpeta):
            sin_entregar.append((carpeta, "Cimiento todavía no comprobó la corrección en el proyecto "
                                          "(falta %s con resultado «pasa»)" % PRUEBA))
            continue
        destino, porque = seguimiento_de(carpeta)
        if not destino:
            sin_entregar.append((carpeta, porque))
            continue'''
assert t.count(a) == 1; t = t.replace(a, b)
a = '''                f.write(PLANTILLA.format(fecha=fecha, version=version,
                                         pendiente=os.path.relpath(carpeta, estandar).replace(os.sep, "/")))'''
b = '''                f.write(PLANTILLA.format(fecha=fecha, version=version, prueba=_tabla_de_la_prueba(carpeta),
                                         pendiente=os.path.relpath(carpeta, estandar).replace(os.sep, "/")))'''
assert t.count(a) == 1; t = t.replace(a, b)
t = t.replace("seguimiento cierra cuando el proyecto pone la fecha en su línea «Comprobado».",
              "aviso llega con «Comprobado» lleno: Cimiento ya probó la corrección en el proyecto (análisis 1 del pendiente 110, acuerdo 7).")
io.open(P, "w", encoding="utf-8", newline="\n").write(t)
print("listo")
