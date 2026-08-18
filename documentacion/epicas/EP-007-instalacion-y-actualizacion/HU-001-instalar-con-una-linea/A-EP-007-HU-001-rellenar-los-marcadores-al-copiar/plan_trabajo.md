# Plan de Trabajo — Fase «A-EP-007-HU-001-rellenar-los-marcadores-al-copiar» (módulo «Instalación»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. Se escribe **antes** de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas` de esta misma fase; lo que quedó hecho, en el `funcionalidad_implementada.md` del cierre.

---

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-007-HU-001-rellenar-los-marcadores-al-copiar` |
| **Épica** | [EP-007 Instalación y actualización](../../epica.md) |
| **HU** | [HU-001 — Instalar con una línea](../HU-001-instalar-con-una-linea.md) — **una sola** (`F12.1`) |
| **Módulo** | Instalación (`validadores/instalar.py`) |
| **Especificación del módulo** | No existe todavía. Esta fase **no la escribe**: se declara como deuda en §10 y se agenda aparte, porque escribirla es trabajo de otra unidad ([`13·DOC6`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-spec-antes-de-tocarlo.md)) |
| **Fecha apertura** | 2026-08-16 |
| **Rama** | `main` — el repositorio del estándar trabaja sobre la principal |

**ORIGEN** (`13·DOC12`):

- 📝 **Modifica fase(s):** ninguna fase previa. Corrige lo que dejó la versión [20.0.1](../../../../../CHANGELOG.md), que cambió cómo las plantillas citan las reglas **sin fase, sin plan y sin pruebas** — el motivo por el que nació [`02·F23`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md).
- ✨ **Funcionalidad nueva:** la prueba de instalación que nunca existió.
- 🔀 **Híbrido:** sí, es de los dos tipos.

**De dónde sale:** [pendiente 40](../../../../../pendientes/hecho/el-instalador-rellena-los-marcadores.md), reportado por el proyecto `shopnest-mesa`.

**CA de la HU que cubre esta fase:**

| CA de `HU-001` que cierra esta fase | Estado |
|---|---|
| [CA-01 — Una línea deja el proyecto listo](../HU-001-instalar-con-una-linea.md#ca-01--una-línea-deja-el-proyecto-listo) | ☐ |
| [CA-02 — Correrla dos veces no rompe nada](../HU-001-instalar-con-una-linea.md#ca-02--correrla-dos-veces-no-rompe-nada) | ☐ |

**Por qué el CA-01 y no otro.** «El proyecto queda con todo lo que debe tener» incluye que lo copiado sirva. Un documento cuyas citas a las reglas no abren no está puesto: está puesto a medias, y hoy la instalación lo declara completo.

---

## 1. Objetivo y alcance

**Objetivo:** que ninguna copia que el instalador escribe en un proyecto conserve un marcador sin llenar, y que una prueba lo compruebe sola de aquí en adelante.

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Instalar deja el proyecto listo, con sus enlaces vivos | Funcional | Baja |
| CA-02 | Reinstalar no rompe ni duplica | Funcional | Baja |

**Fuera de alcance:**

- **Cómo se resuelve el marcador dentro de un proyecto.** Es el [pendiente 41](../../../../../pendientes/hecho/el-marcador-se-resuelve-contra-el-estandar.md) y tiene su propia fase en [EP-004 · HU-005](../../../EP-004-comprobacion-automatica/HU-005-enlaces-y-citas/). Esta fase quita la causa; aquella pone la red.
- **Escribir la especificación del módulo de instalación.** No existe, y escribirla es una unidad aparte (§10).
- **Avisarle a `shopnest-mesa`** que su reporte cerró. Depende del [pendiente 36](../../../../../pendientes/36-falta-la-regla-que-obliga-a-reportar-lo-que-es-del-estandar.md), que todavía no fija el procedimiento.
- **Que la ruta escrita sea la de la máquina donde se instaló.** Ya está declarado como límite conocido en la [20.0.1](../../../../../CHANGELOG.md) y no empeora con este cambio.

---

## 2. Análisis previo — línea base verificada

### 2.1 Archivos que se crean o modifican

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/instalar.py` | Modificar | Instalación | Tres funciones de copia; ver §2.2 |
| `validadores/tests/test_instalar_marcadores.py` | Nuevo | Test | La prueba que faltó |
| `validadores/docs/instalar.md` | Modificar | Documentación | Dice qué hace cada función; hoy no menciona que tres no rellenan |
| `CHANGELOG.md` | Modificar | Versionado | Entrada de la versión |
| `VERSION` | Modificar | Versionado | Sube el número |

