# Planteamiento — Cimiento, el estándar del agente   ·   `[CAPA 3]`

**Encuadre.** Este es el planteamiento de entrada de Cimiento mismo: el problema que resuelve, para quién y qué no negocia. Se escribió el 2026-08-22 con lo que el proyecto ya tenía dicho (el README, los pedidos del usuario en `prompts/`, su dirección del 2026-08-21) y por instrucción del usuario: «los puede responder usted mismo con lo que ya se tiene del proyecto». Cierra el pendiente 56: el estándar exigía a todos un planteamiento y no tenía el suyo.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Nombre del proyecto** | Cimiento (el estándar del agente; su repositorio es `agente/`) |
| **Qué cubre este encargo** | Todo el proyecto |
| **Fecha** | 2026-08-22 (la primera versión del estándar es de julio de 2026) |

## 1. Necesidad — en una frase

Que desarrollar software con un agente de IA sea **predecible, seguro y consistente** en cualquier proyecto, sin que cada sesión reinterprete el proyecto a su manera.

## 2. Contexto

Quien desarrolla con un agente de IA se encuentra, sesión tras sesión, con lo mismo: el agente reinventa el diseño y contradice decisiones previas, olvida el contexto y toma decisiones funcionales por su cuenta, aplica o ignora las buenas prácticas según el día, y puede ejecutar acciones peligrosas: tocar datos reales, publicar cambios, exponer secretos. El usuario que vive esto lleva varios proyectos a la vez (hoy, diez en esta máquina, de stacks distintos: Laravel, Django, Angular, Python) y no puede vigilar cada conversación.

Cimiento es la respuesta: un cuerpo de reglas versionado que el agente lee **antes de actuar**, un ciclo de desarrollo que no se salta eslabones, moldes para cada entregable, programas que comprueban que todo eso se cumple sin depender de la memoria de nadie, y una memoria que persiste entre sesiones. Cada proyecto hereda la base y la extiende con lo suyo sin tocarla.

**La dirección del usuario, con sus palabras (2026-08-21):** «La idea es que Cimiento sea el mecanismo que obligue a cada proyecto a cumplir con los estándares y reglas definidos. Para lograrlo, la interfaz de Cimiento debe permitir administrar y gestionar todos los proyectos directamente desde la aplicación.» Y sobre el ciclo: «el ciclo de vida no hace excepciones»; todos sus entregables existen en todo proyecto, sin importar envergadura.

> El punto de partida (un solo usuario, todo corre en su máquina) **no es un límite del diseño**: el estándar se escribe agnóstico de stack y de dominio para que sirva a cualquier proyecto y a cualquier agente.

## 3. Objetivo y criterio de éxito

- **Objetivo:** que cualquier proyecto del usuario, al instalar Cimiento, quede obligado a recorrer el ciclo de vida completo con sus entregables, bajo las mismas reglas, y que Cimiento pueda decir en cualquier momento si lo cumple.
- **Criterio de éxito (medible):**
  1. En cada proyecto instalado, la revisión de instalación da el total de sus puntos (hoy «14 de 14») y el expediente del ciclo muestra sus entregables presentes y completos (`validar.py expediente`).
  2. Ninguna acción irreversible, ningún dato real tocado y ninguna credencial escrita ocurre sin autorización explícita del usuario (el núcleo blindado, `00·N1` a `00·N6`), y queda rastro de cada sesión en el histórico.
  3. Un defecto del estándar que un proyecto encuentra llega al estándar, se corrige una vez, y el aviso vuelve a todos los instalados: el ciclo se cierra sin que el usuario tenga que acordarse.

## 4. Alcance esperado

- **Qué SÍ se pide:** el cuerpo de reglas por capas (núcleo, convenciones, capa de proyecto); el ciclo de vida con sus moldes y entregables; los validadores y enganches que lo hacen cumplir sin IA; la memoria entre sesiones (histórico, señales, recuerdos); el instalador que lleva todo a cada proyecto; y la interfaz que administra los proyectos y muestra su cumplimiento.
- **Qué NO se pide / fuera de alcance:** reglas atadas a un lenguaje, un framework o un cliente (esas las declara cada proyecto en su capa 3); decidir por el usuario lo que es suyo (alcance, aprobaciones, derogaciones); y sustituir el criterio de quien lee: los programas comprueban lo contable, las personas juzgan lo demás.

