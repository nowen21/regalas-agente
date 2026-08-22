# Funcionalidad implementada — Fase B-EP-004-HU-012-limpiar-los-diez-moldes-del-ciclo   ·   `[CAPA 3]`

**Para qué sirve este documento.** Es el cierre de la fase: **qué quedó hecho, qué se probó, qué se decidió y qué deuda quedó**. El plan dice lo que se iba a hacer; esto dice lo que pasó, para poder comparar los dos.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-004-HU-012-limpiar-los-diez-moldes-del-ciclo` |
| **Épica / HU** | [EP-004](../../epica.md) · [HU-012](../HU-012-marcas-de-generacion-automatica.md) |
| **CA que cierra** | [CA-04](../HU-012-marcas-de-generacion-automatica.md#ca-04--los-moldes-del-ciclo-no-llevan-adorno-de-prosa) |
| **Fecha de cierre** | 2026-08-22 |
| **Veredicto** | [Cumple](resultado_pruebas.md#6-veredicto-de-la-fase) |

---

## 1. Qué se implementó — resumen

Los moldes del ciclo de vida dejaron de llevar adorno de prosa. De **197 marcas a 126**, y las 126 que quedan son notación del formulario. Ningún molde pide menos que antes.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Exigencia | Dónde quedó | Cómo se comprobó |
|---|---|---|
| [CA-04](../HU-012-marcas-de-generacion-automatica.md#ca-04--los-moldes-del-ciclo-no-llevan-adorno-de-prosa) paso 1 | El recuento de `marcas.py` | [resultado_pruebas.md](resultado_pruebas.md) §1 |
| CA-04 paso 2 | La clasificación de las 126 | Ídem §3 |
| CA-04 paso 3 | Los 21 moldes | Comparación sección por sección, ídem §3 |
| CA-04 paso 4 | La batería y `validar.py estandar` | Ídem §2, casos 8 y 9 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué decía el plan | Qué se hizo |
|---|---|---|
| T-01 | Volcar y clasificar | Hecho: 213 apariciones, 7 clases |
| T-02 | Citas de regla en formato canónico | Hecho: 13 |
| T-03 | Raya de inciso a coma, paréntesis o dos puntos | Hecho: 25 líneas, y 6 corregidas a mano al revisarlas |
| T-04 | Punto medio de prosa, y reponer `«…»` si se rompe | Hecho, y se rompió: 24 marcadores repuestos |
| T-05 | Recontar y clasificar | Hecho: 126 |
| T-06 | Las suites que dependen de los moldes | Hecho: 47 pruebas en verde |
| T-07 | `CHANGELOG` y `VERSION` | Hecho, sobre `31.12.0` |

**Archivos tocados fuera de los declarados:** `validadores/tests/test_plantillas_origen_regla.py`, cuyo fixture copiaba literal una línea del molde de la especificación. Se anota por [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md).

---

## 3. Qué se probó  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

El recuento antes y después, la clasificación de lo que queda, la comparación sección por sección de los 21 moldes, las suites que dependen de los moldes (47 pruebas) y `validar.py estandar`, `fases` y `pendientes`.

---

## 4. Cómo se usa / puntos de entrada

```
python validadores/marcas.py --raiz plantillas/ciclo-vida-proyectos
```

Nada nuevo: la fase no agrega código, corrige texto. La herramienta que mide ya existía desde la fase A.

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md)

**Clasificar antes de limpiar, y es lo que salvó los moldes.** Un reemplazo a ciegas sobre las tres marcas habría quitado las 43 etiquetas de campo del formulario y renombrado 23 secciones. Eso no limpia el molde: lo deja pidiendo lo mismo peor escrito, o pidiendo menos.

**Renombrar una sección de un molde no es gratis, y se puede medir.** `validar.py plantilla` compara los encabezados del documento con los de su molde. Cambiar el nombre de una sección hace que los 650 documentos ya escritos con ese molde reporten «sección de la plantilla ausente». Es el argumento más fuerte para dejar los títulos como están.

**Las citas de regla mal escritas no se limpian: se escriben bien.** El molde de la especificación traía `` (regla `01`·C3) ``, que el recuento cuenta porque no es el formato canónico. Escribirlas `` `01·C3` `` baja el recuento y además las vuelve citables, que es lo que el estándar quiere.

**Se paró en la notación a propósito.** El estándar ya recorrió este camino: el 2026-08-18 decidió que el punto medio de los encabezados era notación y no adorno, lo declaró en el anexo, y el recuento bajó de 16 477 a 15 485 sin tocar un solo texto. Las cuatro formas que quedan son el mismo caso, y la decisión es del usuario.

**Y una que no es técnica.** El plan de esta fase se escribió **después** de la intervención, contra [`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md). Está dicho en la primera caja del plan y acá. No se disimula porque el estándar no sirve de nada si el agente lo incumple en silencio mientras lo escribe.

---

## 6. Deuda técnica y pendientes generados

| Qué queda | Dónde |
|---|---|
| Las 126 marcas de notación, esperando la decisión del usuario | [Pendiente 78](../../../../../pendientes/hecho/los-moldes-se-entregan-limpios-de-marcas.md), que sigue abierto con su meta corregida |
| Nada por acá: el D-04 que se reportó resultó falso | [resultado_pruebas.md](resultado_pruebas.md) §4, cerrado por falso |
| Los 21 moldes de `plantillas/` fuera del ciclo, y `base/` | Fuera del alcance declarado. Salen como pendiente cuando estos cierren |

---

## 7. Índices y mapas actualizados

- [HU-012](../HU-012-marcas-de-generacion-automatica.md): CA-04 y la fila de esta fase en §8.
- [Pendiente 78](../../../../../pendientes/hecho/los-moldes-se-entregan-limpios-de-marcas.md) y su fila en el [índice de pendientes](../../../../../pendientes/README.md).

---

## 8. Despliegue — si aplica

No aplica. Los moldes viajan a los proyectos con el instalador, y los documentos ya escritos con ellos no cambian ni se invalidan.
