# 2026-08-22 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-22-sesion-6.md](../../2026-08-22-sesion-6.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

**Viene de:** 2026-08-22 · sesion-5 · H-4, el choque entre el molde de factibilidad y los cuatro frentes que la práctica evalúa. Sigue abierto.

---

## Hallazgos de esta sesión

### H-1 · La documentación se escribía desde lo construido, así que describía la limitación en vez del objetivo

- **Qué pasó:** el usuario cortó el avance con esto: *"el problema es que se está partiendo de lo que actualmente existe. La documentación debe partir de la propuesta y del objetivo que se quiere desarrollar"*.
- **Por qué importa:** una etapa escrita desde lo construido convierte cada carencia de hoy en un requisito de mañana. La decisión `DA-12` es la prueba: decía *"la pantalla solo lee"* porque la que existe solo lee, no porque alguien hubiera decidido que así fuera.
- **Qué lo soluciona:** se resolvió acá, reescribiendo las cuatro primeras etapas y dejando la exigencia en los siete moldes. No dispara historia.
- **Qué se decidió:** las etapas se escriben desde la propuesta, con la prueba del borrado mental: si mañana no existiera nada de lo construido, ¿el documento seguiría diciendo lo mismo? `DA-12` quedó al revés: *"la pantalla administra, y todo cambio queda firmado y registrado"*.
- **Estado:** resuelto acá.
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** [cvds/](../../../cvds/) etapas 1 a 4, y la caja de redacción de los siete moldes de [plantillas/cvds/](../../../plantillas/cvds/).
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

### H-2 · Cimiento dejó de ser un cuerpo de reglas y pasó a ser una plataforma

- **Qué pasó:** el usuario definió el reparto: *"Cimiento = plataforma central de gestión, documentación, auditoría y gobierno de proyectos. Proyecto = software desarrollado y sus componentes técnicos necesarios para funcionar"*.
- **Por qué importa:** cambia qué se está construyendo. Las etapas anteriores describían un estándar que se hereda; ahora describen una aplicación que administra proyectos, guarda su documentación, la audita y genera los entregables. Sin ese giro escrito, la primera versión se habría construido contra el documento viejo.
- **Qué lo soluciona:** se partió en las tres épicas que abrieron el trabajo de la versión 1, ya escritas y aprobadas.
- **Qué se decidió:** análisis, diseño e implementación se escribieron para la plataforma: 32 funcionalidades, 12 decisiones de arquitectura, 18 entidades, 12 pantallas, y cinco versiones de producto con la primera repartida en siete fases.
- **Estado:** resuelto acá.
- **Responde a:** —
- **Dispara:**
  1. [EP-008](../../../documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/epica.md) los proyectos se administran desde un solo lugar. Va primera: las otras dos dependen de que haya proyectos conectados.
  2. [EP-009](../../../documentacion/epicas/EP-009-todo-lo-que-se-hace-queda-registrado/epica.md) todo lo que se hace queda registrado. Después de la anterior: no hay qué auditar sin proyectos.
  3. [EP-010](../../../documentacion/epicas/EP-010-lo-escrito-entra-a-la-plataforma/epica.md) lo escrito entra a la plataforma. Última: es la de mayor incertidumbre.
- **Orden de resolución:** —
- **Dónde queda:** [cvds/analisis-requisitos/](../../../cvds/analisis-requisitos/), [cvds/diseno/](../../../cvds/diseno/), [cvds/implementacion/](../../../cvds/implementacion/).
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

### H-3 · El texto es la fuente y la base es un índice, así que el respaldo es el repositorio

- **Qué pasó:** el usuario pidió que el respaldo fuera un script de base de datos versionado que se disparara solo con cada cambio. Al analizarlo salió que eso se atrasa, choca al fusionar y puede terminar publicando lo que no debe.
- **Por qué importa:** define de dónde sale la verdad. Es lo que la aplicación de `interfaz/` tiene al revés: guarda en la base y genera el texto desde ella, y por eso perder la base ahí sí pierde información.
- **Qué lo soluciona:** se resolvió acá como decisión de arquitectura, y la fase A la probó.
- **Qué se decidió:** la fuente es el texto, la base es un índice que se puede borrar entero y rehacer, y el respaldo es el propio control de versiones. Nada de volcados de base en el repositorio.
- **Estado:** resuelto acá.
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** `DA-01` en [cvds/diseno/decisiones-de-arquitectura.md](../../../cvds/diseno/decisiones-de-arquitectura.md), y probado por CP-003 en la fase A.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

### H-4 · Sin la palabra que diga qué se espera, el agente asumía y hacía lo que quería

