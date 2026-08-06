# Pendiente · Memoria semántica

**Estado:** abierto · anotado 2026-08-04.

Búsqueda **por significado** sobre `senales.db`, además de la léxica que ya existe. Es el gap identificado en [notas/cobertura-del-agente.md](../notas/cobertura-del-agente.md) como el único que pide una pieza adicional; se formaliza aquí como pendiente del backlog.

## El problema

FTS5 encuentra **palabras**. Si la señal dice "el proveedor rechaza el lote cuando el NIT viene sin dígito de verificación" y el agente busca "error de validación tributaria", no la encuentra — aunque sea exactamente lo que necesita. La memoria tiene la lección y el agente repite el error.

Cuanto más crece la base, peor: más señales relevantes que la búsqueda por palabra no alcanza.

## Qué cubriría

- **Embeddings de las señales** — sobre `titulo` + `what` + `why` + `learned`, los mismos campos que ya indexa FTS5.
- **Búsqueda híbrida** — léxica (FTS5) + semántica, fusionando resultados. No reemplazar: la léxica es mejor para nombres propios, códigos e identificadores exactos.
- **Actualización incremental** — recalcular solo lo que cambió, con los mismos triggers que mantienen `senales_fts`.
- **Sin dependencia de red** — el visor y la memoria funcionan offline hoy; el estándar no debería perder eso.

## Recomendación técnica

**`sqlite-vec` antes que Postgres+pgvector o un MCP externo.** Sigues con un archivo: sin servicio que arrancar, sin backup aparte, sin romper el modo offline, y el acceso ya está centralizado en `memoria.py`. Un MCP externo solo se justifica si la memoria pasa a ser compartida por varias máquinas.

Decisión abierta: **qué modelo genera los embeddings** y si corre local. De eso depende que se cumpla lo de "sin red".

## Relación con otros pendientes

Se apoyaba en el [02 · vigencia y poda de la memoria](hecho/vigencia-y-poda-de-memoria.md) —la búsqueda semántica **agrava** el problema de la memoria vieja: encuentra más señales obsoletas que la léxica—; ya está hecho, así que la vigencia (`revisada`, marca de sin-verificar, recencia en el orden) está en su lugar antes de abrir este.

**Hereda del 02 la detección de contradicciones.** Dos señales activas del mismo scope que se contradicen es un problema semántico, no léxico: un detector por palabras miente en las dos direcciones (se le escapan las dichas con otras palabras, marca de más las del mismo tema). Se resuelve aquí, con embeddings; mientras tanto la cubre el ritual humano de `revisar --viejas`.
