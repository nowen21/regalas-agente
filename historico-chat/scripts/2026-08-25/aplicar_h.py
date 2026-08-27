# -*- coding: utf-8 -*-
import io

F = ("documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/"
     "HU-004-administrar-un-proyecto-conectado/"
     "H-EP-008-HU-004-un-proyecto-conectado-se-administra/")

p = F + "plan_trabajo.md"
t = io.open(p, encoding="utf-8").read()
viejo = """### 2.7 Dudas por resolver antes de escribir

| # | Duda | Por qué detiene |
|---|---|---|
| 1 | Un proyecto desconectado, ¿libera su ruta para que se pueda volver a conectar? | Si la ruta sigue tomada, desconectar **no sirve para corregir un error**, que es justo para lo que se pidió: conectar mal, desconectar, y volver a conectar bien. Si la libera, hay que decidir qué pasa con la documentación del desconectado cuando alguien conecta esa misma carpeta otra vez: ¿es el mismo proyecto que vuelve, o uno nuevo que hereda una carpeta ajena? |

**Esta no se decide sin el usuario.** Las dos salidas dejan comportamientos distintos, y la equivocada obliga a reescribir fichas ya guardadas."""
nuevo = """### 2.7 Dudas por resolver antes de escribir

| # | Duda | Cómo se resolvió |
|---|---|---|
| 1 | Un proyecto desconectado, ¿libera su ruta para que se pueda volver a conectar? | **Sí la libera, y volver a conectar esa carpeta reactiva el proyecto desconectado**: mismo identificador, misma documentación. No se crea uno nuevo. Decidido por el usuario el 2026-08-25 |

**Por qué esa y no las otras dos.** Si la ruta siguiera tomada, desconectar no serviría para lo que se pidió: conectar mal y no poder volver a conectar bien es el mismo problema con otro nombre. Y si al reconectar se creara un proyecto nuevo, la documentación del anterior quedaría huérfana: una carpeta con cosas adentro que ya no es de nadie.

**Qué agrega esta decisión al trabajo.** Reconectar deja de ser un caso de `conectar` y pasa a ser uno propio: hay que reconocer que esa ruta pertenece a un desconectado y reactivarlo. Y **la pantalla tiene que avisarlo antes de confirmar**, con un «este proyecto ya estuvo conectado, con documentación guardada», porque si el usuario quería empezar de cero con esa carpeta, va a recibir la historia vieja sin haberla pedido."""
assert viejo in t
t = t.replace(viejo, nuevo, 1)

t = t.replace("| 1 | Resolver la duda de la sección 2.7 | La respuesta, con su porqué escrito |",
              "| 1 | Resolver la duda de la sección 2.7 | ✅ Resuelta el 2026-08-25, con su porqué escrito |")
t = t.replace("| 6 | La sección de desconectados en la pantalla | Se ven, y se ve que su documentación sigue ahí |",
              "| 6 | La sección de desconectados en la pantalla | Se ven, y se ve que su documentación sigue ahí |\n"
              "| 7 | Reconectar: reactivar el desconectado en vez de crear uno nuevo | Vuelve con su identificador y su documentación, avisando antes de confirmar |")
t = t.replace("1 → 2 → 3 → 4 → 5 → 6. La tarea 1 es una puerta: decide si la tarea 2 libera la ruta o no, y eso cambia lo que se escribe en la ficha.",
              "1 → 2 → 3 → 4 → 5 → 6 → 7. La tarea 1 era la puerta y ya está pasada: su respuesta agregó la tarea 7, que no estaba en el plan original.")
t = t.replace("| Los cuatro cambios piden confirmación en una pantalla propia | Una ventana del navegador | La confirmación tiene que decir **qué va a pasar y qué no**, y eso no cabe en una ventana del navegador. En particular: que la documentación se queda |",
              "| Los cambios piden confirmación en una pantalla propia | Una ventana del navegador | La confirmación tiene que decir **qué va a pasar y qué no**, y eso no cabe en una ventana del navegador. En particular: que la documentación se queda al desconectar, y que vuelve al reconectar |\n"
              "| Reconectar una ruta de un desconectado lo reactiva | Crear un proyecto nuevo que herede esa carpeta | Decidido por el usuario el 2026-08-25. Crear uno nuevo dejaría la documentación del anterior sin dueño |")
t = t.replace("- ☐ Los desconectados se ven, y se ve que su documentación sigue ahí.",
              "- ☐ Los desconectados se ven, y se ve que su documentación sigue ahí.\n"
              "- ☐ Reconectar la ruta de un desconectado lo reactiva, con su documentación, avisando antes.")
t = t.replace("La fase cierra cuando los siete puntos de la sección 11 tengan veredicto.",
              "La fase cierra cuando los ocho puntos de la sección 11 tengan veredicto.")
io.open(p, "w", encoding="utf-8", newline="\n").write(t)

