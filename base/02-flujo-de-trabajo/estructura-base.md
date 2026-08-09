# F13 · Estructura base del proyecto   ·   `[CAPA 2 · OBLIGATORIA]`

> **Anexo de la regla F13** — solo el árbol. La regla (alcance, quién crea qué y regla de cumplimiento) vive en [`F13`](reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md), aquí **no se duplica**.
>
> **Línea base oficial** de organización. Separa dos mundos: el **código del usuario** (cuya carpeta crea el instalador, pero cuyo contenido el agente **nunca** toca) y el **espacio de trabajo del agente** (que el agente crea y gestiona, al lado del código).

---

## Estructura

```
<raíz>/
├── proyectos/                        # CÓDIGO FUENTE del/los proyecto(s) · la carpeta la crea el instalador,
│   │                                 #   el CONTENIDO es del USUARIO y el agente NO lo toca
│   └── «nombre-proyecto»/            #   ej. agro-system/   ·   o rni-back/ + rni-front/
│       └── «código fuente»           #   estructura propia del stack (Laravel, Django, Angular…)
│
├── CLAUDE.md                         # setup del agente · LOCAL (gitignored) — lo genera el instalador
├── .agente/                          # config del agente · LOCAL (gitignored) — la crea el instalador
│   ├── stack.md                      #   incluye "Estructura del proyecto" (dónde vive el código)
│   ├── dominio.md
│   ├── mapeo-nombres.md
│   ├── marco-normativo.md
│   ├── reglas-proyecto.md            #   si aplica (DOC10)
│   └── mapa-dependencias.md          #   mapa vivo (DOC9)
│
├── prompts/                          # briefs de entrada · <slug>-brief.md — la crea el instalador
│
└── documentacion/                    # VERSIONADO — lo que produce el flujo — la crea el instalador
    ├── modulos.md                    #   catálogo de módulos (DOC13)
    ├── adr/                          #   ADR-NNN-<slug>.md (transversal)
    ├── analisis/                     #   <modulo>-YYYY-MM-DD-cierre.md (DOC8, transversal)
    └── epicas/                       #   Épica → HU → Fase · jerarquía y ruta: fuente única 02·F12 (F12.11 · F12.13)
```

> La organización interna de `epicas/` (jerarquía **Épica → HU → Fase** en [`F12.11`](reglas/F12-relacion-y-nomenclatura-de-fases.md), anidamiento y ruta física en [`F12.13`](reglas/F12-relacion-y-nomenclatura-de-fases.md), nomenclatura en [`F12.6`](reglas/F12-relacion-y-nomenclatura-de-fases.md)) es la **fuente única [`02·F12`](reglas/F12-relacion-y-nomenclatura-de-fases.md)** — aquí **no se duplica**.
