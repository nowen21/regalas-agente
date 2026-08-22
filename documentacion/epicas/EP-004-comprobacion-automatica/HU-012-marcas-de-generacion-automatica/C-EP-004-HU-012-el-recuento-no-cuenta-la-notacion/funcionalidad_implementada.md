# Funcionalidad implementada — Fase C-EP-004-HU-012-el-recuento-no-cuenta-la-notacion   ·   `[CAPA 3]`

**Para qué sirve este documento.** Es el cierre de la fase: **qué quedó hecho, qué se probó, qué se decidió y qué deuda quedó**. El plan dice lo que se iba a hacer; esto dice lo que pasó, para poder comparar los dos.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `C-EP-004-HU-012-el-recuento-no-cuenta-la-notacion` |
| **Épica / HU** | [EP-004](../../epica.md) · [HU-012](../HU-012-marcas-de-generacion-automatica.md) |
| **CA que cierra** | CA-03 |
| **Fecha de cierre** | 2026-08-22 |
| **Veredicto** | [Cumple](resultado_pruebas.md#6-veredicto-de-la-fase) |

---

## 1. Qué se implementó — resumen

El recuento de marcas cuenta lo que el anexo dice que es marca, y nada más. Los moldes del ciclo de vida quedaron en **0**, y el árbol entero bajó de **15 485 a 6 440** sin que ningún documento cambie de exigencia.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Exigencia | Dónde quedó | Prueba |
|---|---|---|
| CA-03, la notación no se cuenta | `marcas_de_linea()`, con `_ETIQUETA_Y_ENUNCIADO`, `_FILA_DE_TABLA` y `_CAMPO_POR_LLENAR` | CP-001 a CP-004 |
| CA-01, la tipografía sí se cuenta | Las mismas ramas, por lo que **no** eximen | CP-005 a CP-008 |
| La decisión escrita | [`marcadores-de-ia.md`](../../../../../base/00-identidad-y-rol/marcadores-de-ia.md), sección del 2026-08-22 | — |

### 2.2 Plan de trabajo → ejecución

Las seis tareas hechas como estaban escritas. Dos correcciones dentro de la fase, las dos en el `resultado_pruebas` §4: el campo cuyo valor iba en comillas invertidas, y una expectativa de prueba mal contada.

---

## 3. Qué se probó  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Las dos suites que llaman al recuento: 34 pruebas de conteo y 10 del trinquete, todas en verde. Más la medición sobre el repositorio real, carpeta por carpeta.

---

## 4. Cómo se usa / puntos de entrada

Igual que antes; lo que cambia es qué cuenta.

```
python validadores/marcas.py                       # el árbol entero
python validadores/marcas.py --raiz <carpeta>      # una parte
python validadores/validar.py marcas --preparados  # el trinquete del commit
```

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md)

**No se declaró ninguna excepción: se implementó lo que el anexo ya decía.** Sus filas dicen «la raya larga **como inciso**» y «el punto medio separando frases **en prosa**». Un título no es un inciso, y una celda de tabla no es prosa. El programa contaba de más, y eso es un defecto del programa, no una laxitud de la regla. Es exactamente lo que pasó el 2026-08-18 con el punto medio de los encabezados, y aquella vez quedó escrito en el propio anexo: *«el código ya lo tenía decidido y no lo había implementado»*.

**El campo de formulario se reconoce por su valor, no por su carpeta.** Eximir toda viñeta con negrita dentro de `plantillas/` habría dejado pasar prosa por vivir en un molde. Mirando el valor, `- **Objetivo:** «qué se logra»` es un campo, y la misma línea llenada con prosa vuelve a contar. Es lo correcto en los dos casos.

**Un valor vacío también es un campo, y hay que decir por qué.** `marcas_de_linea()` recibe la línea con el código ya quitado, así que `- **Slug:** \`«x»\`` llega sin valor. Pedir la línea original obligaba a cambiar la firma y todos sus llamadores para ganar nada.

**Se descuenta una sola raya por línea en el caso del enunciado.** Un identificador con su enunciado usa una; si además hay un inciso, ese inciso sigue contando. La prueba CP-006 fija ese límite, y fue la que obligó a corregir una expectativa mal contada.

**Bajar la cuenta no puede romper el trinquete**, y se comprobó en vez de suponerlo: el trinquete falla cuando la cuenta **sube**. Ningún commit que hoy pasa va a empezar a fallar.

---

## 6. Deuda técnica y pendientes generados

| Qué queda | Dónde |
|---|---|
| Nada de esta fase | — |
| Las 6 440 marcas que quedan en el árbol son adorno de prosa de verdad, y siguen esperando la decisión de si se limpian | [Pendiente 11](../../../../../pendientes/hecho/limpiar-marcadores-de-ia-del-texto-del-estandar.md), que lo dejó escrito al cerrar |

---

## 7. Índices y mapas actualizados

- [HU-012](../HU-012-marcas-de-generacion-automatica.md): la fila de esta fase, y el cierre de la fase B.
- [Pendiente 78](../../../../../pendientes/hecho/los-moldes-se-entregan-limpios-de-marcas.md), cerrado, con su fila en el índice.
- [`marcadores-de-ia.md`](../../../../../base/00-identidad-y-rol/marcadores-de-ia.md), con la decisión escrita junto a la del 2026-08-18.

---

## 8. Despliegue — si aplica

No aplica. Los proyectos instalados reciben el recuento nuevo al actualizar el estándar, y lo que ven es que la deuda de notación desaparece sin tocar un archivo, porque nunca fue deuda.
