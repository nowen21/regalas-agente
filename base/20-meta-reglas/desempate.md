# El orden del desempate, anexo de `20·M6`

> Anexo del capítulo [`20 · Meta-reglas`](base.md). **No es una regla**: no lleva molde ni identificador propio. Es el orden que [`M6`](reglas/M6-ante-un-conflicto-el-desempate-es-este-y-en-este-orden.md) manda seguir, escrito aparte para que la regla quepa en su molde y el orden no se resuma nunca.

Se recorre **de arriba abajo** y se para en el primero que aplique:

1. **¿Una es `[BLINDADA]`?** → gana esa. Fin. No hay paso 2.
2. **¿Una es de capa 3 y la otra de capa 2?** → gana la de capa 3, **solo si** el proyecto la declaró como ajuste explícito (`CLAUDE.md §5.1` o `.agente/reglas-proyecto.md`). El silencio no es un ajuste.
3. **¿Una deroga expresamente a la otra?** → gana la que deroga.
4. **Misma capa:** gana la **más específica**, la que nombra el caso, sobre la general.
5. **Igual de específicas:** gana la **más restrictiva**, la que exige más. Ante la duda, el lado seguro.
6. **Sigue empatado** → es un **defecto del estándar**, no una decisión del agente: **PAUSAR**, reportar el choque al usuario y arreglar la regla. Prohibido elegir en silencio o inventar un tercer camino.

**El paso 6 es el que importa.** Los cinco primeros resuelven; el sexto reconoce que el estándar tiene un defecto, y ahí la salida no es elegir: es pausar, reportar el choque y arreglar la regla.
