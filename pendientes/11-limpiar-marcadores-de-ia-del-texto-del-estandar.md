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

## Depende de

El validador de la parte mecánica de `ID8`, anotado en [`validadores/reglas-validables.md`](../validadores/reglas-validables.md). Hacer el recuento a mano sobre 200 archivos es lo que convierte este pendiente en inabordable; con el script, el paso 1 es una corrida.
