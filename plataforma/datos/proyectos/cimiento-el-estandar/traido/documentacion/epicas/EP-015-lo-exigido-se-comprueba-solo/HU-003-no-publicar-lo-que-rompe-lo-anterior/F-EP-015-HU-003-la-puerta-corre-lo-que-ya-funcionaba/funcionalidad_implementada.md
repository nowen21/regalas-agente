# Funcionalidad implementada — Fase `F-EP-015-HU-003-la-puerta-corre-lo-que-ya-funcionaba` (módulo Comprobaciones)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [HU-003](../HU-003-no-publicar-lo-que-rompe-lo-anterior.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `F-EP-015-HU-003-la-puerta-corre-lo-que-ya-funcionaba` |
| **Épica / HU** | [EP-015](../../epica.md) · [HU-003](../HU-003-no-publicar-lo-que-rompe-lo-anterior.md) |
| **Módulo** | Comprobaciones |
| **Fecha de cierre** | 2026-09-01 |
| **Versión del estándar bajo la que cerró** | 37.2.0 |

---

## 1. Qué se implementó — resumen

**Antes de publicar se vuelve a correr todo lo que ya funcionaba**, con una sola orden: las 32 comprobaciones del estándar y la suite del proyecto. Si algo está en rojo, no se publica.

**Y las tres respuestas se mantienen separadas:**

| Estado | Qué hace la puerta |
|---|---|
| Algo en rojo | **Detiene** |
| Una funcionalidad en «no cumple» | **Detiene, y la nombra** |
| Funcionalidades sin verificar | **Las declara y no detiene** |
| No se pudo revisar | **No pasa** |

Sobre este repositorio: **118,6 segundos, y pasa**.

**Con esta fase cierra `EP-015`**, y con ella la vuelta de la columna de dependencias: `F-008` ya tiene su puerta.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| «Lo que rompe algo no se publica» (`RN-1`) | servicio | `Puerta.pasa` en [plataforma/nucleo/comprobaciones/puerta.py](../../../../../plataforma/nucleo/comprobaciones/puerta.py) | ✅ | CP-001 |
| «Lo que obliga a rehacer se declara» (`RN-2`) | servicio | `rehacer` | ✅ | CP-002 |
| «Lo sin verificar se declara y no detiene» (`RN-3`) | servicio | `sin_verificar` | ✅ | CP-002 |
| «No haber podido revisar no es haber pasado» (`RN-4`) | servicio | `se_pudo` y `pruebas["corrio"]` | ✅ | CP-004 |
| «Una sola orden» (`RN-5`) | orden | `puerta_de_publicacion` | ✅ | CP-003 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-01 · T-02 | La puerta que junta veredicto, suite y estado |
| T-03 | Que un «no se pudo» no pase |
| T-04 | La orden, con el tiempo |
| T-05 | **14 pruebas** |
| T-06 | **118,6 s, y pasa** — después de arreglar un rojo falso |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `plataforma/nucleo/comprobaciones/` | 38 pruebas, en verde |
| La batería de la plataforma completa | 353 pruebas, en verde |
| La batería del estándar | 733 pruebas, en verde |
| La puerta sobre este repositorio | Pasa, en 118,6 s |

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Desde `plataforma/`:

```
python manage.py puerta_de_publicacion <identificador>
```

Una sola orden. Si pasar la puerta costara varios pasos, se saltaría.

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| **«Lo que ya funcionaba» es todo, no una lista** | Una lista escrita a mano se queda corta justo en lo que nadie se acordó |
| **Un «no se pudo» no pasa** | Es la forma más silenciosa de publicar a ciegas |
| **Lo sin verificar se declara y no detiene** | Detener con eso volvería la puerta inútil desde el primer día |
| **Se corre la suite del proyecto**, no la del estándar | El otro subcomando corre lo del estándar donde el estándar vive, y **dio un rojo falso** |
| **Una sola orden** | Si cuesta trabajo manual, se salta |

Señal registrada: [`S-108`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **118,6 segundos.** Es el precio de correr todo. Se aguanta antes de publicar, que es cuando se pide.
- **La puerta no impide publicar todavía**, porque publicar es `F-008` y no está construido. Hoy es una orden que se pide; cuando exista `F-008`, se enchufa.
- **Sin pantalla**, como el resto del módulo.

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

| Documento | Qué se le agregó |
|---|---|
| [documentacion/comprobaciones/spec.md](../../../../comprobaciones/spec.md) | Su §13 nombra esta fase |
| [documentacion/senales.md](../../../../senales.md) | `S-108` |

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

**Ninguna migración y ninguna dependencia nueva.**
