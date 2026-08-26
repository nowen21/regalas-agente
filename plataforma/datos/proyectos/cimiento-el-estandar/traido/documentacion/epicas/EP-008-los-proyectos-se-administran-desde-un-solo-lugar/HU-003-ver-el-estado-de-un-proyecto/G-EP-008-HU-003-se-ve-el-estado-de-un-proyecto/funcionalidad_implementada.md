# Funcionalidad implementada — Fase G-EP-008-HU-003-se-ve-el-estado-de-un-proyecto (módulo Proyectos)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `G-EP-008-HU-003-se-ve-el-estado-de-un-proyecto` |
| **Módulo** | Proyectos |
| **Especificación del módulo** | [documentacion/proyectos/spec.md](../../../../proyectos/spec.md), §6 · `02·F2` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-25 |
| **HU / CA cubiertas** | [HU-003](../HU-003-ver-el-estado-de-un-proyecto.md): `CA-01`, `CA-02`, `CA-03`. Los tres, y con esto la historia queda cerrada |
| **Fecha de cierre** | 2026-08-25 |
| **Versión del estándar al cerrar** | 34.1.0 |
| **Commit** | `faed710` |

---

## 1. Qué se implementó — resumen

La plataforma ya dice en qué va cada proyecto **sin abrir su carpeta**: qué etapas del ciclo tienen documento y cuáles faltan, cuántas fases hay y cuántas siguen abiertas, y cuántos documentos están aprobados y desde cuándo.

**Lo que no se puede leer se dice, no se supone.** Cinco de las 127 fases de este repositorio escriben su estación de una forma que no se deja leer, y quedan fuera de las dos cuentas, nombradas con su ruta.

**El estado de este repositorio, calculado por primera vez:** 7 de 7 etapas con documento, **41 de 127 fases todavía abiertas**, 228 de 994 documentos aprobados.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| "Se lee lo que la plataforma guardó de ese proyecto" (§6) | servicio | [nucleo/proyectos/estado.py](../../../../../plataforma/nucleo/proyectos/estado.py) | ✅ | CP-009 |
| "Qué etapas tienen documento" (§6) | servicio | `etapas_con_documento` y `etapas_sin_documento` | ✅ | CP-002 |
| "Qué fases están abiertas" (§6) | servicio | `_esta_abierta` en [estado.py](../../../../../plataforma/nucleo/proyectos/estado.py) | ✅ | CP-003, CP-004 |
| "Qué falta aprobar" (§6) | servicio | `_esta_aprobado` y `aprobados` | ✅ | CP-005 |
| "Un proyecto sin nada escrito responde «sin empezar», que es un dato" (§6) | servicio · vista | `que_haria_falta` | ✅ | CP-006 |
| "El estado se calcula al pedirlo, y se guarda solo como índice" (§12) | modelo | `Proyecto.estado` delega en el cálculo; no hay campo | ✅ | Es una propiedad, no un campo |
| "`RN-2` la ruta viva y el estado se calculan, no se guardan" (§4) | modelo | Lo mismo | ✅ | CP-009 |
| "Cambiar el estado desde la plataforma" | — | — | N/A | Versión 5 |
| "Abrir un documento traído para leerlo" | — | — | N/A | Versión 2, con `F-014` |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| 1 | Corregir el hueco de la fase E: `cvds/` entra, con sus moldes | ✅ hecha | [nucleo/importacion/moldes.py](../../../../../plataforma/nucleo/importacion/moldes.py) y `mirar` en su `core.py` | CP-001 |
| 2 | Calcular qué etapas tienen documento | ✅ hecha | [estado.py](../../../../../plataforma/nucleo/proyectos/estado.py) | CP-002 |
| 3 | Calcular qué fases hay y en qué estación van | ✅ hecha | `_esta_abierta` | CP-003, CP-004 |
| 4 | Calcular qué está aprobado y desde cuándo | ✅ hecha | `_esta_aprobado`, `_fecha_de_aprobacion` | CP-005 |
| 5 | Que un proyecto sin nada diga qué haría falta | ✅ hecha | `que_haria_falta` | CP-006 |
| 6 | Mostrarlo en la pantalla, con palabras | ✅ hecha | `templates/proyectos/uno.html` | CP-005, CP-007 |
| 7 | Medir cincuenta proyectos con estado | ✅ hecha | `RendimientoDelEstadoTests` | CP-008: **0,278 s** |

**Correspondencia con el plan:** 7 tareas en el plan, 7 acá.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno. `nucleo/importacion/` es de otro módulo y quedó declarado en el plan §2.1 antes de tocarlo, con su razón.

**Esfuerzo real contra estimado:** el plan no estimó horas.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Qué | Resultado |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | Cumple |
| **Suites ejecutadas** | `python manage.py test nucleo`, 145 de 145 verdes |
| **Defectos abiertos que se aceptaron** | Ninguno |

