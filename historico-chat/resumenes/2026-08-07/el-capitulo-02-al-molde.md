# 2026-08-07 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-07-el-capitulo-02-al-molde.md](../../2026-08-07-el-capitulo-02-al-molde.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

> **Resumen escrito hacia atrás, el 2026-08-16.** La sesión es anterior a la regla que obliga a escribirlo ([`13·DOC22`](../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md)).

**Viene de:** —, es trabajo nuevo. Arranca con cinco palabras: *«pase flujo de trabajo a su carpeta»*.

**Propósito:** bajar el capítulo del flujo a la forma que el propio estándar exige.

---

## Hallazgos de esta sesión

### H-1 · El capítulo más grande entraba entero al arranque

- **Qué pasó:** `02 · Flujo de trabajo` era un archivo de 46 KB con catorce reglas y cinco sub-reglas dentro. El cargador inyecta el índice de cada capítulo temático, y el de este era una línea de 46 KB.
- **Por qué importa:** el agente arrancaba cargando el capítulo completo para poder tocar una regla. Después del cambio son quince líneas que dicen de qué trata cada una, y lee solo la que va a usar.
- **Qué lo soluciona:** una carpeta con `base.md` de índice y una regla por archivo, como ya lo tenían los capítulos `00` y `20`.
- **Qué se decidió:** el usuario corrigió la primera versión —*«las F deben estar en su carpeta reglas como está el estándar»*— y quedó plano: ninguna subcarpeta dentro de `reglas/`, y el anexo de `F13` en la raíz del capítulo porque es anexo, no regla. Ningún ID cambió; los archivos se renombraron detrás del título.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [base/02-flujo-de-trabajo](../../../base/02-flujo-de-trabajo/base.md), versión **2.4.0** del [CHANGELOG](../../../CHANGELOG.md).
- **Nace en:** 2026-08-07 · el capítulo 02 al molde.
- **Cerrado en:** 2026-08-07 · el capítulo 02 al molde.
- **Con qué se retoma:** —.

### H-2 · En la regla estaba la exigencia mezclada con todo lo que la explicaba

- **Qué pasó:** el usuario lo dijo en una línea: *«en reglas solo queda la regla y las explicaciones en `base.md`»*. `F4.3` era la regla más larga del catálogo, 78 líneas; quedó en cinco.
- **Por qué importa:** una regla de cuatro líneas se lee y se cumple. Una de setenta y ocho se hojea, y lo que exige se pierde entre lo que la ilustra.
- **Qué lo soluciona:** que en `reglas/` quede el encabezado, el cuerpo, la dependencia, la excepción y el ejemplo; y que la tabla de etapas, la casuística y los protocolos bajen a una sección por regla en el índice del capítulo.
- **Qué se decidió:** aplicado a las diecinueve. De paso quedaron completas ocho excepciones que estaban a medias, se rompió el ciclo de dependencias entre `F4.4` y `F4.5`, y el texto que `F5`, `F6` y `F7` copiaban de otros capítulos se reemplazó por el enlace.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** versión **2.5.0** del [CHANGELOG](../../../CHANGELOG.md).
- **Nace en:** 2026-08-07 · el capítulo 02 al molde.
- **Cerrado en:** 2026-08-07 · el capítulo 02 al molde.
- **Con qué se retoma:** —.

### H-3 · Convivían dos versiones de `F0` y ninguna decía cuál mandaba

- **Qué pasó:** el anexo de la anatomía publicaba desde la v2.2.0 el texto corregido de `F0` —el que salió de desmenuzarla el día anterior— y el capítulo seguía con el viejo. Nadie lo había aplicado.
- **Por qué importa:** dos textos de la misma regla en dos archivos es el defecto que `M2` llama el más caro: alguien corrige una copia y el estándar se contradice solo.
- **Qué lo soluciona:** que la regla tome el texto que ya se había acordado.
- **Qué se decidió:** `F0` quedó con el texto corregido, y con él seis títulos que antes contaban en vez de mandar: *«Recorre la cadena completa»*, *«Corre solo las suites que la fase toca»*, *«Detente si el proyecto no tiene su estructura base»*. `F13` perdió la marca inventada que era el anti-ejemplo del propio checklist.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [`F0`](../../../base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md). Cierra el H-6 de [la anatomía de la regla](../2026-08-06/la-anatomia-de-la-regla.md).
- **Nace en:** 2026-08-06 · la anatomía de la regla.
- **Cerrado en:** 2026-08-07 · el capítulo 02 al molde.
- **Con qué se retoma:** —.

