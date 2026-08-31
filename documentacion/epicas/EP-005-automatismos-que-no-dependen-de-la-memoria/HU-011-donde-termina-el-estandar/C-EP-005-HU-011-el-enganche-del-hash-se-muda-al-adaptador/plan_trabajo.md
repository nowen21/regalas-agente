# Plan de Trabajo — Fase «C-EP-005-HU-011-el-enganche-del-hash-se-muda-al-adaptador» (módulo «Automatismos — enganches»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas` de esta misma fase; lo que quedó hecho, en el `funcionalidad_implementada.md` del cierre.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `C-EP-005-HU-011-el-enganche-del-hash-se-muda-al-adaptador` |
| **Épica** | [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/epica.md](../../epica.md) |
| **HU** | [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-011-donde-termina-el-estandar/HU-011-donde-termina-el-estandar.md](../HU-011-donde-termina-el-estandar.md) — **una sola** (`F12.1`) |
| **Módulo** | Automatismos — enganches |
| **Especificación del módulo** | La HU citada arriba |
| **Fecha apertura** | 2026-08-31 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- 📝 **Modifica fase(s):** retoma el `CA-04` de la propia HU-011, que la fase `A` dejó cumplido y **una fase posterior deshizo sin darse cuenta**: `A-EP-005-HU-019` creó `hook_estacion.py` y lo dejó en `validadores/`, la carpeta de lo agnóstico. La prueba de la frontera lo viene reportando desde entonces.

**CA de la HU que cubre esta fase:**

