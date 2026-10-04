# Lo que un proyecto reporta es un defecto de todos

**Qué se pide.** Todo lo que un proyecto reporta a Cimiento es un defecto que ya está en todos los proyectos que lo usan. No se analiza como un caso aislado: se busca su causa en Cimiento, se revisa cómo afecta a los demás proyectos y se corrige en la raíz. Nada se plantea pensando solo en Cimiento: antes se analiza que funcione en los proyectos que lo usan.

**Por qué.** El 2026-10-04, al atender los cinco reportes de scilit, el agente empezó a corregirlos pensando en Cimiento y con «Corrija», como si fueran fallas sueltas. El usuario lo detuvo: «nada se puede hacer pensando únicamente en Cimiento» y «lo que un proyecto reporta no se soluciona únicamente para ese proyecto, sino que se utiliza para mejorar Cimiento y, con ello, beneficiar a todos los proyectos que lo implementan».

**Cómo se aplica.**

- Un reporte abre análisis: «Corrija» es para lo que bloquea el trabajo dentro de Cimiento.
- Los proyectos son los de la base de datos de la interfaz, no los de `plantillas/proyectos.md`; cada causa se revisa en todos.
- Cada arreglo se prueba desde un proyecto que no es Cimiento.
- Es la regla [`02·F29`](../../base/02-flujo-de-trabajo/reglas/F29-el-reporte-de-un-proyecto-se-corrige-para-todos.md).

Relacionado: [todo multiproyecto](todo-multiproyecto.md), [el análisis cubre todos los casos](el-analisis-cubre-todos-los-casos.md).
