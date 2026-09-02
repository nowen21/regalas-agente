# Funcionalidad implementada — Fase `A-EP-011-HU-001-lo-conversado-se-indexa-y-se-busca` (módulo Medición)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-001-buscar-en-lo-conversado/HU-001-buscar-en-lo-conversado.md](../HU-001-buscar-en-lo-conversado.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-011-HU-001-lo-conversado-se-indexa-y-se-busca` |
| **Épica / HU** | [documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/epica.md](../../epica.md) · [documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-001-buscar-en-lo-conversado/HU-001-buscar-en-lo-conversado.md](../HU-001-buscar-en-lo-conversado.md) |
| **Módulo** | Medición |
| **Fecha de cierre** | 2026-08-31 |

---

## 1. Qué se implementó — resumen

**Lo conversado se puede buscar.** 67 sesiones y 3 720 mensajes de este repositorio quedaron indexados, y una palabra dicha se encuentra con su sesión, su turno y quién la dijo.

**Sin tocar un solo archivo del histórico**, comprobado por huella sobre los 329 que hay. La fuente sigue siendo el texto que el enganche escribió; el índice se borra entero y se rehace leyéndolo.

Es la fuente de la `HU-002`: sin poder buscar en lo conversado no hay nada que contar.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| «Se recorre `historico-chat/` y se parte en mensajes» (§6) | servicio | `indexar` en [plataforma/nucleo/medicion/core.py](../../../../../plataforma/nucleo/medicion/core.py) | ✅ | CP-001 |
| «Archivo que no se puede leer: se reporta y no se detiene el resto» (§6) | servicio | `indexar`, la lista `ilegibles` | ✅ | CP-003 |
| «Archivo sin marcas: sesión sin mensajes, y se dice» (§6) | servicio | `indexar` | ✅ | CP-003 |
| «Proyecto con la ruta perdida: se responde con la ruta que se buscó» (§6) | servicio | `NoSePuedeIndexar` | ✅ | CP-003 |
| «Se borra entero y se vuelve a leer» (§6) | servicio | `reconstruir_indice` | ✅ | CP-002 |
| «Se responde con las sesiones donde aparece, y en qué mensaje» (§6) | servicio | `buscar` | ✅ | CP-001 |
| «Sin coincidencias se dice» (§6) | servicio | `hay_algo_indexado` y la orden de consola | ✅ | CP-006 |
| «`RN-3` indexar no modifica, no mueve y no borra» (§4) | servicio | `indexar` solo abre para leer | ✅ | CP-004, retrato de 329 archivos |
| «`RN-4` el texto no se copia a la plataforma» (§4) | servicio | El índice guarda la ruta relativa, no el archivo | ✅ | CP-004 |
| «`RN-2` ninguna credencial entra» (§4) | servicio | Se comprueba con el detector del estándar | ✅ | CP-005 |
| Entidades `Sesión` y `Mensaje` (§5) | modelo | [plataforma/nucleo/medicion/models.py](../../../../../plataforma/nucleo/medicion/models.py) | ✅ | Las 22 pruebas |
| Pantalla (§7) | vista | — | **no aplica** | La §7 permite cerrar `F-033` sin pantalla |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-01 | `historico.turnos`, en el estándar, con 11 pruebas |
| T-02 · T-03 · T-04 · T-06 | El módulo `medicion` completo: modelo, indexar, buscar, rehacer |
| T-05 | `indexar_conversaciones` y `buscar_en_lo_conversado` |
| T-07 · T-08 | Las dos comprobaciones sobre el histórico real |
| T-09 · T-10 · T-11 | Los dos silencios, el tiempo medido, y la §13 de la especificación |
| **Fuera del plan** | `plataforma/nucleo/proyectos/tests.py`: dos pruebas en rojo por la subida de versión de la mañana |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `plataforma/nucleo/medicion/tests.py` | 22 pruebas, en verde |
| `validadores/tests/test_la_transcripcion_se_parte_en_turnos.py` | 11 pruebas, en verde |
| La batería de la plataforma completa | 187 pruebas, en verde |
| La batería interna del estándar | Sin fallas nuevas |

**Lo que las pruebas no dicen:** si una conversación escrita por fuera del enganche existe. No se indexa, y nadie se entera. Está declarado como supuesto en la historia y en la especificación.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Desde `plataforma/`:

```
python manage.py indexar_conversaciones                  # todos los proyectos
python manage.py indexar_conversaciones --proyecto <id>  # uno
python manage.py buscar_en_lo_conversado "lo que sea"
```

**Indexar se vuelve a correr cuando haga falta.** Reemplaza lo que ese proyecto tenía indexado, así que una sesión que creció queda completa y no partida.

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| **El lector de turnos vive en el estándar**, no en la plataforma | Quien escribe el formato es quien sabe leerlo. Copiar las expresiones acá dejaría dos verdades que se separan el día que una marca cambie, y la copia vieja indexaría mal en silencio. Es el molde de `claves.py` |
| El puente revienta si no encuentra el estándar | Cero turnos se lee igual que «esa sesión no tenía nada» |
| El texto no se copia a la plataforma | Excepción declarada a `DA-01` en la §12 de la especificación |
| El retrato compara **huellas**, no fechas | Un programa puede reescribir el mismo texto y dejar la fecha igual |
| Las dos pruebas de Proyectos leen la versión publicada | Un número escrito a mano deja de ser cierto el día que el estándar sube |

Señal registrada: [`S-097`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **La batería de la plataforma no la corre nada del estándar.** `validar.py internas` mira solo `validadores/tests/`, así que una subida de versión la puso en rojo esta mañana y se supo esta tarde, por casualidad. Es `S-097`, y es trabajo de `EP-005·HU-021`, que es la historia de que las pruebas que existen se corran.
- **Sin pantalla**, declarado y permitido por la especificación. Llega con `F-034`.
- **`buscar` es por texto contenido**, sin ordenar por relevancia. Alcanza para lo que la `HU-002` va a contar; si el volumen crece, se mira.

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

| Documento | Qué se le agregó |
|---|---|
| [documentacion/medicion/spec.md](../../../../medicion/spec.md) | Nueva, y su §13 nombra esta fase |
| [documentacion/medicion/README.md](../../../../medicion/README.md) | Nuevo, el índice de la carpeta |
| [documentacion/senales.md](../../../../senales.md) | `S-097` |

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

La plataforma corre en la máquina del usuario. Lo único que hay que hacer al traer este cambio es `python manage.py migrate`, que crea dos tablas nuevas y no toca ninguna existente.
