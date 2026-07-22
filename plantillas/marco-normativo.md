# Marco normativo del proyecto  ·  `[CAPA 3 · plantilla]`

> Plantilla de capa 3. Cópiala al proyecto y **llénala** con lo que aplica a *este* cliente. El agente la lee para cumplir por construcción (base `16` · CQ1/CQ2). Borra los ejemplos y deja solo lo real. Lo que no aplique, márcalo "No aplica" con una razón (no lo borres sin dejar rastro).

---

## 1. Para quién se construye

- **Cliente / organización:** `<nombre>`
- **Sector:** `<público | salud | financiero | educación | privado | ...>`
- **Jurisdicción:** `<país / región>`
- **Naturaleza de los datos:** `<personales | sensibles | financieros | clínicos | públicos | ...>`

## 2. Leyes y normas obligatorias

| Norma / Ley | Qué exige | Controles en el sistema | ¿Dónde se implementa? |
|---|---|---|---|
| _(ej.)_ Protección de datos personales | Consentimiento, minimización, derecho de borrado | Base `12` · PR1/PR5 | `<módulo/servicio>` |
| _(ej.)_ Documento de política CONPES aplicable | `<lo que exige>` | `<control>` | `<dónde>` |
| ... | ... | ... | ... |

## 3. Frameworks de gobierno y seguridad adoptados

| Framework | Para qué se adopta | Alcance / nivel de exigencia |
|---|---|---|
| _(ej.)_ ISO/IEC 27001 | Gestión de seguridad de la información | `<controles aplicables al desarrollo>` |
| _(ej.)_ COBIT | Gobierno de TI | `<procesos que tocan el desarrollo>` |
| _(ej.)_ OWASP ASVS | Seguridad de software (nivel N) | Ya es default en base `16` · CQ3 |
| _(ej.)_ ISO/IEC 25010 | Atributos de calidad a exigir | Ya es default en base `16` · CQ4 |
| ... | ... | ... |

## 4. Accesibilidad

- **Estándar exigido:** `<WCAG 2.1 A / AA / AAA | ninguno>`
- **Base legal (si aplica):** `<norma que lo obliga>`
- **Alcance:** `<qué pantallas/flujos deben cumplir>`

## 5. Requisitos que NO se pueden cumplir hoy (y por qué)

> Transparencia: si un control exigido no se puede implementar (limitación técnica, de datos legacy, de presupuesto), se declara aquí con su razón y su plan, en vez de simular que se cumple (base `16` · CQ2).

| Requisito | Por qué no se cumple aún | Plan / mitigación |
|---|---|---|
| ... | ... | ... |

## 6. Decisiones y excepciones

> Decisiones de cumplimiento ya tomadas y blindadas contra reinterpretación (fecha, motivo, quién lo pidió).

- `<fecha>` — `<decisión>` — `<motivo>`
