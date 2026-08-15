# Funcionalidad implementada — Fase A-EP-003-HU-001-marca-de-espacio-por-llenar (módulo Documentos modelo)

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · [`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-003-HU-001-marca-de-espacio-por-llenar` |
| **Módulo** | Documentos modelo |
| **Especificación del módulo** | [documentacion/documentos-modelo/spec.md](../../../../documentos-modelo/spec.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | HU-001: [CA-01](../HU-001-marca-de-espacio-por-llenar.md#ca-01--la-marca-se-ve-y-se-distingue-del-texto), [CA-02](../HU-001-marca-de-espacio-por-llenar.md#ca-02--todos-los-modelos-usan-la-misma-marca), [CA-03](../HU-001-marca-de-espacio-por-llenar.md#ca-03--un-documento-con-marcas-sin-llenar-no-se-da-por-terminado) y los tres [RNF](../HU-001-marca-de-espacio-por-llenar.md#5-requisitos-no-funcionales) |
| **Fecha de cierre** | 2026-08-14 |
| **Commit** | `b877f37`, autorizado el 2026-08-14 |

---

## 1. Qué se implementó — resumen

Los huecos de un documento modelo ahora se marcan de una sola forma, `«…»`, y eso quedó escrito como regla en vez de depender de que alguien se acuerde. Con la regla vinieron dos más: un documento que todavía trae una marca no está terminado, y la sección que no aplica se escribe `N/A` en vez de dejarla marcada o borrarla.

Sirve a quien recibe un documento para aprobarlo: los huecos se ven de una lectura, y a quien construya el programa de EP-004, que ya tiene una marca única que contar.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| RN-01 · una sola marca, `«…»`, en todos los modelos | doc | `base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md` | ✅ | CP-002: 26 de 26 archivos con huecos |
| RN-02 · la marca se nota sin buscarla | doc | La misma regla | ✅ | CP-001: los dos recuentos coinciden |
| RN-03 · un programa la encuentra | doc | La misma regla | ✅ | El propio `grep` de CP-002 y CP-003 |
| RN-04 · la sintaxis de comando no es hueco | doc | La misma regla, segunda frase | ✅ | CP-003: los aciertos de `<texto>` son comandos, y ninguno se marcó |
| RN-05 · con marcas no está terminado | doc | `base/13-documentacion/reglas/DOC20-no-entregues-como-terminado-un-documento-con-marcas.md` | ✅ | CP-004 |
| RN-06 · lo que no aplica se escribe `N/A` | doc | `base/13-documentacion/reglas/DOC21-escribe-n-a-en-la-seccion-que-no-aplica.md` | ✅ | CP-004 |
| RN-07 · la caja de instrucciones se borra al llenar | doc | Dentro de [`DOC20`](../../../../../base/13-documentacion/reglas/DOC20-no-entregues-como-terminado-un-documento-con-marcas.md) | ✅ | Texto de la regla |
| El porqué de la marca | doc | `notas/marca-del-espacio-por-llenar.md` | ✅ | La nota, con las cuatro descartadas |
| Aplicación de la marca a los modelos | plantilla | 13 archivos de `plantillas/` | ✅ | 179 huecos convertidos, más los de `epica.md` y `marco-normativo.md` |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-01 | El porqué de la marca, en `notas/` | ✅ hecha | `notas/marca-del-espacio-por-llenar.md` | El archivo |
| T-02 | Escribir [`DOC19`](../../../../../base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md) con su checklist | ✅ hecha | `base/13-documentacion/reglas/DOC19-…` | La regla, checklist en CUMPLE |
| T-03 | Qué es un hueco y qué no | ✅ hecha | Dentro de [`DOC19`](../../../../../base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md) | Segunda frase del cuerpo |
| T-03b | Las tres filas en el índice del capítulo | ✅ hecha | `base/13-documentacion/base.md`, grupo (c) | El índice |
| T-04 | `plantillas/epica.md` a la marca | ✅ hecha | `plantillas/epica.md` | 45 marcas |
| T-05 | `plantillas/marco-normativo.md` a la marca | ✅ hecha | `plantillas/marco-normativo.md` | Todos sus campos |
| T-06 | Los tres dudosos, con su motivo escrito | ✅ hecha | `notas/marca-del-espacio-por-llenar.md` | La tabla de la nota |
| T-06b | Los 11 archivos con corchetes | ✅ hecha | 11 archivos de `plantillas/` | 179 huecos |
| T-07 | Recorrer las 30 y confirmar | ✅ hecha | — | CP-002 y CP-003 |
| T-08 | Escribir [`DOC20`](../../../../../base/13-documentacion/reglas/DOC20-no-entregues-como-terminado-un-documento-con-marcas.md) | ✅ hecha | `base/13-documentacion/reglas/DOC20-…` | La regla |
| T-09 | Escribir [`DOC21`](../../../../../base/13-documentacion/reglas/DOC21-escribe-n-a-en-la-seccion-que-no-aplica.md) | ✅ hecha | `base/13-documentacion/reglas/DOC21-…` | La regla |
| T-10 | Las tres reglas en `reglas-validables.md` | ✅ hecha | `validadores/reglas-validables.md`, lista de pendientes | Las tres filas |
| T-11 | Correr `validar.py estandar` | ✅ hecha | — | 0 fallas, 2 avisos previos |
| T-12 | Entrada en `CHANGELOG.md` y `VERSION` | ✅ hecha | `CHANGELOG.md` · `VERSION` | Versión 13.0.0 |

**Correspondencia con el plan:** 14 tareas en el plan, 14 acá. Cuadra.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba**  ·  [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md):

| Archivo | Por qué hubo que tocarlo | Quién autorizó ampliar el plan |
|---|---|---|
| `notas/README.md` | El validador lo exige: una nota nueva sin su línea en el índice es falla | Nadie: es la corrección que el propio validador pide, dentro de la tarea que creó la nota |

Todo lo demás salió declarado, pero **el plan se amplió dos veces sobre la marcha**, y las dos veces con el visto bueno del usuario antes de tocar nada. Está escrito en §2 del plan de trabajo.

**Esfuerzo real contra estimado:** 19 h estimadas tras las ampliaciones, contra las 13 del plan aprobado. Lo que se subestimó fue la línea base: contó archivos que tenían alguna marca, no archivos convertidos por completo.

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

- **Fuente:** [resultado_pruebas.md](resultado_pruebas.md) · **Veredicto:** Cumple.
- **Suites corridas + resultado:** `validar.py estandar`, 0 fallas y 2 avisos que ya venían de antes.
- **Verificaciones manuales** ([`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)):
  - Lectura completa de tres plantillas señalando los huecos sin releer, y recuento a ojo contra `grep`.
  - Revisión acierto por acierto de las cuatro marcas descartadas, para separar el hueco de la sintaxis de un comando.
- **Defectos abiertos que se aceptaron:** DEF-03, el `«ADR-XXX»` de `ADR.md`. Cumple [`DOC19`](../../../../../base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md) porque el `XXX` va dentro de la marca, como texto. Lo aceptó el agente al verificar y queda anotado.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

- **Punto de entrada:** abrir cualquier archivo de `plantillas/`. Los huecos son los `«…»`.
- **Permisos o datos base sembrados:** N/A.

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / `DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| La marca es `«…»` | Ya se usaba en 25 de 30 archivos. Se descartaron `[texto]`, `<texto>`, `{{texto}}` y `XXX`, las cuatro por chocar con sintaxis que el documento ya usa | [`notas/marca-del-espacio-por-llenar.md`](../../../../../notas/marca-del-espacio-por-llenar.md) |
| La sintaxis de un comando no es un hueco | Marcarla haría que el programa de EP-004 reportara de más, que es el riesgo que la épica quiere evitar | Dentro de [`DOC19`](../../../../../base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md) |
| Son tres reglas y no una | La fila 9 del checklist reprueba el "y además", y las tres partes se cumplen por separado | §2 del plan de trabajo |
| Tres plantillas quedan sin marca | No son modelos que alguien llene: son procedimientos y explicaciones | La tabla de la nota |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino |
|---|---|---|
| `ADR.md` usa `«ADR-XXX»`; sería más parejo `«ADR-NNN»`, como el resto del catálogo | Atajo decidido, por el agente al verificar | Se corrige cuando se toque `ADR.md`; no amerita fase |
| Las tres reglas nuevas son validables y todavía no las valida nadie | Diferido por el plan | EP-004, ya anotado en `validadores/reglas-validables.md` |

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / `DOC13`

- [x] Índice del capítulo 13 con las tres reglas nuevas.
- [x] Índice de `notas/README.md` con la nota nueva.
- [x] `validadores/reglas-validables.md` con las tres reglas.
- [x] Especificación del módulo al día con lo realmente implementado.
- [ ] Mapa de dependencias vivo (`DOC9`): N/A, este repositorio no lo tiene.
- [ ] Catálogo de módulos (`DOC13`): N/A, este repositorio no lo tiene. Es deuda del propio estándar, no de esta fase.

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

- Cambios de esquema / migraciones: N/A, no hay base de datos.
- Datos base / permisos: N/A.
- Comandos post-deploy: un proyecto que herede corre su instalador para recibir las plantillas nuevas.
- Reversión: revertir el commit. Las plantillas cambian de huella, así que la copia de cada proyecto queda marcada vieja hasta la siguiente corrida del instalador.
