# Pendiente · Buscar en el repositorio antes de preguntar

**Estado:** **cerrado** el 2026-08-18. Anotado el 2026-08-14 · nace del hallazgo H-1 del [2026-08-14 · h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido](../historico-chat/resumenes/2026-08-14/h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.md).

| | |
|---|---|
| **Historia de usuario** | [EP-001 · HU-011 — Buscar en el repositorio antes de preguntar](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-011-buscar-antes-de-preguntar/HU-011-buscar-antes-de-preguntar.md) — el propio pendiente la redactó; acá queda creada con ese texto |

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

---

# Cómo cerró — 2026-08-18

Nace [`01·C23` · Busca en el repositorio antes de preguntar](../base/01-conducta.md#c23--busca-en-el-repositorio-antes-de-preguntar), con su bloque de checklist en **CUMPLE**. La fase es [`A-EP-001-HU-011`](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-011-buscar-antes-de-preguntar/A-EP-001-HU-011-la-regla-de-buscar-antes-de-preguntar/).

## El orden de búsqueda, que era lo único que faltaba decidir

**La historia y su §9 · la épica · el resumen de sesión · el histórico · la memoria.** De lo más específico a lo más general, y se para en cuanto se encuentra.

**No salió de una preferencia:** salió de dónde el estándar ya manda escribir cada cosa. Una decisión sobre una historia vive en la historia antes que en el histórico, y por eso ese es el orden.

## El límite que este pendiente ponía, respetado

Decía: *«no es "no preguntes"; preguntar lo que no está decidido es lo que evita adivinar»*. La regla **no reduce las preguntas, cambia cuáles** — y su fila 16 lo deja escrito: que se pregunte lo que no está escrito no es un caso exento, es la regla funcionando.

## Dos cosas que destapó el plan de pruebas

**1 · La primera redacción no cubría un criterio.** El `CA-03` —mostrar la contradicción cuando lo escrito choca con lo pedido— no estaba. La regla hablaba del caso en que lo escrito **responde**, no del que **contradice**. El caso `CP-001` lo marcó como dudoso **antes** de ejecutar, y tenía razón.

**Se corrigió la regla, no el criterio**, que es lo que el propio plan mandaba. Leyendo la regla contra la historia sin ese caso escrito se habría dado por cubierto.

**2 · No cabía en el molde:** 368 caracteres para 320. Lo que sobraba era el **porqué** del orden, y se fue a la historia. Es el mismo defecto que hoy tienen 78 reglas del cuerpo, cometido en una regla escrita con el checklist a la vista.

## Lo que queda abierto

**La mitad comprobable no tiene programa.** Que el agente haya buscado no se puede ver; que la respuesta traiga su cita, sí — y nada lo comprueba. Está declarado en [validadores/reglas-validables.md](../validadores/reglas-validables.md).

Sin eso, `C23` depende de que el agente se acuerde, que es exactamente lo que el [58](58-nada-hace-cumplir-id9.md) describe para `ID9` y lo que allí falló siete veces en tres días.
