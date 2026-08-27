# -*- coding: utf-8 -*-
"""Cierra H-27 en el resumen y escribe H-29, H-30 y H-31."""
import io
import os

os.chdir(r"c:\Ing. Jose\ia\agente")
ruta = "historico-chat/resumenes/2026-08-22/sesion-6.md"
t = io.open(ruta, encoding="utf-8").read()

CIERRE_27 = [
 ("- **Qué lo soluciona:** nada todavía. Corregir solo el encabezado lo haría "
  "pasar la prueba **mintiendo**: la tabla seguiría sin sus 34 filas.",
  "- **Qué lo soluciona:** se resolvió acá, y **no corrigiendo los números**. "
  "Corregirlos habría movido la fecha del próximo desfase: el pendiente "
  "existía porque una cuenta a mano se desactualiza. Se le quitó la cuenta y "
  "la tabla, y ahora remite al comando que las calcula."),

 ("- **Qué se decidió:** no tocarlo de paso. Rehacer la tabla es trabajo "
  "aparte y se decide aparte.",
  "- **Qué se decidió:** no tocarlo de paso, y bajarlo por la cadena: "
  "`EP-004` · `HU-019` · fase `A`. **Que un programa reescribiera la tabla se "
  "descartó**: `EP-004 §10.2` dice que los programas reportan y no corrigen, "
  "y además dejaría dos copias con alguien teniendo que acordarse de "
  "correrlo."),

 ("- **Estado:** abierto.", "- **Estado:** resuelto acá."),

 ("- **Dispara:** por decidir con el usuario.",
  "- **Dispara:** la [HU-019](../../../documentacion/epicas/"
  "EP-004-comprobacion-automatica/HU-019-inventario-que-no-se-mantiene-a-mano/"
  "HU-019-inventario-que-no-se-mantiene-a-mano.md), construida y cerrada el "
  "2026-08-26."),

 ("- **Orden de resolución:** después del pendiente 87, que cambia cómo se "
  "marca lo cerrado y por lo tanto qué cuenta como completa.",
  "- **Orden de resolución:** se pensó que dependía del pendiente 87, y **no "
  "dependía**: `fases.inventario` cuenta documentos presentes, no estaciones "
  "marcadas. Encadenarlos fue un error mío, corregido al verificarlo."),

 ("- **Dónde queda:** sin resolver. La prueba lo sigue diciendo en cada "
  "corrida.",
  "- **Dónde queda:** el pendiente [48](../../../pendientes/"
  "48-inventario-hu.md), de 148 líneas a 83, y `cuenta_escrita_a_mano` en "
  "[validadores/fases.py](../../../validadores/fases.py)."),

 ("- **Cerrado en:** —\n- **Con qué se retoma:** decidir si la tabla del "
  "pendiente 48 se rehace desde el árbol o deja de mantenerse a mano.",
  "- **Cerrado en:** 2026-08-22 · sesion-6\n- **Con qué se retoma:** —"),
]

for viejo, nuevo in CIERRE_27:
    assert t.count(viejo) == 1, "H-27: no coincide -> %s" % viejo[:45]
    t = t.replace(viejo, nuevo, 1)

