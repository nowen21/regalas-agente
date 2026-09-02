# Funcionalidad implementada — Fase `R-EP-009-HU-002-la-auditoria-se-puede-preguntar` (módulo Auditoría)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [HU-002](../HU-002-buscar-en-la-auditoria.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `R-EP-009-HU-002-la-auditoria-se-puede-preguntar` |
| **Épica / HU** | [EP-009](../../epica.md) · [HU-002](../HU-002-buscar-en-la-auditoria.md) |
| **Módulo** | Auditoría |
| **Fecha de cierre** | 2026-09-01 |
| **Versión del estándar bajo la que cerró** | 37.2.1 |

---

## 1. Qué se implementó — resumen

**La auditoría se puede preguntar**: por proyecto, por rango de fechas y por tipo de acción, con lo hallado de lo más reciente a lo más viejo.

**Con esta fase `EP-009` queda completa.** La fase `D` dejó todo registrado, con la constancia antes que el efecto; faltaba la otra mitad, y la ficha de `F-019` la resumía así: *«sin esta, la auditoría existe pero no sirve»*.

**El hallazgo de la fase fue un borde.** La fecha se guarda como texto con la hora pegada, así que un rango armado con el `hasta` tal cual **corta el último día en la medianoche** — y deja invisible justo lo más reciente. Salió probando, no leyendo.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| «Los tres filtros» (`RN-1`) | servicio | `buscar` en [plataforma/nucleo/auditoria/busqueda.py](../../../../../plataforma/nucleo/auditoria/busqueda.py) | ✅ | CP-001 |
| «De lo más reciente a lo más viejo» (`RN-2`) | servicio | `buscar` | ✅ | CP-001 |
| «Sin coincidencias se dice» (`RN-3`) | servicio | `dicho` | ✅ | CP-003 |
| «Si se recorta, se avisa» (`RN-4`) | servicio | `se_recorto` | ✅ | CP-004 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-01 · T-02 | Los tres filtros, y **el último día del rango entrando completo** |
| T-03 · T-04 | El aviso de vacío, y el tiempo con el aviso de recorte |
| T-05 · T-06 | Los tipos de acción sacados de lo registrado, y la orden de consola |
| T-07 | **14 pruebas** |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `plataforma/nucleo/auditoria/` | 14 pruebas de esta fase, en verde |
| La batería de la plataforma completa | 473 pruebas, en verde |
| La batería del estándar | 733 pruebas, en verde |

**Lo que las pruebas no dicen:** cuánto tarda con un año de registros de verdad.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Desde `plataforma/`:

```
python manage.py buscar_en_la_auditoria <proyecto>
python manage.py buscar_en_la_auditoria <proyecto> --desde 2026-08-01 --hasta 2026-09-01 --accion aprobar
```

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| **El día del `hasta` entra completo** | Sin esto se pierde el último día entero, que es justo lo más reciente |
| **La respuesta dice cuántos y en cuánto tiempo** | El criterio pide un tiempo medido, no supuesto |
| **Un vacío se dice con palabras** | Un vacío se ve igual que una falla — `S-110` |
| **Si se recorta, se avisa** | Un recorte callado se lee como «eso es todo lo que hay» |
| **Los tipos de acción salen de lo registrado** | Una lista fija en el código envejece sin avisar |

Señal registrada: [`S-113`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **El tiempo con un año de registros habrá que volverlo a medir** cuando la auditoría real acumule ese volumen.
- **Sin pantalla**, como el resto de los módulos de esta etapa.

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

| Documento | Qué se le agregó |
|---|---|
| [documentacion/auditoria/spec.md](../../../../auditoria/spec.md) | Su §13 nombra esta fase |
| [documentacion/epicas/EP-009-todo-lo-que-se-hace-queda-registrado/epica.md](../../epica.md) | La `HU-002`, y la épica queda completa |
| [documentacion/senales.md](../../../../senales.md) | `S-113` |

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

**Ninguna migración y ninguna dependencia nueva.**
