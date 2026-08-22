# 00 · Marcadores de generación automática — la lista

> **Qué es.** La lista cerrada de marcas que hacen que un texto se lea como escrito por una máquina. Es el instrumento de [`ID8`](reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md): esa regla exige que el documento no las traiga, y aquí están cuáles son.
>
> **Por qué está aquí y no en la regla.** El cuerpo de una regla va de una a cuatro líneas ([`20·M5`](../20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md)). Una lista de este tamaño se escribe como anexo del capítulo, y la regla la enlaza ([`20·M2`](../20-meta-reglas/reglas/M2-un-tema-un-capitulo-un-dueno.md)).
>
> **Cómo se usa.** Antes de entregar un documento se relee contra estas ocho secciones. Están ordenadas de la marca más fácil de ver a la más difícil de disimular. Las secciones 2 y 3 las puede contar un script; de la 4 en adelante hace falta leer.

---

## 1 · Palabras y muletillas

| Marca | Qué se escribe en su lugar |
|---|---|
| Adjetivos comodín repetidos: *robusto, integral, holístico, clave, fundamental, crucial, esencial, vital* | el dato concreto: qué es, cuánto, para qué |
| Verbos de relleno: *garantizar, permitir, fomentar, potenciar, abordar, aprovechar, implementar, optimizar, maximizar, impulsar, profundizar en* | el verbo que dice la acción real |
| Conectores de relleno: *Es importante destacar que, Cabe señalar que, Cabe resaltar, En este sentido, Por otro lado, Asimismo, Por ende, En definitiva, Sin lugar a dudas, En resumen* | empezar por la frase directa; el conector sobra casi siempre |
| La fórmula *«no solo… sino también»* | dos frases, o una con "y" |
| La construcción *«No es X, es Y»* y *«Más que X, es Y»* | decir qué es, sin la contraposición de adorno |
| Duplas de sinónimos: *claro y conciso, rápido y eficiente, sólido y confiable, simple y sencillo* | una de las dos palabras |
| Aperturas grandilocuentes: *«En un mundo cada vez más digital…»*, *«En el panorama actual…»* | la primera frase ya dice de qué trata el documento |
| *«Es decir»* y *«En otras palabras»* para repetir lo ya dicho | decirlo bien una sola vez |
| Eufemismos de oficina: *desafío* por problema, *oportunidad de mejora* por defecto, *área de trabajo* por lo que sea que se llame | la palabra que nombra la cosa |
| Subtítulos en forma de pregunta retórica: *«¿Qué significa esto?»*, *«¿Por qué importa?»* | el subtítulo que dice de qué trata la sección |
| Cierre servicial: *«Espero que esto te sirva»*, *«¡Éxitos!»*, *«Quedo atento a cualquier duda»* | terminar en el último dato. El documento no saluda |

## 2 · Puntuación y tipografía

| Marca | Qué se escribe en su lugar |
|---|---|
| La raya larga (`—`) como inciso, y muy seguido. En español es la más delatora: casi nadie la escribe a mano | coma, paréntesis, dos puntos o punto y seguido |
| Comillas curvas (`“ ”`) mezcladas con las rectas (`" "`), o angulares (`« »`) mezcladas con las dos | unas solas, las mismas en todo el documento |
| El punto medio (`·`) separando frases **en prosa** | coma o punto. **No cuenta la notación definida**: la cita `NN·ID` de [`20·M4`](../20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md), ni el separador de un **encabezado** —`09 · Control de versiones`, `Fase A · lo que hace`—, que es como esta casa nombra sus capítulos y sus fases |
| Viñetas que abren todas con negrita y dos puntos | negrita solo donde de verdad resalta algo; el resto en texto normal |
| Negrita sobre frases enteras o sobre renglones completos | negrita sobre la palabra que importa, o ninguna |
| La flecha (`→`) y el visto (`✓`) usados como viñeta en prosa | guion de lista, o la palabra que dice la relación |
| Emojis o semáforos (🔴 🟡 🟢) dentro de un documento formal | la palabra: *pendiente*, *en riesgo*, *listo* |
| Títulos Con Mayúscula En Cada Palabra, que es calco del inglés | mayúscula solo en la primera y en los nombres propios |
| Dos puntos al final de todos los encabezados | el encabezado sin nada al final |
| Separador `---` entre todas las secciones | el encabezado ya separa; la línea se usa cuando de verdad corta el documento |
| Espacio fino antes del `%` o de la unidad (*100 %*) | pegado, como se escribe a mano: *100%* |

## 3 · Marcas invisibles

No se ven leyendo: se encuentran buscando. Sobreviven a cualquier reescritura del contenido, y son las únicas que un script cuenta sin equivocarse.

