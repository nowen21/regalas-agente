# Planteamiento — Cimiento, el estándar del agente   ·   `[CAPA 3]`

**Para el agente:** este documento dice **qué** se necesita y **qué no se negocia**. El **cómo** y el **cuándo** los pone el estándar: se recorre la cadena de [`02·F0`](../base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) sin saltar eslabones. Lo que se responda sobre este documento se escribe bajo [`00·ID9`](../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md): la menor extensión con la que se entienda.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Nombre del proyecto** | Cimiento, el estándar del agente (su repositorio es `agente/`) |
| **Qué cubre este encargo** | Todo el proyecto |
| **Fecha** | 2026-08-22 |
| **Cómo se levantó** | Reconstruido del proyecto existente, a partir del README, de los pedidos del usuario guardados en `prompts/`, de las notas de diseño y del inventario de funcionalidades. No hubo entrevista. |

## 1. Necesidad — en una frase

Que desarrollar software con un agente de IA sea predecible, seguro y consistente en cualquier proyecto, sin que cada sesión reinterprete el proyecto a su manera.

## 2. Contexto

Un agente de IA que programa sin reglas escritas repite cuatro fallas, sesión tras sesión: reinventa el diseño y contradice decisiones ya tomadas; olvida el contexto y decide por su cuenta cosas que son del negocio; aplica o ignora las buenas prácticas según el día; y puede ejecutar acciones peligrosas, como tocar datos reales, publicar cambios o exponer credenciales. Ninguna de las cuatro se arregla explicándolas otra vez al empezar cada conversación: la explicación se pierde con la conversación.

Quien pide esto lleva varios proyectos a la vez (hoy, diez en una sola máquina, de stacks distintos: Laravel, Django, Angular, Python), trabaja solo y no puede vigilar cada sesión de cada proyecto. Necesita que el control no dependa de que él esté mirando.

Lo que hace falta, entonces, es un contrato explícito y versionado que el agente lea antes de actuar: un cuerpo de reglas organizado en capas, un ciclo de desarrollo que no se salte eslabones, un molde por cada entregable, programas que comprueben lo comprobable sin depender de la memoria de nadie, y una memoria que sobreviva al cierre del chat. Cada proyecto hereda esa base y la extiende con lo suyo (su stack, su dominio, su sector) sin tocarla.

**La dirección del usuario, con sus palabras (2026-08-21):**

> «La idea es que **Cimiento sea el mecanismo que obligue a cada proyecto a cumplir con los estándares y reglas definidos**. Para lograrlo, la interfaz de Cimiento debe permitir **administrar y gestionar todos los proyectos directamente desde la aplicación** [...] La administración de los proyectos no debe depender de un archivo `.md` donde los proyectos estén definidos de forma hardcodeada.»

Y sobre el ciclo, el mismo día: **«el ciclo de vida no hace excepciones»**. Todos sus entregables existen en todo proyecto, sin importar la envergadura.

> El punto de partida (un solo usuario, todo corriendo en su máquina, un solo agente) no es un límite del diseño: lo que se escriba debe ser agnóstico de stack y de dominio, para que sirva a cualquier proyecto y a cualquier agente. No se recorta estructura apoyándose en que hoy hay un solo usuario.

## 3. Objetivo y criterio de éxito

**Objetivo:** que cualquier proyecto del usuario, al instalar Cimiento, quede obligado a recorrer el ciclo de vida completo con sus entregables y bajo las mismas reglas, y que Cimiento pueda decir en cualquier momento si lo cumple.

**Criterio de éxito.** Se sabe que se logró cuando:

1. En cada proyecto instalado, la revisión de instalación no deja ningún punto incumplido y el expediente del ciclo muestra sus entregables presentes y completos.
2. Ninguna acción irreversible, ningún dato real tocado y ninguna credencial escrita ocurre sin autorización explícita del usuario; y de cada sesión queda rastro escrito sin que nadie tenga que acordarse de escribirlo.
3. Un defecto del estándar que aparece trabajando en un proyecto llega al estándar, se corrige una vez, y el aviso vuelve solo a todos los proyectos instalados.
4. El usuario ve el cumplimiento de todos sus proyectos desde un solo lugar, sin abrir cada repositorio.

## 4. Alcance esperado

**Qué SÍ se pide:**

- El cuerpo de reglas por capas: un núcleo de seguridad que nada sobrescribe, convenciones agnósticas que cada proyecto ajusta, y la capa propia de cada proyecto, con capítulos que se activan solo si el proyecto los necesita.
- El ciclo de vida y sus moldes: la cadena obligatoria de entregables, con un modelo escrito para cada uno, y las vistas consolidadas que se arman a partir de lo ya escrito.
- La comprobación automática: los programas y enganches que detienen lo que se puede comprobar y avisan lo que exige juicio, más una medida única de cumplimiento por proyecto.
- La memoria entre sesiones: la transcripción de cada sesión, el resumen de lo que dejó, las señales de lo aprendido y los recuerdos de cómo trabaja el usuario, todo dentro del repositorio.
- La instalación y el canal de defectos: llevar y poner al día el estándar en cualquier proyecto, avisar del desfase de versión, y devolver al estándar lo que un proyecto encuentra roto.
- La interfaz: administrar el registro de proyectos y medir el cumplimiento de cada uno, con los proyectos registrados en ella y no escritos a mano en un archivo.

