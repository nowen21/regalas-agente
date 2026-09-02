# Funcionalidad implementada — Fase `E-EP-015-HU-002-el-estado-sale-de-la-fase-que-corrio` (módulo Comprobaciones)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [HU-002](../HU-002-fijar-el-estado-desde-la-evidencia.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `E-EP-015-HU-002-el-estado-sale-de-la-fase-que-corrio` |
| **Épica / HU** | [EP-015](../../epica.md) · [HU-002](../HU-002-fijar-el-estado-desde-la-evidencia.md) |
| **Módulo** | Comprobaciones |
| **Fecha de cierre** | 2026-09-01 |
| **Versión del estándar bajo la que cerró** | 37.2.0 |

---

## 1. Qué se implementó — resumen

**El estado de una funcionalidad ya lo fija la fase que la construyó.** Antes las 35 del inventario decían «Sin verificar» porque nada convertía una prueba corrida en un estado. Ahora **14 están verificadas**, y son exactamente las construidas.

El estado **se deriva al pedirlo, siguiendo una cadena que ya estaba escrita**:

```
inventario -> especificacion del modulo (13) -> fase -> veredicto
```

Y trae su porqué: un estado sin origen es una opinión.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| «El estado se deriva, no se escribe» (`RN-1`) | servicio | `estado_de_todas` en [plataforma/nucleo/comprobaciones/estado.py](../../../../../plataforma/nucleo/comprobaciones/estado.py) | ✅ | CP-001 |
| «Sin prueba no se cierra» (`RN-2`) | servicio | `se_puede_cerrar` | ✅ | CP-002 |
| «Con prueba fallida, no cumple» (`RN-3`) | servicio | `NO_CUMPLE` | ✅ | CP-003 |
| «El estado dice de dónde sale» (`RN-4`) | servicio | El campo `porque` | ✅ | CP-001 |
| «Las dos formas de veredicto» (`CA-04`) | servicio | `_CONCEPTO` | ✅ | CP-004 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-01 · T-02 | Leer el inventario y seguir la trazabilidad hasta la fase |
| T-03 | **Las dos formas de veredicto**, que era un defecto real |
| T-04 · T-05 | El estado con su porqué, y las siete filas completadas |
| T-06 · T-07 | La orden de consola, y 11 pruebas |
| T-08 | **14 verificadas de 35** |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `plataforma/nucleo/comprobaciones/` | 24 pruebas, en verde |
| La batería de la plataforma completa | 353 pruebas, en verde |
| La batería del estándar | 733 pruebas, en verde |
| La cuenta sobre este repositorio | 14 verificadas, 21 sin verificar |

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Desde `plataforma/`:

```
python manage.py estado_funcionalidades <identificador>
python manage.py estado_funcionalidades <identificador> --solo "sin verificar"
```

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| **El estado se deriva al pedirlo** | Una copia escrita envejece y vuelve a ser lo que alguien cree |
| **Se leen las dos formas de veredicto** | Una fase cerrada dice lo que era cierto el día que cerró. El que se adapta es el que lee |
| **Las filas de trazabilidad se completan** | Una letra sola es ambigua: cada épica tiene su «A» |
| **El estado dice de dónde sale** | Un estado sin origen es una opinión |
| **Con varias fases, verificada solo si todas declararon** | Una funcionalidad a medias no está verificada |

Señal registrada: [`S-108`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **21 funcionalidades sin verificar**, y está bien: nadie las ha construido. Es la respuesta correcta, no una deuda.
- **La columna «Verificado» del inventario** ya no se mantiene a mano. Queda dicho ahí mismo.
- **Sin pantalla**, como el resto del módulo.

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

| Documento | Qué se le agregó |
|---|---|
| [documentacion/comprobaciones/spec.md](../../../../comprobaciones/spec.md) | Su §13 nombra esta fase |
| [documentacion/proyectos/spec.md](../../../../proyectos/spec.md) · [auditoria](../../../../auditoria/spec.md) · [importacion](../../../../importacion/spec.md) | Las siete filas completadas, con su registro en la §15 |
| [documentacion/senales.md](../../../../senales.md) | `S-108` |

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

**Ninguna migración y ninguna dependencia nueva.**
