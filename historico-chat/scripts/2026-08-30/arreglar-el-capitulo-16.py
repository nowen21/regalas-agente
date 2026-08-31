# -*- coding: utf-8 -*-
"""Pone las cuatro reglas del capitulo 16 dentro del molde que exige M5.

Estaban escritas con tres almohadillas porque el capitulo agrupaba en partes, y
por eso el analizador no las veia: ninguna fila del checklist se les aplico
nunca. Se bajan a dos almohadillas, las partes dejan de ser encabezado, CQ3
recibe el ejemplo que le faltaba, y las cuatro reciben su bloque de checklist.
"""
import io
import os

RAIZ = r"c:\Ing. Jose\ia\agente"
R = os.path.join(RAIZ, "base", "16-cumplimiento-y-calidad.md")

CHECKLIST = u"""

---

### Checklist  ·  **{resultado}**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v36.0.2**, el **2026-08-30**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | {c} |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: {verdes} ✅ · 0 ❌ · {na} N/A.**

{nota}

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
"""

NOTAS = {
 "CQ1": u"**Fila 3 · la regla nombra sector y jurisdicción, y eso no es dominio.** No dice cuál: dice que hay que averiguarlo antes de construir. El capítulo entero es `opt-in` y la capa 3 declara el marco concreto, que es lo que [`20·M3`](20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md) protege.\n\n**Fila 17 es `N/A`:** la regla no declara excepción.",
 "CQ2": u"**Fila 14 · declara su dependencia enlazada** con la regla de trazabilidad, que es la que le da el sitio donde queda la evidencia.\n\n**Fila 17 es `N/A`:** la regla no declara excepción.",
 "CQ3": u"**Fila 12 · el ejemplo se agregó el 2026-08-30, al aplicarle el checklist por primera vez.** La regla llevaba meses publicada sin él, y nadie lo vio porque el analizador no la reconocía como regla.\n\n**Fila 5 · nombrar OWASP no es nombrar tecnología.** [`20·M3`](20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md) prohíbe atar la norma a un lenguaje, un framework o un motor; un catálogo de controles de seguridad no es ninguna de las tres, y el capítulo existe justamente para nombrar marcos.\n\n**Fila 17 es `N/A`:** la regla no declara excepción.",
 "CQ4": u"**Fila 5 · nombrar ISO/IEC 25010 no es nombrar tecnología**, por lo mismo que `CQ3` con OWASP: es un marco de atributos, no una herramienta.\n\n**Fila 17 es `N/A`:** la regla no declara excepción.",
}

CQ3_EJEMPLO = u"""

```
INCORRECTO: revisar la seguridad "a ojo", con lo que cada quien recuerde
CORRECTO:   recorrer los controles de OWASP y decir cuáles aplican y dónde quedan
```"""

with io.open(R, encoding="utf-8") as f:
    t = f.read()

# 1 · Las partes dejan de ser encabezado: el nivel `##` queda para las reglas.
t = t.replace(
    u"## Parte A — Universal (capa 2)",
    u"**Parte A, lo universal**, que aplica siempre que el capítulo esté activo.")
t = t.replace(
    u"## Parte B — Gancho a capa 3 (lo declara cada proyecto)",
    u"## Lo que declara cada proyecto")

# 2 · CQ3 recibe el ejemplo que le faltaba, antes de subir de nivel.
v = (u"### CQ3 · Seguridad de software por defecto (OWASP)\n\nToma **OWASP** "
     u"(ASVS + Top 10) como línea base de controles de código seguro. Es la "
     u"instancia concreta de la seguridad de `04`: inyección, autenticación, "
     u"control de acceso, exposición de datos, configuración segura.")
assert v in t, "CQ3 no encontrada"
t = t.replace(v, v + CQ3_EJEMPLO, 1)

# 3 · Cada regla sube a `##` y recibe su bloque de checklist.
TITULOS = {
 "CQ1": u"### CQ1 · Sabe para quién construyes",
 "CQ2": u"### CQ2 · Cumple por construcción y déjalo trazable",
 "CQ3": u"### CQ3 · Seguridad de software por defecto (OWASP)",
 "CQ4": u"### CQ4 · Atributos de calidad como checklist (ISO/IEC 25010)",
}
ORDEN = ["CQ1", "CQ2", "CQ3", "CQ4"]
for i, cq in enumerate(ORDEN):
    t = t.replace(TITULOS[cq], TITULOS[cq][1:], 1)      # de `###` a `##`

# El bloque de checklist va al final del cuerpo de cada regla, o sea justo
# antes del titulo de la siguiente, y el de CQ4 antes del separador final.
lineas = t.split("\n")
salida = []
for n, linea in enumerate(lineas):
    siguiente_regla = linea.startswith("## CQ") and salida
    fin_de_parte = linea.startswith("## Lo que declara cada proyecto")
    if siguiente_regla or fin_de_parte:
        # Se cierra la regla anterior, si habia una.
        previa = None
        for atras in reversed(salida):
            if atras.startswith("## CQ"):
                previa = atras.split("·")[0].replace("#", "").strip()
                break
        if previa:
            while salida and not salida[-1].strip():
                salida.pop()
            while salida and salida[-1].strip() == "---":
                salida.pop()
                while salida and not salida[-1].strip():
                    salida.pop()
            salida.append(CHECKLIST.format(
                resultado=u"CUMPLE", c=u"✅ ✅ ✅ ✅ ✅ ✅ ✅",
                verdes=19, na=1, nota=NOTAS[previa]).rstrip())
            salida.append("")
            salida.append("---")
            salida.append("")
    salida.append(linea)

# La ultima regla queda cerrada por el separador final del capitulo.
t = "\n".join(salida)

with io.open(R, "w", encoding="utf-8", newline="\n") as f:
    f.write(t)
print("capitulo 16 al dia")
