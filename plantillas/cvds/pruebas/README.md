# Pruebas: ¿cumple, y con qué evidencia?   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito con qué se comprueba cada criterio de aceptación, qué se ejecutó y qué dio. El estado de una funcionalidad lo fija la prueba corrida, no la lectura del código: mientras no haya prueba, lo honesto es «sin verificar».

> Todo documento creado con esta plantilla se redacta aplicando estas reglas. Esta nota se borra al llenarla.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Plantilla. Se llena junto con el plan de trabajo, no después. La envergadura ajusta la profundidad, nunca la existencia: la sección sin materia se llena con `N/A porque «…»`, nunca se borra. Reemplaza los `«…»` y borra esta caja.

> **Cómo se redacta lo que va dentro de cada `«…»`.** En el idioma del proyecto ([`01·C8`](«RUTA-ESTANDAR»/base/01-conducta.md#c8--habla-el-idioma-del-proyecto)) y en la menor cantidad de palabras con la que se entienda ([`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md)): el dato primero, sin repaso, sin justificación que nadie pidió y sin paso a paso. Lo que no cabe se escribe en su documento y se enlaza. Si en una celda va más de una cosa, se escribe como lista: una por renglón, con `<br>` entre ellas y viñeta al empezar. Separarlas con puntos medios en un solo párrafo las vuelve ilegibles.

> Se escribe desde la propuesta, no desde lo que ya está construido. Lo que existe sirve para saber qué se conserva y qué se rehace, nunca para fijar el alcance. La prueba: si se borra mentalmente lo construido y el documento sigue siendo cierto, está bien escrito.

**Estado: «BORRADOR / EN CURSO / CERRADA»** («AAAA-MM-DD»).

## 1. Qué entra a esta etapa

> Son los criterios de entrada: lo que tiene que estar listo para que probar tenga sentido. Empezar sin esto produce defectos de ambiente y no del producto, y quema la confianza en las pruebas.

| Qué se recibe | De dónde viene | ¿Listo? |
|---|---|---|
| Criterios de aceptación, uno por historia | Análisis | «…» |
| Requisitos no funcionales con su forma de comprobarse | Análisis | «…» |
| Lo construido, con sus pruebas unitarias pasando | Implementación | «…» |
| Ambiente de pruebas y datos cargados | Implementación | «…» |

## 2. Qué se prueba, y en qué nivel

> Asigna a cada criterio de aceptación los casos que lo cubren, su nivel y su tipo. Los cuatro niveles miran cosas distintas, y saltarse uno se paga en el siguiente: **unitaria** (una pieza sola), **integración** (dos piezas hablando), **sistema** (todo junto, contra los requisitos), **aceptación** (el usuario, con sus datos, decidiendo si lo recibe).

| Criterio de aceptación | Casos que lo cubren | Nivel | Tipo | Automática |
|---|---|---|---|---|
| «HU-001, criterio 1» | «…» | «Unitaria / Integración / Sistema / Aceptación» | «Funcional / Rendimiento / Seguridad / Usabilidad / Compatibilidad» | «Sí / No, y por qué» |

## 3. Cómo se diseñan los casos

> Dice de dónde se derivan los casos de prueba, que no se inventan. El camino que funciona no basta.

| Qué se cubre | Cómo |
|---|---|
| El camino que funciona | «Un caso por flujo principal del caso de uso» |
| Los bordes | «El primero, el último, el vacío, el máximo, el que sobrepasa» |
| Lo inválido | «Qué pasa con el dato que no debería llegar» |
| Los permisos | «Cada actor intentando lo que no le corresponde» |

## 4. Lo que también se prueba: que NO pase

> Lista lo que el sistema debe rechazar y lo que no debe reportar de más, con cómo se provoca cada caso. Una comprobación que solo mira el caso feliz aprueba cualquier cosa, y una que reprueba de más se apaga a la semana, y entonces no queda nada.

| Qué NO debe pasar | Cómo se provoca | Qué se espera |
|---|---|---|
| «…» | «…» | «…» |

## 5. Con qué datos y en qué ambiente

> Dice con qué datos y en qué ambiente se prueba, y quién puede tocarlo.

| Qué se define | Cómo queda |
|---|---|
| Datos de prueba | «De dónde salen, y cómo se sabe que no son datos reales de personas» |
| Ambiente | «Dónde se corre, y en qué se parece y en qué no a producción» |
| Qué se limpia después | «…» |
| Quién puede tocar ese ambiente | «…» |

## 6. La evidencia

> Registra lo que se ejecutó, cuándo y dónde quedó su salida, en vez de un resumen escrito de memoria. Sin evidencia, un veredicto es una opinión.

| Qué se ejecutó | Cuándo | Dónde queda la salida |
|---|---|---|
| «…» | «AAAA-MM-DD» | «…» |

## 7. El veredicto, criterio por criterio

> Da el resultado de cada criterio de aceptación con su evidencia y, si falló, qué se hace.

| Criterio | Resultado | Evidencia | Si falló, qué se hace |
|---|---|---|---|
| «HU-001, criterio 1» | «Cumple / No cumple / Sin verificar» | «…» | «…» |

## 8. Los defectos, y qué se hace con cada uno

> Registra cada defecto con su gravedad, quién lo corrige y su estado. La gravedad la fija el daño a quien usa, no la incomodidad de arreglarlo, y el defecto corregido vuelve a probarse con el caso que lo encontró, no con uno parecido. Si no apareció ninguno, se escribe `N/A porque «…»`.

| # | Qué falla | Gravedad | ¿Bloquea la entrega? | Quién lo corrige | Estado |
|---|---|---|---|---|---|
| 1 | «…» | «Impide trabajar / Estorba pero hay cómo seguir / Molesta» | «Sí / No» | «…» | «Abierto / Corregido / Vuelto a probar / Aceptado como deuda» |

## 9. Que lo arreglado no rompa lo que servía

> Dice qué se vuelve a correr entero antes de entregar. Cada corrección puede romper algo que ya funcionaba, y esta es la red que lo detecta.

| Qué se vuelve a correr | Cuándo | Cuánto demora |
|---|---|---|
| «…» | «Antes de cada entrega» | «…» |

## 10. Qué quedó sin probar

> Lista lo que no se probó, por qué y qué riesgo se acepta. Si se probó todo, se escribe `N/A porque «…»`.

| Qué no se probó | Por qué | Qué riesgo se acepta |
|---|---|---|
| «…» | «…» | «…» |

## 11. La prueba del usuario

> Registra la prueba de aceptación: el usuario ejecuta sus propios casos con sus propios datos y firma. La última palabra es suya.

| Quién prueba | Qué casos | Cuándo | Resultado |
|---|---|---|---|
| «…» | «…» | «AAAA-MM-DD» | «Acepta / Acepta con reparos / Rechaza» |

## 12. Los entregables de esta etapa, y a quién van

> Lista los documentos que produce la etapa y a quién se entregan.

| Documento | Molde | Va a | Estado |
|---|---|---|---|
| Plan de pruebas | [plantillas/ciclo-vida-proyectos/08-plan-pruebas.md](../../ciclo-vida-proyectos/08-plan-pruebas.md) | Cliente, junto con el plan de trabajo | «…» |
| Resultado de pruebas | [plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md](../../ciclo-vida-proyectos/09-resultado-pruebas.md) | Cliente | «…» |
| Cierre de la funcionalidad | [plantillas/ciclo-vida-proyectos/11-funcionalidad-implementada.md](../../ciclo-vida-proyectos/11-funcionalidad-implementada.md) | Cliente | «…» |
| Registro de defectos | Sección 8 de este documento | Equipo | «…» |
| Acta de aceptación del usuario | Sección 11 de este documento | Cliente, se firma | «…» |

## 13. Las puertas de esta etapa

> Son los criterios de salida: lo que no se hace hasta que se cumpla algo, con la regla que lo exige.

| Qué no se puede hacer | Hasta que | Regla |
|---|---|---|
| Aprobar un plan de trabajo | venga con su plan de pruebas | [`02·F4`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md) |
| Declarar algo terminado | tenga prueba corrida con su evidencia | «…» |
| Desplegar | ningún defecto que bloquee siga abierto | «…» |
| Desplegar | cada criterio de aceptación tenga veredicto | «…» |

## 14. La decisión de cierre

> Registra si la etapa pasa a despliegue, quién lo decidió y qué defecto se acepta como deuda.

**«Se pasa a despliegue / No se pasa»**, decidido por «quién» el «AAAA-MM-DD».

«Qué quedó sin verificar y por qué, y qué defecto se acepta como deuda con su dueño.»
