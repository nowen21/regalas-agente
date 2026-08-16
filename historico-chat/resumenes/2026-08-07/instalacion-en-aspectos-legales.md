# 2026-08-07 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-07-instalacion-en-aspectos-legales.md](../../2026-08-07-instalacion-en-aspectos-legales.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

> **Resumen escrito hacia atrás, el 2026-08-16.** La sesión es anterior a la regla que obliga a escribirlo ([`13·DOC22`](../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md)).

**Viene de:** —, es trabajo nuevo.

**Propósito:** instalar el agente en un proyecto del posgrado.

---

## Hallazgos de esta sesión

### H-1 · El instalador se salta lo que no puede deducir, y lo dice

- **Qué pasó:** la instalación quedó en **12 de 13**. Faltaron los enganches de git —ahí no había repositorio— y los cuatro archivos de `.agente/`, que el agente no llenó a propósito: el marco normativo y el dominio son datos del proyecto, no algo que se invente.
- **Por qué importa:** un instalador que rellena lo que no sabe deja un proyecto que **parece** configurado. Dejar el hueco visible, con qué falta y cómo se arregla, es lo que hace que el checklist sirva.
- **Qué lo soluciona:** que lo que depende del proyecto lo llene el agente en la primera sesión abierta ahí, preguntando lo que haga falta.
- **Qué se decidió:** eso mismo. Los cinco capítulos opt-in quedaron en `no` con la nota de que se revisan cuando se defina qué se va a construir.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** el proyecto instalado y su fila en `plantillas/proyectos.md`, que es archivo local y no se versiona.
- **Nace en:** 2026-08-07 · instalación en Aspectos legales.
- **Cerrado en:** 2026-08-07 · instalación en Aspectos legales.
- **Con qué se retoma:** —.

### H-2 · Sin repositorio no hay enganches de commit, y el checklist los daba por omitidos

- **Qué pasó:** al no haber git, `commit-msg` y `pre-commit` no se instalaron. El usuario inició el repositorio y una segunda corrida los puso. El componente pasó de *omitido* a *ok*, pero el checklist siguió en **12 de 13**.
- **Por qué importa:** «omitido» y «cumple» se ven parecido en un conteo. Lo que faltaba de verdad —los cuatro archivos de `.agente/`— era lo mismo antes y después.
- **Qué lo soluciona:** nada que se decidiera acá; es cómo el checklist reporta.
- **Qué se decidió:** se inició `git init -b main`, se pusieron los enganches y no se commiteó nada: el árbol quedó entero sin rastrear.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** el proyecto. Lo que sí quedó dicho y sin resolver es el PDF de 22 MB y el `.docx`: decidir si van al repositorio o al `.gitignore`, porque git no maneja bien binarios grandes que cambian.
- **Nace en:** 2026-08-07 · instalación en Aspectos legales.
- **Cerrado en:** 2026-08-07 · instalación en Aspectos legales.
- **Con qué se retoma:** —.

---

## ¿Se puede cerrar la sesión?

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ los dos |
| Todo hallazgo abierto tiene su pendiente creado | ☑ ninguno quedó abierto |
| Toda historia disparada está escrita en su épica | ☑ ninguno dispara historia |
| Lo que se hizo está aprobado y guardado | ☑ el cambio fue en el otro repositorio |
