# Histórico de sesiones

Cada sesión de chat queda escrita en `historico-chat/` (raíz del repo del estándar), un archivo por sesión con nombre `AAAA-MM-DD-tema.md`, siguiendo la plantilla de `historico-chat/README.md`.

**Es la transcripción del diálogo, no un resumen:** va cada mensaje del usuario y cada respuesta del agente, en orden y sin saltarse ninguno, **ambos literales** — el mensaje tal como lo escribió y la respuesta tal como la dio, con sus tablas, bloques de código y ejemplos. No se condensa ni se parafrasea. Solo se omite la salida cruda de herramientas.

**Cada interacción lleva marca de tiempo** `AAAA-MM-DD HH:MM:SS` leída del reloj del sistema (`date "+%Y-%m-%d %H:%M:%S"`), nunca inventada: una al recibir el mensaje, otra al escribir la respuesta. Al final, una sección "Abierto". Se agrega la línea al índice del README.

**Por qué:** el usuario quiere retomar el trabajo sin releer el chat y saber por qué quedó algo como quedó. El chat se pierde, el repo no.

Desde 2026-08-06 la obligación está escrita en el `CLAUDE.md` de la raíz del repo (§1), que el agente carga solo al abrir sesión: esta memoria ya no es el único sitio donde vive la regla.

**Excepción:** lo que no es parte del estándar no se registra. Mover, copiar o borrar carpetas ajenas al repo (material de cursos, proyectos del usuario que solo estaban de paso) es tarea de archivo, no una decisión del estándar — no abre ni alimenta entrada de histórico.

**Cómo se aplica:** **no esperar al cierre de la sesión** — crear la entrada apenas la sesión produce su primera decisión o cambio, y **actualizarla cada vez que se cierra un tema**. Esperar al final falla: las sesiones rara vez tienen cierre explícito, así que la entrada nunca se escribe o queda vieja mientras la conversación sigue.

Relacionado: [pendientes en el repo](pendiente-patrones-devops.md) · [respuestas cortas](respuestas-cortas.md) y [estilo de redacción simple](estilo-redaccion-simple.md) al redactar · [aprobar antes de commit](aprobar-antes-de-commit.md) para el commit de la entrada.
