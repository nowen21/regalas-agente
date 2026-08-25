# Decisiones de arquitectura   ·   `[CAPA 3]`

**Para qué sirve este documento.** Las decisiones que cuestan caro de revertir, cada una con las alternativas que se descartaron y por qué. Sin las alternativas, una decisión no se puede defender ni revisar después: solo se puede obedecer o romper.

> Plantilla. Se llena durante el diseño, y cada decisión se agrega el día en que se toma, no al final. La sección sin materia se llena con `N/A porque «…»`, nunca se borra. Reemplaza los `«…»` y borra esta caja.

> **Cómo se redacta lo que va dentro de cada `«…»`.** En el idioma del proyecto ([`01·C8`](«RUTA-ESTANDAR»/base/01-conducta.md#c8--habla-el-idioma-del-proyecto)) y en la menor cantidad de palabras con la que se entienda ([`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md)).

**Cómo se citan.** Cada decisión lleva un número que empieza por `DA`, de **decisión de arquitectura**: `DA-01`, `DA-02`. Ese número se usa para nombrarla en cualquier otro documento, y no se le da a otra decisión aunque esta se cambie después.

**Estado: «BORRADOR / APROBADO»** («AAAA-MM-DD», aprobado por «quién»).

---

## Decisiones

### «La decisión, dicha como afirmación, no como tema»

| Campo | Valor |
|---|---|
| **Identificador** | «`DA-01`, y el siguiente libre para la que venga» |
| **Qué se decide** | «Qué se hace, en una frase que no deje lugar a interpretación» |
| **Qué exige** | «Los requisitos que la obligan, por su identificador» |
| **Alternativas descartadas** | «Una por renglón, con `<br>` entre ellas: "• tal cosa, porque tal razón". Una decisión con una sola alternativa no evaluó, justificó» |
| **Por qué esta** | «Qué gana esta que no ganaban las otras» |
| **Qué se pierde** | «Lo que se sacrifica al elegirla. Si no se pierde nada, no era una decisión difícil» |
| **Cuándo se revisaría** | «Qué tendría que pasar para volver a mirarla. Sin esto, la decisión se vuelve dogma» |

### «…»

«Se repite la ficha por cada decisión.»

---

## Lo que tienen en común

«Qué se repite entre ellas: la misma alternativa descartada por la misma razón, o la misma restricción del proyecto asomando en varias. Si no se repite nada, se escribe `N/A porque cada una responde a algo distinto`.»

**La que más puede cambiar es «…»:** «por qué. Su ficha dice qué la haría cambiar.»
