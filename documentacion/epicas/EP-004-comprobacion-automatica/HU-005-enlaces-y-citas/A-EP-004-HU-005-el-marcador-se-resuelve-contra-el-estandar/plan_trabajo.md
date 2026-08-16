# Plan de Trabajo — Fase «A-EP-004-HU-005-el-marcador-se-resuelve-contra-el-estandar» (módulo «Comprobación»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. Se escribe **antes** de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas` de esta misma fase; lo que quedó hecho, en el `funcionalidad_implementada.md` del cierre.

---

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-004-HU-005-el-marcador-se-resuelve-contra-el-estandar` |
| **Épica** | [EP-004 Comprobación automática](../../epica.md) |
| **HU** | [HU-005 — Comprobar los enlaces y las citas a reglas](../HU-005-enlaces-y-citas.md) — **una sola** (`F12.1`) |
| **Módulo** | Comprobación (`validadores/enlaces.py`) |
| **Especificación del módulo** | No existe todavía. Esta fase **no la escribe**: se declara como deuda en §10, igual que la fase hermana de EP-007 |
| **Fecha apertura** | 2026-08-16 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- 📝 **Modifica fase(s):** ninguna fase previa. Corrige lo que dejó la versión [20.0.1](../../../../../CHANGELOG.md), que le enseñó el marcador a `enlaces.py` **sin fase ni pruebas**, resolviéndolo contra una raíz que solo es correcta cuando se corre sobre el propio estándar.
- ✨ **Funcionalidad nueva:** el caso de prueba que fija que el veredicto no depende de desde dónde se corra.
- 🔀 **Híbrido:** sí.

**De dónde sale:** [pendiente 41](../../../../../pendientes/41-el-marcador-no-se-resuelve-dentro-de-un-proyecto.md), destapado al revisar lo que reportó `shopnest-mesa`.

**CA de la HU que cubre esta fase:**

| CA de `HU-005` que cierra esta fase | Estado |
|---|---|
| [CA-01 — Un enlace roto se reporta](../HU-005-enlaces-y-citas.md#ca-01--un-enlace-roto-se-reporta) | ☐ |

**Por qué solo el CA-01.** Los otros tres criterios de la HU (índices, citas a reglas, cruces) ya están construidos y en verde; esta fase corrige **cómo se resuelve un destino** antes de decidir si el enlace está roto, que es exactamente lo que el CA-01 exige. Los demás no se tocan y quedan cubiertos por la no regresión.

---

## 1. Objetivo y alcance

**Objetivo:** que un enlace escrito con el marcador dé el mismo veredicto se corra desde donde se corra, y que una prueba lo fije.

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Un enlace roto se reporta, y uno bueno no | Funcional | Baja |

**Fuera de alcance:**

- **Que el marcador salga sin rellenar del instalador.** Es el [pendiente 40](../../../../../pendientes/40-el-instalador-copia-sin-rellenar-los-marcadores.md), con su propia fase en [EP-007 · HU-001](../../../EP-007-instalacion-y-actualizacion/HU-001-instalar-con-una-linea/A-EP-007-HU-001-rellenar-los-marcadores-al-copiar/). Aquella quita la causa; esta pone la red.
- **Que `enlaces.py` no tenga bloque `__main__`** y corriéndolo directo no imprima nada. Se vio de paso, está anotado en el [pendiente 41](../../../../../pendientes/41-el-marcador-no-se-resuelve-dentro-de-un-proyecto.md) y **no entra**: es otro defecto, de otra HU (la corrida completa, [HU-008](../../HU-008-corrida-completa/)).
- **Comprobar el ancla del enlace.** Ya está fuera de alcance en la propia HU-005.

---

## 2. Análisis previo — línea base verificada

### 2.1 Archivos que se crean o modifican

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/enlaces.py` | Modificar | Comprobación | La rama del marcador, en `validar_enlaces()` |
| `validadores/tests/test_enlaces_marcador.py` | Nuevo | Test | Los dos casos de §3 |
| `validadores/docs/enlaces.md` | Modificar | Documentación | Explica contra qué se resuelve el marcador |
| `CHANGELOG.md` | Modificar | Versionado | Entrada de la versión |
| `VERSION` | Modificar | Versionado | Sube el número |

**Verificado el 2026-08-16** contra el repositorio: la rama existe en `validar_enlaces()` y el módulo ya conoce su propia raíz, así que no hay que calcularla de nuevo.

### 2.2 Matriz de dependencias del refactor

No cambia ningún contrato: `validar_enlaces(raiz)` conserva su firma y su tipo de retorno. Cambia **contra qué carpeta** se resuelve un destino que empieza con el marcador.

| Archivo a cambiar | Cambio | Quién depende | Dónde podría romper |
|---|---|---|---|
| `validadores/enlaces.py` | El marcador deja de resolverse contra la raíz validada | `validar.py estandar`, `hook_md.py` | Solo si algún `.md` del estándar dependía de que las dos carpetas fueran la misma — y lo son cuando se corre acá, así que el resultado no cambia |

**Comprobación previa obligatoria (T-01):** correr `validar.py estandar` **antes** del cambio y guardar la salida. Es la línea base contra la que se compara después. Sin ella, "no cambió nada" es una afirmación sin respaldo.

### 2.3 Rutas / endpoints y control de acceso