## 5. Restricciones técnicas

Python sin dependencias fuera de la biblioteca estándar para todo lo que viaja a los proyectos (validadores, enganches), para que corra en cualquier máquina. La interfaz es Django con MariaDB (puerto 3307) y vive solo en la máquina del usuario. El adaptador a la herramienta (hoy Claude Code) se mantiene aparte para que el resto sirva a cualquier agente. Los datos verificados del entorno están en el registro de proyectos de la interfaz, no acá.

## 6. Requerimientos funcionales

1. Un cuerpo de reglas heredable, por capas, con precedencia clara y un núcleo que nada sobrescribe.  ← REQUISITO CENTRAL
2. El ciclo de vida completo con un molde por entregable, sin excepciones por envergadura.
3. Comprobación automática: validadores y enganches que detienen lo comprobable y avisan lo que exige juicio.
4. Memoria entre sesiones: transcripción literal de cada sesión, resumen de lo que dejó, señales de lo aprendido y recuerdos de cómo trabaja el usuario.
5. Instalación y actualización en cualquier proyecto, con aviso de desfase de versión.
6. Un canal de defectos de ida y vuelta entre cada proyecto y el estándar.
7. La interfaz: leer el estándar y la memoria, administrar el registro de proyectos y medir el cumplimiento de cada uno.

## 7. Restricciones no negociables

- Las reglas del núcleo blindado no se relajan desde ningún proyecto, prompt ni instrucción puntual.
- Ninguna regla nace fuera del procedimiento del capítulo `20`, y todo cambio de `base/` o `plantillas/` se versiona y se registra.
- Decidir es del usuario: el agente propone con recomendación y espera; lo ordenado se ejecuta de una.
- Todo lo escrito lo entiende quien no sabe del tema, en español correcto y sin marcas de generación automática.

## 8. Casos borde a considerar

- Dos sesiones trabajando a la vez sobre el mismo archivo compartido (ya pasó con la versión y el backlog).
- Una sesión que muere a mitad de una fase y deja artefactos sin cadena (ya pasó; señal S-018).
- Un proyecto cuya ruta tiene espacios o cambia de letra de unidad (ya pasó; pendientes 71 y 72).
- Un validador que reprueba lo que está bien: enseña a ignorar todos los veredictos (señal S-019).

## 9. Referencias

- [README](../README.md) del estándar · [guía de entrada](../base/guia-de-entrada.md) · [notas/entregables-del-ciclo-de-vida.md](../notas/entregables-del-ciclo-de-vida.md).
- Las palabras del usuario: [la-administracion-de-proyectos-desde-cimiento.md](la-administracion-de-proyectos-desde-cimiento.md) y el índice de [prompts/](README.md).
- El inventario de funcionalidades que acompaña este planteamiento: [cimiento-inventario-funcionalidades.md](cimiento-inventario-funcionalidades.md).

## 10. Épicas derivadas

> Cimiento se documentó hacia atrás: sus siete épicas existían antes que este planteamiento. Acá quedan enlazadas para que la cadena se pueda recorrer en las dos direcciones.

| Épica | Título | Estado |
|---|---|---|
| [EP-001](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/epica.md) | Cuerpo de reglas heredable y en capas | En curso |
| [EP-002](../documentacion/epicas/EP-002-versionado-y-adopcion/epica.md) | Versionado y adopción | En curso |
| [EP-003](../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/epica.md) | Documentos modelo y procedimientos | En curso |
| [EP-004](../documentacion/epicas/EP-004-comprobacion-automatica/epica.md) | Comprobación automática | En curso |
| [EP-005](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/epica.md) | Automatismos que no dependen de la memoria | En curso |
| [EP-006](../documentacion/epicas/EP-006-memoria-de-lo-aprendido/epica.md) | Memoria de lo aprendido | En curso |
| [EP-007](../documentacion/epicas/EP-007-instalacion-y-actualizacion/epica.md) | Instalación y actualización | En curso |