### H-4 · Diez de las diecinueve reglas reprueban el checklist, y no por cómo están escritas

- **Qué pasó:** al aplicar el checklist quedaron **9 CUMPLE y 10 NO**. Las diez reprueban por decisiones de catálogo que son del usuario: el sub-ID decimal que `M4` no contempla, reglas con dos exigencias que habría que partir creando IDs nuevos, y tres cuyo dueño de tema está en otro capítulo.
- **Por qué importa:** quedó dicha la distinción que evita el pánico: **reprobar no es dejar de regir.** El ❌ dice que la regla no está bien escrita según el propio estándar, no que el agente pueda saltársela.
- **Qué lo soluciona:** una sola decisión arrastra cuatro de las cinco `F4.N` — legalizar el sub-ID en `M4`, o promoverlas a IDs propios.
- **Qué se decidió:** el usuario eligió convertirlas: nacen `F14`–`F20`, con `F4.3` y `F4.5` partidas en dos porque llevaban dos exigencias cada una. Las cinco viejas quedaron como lápidas `[DEROGADA en 3.1.0 → ver …]` con su texto entero, porque specs y fases cerradas las citan.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** versión **3.1.0**. Lo que quedó vivo es la misma decisión aplicada a `F12.1`–`F12.13` y a la fila 17 de `M4`, hoy en el [pendiente 19](../../../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).
- **Nace en:** 2026-08-07 · el capítulo 02 al molde.
- **Cerrado en:** 2026-08-07 · el capítulo 02 al molde.
- **Con qué se retoma:** —.

### H-5 · Renombrar un archivo rompió el arranque y ninguna prueba lo vio

- **Qué pasó:** al mover `F13`, el `GATE` de [`cargador.py`](../../../validadores/cargador.py) quedó apuntando a una ruta que ya no existía. Se descubrió probándolo a mano.
- **Por qué importa:** ese gate es lo que detiene el arranque cuando el proyecto no tiene su estructura base. Si no carga, la puerta desaparece y nada avisa. Con 191 pruebas verdes, el estándar decía estar bien.
- **Qué lo soluciona:** una prueba que compruebe que `GATE` resuelve a un archivo que existe.
- **Qué se decidió:** se arregló la ruta. La prueba se propuso y **no se hizo** — quedó anotada como «hallazgo derivado, no actuado».
- **Estado:** abierto.
- **Responde a:** —.
- **Dispara:** —, es una prueba de tres líneas.
- **Orden de resolución:** 1 de 1. Va primero por barata: es el arranque lo que protege.
- **Dónde queda:** [pendientes/33](../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md).
- **Nace en:** 2026-08-07 · el capítulo 02 al molde.
- **Cerrado en:** —.
- **Con qué se retoma:** ¿existe hoy esa prueba? Si no, es la más barata del backlog.

### H-6 · El commit se partió en dos, y aun así dos archivos no se pudieron separar

- **Qué pasó:** el árbol tenía mezclado el trabajo de otra sesión que seguía corriendo. El agente hizo dos commits: uno con lo ajeno y otro con lo propio.
- **Por qué importa:** es lo contrario de lo que pasó horas antes en otra sesión, donde todo se subió junto. Acá se intentó separar y quedó a la vista el límite: `CHANGELOG` y `VERSION` traían **tres versiones mezcladas** y viajaron en el commit equivocado.
- **Qué lo soluciona:** que cada sesión suba lo suyo antes de que se acumule; separar después no siempre se puede.
- **Qué se decidió:** subir en dos commits y decir en voz alta cuáles dos archivos quedaron mal repartidos.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** commits `9f2628c` y `b1d8d2f`, y la memoria [no tocar el trabajo de otras sesiones](../../memory/no-tocar-trabajo-de-otras-sesiones.md).
- **Nace en:** 2026-08-07 · el capítulo 02 al molde.
- **Cerrado en:** 2026-08-07 · el capítulo 02 al molde.
- **Con qué se retoma:** —.

---

## ¿Se puede cerrar la sesión?

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ cinco de seis |
| Todo hallazgo abierto tiene su pendiente creado | ☑ H-5 en el [33](../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md) |
| Toda historia disparada está escrita en su épica | ☑ ninguno dispara historia |
| Lo que se hizo está aprobado y guardado | ☑ commits `9f2628c` y `b1d8d2f` |