NUEVOS = """### H-29 · Una comprobación puede estar bien escrita y no estar conectada, y sus pruebas no lo notan

- **Qué pasó:** la fase construyó una comprobación con seis pruebas encima. Un sabotaje la **descolgó de la corrida** —le quitó la llamada desde `validar`— y **las seis siguieron en verde**. La función existía, funcionaba, y por el comando que la gente corre no salía nada.
- **Por qué importa:** las seis la llamaban **directo**, que es lo natural al escribirlas: se prueba lo que se acaba de escribir. Ninguna preguntaba si alguien la llama. Es un modo de fallar que las pruebas de la propia función **no pueden ver por construcción**.
- **Qué lo soluciona:** se resolvió acá, con una prueba que busca el aviso **a través de `validar`**, no llamando a la función.
- **Qué se decidió:** que toda comprobación nueva lleve una prueba que la busque **por el punto de entrada de verdad**. Y que la forma de descubrir que falta es **sabotear la conexión, no el cuerpo**.
- **Estado:** resuelto acá.
- **Responde a:** [EP-004](../../../documentacion/epicas/EP-004-comprobacion-automatica/epica.md) · HU-019.
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** `test_el_aviso_sale_en_la_corrida_de_fases` y la señal `S-043`.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

---

### H-30 · El guion de sabotaje dijo «suite completa en verde» sin haber corrido una sola prueba

- **Qué pasó:** el guion termina corriendo la suite entera, que es lo que dice si algo quedó saboteado. Usaba `unittest discover`, **encontró cero pruebas**, y reportó `OK`. La salida decía `Ran 0 tests in 0.000s` seguida de `OK`.
- **Por qué importa:** el veredicto que cierra una fase salía de una corrida vacía. **Cero pruebas y `OK` se ven igual**, y el guion existe justamente para no confiar en que las pruebas sirven: que él mismo mintiera es el mismo error un nivel más arriba.
- **Qué lo soluciona:** se resolvió acá: lanza el programa en vez de `discover`, y **se cae con error si la corrida final dice `Ran 0`**.
- **Qué se decidió:** que una corrida de pruebas se valida por **dos** cosas, no una: que no haya fallas **y que haya corrido algo**.
- **Estado:** resuelto acá.
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** la señal `S-044`.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

---

### H-31 · La plantilla del inventario sigue enseñando el defecto que el estándar acaba de quitarse

- **Qué pasó:** al reescribir el pendiente del inventario apareció que [`plantillas/inventario-hu.md`](../../../plantillas/inventario-hu.md) sigue describiendo la tabla a mano que acá se quitó.
- **Por qué importa:** **un proyecto que herede el estándar arma su inventario a mano**, con el mismo defecto que este repositorio acaba de dejar atrás después de que se le desfasara tres veces. El estándar estaría repartiendo lo que él mismo dejó de hacer.
- **Qué lo soluciona:** nada todavía, **y a propósito**. El plan de la fase no declara ese archivo, y `02·F8` prohíbe editar lo que el plan no declara. Además, cambiar `plantillas/` suma entrada en el `CHANGELOG` y sube `VERSION` (`20·M10`).
- **Qué se decidió:** reportarlo en vez de tocarlo de paso. Es exactamente lo que la regla pide cuando aparece un archivo nuevo a mitad de una fase: pausar y decir, no editar por iniciativa.
- **Estado:** abierto.
- **Responde a:** —
- **Dispara:** por decidir con el usuario.
- **Orden de resolución:** después de esta fase, que es la que muestra cómo queda un inventario que no se mantiene a mano.
- **Dónde queda:** el cierre de la fase §6, y el `estado-fase.md` §3.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** —
- **Con qué se retoma:** decidir si la plantilla se pone al día, sabiendo que es cambio de `plantillas/` y sube la versión del estándar.

---

"""

ancla = "## ¿Se puede cerrar la sesión?"
assert t.count(ancla) == 1
t = t.replace(ancla, NUEVOS + ancla, 1)

viejo_cierre = ("`H-27` —el inventario a mano con 34 historias de retraso— y "
                "`H-28` —el tope de ruta para quien clone en Windows— están "
                "abiertos y **ninguno tiene pendiente creado**. En los dos "
                "falta lo mismo: una decisión del usuario que es la que dice "
                "qué pendiente escribir — si la tabla del inventario se rehace "
                "desde el árbol o deja de mantenerse a mano, y cuál de las "
                "tres salidas se toma para el tope de ruta.")
nuevo_cierre = ("`H-27` **cerró**: el inventario dejó de mantenerse a mano, por "
                "la cadena completa hasta la fase `A` de la `HU-019`. Quedan "
                "dos abiertos y **ninguno tiene pendiente creado**: `H-28` —el "
                "tope de ruta para quien clone en Windows— y `H-31` —la "
                "plantilla del inventario, que sigue enseñando lo que el "
                "estándar acaba de quitarse—. En los dos falta lo mismo: una "
                "decisión del usuario que es la que dice qué pendiente "
                "escribir.")
assert t.count(viejo_cierre) == 1, "cierre no coincide"
t = t.replace(viejo_cierre, nuevo_cierre, 1)
t = t.replace("☐ · faltan los de `H-27` y `H-28` |",
              "☐ · faltan los de `H-28` y `H-31` |", 1)

io.open(ruta, "w", encoding="utf-8", newline="\n").write(t)
print("H-29, H-30 y H-31 escritos. H-27 cerrado.")
