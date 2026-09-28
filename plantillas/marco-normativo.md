# Marco normativo del proyecto  ·  `[CAPA 3 · plantilla]`

> Todo documento creado con esta plantilla se redacta aplicando estas reglas. Esta nota se borra al llenarla.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |

> Plantilla de capa 3. Se copia al proyecto y se llena con lo que aplica a este cliente. El agente la lee para cumplir por construcción (`16·CQ1`, `16·CQ2`). Se borran los ejemplos y se deja solo lo real; se reemplazan los `«…»` y se borran las notas como esta. Lo que no aplique se escribe `N/A` con su razón, no se borra ([`13·DOC21`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC21-escribe-n-a-en-la-seccion-que-no-aplica.md)).

## 1. Para quién se construye

> Identifica al cliente y la clase de datos que maneja el sistema, que es lo que decide qué normas le aplican.

- **Cliente / organización:** `«nombre»`
- **Sector:** `«público | salud | financiero | educación | privado | ...»`
- **Jurisdicción:** `«país / región»`
- **Naturaleza de los datos:** `«personales | sensibles | financieros | clínicos | públicos | ...»`

## 2. Leyes y normas obligatorias

> Son las leyes y normas que obligan al proyecto, cada una con el control que la cumple y el lugar del sistema donde está implementado.

| Norma / Ley | Qué exige | Controles en el sistema | ¿Dónde se implementa? |
|---|---|---|---|
| _(ej.)_ Protección de datos personales | Consentimiento, minimización, derecho de borrado | Base `12` · PR1/PR5 | `«módulo/servicio»` |
| _(ej.)_ Documento de política CONPES aplicable | `«lo que exige»` | `«control»` | `«dónde»` |
| ... | ... | ... | ... |

## 3. Frameworks de gobierno y seguridad adoptados

> Son los marcos de gobierno y de seguridad que el cliente adoptó, para qué se adoptó cada uno y con qué nivel de exigencia.

| Framework | Para qué se adopta | Alcance / nivel de exigencia |
|---|---|---|
| _(ej.)_ ISO/IEC 27001 | Gestión de seguridad de la información | `«controles aplicables al desarrollo»` |
| _(ej.)_ COBIT | Gobierno de TI | `«procesos que tocan el desarrollo»` |
| _(ej.)_ OWASP ASVS | Seguridad de software (nivel N) | Ya es default en base `16` · CQ3 |
| _(ej.)_ ISO/IEC 25010 | Atributos de calidad a exigir | Ya es default en base `16` · CQ4 |
| ... | ... | ... |

## 4. Accesibilidad

> Dice qué estándar de accesibilidad debe cumplir el sistema, qué norma lo obliga y qué pantallas o flujos cubre.

- **Estándar exigido:** `«WCAG 2.1 A / AA / AAA | ninguno»`
- **Base legal (si aplica):** `«norma que lo obliga»`
- **Alcance:** `«qué pantallas/flujos deben cumplir»`

## 5. Requisitos que NO se pueden cumplir hoy (y por qué)

> Son los controles exigidos que hoy no se pueden implementar, por una limitación técnica, de datos legacy o de presupuesto, cada uno con su razón y su plan. Se declaran aquí en vez de simular que se cumplen (`16·CQ2`). Si no hay, se escribe «Ninguno».

| Requisito | Por qué no se cumple aún | Plan / mitigación |
|---|---|---|
| ... | ... | ... |

## 6. Decisiones y excepciones

> Son las decisiones de cumplimiento ya tomadas y blindadas contra reinterpretación, cada una con su fecha, su motivo y quién la pidió.

- `«fecha»`: `«decisión»`, porque `«motivo»`.
