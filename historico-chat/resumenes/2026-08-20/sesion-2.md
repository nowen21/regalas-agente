# 2026-08-20 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-20-sesion-2.md](../../2026-08-20-sesion-2.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

**Viene de:** —, es trabajo nuevo (la sesión abrió con un saludo y el estándar cargado).

---

## Hallazgos de esta sesión

### H-1 · Este repo está lento porque cada sesión carga `base/` entero a mano, y el enganche no lo carga

- **Qué pasó:** el usuario preguntó por qué este repo está tan lento para contestar. La respuesta que recibió en otra sesión culpó a la cadena (`F23`) y a «cargar `base/` completo a mano porque el enganche no lo hace». Se verificó: en este repo `hook_sesion.py` sale antes de llamar a `cargador.contexto()` (ya lo había encontrado la sesión [core-del-agente-en-la-herramienta](core-del-agente-en-la-herramienta.md), H-2, pendiente [66](../../../pendientes/hecho/las-reglas-llegan-tambien-al-propio-estandar.md)), y el `CLAUDE.md` §0 manda entonces cargar **todos** los archivos de `base/`: 115 archivos, 594 KB (318 KB sin sellos de checklist). Esta misma sesión lo hizo al abrir.
- **Por qué importa:** 594 KB son del orden de 150 000 fichas de contexto antes del primer mensaje. Cada respuesta después arrastra ese peso, y el resumen automático del contexto llega antes y se come primero lo que se cargó. La lentitud no es de la cadena: es del arranque. En los herederos el enganche inyecta 69 KB (`00` y `01` literales, el resto como índice bajo demanda) — ocho veces menos — y eso fue una decisión medida (`cargador.py`). El `CLAUDE.md` de este repo exige lo contrario de lo que el cargador decidió. Corrección a la respuesta anterior de esta sesión: el enganche sí carga `base/` en los herederos, pero **no en este repo**.
- **Qué lo soluciona:** dos piezas, la primera ya disparada.
  1. **Pendiente 66 → fase B de EP-005 · HU-009** (ya escrita, en estación 4): que el enganche le cargue las reglas también al propio estándar, sin el gate `F13`.
  2. **El `CLAUDE.md` §0 de este repo** tiene que pedir lo mismo que da el cargador: núcleo literal, el resto se lee antes de tocar su tema. No toca `base/` ni `plantillas/`: es instructivo del repo, no versiona.
- **Qué se decidió:** sin decidir.
- **Estado:** abierto
- **Responde a:** EP-005 · HU-009 · CA-01 (pieza 1)
- **Dispara:** — (la pieza 2 es una edición del `CLAUDE.md`, no una historia)
- **Orden de resolución:** 1 de 1
- **Dónde queda:** pendiente 66 y su fase; este resumen para la pieza 2
- **Nace en:** 2026-08-20 · sesión 2
- **Cerrado en:** —
- **Con qué se retoma:** ¿aprueba el plan de la fase B de HU-009 y el cambio del §0 del `CLAUDE.md`?

---

## ¿Se puede cerrar la sesión?

Se cierra cuando **ningún hallazgo queda a medias**. Un hallazgo está terminado de una de dos formas, y las dos valen igual:

- **Resuelto acá**, con lo que se hizo escrito en el campo de dónde queda.
- **Anotado**, con su pendiente creado y su historia de usuario disparada escrita. Anotar no es decir "quedó pendiente": es dejar el archivo.

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | N/A — no hay resueltos |
| Todo hallazgo abierto tiene su pendiente creado | ☑ pendiente 66 (pieza 1); la pieza 2 espera decisión |
| Toda historia disparada está escrita en su épica | N/A — no dispara historia nueva |
| Lo que se hizo está aprobado y guardado | ☐ — sin commit |

---

<!-- aviso: resumen sin hallazgos -->

<!-- aviso: falta decir si la sesión se puede cerrar -->

**No se puede cerrar todavía:** H-1 espera la aprobación del plan de la fase B de HU-009 y la decisión sobre el §0 del `CLAUDE.md`.
