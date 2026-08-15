# Pendiente · Buscar en el repositorio antes de preguntar

**Estado:** abierto · anotado 2026-08-14 · nace del hallazgo H-1 del [2026-08-14 · h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido](../historico-chat/resumenes/2026-08-14/h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.md).

## El problema

El agente le preguntó al usuario en qué orden trabajar dos historias, ofreciéndole tres opciones. La respuesta ya estaba escrita: [HU-008](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/HU-008-enganche-del-resumen.md) declara en su sección 9 que depende de HU-009, con impacto alto.

La pregunta tenía premisa falsa: cualquiera de las tres respuestas habría contradicho una dependencia ya escrita. Y le devuelve al usuario el trabajo de leer lo que él mismo dejó escrito.

## Qué falta

**Escribir la historia y decidir dónde vive la regla.** Hoy existe la exigencia de que el pedido incompleto se pregunta en vez de adivinarse, y funcionó: el agente preguntó. Falta el paso previo.

**La historia que dispara:**

> **EP-001 · HU-011 — buscar en el repositorio antes de preguntar**
> - **Como** quien ya dejó una decisión escrita
> - **Quiero** que se busque antes de preguntármela
> - **Para** no volver a decidir lo que ya está decidido
> - **Contexto:** falta decir dónde se busca (la historia y su sección de dependencias, la épica, el resumen de sesión, el histórico) y qué se hace cuando lo escrito y el pedido se contradicen. Preguntar sigue siendo lo correcto cuando de verdad no está escrito.

## El límite

No es "no preguntar". Preguntar lo que no está decidido es lo que evita adivinar. Lo que esta regla ataca es preguntar lo que **sí** está decidido, que es distinto y se nota en que la respuesta ya existe en un archivo.
