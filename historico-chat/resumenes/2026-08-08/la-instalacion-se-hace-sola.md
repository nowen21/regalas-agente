# 2026-08-08 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-08-la-instalacion-se-hace-sola.md](../../2026-08-08-la-instalacion-se-hace-sola.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

> **Resumen escrito hacia atrás, el 2026-08-16.** La sesión es anterior a la regla que obliga a escribirlo ([`13·DOC22`](../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md)). «Responde a» y «dispara» van en `—`: las épicas nacieron el 2026-08-13.

**Viene de:** —, es trabajo nuevo. Un solo pedido largo, y el resto es ejecución.

**Propósito:** que instalar el agente sea correr una línea, y que el agente haga todo lo demás.

---

## Hallazgos de esta sesión

### H-1 · El proceso de instalación era un recuadro que decía «BORRAR ESTE RECUADRO»

- **Qué pasó:** la plantilla del `CLAUDE.md` abría con cuatro instrucciones para la persona: copiar el archivo, reemplazar cada marcador, editar el `.gitignore` y anotar el proyecto en el registro central. **Ese recuadro era el proceso de instalación.**
- **Por qué importa:** hasta que alguien hiciera los siete pasos, el proyecto trabajaba **sin reglas**. Un estándar que depende de un trámite manual no rige: espera.
- **Qué lo soluciona:** que el instalador deje el proyecto entero puesto y el `CLAUDE.md` sea el setup del que salen las instrucciones.
- **Qué se decidió:** [`instalar.py`](../../../validadores/instalar.py) pasó de instalar enganches a instalar el proyecto: estructura base, `CLAUDE.md` generado con las rutas de la máquina, `.gitignore`, los cuatro archivos de `.agente/`, histórico, memoria, enganches de git y de Claude Code, registro central y registro de versión. Al terminar corre el checklist y reporta lo que quede. Los siete puntos que exigían al usuario dejaron de exigirlo.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** versión **5.0.0** del [CHANGELOG](../../../CHANGELOG.md), commit `d2f5800`.
- **Nace en:** 2026-08-08 · la instalación se hace sola.
- **Cerrado en:** 2026-08-08 · la instalación se hace sola.
- **Con qué se retoma:** —.

### H-2 · Dos reglas del estándar prohibían lo que el instalador tenía que hacer

- **Qué pasó:** `F13` decía *«detente si el proyecto no tiene su estructura base»* y `C18` pedía *«avisa y ofrece aplicarlos»*. La primera detenía al agente antes de poder arreglar nada; la segunda hacía una pregunta cuya única respuesta útil es «sí» y, mientras no se contestaba, dejaba el `CLAUDE.md` viejo.
- **Por qué importa:** **crear una carpeta que la norma exige no es una decisión.** Pedir permiso para eso convierte el estándar en un trámite y no protege nada.
- **Qué lo soluciona:** cambiar qué exige cada una, sin cambiarles el número.
- **Qué se decidió:** [`F13`](../../../base/02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md) pasa a *«deja la estructura base puesta antes de trabajar»*, y dice más fuerte lo que **sí** es del usuario: qué va dentro de `proyectos/` — el agente crea la carpeta vacía y **nunca mueve código existente**. `C18` aplica y reporta qué agregó, sin pisar ni borrar lo escrito.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** versión **5.0.0 · MAYOR**, porque `F13` cambia de exigencia.
- **Nace en:** 2026-08-08 · la instalación se hace sola.
- **Cerrado en:** 2026-08-08 · la instalación se hace sola.
- **Con qué se retoma:** —.

### H-3 · Reescribir la regla anuló su checklist y nadie lo notó

- **Qué pasó:** al reescribir `F13` quedó anulado el bloque de checklist que la evaluaba. El agente lo dijo al final: *«a re-aplicar en el próximo repaso del capítulo 02»*.
- **Por qué importa:** el sello es lo que dice que la regla fue evaluada contra el estándar. Una regla reescrita con el sello viejo afirma algo que ya no se comprobó — y `M14` exige el checklist en CUMPLE para publicar.
- **Qué lo soluciona:** re-aplicarlo, o que algo avise cuando el texto de la regla cambia después de su sello.
- **Qué se decidió:** dejarlo anotado. No se re-aplicó.
- **Estado:** abierto.
- **Responde a:** —.
- **Dispara:** —, es aplicar un checklist que ya existe.
- **Orden de resolución:** 1 de 1.
- **Dónde queda:** [pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md](../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md), y se cruza con el [pendiente 19](../../../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).
- **Nace en:** 2026-08-08 · la instalación se hace sola.
- **Cerrado en:** —.
- **Con qué se retoma:** ¿el sello de una regla caduca cuando su texto cambia? Si nada lo comprueba, el checklist envejece en silencio.

### H-4 · El estándar no es un proyecto que use el agente

- **Qué pasó:** al probar el instalador hubo que eximir a la carpeta del propio estándar de recibir la configuración de proyecto.
- **Por qué importa:** un `.gitignore` con `CLAUDE.md` —que es lo correcto en un proyecto— le habría borrado del repositorio su propio instructivo, que es justamente lo que este repositorio necesita versionar.
- **Qué lo soluciona:** que el instalador reconozca su propia carpeta y no se instale a sí mismo.
- **Qué se decidió:** la exención quedó puesta y probada.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [`instalar.py`](../../../validadores/instalar.py).
- **Nace en:** 2026-08-08 · la instalación se hace sola.
- **Cerrado en:** 2026-08-08 · la instalación se hace sola.
- **Con qué se retoma:** —.

---

## ¿Se puede cerrar la sesión?

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ H-1, H-2 y H-4 |
| Todo hallazgo abierto tiene su pendiente creado | ☑ H-3 en el [33](../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md) |
| Toda historia disparada está escrita en su épica | ☑ ninguno dispara historia |
| Lo que se hizo está aprobado y guardado | ☑ commit `d2f5800`, 21 archivos, dejando fuera lo de otras sesiones |