**Verificaciones manuales** (`08·T4`):

| # | Qué se verificó | Resultado |
|---|---|---|
| 1 | Que las pruebas cacen lo que dicen cazar | Siete sabotajes, los siete cazados a la primera |
| 2 | Que el estado del repositorio real sea correcto | 7 de 7 etapas, 127 fases, 41 abiertas, 228 aprobados |
| 3 | Que las cinco fases ilegibles sean reales | Nombradas una por una, con su ruta |
| 4 | Que el estado no dependa del proyecto | Con la ruta apuntando a una carpeta inexistente, idéntico |
| 5 | Que los datos de prueba no quedaran | Los tres índices en cero |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

En la pantalla de un proyecto, la sección **En qué va** muestra el estado. Un proyecto sin nada traído muestra «Sin empezar» y qué haría falta para arrancar.

- **Desde el código:** `proyecto.estado` da el resumen en una palabra; `proyecto.detalle_del_estado` da el objeto completo, con etapas, fases, ilegibles y aprobaciones.
- **De dónde sale:** de lo traído, en `datos/proyectos/<identificador>/traido/`. Nunca de la carpeta del proyecto.

---

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| El estado se calcula desde lo traído, nunca leyendo el proyecto | `CA-01` lo pide, y hay una razón práctica: un proyecto entregado o archivado tiene que seguir mostrando su estado | [estado.py](../../../../../plataforma/nucleo/proyectos/estado.py), y `CP-009` que lo comprueba borrando la carpeta |
| Una estación que no se deja leer queda **fuera de las dos cuentas** | Sumarla a las abiertas o a las cerradas sería afirmar sobre lo que no se leyó. Con las cinco reales, la diferencia es 41 abiertas contra 46 inventadas | `_esta_abierta` devuelve **dos** valores: si está abierta, y si se pudo saber |
| Se busca el número que abre la línea, no la línea entera | Hay doce formas distintas de escribirla, y el número es lo único que se escribe siempre igual. Va a haber una decimotercera | El comentario junto a la expresión, en `estado.py` |
| El `README.md` de una carpeta de etapa es el documento de esa etapa | El nombre solo no alcanza: dos archivos que se llaman igual son documentos distintos según dónde están | `tipo_de` recibe la ruta, no solo el nombre |
| Las etapas que **faltan** también se dicen | Un estado que solo lista lo que hay no deja ver qué falta, que es para lo que se mira | `etapas_sin_documento` |
| Lo que le falta a un proyecto sin nada **depende del caso** | Decirle «traiga su documentación» a alguien cuya carpeta no está es un consejo inútil: primero hay que arreglar la ruta | `que_haria_falta` |
| Se dice con palabras, no con color | Un color no se lee en voz alta ni lo distingue quien no ve los colores. `CA-03` lo exige | La plantilla, y `CP-005` que busca las palabras |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino |
|---|---|---|
| **Cinco fases de este repositorio escriben su estación de una forma ilegible.** La plataforma las nombra, y corregirlas es del usuario | No previsto | Las cinco están nombradas en [EV-03](evidencias/EV-03-corrida-real.txt). Corregirlas es trabajo del repositorio, no de la plataforma |
| `cvds/cumplimiento.md` no tiene molde en el estándar, y por eso no entra | No previsto | Es correcto que se reporte. Si ese documento se vuelve común, el estándar tendrá que darle molde |
| Calcular el estado lee cada documento traído para buscar su marca de aprobación. Con 994 documentos tarda 14 s la primera vez | No previsto | La lista de proyectos tarda 0,278 s porque son proyectos pequeños. Con uno de mil documentos por proyecto habría que guardar la marca al traer, no al mirar |
| Las doce formas de escribir la estación son del repositorio, no del estándar | Diferido por el plan | Si el estándar fijara una sola forma, esto se simplifica solo |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] Mapa de dependencias: Proyectos ahora lee lo que Importación trajo. Es una dependencia nueva, y va en ese sentido.
- [x] Catálogo de módulos: los dos ya están registrados.
- [x] Índice de la carpeta de la fase: [README.md](README.md).
- [x] Especificación del módulo: ya describía este comportamiento en su §6. No hizo falta tocarla.
- [x] **El defecto de la fase E quedó anotado en su documento de cierre**, con su fecha y dónde se corrigió.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

- **Migraciones a correr:** ninguna. El estado no se guarda.
- **Qué cambia para quien ya tenía la plataforma:** la pantalla de cada proyecto muestra su estado. Y **lo traído antes de esta fase no incluye las etapas del ciclo**: hay que volver a traer, que no duplica y actualiza lo que cambió.
- **Reversión:** se descarta la rama de la fase. El estado no se guarda, así que no deja datos que limpiar.
