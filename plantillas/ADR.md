# ADR-000 · «Título de la decisión»   ·   `[CAPA 3]`

> Todo documento creado con esta plantilla se redacta aplicando estas reglas. Esta nota se borra al llenarla.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |

> **Architecture Decision Record**: registra una decisión de arquitectura **no obvia** y su porqué ([`13·DOC2`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md)), para que no se pierda ni se vuelva a discutir. La produce la estación de diseño (`disenar-arquitectura`) y la referencia la épica (`epica.md §10.2`). Se guarda en `documentacion/adr/ADR-<NNN>-<slug>.md`. Reemplaza los `«…»` y borra esta caja.

## 1. Identificación

> Identifica la decisión y la ubica en el proyecto. Si no reemplaza a otro ADR, o ninguno la reemplaza, esa fila dice «Ninguno».

| Campo | Valor |
|---|---|
| **ID** | ADR-000 |
| **Título** | «…» |
| **Estado** | Propuesta / **Aceptada** / Reemplazada / Deprecada |
| **Fecha** | AAAA-MM-DD |
| **Decisores** | «quién decide» |
| **Épica / Módulo** | «a qué pertenece» |
| **Reemplaza a** | «ADR-XXX» (si aplica) |
| **Reemplazada por** | «ADR-XXX» (si esta quedó obsoleta) |

## 2. Contexto y problema

> Explica por qué hubo que tomar una decisión, antes de hablar de las opciones.

«La situación que obliga a decidir: qué restricción, requisito o fuerza técnica está en juego. En lenguaje neutro, sin adelantar la solución.»

## 3. Opciones consideradas

> Son las alternativas que se evaluaron, cada una con lo que tiene a favor y en contra. Se ponen las que hubo, sean dos o más.

| Opción | A favor | En contra |
|---|---|---|
| **A — «…»** | «…» | «…» |
| **B — «…»** | «…» | «…» |
| **C — «…»** | «…» | «…» |

## 4. Decisión

> Dice qué opción se eligió y por qué.

**Se elige: «Opción X».**

«Por qué esta y no las otras: el criterio que inclinó la balanza (costo, riesgo, simplicidad, reversibilidad, encaje con el resto del sistema).»

## 5. Consecuencias

> Es lo que la decisión trae consigo, lo bueno y lo malo, para que quien la herede sepa qué aceptó.

- Positivas: «qué mejora o habilita».
- Negativas / costo: «qué se sacrifica o se vuelve más difícil».
- Riesgos y mitigación: «qué puede salir mal y cómo se acota».
- Reversibilidad: «qué tan caro es dar marcha atrás si fue un error».

## 6. Enlaces

> Une el ADR con el resto de la documentación. Si no afecta a otro documento, «Afecta a» dice «Ninguno».

- Señal asociada ([`13·DOC5`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)): «id o enlace en la memoria, tipo `decisión`».
- Afecta a: «módulos, especificaciones o ADR relacionados».
