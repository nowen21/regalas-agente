# Pruebas: ¿cumple, y con qué evidencia?   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito con qué se comprueba cada criterio de aceptación, qué se ejecutó y qué dio. **El estado de una funcionalidad lo fija la prueba corrida, no la lectura del código:** mientras no haya prueba, lo honesto es «sin verificar».

> Plantilla. Se llena junto con el plan de trabajo, no después. La envergadura ajusta la profundidad, nunca la existencia: la sección sin materia se llena con `N/A porque «…»`, nunca se borra. Reemplaza los `«…»` y borra esta caja.

> **Cómo se redacta lo que va dentro de cada `«…»`.** En el idioma del proyecto ([`01·C8`](«RUTA-ESTANDAR»/base/01-conducta.md#c8--habla-el-idioma-del-proyecto)) y en la menor cantidad de palabras con la que se entienda ([`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md)): el dato primero, sin repaso, sin justificación que nadie pidió y sin paso a paso. Lo que no cabe se escribe en su documento y se enlaza.

**Estado: «BORRADOR / EN CURSO / CERRADA»** («AAAA-MM-DD»).

---

## 1. Qué entra a esta etapa

| Qué se recibe | De dónde viene | ¿Aprobado? |
|---|---|---|
| Criterios de aceptación, uno por historia | Análisis | «…» |
| Requisitos no funcionales con su forma de comprobarse | Análisis | «…» |
| Lo construido, fase por fase | Implementación | «…» |

## 2. Qué se prueba, y con qué se comprueba

> **Cada criterio de aceptación tiene al menos un caso.** El criterio sin caso es una promesa; el caso sin criterio es trabajo que nadie pidió.

| Criterio de aceptación | Casos que lo cubren | Tipo | Automática |
|---|---|---|---|
| «HU-001, criterio 1» | «…» | «Unitaria / Integración / De aceptación / De carga / De seguridad» | «Sí / No, y por qué» |

## 3. Lo que también se prueba: que NO pase

> Una comprobación que solo mira el caso feliz aprueba cualquier cosa. Acá va lo que el sistema debe rechazar, y lo que no debe reportar de más: **una comprobación que reprueba de más se apaga a la semana, y entonces no queda nada.**

| Qué NO debe pasar | Cómo se provoca | Qué se espera |
|---|---|---|
| «…» | «…» | «…» |

## 4. Con qué datos y en qué ambiente

| Qué se define | Cómo queda |
|---|---|
| Datos de prueba | «De dónde salen, y cómo se sabe que no son datos reales de personas» |
| Ambiente | «Dónde se corre, y en qué se parece y en qué no a producción» |
| Qué se limpia después | «…» |

## 5. La evidencia

> **Sin evidencia, un veredicto es una opinión.** Se guarda lo que se ejecutó y su salida, no un resumen escrito de memoria.

| Qué se ejecutó | Cuándo | Dónde queda la salida |
|---|---|---|
| «…» | «AAAA-MM-DD» | «…» |

## 6. El veredicto, criterio por criterio

| Criterio | Resultado | Evidencia | Si falló, qué se hace |
|---|---|---|---|
| «HU-001, criterio 1» | «Cumple / No cumple / Sin verificar» | «…» | «…» |

## 7. Los defectos encontrados

| # | Qué falla | Gravedad | ¿Bloquea la entrega? | Estado |
|---|---|---|---|---|
| 1 | «…» | «Alta / Media / Baja» | «Sí / No» | «Abierto / Corregido / Aceptado como deuda» |

## 8. Los entregables de esta etapa, y a quién van

| Documento | Molde | Va a | Estado |
|---|---|---|---|
| Plan de pruebas | [plantillas/ciclo-vida-proyectos/08-plan-pruebas.md](../../ciclo-vida-proyectos/08-plan-pruebas.md) | Cliente, junto con el plan de trabajo | «…» |
| Resultado de pruebas | [plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md](../../ciclo-vida-proyectos/09-resultado-pruebas.md) | Cliente | «…» |
| Cierre de la funcionalidad | [plantillas/ciclo-vida-proyectos/11-funcionalidad-implementada.md](../../ciclo-vida-proyectos/11-funcionalidad-implementada.md) | Cliente | «…» |

## 9. Las puertas de esta etapa

| Qué no se puede hacer | Hasta que | Regla |
|---|---|---|
| Aprobar un plan de trabajo | venga con su plan de pruebas | [`02·F4`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md) |
| Declarar algo terminado | tenga prueba corrida con su evidencia | «…» |
| Desplegar | ningún defecto que bloquee siga abierto | «…» |

## 10. La decisión de cierre

**«Se pasa a despliegue / No se pasa»**, decidido por «quién» el «AAAA-MM-DD».

«Qué quedó sin verificar y por qué, y qué defecto se acepta como deuda con su dueño.»
