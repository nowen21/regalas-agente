# Funcionalidad implementada — Fase `M-EP-017-HU-001-una-aprobacion-guarda-la-huella-del-texto` (módulo Aprobaciones)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [HU-001](../HU-001-registrar-una-aprobacion-con-su-firma.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `M-EP-017-HU-001-una-aprobacion-guarda-la-huella-del-texto` |
| **Épica / HU** | [EP-017](../../epica.md) · [HU-001](../HU-001-registrar-una-aprobacion-con-su-firma.md) |
| **Módulo** | Aprobaciones |
| **Fecha de cierre** | 2026-09-01 |
| **Versión del estándar bajo la que cerró** | 37.2.1 |

---

## 1. Qué se implementó — resumen

**Una aprobación ya dice quién, cuándo y sobre qué texto exacto.** Es la pieza de la que se sostiene el resto del gobierno, y hasta hoy no existía: las aprobaciones se escriben a mano dentro de los documentos, y **ninguna de las 21 de este repositorio dice sobre qué texto se dio**.

**Es el segundo módulo de la plataforma con una entidad propia**, y por un motivo que vale escribir: los demás calculan su respuesta al pedirla, porque está en el texto. **Esta no: el texto no sabe quién lo aprobó.**

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| «La aprobación guarda la huella» (`RN-1`) | modelo | `Aprobacion` en [plataforma/nucleo/aprobaciones/models.py](../../../../../plataforma/nucleo/aprobaciones/models.py) | ✅ | CP-001 |
| «No se aprueba lo que no existe» (`RN-2`) | servicio | `aprobar` en [plataforma/nucleo/aprobaciones/core.py](../../../../../plataforma/nucleo/aprobaciones/core.py) | ✅ | CP-002 |
| «Aprobar queda registrado» (`RN-3`) | servicio | `con_constancia` | ✅ | CP-001 |
| «Nada se borra» (`RN-4`) | modelo | Cada aprobación se agrega | ✅ | CP-001 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-01 · T-02 | La entidad con su huella, y aprobar leyendo el texto que hay |
| T-03 · T-04 | Rechazar lo que no existe, y el registro en la auditoría |
| T-05 · T-06 | La historia, y la orden de consola |
| T-07 | **7 pruebas** |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `plataforma/nucleo/aprobaciones/` | 7 pruebas de esta fase, en verde |
| La batería de la plataforma completa | 473 pruebas, en verde |
| La batería del estándar | 733 pruebas, en verde |

**Lo que las pruebas no dicen:** si quien aprueba es quien dice ser.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Desde `plataforma/`:

```
python manage.py aprobar <proyecto> <documento> --quien "Ing. José"
```

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| **La aprobación se guarda en la base** | El texto no sabe quién lo aprobó |
| **Se guarda la huella del texto** | Sin ella sería lo mismo que hay escrito a mano, con más pasos |
| **No se aprueba lo que no existe** | Sería firmar en blanco |
| **Se guarda también el tamaño** | Permite decir cuánto cambió, no solo que cambió |
| **Las 21 marcas a mano no se migran** | Dirían que se aprobó un texto que no se puede reconstruir |

Señal registrada: [`S-111`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **Las 21 marcas escritas a mano siguen ahí**, y así queda declarado. Migrarlas sería inventar aprobaciones.
- **No se comprueba quién aprueba.** Es la misma confianza que rige el resto de la plataforma.
- **Sin pantalla**, como el resto de los módulos de esta etapa.

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

| Documento | Qué se le agregó |
|---|---|
| [documentacion/aprobaciones/spec.md](../../../../aprobaciones/spec.md) | Nace: módulo nuevo |
| [documentacion/senales.md](../../../../senales.md) | `S-111` |
| [documentacion/epicas/README.md](../../../README.md) | `EP-017` |

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

**Una migración**, la de la tabla nueva. Ninguna dependencia nueva.
