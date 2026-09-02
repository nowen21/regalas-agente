# Funcionalidad implementada — Fase `I-EP-016-HU-003-un-sello-no-sobrevive-a-un-cambio` (módulo Reglas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [HU-003](../HU-003-aplicar-el-checklist-y-guardar-su-sello.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `I-EP-016-HU-003-un-sello-no-sobrevive-a-un-cambio` |
| **Épica / HU** | [EP-016](../../epica.md) · [HU-003](../HU-003-aplicar-el-checklist-y-guardar-su-sello.md) |
| **Módulo** | Reglas |
| **Fecha de cierre** | 2026-09-01 |
| **Versión del estándar bajo la que cerró** | 37.2.1 |

---

## 1. Qué se implementó — resumen

**Las veinte filas del checklist se traen del estándar**, se guarda lo que se responda, y el sello queda con su versión, su fecha y su aviso de caducidad. Una fila que no aplica **lleva su motivo**, y sin motivo queda un hueco marcado que se ve.

**Y lo más importante es un nombre.** La comparación barata, la fecha del sello contra la del último cambio, se llama `parece_vencido`, no `esta_vencido`. Medida así, **185 de las 248 reglas vigentes salían anuladas**, y el estándar dice que ninguna lo está: compara el cuerpo de la regla y descuenta la tipografía.

El veredicto se le pregunta a quien sabe darlo.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| «El checklist se lee, no se copia» (`RN-1`) | servicio | `filas` en [plataforma/nucleo/reglas/sello.py](../../../../../plataforma/nucleo/reglas/sello.py) | ✅ | CP-001 |
| «Una fila que no aplica lleva su motivo» (`RN-2`) | servicio | `molde_del_sello` | ✅ | CP-004 |
| «Si la regla se edita, el sello se anula» (`RN-3`) | servicio | `parece_vencido` | ✅ | CP-003 |
| «Las fechas no son el veredicto» (`RN-4`) | servicio | `veredicto_del_estandar` | ✅ | CP-003 |
| «El sello dice contra qué versión» (`RN-5`) | servicio | `contra_que` | ✅ | CP-002 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-01 · T-02 | Las filas del checklist, y el sello de una regla |
| T-03 · T-04 | **La comparación con su nombre**, y el veredicto del estándar |
| T-05 | El molde, con los motivos de lo que no aplica |
| T-06 · T-07 | La orden, y 16 pruebas |
| T-08 | **0 contra 185**: las dos formas de medir, al lado |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `plataforma/nucleo/reglas/tests_sello.py` | 16 pruebas, en verde |
| La batería de la plataforma completa | 426 pruebas, en verde |
| La batería del estándar | 733 pruebas, en verde |

**Lo que las pruebas no dicen:** si las respuestas del checklist son correctas. Eso pide criterio.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Desde `plataforma/`:

```
python manage.py sello_de_regla <proyecto> M11
python manage.py sello_de_regla <proyecto> M11 --con-las-filas
```

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| **La comparación por fechas se llama `parece_vencido`** | Medida así daba 185 falsos en 248 |
| **El veredicto se le pregunta al estándar** | Dos versiones de la misma pregunta se separan |
| **Una fila que no aplica lleva su motivo** | Sin motivo no se distingue de una que se saltó |
| **Sin motivo queda un hueco marcado** | Un hueco se ve; un vacío no |
| **Hay una prueba de nombre** | Que no exista una función que se llame como si las fechas decidieran |

Señal registrada: [`S-110`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **Escribir el sello en la regla** no está: se arma el bloque y se devuelve. Escribirlo se hace por el módulo Ciclo de vida.
- **Responder las filas** sigue siendo de una persona, y así queda.
- **Sin pantalla**, como el resto del módulo.

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

| Documento | Qué se le agregó |
|---|---|
| [documentacion/reglas/spec.md](../../../../reglas/spec.md) | Su §13 nombra esta fase |
| [documentacion/senales.md](../../../../senales.md) | `S-110` |

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

**Ninguna migración y ninguna dependencia nueva.**
