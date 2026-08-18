# Retro-documentar un módulo sin especificación — el procedimiento

> **Cuándo.** Un módulo ya en producción que nunca tuvo especificación, o cuya especificación quedó más vieja que el código. Lo exige la regla [`13·DOC6`](reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md) del capítulo 13 · Documentación.
>
> **Qué es.** Una unidad de trabajo formal, con sus entregables, no un comentario apurado antes de tocar el código.

---

## Los seis pasos

**1 · Explorar con lectura amplia.** Mapear el módulo real: archivos, tablas o estructuras de datos, relaciones, y de qué otros módulos depende.

**2 · Persistir el análisis.** Un archivo bajo la carpeta de análisis del proyecto, con lo que se encontró y enlaces a los archivos concretos. Es la fotografía del estado actual, y queda inmutable.

**3 · Crear la especificación de referencia.** El documento vivo del módulo, con las secciones que pide la plantilla de especificación de módulo. Se marca como *retro-doc inicial*: nace provisional.

**4 · Preguntar lo que el código no dice.** Todo dato de negocio que no se puede deducir leyendo el código se anota como pregunta abierta en la especificación, dirigida al usuario. No se inventa.

**5 · Listar los huecos.** Lo que el código hace y no debería —deuda—, y lo que debería hacer y no hace. Van numerados, para poder citarlos después desde una fase.

**6 · Registrar el módulo.** En el catálogo de módulos del proyecto ([`13·DOC13`](reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)), con un puntero a la especificación recién creada.

---

## Cuándo deja de ser provisional

En el primer audit profundo del módulo —una fase dedicada— cuando la especificación se completa según la plantilla canónica. Hasta entonces, quien la lea tiene que saber que es una reconstrucción, no un acuerdo.

Las preguntas del paso 4, cuando el usuario las responda, se cierran con la tabla de decisiones que pide [`13·DOC8`](reglas/DOC8-cierra-todo-analisis-con-su-tabla-de-decisiones.md) — no en el chat.
