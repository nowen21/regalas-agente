# Funcionalidad implementada — Fase `Z-EP-021-HU-001-lo-vacio-se-dice` (módulo Avisos, Ciclo de vida, Comprobaciones, Aprobaciones y Memoria)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [HU-001](../HU-001-ver-el-estado-sin-abrir-la-consola.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `Z-EP-021-HU-001-lo-vacio-se-dice` |
| **Épica / HU** | [EP-021](../../epica.md) · [HU-001](../HU-001-ver-el-estado-sin-abrir-la-consola.md) |
| **Módulo** | Avisos, Ciclo de vida, Comprobaciones, Aprobaciones y Memoria |
| **Fecha de cierre** | 2026-09-01 |
| **Versión del estándar bajo la que cerró** | 37.2.1 |

---

## 1. Qué se implementó — resumen

**Cinco pantallas de solo mirar**, que cierran la mitad que faltaba de seis funcionalidades ya construidas: el tablero, las fases, las funcionalidades, las aprobaciones y la memoria.

**Ninguna calcula.** Piden a su módulo lo que ya sabía; si alguna hubiera calculado algo propio, sería lógica en dos lugares.

**Y ninguna sale en blanco.** Un proyecto recién conectado ve las cinco vacías, y cada una dice que está vacía y por qué. Una pantalla en blanco se lee como un error de la plataforma, y casi nunca lo es.

**Lo que la pantalla no muestra, lo dice.** Las aprobaciones advierten que no son todos los documentos; el tablero, que «vencida» es un número puesto acá y no un vencimiento acordado; las fases, cuáles usan otra tabla. Una advertencia que vive en otro archivo no se lee.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| «Lo vacío se dice» (`RN-1`) | plantilla | Los cinco bloques `.vacio` de `plataforma/templates/` | ✅ | CP-002 |
| «Ningún cero donde no se sabe» (`RN-2`) | plantilla | `tablero.html` y `fases.html` | ✅ | CP-003 |
| «Cada una dice qué no muestra» (`RN-3`) | plantilla | Las cinco | ✅ | CP-004 |
| «Las vistas piden, no calculan» (`RN-4`) | vista | Los cinco `views.py` | ✅ | CP-001 |
| «Nada sale a la red» (`RN-5`) | plantilla | `base.html`, con los estilos adentro | ✅ | — |
| «404 para el que no existe» (`RN-6`) | vista | `get_object_or_404` | ✅ | CP-001 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-01 a T-04 | Las cinco vistas, que piden y no calculan |
| T-05 · T-06 | **El caso vacío de cada una, y ningún cero donde no se sabe** |
| T-07 | Las rutas antes de la comodín, y los enlaces |
| T-08 · T-09 | **15 pruebas**, y las cinco §7 puestas al día |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `plataforma/nucleo/avisos/` | 15 pruebas de esta fase, en verde |
| La batería de la plataforma completa | 552 pruebas, en verde |
| La batería del estándar | 733 pruebas, en verde |

**Lo que las pruebas no dicen:** si las pantallas se entienden, ni cómo se ven.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Desde `plataforma/`:

```
/tablero/
/proyecto/<identificador>/fases/
/proyecto/<identificador>/funcionalidades/
/proyecto/<identificador>/aprobaciones/
/proyecto/<identificador>/memoria/
```

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| **Las vistas piden, no calculan** | Lógica en dos lugares es lógica que un día dirá dos cosas |
| **Solo mirar** | Los cambios de estado quieren su confirmación (`00·N1`), y hacerlos acá sería media confirmación |
| **Las rutas nuevas van antes de la comodín** | `proyecto/<id>/<que>/` se traga cualquier segmento |
| **Las advertencias se imprimen con los datos** | Una que vive en otro archivo no se lee |
| **Cinco casos vacíos, cinco frases distintas** | No tener fases no es lo mismo que no tener aprobaciones |

Señal registrada: [`S-119`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **Seis módulos siguen sin pantalla:** Auditoría, Medición, Expediente, Reglas, Seguridad y Almacén.
- **No se puede cambiar nada desde la pantalla**, y así se quiso.
- **No hay prueba de cómo se ven**, solo de lo que dicen.

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

| Documento | Qué se le agregó |
|---|---|
| Las §7 de [avisos](../../../../avisos/spec.md), [ciclo-de-vida](../../../../ciclo-de-vida/spec.md), [comprobaciones](../../../../comprobaciones/spec.md), [aprobaciones](../../../../aprobaciones/spec.md) y [memoria](../../../../memoria/spec.md) | Decían «sin pantalla», y dejó de ser cierto |
| [documentacion/senales.md](../../../../senales.md) | `S-119` |
| [documentacion/epicas/README.md](../../../README.md) | `EP-021` |

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

**Ninguna migración y ninguna dependencia nueva.**