p = F + "plan_pruebas.md"
t = io.open(p, encoding="utf-8").read()
t = t.replace("| `CA-05` · que NO pase: que desconectar toque el proyecto | [CP-007](#cp-007--que-no-pase-que-desconectar-toque-la-carpeta-del-proyecto) | ☐ |",
              "| Reconectar reactiva al desconectado, con su documentación | [CP-007](#cp-007--reconectar-la-ruta-de-un-desconectado-lo-reactiva) | ☐ |\n"
              "| `CA-05` · que NO pase: que desconectar toque el proyecto | [CP-008](#cp-008--que-no-pase-que-desconectar-toque-la-carpeta-del-proyecto) | ☐ |")
t = t.replace("### CP-007 · Que NO pase: que desconectar toque la carpeta del proyecto",
"""### CP-007 · Reconectar la ruta de un desconectado lo reactiva

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que desconectar sirva de verdad para corregir un error: conectar mal, desconectar, volver a conectar bien |
| **Cómo se corre** | Se conecta un proyecto, se le guarda documentación, se desconecta, y se vuelve a conectar **la misma carpeta** |
| **Resultado esperado** | Vuelve el **mismo** proyecto: mismo identificador, misma documentación. No aparece uno nuevo, y no hay dos apuntando a esa ruta |
| **Si falla** | Si se crea uno nuevo, la documentación del anterior queda huérfana: una carpeta con cosas adentro que ya no es de nadie |

**Antes de confirmar tiene que avisar.** Si el usuario quería empezar de cero con esa carpeta, va a recibir la historia vieja sin haberla pedido. La pantalla dice que ese proyecto ya estuvo conectado y que tiene documentación guardada.

### CP-008 · Que NO pase: que desconectar toque la carpeta del proyecto""")
t = t.replace("- Los siete casos con veredicto escrito.", "- Los ocho casos con veredicto escrito.")
t = t.replace("- **Que volver a conectar un proyecto desconectado haga lo correcto.** Depende de cómo se resuelva la duda 1 del plan de trabajo, y el caso se escribe cuando esté decidida.",
              "- **Que reactivar sea siempre lo que el usuario quería.** Se prueba que reactive y que avise antes; si alguien quería empezar de cero con esa carpeta, el aviso se lo dice y la decisión sigue siendo suya.")
io.open(p, "w", encoding="utf-8", newline="\n").write(t)

p = F + "estado-fase.md"
t = io.open(p, encoding="utf-8").read()
t = t.replace("**Estación actual:** 5, aprobada. **Última puerta pasada:** 5. **No arranca todavía:** falta la respuesta a la duda.",
              "**Estación actual:** 6, ejecución. **Última puerta pasada:** 5.")
t = t.replace("| 6 | Ejecución continua | Los tres cambios y su confirmación | ☐ |",
              "| 6 | Ejecución continua | Los tres cambios, su confirmación, y reconectar | ☐ |")
t = t.replace("| 7 | Pruebas | Los siete casos con veredicto | ☐ |",
              "| 7 | Pruebas | Los ocho casos con veredicto | ☐ |")
i, j = t.index("## 2. Qué falta para avanzar"), t.index("## 3. Lo que ya se decidió")
t = t[:i] + """## 2. Qué falta para avanzar

**Nada: la fase está en ejecución.** La historia, los dos planes y la duda quedaron resueltos el 2026-08-25.

**Cómo quedó la duda.** Un proyecto desconectado **libera su ruta**, y volver a conectar esa carpeta **reactiva el proyecto desconectado**: mismo identificador, misma documentación. No se crea uno nuevo.

**Qué agregó eso al trabajo.** Una tarea y un caso de prueba que no estaban: reconectar deja de ser un caso de conectar y pasa a ser uno propio. Y la pantalla tiene que avisar antes de confirmar que ese proyecto ya estuvo conectado, porque si el usuario quería empezar de cero con esa carpeta, va a recibir la historia vieja sin pedirla.

""" + t[j:]
t = t.replace("| Qué se prueba | Siete casos, incluido uno de lo que NO debe pasar: que desconectar toque la carpeta del proyecto |",
              "| Qué se prueba | Ocho casos, incluido uno de lo que NO debe pasar: que desconectar toque la carpeta del proyecto |\n"
              "| Qué pasa al reconectar una ruta liberada | Reactiva el proyecto desconectado, con su documentación, avisando antes |")
io.open(p, "w", encoding="utf-8", newline="\n").write(t)

p = F + "README.md"
t = io.open(p, encoding="utf-8").read()
t = t.replace("**Qué la detiene.** Una duda que decide el usuario: un proyecto desconectado, ¿libera su ruta? Si no la libera, desconectar no sirve para corregir el error que motivó todo esto.",
              "**Qué la detenía.** Una duda, cerrada el 2026-08-25: un proyecto desconectado **libera su ruta**, y volver a conectar esa carpeta **reactiva el proyecto**, con su documentación. No se crea uno nuevo, porque eso dejaría la documentación del anterior sin dueño.")
t = t.replace("**Estado:** estación 5. La historia y los dos planes aprobados el 2026-08-25. No arranca hasta que se responda la duda.",
              "**Estado:** estación 6. La historia, los planes y la duda resueltos el 2026-08-25; la fase está en construcción.")
io.open(p, "w", encoding="utf-8", newline="\n").write(t)
print("ok")
