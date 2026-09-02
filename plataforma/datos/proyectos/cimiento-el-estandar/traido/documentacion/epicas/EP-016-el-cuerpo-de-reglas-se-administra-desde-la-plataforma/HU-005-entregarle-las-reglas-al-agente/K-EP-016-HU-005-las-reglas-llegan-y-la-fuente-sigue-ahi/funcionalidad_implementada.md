# Funcionalidad implementada — Fase `K-EP-016-HU-005-las-reglas-llegan-y-la-fuente-sigue-ahi` (módulo Reglas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [HU-005](../HU-005-entregarle-las-reglas-al-agente.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `K-EP-016-HU-005-las-reglas-llegan-y-la-fuente-sigue-ahi` |
| **Épica / HU** | [EP-016](../../epica.md) · [HU-005](../HU-005-entregarle-las-reglas-al-agente.md) |
| **Módulo** | Reglas |
| **Fecha de cierre** | 2026-09-01 |
| **Versión del estándar bajo la que cerró** | 37.2.1 |

---

## 1. Qué se implementó — resumen

**Las reglas vigentes de un proyecto se entregan enteras**, con su cuenta y bajo qué versión rigen. Sobre este repositorio: **248 reglas en 124 archivos, 679 511 caracteres, en 0,17 segundos** contra un límite de dos.

**Se entrega el texto, no un resumen.** Un resumen de una regla es otra regla.

**Y la fuente se nombra siempre**, se haya podido o no. Es lo que recuerda que esta pieza acelera y ordena, pero **no es un intermediario sin el cual no se puede**.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| «Se entrega el texto» (`RN-1`) | servicio | `entregar` en [plataforma/nucleo/reglas/entrega.py](../../../../../plataforma/nucleo/reglas/entrega.py) | ✅ | CP-001 |
| «Se dice bajo qué versión rige» (`RN-2`) | servicio | `encabezado` | ✅ | CP-001 |
| «Si no se puede, se dice dónde está la fuente» (`RN-3`) | servicio | `donde_esta_la_fuente` | ✅ | CP-003 |
| «La fuente se nombra siempre» (`RN-4`) | servicio | El campo va en las dos salidas | ✅ | CP-003 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-01 · T-02 | Los capítulos en su orden, con su texto y su ruta relativa |
| T-03 · T-04 | La cuenta de vigentes, y el tiempo |
| T-05 | La fuente, nombrada pase lo que pase |
| T-06 · T-07 | La orden, y 9 pruebas |
| T-08 | **0,17 s sobre 679 511 caracteres** |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `plataforma/nucleo/reglas/tests_entrega.py` | 9 pruebas, en verde |
| La batería de la plataforma completa | 426 pruebas, en verde |
| La batería del estándar | 733 pruebas, en verde |
| La medición sobre este repositorio | 0,17 s |

**Lo que las pruebas no dicen:** cómo se comporta con un cuerpo de reglas diez veces más grande.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Desde `plataforma/`:

```
python manage.py entregar_reglas <proyecto>
python manage.py entregar_reglas <proyecto> --con-el-texto
```

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| **Se entrega el texto, no un resumen** | Un resumen de una regla es otra regla |
| **La fuente se nombra siempre** | Recuerda que esto no es un intermediario obligatorio |
| **Un fallo se dice, no se devuelve vacío** | Una lista vacía se leería como «no hay reglas» |
| **El tiempo se reporta** | El límite de la ficha es un número, y se comprueba con otro |

Señal registrada: [`S-110`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **Enchufarlo al arranque de una sesión** no está: hoy es una orden que se pide. El enganche que carga las reglas sigue leyendo la fuente directamente, y eso **es correcto por diseño**.
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
