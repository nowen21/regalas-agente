# -*- coding: utf-8 -*-
"""La lista de comprobación de una regla, y el sello que deja.

**El checklist ya existe**, con sus veinte filas, y cada fila nombra la
meta-regla que la respalda. Acá no se inventa ninguna: se leen las que hay y se
presentan contra una regla.

**Buena parte de las filas pide criterio, y eso no se automatiza.** Lo dice la
ficha de `F-007`: *«la plataforma acompaña, no decide»*. Preguntas como si el
capítulo es el dueño del tema, o si la regla no existe ya con otras palabras,
las responde una persona. Lo que la plataforma hace es **traer las veinte filas,
guardar lo que se respondió, y no dejar que el resultado sobreviva a un cambio
del texto**.

**Y esa última parte es la que de verdad protege.** Un sello que se queda pegado
a una regla que después se editó dice que algo se comprobó, y lo que se comprobó
era otro texto. Peor que no tener sello: da confianza sin respaldo.
"""
import io
import os
import re

# Una fila del checklist: `| 7 | Título | [M5](...) | criterio |`.
_FILA = re.compile(u"(?m)^\\|\\s*(\\d+)\\s*\\|\\s*([^|]+?)\\s*\\|\\s*([^|]*?)\\s*\\|\\s*([^|]*?)\\s*\\|")

# El bloque del sello dentro de una regla.
_SELLO = re.compile(u"(?m)^###\\s+Checklist\\b")

# `contra **v2.2.0**, el **2026-08-07**`
_CONTRA = re.compile(u"contra\\s+\\**v?([\\d.]+)\\**")
_CUANDO = re.compile(u"el\\s+\\**(\\d{4}-\\d{2}-\\d{2})\\**")

# La frase que hace caducar el sello al editar la regla.
AVISO_DE_CADUCIDAD = (
    u"> Vale mientras el texto de arriba no cambie. Si la regla se edita, este "
    u"resultado queda **anulado** y se vuelve a aplicar el checklist.")


class NoHayChecklist(Exception):
    """No se encontró la lista de comprobación del estándar."""


def filas(raiz):
    """Las veinte filas del checklist, tal como están escritas.

    Devuelve `[{"numero", "que", "respaldo", "criterio"}]`.
    """
    ruta = os.path.join(raiz, "base", "20-meta-reglas", "checklist.md")
    if not os.path.isfile(ruta):
        raise NoHayChecklist(
            "No está la lista de comprobación del estándar: %s" % ruta)
    with io.open(ruta, encoding="utf-8", errors="replace") as archivo:
        texto = archivo.read()
    return [{"numero": int(n), "que": que, "respaldo": respaldo,
             "criterio": criterio}
            for n, que, respaldo, criterio in _FILA.findall(texto)
            if que.lower() not in ("qué comprueba", "que comprueba")]


def tiene_sello(texto_de_la_regla):
    """Si esa regla trae un sello escrito."""
    return bool(_SELLO.search(texto_de_la_regla or ""))


def contra_que(texto_de_la_regla):
    """Contra qué versión y en qué fecha se selló, o `("", "")`."""
    if not tiene_sello(texto_de_la_regla):
        return "", ""
    desde = _SELLO.search(texto_de_la_regla).start()
    bloque = texto_de_la_regla[desde:]
    version = _CONTRA.search(bloque)
    cuando = _CUANDO.search(bloque)
    return (version.group(1) if version else "",
            cuando.group(1) if cuando else "")


