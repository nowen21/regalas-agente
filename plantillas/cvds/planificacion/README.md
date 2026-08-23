# Planificación Proyecto: «Nombre del proyecto»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito, antes de comprometer trabajo, **por qué vale la pena hacer el proyecto, por qué camino y con qué**: el problema, los límites del alcance, los recursos, el cronograma, los riesgos, quién responde por cada cosa y cómo se le informa a quién. Es la única etapa que puede terminar en «no se hace», y ese también es un resultado que se escribe acá.

> Plantilla. Se llena al abrir el proyecto y se congela al aprobarse; lo que cambie después se cambia con nota de qué cambió y por qué. La envergadura ajusta la profundidad, nunca la existencia: la sección sin materia se llena con `N/A porque «…»`, nunca se borra. Reemplaza los `«…»` y borra esta caja.

> **Cómo se redacta lo que va dentro de cada `«…»`.** En el idioma del proyecto ([`01·C8`](«RUTA-ESTANDAR»/base/01-conducta.md#c8--habla-el-idioma-del-proyecto)) y en la menor extensión con la que se entienda ([`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md)): el dato primero, sin repaso, sin justificación no pedida y sin paso a paso. Lo que no cabe no se recorta: se escribe en su archivo y se enlaza. Un hueco de una tabla que necesita un párrafo es señal de que el detalle va en otro documento.

**Estado: «BORRADOR / APROBADO»** («AAAA-MM-DD», aprobado por «quién»).

---

## 1. El problema y el objetivo

> **Se escribe desde la necesidad, no desde lo construido.** Va lo que le duele a quien pide, antes de saber con qué se resuelve. Nombrar acá módulos, archivos, herramientas o decisiones de diseño es adelantar la etapa 3.
>
> **Si el proyecto ya está andando, se reconstruye al revés:** por cada cosa que hoy existe se pregunta *qué pasaba cuando no existía*, y esa respuesta es la necesidad. Esa lista intermedia es borrador de trabajo: no se entrega.
>
> **La prueba:** si se borra mentalmente todo lo construido y el texto sigue siendo cierto y entendible, está bien escrito. Si deja de entenderse, está describiendo el producto.

**¿Cuál es el problema?** 

«El problema en dos o tres frases, con las palabras de quien lo sufre, no con las de quien lo va a programar.»

**¿Qué le cuesta hoy?** 

«En qué se paga: horas, dinero, retrabajo, errores que llegan al cliente. Con número si lo hay; si no lo hay, se dice que no se ha medido.»

**¿Qué necesita que pase?** 

«El resultado esperado, dicho sin herramienta: "que lo acordado una vez siga valiendo", no "que haya un archivo de reglas".»

**Objetivo principal**

> **Uno solo, en infinitivo y en una frase: qué se va a construir, qué resuelve y para qué.** `Desarrollar…`, `Implementar…`, `Construir…`. **Es el único lugar de esta sección donde se nombra la solución**: el problema se escribe sin ella, pero el objetivo principal declara qué se va a hacer.
>
> Los diez de abajo lo desglosan: si alguno no aporta a este, sobra; si el conjunto dice más que este, falta él.

«Desarrollar «qué sistema» que «qué resuelve», para «qué resultado para quien pide»»

**Objetivos**

> **Se escriben diez, y cada uno abre con un verbo en infinitivo.** Salen de *¿qué necesita que pase?*, no del producto: `Conservar…`, `Evitar…`, `Reducir…`, `Garantizar…`, nunca `Un sistema que…`.
>
> **Los diez son el piso, no un adorno:** los tres primeros salen solos y son los generales; llegar al décimo es lo que obliga a bajar de la generalidad y sacar lo que de otro modo aparece recién en la etapa 4, cuando ya cuesta. Si el proyecto de verdad no da para diez, las filas que sobren se llenan con `N/A porque «…»`.
>
> **En qué se nota** es el resultado observable, no el mecanismo ni el estado de lo construido: eso vive en las secciones 8 y 14. **Para quién** es la persona concreta que lo nota (quien paga, quien usa, quien opera), y separarla evita el objetivo que no le sirve a nadie en particular. **Si no se puede llenar alguna de las dos, no es un objetivo: es una función, y va al inventario.**

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

| Entra | Queda fuera | Por qué queda fuera |
|---|---|---|
| «…» | «…» | «…» |
| «…» | «…» | «…» |

> La columna del medio es la que evita el crecimiento descontrolado de funciones. Un alcance sin exclusiones escritas no delimitó nada.

El alcance ítem por ítem no va acá: va al inventario, [plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md](../../ciclo-vida-proyectos/02-inventario-funcionalidades.md), y **aprobado por el usuario** es la puerta de las épicas ([`02·F26`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F26-el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-epicas.md)).

## 3. Supuestos, restricciones y dependencias

> **Lo que se está dando por cierto sin haberlo comprobado, y lo que no se puede cambiar.** Es la sección que más barato sale escribir y más caro sale omitir: un supuesto que resultó falso explica la mayoría de los proyectos que se pasan de plazo, y una restricción no escrita se descubre cuando ya se construyó en contra de ella.

**Supuestos.** Se dan por ciertos, y si alguno falla el plan cambia.

| # | Se da por cierto que | Qué pasa si resulta falso | Quién lo confirma |
|---|---|---|---|
| 1 | «…» | «…» | «…» |
| 2 | «…» | «…» | «…» |

**Restricciones.** No se negocian: vienen dadas.

| Tipo | Restricción | De dónde viene |
|---|---|---|
| Plazo | «…» | «…» |
| Presupuesto | «…» | «…» |
| Tecnología o plataforma | «…» | «…» |
| Formato de los entregables | «En qué formato se escriben y en cuál se entregan» | «…» |
| Normativa o licencias | «…» | «…» |

**Dependencias de terceros.** Lo que el proyecto necesita de alguien que no está en el equipo.

| De quién o de qué | Qué se necesita | Para cuándo | Qué se hace si no llega |
|---|---|---|---|
| «…» | «…» | «…» | «…» |

## 4. Viabilidad, en cuatro frentes

| Frente | Pregunta | Respuesta | ¿Bloquea? |
|---|---|---|---|
| Técnica | ¿Existe la tecnología y el conocimiento para hacerlo? | «Sí / No, y por qué» | «Sí / No» |
| Económica | ¿Los beneficios justifican el costo? | «El costo-beneficio o el retorno esperado, en una línea» | «…» |
| Operativa | ¿La organización y los usuarios lo van a adoptar? | «…» | «…» |
| Legal | ¿Cumple normativas, licencias y protección de datos? | «…» | «…» |

**Recomendación: «continuar / continuar con condiciones / no hacerlo».** «El porqué en dos líneas, apoyado en las filas de arriba.»

El análisis largo, con las alternativas descartadas, vive en [plantillas/ciclo-vida-proyectos/12-estudio-factibilidad.md](../../ciclo-vida-proyectos/12-estudio-factibilidad.md); acá va solo su conclusión.

## 5. Recursos

**Personas.**

| Perfil | Cuántas | Dedicación | Quién |
|---|---|---|---|
| «…» | «…» | ««N» % / «N» h semanales» | «Nombre o "por asignar"» |

**Infraestructura, herramientas y licencias.**

| Qué | Para qué | Costo | ¿Ya se tiene? |
|---|---|---|---|
| «…» | «…» | «…» | «Sí / No» |

## 6. Presupuesto

| Rubro | Costo estimado | Cómo se estimó |
|---|---|---|
| Personal | «…» | «…» |
| Infraestructura | «…» | «…» |
| Herramientas y licencias | «…» | «…» |
| Reserva para imprevistos | «…» | ««N» % del total» |
| **Total** | **«…»** | |

## 7. Estimación de esfuerzo

**Técnica usada: «juicio experto / puntos de historia / puntos función / COCOMO».**

| Bloque de trabajo | Esfuerzo | Supuesto del que depende |
|---|---|---|
| «…» | ««N» horas-persona / «N» puntos» | «…» |

## 8. Cronograma y desglose del trabajo

**Desglose (WBS/EDT).** Una fila por paquete de trabajo; el nivel de detalle baja hasta donde se pueda estimar sin adivinar.

| Código | Paquete de trabajo | Depende de | Duración | Responsable |
|---|---|---|---|---|
| 1 | «…» | — | «…» | «…» |
| 1.1 | «…» | «1» | «…» | «…» |

**Hitos y fecha de entrega.**

| Hito | Fecha | Qué tiene que estar listo para darlo por cumplido |
|---|---|---|
| «…» | «AAAA-MM-DD» | «…» |

**Ruta crítica: «…».** «Qué se atrasa si eso se atrasa.»

## 9. Modelo de desarrollo

**Se usa «cascada / iterativo / espiral / Scrum u otro marco ágil»**, porque «los requisitos son estables o no, el cliente puede revisar cada N semanas o no, la entrega es una o es incremental».

## 10. Riesgos

| # | Riesgo | Probabilidad | Impacto | Responsable | Mitigación | Qué se hace si ocurre |
|---|---|---|---|---|---|---|
| 1 | «…» | «Alta / Media / Baja» | «Alto / Medio / Bajo» | «…» | «…» | «…» |
| 2 | «…» | «…» | «…» | «…» | «…» | «…» |

## 11. Roles y responsabilidades

| Actividad o entregable | Quién lo hace | Quién responde | A quién se consulta | A quién se informa |
|---|---|---|---|---|
| «…» | «…» | «…» | «…» | «…» |

**Quién aprueba las entregas: «…».**

## 12. Interesados y comunicación

| Interesado | Qué papel tiene | Influencia | Qué recibe | Cada cuánto | En qué formato |
|---|---|---|---|---|---|
| «Quien paga» | «…» | «Alta / Media / Baja» | «…» | «…» | «…» |
| «Quien usa» | «…» | «…» | «…» | «…» | «…» |
| «Quien aprueba» | «…» | «…» | «…» | «…» | «…» |

## 13. Plan de calidad

| Qué se exige | Cómo se mide | Umbral para aceptar |
|---|---|---|
| «…» | «…» | «…» |

Los criterios de aceptación por funcionalidad no van acá: viven en [plantillas/ciclo-vida-proyectos/04-HU.md](../../ciclo-vida-proyectos/04-HU.md) y su comprobación en [plantillas/ciclo-vida-proyectos/08-plan-pruebas.md](../../ciclo-vida-proyectos/08-plan-pruebas.md).

## 14. Los entregables de esta etapa, y a quién van

Una fila por documento. La columna del molde dice dónde se escribe; la de destino, quién lo firma.

| Documento | Molde | Va a | Estado |
|---|---|---|---|
| Acta de constitución (*project charter*) | [plantillas/ciclo-vida-proyectos/13-acta-de-constitucion-y-plan-de-proyecto.md](../../ciclo-vida-proyectos/13-acta-de-constitucion-y-plan-de-proyecto.md), sección 1 | Cliente o patrocinador — **se firma** | «Pendiente / Listo / N/A porque «…»» |
| Estudio de viabilidad | [plantillas/ciclo-vida-proyectos/12-estudio-factibilidad.md](../../ciclo-vida-proyectos/12-estudio-factibilidad.md) | Cliente — **se firma** | «…» |
| Visión y alcance | [plantillas/ciclo-vida-proyectos/01-planteamiento.md](../../ciclo-vida-proyectos/01-planteamiento.md), secciones 1 a 4 | Cliente — **se firma** | «…» |
| Plan de proyecto | [plantillas/ciclo-vida-proyectos/13-acta-de-constitucion-y-plan-de-proyecto.md](../../ciclo-vida-proyectos/13-acta-de-constitucion-y-plan-de-proyecto.md), secciones 2 a 5 | Cliente y equipo | «…» |
| Cronograma con hitos y fecha | Sección 8 de este documento | Cliente — **se firma** | «…» |
| Presupuesto | Sección 6 de este documento | Cliente — **se firma** | «…» |
| Desglose del trabajo (WBS/EDT) | Sección 8 de este documento | Equipo interno | «…» |
| Registro de riesgos | Sección 10 de este documento | Equipo interno | «…» |
| Roles y matriz de responsabilidades | Sección 11 de este documento | Equipo interno | «…» |
| Estimación de esfuerzo | Sección 7 de este documento | Equipo interno | «…» |
| Plan de calidad | Sección 13 de este documento | Equipo interno | «…» |
| Plan de comunicaciones | Sección 12 de este documento | Ambos — compromete reportes al cliente | «…» |

## 15. La decisión de la etapa

**«Se hace / Se hace con estas condiciones / No se hace»**, decidido por «quién» el «AAAA-MM-DD».

«El porqué en dos líneas. Si se hace con condiciones, cuáles y quién las levanta. Si no se hace, qué tendría que cambiar para volver a mirarlo.»
