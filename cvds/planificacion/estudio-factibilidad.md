# Estudio de factibilidad: ¿conviene hacerlo, y por este camino?   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito, antes de comprometer trabajo, si el proyecto es viable y por qué camino: qué es posible técnicamente, qué cuesta, cuánto toma y qué alternativas se evaluaron. Su valor está en las alternativas descartadas: sin ellas, la decisión no se puede defender ni revisar después.

> **Escrito desde la propuesta**, igual que el resto de [cvds/](../README.md). Reemplaza al estudio firmado el 2026-08-24, que evaluaba otro producto: un estándar que viajaba dentro de cada proyecto.

**Estado: APROBADO** (2026-08-24, por Ing. José Dúmar Jiménez Ruíz).

## 1. Qué se evalúa

El usuario trabaja en varios proyectos, no tiene desde dónde gobernarlos, y el agente que lo ayuda olvida entre sesiones, entrega sin comprobar y cambia lo que no se pidió. La pregunta: ¿se puede administrar todos los proyectos desde un solo lugar, con lo que hay hoy y sin gasto?

## 2. Alternativas evaluadas

| # | Alternativa | Qué implica | Costo estimado | Tiempo estimado | Riesgo mayor |
|---|---|---|---|---|---|
| 1 | Una plataforma en la máquina del usuario, dueña de la documentación, con la fuente en texto y la base como índice ✔ | Construir la plataforma, servirle las reglas al agente y generar el expediente | Tiempo del autor, unas 173 jornadas | Sin fecha: por versiones | Que todo dependa de una máquina y de una persona |
| 2 | Que cada proyecto siga guardando su documentación adentro | Seguir como hoy, mejorando los moldes | Bajo | Semanas | No se puede consultar de conjunto, ni auditar, ni entregar sin armarlo a mano |
| 3 | Una plataforma que solo lea los proyectos y los muestre | Indexar lo que cada proyecto escribe, sin ser dueña | Media, unas 90 jornadas | Meses | La documentación sigue dispersa, y auditar depende de que cada proyecto la escriba bien |
| 4 | Un servicio en línea que aloje todo | Contratar, sostener y asegurar infraestructura | Alto, y recurrente | Meses | La documentación de clientes sale de la máquina del usuario |
| 5 | Comprar una herramienta de gestión de proyectos | Adaptarse a lo que traiga | Suscripción | Días | Ninguna gobierna al agente ni sirve las reglas con que trabaja |
| 6 | No hacer nada | Seguir entrando proyecto por proyecto | Cero al empezar | Ninguno | El costo crece con cada proyecto, y lo aprobado se sigue perdiendo |

## 3. Viabilidad, en cuatro frentes

| Frente | Pregunta | Respuesta | ¿Bloquea? |
|---|---|---|---|
| Técnica | ¿Existe la capacidad y las herramientas? | Sí: texto, una base local, una aplicación que corre en la máquina y los enganches de la herramienta del agente | No |
| Económica | ¿Los beneficios justifican el costo? | Sí: no hay gasto, y lo que ahorra es la revisión repetida y el armado del expediente | No |
| Operativa | ¿Lo van a adoptar? | Es la herramienta del propio autor. Fuera de él, sin evidencia | No, pero es el frente sin comprobar |
| Legal | ¿Cumple normativa, licencias y protección de datos? | Sin datos de personas, y la información de clientes no sale de la máquina | No |

## 4. La decisión

**Se hace por la alternativa 1**, decidido por el autor el 2026-08-24.

La 2 es lo que hay hoy y es el problema. La 3 cuesta la mitad y deja sin resolver lo que más duele: la documentación seguiría dispersa y el expediente habría que armarlo. La 4 y la 5 sacan la información de la máquina del usuario o no gobiernan al agente, que es el punto.

**Qué obligaría a reevaluar:** que alguien más tenga que usar la plataforma. Con un segundo usuario aparecen permisos, roles y responsabilidad sobre datos ajenos, y eso cambia los cuatro frentes a la vez.