def parece_vencido(texto_de_la_regla, tocado_el):
    """Si por fechas el sello **parece** anulado. No es el veredicto.

    `tocado_el` es cuándo cambió el archivo por última vez. Comparar fechas es
    barato y sirve para mirar; **no sirve para decidir**, y por eso el nombre lo
    dice.

    **Se midió, y por poco sale un aviso falso.** Comparando solo fechas, 185
    de las 248 reglas vigentes de este repositorio quedaban con el sello
    anulado. El estándar dice que ninguna lo está, y tiene razón: compara el
    **cuerpo** de la regla contra el guardado, y **la tipografía no vence un
    sello**. Limpiar unas semirayas no cambia ninguna respuesta del checklist.

    Un aviso falso de esta magnitud haría lo mismo que un rojo falso: enseñar a
    ignorarlo. Quien lo pregunte de verdad usa `veredicto_del_estandar`.
    """
    if not tiene_sello(texto_de_la_regla):
        return True
    _, cuando = contra_que(texto_de_la_regla)
    if not cuando or not tocado_el:
        return True
    return tocado_el > cuando


def veredicto_del_estandar(raiz):
    """Qué dice el estándar sobre los sellos de ese proyecto.

    **Es el que manda.** El estándar compara el cuerpo de cada regla contra el
    guardado y descuenta los cambios de tipografía; acá no se reimplementa esa
    comparación, porque dos versiones de la misma pregunta se separan y la que
    quede vieja va a avisar de más.

    Devuelve `{"se_pudo", "porque", "sellos_vencidos"}`.
    """
    import subprocess
    import sys

    from django.conf import settings

    entrada = os.path.join(str(settings.CARPETA_VALIDADORES), "validar.py")
    if not os.path.isfile(entrada):
        return {"se_pudo": False,
                "porque": "no está el punto de entrada del estándar",
                "sellos_vencidos": []}
    try:
        corrida = subprocess.run(
            [sys.executable, entrada, "metareglas", "--raiz", raiz],
            capture_output=True, text=True, encoding="utf-8",
            errors="replace", timeout=900)
    except (OSError, subprocess.SubprocessError) as falla:
        return {"se_pudo": False, "porque": str(falla), "sellos_vencidos": []}

    salida = (corrida.stdout or "") + (corrida.stderr or "")
    vencidos = [linea.strip() for linea in salida.split("\n")
                if "sello" in linea.lower() and linea.strip().startswith("[")]
    return {"se_pudo": True, "porque": "", "sellos_vencidos": vencidos}


def molde_del_sello(version_del_estandar, cuando, respuestas):
    """El bloque del sello, para escribirlo debajo de la regla.

    `respuestas` es `{numero: "si" | "no" | "n/a"}`. Las que digan `n/a`
    **tienen que traer su motivo** en `{numero: (estado, motivo)}`, porque una
    fila que no aplica sin decir por qué no se distingue de una que se saltó.
    """
    marcas = {"si": u"✅", "no": u"❌", "n/a": u"N/A"}
    cuenta = {"si": 0, "no": 0, "n/a": 0}
    lineas, motivos = [], []
    for numero in sorted(respuestas):
        valor = respuestas[numero]
        estado, motivo = valor if isinstance(valor, tuple) else (valor, "")
        estado = (estado or "").lower()
        cuenta[estado] = cuenta.get(estado, 0) + 1
        lineas.append(u"| %d | %s |" % (numero, marcas.get(estado, estado)))
        if estado == "n/a":
            motivos.append(u"**%d**: %s" % (numero, motivo or u"«…»"))

    veredicto = u"**NO CUMPLE**" if cuenta.get("no") else u"**CUMPLE**"
    total = sum(cuenta.values())
    return (
        u"---\n\n"
        u"### Checklist  ·  %s\n\n"
        u"Aplicado el [checklist del estándar](../checklist.md) contra "
        u"**v%s**, el **%s**.\n\n"
        u"| Fila | Resultado |\n|---|---|\n%s\n\n"
        u"**%d filas: %d ✅ · %d ❌ · %d N/A.**%s\n\n"
        u"%s\n"
    ) % (veredicto, version_del_estandar, cuando, u"\n".join(lineas), total,
         cuenta.get("si", 0), cuenta.get("no", 0), cuenta.get("n/a", 0),
         (u" **N/A** — " + u" · ".join(motivos)) if motivos else u"",
         AVISO_DE_CADUCIDAD)
