# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, r"C:/Users/user/AppData/Local/Temp/claude/c--Ing--Jose-ia-agente/563dc2f9-c782-46f9-af82-c9bc948b3566/scratchpad")
import p19lib as L
os.chdir(r"c:\Ing. Jose\ia\agente")

# M17: la entrada de la 30.8.3 no puede abrir con una ruta
c = L.leer("CHANGELOG.md")
mal = "**El detalle.** Pendiente [19](pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md), capítulo `02`."
bien = "**El detalle.** Es la ronda del capítulo `02` del pendiente [19](pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md)."
assert mal in c
c = c.replace(mal, bien, 1)

n = "notas/porques-recortados-al-molde.md"
s = L.leer(n)
s = s.replace("## Capítulos 18 y 19", """## Capítulos 03, 13 y 20

Diecisiete reglas más pasaban del molde con el sello en ✅. Dos no se recortaron sino que ganaron **anexo**, como `02·F12`: su detalle es una tabla y una lista que no se pueden resumir sin perderlas.

| Regla | Lo que se recortó |
|---|---|
| `03·D1` | Los ejemplos de columna en montón («listas, estructuras serializadas»), que el ejemplo de la regla ya muestra. |
| `03·D9` | «no confiando en que no pase», que era el porqué de proteger en el almacén. |
| `13·DOC5` | Que la capa 3 declara el sitio único donde viven las señales y que sin esa declaración la regla no está activada: eso es la marca *opt-in* del título y el capítulo lo explica. |
| `13·DOC7` | «si solo se escribe en uno, el conocimiento queda atrapado ahí», el porqué de exigir los dos lados. |
| `13·DOC9` | «explorar de cero lo que ya está mapeado es releer quince archivos para saber lo mismo». |
| `13·DOC10` | «cuerpo duplicado en dos sitios es un día alguien arregla uno y la contradicción queda». |
| `13·DOC11` | **La tabla de cinco columnas pasa a [anexo](../base/13-documentacion/tabla-de-trazabilidad.md)**, entera y con qué se espera de cada estado. |
| `13·DOC12` | «Sin esto aparecen fases sueltas y nadie sabe si continúan el plan o reaccionan a un hallazgo». |
| `13·DOC13` | «Sin el catálogo, la próxima sesión planifica creyendo que el sistema es solo lo que alcanzó a leer». |
| `13·DOC15` | «no de memoria ni de una copia local, que envejece», que es el porqué de leerla cada vez. |
| `13·DOC16` | «el comportamiento vive en las HU» y «toda HU pertenece a una épica, aunque agrupe una sola». |
| `13·DOC17` | «no es la foto de una fecha», el porqué de actualizarlo en el mismo cambio. |
| `13·DOC19` | La remisión a la nota de por qué esa marca y no otra, que sigue en [notas/marca-del-espacio-por-llenar.md](marca-del-espacio-por-llenar.md). |
| `13·DOC20` | «incluida la caja de instrucciones del modelo, que se borra al llenarlo». |
| `13·DOC22` | «un chat no tiene final, y lo que se deja para el final no se escribe». |
| `20·M6` | **Los seis pasos del desempate pasan a [anexo](../base/20-meta-reglas/desempate.md)**, enteros y sin reescribir. |
| `20·M16` | La remisión al procedimiento completo y a que la regla de base nace agnóstica, que ya exigen `M14` y `M3`. |

## Capítulos 18 y 19""", 1)
L.escribir(n, s)

assert L.leer("VERSION").strip() == "30.8.3"
L.escribir("VERSION", "30.9.0\n")
e = """## 30.9.0 — 2026-08-22

**MENOR** (diecisiete reglas de tres capítulos caben ya en su molde, y nacen dos anexos; nada cambia en lo que se exige).

**Ninguna regla del estándar se pasa ya del largo que ella misma fija.** Era la última deuda de la fila 10 del checklist: quince reglas de los capítulos de datos, documentación y meta-reglas decían en el sello que cabían en cuatro líneas y medían hasta el doble. Dos de ellas no se podían recortar sin perder algo, porque su contenido era una tabla y una lista de pasos: esas dos ganaron **anexo**, la misma salida que el usuario aprobó para la nomenclatura de fases.

**El detalle.** Es la ronda de los capítulos `03`, `13` y `20` del pendiente [19](pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md). Nacen [la tabla canónica de trazabilidad](base/13-documentacion/tabla-de-trazabilidad.md), que sale del cuerpo de `DOC11`, y [el orden del desempate](base/20-meta-reglas/desempate.md), que sale del de `M6` con sus seis pasos intactos. Las otras quince se recortaron dejando lo que exigen; los porqués están en [notas/porques-recortados-al-molde.md](notas/porques-recortados-al-molde.md). Con esto `validar.py metareglas` no reporta ni una falla ni un aviso de largo.

"""
c = c.replace("## 30.8.3 — 2026-08-22", e + "## 30.8.3 — 2026-08-22", 1)
L.escribir("CHANGELOG.md", c)
print("ok")
