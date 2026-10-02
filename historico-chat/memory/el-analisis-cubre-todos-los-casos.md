# El análisis cubre todos los casos, porque Cimiento es la base de todos los proyectos

**Qué se pide.** Un análisis considera todo lo que puede pasar en cualquier proyecto que herede Cimiento: otras herramientas, otros agentes, otros sistemas y otras formas de hacer lo mismo. No se queda en el caso que destapó el hallazgo. Y en el análisis se propone todo lo que haga falta discutir, porque es la etapa donde las posibilidades se evalúan y se aprueban antes de decidir cómo se procede.

**Por qué.** El 2026-10-02 el agente escribió fuera del proyecto por la consola y en segundo plano, y propuso ampliar el freno solo a la consola. El usuario lo corrigió: *«Entienda que Cimiento es la base de todos los proyectos que lo implementan. Por lo tanto, los análisis deben realizarse considerando todas las posibilidades que puedan presentarse, y no pensando únicamente en un caso particular.»* Una solución para un solo caso deja abiertos los demás, y el hallazgo vuelve por otro lado.

**Cómo se aplica.**

- Antes de proponer, listar todas las formas en que puede pasar lo mismo, en cualquier herramienta o proyecto, y decir cuáles cubre cada propuesta.
- En el análisis se proponen todas las opciones que haga falta, con su recomendación. Fuera del análisis rige [`01·C30`](../../base/01-conducta.md#c30--no-agregues-lo-que-no-se-pidió): no se agrega lo que no se pidió.

Relacionado: [decidir es del usuario](decidir-es-del-usuario.md) · [todo multiproyecto](todo-multiproyecto.md).
