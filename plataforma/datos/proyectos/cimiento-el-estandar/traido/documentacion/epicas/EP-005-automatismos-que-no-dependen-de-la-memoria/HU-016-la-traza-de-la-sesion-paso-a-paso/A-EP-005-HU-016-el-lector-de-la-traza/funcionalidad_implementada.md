# Funcionalidad implementada — Fase A-EP-005-HU-016-el-lector-de-la-traza (módulo Automatismos — lectores de la sesión)

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-005-HU-016-el-lector-de-la-traza` |
| **Módulo** | Automatismos — lectores de la sesión |
| **Especificación del módulo** | [documentacion/automatismos/spec.md](../../../../automatismos/spec.md) §4.9 |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | [HU-016](../HU-016-la-traza-de-la-sesion-paso-a-paso.md) ([CA-01](../HU-016-la-traza-de-la-sesion-paso-a-paso.md#ca-01--la-línea-de-tiempo-de-una-sesión) a [CA-04](../HU-016-la-traza-de-la-sesion-paso-a-paso.md#ca-04--lo-raro-no-revienta)) |
| **Fecha de cierre** | 2026-08-20 |
| **Commit** | Pendiente — el commit lo autoriza el usuario aparte (`00·N2`) |

---

## 1. Qué se implementó — resumen

La traza de la sesión: `validar.py traza <transcripción>` saca la línea de tiempo de lo que el agente ejecutó — cada herramienta con su hora, lo que se le pidió, cuánto tardó y si falló — y con `--escribir` la deja en `historico-chat/trazas/` con el mismo nombre que el histórico de esa sesión. La primera traza real ya está escrita: la de esta misma sesión, 191 pasos.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem del especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| RN-52 · un paso por llamada, emparejado por identificador, con duración | servicio | `validadores/traza.py` (`pasos`) | ✅ | CP-001 y el caso de respuestas desordenadas |
| RN-53 · la fila y el cierre | servicio | `validadores/traza.py` (`como_texto`, `cierre`) | ✅ | CP-001, CP-002 |
| RN-54 · no copia contenido de resultados | servicio | `validadores/traza.py` (`_resumen_entrada`) | ✅ | CP-001 paso 4 y la verificación manual |
| RN-55 · `--escribir` junto al histórico, indexada una vez | servicio | `validadores/traza.py` (`escribir`, `_indexar`) · `validadores/historico.py` (`archivo_de_sesion`) | ✅ | CP-003, CP-004 |
| RN-56 · lo raro no revienta; vacío o inexistente da frase y código 1 | servicio | `validadores/validar.py` (`cmd_traza`) · `validadores/traza.py` | ✅ | CP-005 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-01 | `pasos(ruta)`: emparejar, recortar, medir | ✅ hecha | `validadores/traza.py` | EV-01 |
| T-02 | `como_texto`: las filas | ✅ hecha | `validadores/traza.py` | EV-01 |
| T-03 | `cierre(pasos)` y su texto | ✅ hecha | `validadores/traza.py` | EV-01 |
| T-04 | `archivo_de_sesion`; `escribir` con índice; subcomando | ✅ hecha | `validadores/historico.py` · `validadores/traza.py` · `validadores/validar.py` | EV-01 |
| T-05 | Los casos | ✅ hecha | `validadores/tests/test_la_sesion_tiene_traza.py` (6 casos) | EV-01 |
| T-06 | Especificación §4.9 y §13, mapa del sitio, README del histórico | ✅ hecha | `documentacion/automatismos/spec.md` · `anatomia/mapa-del-sitio.md` · `historico-chat/README.md` | EV-03 y este documento |
| T-07 | Trazar una sesión real | ✅ hecha | `historico-chat/trazas/2026-08-20-sesion-5.md` | EV-02 |

**Correspondencia con el plan:** 7 tareas en el plan, 7 acá.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba**  ·  [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md):

| Archivo | Por qué hubo que tocarlo | Quién autorizó ampliar el plan |
|---|---|---|
| `anatomia/que-esta-amarrado-a-la-herramienta.md` | La pieza nueva sube el recuento a 24 de 69 y su prueba exige el mapa al día; el plan lo declaró para la fase del portero y esta lo volvió a tocar | Mantenimiento que la propia prueba reclama; quedó dicho acá |
| `historico-chat/trazas/` (la traza real y su índice) | Es el producto de T-07: lo escribe el programa nuevo | El plan lo pedía en T-07 |

**Esfuerzo real contra estimado:** ~2,5 h contra 4,5 h del plan.

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

- **Fuente:** [resultado_pruebas.md](resultado_pruebas.md) · **Veredicto:** Cumple.
- **Suites ejecutadas + resultado:** la suite nueva 6/6; `validadores/tests/` (488) y `pruebas.py` (365) con solo las fallas ajenas y anteriores; `validar.py amarre` OK con `traza.py` libre.
- **Verificaciones manuales:** la traza real de esta sesión leída completa: 191 pasos (igual al conteo directo), 0,69 s, sin contenido de resultados.
- **Defectos abiertos que se aceptaron:** ninguno.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

- **Punto de entrada:** `python validadores/validar.py traza <transcripción>` para verla; con `--escribir --raiz <proyecto>` queda en `historico-chat/trazas/` junto a su histórico. La transcripción es el archivo de líneas JSON de la sesión (la ruta llega en `transcript_path` a los enganches, o se toma de la carpeta de la herramienta).
- **Permisos o datos base sembrados:** ninguno.

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Lector a demanda, no enganche; sin copiar resultados; nombrada como su histórico; emparejar por identificador | Cero cambios en nueve proyectos; privacidad; los dos archivos emparejados a la vista; las llamadas en paralelo desordenan las respuestas | S-017 en [documentacion/senales.md](../../../../senales.md) |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino (fase futura / ticket / `pendientes/`) |
|---|---|---|
| Escribir la traza sola al cerrar la sesión (un enganche de una línea sobre este lector) | Diferido por el plan | Otra historia, si algún día conviene; quedó en el fuera de alcance |

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

- [x] Mapa del sitio con `traza.py`.
- [x] Mapa del amarre: 24 amarradas de 69, `traza.py` entre las libres.
- [x] Especificación del módulo §4.9 y §13.
- [x] README del histórico con el párrafo de `trazas/`.
- [x] `CHANGELOG.md` 28.0.0 (la traza viaja en la misma entrada que el portero).

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

Nada que desplegar: es un subcomando que viaja con `validadores/` en el `git pull`. Reversión: revertir el commit.
