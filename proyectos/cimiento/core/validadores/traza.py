"""La traza de la sesión, paso a paso (`EP-005·HU-016`).

Lee la transcripción de una sesión (un archivo de líneas JSON) y saca la línea
de tiempo de lo que se ejecutó: un paso por cada llamada a una herramienta, con
su hora, un resumen de lo que se le pidió, cuánto tardó y si falló; y un cierre
con los totales. `escribir()` la deja en `historico-chat/trazas/` con el mismo
nombre que el histórico de esa sesión.

**Lee, no valida**: no devuelve hallazgos, por eso no hereda de `Validador`.

**No copia, a propósito**, el contenido de los resultados ni las respuestas del
agente: ahí viajan claves y datos (`00·N6`). Solo la entrada, recortada, y el
estado.

**El formato que lee.** Los bloques `tool_use` (nombre, argumentos) van en los
turnos del agente y los `tool_result` (a qué `tool_use_id` responden,
`is_error`) en los del usuario, cada línea con su marca de tiempo ISO 8601.
Una línea ilegible se salta.
"""
import io
import json
import os
from datetime import datetime

from ..enganches.historico import Historico

CARPETA = os.path.join("historico-chat", "trazas")
INDICE = "README.md"
LARGO = 80
# Llaves donde una herramienta recibe lo esencial de su encargo, en orden.
LLAVES = ("file_path", "command", "url", "pattern", "path", "query", "prompt")


