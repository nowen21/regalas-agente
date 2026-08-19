# Pendiente · Patrón IA (opt-in)

**Estado:** abierto · anotado 2026-08-13.

| | |
|---|---|
| **Historia de usuario** | [EP-001 · HU-013 — Capítulos opt-in de dominio](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-013-capitulos-opt-in-de-dominio/HU-013-capitulos-opt-in-de-dominio.md) — mismo caso que el 08: un capítulo opt-in, acá el 21 |

Un capítulo opt-in, el `21`, que es el siguiente número libre, para los proyectos que **construyen con inteligencia artificial**: los que entrenan un modelo, los que llaman al de un tercero, o los que dejan que un modelo decida algo dentro del producto.

Hoy el estándar sirve para desarrollar uno de esos proyectos como cualquier otro. Lo que no trae es conocimiento propio del tema. El capítulo [`12`](../base/12-privacidad-datos.md) cubre datos personales, el [`16`](../base/16-cumplimiento-y-calidad.md) cumplimiento y el [`19`](../base/19-observabilidad-y-operacion.md) cómo se vigila un sistema en marcha, y ninguno pregunta qué modelo hay corriendo, con qué datos se entrenó, ni quién responde cuando se equivoca.

## De dónde sale

De los apuntes del diplomado de IA, módulo 2 (IA estratégica, ética y análisis de riesgos organizacionales), en `Escom/.../proyecto-grado/diplomado-ia/`. Las piezas vienen de tres archivos de ese material: la nota de clase sobre la administración de la IA, la de los cuatro componentes, y la diapositiva de sistemas autónomos.

Es la primera vez que se aplica la idea 1 de [10-ideas](10-ideas.md): que lo que el usuario aprende en el posgrado entre al estándar.

## Qué cubriría

### 1. El ciclo de vida, con un responsable en cada tramo

Un sistema de IA no se instala una vez y queda. Se sostiene, y en cada tramo hay una decisión que no es técnica:

| Tramo | La pregunta que hay que responder |
|---|---|
| Caso de uso | ¿Qué problema resuelve y cuánto vale resolverlo? |
| Datos | ¿De dónde salen y qué permiten hacer con ellos? |
| Modelo | ¿Qué método, y qué tanto se puede explicar lo que responde? |
| Despliegue | ¿Quién lo usa, con qué límites y qué pasa si se cae? |
| Monitoreo | ¿Sigue acertando? ¿Se desvió? |
| Retiro | ¿Cuándo se apaga o se vuelve a entrenar? |

El tramo que se olvida es el monitoreo. Un modelo que ayer acertaba puede fallar hoy sin que nada se rompa: cambió la realidad que retrataban los datos, no el código. Eso se llama deriva, y solo se ve si alguien está mirando.

### 2. Los instrumentos

| Instrumento | Para qué sirve |
|---|---|
| Inventario de modelos | Saber qué hay corriendo, quién lo hizo, con qué datos y desde cuándo. Sin inventario no hay nada más. |
| Clasificación por riesgo | Un modelo que ordena un catálogo y uno que niega un crédito no pueden tener el mismo control. |
| Política de uso | Qué datos no se cargan y qué decisiones no se delegan. |
| Dueño por modelo | Un nombre, no un área. |
| Revisión humana | En qué casos la respuesta de la máquina no se ejecuta sola. |
| Métricas y auditoría | Qué se mide, cada cuánto y quién lo revisa. Incluye sesgo, no solo aciertos. |
| Registro de decisiones | Por qué se aprobó, con qué supuestos y qué se descartó. Es lo que permite explicarlo después. |

### 3. El riesgo que trae cada insumo

Un sistema de IA necesita cuatro cosas al tiempo, y cada una llega con su problema:

| Insumo | Riesgo que introduce |
|---|---|
| Datos | Sesgo, datos personales, calidad, de dónde salieron y bajo qué términos se pueden usar. |
| Algoritmo | Opacidad: modelos que aciertan sin poder decir por qué. |
| Capacidad de cómputo | Dependencia del proveedor, costo que sube con el uso, y en qué país queda alojado el dato. |
| Talento humano | Quién responde. Sin alguien a cargo, nadie responde. |

La mayoría de los proyectos de IA no fracasa por el algoritmo. Fracasa por los datos, que son lo más barato de conseguir y lo más caro de arreglar, o por el talento, que es el único de los cuatro que no se compra hecho.

### 4. Tres exigencias que no salen de lo anterior

- **Sugerir y ejecutar no son lo mismo.** Mientras el sistema sugiere, el error lo filtra una persona. Cuando ejecuta, el error ya ocurrió. El control tiene que subir en ese salto, y hoy ninguna regla lo nombra.
- **Un sistema que se adapta ya no es el que se auditó.** Si el modelo sigue aprendiendo después de aprobado, la aprobación de una sola vez no vale. Por eso el monitoreo del punto 1 es obligación y no cortesía.
- **La recompensa mal puesta.** Un sistema entrenado por consecuencias optimiza la medida que se le definió, no la que se tenía en la cabeza. Cuando el resultado sale absurdo, casi siempre la medida estaba mal escrita, y eso lo escribió alguien.

### 5. Plantillas

Dos: la ficha del modelo (qué hace, con qué datos, qué tan explicable es, quién es el dueño, cómo se mide) y el registro de decisiones del ciclo de vida.

## Por qué cabe en `base/`

Todo lo de arriba es agnóstico de stack ([`20·M3`](../base/20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md)): habla de ciclo de vida, de quién responde y de qué se vigila, no de una librería ni de un proveedor. La parte que sí es de stack (qué modelo, en qué nube) la declara cada proyecto en su `.agente/stack.md`, igual que ya lo hace con lo demás.

Y es opt-in porque un proyecto que no toca IA no gana nada teniéndolo encendido, que es el mismo criterio de los capítulos `15`, `16`, `17`, `18` y `19`.

## Relación con lo que ya existe

- Hermano de [07 · patrones DevOps](hecho/patrones-devops.md) (hecho) y [08 · patrón RPA](hecho/patrones-rpa.md): los tres son cobertura opt-in de dominio y ninguno depende de la fila 01 a 06.
- El instrumento «clasificación por riesgo» es el mismo que el [pendiente 13](hecho/inventario-y-riesgo-de-las-acciones-del-agente.md) propone aplicarle al propio agente. Conviene escribir primero el 13, que es más pequeño, y reusar su tabla acá.
- El monitoreo del ciclo de vida se apoya en el capítulo `19`, que ya existe. Acá se agrega qué se vigila de un modelo, que es distinto de lo que se vigila de un servicio.
