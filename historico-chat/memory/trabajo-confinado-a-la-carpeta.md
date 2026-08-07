# Trabajo confinado a la carpeta

Mientras se trabaja un tema del estándar, **todo lo que se cree o se edite va únicamente dentro de la carpeta de ese tema**. No se toca el capítulo padre, ni `VERSION`, ni `CHANGELOG.md`, ni ningún otro archivo del repo. **El usuario indica cuándo replicar.**

**Por qué:** el modelo en construcción todavía se está validando. Aplicarlo al resto del estándar antes de que el usuario lo apruebe convierte un borrador en norma vigente — y `M10` (versionar + CHANGELOG) hace que ese salto parezca obligatorio cuando en realidad presupone una aprobación que no se dio. Aprobar el cambio y aprobar su propagación son dos permisos distintos, igual que aprobar el cambio no es aprobar el commit.

**Cómo se aplica:** al crear un anexo o documento nuevo bajo `base/<tema>/`, entregar solo ese archivo y **decirlo**: *"queda suelto; el enlace desde el capítulo, `VERSION` y `CHANGELOG` los hago cuando me digas"*. Nunca ejecutarlos por iniciativa propia, aunque `M10` los exija: la exigencia arranca cuando el cambio se adopta.

Relacionado: [aprobar antes de commit](aprobar-antes-de-commit.md) · [una pregunta no es una instrucción](pregunta-no-es-instruccion.md).