**Qué NO se pide / fuera de alcance:**

- Reglas atadas a un lenguaje, un framework o un cliente: esas las declara cada proyecto en su capa 3, y no suben al estándar.
- Decidir por el usuario lo que es suyo: alcance, aprobaciones, derogaciones y prioridades.
- Sustituir el criterio de quien lee. Los programas comprueban lo contable (que el archivo esté, que el enlace resuelva, que la versión suba); que un texto sea correcto lo juzga una persona.
- Servir a varios usuarios a la vez, o correr fuera de la máquina del usuario.

## 5. Restricciones técnicas

Todo lo que viaje a los proyectos (validadores y enganches) se escribe en Python usando solo la biblioteca estándar, para que corra en cualquier máquina sin instalar nada. La interfaz se construye en Django sobre MariaDB en el puerto 3307, y vive únicamente en la máquina del usuario. Lo que ata el estándar a una herramienta concreta, hoy Claude Code, se mantiene apartado del resto, para que el cuerpo de reglas sirva a cualquier agente. Los datos verificados de cada entorno los lleva el registro de proyectos de la interfaz; este documento no los repite.

## 6. Requerimientos funcionales

1. Un cuerpo de reglas heredable y en capas, con precedencia declarada y un núcleo que ninguna instrucción, prompt ni proyecto puede relajar.  ← REQUISITO CENTRAL
2. El ciclo de vida completo, con un molde por entregable y sin excepciones por envergadura.
3. Comprobación automática que detenga lo comprobable, avise lo que exige juicio, y entregue una medida única de cumplimiento por proyecto.
4. Memoria entre sesiones: transcripción, resumen de lo que quedó, señales de lo aprendido y recuerdos del modo de trabajo, escritos por el programa y guardados en el repositorio.
5. Instalación y actualización en cualquier proyecto, con aviso automático cuando el proyecto se quede atrás de la versión del estándar.
6. Un canal de defectos de ida y vuelta entre cada proyecto y el estándar, que cierre el ciclo sin intervención manual.
7. La interfaz: registrar y administrar los proyectos, leer el estándar y la memoria, y mostrar el cumplimiento de todos de un vistazo.

## 7. Restricciones no negociables

- Las reglas del núcleo no se relajan desde ningún proyecto, prompt ni instrucción puntual.
- Ninguna regla nace fuera de un procedimiento escrito, y todo cambio del cuerpo de reglas o de los moldes se versiona y se registra.
- Nada se renumera ni se borra: lo que deja de aplicar se deroga, porque los documentos ya escritos citan por identificador.
- Decidir es del usuario: el agente propone con su recomendación y espera; lo que el usuario ordena se ejecuta de una.
- Todo lo escrito lo entiende quien no sabe del tema: en español correcto, sin jerga innecesaria y sin marcas de generación automática.
- Nada del estándar depende de que el agente se acuerde: lo que hay que cumplir siempre, lo comprueba un programa.

## 8. Casos borde a considerar

- Dos sesiones trabajando a la vez sobre el mismo archivo compartido: la versión, el backlog, un índice.
- Una sesión que se corta a mitad de una fase y deja artefactos sueltos, sin la cadena que los explica.
- Un proyecto cuya ruta tiene espacios, o que cambia de letra de unidad entre una sesión y otra.
- Un validador que reprueba lo que está bien: enseña a ignorar los veredictos, y desde ahí ninguno vuelve a servir.
- Un archivo ilegible, por permisos o por codificación, en medio de una revisión que recorre el repositorio entero.
- Un proyecto que se instala una vez y queda años sin abrirse, mientras el estándar avanza.
- Reglas de dos capas que se contradicen, y el agente tiene que saber cuál gana sin preguntar.

## 9. Referencias

Material del proyecto disponible al redactar este planteamiento:

- [README del estándar](../README.md)
- [Guía de entrada](../base/guia-de-entrada.md)
- [notas/entregables-del-ciclo-de-vida.md](../notas/entregables-del-ciclo-de-vida.md)
- Las palabras del usuario: [la-administracion-de-proyectos-desde-cimiento.md](la-administracion-de-proyectos-desde-cimiento.md), y el índice de [prompts/](README.md)
- El inventario de funcionalidades que acompaña a este planteamiento: [cimiento-inventario-funcionalidades.md](cimiento-inventario-funcionalidades.md)

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
