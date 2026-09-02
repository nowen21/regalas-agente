# Funcionalidad implementada — Fase `V-EP-008-HU-005-lo-obligatorio-no-se-apaga` (módulo Proyectos)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [HU-005](../HU-005-configurar-que-rige-en-cada-proyecto.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `V-EP-008-HU-005-lo-obligatorio-no-se-apaga` |
| **Épica / HU** | [EP-008](../../epica.md) · [HU-005](../HU-005-configurar-que-rige-en-cada-proyecto.md) |
| **Módulo** | Proyectos |
| **Fecha de cierre** | 2026-09-01 |
| **Versión del estándar bajo la que cerró** | 37.2.1 |

---

## 1. Qué se implementó — resumen

**Un proyecto puede encender y apagar las reglas opcionales del estándar, y solo las opcionales.** De las 257 reglas, **49 son opcionales**; las demás rigen siempre y no aparecen en la lista.

**Lo obligatorio no se puede apagar, y ese es el punto entero.** Sin esa negativa, «configurable» quiere decir «el estándar rige cuando conviene».

**La lista de opcionales estuvo mal, y el error era del tamaño exacto del daño.** Buscar la marca en todo el archivo daba 52 reglas e incluía `02·F0` —la cadena completa del flujo de trabajo—, además de `R7` y `R8`, que ni siquiera son reglas: son los ejemplos del capítulo que explica cómo escribir una. Una marca vale donde está escrita, no en el archivo que la contiene.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| «Lo opcional lo dice el estándar» (`RN-1`) | servicio | `opcionales` en [plataforma/nucleo/proyectos/configuracion.py](../../../../../plataforma/nucleo/proyectos/configuracion.py) | ✅ | CP-004 |
| «Lo obligatorio no se apaga» (`RN-2`) | servicio | `poner` | ✅ | CP-002 |
| «De fábrica, apagado» (`RN-3`) | servicio | `rige` | ✅ | CP-001 |
| «Vive en el proyecto» (`RN-4`) | servicio | `CARPETA` y `ARCHIVO` | ✅ | CP-001 |
| «Ante la duda, obligatoria» (`RN-5`) | servicio | `rige` | ✅ | CP-002 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-01 | La lista de opcionales — **y su corrección, que fue el trabajo de verdad** |
| T-02 · T-03 | El estado escrito con fecha, y el rechazo con su porqué |
| T-04 · T-05 | Lo que se entrega por proyecto, y la orden de consola |
| T-06 | **14 pruebas** |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `plataforma/nucleo/proyectos/` | 14 pruebas de esta fase, en verde |
| La batería de la plataforma completa | 552 pruebas, en verde |
| La batería del estándar | 733 pruebas, en verde |

**Lo que las pruebas no dicen:** si el estándar marcó bien lo opcional, ni si apagar muchas reglas aleja dos proyectos.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Desde `plataforma/`:

```
python manage.py que_rige <proyecto>
python manage.py que_rige <proyecto> --encender DOC5 --cuando 2026-09-01
python manage.py que_rige <proyecto> --apagar DOC5 --cuando 2026-09-01
```

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| **Qué es opcional lo dice el estándar** | Una lista propia envejece en cuanto se marque una regla más |
| **La marca vale donde está escrita** | Buscarla en todo el archivo dio 52 reglas, y una era la cadena entera |
| **Ante la duda, es obligatoria** | La respuesta segura es la que no deja apagar nada |
| **La configuración vive en el proyecto** | Un proyecto clonado se quedaría sin ella |
| **Cambiar de estado reemplaza la fila** | La historia la guarda el control de versiones |

Señal registrada: [`S-115`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **Elegir moldes por proyecto se dejó para después**, cuando haya más de uno por documento.
- **Cada opción aleja dos proyectos**, y eso está declarado en la ficha.
- **Sin pantalla**, como el resto de los módulos de esta etapa.

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

| Documento | Qué se le agregó |
|---|---|
| [documentacion/proyectos/spec.md](../../../../proyectos/spec.md) | Su §13 nombra esta fase |
| [documentacion/senales.md](../../../../senales.md) | `S-115` |

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

**Ninguna migración y ninguna dependencia nueva.**