class Traza:
    """Todo es estático salvo `escribir`, que deja el archivo junto al histórico."""

    @staticmethod
    def _momento(marca):
        try:
            return datetime.fromisoformat(str(marca).replace("Z", "+00:00"))
        except (TypeError, ValueError):
            return None

    @staticmethod
    def _hora(momento):
        return momento.strftime("%H:%M:%S") if momento else ""

    @staticmethod
    def _segundos(desde, hasta):
        if not desde or not hasta:
            return None
        return (hasta - desde).total_seconds()

    @staticmethod
    def _duracion(segundos):
        if segundos is None:
            return ""
        if segundos >= 10:
            return "%d s" % round(segundos)
        entero = round(segundos)
        return ("%d s" % entero) if abs(segundos - entero) < 0.05 else ("%.1f s" % segundos)

    @staticmethod
    def _resumen_entrada(entrada):
        """Una línea con lo esencial de lo que se le pidió, recortada (RN-02)."""
        if not isinstance(entrada, dict):
            return ""
        for llave in LLAVES:
            valor = entrada.get(llave)
            if valor:
                texto = " ".join(str(valor).split())
                return texto[:LARGO] + ("…" if len(texto) > LARGO else "")
        return ""

    @staticmethod
    def _bloques(dato):
        contenido = (dato.get("message") or {}).get("content") if isinstance(dato, dict) else None
        return contenido if isinstance(contenido, list) else []

    @classmethod
    def pasos(cls, ruta):
        """`[{"n", "hora", "herramienta", "entrada", "duracion", "estado", …}]`, en orden.

        Un paso es un bloque `tool_use`; su respuesta, el `tool_result` con el
        mismo `tool_use_id` (RN-01), por el identificador y no por el orden:
        con llamadas en paralelo las respuestas llegan desordenadas.
        """
        usos, respuestas = [], {}
        try:
            with io.open(ruta, encoding="utf-8", errors="replace") as f:
                lineas = f.readlines()
        except OSError:
            return []
        for linea in lineas:
            try:
                dato = json.loads(linea)
            except (json.JSONDecodeError, ValueError):
                continue                    # lo ilegible se salta (RN-06)
            if not isinstance(dato, dict):
                continue
            momento = cls._momento(dato.get("timestamp"))
            for bloque in cls._bloques(dato):
                if not isinstance(bloque, dict):
                    continue
                if bloque.get("type") == "tool_use":
                    usos.append({"id": bloque.get("id"), "momento": momento,
                                 "herramienta": bloque.get("name") or "(sin nombre)",
                                 "entrada": cls._resumen_entrada(bloque.get("input"))})
                elif bloque.get("type") == "tool_result":
                    respuestas[bloque.get("tool_use_id")] = {
                        "momento": momento, "error": bool(bloque.get("is_error"))}

        salida = []
        for n, uso in enumerate(usos, 1):
            r = respuestas.get(uso["id"])
            segundos = cls._segundos(uso["momento"], r["momento"]) if r else None
            salida.append({
                "n": n, "hora": cls._hora(uso["momento"]),
                "herramienta": uso["herramienta"], "entrada": uso["entrada"],
                "segundos": segundos, "duracion": cls._duracion(segundos),
                "estado": ("error" if r["error"] else "ok") if r else "sin respuesta",
                "_fin": r["momento"] if r else None, "_inicio": uso["momento"]})
        return salida

    @classmethod
    def cierre(cls, lista):
        """Los totales (RN-03): pasos, errores, por herramienta, el más lento, duración."""
        por = {}
        for p in lista:
            por[p["herramienta"]] = por.get(p["herramienta"], 0) + 1
        con_tiempo = [p for p in lista if p["segundos"] is not None]
        lento = max(con_tiempo, key=lambda p: p["segundos"], default=None)
        inicios = [p["_inicio"] for p in lista if p["_inicio"]]
        fines = [p["_fin"] for p in lista if p["_fin"]]
        total = cls._segundos(min(inicios), max(fines)) if inicios and fines else None
        return {"pasos": len(lista),
                "errores": sum(1 for p in lista if p["estado"] == "error"),
                "por_herramienta": por,
                "mas_lento": ("%s (%s)" % (lento["herramienta"], cls._duracion(lento["segundos"]))
                              if lento else ""),
                "duracion_total": cls._duracion(total)}

    @staticmethod
    def como_texto(lista, totales):
        """La traza en Markdown: la tabla de pasos y el cierre."""
        filas = ["| # | Hora | Herramienta | Qué se le pidió | Duración | Estado |",
                 "|---:|---|---|---|---:|---|"]
        filas += ["| %d | %s | %s | %s | %s | %s |"
                  % (p["n"], p["hora"], p["herramienta"], p["entrada"], p["duracion"], p["estado"])
                  for p in lista]
        conteo = " · ".join("%s %d" % (h, n) for h, n in sorted(totales["por_herramienta"].items()))
        pie = ["", "**Cierre:** %d pasos · %d error(es) · %s." % (totales["pasos"], totales["errores"], conteo)]
        if totales["mas_lento"]:
            pie.append("**El más lento:** %s. **Duración total:** %s." % (
                totales["mas_lento"], totales["duracion_total"]))
        return "\n".join(filas + pie) + "\n"

    @classmethod
    def escribir(cls, raiz, sesion, texto):
        """Deja la traza junto al histórico de esa sesión (RN-05). La ruta
        escrita, o `""`: sin `historico-chat/`, o sin un histórico con la marca
        de la sesión, no se inventa nada."""
        origen = Historico(raiz).archivo_de_sesion(sesion)
        if not origen:
            return ""
        nombre = os.path.basename(origen)
        carpeta = os.path.join(raiz, CARPETA)
        os.makedirs(carpeta, exist_ok=True)
        ruta = os.path.join(carpeta, nombre)
        cuerpo = ("# Traza de la sesión — %s\n\n"
                  "Qué ejecutó el agente, paso a paso. La conversación está en "
                  "[historico-chat/%s](../%s); acá va cada herramienta con su "
                  "hora, su duración y si falló. La produce `validar.py traza` "
                  "y no copia el contenido de ningún resultado.\n\n"
                  % (nombre[:-3], nombre, nombre)) + texto
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(cuerpo)
        cls._indexar(carpeta, nombre)
        return ruta

    @staticmethod
    def _indexar(carpeta, nombre):
        indice = os.path.join(carpeta, INDICE)
        if not os.path.isfile(indice):
            with io.open(indice, "w", encoding="utf-8", newline="\n") as f:
                f.write("# Trazas de sesión\n\n"
                        "Una por sesión trazada: qué ejecutó el agente, paso a "
                        "paso. Las produce `validar.py traza`; la conversación "
                        "de cada una está en su histórico, con el mismo nombre.\n\n")
        with io.open(indice, encoding="utf-8") as f:
            texto = f.read()
        if "(%s)" % nombre in texto:
            return
        linea = "- [historico-chat/trazas/%s](%s) — traza de esa sesión.\n" % (nombre, nombre)
        with io.open(indice, "a", encoding="utf-8", newline="\n") as f:
            f.write(linea if texto.endswith("\n") else "\n" + linea)

    @staticmethod
    def sesion_de(ruta):
        """El id de la sesión: el nombre del archivo de la transcripción."""
        return os.path.splitext(os.path.basename(ruta))[0]
