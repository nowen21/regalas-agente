# -*- coding: utf-8 -*-
"""Fase A de la HU-003: T-06 (`13·DOC22`), T-08 (`02·F24`), T-09 (dónde vive el pendiente) y T-10 (`02·F13`
e `instalar.py`). Los sellos de checklist de las reglas que cambian se vuelven a aplicar contra 45.0.0."""
import os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))


def cambiar(relativa, pares):
    ruta = os.path.join(RAIZ, *relativa.split("/"))
    with open(ruta, encoding="utf-8") as f:
        t = f.read()
    for viejo, nuevo in pares:
        assert t.count(viejo) == 1, (relativa, viejo[:70])
        t = t.replace(viejo, nuevo)
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)


def main():
    cambiar("base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md", [
        ("Cada hallazgo dice si quedó resuelto o abierto, dónde quedó, qué trabajo dispara y con qué pregunta se retoma.",
         "Cada hallazgo dice qué pasó y por qué importa, y enlaza su pendiente; si quedó resuelto y por dónde se retoma se calculan siguiendo ese enlace."),
        ("CORRECTO:   su resumen los lista, cada uno con su estado y con la pregunta\n            que quedó viva\n",
         "CORRECTO:   su resumen los lista, cada uno con su pendiente enlazado, y el\n            programa dice cuáles siguen abiertos y por dónde se retoman\n"),
        ("contra **v30.8.0**, el **2026-08-22**.", "contra **v45.0.0**, el **2026-10-02**."),
        ("Fila 9: la exigencia es una sola, que el resumen exista y se escriba mientras pasa; qué campos lleva lo dice el modelo, no esta regla.",
         "Fila 9: la exigencia es una sola, que el resumen exista y se escriba mientras pasa; qué filas lleva cada hallazgo lo dice el modelo. Cambió en `EP-023·HU-003`, fase `A`: el hallazgo pasa a dos campos y el enlace a su pendiente (análisis 1 del pendiente 103, conclusiones 14, 34 y 35)."),
    ])
    cambiar("base/02-flujo-de-trabajo/reglas/F24-el-defecto-del-estandar-se-reporta-no-se-corrige.md", [
        ("abre un pendiente allá nombrando el proyecto de origen, otro acá diciendo que espera esa corrección, y sigue con lo suyo. El de acá queda abierto hasta que llegue el aviso de que se corrigió",
         "abre un pendiente allá que enlaza el hallazgo de acá, otro acá que enlaza el de allá, y sigue con lo suyo. El de acá cierra cuando se cumple el plan del de allá"),
        ("contra **v23.7.0**, el **2026-08-18**.", "contra **v45.0.0**, el **2026-10-02**."),
        ("**Validable a medias, y la mitad que se puede ya corre:** `validar.py pendientes` comprueba que un pendiente que declara «Proyecto de origen» lo **nombre** de verdad, en vez de dejar la casilla vacía o con el marcador sin llenar.",
         "**Validable a medias:** desde la 45.0.0 nadie escribe «Proyecto de origen»: el enlace de «De dónde sale» ya dice de qué proyecto viene, y el estado del de acá lo calcula `validadores/pendientes.py` siguiendo ese enlace (análisis 1 del pendiente 103, conclusión 36)."),
        ("Lo que **no** puede ver ningún programa de acá: si el pendiente del otro lado existe —vive en otro repositorio— ni si el aviso de vuelta llegó.",
         "Lo que **no** puede ver ningún programa de acá: el pendiente del otro lado cuando vive en un repositorio que no está en esta máquina."),
    ])
    cambiar("base/02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md", [
        ("`.agente/`, `prompts/`, `documentacion/` y `pendientes/`. Crearlas",
         "`.agente/`, `prompts/` y `documentacion/`. Crearlas"),
        ("contra **v23.12.2**, el **2026-08-18**.", "contra **v45.0.0**, el **2026-10-02**."),
        ("**Solo se sumó una carpeta a la lista: lo que la regla exige —dejarla puesta antes de trabajar— no cambió.**",
         "**Solo se sumó una carpeta a la lista: lo que la regla exige —dejarla puesta antes de trabajar— no cambió.**\n\n"
         "**Vuelto a aplicar el 2026-10-02**, porque `pendientes/` salió de la lista: cada pendiente vive en una carpeta `pendientes/` dentro de lo que lo origina, y la de la raíz queda como historia (`EP-023·HU-003`, fase `A`). Lo que la regla exige no cambió."),
    ])
    cambiar("base/20-meta-reglas/base.md", [
        ("| Mejora acordada pero **aún no hecha** | `pendientes/` |",
         "| Mejora acordada pero **aún no hecha** | Un pendiente, en la carpeta `pendientes/` de lo que lo origina (épica, HU, o el resumen del día mientras no tiene dueño); `pendientes/` de la raíz queda como historia |"),
        ("3. **La memoria** (señales) y `pendientes/`: puede estar decidido o en cola.",
         "3. **La memoria** (señales) y el índice de pendientes, `documentacion/pendientes.md`: puede estar decidido o en cola."),
    ])
    cambiar("base/glosario.md", [
        ("El documento donde queda escrita una mejora ya acordada que todavía no se hizo | Agente | `pendientes/` |",
         "El documento donde queda escrita una mejora ya acordada que todavía no se hizo | Agente | La carpeta `pendientes/` de lo que lo origina |"),
    ])
    cambiar("base/00-identidad-y-rol/acciones-y-riesgo.md", [
        ("3. **Se anota para clasificarla**, en `pendientes/`, para que la próxima vez sí esté.",
         "3. **Se anota para clasificarla**, como pendiente, para que la próxima vez sí esté."),
    ])
    cambiar("validadores/instalar.py", [
        ('CARPETAS_BASE = ["proyectos", "documentacion", "prompts", "pendientes"]',
         'CARPETAS_BASE = ["proyectos", "documentacion", "prompts"]'),
    ])


if __name__ == "__main__":
    main()
