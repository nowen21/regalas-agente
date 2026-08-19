# Pendiente · Limpiar del estándar las marcas que su propia regla prohíbe

**Estado:** abierto · anotado 2026-08-10, al publicar [`00·ID8`](../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) en la v7.0.0.

| | |
|---|---|
| **Historia de usuario** | [EP-004 · HU-012 — Marcas de generación automática](../documentacion/epicas/EP-004-comprobacion-automatica/HU-012-marcas-de-generacion-automatica/HU-012-marcas-de-generacion-automatica.md) — es la deuda que destapa el conteo de esa historia: limpiar lo que el programa cuenta |

`ID8` exige que ningún documento se entregue con las marcas de [`marcadores-de-ia.md`](../base/00-identidad-y-rol/marcadores-de-ia.md). El texto que ya estaba escrito no cumple: `base/`, `plantillas/` y los README del repositorio usan la raya larga como inciso en casi todos los párrafos, y hay bastante viñeta que abre con negrita y dos puntos.

Por [`20·M10`](../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md) una norma nueva no reabre lo cerrado, así que la regla rige para lo que se escriba desde ahora y el texto viejo no queda "incumpliendo". Pero mientras no se limpie, el estándar enseña con el ejemplo lo contrario de lo que pide.

## Qué hay que hacer

1. **Contar antes de tocar.** Un recuento por archivo de cada marca mecánica: raya larga como inciso, comillas curvas, punto medio fuera de una cita `NN·ID`, viñetas con negrita y dos puntos, separadores `---` de adorno, y las invisibles de la sección 3. Sin el recuento no se sabe si el trabajo son dos horas o dos días.
2. **Empezar por lo que se hereda.** `base/` y `plantillas/` van primero: son lo que viaja a los proyectos. `notas/`, `analisis/` y el histórico son bitácora y pueden esperar.
3. **No tocar el histórico.** `historico-chat/` es transcripción literal de lo que se dijo ([`CLAUDE.md`](../CLAUDE.md) §1). Reescribirlo lo dañaría.
4. **Reaplicar el checklist a lo que se reescriba.** Editar el texto de una regla anula su resultado ([`checklist.md`](../base/20-meta-reglas/checklist.md) §3), aunque el cambio sea de redacción.

## El recuento, que era el paso 1 — 2026-08-18

**Hecho.** Fase [`A-EP-004-HU-012`](../documentacion/epicas/EP-004-comprobacion-automatica/HU-012-marcas-de-generacion-automatica/A-EP-004-HU-012-contar-las-marcas-de-generacion-automatica/), veredicto **Cumple**. Se corre con `python validadores/marcas.py`; lo que se hereda, con `validar.py marcas`.

| Marca | Cuántas |
|---|---:|
| Raya larga (`—`) como inciso | **7 286** |
| Punto medio (`·`) fuera de una cita `NN·ID` | **6 237** |
| Viñeta que abre con negrita y dos puntos | **1 539** |
| Semiraya (`–`) donde va un guion | **1 087** |
| Puntos suspensivos en un carácter, semáforos, flechas, encabezados con dos puntos | 328 entre las cuatro |
| **Total, fuera del histórico** | **16 477 en 820 archivos** |

| Reparto | |
|---|---:|
| `base/` y `plantillas/` — por donde manda empezar el paso 2 | **4 491 en 137 archivos** |
| Con el histórico, que no se reescribe | 26 920 en 945 |

**La pregunta era si limpiar son dos horas o dos días. No es ninguna de las dos.**

### Lo que el recuento deja decidido, y lo que no

### El punto medio de los títulos — decidido el 2026-08-18

**Se conserva, y no como excepción: como notación definida.** El [anexo](../base/00-identidad-y-rol/marcadores-de-ia.md) ya eximía la cita `NN·ID` por ser notación de la casa, y el separador de un encabezado —`09 · Control de versiones`— es la misma clase de cosa.

**El propio código ya lo tenía decidido y no lo había implementado:** el comentario de `marcas.py` decía *«ni de un `A · B` de encabezado»* y la expresión solo cubría la cita.