| CA de `HU-011` que cierra esta fase | Estado |
|---|---|
| [CA-04 — El adaptador vive en un solo sitio, separado de lo agnóstico](../HU-011-donde-termina-el-estandar.md#ca-04--el-adaptador-vive-en-un-solo-sitio-separado-de-lo-agnóstico) | ☐ |

---

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que no quede ninguna pieza de adaptador en la carpeta de lo agnóstico, y que la comprobación que lo vigila **cuente los dos canales por los que un enganche se conecta**.

**Lo que se descubrió al empezar.** La prueba de la frontera compara los enganches que hay en el adaptador contra los que el instalador conecta, y para eso miraba **una sola tabla**: la de la herramienta (`.claude/settings.json`). Pero un enganche se conecta por dos vías, y `hook_estacion.py` va por la otra: lo llama el `post-commit` de git. Mudarlo sin ampliar esa cuenta lo dejaba pareciendo un archivo que nadie usa.

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-04 | Ninguna pieza de adaptador fuera de su carpeta | Funcional | Baja |
| CA-04 | El recuento del amarre no baja por la mudanza | Funcional | Baja |

**Fuera de alcance:**

- Las otras cuatro fallas de la batería interna. Son de `EP-004·HU-008` y van en su propia fase, porque una fase pertenece a una sola historia (`02·F12.1`).

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

### 2.1 Archivos que se crean o modifican

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/hook_estacion.py` → `adaptadores/claude-code/hook_estacion.py` | Mover | Enganche | Con `git mv`, para no perder su historia |
| `adaptadores/claude-code/hook_estacion.py` | Modificar | Enganche | La ruta a `validadores/` sube un nivel más |
| `validadores/instalar.py` | Modificar | Instalador | La plantilla del `post-commit` apunta al sitio nuevo, y se deriva la lista de lo que se conecta por los dos canales |
| `validadores/tests/test_la_frontera_del_adaptador.py` | Modificar | Prueba | Que cuente los dos canales |
| `anatomia/que-esta-amarrado-a-la-herramienta.md` | Modificar | Mapa | Dónde vive ahora |
| `.githooks/post-commit` | Modificar | Enganche de git | Lo reescribe el instalador; no se edita a mano |

### 2.2 Matriz de dependencias del refactor

| Archivo a refactorizar | Cambio de contrato | Archivos que dependen | Dónde rompe |
|---|---|---|---|
| `hook_estacion.py` | Cambia de carpeta | `.githooks/post-commit` | Lo llama por ruta absoluta; lo reescribe el instalador |
| `instalar.py` | Función nueva `enganches_enchufados()` | `test_la_frontera_del_adaptador.py` | Deja de leer la tabla directamente |

### 2.3 Rutas / endpoints y control de acceso · 2.4 Punto de entrada en la UI · 2.5 Permisos

No aplican: ni rutas, ni interfaz, ni permisos.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Ampliar la cuenta de «lo que se conecta» a los dos canales | Dejar `hook_estacion.py` en `validadores/` y exceptuarlo | La carpeta de lo agnóstico no puede tener excepciones, o deja de decir lo que dice |
| La lista se **deriva de las plantillas que se escriben** | Escribirla al lado, a mano | Una lista escrita aparte envejece sin avisar (`S-091`); esta se cae si alguien cambia la plantilla |
| Mover con `git mv` | Copiar y borrar | La historia del archivo es lo que explica por qué está escrito así |

### 2.7 Dudas por resolver antes de codificar

Ninguna abierta.

---

## 3. Desglose de tareas por criterio de aceptación

### [CA-04](../HU-011-donde-termina-el-estandar.md#ca-04--el-adaptador-vive-en-un-solo-sitio-separado-de-lo-agnóstico) — El adaptador vive en un solo sitio

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Mover el enganche con `git mv` y corregir su ruta a `validadores/` | Enganche | 1 h | — | EV-01 |
| T-02 | La plantilla del `post-commit` apunta al sitio nuevo | Instalador | 1 h | T-01 | EV-02 |
| T-03 | `enganches_enchufados()`, derivada de las dos tablas | Instalador | 1 h | T-02 | EV-01 |
| T-04 | La prueba de la frontera cuenta los dos canales | Test | 1 h | T-03 | EV-01 |
| T-05 | Correr el instalador y comprobar el enganche de verdad | Instalador | 1 h | T-02 | EV-02 |
| T-06 | El mapa del amarre dice dónde vive ahora | Mapa | 1 h | T-01 | EV-03 |

**Total estimado:** 6 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-04. T-06 no depende de las demás.

---

## 5. Verificación de criterios de aceptación

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| [CA-04](../HU-011-donde-termina-el-estandar.md#ca-04--el-adaptador-vive-en-un-solo-sitio-separado-de-lo-agnóstico) | Las nueve pruebas de la frontera, y el recuento del amarre antes y después | EV-01, EV-02, EV-03 | | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Las pruebas de la frontera del adaptador | `resultado_pruebas.md` §2 |
| EV-02 | Salida del instalador y el `post-commit` corriendo | `resultado_pruebas.md` §3 |
| EV-03 | El recuento del amarre, antes y después | `resultado_pruebas.md` §2 |

---

## 6. Datos y ambiente de prueba

El propio repositorio. Ningún dato real ([`00·N4`](../../../../../base/00-nucleo-blindado.md)).

---

## 7. Reversión / rollback

Todo está versionado: `git revert` deshace la mudanza, y el instalador reescribe el `post-commit` desde la plantilla.

---

## 8. Producción y migración incremental

**Aditivo para quien hereda.** Un proyecto instalado tiene el `post-commit` apuntando a la ruta vieja; el instalador lo reescribe en la siguiente corrida, y hasta entonces el enganche no corre. No rompe el commit: la línea termina en `|| true`.

---

## 9. Reglas del estándar y del proyecto aplicadas

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F12.1`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md), [`02·F21`](../../../../../base/02-flujo-de-trabajo/reglas/F21-un-incumplimiento-ya-identificado-no-se-repite-en-lo-nuevo.md).
- Proyecto: no aplica.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que la mudanza baje el recuento del amarre y parezca una mejora | Medio | El recuento mira las dos carpetas; se compara antes y después | Cerrado |
| B-02 | Que el `post-commit` quede apuntando a un archivo que no existe y deje de correr en silencio | Alto | Se corre el instalador y se comprueba el enganche de verdad, con un commit | Cerrado |

---

## 11. Definition of Done

- [ ] El CA-04 verificado con evidencia
- [ ] Pruebas de la fase en verde
- [ ] Mapa del amarre al día
- [ ] Señales registradas
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
