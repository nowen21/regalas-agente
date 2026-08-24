# Pruebas: ¿cumple, y con qué evidencia?   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito con qué se comprueba cada criterio del estándar de trabajo heredable, qué se ejecutó y qué dio.

> **Escrito como si no hubiera nada construido.** Los casos salen de los requisitos del [análisis](../analisis-requisitos/README.md) y de las doce fases de la [implementación](../implementacion/README.md), no del repositorio.

**Estado: BORRADOR** (2026-08-22, sin abrir).

---

## 1. Qué entra a esta etapa

| Qué se recibe | De dónde viene | ¿Aprobado? |
|---|---|---|
| Criterios de aceptación, uno por historia | Análisis | No: las historias están pendientes |
| Siete requisitos no funcionales con su forma de comprobarse | Análisis | No |
| Lo construido, fase por fase | Implementación | No: la etapa no se ha abierto |

## 2. Qué se prueba, y con qué se comprueba

| Criterio de aceptación | Casos que lo cubren | Tipo | Automática |
|---|---|---|---|
| Las reglas se cargan al abrir la sesión | Abrir con reglas, abrir sin ellas, abrir con una regla rota | Integración | Sí |
| Nada cambia de estado sin aprobación | Intento de borrado sin aprobar, con aprobación, y de una acción no incluida en el plan | Integración | Sí |
| Lo escrito se comprueba solo | Un documento que cumple, uno que no, y uno a medio llenar | Unitaria | Sí |
| Lo no probado se declara sin verificar | Funcionalidad con prueba, sin prueba, y con prueba fallida | Unitaria | Sí |
| La instalación deja el proyecto funcionando | Instalar en un proyecto vacío y en uno con archivos propios | De aceptación | No: la revisa una persona |
| El proyecto sabe cuándo quedó atrás | Versión igual, anterior, posterior e inexistente | Unitaria | Sí |
| La sesión deja su rastro fuera del chat | Sesión de un mensaje, sesión larga, sesión interrumpida | Integración | Sí |
| Ninguna credencial queda escrita | Clave entre comillas, sin comillas, y una palabra que solo parece clave | De seguridad | Sí |
| El entregable sale del `.md` | Documento completo, documento con `«…»` sin llenar | De aceptación | No: se abre el `.docx` |
| Abrir la sesión no demora más de dos segundos | Repositorio de diez, cien y mil archivos | De carga | Sí |

## 3. Lo que también se prueba: que NO pase

| Qué NO debe pasar | Cómo se provoca | Qué se espera |
|---|---|---|
| Que una comprobación acuse sobre lo que no leyó | Se la apunta a una carpeta que no es la suya | Dice que esa carpeta no es la que revisa, y no da veredicto |
| Que se tape lo que no es una clave | Un fragmento de programa donde «clave» es el nombre de una variable | Queda tal cual: el registro sigue siendo legible |
| Que el aviso de desfase se apague | Se declara una versión mayor que la publicada | Avisa que el número no existe, en vez de concluir que va adelantado |
| Que una fase se cierre sin veredicto | Se intenta cerrar con el resultado vacío | Se rechaza el cierre |
| Que la instalación pise algo del proyecto | Se instala sobre un proyecto que ya tiene archivos con esos nombres | No sobrescribe: avisa y se detiene |

## 4. Con qué datos y en qué ambiente

| Qué se define | Cómo queda |
|---|---|
| Datos de prueba | Proyectos de mentira creados por la propia prueba; ninguna clave real, ni siquiera vencida |
| Ambiente | La misma máquina donde corre el agente, sin red: es también el ambiente de producción |
| Qué se limpia después | Los proyectos de mentira se borran al terminar; lo que quede se detecta en la siguiente corrida |

## 5. La evidencia

| Qué se ejecutó | Cuándo | Dónde queda la salida |
|---|---|---|
| Pendiente: la etapa no se ha abierto | «AAAA-MM-DD» | El resultado de pruebas de cada fase |

## 6. El veredicto, criterio por criterio

| Criterio | Resultado | Evidencia | Si falló, qué se hace |
|---|---|---|---|
| Los diez de la sección 2 | Sin verificar | Ninguna todavía | Se corrige antes de cerrar la fase que lo introdujo |

## 7. Los defectos encontrados

| # | Qué falla | Gravedad | ¿Bloquea la entrega? | Estado |
|---|---|---|---|---|
| — | Ninguno todavía: nada se ha ejecutado | — | — | — |

## 8. Los entregables de esta etapa, y a quién van

| Documento | Molde | Va a | Estado |
|---|---|---|---|
| Plan de pruebas por fase | [plantillas/ciclo-vida-proyectos/08-plan-pruebas.md](../../plantillas/ciclo-vida-proyectos/08-plan-pruebas.md) | Usuario, con el plan de trabajo | Pendiente |
| Resultado de pruebas por fase | [plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md](../../plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md) | Usuario | Pendiente |
| Cierre de cada funcionalidad | [plantillas/ciclo-vida-proyectos/11-funcionalidad-implementada.md](../../plantillas/ciclo-vida-proyectos/11-funcionalidad-implementada.md) | Usuario | Pendiente |

## 9. Las puertas de esta etapa

| Qué no se puede hacer | Hasta que | Regla |
|---|---|---|
| Aprobar un plan de trabajo | venga con su plan de pruebas | [`02·F4`](../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md) |
| Declarar algo terminado | tenga prueba corrida con su evidencia | El estado lo fija la prueba, no la lectura |
| Desplegar | ningún defecto que bloquee siga abierto | Sección 7 de este documento |

## 10. La decisión de cierre

**No se abre la etapa todavía**, decidido por el autor el 2026-08-22.

Lo que este documento deja fijado antes de empezar es la sección 3: buena parte del esfuerzo se va en comprobar **lo que no debe pasar**, porque una comprobación que reprueba de más se apaga a la semana y entonces no queda nada vigilando.
