# Cierre de análisis · «módulo» «tema»   ·   `[CAPA 3]`

> Todo documento creado con esta plantilla se redacta aplicando estas reglas. Esta nota se borra al llenarla.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |

> Consolida un análisis persistido ([`13·DOC8`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC8-cierra-todo-analisis-con-su-tabla-de-decisiones.md)): qué se preguntó, qué se decidió, qué quedó. Se crea al terminar un análisis: el `analisis/<...>.md` de [`13·DOC6`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), una exploración o una auditoría. Ruta canónica: `analisis/<modulo>-YYYY-MM-DD-cierre.md`.
>
> Al llenarla se reemplazan los `«…»` y se borran todas las notas como esta.

## 0. Referencia

> Identifica el análisis que se cierra, su módulo, la fecha de cierre y el prompt vivo donde queda registrado.

| Campo | Valor |
|---|---|
| **Análisis original** | «enlace al `analisis/<...>.md`» |
| **Módulo** | «…» |
| **Fecha de cierre** | AAAA-MM-DD |
| **Prompt vivo del módulo** | «enlace» |

## 1. Tabla de trazabilidad · pregunta/hallazgo → decisión

> Tiene una fila por cada pregunta abierta o hallazgo del análisis, con la decisión tomada, su estado y el gap que generó. Si no generó gap, la última columna dice «Ninguno».

| Pregunta / hallazgo | Decisión tomada | Estado | Gap generado (si aplica) |
|---|---|---|---|
| (frase original) | (respuesta del usuario o decisión de diseño) | resuelta / diferida / descartada | `«gap-N»` → §Qué falta del prompt vivo |

## 2. Cierre

> Son los registros que dejan el análisis cerrado y enlazado desde donde se consulta.

- En el análisis original, al inicio del `analisis/<...>.md`, se agrega este banner:
  `> Cerrado en <ruta-de-este-cierre> — consultar allí el estado vigente de cada decisión.`
- En el prompt vivo, bajo su `## Historial de análisis`, se agrega esta línea:
  `YYYY-MM-DD · <tema> · <ruta-a-este-cierre>`.
- Cada `«gap-N»` generado queda en la §Qué falta del prompt vivo, listo para una fase futura ([`13·DOC12`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md) ORIGEN).
