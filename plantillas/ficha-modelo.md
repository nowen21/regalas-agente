# Ficha del modelo · «NOMBRE DEL MODELO»

> Todo documento creado con esta plantilla se redacta aplicando estas reglas. Esta nota se borra al llenarla.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |

> Plantilla del capítulo opt-in [`22`](../base/22-sistemas-que-aprenden-de-datos.md). Una ficha por modelo. Los `«…»` se reemplazan y las notas como esta se borran; lo que no aplique se escribe `N/A` con el motivo (`13·DOC21`).

## Qué decide

> Dice qué pregunta responde el modelo, si solo sugiere o actúa por su cuenta, desde cuándo corre y quién responde por él.

| | |
|---|---|
| **Qué decide o sugiere** | «una frase: qué pregunta responde» |
| **Sugiere o ejecuta** | «sugiere» / «ejecuta directo»; si ejecuta, quién lo autorizó y cuándo (`IA4`) |
| **Desde cuándo está corriendo** | «AAAA-MM-DD» |
| **Persona a cargo** | «nombre», y su reemplazo: «nombre» (`IA2`) |

## Qué tan grave es que se equivoque

> Mide el daño de un error: a quién alcanza la decisión, qué pasa en concreto, en qué nivel queda y qué control le toca por ese nivel.

| | |
|---|---|
| **A quién afecta la decisión** | «a una persona identificable» / «a nadie en particular» |
| **Qué pasa si se equivoca** | «lo que ocurre en concreto» |
| **Nivel** | «bajo» / «medio» / «alto» (`IA3`) |
| **Qué control lleva por ese nivel** | «revisión humana antes de ejecutar», «medición de sesgo cada mes», ... |

## De qué datos aprendió

> Lista los conjuntos de datos con que se entrenó el modelo, una fila por conjunto (`IA7`), y dice si entre ellos hay datos de personas.

| Conjunto | De dónde salió | Periodo | Quién lo cedió | Para qué usos se puede |
|---|---|---|---|---|
| «nombre» | «qué sistema» | «desde-hasta» | «quién» | «qué permite y qué no» |

**Datos de personas:** «sí / no». Si sí, con qué base los trata el proyecto; ver [`12`](../base/12-privacidad-datos.md).

## Qué medida persigue

> Registra la medida que el modelo optimiza, qué se buscaba de verdad con ella y qué saldría mal si la persigue al extremo.

| | |
|---|---|
| **Qué se le pidió optimizar** | «la medida, escrita como se le dio» |
| **Por qué esa** | «qué se buscaba de verdad» (`IA8`) |
| **Qué comportamiento indeseado podría producir** | «lo que pasaría si la persigue al extremo» |

## Cómo se vigila

> Dice cómo se sabe, mientras el modelo corre, que sigue acertando, y quién se entera cuando deja de hacerlo.

| | |
|---|---|
| **Qué se mide para saber si sigue acertando** | «la medida, no la disponibilidad» (`IA6`) |
| **Cuánto acertaba el día que se aprobó** | «el número de referencia» |
| **Umbral que dispara aviso** | «el valor» |
| **A quién le llega el aviso** | «nombre» |

## Cuándo se vuelve a revisar

> Fija cuándo se vuelve a mirar el modelo y quién firmó la aprobación con que corre hoy.

| | |
|---|---|
| **¿Sigue aprendiendo después de aprobado?** | «sí / no» |
| **Próxima revisión** | «AAAA-MM-DD» (`IA5`) |
| **Aprobación vigente** | «quién y cuándo» |

## Si se retira

> Dice cuándo deja de usarse el modelo y qué toma sus decisiones desde entonces.

| | |
|---|---|
| **Fecha de retiro** | «AAAA-MM-DD» / «sigue en marcha» |
| **Qué decide en su lugar** | «otro modelo» / «una regla fija, cuál» / «una persona» (`IA9`) |
