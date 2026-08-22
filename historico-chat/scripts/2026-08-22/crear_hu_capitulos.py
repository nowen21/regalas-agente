# -*- coding: utf-8 -*-
"""Pendiente 60, salida (a): una historia de usuario por capítulo de base/."""
import io
import os
import re
import subprocess
import sys
import unicodedata

RAIZ = r"c:\Ing. Jose\ia\agente"
os.chdir(RAIZ)
EP = "EP-001-cuerpo-de-reglas-heredable"
EPDIR = os.path.join("documentacion", "epicas", EP)
YA = {"00": "HU-012-inventario-de-acciones-y-riesgo",
      "01": "HU-011-buscar-antes-de-preguntar"}


def slug(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-zA-Z0-9]+", "-", t.lower()).strip("-")


def capitulos():
    salida = []
    for nombre in sorted(os.listdir("base")):
        m = re.match(r"^(\d\d)-(.+?)(\.md)?$", nombre)
        if not m:
            continue
        num = m.group(1)
        ruta = os.path.join("base", nombre)
        es_carpeta = os.path.isdir(ruta)
        if num == "00" and "identidad" in nombre:
            continue
        archivo = os.path.join(ruta, "base.md") if es_carpeta else ruta
        h1 = io.open(archivo, encoding="utf-8").readline().strip()
        titulo = re.sub(r"^#\s*\d\d\s*\u00b7\s*", "", h1)
        titulo = re.split(r"\s+\u00b7\s+`", titulo)[0].strip()
        if es_carpeta:
            reglas = len([f for f in os.listdir(os.path.join(ruta, "reglas"))
                          if f.endswith(".md")])
        else:
            cuerpo = io.open(archivo, encoding="utf-8").read()
            reglas = len(re.findall(r"^## [A-Z]+\d+(?:\.\d+)? \u00b7 ", cuerpo, re.M))
        salida.append((num, titulo, archivo, es_carpeta, reglas))
    return salida


def plantilla(hu_id, hu_dir, num, titulo, archivo, reglas):
    cap_rel = "../../../../" + archivo.replace("\\", "/")
    cap_txt = archivo.replace("\\", "/")
    return f"""# {hu_id} — El capítulo `{num}` · {titulo}: su texto tiene dueña

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | {hu_id} |
| **Épica** | [EP-001 — Cuerpo de reglas heredable y en capas](../epica.md) |
| **Módulo / Componente** | Capítulo `{num}` · {titulo} |
| **Tipo** | Técnica |
| **Prioridad** | Should |
| **Estimación** | S |
| **Solicitante** | Quien define el estándar (pendiente 60, salida «una historia por capítulo», decidida por el usuario el 2026-08-22) |
| **Estado** | Backlog |

## 2. Narrativa

- **Como** quien mantiene el estándar
- **Quiero** que el texto del capítulo `{num}` tenga una historia de usuario dueña, que diga de dónde baja cada una de sus reglas y reciba todo cambio de su texto
- **Para** que un cambio del capítulo tenga dónde bajarse por la cadena (`02·F23`) y la pregunta «¿de dónde salió esta regla?» tenga respuesta

## 3. Contexto y descripción

El capítulo [`{num} · {titulo}`]({cap_rel}) tiene hoy **{reglas} regla(s)** y, hasta esta historia, ninguna historia de usuario declaraba su texto como módulo: se escribió sin recorrer la cadena que él mismo exige. Lo midió el [pendiente 60](../../../../pendientes/hecho/cada-capitulo-tiene-su-historia.md): 19 de 21 capítulos estaban así, y el usuario decidió una historia por capítulo.

Esta historia es la dueña del **texto** del capítulo. No de su comprobación (eso vive en EP-004) ni de su disparo (EP-005): de lo que el capítulo dice.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Todo cambio del texto del capítulo `{num}` entra como fase de esta historia (`02·F23`) |
| RN-02 | Toda regla nueva del capítulo nace por el procedimiento del `20` y cita esta historia como su origen |
| RN-03 | El capítulo declara su historia dueña en su cabecera, para que se lea desde el capítulo mismo |

### 3.2 Supuestos

- El capítulo existe y se usa: esta historia lo retrodocumenta; no lo reescribe.

### 3.3 Fuera de alcance

- Arreglar las reglas del capítulo que reprueban su checklist: eso es el pendiente 19 y sus fases en HU-009.
- La comprobación automática de las reglas del capítulo (EP-004).

## 4. Criterios de aceptación

### CA-01 — El capítulo nombra su historia dueña

```gherkin
Dado que el capítulo {num} existe
Cuando alguien abre su cabecera
Entonces encuentra la historia de usuario dueña de su texto, enlazada
```

**Cómo validarlo:**

1. Abrir [`{cap_txt}`]({cap_rel}). Resultado esperado: bajo el título hay una línea «Historia dueña del texto» que enlaza a esta historia.
- **Aprobado cuando:** la línea existe y el enlace resuelve.

### CA-02 — Un cambio del capítulo tiene dónde bajarse

```gherkin
Dado que hay que cambiar el texto de una regla del capítulo {num}
Cuando se baja el cambio por la cadena
Entonces la fase nace bajo esta historia y su plan declara qué reglas toca
```

**Cómo validarlo:**

1. Levantar con el andamio una fase de esta historia para un cambio cualquiera del capítulo (simulado). Resultado esperado: la fase se crea bajo `{hu_dir}/`.
- **Aprobado cuando:** la cadena tiene un eslabón para el capítulo, que antes no tenía.

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| Trazabilidad | Se puede nombrar, para el capítulo `{num}`, la historia donde se escribe su texto |

## 6. Tareas técnicas derivadas

- [x] Declarar la historia dueña en la cabecera del capítulo (hecho al crear esta historia).
- [ ] Retrodocumentar el capítulo en una fase: de dónde baja cada regla.

## 7. Fases que la implementan

| Fase | Qué CA cubre | Estado |
|---|---|---|
| (ninguna todavía) | | La primera fase será la retrodocumentación del capítulo |

## 8. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-007 (el procedimiento de la regla) y HU-009 (checklists al día) | Medio |
| Riesgo | Que la historia quede como cascarón sin fase | Bajo: el inventario de HU (pendiente 48) la cuenta como incompleta hasta que la tenga |

## 9. Definition of Ready

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y verificables
- [x] Dependencias identificadas

## 10. Definition of Done

- [x] El capítulo declara su dueña
- [ ] Fase de retrodocumentación cerrada

## 11. Validación INVEST

| Criterio | Cumple | Observación |
|---|:--:|---|
| Independiente | Sí | Un capítulo, una historia |
| Negociable | Sí | Qué entra en la retrodocumentación se discute en su fase |
| Valiosa | Sí | Cierra la trazabilidad hacia arriba de {reglas} regla(s) |
| Estimable | Sí | Una fase de retrodocumentación |
| Pequeña | Sí | |
| Testeable | Sí | La línea en la cabecera y la fase que nace bajo ella |

## 12. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-22 | El agente, por decisión del usuario (pendiente 60, salida a) | Creación: una historia por capítulo |
"""