No aplica.

### 2.4 Punto de entrada en la interfaz

No aplica porque la fase no introduce navegación. Lo que cambia se ve en la salida de la comprobación.

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El marcador se resuelve contra la carpeta del estándar | Que el proyecto pase la ruta del estándar por parámetro | El módulo ya sabe dónde vive; pedir el dato por fuera agrega una forma más de equivocarse |
| Se conserva la rama del marcador en vez de quitarla | Quitarla, ya que el pendiente 40 hará que no lleguen marcadores | Es la red de seguridad: el día que se escape uno, el veredicto tiene que seguir siendo correcto |

### 2.7 Dudas por resolver antes de codificar

Ninguna abierta.

---

## 3. Desglose de tareas por criterio de aceptación

### [CA-01](../HU-005-enlaces-y-citas.md#ca-01--un-enlace-roto-se-reporta) — Un enlace roto se reporta

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Guardar la salida de `validar.py estandar` **antes** del cambio | Test | 0,25 h | — | EV-01 |
| T-02 | Resolver el marcador contra la carpeta del estándar | Comprobación | 0,5 h | T-01 | EV-02 |
| T-03 | Prueba: el mismo `.md` con el mismo marcador da el mismo veredicto con `--raiz` sobre el estándar y sobre una carpeta ajena | Test | 1,5 h | T-02 | EV-02 |
| T-04 | Prueba: un marcador que apunta a una regla que no existe se sigue reportando | Test | 0,5 h | T-02 | EV-03 |
| T-05 | Comparar la salida de hoy contra la de T-01 | Test | 0,25 h | T-02 | EV-01 |
| T-06 | Actualizar `validadores/docs/enlaces.md` | Documentación | 0,5 h | T-02 | — |

### Cierre de la fase

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-07 | Entrada en `CHANGELOG.md` y subir `VERSION` | Versionado | 0,25 h | T-05 | — |

**Total estimado:** 3,75 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-05 → T-07
**Paralelizables:** T-04 y T-06 después de T-02.

**T-01 va primero y no se salta.** Es lo único que permite afirmar que acá no cambió nada.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| [CA-01](../HU-005-enlaces-y-citas.md#ca-01--un-enlace-roto-se-reporta) | Prueba automática desde dos raíces + comparación con la línea base | EV-01, EV-02, EV-03 | | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de `validar.py estandar` antes y después | `resultado_pruebas.md` de esta fase |
| EV-02 | Salida de la prueba de las dos raíces | `resultado_pruebas.md` de esta fase |
| EV-03 | Salida de la prueba del marcador que no resuelve | `resultado_pruebas.md` de esta fase |

---

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | Carpetas temporales desechables. Nunca un proyecto real ([`00·N4`](«RUTA-ESTANDAR»/base/00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada)) |
| Usuarios de prueba | No aplica |
| Datos precargados | Un `.md` de mentira con dos enlaces: uno con marcador que resuelve y otro que no |

---

## 7. Reversión / rollback

Es un cambio de una línea, sin datos de por medio. Se revierte volviendo el commit atrás.

---

## 8. Producción y migración incremental

**No toca datos ni esquemas.** Sí cambia el veredicto que un proyecto ya instalado recibe al correr la comprobación: un enlace con marcador que hoy se reporta roto pasará a resolver bien. Eso es la corrección, no una regresión, y se declara en el `CHANGELOG`.

No hace falta migrar nada: los proyectos corren el programa desde la carpeta del estándar, no una copia ([`instalar.py`](../../../../../validadores/instalar.py), donde el enganche se escribe con la ruta absoluta).

---

## 9. Reglas del estándar y del proyecto aplicadas

- Base: [`02·F23`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), [`02·F4`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F11`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F11-una-fase-solo-modifica-codigo-de-su-propio-modulo.md), [`02·F14`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md), [`02·F17`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`02·F20`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md) (el bloque `__main__` se propone, no se arregla de paso), [`08·T4`](«RUTA-ESTANDAR»/base/08-pruebas.md#t4--protege-los-datos-reales-al-probar), [`20·M10`](«RUTA-ESTANDAR»/base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).
- Proyecto: el `CLAUDE.md` de este repositorio, §2 y §4.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que el cambio altere el veredicto dentro del propio estándar sin que nadie lo note | Se rompería la comprobación que más se corre | T-01 y T-05: comparar la salida antes y después | Abierto |
| B-02 | El módulo de comprobación no tiene especificación | Se toca código sin documento que diga qué debe hacer | Se declara como deuda y se agenda | Abierto |
| B-03 | Que `enlaces.py` sin bloque `__main__` haga leer como "sin hallazgos" un resultado que nadie calculó | Se dan por buenas comprobaciones que no corrieron | Fuera de alcance; anotado en el pendiente 41 para su propia HU | Abierto |

---

## 11. Definition of Done

- [ ] El CA-01 verificado con evidencia (§5)
- [ ] La salida de `validar.py estandar` es la misma antes y después
- [ ] La prueba de las dos raíces corre sola
- [ ] `validadores/docs/enlaces.md` dice contra qué se resuelve el marcador
- [ ] Entrada en `CHANGELOG.md` y `VERSION` subida
- [ ] Rama lista para el commit único de la fase
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md` de esta fase.
