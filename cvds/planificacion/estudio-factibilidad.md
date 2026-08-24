# Estudio de factibilidad: ¿conviene hacerlo, y por este camino?   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito, antes de comprometer trabajo, si el proyecto es viable y por qué camino: qué es posible técnicamente, qué cuesta, cuánto toma y qué alternativas se evaluaron. Su valor está en las alternativas descartadas: sin ellas, la decisión no se puede defender ni revisar después.

> **Escrito como si no hubiera nada construido**, igual que el resto de [cvds/](../README.md). Acompaña a [cvds/planificacion/README.md](README.md) y su conclusión está en la sección 6 de ese documento.

**Estado: APROBADO** (2026-08-24, por Ing. José Dúmar Jiménez Ruíz).

## 1. Qué se evalúa

El agente de IA no recuerda nada entre sesiones, entrega sin comprobar y cambia lo que no se le pidió, y el usuario paga eso revisándolo todo. La pregunta: ¿se puede hacer que lo acordado una vez siga valiendo, con lo que hay hoy, sin infraestructura ni gasto?

## 2. Alternativas evaluadas

| # | Alternativa | Qué implica | Costo estimado | Tiempo estimado | Riesgo mayor |
|---|---|---|---|---|---|
| 1 | Reglas en texto dentro del repositorio, cargadas al abrir la sesión ✔ | Escribirlas, comprobarlas con programas y heredarlas por instalación | Solo tiempo del autor, unas 88 jornadas | Sin fecha: se construye por fases | Que el agente no obedezca lo que se le carga |
| 2 | Configurar la herramienta con recordatorios | Guardar preferencias en el almacén de la herramienta | Casi nulo | Días | No viaja con el proyecto, no se versiona y nadie más lo ve |
| 3 | Un servicio que vigile al agente desde afuera | Construir y sostener un servicio propio | Alto, y recurrente | Meses | Infraestructura que hay que mantener, y otro sistema que puede caerse |
| 4 | Afinar un modelo propio con las correcciones | Recolectar ejemplos y entrenar | Alto, con conocimiento que no se tiene | Meses | Corregir una regla exige volver a entrenar, y lo aprendido no se puede citar |
| 5 | No hacer nada | Seguir corrigiendo por chat | Cero al empezar | Ninguno | El costo se repite en cada sesión y crece con cada proyecto |

## 3. Viabilidad, en cuatro frentes

| Frente | Pregunta | Respuesta | ¿Bloquea? |
|---|---|---|---|
| Técnica | ¿Existe la capacidad y las herramientas? | Sí: archivos de texto, Python de la biblioteca estándar y los enganches que la herramienta ya ofrece | No |
| Económica | ¿El costo cabe en lo que se está dispuesto a invertir? | Sí: no hay gasto, solo tiempo del autor, y lo que ahorra es la revisión repetida | No |
| Operativa | ¿Lo van a adoptar? | Un solo usuario, que es quien lo escribe. Fuera de él, sin evidencia | No, pero es el frente sin comprobar |
| Legal | ¿Cumple normativa, licencias y protección de datos? | Sin datos de personas ni de terceros; las credenciales no se escriben | No |

## 4. La decisión

**Se hace por la alternativa 1**, decidido por el autor el 2026-08-24.

Es la única que sobrevive a las tres exigencias a la vez: viaja con el proyecto, se puede citar y corregir sin rehacer nada, y no obliga a sostener infraestructura. La 2 falla porque lo acordado no sale de la máquina; la 3 y la 4 cuestan más que el problema que resuelven.

**Qué obligaría a reevaluar:** que alguien ajeno al autor instale el estándar y no lo use. Ese es el frente operativo, el único sin evidencia, y su resultado decide si esto es un estándar o una preferencia personal.
