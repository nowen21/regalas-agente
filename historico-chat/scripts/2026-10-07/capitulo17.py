# -*- coding: utf-8 -*-
"""EP-028·HU-001 · Redacta la propuesta del capítulo 17: sin opt-in, I5 con la
plantilla instalada primero, e I7 «La pantalla orienta sola». Se corre desde la
raíz del repositorio: la ruta de la fase es larga para Windows."""
import glob
import io

p = glob.glob("documentacion/epicas/EP-028-*/HU-001-*/A-EP-028-HU-001-*/propuestas/17-interfaz.txt")[0]
t = io.open(p, encoding="utf-8", newline="").read()


def rep(a, b):
    global t
    assert a in t, a
    t = t.replace(a, b, 1)


rep("# 17 · Interfaz y experiencia de usuario  ·  `[CAPA 2 · opt-in]`",
    "# 17 · Interfaz y experiencia de usuario  ·  `[CAPA 2]`")
rep("**Opt-in.** Reglas agnósticas para lo que ve y usa el **usuario final**. Aplican a proyectos con interfaz "
    "(web, escritorio, móvil); un proyecto sin UI (librería, servicio backend, CLI) las omite. El framework, el "
    "sistema de diseño y el estándar de accesibilidad concretos los declara la capa 3.",
    "**Rige para todo proyecto con pantallas** (web, escritorio, móvil): reglas agnósticas para lo que ve y usa el "
    "**usuario final**. Un proyecto sin pantallas (librería, servicio backend, CLI) no tiene a qué aplicarlas. Desde "
    "el 2026-10-07 dejó de ser opt-in (análisis 1 del pendiente 137, acuerdo 2): lo que hace usable una interfaz no "
    "se apaga. La plantilla de interfaz y el estándar de accesibilidad concretos los declara la capa 3.")

i = t.index("## I5 · Consistencia con el sistema de diseño")
j = t.index("## I6", i)
seccion = t[i:j]
nueva = seccion.replace(
    "Usar los componentes y patrones que el proyecto ya tiene (el sistema de diseño lo declara la capa 3) antes de "
    "inventar unos nuevos.",
    "Antes de crear un componente, un estilo o un patrón, usar el que trae la plantilla de interfaz instalada en el "
    "proyecto, o uno que el proyecto ya tenga.")
nueva = nueva.replace(
    "CORRECTO:   los componentes que ya existen, y las acciones donde el usuario\n            ya sabe buscarlas",
    "CORRECTO:   el botón, el modal y la tabla que trae la plantilla instalada, y las\n"
    "            acciones donde el usuario ya sabe buscarlas")
nueva = nueva.replace("contra **v23.4.0**, el **2026-08-18**.",
                      "contra **v56.16.0**, el **2026-10-07**, al pedir primero la plantilla instalada (EP-028·HU-001).")
assert nueva.count("plantilla") >= 3, nueva
t = t[:i] + nueva + t[j:]

I7 = """## I7 · La pantalla orienta sola

Quien usa la pantalla encuentra cada función y sabe qué hacer en ella sin conocer cómo está armado el sistema por dentro: lo que se puede hacer se alcanza desde el menú o desde lo que lo pide, y cada pantalla dice para qué sirve y cuál es el paso siguiente.

```
INCORRECTO: la pantalla de aprobar solo se alcanza por un enlace dentro de un
            párrafo de otra pantalla, y nada avisa que hay algo por aprobar
CORRECTO:   está en el menú, el inicio avisa cuántas cosas esperan una
            decisión, y la pantalla dice qué hacer con cada una
```

**Aplica a:** cambiar-codigo

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v56.16.0**, el **2026-10-07**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** **N/A** — **14** y **15**: no declara dependencia · **16**: no tiene excepción. Fila **9**: encontrar la función y saber qué hacer en ella son la misma exigencia, orientar, vista desde la llegada y desde la pantalla. Fila **18**: «validable» es *no*: decidir si una pantalla orienta pide criterio.

**Nació el 2026-10-07** (análisis 1 del pendiente 137, acuerdo 2): el usuario no encontró cómo aprobar las propuestas de Cimiento, que es la línea base de los demás proyectos.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

---

"""
k = t.index("Ver: [`01·C8`]")
t = t[:k] + I7 + t[k:]
io.open(p, "w", encoding="utf-8", newline="").write(t)
print("listo")