**Verificado el 2026-08-16** contra el repositorio: las tres funciones existen con esas líneas, y `_rellenar` y `_rellenos` están definidas en el mismo archivo.

### 2.2 Matriz de dependencias del refactor

No cambia ningún contrato: las tres funciones conservan su firma `(ruta, aplicar)` y su valor de retorno. Lo que cambia es el **contenido** de lo que escriben.

| Función | Qué hace hoy | Qué escribirá | Quién depende |
|---|---|---|---|
| `instalar_stack` (línea 333) | `leer(original) + sello` | el mismo texto con los marcadores llenos | `checklist.huella_instalada()`, que lee el sello — **no se toca** |
| `instalar_recuerdos` (línea 434) | `_escribir_sellado(archivo, leer(PLANTILLA_MEMORIA), …)` | ídem, con el texto relleno | `recuerdos.indice_presente()` |
| `instalar_agente_config` (línea 708) | `f.write(leer(origen))` | ídem, con el texto relleno | nadie lee su contenido; los llena el proyecto |

**El sello no se ve afectado.** La huella se calcula del stack central ([`checklist.py` · `huella()`](../../../../../validadores/checklist.py)), no del texto del archivo copiado. Verificado leyendo la función: llama a `versiones.huella_central(_STACK, estandar)`.

### 2.3 Rutas / endpoints y control de acceso

No aplica: es un programa de línea de comandos, sin rutas ni permisos.

### 2.4 Punto de entrada en la interfaz

No aplica porque la fase no introduce navegación. Lo que cambia se ve al correr la instalación y al abrir un enlace de los archivos copiados.

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Rellenar en cada una de las tres funciones | Un solo envoltorio de escritura por el que pasen todas | El envoltorio es mejor diseño y es un refactor más grande; se declara como deuda (§10) en vez de meterlo en la fase que arregla un P0 |
| Comprobar la ausencia de `«…»` con la marca de [`13·DOC19`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md) | Buscar `«RUTA-ESTANDAR»` y nada más | La regla ya fija una sola marca para todos los huecos; buscarla entera atrapa también los que se agreguen mañana |
| La prueba instala en una carpeta temporal | Instalar en un proyecto real de la máquina | [`00·N4`](«RUTA-ESTANDAR»/base/00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada) y [`08·T4`](«RUTA-ESTANDAR»/base/08-pruebas.md#t4--protege-los-datos-reales-al-probar): nunca se prueba contra lo real |

### 2.7 Dudas por resolver antes de codificar

| # | Duda | A quién se consulta | Estado |
|---|---|---|---|
| 1 | Un proyecto ya instalado, ¿se pone al día reinstalando o hay que decirle algo más? | usuario | Pendiente — la respuesta va en el `CHANGELOG` (T-07) |

---

## 3. Desglose de tareas por criterio de aceptación

### [CA-01](../HU-001-instalar-con-una-linea.md#ca-01--una-línea-deja-el-proyecto-listo) — Una línea deja el proyecto listo

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Pasar `instalar_stack` por `_rellenar(…, _rellenos(ruta))` | Instalación | 0,5 h | — | EV-01 |
| T-02 | Ídem en `instalar_recuerdos` | Instalación | 0,5 h | — | EV-01 |
| T-03 | Ídem en `instalar_agente_config` | Instalación | 0,5 h | — | EV-01 |
| T-04 | Escribir la prueba: instalar en carpeta temporal y comprobar que ningún archivo copiado conserva `«…»` | Test | 2 h | T-01, T-02, T-03 | EV-01 |
| T-05 | Actualizar `validadores/docs/instalar.md` con qué rellena cada función | Documentación | 0,5 h | T-03 | EV-03 |

### [CA-02](../HU-001-instalar-con-una-linea.md#ca-02--correrla-dos-veces-no-rompe-nada) — Correrla dos veces no rompe nada

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-06 | Agregar a la prueba una segunda corrida y comparar el antes y el después | Test | 1 h | T-04 | EV-02 |

### Cierre de la fase

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-07 | Entrada en `CHANGELOG.md` y subir `VERSION`, con qué hacer para quedar al día | Versionado | 0,5 h | T-06 | — |

**Total estimado:** 5,5 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-04 → T-06 → T-07
**Paralelizables:** T-01, T-02 y T-03 son independientes entre sí. T-05 puede ir en cualquier momento después de T-03.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)). Descubrir uno nuevo → PAUSAR, reportar, ampliar el plan con OK.

