# Funcionalidad implementada — Fase `Y-EP-011-HU-003-la-linea-base-dice-que-es-reconstruida` (módulo Medición)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [HU-003](../HU-003-medir-el-tiempo-que-se-gasta-revisando.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `Y-EP-011-HU-003-la-linea-base-dice-que-es-reconstruida` |
| **Épica / HU** | [EP-011](../../epica.md) · [HU-003](../HU-003-medir-el-tiempo-que-se-gasta-revisando.md) |
| **Módulo** | Medición |
| **Fecha de cierre** | 2026-09-01 |
| **Versión del estándar bajo la que cerró** | 37.2.1 |

---

## 1. Qué se implementó — resumen

**El tiempo que se gasta revisando se mide solo**, de las horas que el enganche del estándar ya escribe en cada mensaje. Nadie cronometra nada: entre la respuesta del agente y el mensaje siguiente hay un hueco, y ese hueco es lo que se tardó en leer.

**Medido acá: 1615 revisiones, 144 horas, mediana de 99 segundos.** Todo en un mes, así que **no hay contra qué comparar**, y el módulo se niega a hacerlo.

**Lo que más costó de esta fase es una frase.** La línea base sale siempre marcada como reconstruida, porque la de verdad debió tomarse antes de empezar y no se tomó. Presentarla como un antes haría que cualquier mejora futura pareciera mayor de lo que es.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| «Medir no obliga a anotar» (`RN-1`) | servicio | `huecos` en [plataforma/nucleo/medicion/revision.py](../../../../../plataforma/nucleo/medicion/revision.py) | ✅ | CP-001 |
| «La base sale marcada» (`RN-2`) | servicio | `linea_base` | ✅ | CP-002 |
| «Un hueco larguísimo no cuenta» (`RN-3`) | servicio | `TOPE_SEGUNDOS` | ✅ | CP-003 |
| «Sin hora se dice aparte» (`RN-4`) | servicio | `_cuando` | ✅ | CP-001 |
| «Con un mes no se compara» (`RN-5`) | servicio | `comparar` | ✅ | CP-004 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-01 · T-02 | Los huecos, y los descartes por arriba y por abajo |
| T-03 · T-04 | La mediana por mes, y la línea base marcada |
| T-05 · T-06 | La negativa a comparar, y la orden de consola |
| T-07 | **14 pruebas** |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `plataforma/nucleo/medicion/` | 14 pruebas de esta fase, en verde |
| La batería de la plataforma completa | 552 pruebas, en verde |
| La batería del estándar | 733 pruebas, en verde |

**Lo que las pruebas no dicen:** si el tiempo bajó porque el estándar sirvió, ni si la línea base es comparable con el antes.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Desde `plataforma/`:

```
python manage.py cuanto_se_revisa
python manage.py cuanto_se_revisa --proyecto <proyecto> --por-mes
```

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| **El tiempo sale de lo ya escrito** | Medir no puede costar más que lo que ahorra |
| **La base siempre dice que es reconstruida** | Presentarla como un antes agranda cualquier mejora |
| **Un hueco de más de dos horas no cuenta** | No es revisión: es que se fue |
| **La mediana, no el promedio** | Un solo hueco largo mueve el promedio, y acá son lo normal |
| **Con un mes no se compara** | Comparar contra sí mismo es inventar una mejora |

Señal registrada: [`S-117`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **La medición inicial no existe**, y no tiene arreglo. Queda declarado.
- **Bajar el tiempo puede no querer decir que se mejoró**: puede ser costumbre.
- **Sin pantalla**, como el resto de los módulos de esta etapa.

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

| Documento | Qué se le agregó |
|---|---|
| [documentacion/medicion/spec.md](../../../../medicion/spec.md) | Su §13 nombra esta fase |
| [documentacion/senales.md](../../../../senales.md) | `S-117` |

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

**Ninguna migración y ninguna dependencia nueva.**
