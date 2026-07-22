# 16 · Cumplimiento y calidad  ·  `[CAPA 2 · opt-in]`

El agente construye de modo que **el desarrollo cumpla** el marco que aplica al cliente: leyes, normas y frameworks. Cumplimiento **por construcción**, no auditoría aparte. Opt-in: la capa 3 activa esta sección y declara el marco concreto.

Esta sección tiene dos mitades: lo **universal** (capa 2, siempre aplica) y el **gancho a capa 3** (lo que cada proyecto declara).

---

## Parte A — Universal (capa 2)

### CQ1 · Sabe para quién construyes

Al iniciar un proyecto, identifica **sector**, **jurisdicción** y **marco aplicable** (lo declara la capa 3). Sin eso, no asumas requisitos ni los inventes: pregúntalos o pide la plantilla de marco normativo.

```
INCORRECTO: construir sin saber si es sector público, salud o privado
CORRECTO:   "¿Qué sector y jurisdicción? ¿Qué normas/frameworks aplican?" antes de decidir
```

### CQ2 · Cumple por construcción y déjalo trazable

Traduce cada control del marco a una **decisión concreta** (esquema, validación, permiso, cifrado, log, retención) y verifícalo junto con la trazabilidad spec→implementación (`13` · DOC3). Si un requisito **no se puede cumplir**, avísalo — no lo omitas en silencio.

```
INCORRECTO: implementar y dar por hecho que "cumple"
CORRECTO:   mapear cada requisito del marco a un control real + evidencia en la trazabilidad
```

### CQ3 · Seguridad de software por defecto (OWASP)

Toma **OWASP** (ASVS + Top 10) como línea base de controles de código seguro. Es la instancia concreta de la seguridad de `04`: inyección, autenticación, control de acceso, exposición de datos, configuración segura.

### CQ4 · Atributos de calidad como checklist (ISO/IEC 25010)

Evalúa y prioriza contra los atributos de **ISO/IEC 25010**: funcionalidad, fiabilidad, seguridad, usabilidad, eficiencia de desempeño, mantenibilidad, compatibilidad, portabilidad. Sirve para decidir qué mejorar y para justificar trade-offs.

```
INCORRECTO: "está listo" sin mirar mantenibilidad ni fiabilidad
CORRECTO:   revisar el cambio contra los atributos de 25010 y nombrar los trade-offs
```

---

## Parte B — Gancho a capa 3 (lo declara cada proyecto)

Lo específico **no** vive aquí; vive en la plantilla `plantillas/marco-normativo.md` que cada proyecto copia y llena. Ahí se declara:

| Qué | Ejemplos (según cliente) |
|---|---|
| **Sector y jurisdicción** | público / salud / financiero / privado · país |
| **Leyes obligatorias** | protección de datos (p. ej. Ley 1581 Habeas Data + Decreto 1377), documentos CONPES, normas sectoriales |
| **Frameworks de gobierno/seguridad** | COBIT (gobierno de TI), ISO/IEC 27001 (seguridad), ITIL (servicios), NIST CSF |
| **Gobierno digital (si público)** | MSPI de MinTIC, lineamientos de Gobierno Digital |
| **Accesibilidad exigida** | WCAG 2.1 AA (obligatoria para entidades públicas en varias jurisdicciones) |
| **Controles concretos** | por cada norma: qué exige y **dónde** se implementa en el sistema |

**Regla:** el agente **no hardcodea** el marco en el código ni asume uno por defecto. Lee el declarado en capa 3 y construye contra él. Si la capa 3 no existe todavía, CQ1 obliga a pedirla antes de tocar código sensible a cumplimiento.

---

Ver: `04` (seguridad), `12` (privacidad de datos), `13` DOC3 (trazabilidad), `08` (pruebas de los controles), y la plantilla de capa 3 `marco-normativo.md`.