**El recuento baja de 16 477 a 15 485**, y el punto medio de 6 237 a **4 638**. Se exime solo en la línea de un encabezado: en prosa sigue contando.

~~**El punto medio de los títulos de este repositorio sí se cuenta.**~~ `09 · Control de versiones`, `Fase A · …`: el anexo llama marca a *«adornar títulos»* con él, y son buena parte de los 6 237. **No se le hizo excepción a propósito** — si el estándar quiere conservar esa forma, es una decisión que se escribe, no un descuento que el programa hace callando.

**La mitad del anexo no se cuenta, y está declarado.** Si la raya aparece «muy seguido», si el paralelismo es «perfecto», si el español «no es de acá». Un programa que opinara de eso llenaría de ruido lo que hoy nadie mira.

### Lo que hay que saber antes de limpiar

**Buena parte de esas 16 477 se escribieron después del 2026-08-10**, cuando la marca ya estaba registrada. [`02·F21`](../base/02-flujo-de-trabajo/reglas/F21-un-incumplimiento-ya-identificado-no-se-repite-en-lo-nuevo.md) dice que desde ahí lo nuevo nace cumpliendo, y **no pasó**.

**El recuento no separaba lo viejo de lo nuevo, y saberlo cambia el tamaño del problema:** si la deuda es histórica se limpia una vez; si sigue creciendo, limpiarla sin más es rehacer el trabajo el mes que viene.

### Medido el 2026-08-18: sigue creciendo

Se le preguntó al control de versiones **cuándo entró la línea** de cada marca de `base/` y `plantillas/`, tomando como corte el 2026-08-10, el día que se publicó `ID8`:

| Cuándo se escribió | Marcas |
|---|---:|
| Antes del 2026-08-10 — `ID8` todavía no existía | 2 110 |
| **Desde el 2026-08-10** — `02·F21` ya aplicaba | **2 872** |
| Sin atribuir | 8 |
| **Total** | **4 990** |

**El 58 % de la deuda es posterior a la regla.** No es un texto viejo que quedó atrás: es texto escrito por el agente **después** de que la marca estuviera registrada, con [`02·F21`](../base/02-flujo-de-trabajo/reglas/F21-un-incumplimiento-ya-identificado-no-se-repite-en-lo-nuevo.md) vigente y diciendo que lo nuevo nace cumpliendo.

**Y hay dos marcas que empeoran, no solo se repiten:**

| Marca | Nueva | Vieja |
|---|---:|---:|
| Punto medio (`·`) fuera de una cita `NN·ID` | **1 531** | 1 136 |
| Semiraya (`–`) donde va un guion | **713** | 294 |
| Raya larga (`—`) como inciso | 453 | 471 |
| Viñeta que abre con negrita y dos puntos | 91 | 97 |

La raya larga y la viñeta están estables — se dejaron de escribir al ritmo que se escribían. **El punto medio y la semiraya se aceleraron.**

### Lo que esto decide

**Limpiar primero es hacer el trabajo dos veces.** Con el 58 % naciendo después de la regla, lo que hay que cerrar antes es la llave: que la marca no entre. Después se limpia, una sola vez.

**Y cambia el orden del paso 2.** No es «empezar por `base/` porque es lo que se hereda»: es **empezar por lo que impide que vuelva a entrar**. La parte mecánica ya se cuenta con `validar.py marcas`; lo que falta es que ese recuento **detenga** algo, en vez de informar.

> Los doce archivos que más marcas nuevas trajeron son capítulos enteros de `base/` —`01-conducta.md` solo aporta 377—, no reglas sueltas. Es prosa de capítulo, que es justo la que nadie relee.

---

## Depende de

~~El validador de la parte mecánica de `ID8`~~ — **construido el 2026-08-18**, ver arriba. Estaba anotado en [`validadores/reglas-validables.md`](../validadores/reglas-validables.md). Hacer el recuento a mano sobre 200 archivos es lo que convierte este pendiente en inabordable; con el script, el paso 1 es una corrida.