| Marca | Qué se escribe en su lugar |
|---|---|
| Espacio duro (`U+00A0`) entre palabras o antes de un signo | el espacio normal del teclado |
| Caracteres de ancho cero (`U+200B`, `U+FEFF`) | se borran; no se ven y quedan pegados al copiar |
| Guion suave (`U+00AD`) dentro de una palabra | nada: la palabra entera |
| Puntos suspensivos como un solo carácter (`…`) | tres puntos seguidos |
| Semiraya (`–`) donde va un guion corriente | el guion del teclado (`-`) |
| Comillas y guiones que el editor cambia solo al escribir | revisarlos antes de entregar; el editor los mete sin avisar |

## 4 · Estructura

| Marca | Qué se escribe en su lugar |
|---|---|
| Regla de tres obsesiva: siempre tres ejemplos, tres razones, tres viñetas | los que haya. A veces son dos y a veces cinco |
| Paralelismo perfecto: todas las viñetas del mismo largo y la misma forma | cada punto del largo que pida lo que dice |
| Todas las secciones del mismo tamaño | la sección corta se queda corta |
| Todas las secciones con el mismo número de viñetas | las que tenga cada una |
| Encabezado con subtítulo explicativo en cada apartado | el encabezado solo, si ya se entiende |
| El trío *Introducción / Desarrollo / Conclusión* completo, venga o no al caso | las secciones que el asunto pida |
| Lista numerada para cosas que no llevan orden | lista con guiones |
| Resumen de cierre al final de cada sección | resumen al final del documento, si hace falta |
| Índice o resumen ejecutivo en un documento de una página | el documento, y ya |
| Cerrar siempre con *«Próximos pasos»*, haya o no pasos siguientes | la sección solo cuando hay algo que sigue |
| Tabla para lo que no la necesita | párrafo o lista |

## 5 · El español que no es de acá

El modelo escribe por defecto en un español de traducción, sin acento de ninguna parte, y cuando se le escapa un giro suele ser de España. En Colombia eso salta a la primera lectura.

| Marca | Qué se escribe en su lugar |
|---|---|
| Léxico de España: *ordenador, fichero, móvil, coche, zumo, chaval, vale, gafas* | *computador, archivo, celular, carro, jugo, muchacho, listo, lentes* |
| *Vosotros, os, vuestro*, y el imperativo en `-ad` (*mirad, tened*) | *ustedes, les, su*, y el imperativo en `-en` (*miren, tengan*) |
| Pretérito compuesto donde acá se usa el simple: *«he llegado hoy»*, *«ya lo he revisado»* | *«llegué hoy»*, *«ya lo revisé»* |
| Mezclar *usted* y *tú* en el mismo documento | uno de los dos, sostenido de principio a fin |
| Calcos del inglés: *aplicar a un cargo, remover, asumir* (por suponer), *eventualmente* (por finalmente), *en orden de* (por para) | *postularse, quitar, suponer, con el tiempo, para* |
| Español neutro sin un solo giro propio, del que nadie reconoce de dónde es | el giro que se usa acá, sin caer en jerga cerrada ni en localismo que el lector de afuera no entienda |

## 6 · Contenido y tono