- **Qué pasó:** el usuario lo dijo así: *"si escribo algo preguntando sobre algo, Cimiento de una asume que tiene que corregir cuando estoy es haciendo una pregunta"*.
- **Por qué importa:** asumir no falla una vez. Es lo que hace que una pregunta termine en un archivo cambiado, y el usuario se entere después.
- **Qué lo soluciona:** se resolvió acá por la cadena completa del capítulo 20, con su historia de usuario y su fase.
- **Qué se decidió:** toda petición abre con una de 18 palabras clave. Una palabra parecida no cuenta, y la palabra fija el máximo, no el mínimo.
- **Estado:** resuelto acá.
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** [`01·C28`](../../../base/01-conducta.md) y su anexo [base/01-conducta/palabras-clave.md](../../../base/01-conducta/palabras-clave.md).
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

### H-5 · El validador encontró lo que dos lecturas no: una regla no puede depender de una blindada

- **Qué pasó:** `01·C28` se escribió declarando que extendía `00·N1`. Se leyó dos veces y pasó. `validar.py metareglas` la rechazó.
- **Por qué importa:** el repositorio tiene los validadores escritos, y el agente los corrió después de dar el trabajo por hecho, no antes. Leer no reemplaza correrlos.
- **Qué lo soluciona:** se resolvió acá quitando la dependencia y dejando escrito el porqué en el sello de la regla.
- **Qué se decidió:** [`20·M7`](../../../base/20-meta-reglas/reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md) prohíbe depender de una regla blindada, así que `C28` no declara dependencia, y las dos filas de su lista de comprobación quedan como no aplica con su motivo escrito.
- **Estado:** resuelto acá.
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** [base/01-conducta.md](../../../base/01-conducta.md), sello de `C28`.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

### H-6 · Todo se escribe en español colombiano, no en español a secas

- **Qué pasó:** el agente escribió *"una pieza"* y el usuario preguntó qué era. Después lo dejó fijo: *"todo debe ser escrito en español colombiano"*.
- **Por qué importa:** [`01·C8`](../../../base/01-conducta.md) pide el idioma del proyecto, y el agente lo cumplía a medias, con palabras que se entienden en otro país pero no acá. Depender de que el usuario lo repita cada sesión es lo mismo que no tenerlo.
- **Qué lo soluciona:** se resolvió acá, escribiéndolo como recuerdo del repositorio.
- **Qué se decidió:** *pieza* pasó a *componente*, se revisó el ciclo entero, y quedó como recuerdo con el caso que lo originó de evidencia.
- **Estado:** resuelto acá.
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** [historico-chat/memory/espanol-colombiano.md](../../memory/espanol-colombiano.md), con su línea en el índice.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

### H-7 · La fase A quedó construida y probada: la plataforma levanta, guarda y rehace su índice

- **Qué pasó:** el usuario decidió empezar de cero en vez de aprovechar `interfaz/`, y trabajar con el molde de estructura que el estándar ya tiene escrito para Django.
- **Por qué importa:** es la primera vez que el estándar produce código propio. Y la razón de empezar de cero es la de `H-3`: adaptar `interfaz/` obligaba a invertirle la fuente y cambiarle la base, que es casi reescribirla cargando lo viejo.
- **Qué lo soluciona:** se resolvió acá. Lo que falta de la versión 1 son las fases B a G, que ya están declaradas.
- **Qué se decidió:** los seis casos del plan de pruebas se corrieron y los seis pasaron. El de la red se hizo más estricto que lo planeado, tapando la salida desde adentro en vez de desconectar la máquina, y ese desvío quedó anotado en vez de corregir el plan aprobado. La aplicación de `interfaz/` no se tocó.
- **Estado:** resuelto acá.
- **Responde a:** [EP-008](../../../documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/epica.md) · [HU-001](../../../documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-001-conectar-un-proyecto/HU-001-conectar-un-proyecto.md). Ningún criterio de aceptación: la fase A construye la base y la B los cumple.
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** [plataforma/](../../../plataforma/), y el cierre en [funcionalidad_implementada.md](../../../documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-001-conectar-un-proyecto/A-EP-008-HU-001-la-plataforma-levanta-y-guarda/funcionalidad_implementada.md), con cuatro deudas declaradas.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

---

## ¿Se puede cerrar la sesión?

Se cierra cuando **ningún hallazgo queda a medias**. Un hallazgo está terminado de una de dos formas, y las dos valen igual:

- **Resuelto acá**, con lo que se hizo escrito en el campo de dónde queda.
- **Anotado**, con su pendiente creado y su historia de usuario disparada escrita. Anotar no es decir "quedó pendiente": es dejar el archivo.

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ |
| Todo hallazgo abierto tiene su pendiente creado | ☑ |
| Toda historia disparada está escrita en su épica | ☑ |
| Lo que se hizo está aprobado y guardado | ☑ |

Con las cuatro marcadas, el tema cerró: la sesión se cierra y lo que siga se abre en otra, con el tema que salió de estos hallazgos.

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.
