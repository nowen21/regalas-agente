# Análisis «N»: «el problema que trata el análisis, en una frase»

> Plantilla del análisis. Al llenarla se reemplazan los `«…»` y se borran las notas como esta, menos la tabla de reglas.
>
> Solo entra lo que ayuda a entender qué pasa y a tomar una decisión. Lo que no aporta a decidir no se escribe.
>
> Todo título y todo enlace dicen de qué se trata, nunca solo un número: «Pendiente: lo que se construye se aparta de lo aprobado», no «pendiente 103».
>
> Este análisis se redacta aplicando estas reglas.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Un análisis aprobado no se reescribe. Si al ejecutar el plan aparece un hallazgo, se abre `analisis-«N+1»`.md, que trata solo lo que falló y sus implicaciones sobre lo ya hecho.

---

## Hallazgo

> Copia del hallazgo que origina el análisis, tal como estaba al empezar. No se toca nunca: si el análisis concluye que el hallazgo debe cambiar, el cambio se hace en el resumen de la sesión donde nació.

«copia del hallazgo»

## Pendiente

> Copia del pendiente, tal como estaba al empezar. No se toca nunca: los cambios se hacen en el archivo del pendiente.

«copia del pendiente»

---

## Conversación

> La escribe el enganche en tiempo real, turno por turno, desde la transcripción de la sesión. No se escribe a mano.

> acá termina la conversación

---

## Lo acordado

> Se escribe en el mismo turno en que el usuario acepta algo: un punto por cada decisión, con su tema y el turno de la conversación donde se acordó.

1. «tema»: «lo que se decidió» (turno «N»).

Siguen abiertas: «pregunta sin decidir, o "ninguna"».

---

## Lo que aportó cada parte

> Cada subsección es obligatoria: el validador detiene el cierre si falta una. Lo que aportan el usuario y Claude queda en la conversación y no se repite aquí.

### Cimiento: las reglas que aplican y las que chocan

«reglas que aplican, con su ID; reglas que chocan y en qué punto de lo que se tiene que hacer se resuelven»

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| «tema» | «qué existe, qué funciona y qué falta, con la ruta» |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| «señal, lección o análisis anterior» | «si confirma, contradice o muestra un intento que falló, y qué punto de «Lo acordado» lo recoge» |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | «tipo de versión según `20·M10`, y si aplica `02·F22`» |
| Normas y leyes | «cuáles aplican, o "ninguna"» |
| Herramientas | «qué condiciona lo que se va a construir» |

---

## Propuesta final: hallazgo y pendiente V«N+1», épica y HU

> Así quedan el hallazgo y el pendiente según lo que concluyó el análisis, con solo los campos que les corresponden. Antes de aprobar, se pasan a los originales con la conversación prendida, para que el cambio quede en el análisis: el hallazgo en el resumen de su sesión y el pendiente en su archivo. Después de aprobar no se cambia nada.

### Hallazgo V«N+1». «título que diga de qué se trata»

| Campo | Valor |
|---|---|
| Qué pasó | «…» |
| Por qué importa | «…» |

### Pendiente V«N+1». «título que diga de qué se trata»

| Campo | Valor |
|---|---|
| De dónde sale | «el hallazgo V«N+1», con su título» |
| El problema | «…» |
| Por qué importa | «…» |

### Épica y HU que salen del análisis

«épica: título que diga su resultado, o la épica existente a la que se suman las HU»

| HU | Título | Parte del problema que resuelve | Puntos de lo que se tiene que hacer |
|---|---|---|---|
| «n» | «título que diga su resultado» | «la frase del problema que le toca a esta HU; es lo que va en su contexto» | «números» |

«orden en que se construyen y por qué»

## Lecciones aprendidas

> Salen de lo que funcionó, para repetirlo, y de lo que falló, para no repetirlo. El texto completo vive en el almacén de señales; aquí va el enlace.

| # | Lección | Tipo | Señal |
|---|---|---|---|
| 1 | «lección» | Funcionó / Falló | «enlace a la señal» |

## Lo que se tiene que hacer

> Cada fila se convierte en un criterio de aceptación de una HU, y «Pasó a» dice cuál. Ninguna fila queda sin destino. «Sale de» cita el punto de «Lo acordado» de donde sale; lo que no tenga punto acordado no entra.

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | «qué hay que hacer» | «número» | «épica y HU, con su título y su enlace» |