def reemplazar(p, a, b):
    s = io.open(p, encoding="utf-8").read()
    if a not in s:
        print("  (no estaba en", p, ")", a[:60])
    io.open(p, "w", encoding="utf-8", newline="").write(s.replace(a, b))


creadas = []
for num, titulo, archivo, es_carpeta, reglas in capitulos():
    if num in YA:
        hu_dir = YA[num]
    else:
        s = f"el-capitulo-{num}-{slug(titulo)}"
        r = subprocess.run([sys.executable, "validadores/andamio.py", "hu", EP, s, "--aplicar"],
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
        m = re.search(r"(HU-\d{3}-[^\s\\/]+)", r.stdout)
        if not m:
            print("FALLÓ el andamio para", num, r.stdout[:200], r.stderr[:200])
            continue
        hu_dir = m.group(1)
        hu_id = hu_dir[:6]
        hu_md = os.path.join(EPDIR, hu_dir, hu_dir + ".md")
        io.open(hu_md, "w", encoding="utf-8", newline="").write(
            plantilla(hu_id, hu_dir, num, titulo, archivo, reglas))
        reemplazar(os.path.join(EPDIR, "epica.md"),
                   f"| [{hu_id}]({hu_dir}/{hu_dir}.md) | «Título» | «Prioridad» | «Estimación» |",
                   f"| [{hu_id}]({hu_dir}/{hu_dir}.md) | El capítulo `{num}` · {titulo}: su texto tiene dueña | Should | S |")
        reemplazar(os.path.join(EPDIR, "README.md"),
                   f"]({hu_dir}/) | Historia de usuario: «…» |",
                   f"]({hu_dir}/) | Historia de usuario: el capítulo `{num}` ({titulo}) tiene dueña de su texto |")
        creadas.append((num, hu_id))
    prefijo = "../../documentacion/epicas/" if es_carpeta else "../documentacion/epicas/"
    s = io.open(archivo, encoding="utf-8").read()
    if "Historia dueña del texto" not in s:
        lineas = s.split("\n")
        lineas.insert(1, "")
        lineas.insert(2, f"> **Historia dueña del texto:** [EP-001 · {hu_dir[:6]}]({prefijo}{EP}/{hu_dir}/{hu_dir}.md). Todo cambio de este capítulo baja por ella (`02·F23`).")
        io.open(archivo, "w", encoding="utf-8", newline="").write("\n".join(lineas))

reemplazar(os.path.join(EPDIR, "epica.md"),
           "| [HU-014](HU-014-la-guia-de-entrada-del-estandar/HU-014-la-guia-de-entrada-del-estandar.md) | «Título» | «Prioridad» | «Estimación» |",
           "| [HU-014](HU-014-la-guia-de-entrada-del-estandar/HU-014-la-guia-de-entrada-del-estandar.md) | La guía de entrada del estándar | Should | S |")
reemplazar(os.path.join(EPDIR, "README.md"),
           "](HU-014-la-guia-de-entrada-del-estandar/) | Historia de usuario: «…» |",
           "](HU-014-la-guia-de-entrada-del-estandar/) | Historia de usuario: la guía de entrada del estándar |")
print("creadas:", len(creadas), creadas[:1], "...", creadas[-1:])
