<!-- sesion: 62b1cf41-f44d-4e11-aa33-5b57f96a9ab1 -->

# 2026-08-08 — La instalacion se hace sola

## Conversación

### 1 · Usuario — 2026-08-08 15:27:10
> <ide_opened_file>The user opened the file c:\Ing. Jose\ia\agente\plantillas\CLAUDE.md.plantilla in the IDE. This may or may not be related to the current task.</ide_opened_file>
> Corrija el proceso de instalación para que `CLAUDE.md` sea tratado como el **setup principal del agente**.
>
> El objetivo es que, al ejecutar el proceso de instalación, el agente sea capaz de **instalar, configurar y dejar completamente operativo el entorno por sí mismo**, sin depender de que el usuario tenga que intervenir manualmente.
>
> El proceso debe cumplir con lo siguiente:
>
> * `CLAUDE.md` debe contener las instrucciones necesarias para que el agente pueda realizar correctamente su propio proceso de instalación y configuración.
> * El agente debe detectar automáticamente el estado actual del proyecto y determinar qué elementos hacen falta.
> * Debe crear, modificar o configurar automáticamente los archivos, carpetas, estructuras y componentes necesarios para dejar la instalación completa y funcional.
> * **No debe preguntar al usuario** por decisiones que ya estén definidas en `CLAUDE.md`, las reglas del agente o la estructura estándar del proyecto.
> * **No debe exigir al usuario guardar, copiar, mover o crear manualmente ningún archivo** como parte del proceso de instalación.
> * Si el proyecto no cumple con la estructura requerida, el agente debe realizar las acciones necesarias para adecuarlo automáticamente, siempre respetando las reglas establecidas.
> * El proceso debe ser **idempotente**: si se ejecuta nuevamente sobre un proyecto ya instalado, debe detectar lo que ya existe y no duplicar ni sobrescribir innecesariamente elementos.
> * Al finalizar, debe validar que toda la estructura y configuración requerida esté correctamente instalada y operativa.
> * Si encuentra un problema que realmente impida continuar y que no pueda resolverse automáticamente sin una decisión del usuario, debe detenerse e informar claramente cuál es el bloqueo y por qué requiere intervención.
>
> Revise y corrija **todo el proceso de instalación actual** para eliminar cualquier paso que contradiga este comportamiento.
>
> El resultado esperado es que el usuario pueda iniciar el proceso de instalación y que el agente, utilizando `CLAUDE.md` como su setup y fuente de instrucciones, **se encargue de todo el proceso hasta dejarlo correctamente instalado y listo para trabajar**, sin depender de instrucciones adicionales del usuario.

**Agente** — 2026-08-08 16:12:58
<!-- agente: 99f4407b-641d-49ac-a2cf-99ab28696da4 -->

I'll start by understanding the current installation process before changing anything.

Now I have the full picture. Let me rewrite the template — `CLAUDE.md` becomes the agent's setup.

Now the installer — the core of the change:

Now the seal helper and the checklist wiring:

I need to fix two things: keep section titles stable (so old projects don't get everything re-appended), and exempt the standard's own folder.

Now the standard's own folder must be exempt from the project-setup pieces:

Now let me test end-to-end on a scratch project:

Now the stack list — every row must point at the one command:

Now the rule itself — `F13` currently forbids what the installer must do:

Now update the chapter text that describes F13's old behavior:

Now `sesion.py`, whose start-of-session check still treats the missing folder as a stop:

Now the remaining docs that describe the old flow:

Now the standard's own link/index validation:

Final end-to-end check on a clean project, including the version bump:

Listo. El proceso de instalación ahora es una sola línea que el agente corre solo.

**Qué cambió**

`plantillas/CLAUDE.md.plantilla` abría con un recuadro *"BORRAR ESTE RECUADRO"* y cuatro instrucciones para el usuario — copiar el archivo, reemplazar cada `«…»`, editar el `.gitignore`, anotar el proyecto en el registro central. **Ese recuadro era el proceso de instalación**, y era lo que fallaba: hasta que alguien lo hiciera, el proyecto trabajaba sin reglas. Ahora arranca con la sección **Instalación** y la única línea que hay que correr.

[validadores/instalar.py](validadores/instalar.py) pasó de instalar enganches a instalar el proyecto entero: estructura base, `CLAUDE.md` generado desde la plantilla con las rutas de la máquina, `.gitignore`, los 4 archivos de `.agente/`, histórico, memoria, enganches de git y de Claude Code, fila en el registro central, registro de versión — y al terminar corre el checklist y reporta lo que quede.

Los siete puntos que exigían al usuario ya no lo hacen: `f13`, `claude-md`, `gitignore`, `agente-config`, `documentacion`, `registro` y `version`.

**Reglas que contradecían esto, corregidas**

- [`02·F13`](base/02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md) — de *"Detente si el proyecto no tiene su estructura base"* a *"Deja la estructura base puesta antes de trabajar"*. Crear una carpeta que la norma exige no es una decisión. Lo que sí sigue siendo del usuario, y la regla lo dice más fuerte: **qué va dentro de `proyectos/`** — el agente crea la carpeta vacía y nunca mueve código existente.
- [`01·C18`](base/01-conducta.md) — pedía *"avisa y ofrece aplicarlos"*, una pregunta cuya única respuesta útil es "sí" y que mientras no se contestaba dejaba el `CLAUDE.md` viejo. Ahora se aplica y **se reporta qué se agregó**; sigue sin pisar ni borrar lo escrito.

**Verificado**

| Escenario | Resultado |
|---|---|
| Proyecto vacío, desde cero | 13 de 13 componentes |
| Segunda corrida (idempotencia) | 13 de 13, todo "ya estaba" |
| Proyecto con el `CLAUDE.md` viejo | 13 de 13; agrega solo las 2 secciones nuevas, conserva el opt-in `17: sí` y la sección propia |
| Proyecto con código suelto en `src/` | 13 de 13; crea `proyectos/` vacía y **no mueve** `src/` |
| Suite de validadores | 212 pruebas OK (6 nuevas) |
| Coherencia del estándar | sin incumplimientos |

`VERSION` a **5.0.0** (MAYOR: `F13` cambia de exigencia) con su entrada en [CHANGELOG.md](CHANGELOG.md).

Dos cosas que dejé fuera a propósito: la carpeta del propio estándar no recibe configuración de proyecto (no es un proyecto que use el agente — y un `.gitignore` con `CLAUDE.md` le borraría su instructivo del repositorio), y el checklist de `F13` quedó anulado por la reescritura, a re-aplicar en el próximo repaso del capítulo `02`.

No hice commit — queda para tu revisión.

### 2 · Usuario — 2026-08-08 22:34:43
> suba a git

**Agente** — 2026-08-08 22:37:21
<!-- agente: 89fa5faf-57b0-4f7a-b52f-5df2a7fa53fc -->

Todo lo de esta sesión está preparado; el trabajo de otras sesiones (`base/README.md`, `2026-08-07-sesion-12.md`, `pendientes/10-ideas.md`, los dos históricos del 07) queda fuera.

**Archivos — 21, +757 −235**

```
CHANGELOG.md · VERSION
base/01-conducta.md                                  C18 se aplica sola
base/02-flujo-de-trabajo/base.md · estructura-base.md
base/02-flujo-de-trabajo/reglas/F13-…                renombrada + reescrita
plantillas/CLAUDE.md.plantilla · stack-instalacion.md
validadores/instalar.py (+413) · checklist.py · sesion.py · versiones.py
validadores/pruebas.py (6 pruebas nuevas) · cargador.py · README.md
anatomia/componentes-del-agente.md · mapa-del-sitio.md
analisis/base-2026-08-07-…md                         solo el enlace renombrado
historico-chat/2026-08-08-sesion.md · README.md
```

**Mensaje**

```
estandar: la instalación se hace sola y CLAUDE.md es el setup (5.0.0)

El proceso de instalación no puede depender de que el usuario guarde, copie o
cree archivos a mano. Al correrlo, el agente tiene que dejar el entorno
completo y operativo por sí mismo: detectar qué falta, crearlo, no preguntar
lo que el estándar ya decidió, y detenerse solo ante un bloqueo real que
necesite una decisión. CLAUDE.md es su setup y de ahí salen las instrucciones.

Se quitó el recuadro de pasos manuales de plantillas/CLAUDE.md.plantilla. Ese
recuadro era el proceso de instalación, y era lo que fallaba: hasta que
alguien hiciera los siete pasos, el proyecto trabajaba sin reglas. En su lugar
va la sección Instalación, con la única línea que hay que correr.

validadores/instalar.py pasa de instalar enganches a instalar el proyecto
entero: estructura base, CLAUDE.md generado desde la plantilla con las rutas
de la máquina, .gitignore, los 4 archivos de .agente/, histórico, memoria,
enganches de git y de Claude Code, registro central y registro de versión. Al
terminar corre el checklist y reporta lo que quede. Es idempotente y no pisa
lo que el proyecto escribió.

02·F13 pasa de "Detente si el proyecto no tiene su estructura base" a "Deja la
estructura base puesta antes de trabajar": crear una carpeta que la norma
exige no es una decisión. Qué va dentro de proyectos/ sí lo es, y el agente
nunca mueve código existente. 01·C18 deja de preguntar si aplica lo que el
estándar ya decidió: lo aplica y reporta qué agregó.

Verificado desde cero, en segunda corrida, sobre un CLAUDE.md viejo y sobre un
proyecto con código suelto: 13 de 13 componentes. 212 pruebas OK, coherencia
del estándar sin incumplimientos.
```

`G7` pide que leas el mensaje antes de ejecutar. ¿Le doy commit y push a `main`?

### 3 · Usuario — 2026-08-08 22:37:43
> <ide_opened_file>The user opened the file c:\Ing. Jose\ia\agente\pendientes\10-ideas.md in the IDE. This may or may not be related to the current task.</ide_opened_file>
> si

**Agente** — 2026-08-08 22:39:14
<!-- agente: efe29410-afde-4aab-bef4-b7563ccab008 -->

Subido a `main` — commit `d2f5800`, 21 archivos, +757 −235.

Los enganches pasaron antes de aceptarlo: nada indebido versionado, mensaje conforme a `G2`/`G8`.

Quedó fuera del commit, como corresponde, el trabajo de otras sesiones: [base/README.md](base/README.md), [historico-chat/2026-08-07-sesion-12.md](historico-chat/2026-08-07-sesion-12.md), [pendientes/10-ideas.md](pendientes/10-ideas.md) y las dos transcripciones del 07 que estaban modificadas.
