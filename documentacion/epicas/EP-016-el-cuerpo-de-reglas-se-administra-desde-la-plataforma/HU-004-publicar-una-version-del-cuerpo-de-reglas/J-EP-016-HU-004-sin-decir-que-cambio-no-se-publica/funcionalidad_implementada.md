# Funcionalidad implementada — Fase `J-EP-016-HU-004-sin-decir-que-cambio-no-se-publica` (módulo Reglas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [HU-004](../HU-004-publicar-una-version-del-cuerpo-de-reglas.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `J-EP-016-HU-004-sin-decir-que-cambio-no-se-publica` |
| **Épica / HU** | [EP-016](../../epica.md) · [HU-004](../HU-004-publicar-una-version-del-cuerpo-de-reglas.md) |
| **Módulo** | Reglas |
| **Fecha de cierre** | 2026-09-01 |
| **Versión del estándar bajo la que cerró** | 37.2.1 |

---

## 1. Qué se implementó — resumen

**Una versión se publica solo cuando tres cosas se cumplen:** el número está libre, el registro dice qué cambió con su tipo, y la puerta de `F-022` pasa. Lo que falte sale **todo junto**, y si falta algo **el archivo de versión no se toca**.

**Con esto se cierra la vuelta de la columna de dependencias** que parecía impedir arrancar la versión 3.

**Y lo que la plataforma no hace, a propósito:** escribir la entrada del registro. Es prosa, dice qué pasó y por qué importa, y generada diría lo mismo siempre.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| «Un número no se publica dos veces» (`RN-1`) | servicio | `revisar` en [plataforma/nucleo/reglas/publicacion.py](../../../../../plataforma/nucleo/reglas/publicacion.py) | ✅ | CP-001 |
| «Sin entrada no se publica» (`RN-2`) | servicio | `entrada_del_registro` | ✅ | CP-002 |
| «Si la puerta no pasa, no se publica» (`RN-3`) | servicio | `puerta.revisar_antes_de_publicar` | ✅ | CP-003 |
| «Lo que falta se dice todo junto» (`RN-4`) | servicio | `NoSePuedePublicar` | ✅ | CP-004 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-01 · T-02 | La entrada del registro, recortada, y su tipo **en los dos órdenes** |
| T-03 · T-04 | El número libre, y la puerta |
| T-05 · T-06 | Todo lo que falte junto, y escribir solo si no falta nada |
| T-07 · T-08 | La orden, y 13 pruebas |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `plataforma/nucleo/reglas/tests_publicacion.py` | 13 pruebas, en verde |
| La batería de la plataforma completa | 426 pruebas, en verde |
| La batería del estándar | 733 pruebas, en verde |

**Lo que las pruebas no dicen:** si la puerta acierta. Eso lo probó su propia fase.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Desde `plataforma/`:

```
python manage.py publicar_version <proyecto> 37.3.0
python manage.py publicar_version <proyecto> 37.3.0 --igual-la-publico
```

**Sin `--igual-la-publico` no publica:** la revisión se puede pedir todas las veces que haga falta antes de decidir.

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| **La plataforma no escribe la entrada del registro** | Es prosa; generada diría lo mismo siempre |
| **Una entrada sin tipo tampoco pasa** | Suponer el tipo es decidir por el que adopta |
| **Lo que falta se dice todo junto** | De a uno obliga a intentar tres veces |
| **La revisión se puede pedir sin publicar** | Sirve para saber qué falta antes de decidir |
| **El tipo se lee en los dos órdenes** | El registro se escribió de las dos formas |

Señal registrada: [`S-110`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **La puerta se simula en las pruebas.** Correrla de verdad tarda dos minutos por prueba; que acierte lo probó su propia fase.
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