---

## 5. Verificación de criterios de aceptación

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| [CA-01](../HU-001-instalar-con-una-linea.md#ca-01--una-línea-deja-el-proyecto-listo) | Prueba automática sobre carpeta temporal + apertura manual de un enlace | EV-01, EV-03 | | ☐ |
| [CA-02](../HU-001-instalar-con-una-linea.md#ca-02--correrla-dos-veces-no-rompe-nada) | Segunda corrida y comparación | EV-02 | | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de la prueba | `resultado_pruebas.md` de esta fase |
| EV-02 | Comparación antes/después de la segunda corrida | `resultado_pruebas.md` de esta fase |
| EV-03 | Verificación manual: abrir un enlace del `.agente/stack-instalacion.md` instalado | `resultado_pruebas.md` de esta fase |

---

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | Carpeta temporal desechable, creada y borrada por la prueba. Nunca un proyecto real ([`00·N4`](«RUTA-ESTANDAR»/base/00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada)) |
| Usuarios de prueba | No aplica |
| Datos precargados | Ninguno: la carpeta arranca vacía, que es el caso del CA-01 |

---

## 7. Reversión / rollback

El cambio es de tres líneas y no toca datos. Se revierte volviendo el commit atrás. Un proyecto ya instalado con marcadores crudos no empeora: reinstalar los rellena, y si se revierte vuelve a quedar como está hoy.

---

## 8. Producción y migración incremental

**Sí toca algo que está en producción:** los proyectos ya instalados tienen los archivos copiados con el marcador crudo. El cambio es **aditivo** y se aplica al reinstalar, que es lo que cada proyecto hace al abrir sesión ([`01·C18`](«RUTA-ESTANDAR»/base/01-conducta.md#c18--auto-sincronización-del-claudemd-con-la-plantilla-central)).

Cuidado con uno: los cuatro archivos de `.agente/` **no se pisan** una vez creados, porque los llena el proyecto. Un proyecto que ya los tenga con el marcador crudo **no se arregla solo**. Eso se declara en el `CHANGELOG` (T-07) y, si hace falta más, se agenda aparte.

---

## 9. Reglas del estándar y del proyecto aplicadas

- Base: [`02·F23`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md) (por qué esta fase existe), [`02·F4`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F14`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md), [`02·F17`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T4`](«RUTA-ESTANDAR»/base/08-pruebas.md#t4--protege-los-datos-reales-al-probar), [`13·DOC19`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md), [`13·DOC20`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC20-no-entregues-como-terminado-un-documento-con-marcas.md), [`20·M10`](«RUTA-ESTANDAR»/base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).
- Proyecto: el `CLAUDE.md` de este repositorio, §2 y §4.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Los 4 archivos de `.agente/` no se pisan, así que un proyecto viejo no se arregla solo | Queda un enlace muerto en proyectos ya instalados | Declararlo en el `CHANGELOG`; si hace falta arreglarlo, es fase aparte | Abierto |
| B-02 | El módulo de instalación no tiene especificación | La fase toca código sin documento que diga qué debe hacer | Se declara como deuda y se agenda; no se escribe acá | Abierto |
| B-03 | Que rellenar rompa la comparación de huella | La instalación se declararía desactualizada siempre | Verificado que no: la huella sale del stack central, no del texto | Cerrado |

---

## 11. Definition of Done

- [ ] Los dos CA de §0 verificados con evidencia (§5)
- [ ] La prueba corre sola y falla si vuelve a aparecer un `«…»`
- [ ] `validadores/docs/instalar.md` dice qué rellena cada función
- [ ] Entrada en `CHANGELOG.md` y `VERSION` subida
- [ ] Rama lista para el commit único de la fase
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica: el trabajo lo lleva una sola persona y el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md` de esta fase. Este plan se queda como se aprobó, para poder comparar lo que se dijo contra lo que pasó.
