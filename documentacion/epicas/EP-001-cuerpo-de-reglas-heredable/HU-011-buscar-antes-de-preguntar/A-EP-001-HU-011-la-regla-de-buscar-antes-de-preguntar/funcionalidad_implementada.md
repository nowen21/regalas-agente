# Funcionalidad implementada — Fase A-EP-001-HU-011

| Campo | Valor |
|---|---|
| **Cierra** | El [pendientes/hecho/buscar-en-el-repositorio-antes-de-preguntar.md](../../../../../pendientes/hecho/buscar-en-el-repositorio-antes-de-preguntar.md) |
| **Fecha de cierre** | 2026-08-18 |
| **Veredicto** | **Cumple** — [resultado_pruebas.md](resultado_pruebas.md) §5 |
| **Versión** | 23.5.0 (**MENOR** — regla nueva, aditiva) |

## Qué hay ahora que antes no había

**[`01·C23` · Busca en el repositorio antes de preguntar](../../../../../base/01-conducta.md#c23--busca-en-el-repositorio-antes-de-preguntar)**, con su bloque de checklist en **CUMPLE** — 19 ✅, 0 ❌, 1 N/A.

Antes de pedirle una decisión al usuario se busca si ya la dejó escrita, **en este orden**: la historia y su §9 · la épica · el resumen de sesión · el histórico · la memoria. De lo más específico a lo más general, y se para en cuanto se encuentra.

- **Si está**, se sigue **citando dónde** — o se muestra, si contradice lo que el usuario acaba de pedir.
- **Si no está**, se pregunta **diciendo dónde se buscó**.

**Extiende [`01·C7`](../../../../../base/01-conducta.md#c7--ante-dos-lecturas-pregunta)**, y esa es la relación exacta: `C7` manda preguntar ante dos lecturas y **da por hecho que el dato no está**. `C23` agrega el paso previo.

## Lo que no hace, y está escrito

**No reduce las preguntas.** Preguntar lo que de verdad no está decidido es lo que evita adivinar. Cambia **cuáles**, no cuántas — y por eso su fila 16 dice N/A: que se pregunte lo que no está escrito no es un caso exento, es la regla funcionando.

## Lo que se decidió y no estaba decidido

**El orden de búsqueda**, que era lo único que la historia dejaba abierto. No salió de una preferencia: salió de **dónde el estándar ya manda escribir cada cosa**. Por eso va de lo más específico a lo más general — la decisión sobre una historia vive en la historia antes que en el histórico.

## Lo que se supo

**El plan de pruebas encontró lo que la lectura no.** Su caso `CP-001` marcó, antes de ejecutar, que el `CA-03` era el dudoso — y lo era: la primera redacción no cubría el caso de que lo escrito **contradiga** lo pedido. Leyendo la regla contra la historia sin ese caso escrito se habría dado por cubierto, porque la regla *habla* de lo que está escrito y de un vistazo parece cubrirlo todo.

**Se corrigió la regla, no el criterio**, que es lo que el propio plan mandaba hacer.

Y una segunda: **la regla no cabía en su primera redacción** —368 caracteres para un molde de 320—. Lo que sobraba era el **porqué** del orden, y se fue a la historia. Es exactamente lo que la fila 10 manda, y el mismo defecto que hoy tienen 78 reglas del cuerpo.

## Lo que queda abierto

**La mitad comprobable no tiene programa.** Que el agente haya buscado no se puede ver; que la respuesta traiga su cita, sí — y nada lo comprueba. Declarado en [validadores/reglas-validables.md](../../../../../validadores/reglas-validables.md), y es su propia fase.

Sin eso, `C23` depende de que el agente se acuerde, que es lo que el [pendientes/hecho/nada-hace-cumplir-id9.md](../../../../../pendientes/hecho/nada-hace-cumplir-id9.md) describe para `ID9` y lo que allí ya falló siete veces en tres días.
