# 16 · Cumplimiento y calidad  ·  `[CAPA 2 · opt-in]`

> **Historia dueña del texto:** [EP-001 HU-029](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-029-el-capitulo-16-cumplimiento-y-calidad/HU-029-el-capitulo-16-cumplimiento-y-calidad.md). Todo cambio de este capítulo baja por ella ([`02·F23`](02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md)).

El agente construye de modo que **el desarrollo cumpla** el marco que aplica al cliente: leyes, normas y frameworks. Cumplimiento **por construcción**, no auditoría aparte. Opt-in: la capa 3 activa esta sección y declara el marco concreto.

Esta sección tiene dos mitades: lo **universal** (capa 2, siempre aplica) y el **gancho a capa 3** (lo que cada proyecto declara).

---

**Parte A, lo universal**, que aplica siempre que el capítulo esté activo.

## CQ1 · Sabe para quién construyes

Al iniciar un proyecto, identifica **sector**, **jurisdicción** y **marco aplicable** (lo declara la capa 3). Sin eso, no asumas requisitos ni los inventes: pregúntalos o pide la plantilla de marco normativo.

```
INCORRECTO: construir sin saber si es sector público, salud o privado
CORRECTO:   "¿Qué sector y jurisdicción? ¿Qué normas/frameworks aplican?" antes de decidir
```


---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v36.0.2**, el **2026-08-30**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.**

**Fila 3 · la regla nombra sector y jurisdicción, y eso no es dominio.** No dice cuál: dice que hay que averiguarlo antes de construir. El capítulo entero es `opt-in` y la capa 3 declara el marco concreto, que es lo que [`20·M3`](20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md) protege.

**Fila 17 es `N/A`:** la regla no declara excepción.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

---

## CQ2 · Cumple por construcción y déjalo trazable

Traduce cada control del marco a una **decisión concreta** (esquema, validación, permiso, cifrado, log, retención) y verifícalo junto con la trazabilidad especificación→implementación ([`13·DOC3`](13-documentacion/reglas/DOC3-verifica-la-trazabilidad-especificacion-implementacion-antes-de-cerrar.md)). Si un requisito **no se puede cumplir**, avísalo — no lo omitas en silencio.

```
INCORRECTO: implementar y dar por hecho que "cumple"
CORRECTO:   mapear cada requisito del marco a un control real + evidencia en la trazabilidad
```


---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v36.0.2**, el **2026-08-30**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.**

**Fila 14 · declara su dependencia enlazada** con la regla de trazabilidad, que es la que le da el sitio donde queda la evidencia.

**Fila 17 es `N/A`:** la regla no declara excepción.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

---

## CQ3 · Seguridad de software por defecto (OWASP)

Toma **OWASP** (ASVS + Top 10) como línea base de controles de código seguro. Es la instancia concreta de la seguridad de `04`: inyección, autenticación, control de acceso, exposición de datos, configuración segura.

```
INCORRECTO: revisar la seguridad "a ojo", con lo que cada quien recuerde
CORRECTO:   recorrer los controles de OWASP y decir cuáles aplican y dónde quedan
```


---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v36.0.2**, el **2026-08-30**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.**

**Fila 12 · el ejemplo se agregó el 2026-08-30, al aplicarle el checklist por primera vez.** La regla llevaba meses publicada sin él, y nadie lo vio porque el analizador no la reconocía como regla.

**Fila 5 · nombrar OWASP no es nombrar tecnología.** [`20·M3`](20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md) prohíbe atar la norma a un lenguaje, un framework o un motor; un catálogo de controles de seguridad no es ninguna de las tres, y el capítulo existe justamente para nombrar marcos.

**Fila 17 es `N/A`:** la regla no declara excepción.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

---

## CQ4 · Atributos de calidad como checklist (ISO/IEC 25010)

Evalúa y prioriza contra los atributos de **ISO/IEC 25010**: funcionalidad, fiabilidad, seguridad, usabilidad, eficiencia de desempeño, mantenibilidad, compatibilidad, portabilidad. Sirve para decidir qué mejorar y para justificar trade-offs.

```
INCORRECTO: "está listo" sin mirar mantenibilidad ni fiabilidad
CORRECTO:   revisar el cambio contra los atributos de 25010 y nombrar los trade-offs
```


---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v36.0.2**, el **2026-08-30**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.**

**Fila 5 · nombrar ISO/IEC 25010 no es nombrar tecnología**, por lo mismo que `CQ3` con OWASP: es un marco de atributos, no una herramienta.

**Fila 17 es `N/A`:** la regla no declara excepción.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

---

## Lo que declara cada proyecto

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
