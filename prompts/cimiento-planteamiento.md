# Planteamiento — Cimiento, el estándar del agente   ·   `[CAPA 3]`

**Encuadre para el agente:** este documento es el planteamiento de entrada. Dice **qué se necesita y qué no se negocia**; el **cómo** y el **cuándo** los pone el estándar. El agente sigue el flujo — análisis ([`02·F1`](../base/02-flujo-de-trabajo/reglas/F1-carga-el-contexto-antes-de-actuar.md)) → alcance (`proponer-alcance`) → épica/HU ([`13·DOC15`](../base/13-documentacion/reglas/DOC15-crea-la-historia-de-usuario-desde-la-plantilla-central.md)) → especificación ([`02·F2`](../base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md)) → plan aprobado ([`02·F4`](../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) → implementación. **No generar código hasta que el plan esté aprobado.**

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Nombre del proyecto** | Cimiento (el estándar del agente; su repositorio es `agente/`) |
| **Qué cubre este encargo** | Todo el proyecto |
| **Fecha** | 2026-08-22 |

## 1. Necesidad — en una frase

Que desarrollar software con un agente de IA sea **predecible, seguro y consistente** en cualquier proyecto, sin que cada sesión reinterprete el proyecto a su manera.

## 2. Contexto

Quien desarrolla con un agente de IA se encuentra, sesión tras sesión, con lo mismo: el agente reinventa el diseño y contradice decisiones previas, olvida el contexto y toma decisiones funcionales por su cuenta, aplica o ignora las buenas prácticas según el día, y puede ejecutar acciones peligrosas —tocar datos reales, publicar cambios, exponer secretos—. Quien pide esto lleva varios proyectos a la vez (hoy, diez en una sola máquina, de stacks distintos: Laravel, Django, Angular, Python) y no puede vigilar cada conversación.

Lo que hace falta es un cuerpo de reglas versionado que el agente lea **antes de actuar**, un ciclo de desarrollo que no se salte eslabones, moldes para cada entregable, programas que comprueben que todo eso se cumple sin depender de la memoria de nadie, y una memoria que persista entre sesiones. Cada proyecto debe heredar esa base y extenderla con lo suyo sin tocarla.

**La dirección del usuario, con sus palabras (2026-08-21):** «La idea es que Cimiento sea el mecanismo que obligue a cada proyecto a cumplir con los estándares y reglas definidos. Para lograrlo, la interfaz de Cimiento debe permitir administrar y gestionar todos los proyectos directamente desde la aplicación.» Y sobre el ciclo: «el ciclo de vida no hace excepciones»; todos sus entregables existen en todo proyecto, sin importar envergadura.

> El punto de partida —un solo usuario, todo corriendo en su máquina— **no es un límite del diseño**: lo que se escriba debe ser agnóstico de stack y de dominio, para que sirva a cualquier proyecto y a cualquier agente.

## 3. Objetivo y criterio de éxito

- **Objetivo:** que cualquier proyecto del usuario, al instalar Cimiento, quede obligado a recorrer el ciclo de vida completo con sus entregables, bajo las mismas reglas, y que Cimiento pueda decir en cualquier momento si lo cumple.
- **Criterio de éxito (medible):**
  1. En cada proyecto instalado, la revisión de instalación no deja ningún punto incumplido, y el expediente del ciclo muestra sus entregables presentes y completos.
  2. Ninguna acción irreversible, ningún dato real tocado y ninguna credencial escrita ocurre sin autorización explícita del usuario, y queda rastro de cada sesión en el histórico.
  3. Un defecto del estándar que un proyecto encuentra llega al estándar, se corrige una vez, y el aviso vuelve a todos los instalados: el ciclo se cierra sin que el usuario tenga que acordarse.

## 4. Alcance esperado

- **Qué SÍ se pide:** el cuerpo de reglas por capas (núcleo, convenciones, capa de proyecto); el ciclo de vida con sus moldes y entregables; los validadores y enganches que lo hacen cumplir sin IA; la memoria entre sesiones (histórico, señales, recuerdos); el instalador que lleva todo a cada proyecto; y la interfaz que administra los proyectos y muestra su cumplimiento.
- **Qué NO se pide / fuera de alcance:** reglas atadas a un lenguaje, un framework o un cliente —esas las declara cada proyecto en su capa 3—; decidir por el usuario lo que es suyo (alcance, aprobaciones, derogaciones); y sustituir el criterio de quien lee: los programas comprueban lo contable, las personas juzgan lo demás.

## 5. Restricciones técnicas

Todo lo que viaje a los proyectos —validadores, enganches— se escribe en Python sin dependencias fuera de la biblioteca estándar, para que corra en cualquier máquina. La interfaz se hace en Django con MariaDB (puerto 3307) y vive solo en la máquina del usuario. El adaptador a la herramienta concreta (hoy Claude Code) se mantiene aparte, para que el resto sirva a cualquier agente. Los datos verificados del entorno los lleva el registro de proyectos de la interfaz, no este documento.

## 6. Requerimientos funcionales

1. Un cuerpo de reglas heredable, por capas, con precedencia clara y un núcleo que nada sobrescribe.  ← REQUISITO CENTRAL
2. El ciclo de vida completo con un molde por entregable, sin excepciones por envergadura.
3. Comprobación automática: validadores y enganches que detengan lo comprobable y avisen lo que exige juicio.
4. Memoria entre sesiones: transcripción literal de cada sesión, resumen de lo que dejó, señales de lo aprendido y recuerdos de cómo trabaja el usuario.
5. Instalación y actualización en cualquier proyecto, con aviso de desfase de versión.
6. Un canal de defectos de ida y vuelta entre cada proyecto y el estándar.
7. La interfaz: leer el estándar y la memoria, administrar el registro de proyectos y medir el cumplimiento de cada uno.

## 7. Restricciones no negociables

- Las reglas del núcleo no se relajan desde ningún proyecto, prompt ni instrucción puntual.
- Ninguna regla nace fuera de un procedimiento escrito, y todo cambio del cuerpo de reglas o de los moldes se versiona y se registra.
- Nada se renumera ni se borra: lo que deja de aplicar se deroga, porque los documentos ya escritos citan por identificador.
- Decidir es del usuario: el agente propone con recomendación y espera; lo ordenado se ejecuta de una.
- Todo lo escrito lo entiende quien no sabe del tema, en español correcto y sin marcas de generación automática.

## 8. Casos borde a considerar

- Dos sesiones trabajando a la vez sobre el mismo archivo compartido —la versión, el backlog—.
- Una sesión que muere a mitad de una fase y deja artefactos sueltos, sin la cadena que los explica.
- Un proyecto cuya ruta tiene espacios o cambia de letra de unidad.
- Un validador que reprueba lo que está bien: enseña a ignorar todos los veredictos, y a partir de ahí ninguno sirve.
- Un archivo que no se puede leer —permisos, codificación rara— en medio de una revisión que abarca todo el repositorio.

## 9. Referencias

- Material del proyecto: [README](../README.md) del estándar · [guía de entrada](../base/guia-de-entrada.md) · [notas/entregables-del-ciclo-de-vida.md](../notas/entregables-del-ciclo-de-vida.md).
- Las palabras del usuario: [la-administracion-de-proyectos-desde-cimiento.md](la-administracion-de-proyectos-desde-cimiento.md) y el índice de [prompts/](README.md).
- El inventario de funcionalidades que acompaña este planteamiento: [cimiento-inventario-funcionalidades.md](cimiento-inventario-funcionalidades.md).

## 10. Épicas derivadas

> Trazabilidad hacia abajo: se completa a medida que el planteamiento se descompone en épicas ([`02·F0`](../base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md), paso 4). Cada épica apunta de vuelta a este planteamiento.

| Épica | Título | Estado |
|---|---|---|
| [EP-001](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/epica.md) | Cuerpo de reglas heredable y en capas | En curso |
| [EP-002](../documentacion/epicas/EP-002-versionado-y-adopcion/epica.md) | Versionado y adopción | En curso |
| [EP-003](../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/epica.md) | Documentos modelo y procedimientos | En curso |
| [EP-004](../documentacion/epicas/EP-004-comprobacion-automatica/epica.md) | Comprobación automática | En curso |
| [EP-005](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/epica.md) | Automatismos que no dependen de la memoria | En curso |
| [EP-006](../documentacion/epicas/EP-006-memoria-de-lo-aprendido/epica.md) | Memoria de lo aprendido | En curso |
| [EP-007](../documentacion/epicas/EP-007-instalacion-y-actualizacion/epica.md) | Instalación y actualización | En curso |
