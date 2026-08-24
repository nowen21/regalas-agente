# Pruebas: ¿cumple, y con qué evidencia?   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito con qué se comprueba cada criterio de aceptación, qué se ejecutó y qué dio. **El estado de una funcionalidad lo fija la prueba corrida, no la lectura del código:** mientras no haya prueba, lo honesto es «sin verificar».

> Plantilla. Se llena junto con el plan de trabajo, no después. La envergadura ajusta la profundidad, nunca la existencia: la sección sin materia se llena con `N/A porque «…»`, nunca se borra. Reemplaza los `«…»` y borra esta caja.

> **Cómo se redacta lo que va dentro de cada `«…»`.** En el idioma del proyecto ([`01·C8`](«RUTA-ESTANDAR»/base/01-conducta.md#c8--habla-el-idioma-del-proyecto)) y en la menor cantidad de palabras con la que se entienda ([`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md)): el dato primero, sin repaso, sin justificación que nadie pidió y sin paso a paso. Lo que no cabe se escribe en su documento y se enlaza.

**Estado: «BORRADOR / EN CURSO / CERRADA»** («AAAA-MM-DD»).

---

## 1. Qué entra a esta etapa

> **Criterios de entrada:** lo que tiene que estar listo para que probar tenga sentido. Empezar sin esto produce defectos que son de ambiente, no del producto, y queman la confianza en las pruebas.

| Qué se recibe | De dónde viene | ¿Listo? |
|---|---|---|
| Criterios de aceptación, uno por historia | Análisis | «…» |
| Requisitos no funcionales con su forma de comprobarse | Análisis | «…» |
| Lo construido, con sus pruebas unitarias pasando | Implementación | «…» |
| Ambiente de pruebas y datos cargados | Implementación | «…» |

## 2. Qué se prueba, y en qué nivel

> Los cuatro niveles miran cosas distintas, y saltarse uno se paga en el siguiente: **unitaria** (una pieza sola), **integración** (dos piezas hablando), **sistema** (todo junto, contra los requisitos), **aceptación** (el usuario, con sus datos, decidiendo si lo recibe).

| Criterio de aceptación | Casos que lo cubren | Nivel | Tipo | Automática |
|---|---|---|---|---|
| «HU-001, criterio 1» | «…» | «Unitaria / Integración / Sistema / Aceptación» | «Funcional / Rendimiento / Seguridad / Usabilidad / Compatibilidad» | «Sí / No, y por qué» |

## 3. Cómo se diseñan los casos

> Un caso no se inventa: se deriva. Y no basta el camino que funciona.

| Qué se cubre | Cómo |
|---|---|
| El camino que funciona | «Un caso por flujo principal del caso de uso» |
| Los bordes | «El primero, el último, el vacío, el máximo, el que sobrepasa» |
| Lo inválido | «Qué pasa con el dato que no debería llegar» |
| Los permisos | «Cada actor intentando lo que no le corresponde» |

## 4. Lo que también se prueba: que NO pase

> Una comprobación que solo mira el caso feliz aprueba cualquier cosa. Acá va lo que el sistema debe rechazar, y lo que no debe reportar de más: **una comprobación que reprueba de más se apaga a la semana, y entonces no queda nada.**

| Qué NO debe pasar | Cómo se provoca | Qué se espera |
|---|---|---|
| «…» | «…» | «…» |

## 5. Con qué datos y en qué ambiente

| Qué se define | Cómo queda |
|---|---|
| Datos de prueba | «De dónde salen, y cómo se sabe que no son datos reales de personas» |
| Ambiente | «Dónde se corre, y en qué se parece y en qué no a producción» |
| Qué se limpia después | «…» |
| Quién puede tocar ese ambiente | «…» |

## 6. La evidencia

> **Sin evidencia, un veredicto es una opinión.** Se guarda lo que se ejecutó y su salida, no un resumen escrito de memoria.

| Qué se ejecutó | Cuándo | Dónde queda la salida |
|---|---|---|
| «…» | «AAAA-MM-DD» | «…» |

## 7. El veredicto, criterio por criterio

| Criterio | Resultado | Evidencia | Si falló, qué se hace |
|---|---|---|---|
| «HU-001, criterio 1» | «Cumple / No cumple / Sin verificar» | «…» | «…» |

## 8. Los defectos, y qué se hace con cada uno

> La gravedad la fija el daño a quien usa, no la incomodidad de arreglarlo. Y el defecto corregido vuelve a probarse **con el caso que lo encontró**, no con uno parecido.

| # | Qué falla | Gravedad | ¿Bloquea la entrega? | Quién lo corrige | Estado |
|---|---|---|---|---|---|
| 1 | «…» | «Impide trabajar / Estorba pero hay cómo seguir / Molesta» | «Sí / No» | «…» | «Abierto / Corregido / Vuelto a probar / Aceptado como deuda» |

## 9. Que lo arreglado no rompa lo que servía

> Cada corrección puede romper algo que ya funcionaba. Lo que se vuelve a correr entero antes de entregar es la red que lo detecta.

| Qué se vuelve a correr | Cuándo | Cuánto demora |
|---|---|---|
| «…» | «Antes de cada entrega» | «…» |

## 10. Qué quedó sin probar

| Qué no se probó | Por qué | Qué riesgo se acepta |
|---|---|---|
| «…» | «…» | «…» |

## 11. La prueba del usuario

> La última palabra no es del equipo. **Aceptación** es el usuario ejecutando sus propios casos con sus propios datos, y firmando.

| Quién prueba | Qué casos | Cuándo | Resultado |
|---|---|---|---|
| «…» | «…» | «AAAA-MM-DD» | «Acepta / Acepta con reparos / Rechaza» |

## 12. Los entregables de esta etapa, y a quién van

| Documento | Molde | Va a | Estado |
|---|---|---|---|
| Plan de pruebas | [plantillas/ciclo-vida-proyectos/08-plan-pruebas.md](../../ciclo-vida-proyectos/08-plan-pruebas.md) | Cliente, junto con el plan de trabajo | «…» |
| Resultado de pruebas | [plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md](../../ciclo-vida-proyectos/09-resultado-pruebas.md) | Cliente | «…» |
| Cierre de la funcionalidad | [plantillas/ciclo-vida-proyectos/11-funcionalidad-implementada.md](../../ciclo-vida-proyectos/11-funcionalidad-implementada.md) | Cliente | «…» |
| Registro de defectos | Sección 8 de este documento | Equipo | «…» |
| Acta de aceptación del usuario | Sección 11 de este documento | Cliente, se firma | «…» |

## 13. Las puertas de esta etapa

> **Criterios de salida:** lo que tiene que cumplirse para dar la etapa por terminada.

| Qué no se puede hacer | Hasta que | Regla |
|---|---|---|
| Aprobar un plan de trabajo | venga con su plan de pruebas | [`02·F4`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md) |
| Declarar algo terminado | tenga prueba corrida con su evidencia | «…» |
| Desplegar | ningún defecto que bloquee siga abierto | «…» |
| Desplegar | cada criterio de aceptación tenga veredicto | «…» |

## 14. La decisión de cierre

**«Se pasa a despliegue / No se pasa»**, decidido por «quién» el «AAAA-MM-DD».

«Qué quedó sin verificar y por qué, y qué defecto se acepta como deuda con su dueño.»
