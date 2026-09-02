# Funcionalidad implementada — Fase `X-EP-020-HU-002-sin-datos-no-es-cero` (módulo Avisos)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [HU-002](../HU-002-reportar-como-va-cada-proyecto.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `X-EP-020-HU-002-sin-datos-no-es-cero` |
| **Épica / HU** | [EP-020](../../epica.md) · [HU-002](../HU-002-reportar-como-va-cada-proyecto.md) |
| **Módulo** | Avisos |
| **Fecha de cierre** | 2026-09-01 |
| **Versión del estándar bajo la que cerró** | 37.2.1 |

---

## 1. Qué se implementó — resumen

**Cada proyecto conectado sale con su avance, su deuda, su deuda vencida y lo que lleva quieto sin decir desde cuándo** — y con la definición de cada columna impresa debajo de la tabla.

**Un proyecto sin datos aparece así, no en cero.** Cero fases terminadas de cero es una división que no existe, y escribir «cero por cien» ahí dice que el proyecto va mal cuando lo que pasa es que no se sabe. Van al final de la lista: no son los peores, son los que no se sabe.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| «La misma medida, y escrita» (`RN-1`) | servicio | `QUE_MIDE` en [plataforma/nucleo/avisos/reporte.py](../../../../../plataforma/nucleo/avisos/reporte.py) | ✅ | CP-004 |
| «Deuda y vencida separadas» (`RN-2`) | servicio | `de_un_proyecto` | ✅ | CP-004 |
| «Sin datos no es cero» (`RN-3`) | servicio | `como_se_escribe` | ✅ | CP-005 |
| «Los sin datos van al final» (`RN-4`) | servicio | `de_todos` | ✅ | CP-005 |
| «Lo no verificado se reporta así» (`RN-5`) | servicio | La deuda incluye lo construido sin verificar | ✅ | CP-004 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-01 · T-02 | La fila de cada proyecto, y el avance o el «sin datos» |
| T-03 · T-04 | La deuda y la vencida separadas, y la definición impresa |
| T-05 · T-06 | La orden de consola, y **7 pruebas** |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `plataforma/nucleo/avisos/` | 7 pruebas de esta fase, en verde |
| La batería de la plataforma completa | 552 pruebas, en verde |
| La batería del estándar | 733 pruebas, en verde |

**Lo que las pruebas no dicen:** si la misma medida es justa entre proyectos muy distintos.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Desde `plataforma/`:

```
python manage.py como_van --hoy 2026-09-01
python manage.py como_van --hoy 2026-09-01 --dias 60
```

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| **La definición sale con la tabla** | Una definición que vive en otro archivo no se lee |
| **Sin datos no es cero** | Cero dice «va mal»; sin datos dice «no se sabe» |
| **Los sin datos van al final** | No son los peores: son los que no se sabe |
| **La deuda y la vencida, separadas** | Diez avisos recientes y diez de hace un año no son lo mismo |
| **Las quietas tienen su propia columna** | No saber no es deuda: es no saber |

Señal registrada: [`S-116`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **La misma medida entre proyectos muy distintos puede engañar**, y solo se contrarresta con la definición impresa.
- **El avance mide fases cerradas**, no funcionalidad entregada.
- **Sin pantalla**, como el resto de los módulos de esta etapa.

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

| Documento | Qué se le agregó |
|---|---|
| [documentacion/avisos/spec.md](../../../../avisos/spec.md) | Su §13 nombra esta fase, y con ella cierra `EP-020` |

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

**Ninguna migración y ninguna dependencia nueva.**
