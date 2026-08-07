# F13 · Estructura base del proyecto   ·   `[CAPA 2 · OBLIGATORIA]`

> **Anexo de la regla F13** — solo el árbol. La regla (alcance, gate, mensaje de orientación y regla de cumplimiento) vive en [`base.md`](base.md), aquí **no se duplica**.
>
> **Línea base oficial** de organización. Separa dos mundos: el **código del usuario** (que el agente **nunca** toca) y el **espacio de trabajo del agente** (que el agente crea y gestiona, al lado del código).

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
