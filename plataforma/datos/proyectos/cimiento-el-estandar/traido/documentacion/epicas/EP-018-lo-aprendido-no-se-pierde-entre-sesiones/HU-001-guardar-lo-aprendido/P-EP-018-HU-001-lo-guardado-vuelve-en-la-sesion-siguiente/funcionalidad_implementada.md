# Funcionalidad implementada — Fase `P-EP-018-HU-001-lo-guardado-vuelve-en-la-sesion-siguiente` (módulo Memoria)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [HU-001](../HU-001-guardar-lo-aprendido.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `P-EP-018-HU-001-lo-guardado-vuelve-en-la-sesion-siguiente` |
| **Épica / HU** | [EP-018](../../epica.md) · [HU-001](../HU-001-guardar-lo-aprendido.md) |
| **Módulo** | Memoria |
| **Fecha de cierre** | 2026-09-01 |
| **Versión del estándar bajo la que cerró** | 37.2.1 |

---

## 1. Qué se implementó — resumen

**Los recuerdos se leen, se buscan y se guardan desde la plataforma**, sobre los mismos archivos donde ya vivían.

**El módulo no inventó un lugar nuevo, y eso es lo importante.** `01·C19` ya había decidido que la memoria del agente es un archivo del repositorio y no un ajuste de la herramienta. Lo que faltaba era poder trabajarla sin abrir los archivos a mano.

**Guardar no pisa.** En un módulo cuyo único trabajo es no perder nada, sobrescribir por reusar un nombre sería el único fallo irreparable.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| «Vive donde no se borra» (`RN-1`) | servicio | `CARPETA` en [plataforma/nucleo/memoria/core.py](../../../../../plataforma/nucleo/memoria/core.py) | ✅ | CP-001 |
| «Guardar no pisa» (`RN-2`) | servicio | `guardar` | ✅ | CP-002 |
| «Su línea en el índice» (`RN-3`) | servicio | `guardar` | ✅ | CP-001 |
| «Un tema vacío se dice» (`RN-5`) | servicio | `buscar` | ✅ | CP-003 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-01 · T-02 | Leer la carpeta y el índice, y separar vigentes de dados de baja |
| T-03 · T-04 | Buscar por palabra, y guardar sin pisar |
| T-05 · T-06 | El resumen, y la orden de consola |
| T-07 | **6 pruebas** |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `plataforma/nucleo/memoria/` | 6 pruebas de esta fase, en verde |
| La batería de la plataforma completa | 473 pruebas, en verde |
| La batería del estándar | 733 pruebas, en verde |

**Lo que las pruebas no dicen:** si lo guardado sigue siendo cierto.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Desde `plataforma/`:

```
python manage.py memoria <proyecto>
python manage.py memoria <proyecto> --buscar <palabra>
```

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| **Sin entidad en la base** | Todo lo que el módulo responde está en el texto (`DA-01`) |
| **Guardar no pisa** | Perder un recuerdo es el único fallo irreparable acá |
| **Se lee al pedir, sin caché** | Los archivos cambian por fuera, y el caché mentiría |
| **Un tema vacío se dice con palabras** | Un vacío se ve igual que una falla — `S-110` |

Señal registrada: [`S-112`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **Nada revisa si un recuerdo sigue siendo cierto.** Declarado y aceptado.
- **Sin pantalla**, como el resto de los módulos de esta etapa.

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

| Documento | Qué se le agregó |
|---|---|
| [documentacion/memoria/spec.md](../../../../memoria/spec.md) | Nace: módulo nuevo |
| [documentacion/senales.md](../../../../senales.md) | `S-112` |
| [documentacion/epicas/README.md](../../../README.md) | `EP-018` |

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

**Ninguna migración y ninguna dependencia nueva.**
