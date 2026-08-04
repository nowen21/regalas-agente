# Estructura base del proyecto   ·   `[CAPA 2 · OBLIGATORIA]`

> **Línea base oficial** de organización. Su obligatoriedad y el gate de verificación los fija `02·F13`. Separa dos mundos: el **código del usuario** (que el agente **nunca** toca) y el **espacio de trabajo del agente** (que el agente crea y gestiona, al lado del código).

---

## Estructura

```
<raíz>/
├── proyectos/                        # CÓDIGO FUENTE del/los proyecto(s) · del USUARIO · el agente NO lo toca
│   └── «nombre-proyecto»/            #   ej. agro-system/   ·   o rni-back/ + rni-front/
│       └── «código fuente»           #   estructura propia del stack (Laravel, Django, Angular…)
│
├── CLAUDE.md                         # config del agente · LOCAL (gitignored)
├── .agente/                          # config del agente · LOCAL (gitignored) — la crea el agente
│   ├── stack.md                      #   incluye "Estructura del proyecto" (dónde vive el código)
│   ├── dominio.md
│   ├── mapeo-nombres.md
│   ├── marco-normativo.md
│   ├── reglas-proyecto.md            #   si aplica (DOC10)
│   └── mapa-dependencias.md          #   mapa vivo (DOC9)
│
├── prompts/                          # briefs de entrada · <slug>-brief.md — la crea el agente
│
└── documentacion/                    # VERSIONADO — lo que produce el flujo — la crea el agente
    ├── modulos.md                    #   catálogo de módulos (DOC13)
    ├── adr/                          #   ADR-NNN-<slug>.md (transversal)
    ├── analisis/                     #   <modulo>-YYYY-MM-DD-cierre.md (DOC8, transversal)
    └── epicas/                       #   Épica → HU → Fase · jerarquía y ruta: fuente única 02·F12 (F12.11 · F12.13)
```

> La organización interna de `epicas/` (jerarquía **Épica → HU → Fase** en `F12.11`, anidamiento y ruta física en `F12.13`, nomenclatura en `F12.6`) es la **fuente única `02·F12`** — aquí **no se duplica**.

---

## Qué se verifica (F13 · gate de arranque)

F13 hace **un solo chequeo**, sin leer el contenido de nada:

**¿Existe la carpeta `proyectos/`?**

- **SÍ** → el agente **crea su espacio de trabajo** (`.agente/`, `prompts/`, `documentacion/`) al lado y continúa.
- **NO** → **no cumple**: el agente **se detiene** y **orienta al usuario** para que cree `proyectos/` y coloque ahí el/los código(s) fuente. La ubicación y los nombres los decide el **usuario** (ej. RNI: `proyectos/rni-back/` + `proyectos/rni-front/`) — el agente no los asume.

---

## Regla de cumplimiento

- El agente **crea y gestiona solo su espacio** (`.agente/`, `prompts/`, `documentacion/`).
- El agente **nunca toca, modifica ni reestructura el código** dentro de `proyectos/`.
- La existencia y organización de `proyectos/` corresponde **exclusivamente al usuario**; el agente no la crea ni la asume por iniciativa propia.
