# Pendiente · El glosario, y lo que quedó en inglés

**Estado:** **cerrado** el 2026-08-18 · anotado 2026-08-14 · nace del hallazgo H-8 de [historico-chat/resumenes/2026-08-14/hu-de-la-comprobacion-automatica.md](../../historico-chat/resumenes/2026-08-14/hu-de-la-comprobacion-automatica.md).

| | |
|---|---|
| **Historia de usuario** | [EP-003 · HU-010 — Glosario de la terminología](../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/HU-010-glosario-de-la-terminologia.md) — el glosario es esa historia, y los trece roles en inglés son su otra mitad |

## El problema

El 2026-08-14 se tradujo "spec" a "especificación" en 53 archivos y nació [`01·C20`](../../base/01-conducta.md#c20--la-palabra-de-otro-idioma-se-traduce-y-si-no-se-puede-se-explica). Quedaron dos cosas sin hacer:

**Los nombres de los roles siguen en inglés.** Las trece estaciones del flujo se llaman Explorer, Proposer, Épica Writer, HU Writer, Spec Writer, Designer, Task Planner, Implementer, Verifier, Crítico, y así. Es el mismo incumplimiento de `C8` que se acaba de corregir en el texto.

**No hay glosario.** La terminología del estándar está repartida en las reglas que usan cada palabra, así que para entender un término hay que leer el capítulo entero.

## Qué falta

**1. El glosario.** **Hecho el 2026-08-14**, estándar 15.3.0. Está en [base/glosario.md](../../base/glosario.md): 72 términos en cuatro grupos, cada uno en una línea, con quién lo escribe, dónde vive y qué regla lo manda. Lo entregó la fase [documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/A-EP-003-HU-010-glosario-de-la-terminologia/README.md](../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/A-EP-003-HU-010-glosario-de-la-terminologia/README.md).

Salieron 72 y no los treinta que se estimaban. No se recortó: entra todo lo que aparece en una regla o en una plantilla, y las 67 lo cumplen.

**2. Los roles.** **Hecho el 2026-08-18**, estándar 23.8.0. 211 apariciones en 39 archivos, y cuatro archivos renombrados con sus citas arrastradas. `00·ID6` reselló su checklist. **Queda la carpeta `skills/generar-spec-modulo/`**: el nombre de una skill es cómo se la invoca, así que renombrarla cambia comportamiento y va aparte.

~~Sigue abierto.~~ El glosario ya dejó el inventario: **12 términos con traducción usada que todavía están en inglés**, cada uno con el archivo donde vive, en la sección [Lo que sigue en otro idioma](../../base/glosario.md#lo-que-sigue-en-otro-idioma). Son trece nombres en diez archivos entre `base/`, `plantillas/`, `skills/` y `notas/`, más los nombres de archivo que llevan `spec`.

Renombrar un archivo rompe todo enlace que apunte a él, así que el cambio va de una vez, con su historia de usuario y su plan. No de a poco.

## El límite

El glosario no es una regla: es un anexo, como la lista de marcadores. No lleva checklist, pero sí entrada en el registro de cambios y subida de versión.
