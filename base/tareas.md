# Las tareas del agente

Antes de hacer una tarea, el agente lee las reglas que le aplican. Para encontrarlas, cada regla dice a qué tareas aplica con una línea `**Aplica a:**`, y [base/mapa-de-tareas.md](mapa-de-tareas.md) las junta por tarea.

Esta es la lista cerrada de esas tareas. Una regla solo puede nombrar las que están aquí. Si una regla no cabe en ninguna, se agrega una tarea a esta lista antes de anotarla.

| Tarea | Cuándo aplica | Palabras del pedido que la señalan |
|---|---|---|
| `recibir-pedido` | Llega un mensaje del usuario y hay que decidir qué pide y qué autoriza | siempre |
| `responder` | Se escribe la respuesta en el chat | siempre |
| `escribir-documento` | Se crea o se cambia un documento del proyecto que no es código | documento, documentos, readme, plantilla, plantillas, redaccion, redactar, redacte, escriba, escribir, escribe, texto, textos, resumen, informe, manual, glosario, markdown, md, nota, notas, tabla |
| `cambiar-codigo` | Se crea o se cambia código, pruebas o configuración | codigo, funcion, funciones, clase, clases, metodo, programa, script, guion, prueba, pruebas, test, tests, validador, validadores, enganche, enganches, hook, refactor, refactorizar, bug, arreglar, arregle, configuracion |
| `correr-comando` | Se ejecuta un comando en la máquina | corra, correr, ejecute, ejecutar, comando, comandos, instale, instalar, instalacion, terminal, consola, proceso |
| `tocar-git` | Se hace commit o push, o se cambia de rama | git, commit, commitear, push, suba, subir, subalo, subelo, rama, ramas, merge, pull, publique, publicar, versionar |
| `tocar-datos` | Se leen o se cambian datos reales, o se corre una migración | datos, bd, migracion, migre, migrar, borrar, borre, elimine, eliminar, produccion, respaldo, restaurar, sql, registros |
| `ir-afuera` | Se envía algo a un servicio de afuera o se trae algo de allá | internet, web, url, api, descargar, descargue, enviar, envie, correo, externo, pagina |
| `cambiar-estandar` | Se crea o se cambia una regla, una plantilla o un validador del estándar | regla, reglas, estandar, nucleo, capitulo, checklist, plantilla, plantillas, validador |
| `trabajar-cadena` | Se abre, se planea o se cierra un pendiente, una historia o una fase | pendiente, pendientes, hu, historia, historias, epica, fase, fases, plan, planes, hallazgo, hallazgos, criterio, cadena, registre |

Una regla puede aplicar a varias tareas. Se escriben separadas por coma: `**Aplica a:** escribir-documento, cambiar-estandar`.

La línea va después del ejemplo de la regla, igual que la de quién la hace cumplir. No es parte del cuerpo: no cuenta para su largo ni anula su checklist.

**Las palabras de la tercera columna** las usa el recuperador de reglas para saber qué tareas pide un mensaje. Se escriben sin tildes y en minúscula, con las formas del verbo que se usan al pedir («subir», «suba», «súbalo»): el recuperador compara palabra por palabra, sin adivinar raíces. `siempre` quiere decir que la tarea va en todo mensaje, porque todo mensaje es un pedido y lleva respuesta.
