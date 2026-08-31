# Plan de Trabajo — Fase «A-EP-011-HU-001-lo-conversado-se-indexa-y-se-busca» (módulo «Medición»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas` de esta misma fase; lo que quedó hecho, en el `funcionalidad_implementada.md` del cierre.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-011-HU-001-lo-conversado-se-indexa-y-se-busca` |
| **Épica** | [documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/epica.md](../../epica.md) |
| **HU** | [documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-001-buscar-en-lo-conversado/HU-001-buscar-en-lo-conversado.md](../HU-001-buscar-en-lo-conversado.md) — **una sola** (`F12.1`) |
| **Módulo** | Medición |
| **Especificación del módulo** | [documentacion/medicion/spec.md](../../../../medicion/spec.md), aprobada el 2026-08-31 |
| **Fecha apertura** | 2026-08-31 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- ✨ **Funcionalidad nueva:** `F-033` del inventario. Es el primer módulo de la versión 2 de la plataforma, y la fuente de `F-034`: sin poder buscar en lo conversado no hay nada que contar.

**CA de la HU que cubre esta fase:**

| CA de `HU-001` que cierra esta fase | Estado |
|---|---|
| [CA-01 — Lo conversado se encuentra por una palabra suya](../HU-001-buscar-en-lo-conversado.md#ca-01--lo-conversado-se-encuentra-por-una-palabra-suya) | ☐ |
| [CA-02 — El índice se puede borrar y rehacer](../HU-001-buscar-en-lo-conversado.md#ca-02--el-índice-se-puede-borrar-y-rehacer) | ☐ |
| [CA-03 — Ninguna credencial queda en lo indexado](../HU-001-buscar-en-lo-conversado.md#ca-03--ninguna-credencial-queda-en-lo-indexado) | ☐ |
| [CA-04 — Indexar no toca el histórico](../HU-001-buscar-en-lo-conversado.md#ca-04--indexar-no-toca-el-histórico) | ☐ |
| Transversal — una búsqueda sin coincidencias lo dice | ☐ |

---

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que lo que ya se conversó se pueda buscar por una palabra suya, sin abrir archivo por archivo, y sin tocar un solo archivo del histórico.

**La línea base, medida.** Sobre este repositorio, que es el primer proyecto conectado:

| Lo medido | Cuánto |
|---|---|
| Archivos de sesión en `historico-chat/` | se cuenta al abrir la fase, y queda en el resultado |
| Formas de buscar hoy | ninguna: se abre archivo por archivo |

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Buscar una palabra y ver en qué mensaje se dijo | Funcional | Media |
| CA-02 | Borrar el índice entero y rehacerlo | Funcional | Baja |
| CA-03 | Ninguna credencial en lo indexado | No funcional · seguridad | Media |
| CA-04 | Indexar no modifica, no mueve y no borra nada | **Que NO pase** | Media |
| Transversal | Sin coincidencias, se dice | Funcional | Baja |

**Fuera de alcance:**

- **Contar y agrupar lo repetido** (`F-034`), que es la `HU-002` de la épica.
- **Pantalla.** La especificación lo permite en su §7: el usuario de `F-033` es el sistema, y el valor para el usuario lo cobra `F-034`. Se entrega con orden de consola.
- Traer conversaciones de otras herramientas.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Lo que ya existe, comprobado contra el código real:**

| Pieza | Dónde | Qué aporta |
|---|---|---|
| El texto de las conversaciones | `historico-chat/` de cada proyecto | Lo escribe [validadores/historico.py](../../../../../validadores/historico.py), con las claves ya tapadas |
| El índice reconstruible | [plataforma/nucleo/almacen/core.py](../../../../../plataforma/nucleo/almacen/core.py) | `reconstruir_indice()` y `huella()` |
| Dónde vive cada proyecto | [plataforma/nucleo/proyectos/models.py](../../../../../plataforma/nucleo/proyectos/models.py) | `ruta_codigo` y `ruta_viva` |
| El puente hacia el estándar | [plataforma/nucleo/seguridad/claves.py](../../../../../plataforma/nucleo/seguridad/claves.py) | El precedente: la plataforma **lee** de `validadores/` y nunca escribe |

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/historico.py` | Modificar | Estándar | Función nueva `turnos(texto)`: quién habló, cuándo y qué dijo. **Quien escribe el formato es quien sabe leerlo** |
| `plataforma/nucleo/medicion/__init__.py` | Nuevo | Módulo | |
| `plataforma/nucleo/medicion/apps.py` | Nuevo | Módulo | |
| `plataforma/nucleo/medicion/models.py` | Nuevo | Modelo | `Sesion` y `Mensaje`, el diccionario de la §5 de la especificación |
| `plataforma/nucleo/medicion/core.py` | Nuevo | Servicio | `indexar`, `reconstruir_indice`, `buscar` |
| `plataforma/nucleo/medicion/conversacion.py` | Nuevo | Servicio | El puente hacia `historico.turnos`, con el mismo molde que `claves.py` |
| `plataforma/nucleo/medicion/management/commands/indexar_conversaciones.py` | Nuevo | Orden | Indexar un proyecto |
| `plataforma/nucleo/medicion/management/commands/buscar_en_lo_conversado.py` | Nuevo | Orden | Buscar |
| `plataforma/nucleo/medicion/migrations/0001_initial.py` | Nuevo | Modelo | Lo genera Django |
| `plataforma/nucleo/medicion/tests.py` | Nuevo | Prueba | Los cinco CA |
| `plataforma/config/settings/base.py` | Modificar | Config | `nucleo.medicion` en la lista de aplicaciones |
| `documentacion/medicion/spec.md` | Modificar | Especificación | Solo su §13, para nombrar la fase que construye `F-033` |

### 2.2 Matriz de dependencias del refactor

| Archivo a refactorizar | Cambio de contrato | Archivos que dependen | Dónde rompe |
|---|---|---|---|
| `validadores/historico.py` | **Función nueva**, no cambia ninguna existente | `brevedad.py`, `hook_historico.py`, `resumen.py` | No rompen: nada de lo que ya existe se toca |

### 2.3 Rutas / endpoints y control de acceso  ·  Q6

No aplica en esta fase: no hay pantalla ni endpoint. Los dos puntos de entrada son órdenes de consola.

### 2.4 Punto de entrada en la UI  ·  Q7

**No aplica, y está declarado.** La §7 de la especificación permite terminar `F-033` sin pantalla: su usuario es el sistema. La pantalla llega con `F-034`.

### 2.5 Permisos / roles a sembrar  ·  Q8

Ninguno. La plataforma corre con un solo usuario.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Leer el formato con una función **del estándar** | Copiar las expresiones que reconocen los turnos dentro de la plataforma | Quien escribe el formato es quien sabe leerlo. Copiarlo deja dos verdades que se separan el día que el enganche cambie una marca, y la copia vieja indexaría mal en silencio. Es el mismo argumento de `claves.py` |
| El puente revienta si no encuentra el estándar | Devolver cero turnos | Cero turnos se lee igual que «esa sesión no tenía nada», y sería un índice vacío que parece completo |
| El índice guarda el texto del mensaje | Guardar solo dónde está | `CA-01` pide ver **en qué mensaje** se dijo |
| Indexar abre los archivos **solo para leer** | Abrirlos con permiso de escritura por comodidad | `CA-04` es el criterio de «que NO pase» de esta historia, y se comprueba comparando la carpeta entera antes y después |
| `reconstruir_indice` borra y relee, sin intentar actualizar lo que cambió | Comparar huellas y actualizar solo lo distinto | Rehacer entero es lo que `CA-02` pide y lo que prueba que la base es prescindible. Actualizar por huella es una mejora de la fase siguiente, si el volumen la pide |

### 2.7 Dudas por resolver antes de codificar

| # | Duda | A quién se consulta | Estado |
|---|---|---|---|
| 1 | Si el texto se copia a la plataforma o se indexa donde vive | usuario | **Resuelta** en la especificación §12: se indexa donde vive, y es una excepción declarada a `DA-01` |
| 2 | Si `F-033` puede cerrarse sin pantalla | usuario | **Resuelta** en la especificación §7: sí |

---

## 3. Desglose de tareas por criterio de aceptación

### [CA-01](../HU-001-buscar-en-lo-conversado.md#ca-01--lo-conversado-se-encuentra-por-una-palabra-suya) — Lo conversado se encuentra por una palabra suya

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-00 | Contar los archivos de sesión de este repositorio: la línea base | Medición | 1 h | — | EV-01 |
| T-01 | `historico.turnos(texto)`: quién, cuándo y qué dijo | Estándar | 2 h | — | EV-02 |
| T-02 | El módulo `medicion` con su modelo `Sesion` y `Mensaje` | Modelo | 2 h | — | EV-03 |
| T-03 | `indexar(proyecto)`: recorre, parte en turnos y guarda | Servicio | 3 h | T-01, T-02 | EV-03 |
| T-04 | `buscar(texto)`: en qué sesión y en qué mensaje | Servicio | 2 h | T-03 | EV-03 |
| T-05 | Las dos órdenes de consola | Orden | 1 h | T-04 | EV-04 |

### [CA-02](../HU-001-buscar-en-lo-conversado.md#ca-02--el-índice-se-puede-borrar-y-rehacer) — El índice se puede borrar y rehacer

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-06 | `reconstruir_indice()`: borra entero y relee | Servicio | 1 h | T-03 | EV-03 |

### [CA-03](../HU-001-buscar-en-lo-conversado.md#ca-03--ninguna-credencial-queda-en-lo-indexado) — Ninguna credencial queda en lo indexado

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-07 | Comprobar lo indexado con el detector de secretos del estándar | Prueba | 2 h | T-03 | EV-05 |

### [CA-04](../HU-001-buscar-en-lo-conversado.md#ca-04--indexar-no-toca-el-histórico) — Indexar no toca el histórico

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-08 | Retrato de la carpeta antes y después, archivo por archivo | Prueba | 2 h | T-03 | EV-06 |

### Transversal y cierre

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-09 | Sin coincidencias se dice, en vez de una lista vacía | Servicio | 1 h | T-04 | EV-03 |
| T-10 | Indexar este repositorio de verdad, y decir cuánto tardó | Medición | 1 h | T-05 | EV-01 |
| T-11 | La §13 de la especificación nombra esta fase | Especificación | 1 h | T-10 | EV-07 |

**Total estimado:** 19 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-00 → T-01 → T-02 → T-03 → T-04 → T-10
**Paralelizables:** T-07 y T-08 cuelgan de T-03 y no entre sí.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| [CA-01](../HU-001-buscar-en-lo-conversado.md#ca-01--lo-conversado-se-encuentra-por-una-palabra-suya) | Buscar una palabra que sí se dijo, en el histórico real | EV-01, EV-03 | | ☐ |
| [CA-02](../HU-001-buscar-en-lo-conversado.md#ca-02--el-índice-se-puede-borrar-y-rehacer) | Borrar el índice y rehacerlo; misma cuenta | EV-03 | | ☐ |
| [CA-03](../HU-001-buscar-en-lo-conversado.md#ca-03--ninguna-credencial-queda-en-lo-indexado) | El detector de secretos sobre lo indexado | EV-05 | | ☐ |
| [CA-04](../HU-001-buscar-en-lo-conversado.md#ca-04--indexar-no-toca-el-histórico) | Retrato de la carpeta antes y después | EV-06 | | ☐ |
| Transversal | Buscar algo que no se dijo nunca | EV-03 | | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | La corrida sobre el histórico real, con su cuenta y su tiempo | `resultado_pruebas.md` §2 |
| EV-02 | Las pruebas de `historico.turnos` | `validadores/tests/` |
| EV-03 | Las pruebas del módulo | `plataforma/nucleo/medicion/tests.py` |
| EV-04 | Las dos órdenes corridas | `resultado_pruebas.md` §3 |
| EV-05 | El detector de secretos sobre lo indexado | `resultado_pruebas.md` §2 |
| EV-06 | El retrato de la carpeta, antes y después | `resultado_pruebas.md` §2 |
| EV-07 | La §13 de la especificación | [documentacion/medicion/spec.md](../../../../medicion/spec.md) |

---

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La plataforma en esta máquina, con su base local. Las pruebas usan carpetas temporales; la corrida final usa el histórico real **solo para leer** |
| Usuarios de prueba | No aplica |
| Datos precargados | Transcripciones de mentiras que la propia prueba escribe, y una clave inventada para el `CA-03` |

**El histórico real no es un dato de prueba**: es la fuente que no se toca ([`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)). Se lee, se mide y se compara antes y después.

---

## 7. Reversión / rollback  ·  Q11

El índice se borra con una orden y no pierde nada: la fuente es el texto. El código está versionado. **La migración es aditiva**: crea dos tablas nuevas y no toca ninguna existente.

---

## 8. Producción y migración incremental  ·  Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

**Aditivo.** Dos tablas nuevas y una aplicación más en la lista. Nada de lo que hay cambia de forma, así que un `migrate` basta y no hace falta backfill: indexar es la primera corrida.

---

## 9. Reglas del estándar y del proyecto aplicadas  ·  Q13

- Base: [`00·N6`](../../../../../base/00-nucleo-blindado.md) (ninguna credencial), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F19`](../../../../../base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md), [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar), [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md).
- Producto: `DA-01` del [cvds/diseno/decisiones-de-arquitectura.md](../../../../../cvds/diseno/decisiones-de-arquitectura.md), con la excepción que la especificación declara en su §12.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que indexar lo acumulado pese demasiado | Medio | Se mide con lo que ya hay, que es volumen real, y el número queda escrito | Abierto hasta T-10 |
| B-02 | Que el puente al estándar se rompa el día que los dos vivan en repositorios distintos | Bajo hoy | Es el mismo riesgo aceptado de `claves.py`, y queda anotado en el mismo sitio | Aceptado |
| B-03 | Que una sesión escrita por fuera del enganche no se indexe y **nadie se entere** | Medio | Está declarado como supuesto en la HU y en la especificación §3. Esta fase no lo resuelve, y lo dice | Declarado |

---

## 11. Definition of Done

- [ ] Los cinco criterios verificados con evidencia (§5)
- [ ] El histórico real indexado, con su cuenta y su tiempo escritos
- [ ] Comprobado que ningún archivo del histórico cambió
- [ ] Pruebas de la fase en verde, y las del estándar sin regresión
- [ ] La §13 de la especificación nombra esta fase
- [ ] Señales registradas
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario  ·  *(opcional — equipo)*

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
