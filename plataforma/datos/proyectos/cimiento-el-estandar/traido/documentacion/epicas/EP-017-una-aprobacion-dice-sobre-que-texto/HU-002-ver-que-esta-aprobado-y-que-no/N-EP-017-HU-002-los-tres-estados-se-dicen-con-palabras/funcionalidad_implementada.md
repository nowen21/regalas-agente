# Funcionalidad implementada — Fase `N-EP-017-HU-002-los-tres-estados-se-dicen-con-palabras` (módulo Aprobaciones)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [HU-002](../HU-002-ver-que-esta-aprobado-y-que-no.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `N-EP-017-HU-002-los-tres-estados-se-dicen-con-palabras` |
| **Épica / HU** | [EP-017](../../epica.md) · [HU-002](../HU-002-ver-que-esta-aprobado-y-que-no.md) |
| **Módulo** | Aprobaciones |
| **Fecha de cierre** | 2026-09-01 |
| **Versión del estándar bajo la que cerró** | 37.2.1 |

---

## 1. Qué se implementó — resumen

**De cada documento se sabe en cuál de los tres estados está**, y se dice con palabras: aprobado, la aprobación caducó, o nadie lo ha aprobado todavía.

**Son tres y no dos, y eso es lo que la fase decidió.** «Caducada» dice que hubo un juicio y que algo lo invalidó; «sin aprobación», que nunca lo hubo. Meterlas en el mismo cajón pierde justo la información que hace falta.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| «Los tres estados se dicen con palabras» (`RN-1`) | servicio | `EN_PALABRAS` en [plataforma/nucleo/aprobaciones/core.py](../../../../../plataforma/nucleo/aprobaciones/core.py) | ✅ | CP-005 |
| «Sin aprobación aparece, no vacío» (`RN-2`) | servicio | `estado_de` | ✅ | CP-005 |
| «Se ve desde cuándo y por quién» (`RN-3`) | servicio | Los campos `desde` y `quien` | ✅ | CP-005 |
| «La frase de caducada dice por qué» (`RN-4`) | servicio | `EN_PALABRAS` | ✅ | CP-005 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-01 · T-02 | Los tres estados con su frase, y la comparación de huellas |
| T-03 · T-04 | Desde cuándo y por quién, y que lo sin aprobación aparezca |
| T-05 · T-06 | La orden de consola, y 4 pruebas |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `plataforma/nucleo/aprobaciones/` | 4 pruebas de esta fase, en verde |
| La batería de la plataforma completa | 473 pruebas, en verde |
| La batería del estándar | 733 pruebas, en verde |

**Lo que las pruebas no dicen:** si las frases se entienden.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Desde `plataforma/`:

```
python manage.py aprobaciones <proyecto>
python manage.py aprobaciones <proyecto> --documento documentacion/x/spec.md
```

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| **Tres estados, no dos** | Meter «caducada» en cualquiera de los otros dos miente |
| **Cada estado con su frase** | Quien no distingue colores tiene que poder saberlo |
| **La frase de caducada dice por qué** | Lo primero que hay que ver es qué cambió |
| **Ninguno es «rechazado»** | La plataforma no rechaza: registra lo que pasó |

Señal registrada: [`S-111`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **Sin pantalla**, como el resto de los módulos de esta etapa.
- **Solo se listan los documentos que tienen alguna aprobación.** Listar todos los del proyecto es del módulo Expediente, que ya sabe cuáles son.

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

| Documento | Qué se le agregó |
|---|---|
| [documentacion/aprobaciones/spec.md](../../../../aprobaciones/spec.md) | Su §13 nombra esta fase |

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

**Ninguna migración y ninguna dependencia nueva.**
