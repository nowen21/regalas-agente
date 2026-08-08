# Retro-documentar un módulo sin spec — el procedimiento

> **Cuándo.** Un módulo ya en producción que nunca tuvo spec, o cuya spec quedó más vieja que el código. Lo exige la regla `DOC6` del capítulo 13 · Documentación.
>
> **Qué es.** Una unidad de trabajo formal, con sus entregables, no un comentario apurado antes de tocar el código.

---

## Los seis pasos

**1 · Explorar con lectura amplia.** Mapear el módulo real: archivos, tablas o estructuras de datos, relaciones, y de qué otros módulos depende.

**2 · Persistir el análisis.** Un archivo bajo la carpeta de análisis del proyecto, con lo que se encontró y enlaces a los archivos concretos. Es la fotografía del estado actual, y queda inmutable.

**3 · Crear la spec de referencia.** El documento vivo del módulo, con las secciones que pide la plantilla de spec de módulo. Se marca como *retro-doc inicial*: nace provisional.

**4 · Preguntar lo que el código no dice.** Todo dato de negocio que no se puede deducir leyendo el código se anota como pregunta abierta en la spec, dirigida al usuario. No se inventa.

**5 · Listar los huecos.** Lo que el código hace y no debería —deuda—, y lo que debería hacer y no hace. Van numerados, para poder citarlos después desde una fase.

**6 · Registrar el módulo.** En el catálogo de módulos del proyecto (`DOC13`), con un puntero a la spec recién creada.

---

## Cuándo deja de ser provisional

En el primer audit profundo del módulo —una fase dedicada— cuando la spec se completa según la plantilla canónica. Hasta entonces, quien la lea tiene que saber que es una reconstrucción, no un acuerdo.

Las preguntas del paso 4, cuando el usuario las responda, se cierran con la tabla de decisiones que pide `DOC8` — no en el chat.