| Marca | Qué se escribe en su lugar |
|---|---|
| Densidad pareja: ningún párrafo flojo, ninguno brillante, ninguna frase que se salga | el ritmo desigual que sale al escribir con cuidado. La ortografía correcta se mantiene: no se meten errores a propósito, lo que se quita es el alisado |
| Nunca decir *«no sé»*, *«no lo encontramos»*, *«esto habría que confirmarlo»* | decirlo, que además lo pide [`01·C9`](../01-conducta.md#c9--reporta-los-tropiezos) |
| Repetir la pregunta antes de responderla | responder |
| Simetría sospechosa: exactamente 5 filas, exactamente 3 problemas, ventajas y desventajas en el mismo número | los que haya, aunque queden desparejos |
| Ninguna opinión, ningún juicio discutible | la recomendación con su motivo, que es lo que se le pide a un senior ([`ID1`](reglas/ID1-trabaja-con-criterio-de-desarrollador-senior.md)) |
| Afirmar con seguridad lo que en realidad es una inferencia | marcarlo como supuesto |
| Cifras redondas sin fuente: *«mejora un 30%»*, *«el 80% de los casos»* | el número medido, con de dónde salió; o ninguno |
| Ejemplos de manual: *Juan Pérez, empresa XYZ, ejemplo.com, foo, bar* | el caso real del proyecto, o uno que se parezca a él |
| Advertencias genéricas: *«consulta a un profesional»*, *«los resultados pueden variar»* | la advertencia concreta, o ninguna |

## 7 · Metadatos del archivo

Solo cuando lo que se entrega es un archivo que guarda propiedades por dentro, como un documento de texto, una presentación o una hoja de cálculo:

| Marca | Qué se revisa |
|---|---|
| Autor y «última modificación por» que no son de quien entrega | las propiedades del archivo antes de mandarlo |
| Tiempo total de edición en 0 minutos, con número de revisión bajo | lo mismo |
| Fecha de creación y de modificación idénticas | lo mismo |
| Idioma del documento distinto del que está escrito | lo mismo |
| Fuentes o estilos que no son los del documento original | conservar los del documento que se recibió |
| Estilos que viajan pegados al copiar de otra aplicación | pegar sin formato |

## 8 · El contraste con lo escrito antes

Es la marca más difícil de disimular y la que más pesa. Quien ya leyó algo anterior de la misma persona o del mismo proyecto nota el salto: frases cortas y directas antes, párrafos largos con subordinadas encadenadas y vocabulario parejo después.

Cuando el documento continúa a otro que ya existe, se escribe en el registro de aquel.

---

## Lo que no es un marcador

- **La notación que el estándar define.** La cita `NN·ID`, los `[BLINDADA]` y `*opt-in*`, los bloques `INCORRECTO / CORRECTO`, y los ✅ ❌ N/A de la tabla de resultado que exige el [checklist del estándar](../20-meta-reglas/checklist.md). Son formato acordado, no adorno: por eso los ✅ de esa tabla no cuentan como los emojis de la sección 2.
- **La flecha en una notación.** `antes → después` en una tabla de cambios, o la salida de una herramienta que la trae. Lo que delata es usarla como viñeta en prosa.
- **La sección fija que pide una plantilla.** Si la plantilla del proyecto exige *«Próximos pasos»* o un índice, se ponen. Lo que delata es agregarlos a todo documento sin que nadie los pida.
- **El bloque de código y la salida de una herramienta.** Van tal como son.
- **La precisión técnica.** Un dato exacto no se cambia por uno vago para que suene más humano: eso choca con [`ID7`](reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md), que manda cambiar la palabra difícil por la fácil y nunca el dato.

**Si evitar una marca vuelve el texto confuso, manda [`ID7`](reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md)** y se busca otra forma de decirlo. Esta lista quita adorno; no autoriza a escribir peor.

---

## Lo que este anexo no cubre

La **norma del español**: ortografía, gramática, sintaxis y variedad del país. Escribir bien no es lo mismo que no sonar a máquina, y hoy el estándar solo fija el idioma ([`01·C8`](../01-conducta.md#c8--habla-el-idioma-del-proyecto)), no cómo se escribe en él. La sección 5 toca el tema por un solo lado: el español de ninguna parte delata al que lo escribió. Exigir norma correcta y variedad colombiana necesita su propia regla, y todavía no existe.


---

## El separador de encabezado, decidido el 2026-08-18

**Se conserva, y no como excepción: como notación definida.**

Hasta hoy la fila del punto medio decía *«separando frases o adornando títulos»*, y contaba los **1 599** que separan el número del capítulo de su nombre. Con eso, el propio índice de este anexo —`## 2 · Puntuación y tipografía`— era una marca de generación automática.

**El código ya lo tenía decidido y no lo había implementado.** El comentario de [`validadores/marcas.py`](../../validadores/marcas.py) decía, desde que se escribió: *«el punto medio que no forma parte de una cita `NN·ID` **ni de un `A · B` de encabezado**: los dos son notación definida del estándar»* — y la expresión regular solo implementaba la primera mitad.

**Dónde queda el límite.** Se exime **solo en la línea de un encabezado**. En prosa, un punto medio entre frases sigue siendo lo que este anexo llama adorno, y se cuenta.

**Lo que cambió el recuento:** de 16 477 marcas a **15 485**.

---

## Lo que se contaba y no era marca, decidido el 2026-08-22

**Mismo caso que el separador de encabezado, y por eso va aquí abajo con él.** El anexo ya decía qué se cuenta; el programa contaba de más. No se agregó ninguna excepción: se implementó lo que estas dos filas dicen desde que se escribieron.

**«La raya larga (`—`) como inciso».** Un inciso es prosa. No lo son:

| Forma | Ejemplo | Qué es |
|---|---|---|
| El título de un documento y el nombre de una sección | `# EP-000 — «Título»`, `## 1. Necesidad — en una frase` | Es como esta casa nombra sus documentos y sus secciones, igual que el `·` de los encabezados |
| Un identificador con lo que enuncia | `- [ ] **CAE-01** — «resultado observable»` | La raya separa el nombre de la cosa de la cosa, no interrumpe una frase |
| Una celda de tabla | `\| Fase 1 — MVP \|` | Una celda es un dato, no un párrafo |

**«El punto medio (`·`) separando frases en prosa».** Una celda de tabla tampoco es prosa: ahí separa dato de dato.

**«Viñetas que abren todas con negrita y dos puntos».** La marca es una uniformidad de la prosa. El rótulo de un campo de formulario no lo es, y se reconoce porque **lo que sigue a los dos puntos es el espacio por llenar**:

```
NO es marca: - **Objetivo:** «qué se logra cuando esto esté hecho»
SÍ es marca: - **Objetivo:** dejar el módulo andando antes del viernes
```

**Lo que cambió el recuento:** de **15 485** marcas a **6 440**. Los moldes del ciclo de vida pasaron de 197 a **0**, sin que ninguno pida nada distinto de lo que pedía.

**Dónde queda el límite, otra vez.** En prosa, las tres siguen contando exactamente igual. Lo que se dejó de contar es lo que nunca fue prosa.

