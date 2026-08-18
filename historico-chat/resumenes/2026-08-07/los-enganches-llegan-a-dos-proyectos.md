# 2026-08-07 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-07-los-enganches-llegan-a-dos-proyectos.md](../../2026-08-07-los-enganches-llegan-a-dos-proyectos.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

> **Resumen escrito hacia atrás, el 2026-08-16.** La sesión es anterior a la regla que obliga a escribirlo ([`13·DOC22`](../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md)).

**Viene de:** —, es trabajo nuevo. Cuatro palabras del propio usuario: *«enganches de histórico instalados»*.

**Propósito:** saber si dos proyectos reales ya guardan el histórico, y ponérselo si no.

---

## Hallazgos de esta sesión

### H-1 · Una herramienta que se autoinstala igual no llega si nadie corre el instalador

- **Qué pasó:** ni LocalHub ni AgroSystem tenían `historico-chat/` ni los enganches. Los dos habían quedado con el `settings.json` de antes: solo `hook_md` y `hook_sesion`.
- **Por qué importa:** el día anterior se había decidido que toda herramienta llega sola por el instalador. Es cierto, pero el instalador corre **al abrir sesión en ese proyecto** — y a un proyecto en el que no se ha trabajado no le llega nada. La herramienta se autoinstala; no se autopropaga.
- **Qué lo soluciona:** correr el instalador contra cada proyecto desde el estándar. Es idempotente.
- **Qué se decidió:** se corrió en los dos. Quedaron los dos enganches, la carpeta con su `README` y el stack de instalación. Lo que ya estaba no se tocó, y se verificó que no quedaran enganches duplicados.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** los dos proyectos, y la memoria [toda herramienta se autoinstala](../../memory/herramienta-se-autoinstala.md).
- **Nace en:** 2026-08-07 · los enganches llegan a dos proyectos.
- **Cerrado en:** 2026-08-07 · los enganches llegan a dos proyectos.
- **Con qué se retoma:** —.

### H-2 · Los dos proyectos no quedaron iguales

- **Qué pasó:** en AgroSystem el instalador además selló el `CLAUDE.md` contra la plantilla y escribió `documentacion/versiones/2026-08-07-2.0.0.md`. En LocalHub no.
- **Por qué importa:** el sello es lo que hace que un documento viejo reprueba el checklist. Un proyecto sin sello figura al día sin que nadie lo haya comprobado — que es justo lo que el sello se construyó para evitar, el día anterior.
- **Qué lo soluciona:** entender por qué difieren. La diferencia está en lo que cada proyecto ya tenía: el sello se pone sobre el `CLAUDE.md` que existe, y LocalHub no llegó a esa condición en esa corrida.
- **Qué se decidió:** nada. Quedó anotado en la respuesta del agente como diferencia entre las dos instalaciones, sin explicar la causa.
- **Estado:** abierto.
- **Responde a:** —.
- **Dispara:** —, es correr el instalador otra vez y mirar.
- **Orden de resolución:** 1 de 1.
- **Dónde queda:** [pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md](../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md).
- **Nace en:** 2026-08-07 · los enganches llegan a dos proyectos.
- **Cerrado en:** —.
- **Con qué se retoma:** ¿LocalHub quedó sin sello por algo del proyecto, o el instalador se saltó el paso?

---

## ¿Se puede cerrar la sesión?

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ H-1 |
| Todo hallazgo abierto tiene su pendiente creado | ☑ H-2 en el [33](../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md) |
| Toda historia disparada está escrita en su épica | ☑ ninguno dispara historia |
| Lo que se hizo está aprobado y guardado | ☑ el cambio fue en los otros dos repositorios; acá no hubo nada que subir |
