# Planificación Proyecto: «Nombre del proyecto»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito, antes de comprometer trabajo, por qué vale la pena hacer el proyecto, por qué camino y con qué: el problema, los límites del alcance, los recursos, el cronograma, los riesgos, quién responde por cada cosa y cómo se le informa a quién. Es la única etapa que puede terminar en «no se hace», y ese también es un resultado que se escribe acá.

> Todo documento creado con esta plantilla se redacta aplicando estas reglas. Esta nota se borra al llenarla.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |

> Plantilla. Se llena al abrir el proyecto y se congela al aprobarse; lo que cambie después se cambia con nota de qué cambió y por qué. La envergadura ajusta la profundidad, nunca la existencia: la sección sin materia se llena con `N/A porque «…»`, nunca se borra. Reemplaza los `«…»` y borra esta caja.

> **Cómo se redacta lo que va dentro de cada `«…»`.** En el idioma del proyecto ([`01·C8`](«RUTA-ESTANDAR»/base/01-conducta.md#c8--habla-el-idioma-del-proyecto)) y en la menor extensión con la que se entienda ([`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md)): el dato primero, sin repaso, sin justificación no pedida y sin paso a paso. Lo que no cabe no se recorta: se escribe en su archivo y se enlaza. Un hueco de una tabla que necesita un párrafo es señal de que el detalle va en otro documento. Si en una celda va más de una cosa, se escribe como lista: una por renglón, con `<br>` entre ellas y viñeta al empezar. Separarlas con puntos medios en un solo párrafo las vuelve ilegibles.

> Se escribe desde la propuesta, no desde lo que ya está construido. Lo que existe sirve para saber qué se conserva y qué se rehace, nunca para fijar el alcance. La prueba: si se borra mentalmente lo construido y el documento sigue siendo cierto, está bien escrito.

**Estado: «BORRADOR / APROBADO»** («AAAA-MM-DD», aprobado por «quién»).

## 1. El problema y el objetivo

> Describe la necesidad que justifica el proyecto, dicha desde lo que le duele a quien pide y antes de saber con qué se resuelve. Nombrar acá módulos, archivos, herramientas o decisiones de diseño es adelantar la etapa 3.
>
> Si el proyecto ya está andando, se reconstruye al revés: por cada cosa que hoy existe se pregunta *qué pasaba cuando no existía*, y esa respuesta es la necesidad. Esa lista intermedia es borrador de trabajo y no se entrega. Si al borrar mentalmente lo construido el texto deja de entenderse, está describiendo el producto.

| Pregunta | Respuesta |
|---|---|
| **¿Cuál es el problema?** | «El problema en dos o tres frases, con las palabras de quien lo sufre, no con las de quien lo va a programar.» |
| **¿A quién le pasa?** | «Quién lo sufre, con nombre o con papel: quien paga, quien usa, quien opera. Un problema sin alguien concreto que lo padezca no sostiene un proyecto.» |
| **¿Cada cuánto pasa?** | «Cuántas veces al día, a la semana o al año. Es lo que separa la molestia del costo.» |
| **¿A qué escala?** | «Sobre cuánto: cuántos casos, cuántas personas, cuánto volumen. Un problema que le pasa a uno y otro que le pasa a mil piden proyectos distintos.» |
| **¿Cómo se resuelve hoy?** | «El arreglo con el que se está saliendo del paso: a mano, en una hoja de cálculo, pidiéndoselo a alguien. Ese arreglo es el competidor real del proyecto, y si lo nuevo no lo supera, nadie lo adopta.» |
| **¿Qué se intentó antes?** | «Los intentos anteriores, uno por uno. Si no hubo ninguno, se escribe `N/A porque nunca se intentó`, que también es un dato: nadie lo ha visto lo bastante grave como para intentarlo.» |
| **¿Por qué no funcionó?** | «En qué falló cada intento. Es lo que evita repetirlo con otro nombre, y suele ser el dato más caro de la etapa.» |
| **¿Qué le cuesta hoy?** | «En qué se paga: horas, dinero, retrabajo, errores que llegan al cliente. Con número si lo hay; si no lo hay, se dice que no se ha medido.» |
| **¿Qué pasa si no se hace nada?** | «Qué ocurre si todo sigue igual: el costo se repite, crece, o alguien se va. Es lo que vuelve urgente al proyecto, y la alternativa de no hacer nada del estudio de factibilidad.» |
| **¿Qué necesita que pase?** | «El resultado esperado, dicho sin herramienta: "que lo acordado una vez siga valiendo", no "que haya un archivo de reglas".» |

**Objetivo principal**

> Uno solo, en infinitivo y en una frase: qué se va a construir, qué resuelve y para qué (`Desarrollar...`, `Implementar...`, `Construir...`). Es el único lugar de esta sección donde se nombra la solución: el problema se escribe sin ella.
>
> Los diez objetivos específicos lo desglosan: si alguno no aporta a este, sobra; si el conjunto dice más que este, el principal se quedó corto.

«Desarrollar «qué sistema» que «qué resuelve», para «qué resultado para quien pide»»

**Objetivos específicos**

> Se escriben diez, y cada uno abre con un verbo en infinitivo. Salen de *¿Qué necesita que pase?* y no del producto: `Conservar...`, `Evitar...`, `Reducir...`, `Garantizar...`, nunca `Un sistema que...`.
>
> Los diez son el piso: los tres primeros salen solos y son los generales, y llegar al décimo obliga a bajar de la generalidad y sacar lo que de otro modo aparece recién en la etapa 4, cuando ya cuesta. Si el proyecto de verdad no da para diez, las filas que sobren se llenan con `N/A porque «…»`.
>
> **En qué se nota** es el resultado observable, no el mecanismo ni el estado de lo construido: eso vive en las secciones 11 y 17. **Para quién** es la persona concreta que lo nota (quien paga, quien usa, quien opera), y separarla evita el objetivo que no le sirve a nadie en particular. Si alguna de las dos no se puede llenar, se trata de una función y va al inventario.

| # | Objetivo | En qué se nota | Para quién |
|---|---|---|---|
| 1 | «Infinitivo + qué + para qué» | «El hecho observable» | «Quien lo nota» |
| 2 | «…» | «…» | «…» |
| 3 | «…» | «…» | «…» |
| 4 | «…» | «…» | «…» |
| 5 | «…» | «…» | «…» |
| 6 | «…» | «…» | «…» |
| 7 | «…» | «…» | «…» |
| 8 | «…» | «…» | «…» |
| 9 | «…» | «…» | «…» |
| 10 | «…» | «…» | «…» |

## 2. El alcance

> Es la frontera del proyecto: todo lo que el sistema va a hacer y todo lo que no. La lista de funciones va al inventario; acá va hasta dónde llega el compromiso. Se acuerda antes de construir, porque después cada agregado parece pequeño y ninguno lo es.
>
> Se agregan todas las opciones posibles, sin omitir ninguna por obvia: lo que no queda escrito acá se discute después, cuando ya se construyó en contra. Cada celda se escribe corta, como pide la nota de redacción del comienzo, y enumerar mucho y escribir corto son las dos mitades de esta tabla.

| ¿Qué se incluye? | ¿Qué queda fuera? | ¿Por qué queda fuera? |
|---|---|---|
| «…» | «…» | «…» |
| «…» | «…» | «…» |

> La columna del medio es la que evita el crecimiento descontrolado de funciones. Un alcance sin exclusiones escritas no delimitó nada.

## 3. Supuestos

> Un supuesto es un hecho que el plan necesita cierto y nadie comprobó; si alguno falla, el plan cambia. Es lo más barato de escribir y lo más caro de omitir: un supuesto falso explica la mayoría de los proyectos que se pasan de plazo.

| # | Se da por cierto que | ¿Qué pasa si resulta falso? | ¿Quién lo confirma? |
|---|---|---|---|
| 1 | «…» | «…» | «…» |
| 2 | «…» | «…» | «…» |

## 4. Restricciones

> Una restricción es un límite que el proyecto no puede mover: viene dado por alguien de afuera o por una decisión ya tomada. La que no se escribe se descubre cuando ya se construyó en contra de ella.

| Tipo | Restricción | De dónde viene |
|---|---|---|
| Plazo | «…» | «…» |
| Presupuesto | «…» | «…» |
| Tecnología o plataforma | «…» | «…» |
| Formato de los entregables | «¿En qué formato se escriben y en cuál se entregan?» | «…» |
| Normativa o licencias | «…» | «…» |

## 5. Dependencias de terceros

> Una dependencia es algo que el proyecto necesita y no puede producir: lo entrega alguien que no está en el equipo, y por eso no se le puede exigir la fecha. Si no hay ninguna, se escribe `N/A porque «…»`.

| ¿De quién o de qué? | ¿Qué se necesita? | ¿Para cuándo? | ¿Qué se hace si no llega? |
|---|---|---|---|
| «…» | «…» | «…» | «…» |

## 6. Viabilidad, en cuatro frentes

> Dice si el proyecto se puede hacer con lo que hay: capacidad, dinero, tiempo y permiso legal. Si conviene hacerlo se decide en la sección 19. Un frente que bloquea detiene el proyecto aunque los otros tres den bien.

| Frente | Pregunta | Respuesta | ¿Bloquea? |
|---|---|---|---|
| Técnica | ¿Existe la tecnología y el conocimiento para hacerlo? | «Sí / No, y por qué» | «Sí / No» |
| Económica | ¿Los beneficios justifican el costo? | «El costo-beneficio o el retorno esperado, en una línea» | «…» |
| Operativa | ¿La organización y los usuarios lo van a adoptar? | «…» | «…» |
| Legal | ¿Cumple normativas, licencias y protección de datos? | «…» | «…» |

**Recomendación: «continuar / continuar con condiciones / no hacerlo».** «El porqué en dos líneas, apoyado en las filas de arriba.»

El análisis largo, con las alternativas descartadas, vive en [plantillas/ciclo-vida-proyectos/12-estudio-factibilidad.md](../../ciclo-vida-proyectos/12-estudio-factibilidad.md); acá va solo su conclusión.

## 7. Recursos

> Lista las personas y los medios que el proyecto necesita, y si ya se tienen.

**Personas.**

| Perfil | Cuántas | Dedicación | Quién |
|---|---|---|---|
| «…» | «…» | ««N» % / «N» h semanales» | «Nombre o "por asignar"» |

**Infraestructura, herramientas y licencias.**

| Qué | Para qué | Costo | ¿Ya se tiene? |
|---|---|---|---|
| «…» | «…» | «…» | «Sí / No» |

## 8. Presupuesto

> Dice cuánto cuesta el proyecto por rubro y cómo se estimó cada cifra.

| Rubro | Costo estimado | Cómo se estimó |
|---|---|---|
| Personal | «…» | «…» |
| Infraestructura | «…» | «…» |
| Herramientas y licencias | «…» | «…» |
| Reserva para imprevistos | «…» | ««N» % del total» |
| **Total** | **«…»** | |

## 9. Estimación de esfuerzo

> Dice cuánto trabajo lleva cada paquete del desglose y con qué técnica se estimó. Se estima como si se construyera desde cero: lo ya hecho no se descuenta acá, y si el proyecto viene andando, el avance se dice en el cronograma. Una estimación que solo cuenta lo que falta no sirve para comparar contra nada, y comparar es su único uso.

**Técnica usada: «juicio experto / puntos de historia / puntos función / COCOMO».**

| Paquete del desglose | Esfuerzo | Supuesto del que depende |
|---|---|---|
| «1 · el mismo código de la sección 10» | ««N» jornadas / horas-persona / puntos» | «…» |
| «…» | «…» | «…» |

**Total: ««N»».** «Y con qué margen: una estimación sin margen declarado se lee como promesa.»

## 10. Desglose del trabajo (WBS/EDT)

> Parte el proyecto en paquetes de trabajo, una fila por paquete, hasta el nivel en que se pueda estimar sin adivinar. El desglose sale de los objetivos y no de lo que ya existe: en un proyecto andando, listar lo hecho y llamarlo plan hace que el cronograma deje de planear y pase a narrar. La columna «Objetivos que atiende» es el control: un paquete que no atiende a ninguno sobra, y un objetivo que no aparece en ningún paquete no se va a cumplir solo.

| Código | Paquete de trabajo | Objetivos que atiende | Depende de | Duración | Responsable |
|---|---|---|---|---|---|
| 1 | «…» | «1, 4» | — | «…» | «…» |
| 1.1 | «…» | «…» | «1» | «…» | «…» |

## 11. Cronograma

> Pone fechas al desglose de la sección 10: cuándo se alcanza cada hito y cuál es la ruta crítica. Sin desglose no hay cronograma, solo fechas puestas sobre nada.

**Hitos y fecha de entrega.**

| Hito | Fecha | Qué tiene que estar listo para darlo por cumplido |
|---|---|---|
| «…» | «AAAA-MM-DD» | «…» |

**Ruta crítica: «…».** «Qué se atrasa si eso se atrasa.»

> La ruta crítica es la cadena de tareas que no admite atraso: si una se corre un día, la entrega se corre un día. Lo que no está en ella tiene holgura.

## 12. Modelo de desarrollo

> Dice con qué modelo de desarrollo se trabaja y qué del proyecto lo justifica.

**Se usa «cascada / iterativo / espiral / Scrum u otro marco ágil»**, porque «los requisitos son estables o no, el cliente puede revisar cada N semanas o no, la entrega es una o es incremental».

## 13. Riesgos

> Registra lo que puede salir mal, qué tan probable es, cuánto daña, quién lo vigila y qué se hace antes y después de que ocurra.

| # | Riesgo | Probabilidad | Impacto | Responsable | Mitigación | Qué se hace si ocurre |
|---|---|---|---|---|---|---|
| 1 | «…» | «Alta / Media / Baja» | «Alto / Medio / Bajo» | «…» | «…» | «…» |
| 2 | «…» | «…» | «…» | «…» | «…» | «…» |

## 14. Roles y responsabilidades

> Dice, por actividad, quién hace, quién responde, a quién se consulta y a quién se informa. Hacer y responder van en columnas distintas porque no son lo mismo: si una fila tiene dos responsables, no tiene ninguno.

| Actividad o entregable | Quién lo hace | Quién responde | A quién se consulta | A quién se informa |
|---|---|---|---|---|
| «…» | «…» | «…» | «…» | «…» |

**Quién aprueba las entregas: «…».**

## 15. Interesados y comunicación

> Lista a quién le importa el proyecto, cuánto pesa su opinión y qué información recibe.

| Interesado | Qué papel tiene | Influencia | Qué recibe | Cada cuánto | En qué formato |
|---|---|---|---|---|---|
| «Quien paga» | «…» | «Alta / Media / Baja» | «…» | «…» | «…» |
| «Quien usa» | «…» | «…» | «…» | «…» | «…» |
| «Quien aprueba» | «…» | «…» | «…» | «…» | «…» |

## 16. Plan de calidad

> Dice qué se le exige al producto en conjunto, cómo se mide y desde qué umbral se acepta.

| Qué se exige | Cómo se mide | Umbral para aceptar |
|---|---|---|
| «…» | «…» | «…» |

Los criterios de aceptación por funcionalidad no van acá: viven en [plantillas/ciclo-vida-proyectos/04-HU.md](../../ciclo-vida-proyectos/04-HU.md) y su comprobación en [plantillas/ciclo-vida-proyectos/08-plan-pruebas.md](../../ciclo-vida-proyectos/08-plan-pruebas.md).

## 17. Los entregables de esta etapa, y a quién van

> Lista los documentos que produce la etapa, una fila por documento. La columna del molde dice dónde se escribe; la de destino, quién lo firma.

| Documento | Molde | Va a | Estado |
|---|---|---|---|
| Acta de constitución (*project charter*) | [plantillas/ciclo-vida-proyectos/13-acta-de-constitucion-y-plan-de-proyecto.md](../../ciclo-vida-proyectos/13-acta-de-constitucion-y-plan-de-proyecto.md), sección 1 | Cliente o patrocinador — **se firma** | «Pendiente / Listo / N/A porque «…»» |
| Estudio de viabilidad | [plantillas/ciclo-vida-proyectos/12-estudio-factibilidad.md](../../ciclo-vida-proyectos/12-estudio-factibilidad.md) | Cliente — **se firma** | «…» |
| Visión y alcance | [plantillas/ciclo-vida-proyectos/01-planteamiento.md](../../ciclo-vida-proyectos/01-planteamiento.md), secciones 1 a 4 | Cliente — **se firma** | «…» |
| Plan de proyecto | [plantillas/ciclo-vida-proyectos/13-acta-de-constitucion-y-plan-de-proyecto.md](../../ciclo-vida-proyectos/13-acta-de-constitucion-y-plan-de-proyecto.md), secciones 2 a 5 | Cliente y equipo | «…» |
| Cronograma con hitos y fecha | Sección 11 de este documento | Cliente — **se firma** | «…» |
| Presupuesto | Sección 8 de este documento | Cliente — **se firma** | «…» |
| Desglose del trabajo (WBS/EDT) | Sección 10 de este documento | Equipo interno | «…» |
| Registro de riesgos | Sección 13 de este documento | Equipo interno | «…» |
| Roles y matriz de responsabilidades | Sección 14 de este documento | Equipo interno | «…» |
| Estimación de esfuerzo | Sección 9 de este documento | Equipo interno | «…» |
| Plan de calidad | Sección 16 de este documento | Equipo interno | «…» |
| Plan de comunicaciones | Sección 15 de este documento | Ambos — compromete reportes al cliente | «…» |

## 18. Cambios después de la aprobación

> La línea base solo sirve si se sabe cuándo se movió y por qué. Desde que la etapa se aprueba, lo que cambie se anota acá, una fila por cambio aunque parezca menor, y no se corrige en silencio. Si el cambio deja sin efecto algo ya firmado, se dice: un acta o un estudio que autorizaban otra cosa no siguen valiendo porque nadie los haya tocado. Mientras no haya cambios, se escribe `N/A porque «…»`.

| Fecha | Qué cambió | Por qué | Quién lo pidió |
|---|---|---|---|
| «AAAA-MM-DD» | «…» | «…» | «…» |

## 19. La decisión de la etapa

> Registra si el proyecto se hace, se hace con condiciones o no se hace, y quién lo decidió.

**«Se hace / Se hace con estas condiciones / No se hace»**, decidido por «quién» el «AAAA-MM-DD».

«El porqué en dos líneas. Si se hace con condiciones, cuáles y quién las levanta. Si no se hace, qué tendría que cambiar para volver a mirarlo.»
