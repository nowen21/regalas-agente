# Plan de Trabajo — Fase A-EP-003-HU-001-marca-de-espacio-por-llenar (módulo Documentos modelo)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en [HU-001](../HU-001-marca-de-espacio-por-llenar.md); el detalle de las pruebas, en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase; lo que dieron al correrlas, en el [resultado_pruebas.md](resultado_pruebas.md); lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-003-HU-001-marca-de-espacio-por-llenar` |
| **Épica** | [EP-003](../../epica.md) |
| **HU** | [HU-001 Definir cómo se marca un espacio por llenar en un modelo](../HU-001-marca-de-espacio-por-llenar.md) |
| **Módulo** | Documentos modelo |
| **Especificación del módulo** | [documentacion/documentos-modelo/spec.md](../../../../documentos-modelo/spec.md). Sí la lleva aparte, por decisión del usuario del 2026-08-14: `02·F2` se cumple y no lleva excepción. Eso cierra la duda que arrastraban las fases `A-EP-001-HU-001-molde-de-regla` y `A-EP-004-HU-010-declaracion-y-comprobacion`, que se habían abierto declarando que no la necesitaban |
| **Fecha apertura** | 2026-08-14 |
| **Rama** | `feature/A-EP-003-HU-001-marca-de-espacio-por-llenar` |

**ORIGEN** (`DOC12`): ✨ **Funcionalidad nueva.** Es la primera historia de EP-003 y la primera de la cadena que abre el hallazgo [H-4 del 2026-08-14](../../../../../historico-chat/resumenes/2026-08-14/hu-de-la-comprobacion-automatica.md): el resumen de sesión no tiene dónde escribirse. Esa cadena es EP-003 · HU-001 → EP-003 · HU-009 → EP-005 · HU-008, y HU-009 declara esta historia como dependencia de impacto alto.

**Por qué una sola fase para los tres CA.** Los tres se apoyan en la misma decisión (cuál es la marca), y ninguno se puede probar sin ella. Partirlos daría dos fases esperando a la primera, que es lo que `02·F12.10` manda evitar.

**CA de la HU que cubre esta fase** (una sola HU · `02·F12.1` · trazabilidad `DOC11`)

| CA de HU-001 | Qué valida | Estado |
|---|---|---|
| [CA-01](../HU-001-marca-de-espacio-por-llenar.md#ca-01--la-marca-se-ve-y-se-distingue-del-texto) | La marca se ve y se distingue del texto | Cumple |
| [CA-02](../HU-001-marca-de-espacio-por-llenar.md#ca-02--todos-los-modelos-usan-la-misma-marca) | Todos los modelos usan la misma marca | Cumple |
| [CA-03](../HU-001-marca-de-espacio-por-llenar.md#ca-03--un-documento-con-marcas-sin-llenar-no-se-da-por-terminado) | Un documento con marcas sin llenar no se da por terminado | Cumple |

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** dejar escrita una sola marca para el espacio por llenar, con el porqué de esa y no otra, aplicada a todas las plantillas del estándar, y con la condición de "documento terminado" definida de forma objetiva.

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| [CA-01](../HU-001-marca-de-espacio-por-llenar.md#ca-01--la-marca-se-ve-y-se-distingue-del-texto) | La marca se distingue del texto del modelo al leerlo | Funcional | Baja |
| [CA-02](../HU-001-marca-de-espacio-por-llenar.md#ca-02--todos-los-modelos-usan-la-misma-marca) | Las 30 plantillas usan la misma marca y ninguna usa otra | Funcional | Media |
| [CA-03](../HU-001-marca-de-espacio-por-llenar.md#ca-03--un-documento-con-marcas-sin-llenar-no-se-da-por-terminado) | Un documento con marcas sin reemplazar no está terminado | Funcional | Baja |
| [RNF-01](../HU-001-marca-de-espacio-por-llenar.md#5-requisitos-no-funcionales) | La marca no estorba la lectura del modelo | No funcional | Baja |
| [RNF-02](../HU-001-marca-de-espacio-por-llenar.md#5-requisitos-no-funcionales) | Un programa la encuentra sin falsos positivos | No funcional | Media |
| [RNF-03](../HU-001-marca-de-espacio-por-llenar.md#5-requisitos-no-funcionales) | Una sola marca en todo el catálogo | No funcional | Media |

**Fuera de alcance** (qué explícitamente NO entra en esta fase):

- **El programa que cuenta las marcas.** Es de EP-004, y así lo dice la propia HU en su §3.3.
- **Los modelos en sí.** Esta fase toca la marca de los que ya existen; no escribe modelos nuevos ni les cambia el contenido.
- **Los documentos ya llenados** en `documentacion/`, `historico-chat/` y `pendientes/`. Son documentos terminados, no modelos.
- **El modelo del resumen de sesión.** Es HU-009, la siguiente de la cadena.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado contra el repositorio el 2026-08-14, contando las marcas archivo por archivo en `plantillas/`.
>
> **Ampliación aprobada el 2026-08-14**, antes de escribir la primera línea. Dos cosas que el plan original daba por ciertas y no lo eran:
>
> 1. **La ruta del capítulo 13.** Decía `base/13-documentacion.md`, y el capítulo es una carpeta: `base.md` con el índice y un archivo por regla en `reglas/`.
> 2. **No es una regla, son tres.** La fila 9 del [checklist del estándar](../../../../../base/20-meta-reglas/checklist.md) reprueba el "y además", y su prueba es si las partes se cumplen por separado. Acá se cumplen: se puede usar la marca y entregar igual con marcas sin llenar, y se pueden hacer las dos cosas sin escribir `N/A` donde no aplica.
>
> **Segunda ampliación, aprobada el mismo día.** La línea base contaba mal: contó archivos que **tienen alguna** `«…»`, no archivos convertidos por completo. Once plantillas usan las dos marcas a la vez, con unos 179 huecos en corchetes. Son 11 archivos por convertir, no 2, y así lo declara §2.1.
>
> El aviso salió las dos veces de [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md): parar y reportar en vez de editar por iniciativa.

**Qué hay hoy.** La marca `«…»` no está escrita en ninguna regla, pero se usa de hecho en **25 de los 30 archivos** de `plantillas/`. Los otros cinco no la usan, y tres de ellos tienen huecos marcados de otra forma:

| Archivo | Marca que usa hoy | Qué hay que hacer |
|---|---|---|
| `plantillas/epica.md` | `[Resultado observable a nivel de negocio]`, `<slug>` | Pasar a la marca acordada |
| `plantillas/marco-normativo.md` | `` `<nombre>` ``, `` `<lo que exige>` `` | Pasar a la marca acordada |
| `plantillas/memoria.md` | `<nombre>` dentro de una frase explicativa | Revisar: puede no ser un hueco |
| `plantillas/historico-chat.md` | `<estándar>`, `<archivo>` dentro de comandos | Revisar: es sintaxis de comando, no hueco |
| `plantillas/retrodocumentacion.md` | Ninguna | Revisar si le faltan huecos o no los necesita |

**La distinción que hay que decidir** es esa última columna: un `<algo>` dentro de un comando que el usuario copia y pega **no es un hueco del modelo**, es la sintaxis de ese comando. Si la regla no lo dice, el programa de EP-004 va a contar falsos positivos.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md` | Nuevo | Regla | Cuál es la marca y que es la misma en todos los modelos |
| `base/13-documentacion/reglas/DOC20-no-entregues-como-terminado-un-documento-con-marcas.md` | Nuevo | Regla | Un documento con marcas sin reemplazar no está terminado |
| `base/13-documentacion/reglas/DOC21-escribe-n-a-en-la-seccion-que-no-aplica.md` | Nuevo | Regla | Lo que no aplica se escribe `N/A`, no se deja con la marca ni se borra |
| `base/13-documentacion/base.md` | Modificar | Regla | Las tres filas nuevas en el índice del capítulo |
| `notas/` (archivo nuevo) | Nuevo | Documentación | Por qué esa marca y no otra: las alternativas que se descartaron |
| `plantillas/epica.md` | Modificar | Plantilla | Pasa sus huecos a la marca acordada |
| `plantillas/marco-normativo.md` | Modificar | Plantilla | Pasa sus huecos a la marca acordada |
| `plantillas/HU.md` | Modificar | Plantilla | 63 huecos en corchetes |
| `plantillas/planes/pruebas.md` | Modificar | Plantilla | 37 huecos en corchetes |
| `plantillas/planes/trabajo.md` | Modificar | Plantilla | 33 huecos en corchetes |
| `plantillas/funcionalidad-implementada.md` | Modificar | Plantilla | 22 huecos en corchetes |
| `plantillas/plantilla-spec-modulo.md` | Modificar | Plantilla | 13 huecos en corchetes |
| `plantillas/cierre-analisis.md` | Modificar | Plantilla | 4 huecos en corchetes |
| `plantillas/planes/resultados.md` | Modificar | Plantilla | 3 huecos en corchetes |
| `plantillas/senales.md` · `plantillas/proyectos.md` · `plantillas/estado-fase.md` · `plantillas/catalogo-modulos.md` | Modificar | Plantilla | 1 hueco cada una |
| `plantillas/memoria.md` · `plantillas/historico-chat.md` · `plantillas/retrodocumentacion.md` | Sin tocar | Plantilla | No son modelos que alguien llene: son procedimientos y explicaciones. Queda escrito en la nota |
| `validadores/reglas-validables.md` | Modificar | Documentación | La regla nueva entra como validable, pendiente de EP-004 |
| `CHANGELOG.md` · `VERSION` | Modificar | Versionado | Entrada y subida de versión (`20·M10`) |

### 2.2 Matriz de dependencias del refactor  ·  `F17`

| Archivo a refactorizar | Cambio de contrato | Archivos que dependen (rompen) | Dónde rompe |
|---|---|---|---|
| `plantillas/*.md` | Cambia el contenido, no la ruta ni el nombre | `validadores/instalar.py` | No rompe: las copia sin leerlas. Sí les cambia la huella, así que la copia de cada proyecto queda marcada vieja hasta la siguiente corrida |
| `base/13-documentacion.md` | Suma una regla; ninguna existente cambia de ID ni de texto | Lo que cite el capítulo 13 | No rompe: nada se renumera (`20·M11`) |

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica: el entregable es texto normativo y plantillas. No hay rutas ni autenticación.

### 2.4 Punto de entrada en la UI  ·  `F14` Q7

No aplica porque la fase no introduce interfaz. Se lee abriendo el capítulo 13 y cualquier plantilla.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La marca es `«…»` | `[texto]`, `<texto>`, `{{texto}}`, `XXX` | Ya se usa en 25 de 30 plantillas: elegir otra obliga a cambiar 25 archivos en vez de 5. Y las descartadas chocan con sintaxis que el propio documento usa: `[]` con los enlaces de markdown, `<>` con las etiquetas y con la sintaxis de los comandos, `{{}}` con los motores de plantillas |
| La sintaxis de un comando no es un hueco | Marcar todo `<algo>` como hueco | Un comando que el usuario copia y pega tiene su propia sintaxis. Contarla como hueco daría falsos positivos, y el riesgo de la épica es perder la confianza por eso |
| La regla va en el capítulo 13 | Un capítulo nuevo de documentos modelo | `20·M13` manda enrutar a lo que ya existe: la marca es cómo se escribe la documentación, y ese es el capítulo 13 |
| El porqué de la marca va a `notas/` | Dejarlo dentro de la regla | Una regla dice qué se exige, no por qué se eligió entre alternativas. El `CLAUDE.md` de este repositorio manda el razonamiento a `notas/` |

> Las decisiones no obvias se registran también como señal (`13·DOC5`).

### 2.7 Dudas por resolver antes de codificar

| # | Duda | A quién se consulta | Estado |
|---|---|---|---|
| 1 | Si la HU podía hacer de especificación, como en las dos fases anteriores | usuario | **Resuelta** el 2026-08-14: no. Lleva especificación aparte, y está escrita |
| 2 | Si un `<algo>` dentro de un comando se marca o se deja como está | usuario | **Resuelta** el 2026-08-14: no se marca. Es RN-04 de la especificación |
| 3 | Qué se escribe cuando una sección del modelo no aplica | usuario | **Resuelta** el 2026-08-14: `N/A`. Es RN-06 de la especificación |

> Ninguna tarea de construcción inicia con una duda abierta que la bloquee. Las tres se cerraron antes de aprobar el plan.

---

## 3. Desglose de tareas por criterio de aceptación

> Cada CA se descompone en tareas atómicas. **Depende de** ordena la ejecución; **Ev.** referencia la evidencia de §5.

### CA-01 — La marca se ve y se distingue del texto

| ID | Tarea | Capa | Est. | Depende de | Estado | Ev. |
|---|---|---|:--:|---|---|---|
| T-01 | Escribir en `notas/` por qué `«…»` y no las cuatro alternativas | Documentación | 1 h | — | ☑ | EV-01 |
| T-02 | Escribir `DOC19` con su ejemplo INCORRECTO/CORRECTO (`20·M5`) y aplicarle el checklist | Regla | 2 h | T-01 | ☑ | EV-01 |
| T-03 | Escribir dentro de `DOC19` qué es un hueco y qué no lo es: la sintaxis de comando queda fuera | Regla | 1 h | T-02 | ☑ | EV-01 |
| T-03b | Sumar las tres filas nuevas al índice de `base/13-documentacion/base.md` | Regla | 1 h | T-02, T-08, T-09 | ☑ | EV-01 |

### CA-02 — Todos los modelos usan la misma marca

| ID | Tarea | Capa | Est. | Depende de | Estado | Ev. |
|---|---|---|:--:|---|---|---|
| T-04 | Pasar `plantillas/epica.md` a la marca acordada | Plantilla | 1 h | T-03 | ☑ | EV-02 |
| T-05 | Pasar `plantillas/marco-normativo.md` a la marca acordada | Plantilla | 1 h | T-03 | ☑ | EV-02 |
| T-06 | Revisar los tres archivos dudosos y dejar escrito por qué cada uno cambia o no | Plantilla | 1 h | T-03 | ☑ | EV-02 |
| T-06b | Pasar los 11 archivos que conviven con corchetes, unos 179 huecos, sin tocar enlaces ni casillas | Plantilla | 3 h | T-03 | ☑ | EV-02 |
| T-07 | Recorrer las 30 plantillas y confirmar que no queda ninguna otra marca | Plantilla | 1 h | T-04, T-05, T-06, T-06b | ☑ | EV-02 |

### CA-03 — Un documento con marcas sin llenar no se da por terminado

| ID | Tarea | Capa | Est. | Depende de | Estado | Ev. |
|---|---|---|:--:|---|---|---|
| T-08 | Escribir `DOC20`, con su ejemplo y su checklist: un documento con marcas sin reemplazar no está terminado | Regla | 2 h | T-02 | ☑ | EV-03 |
| T-09 | Escribir `DOC21`, con su ejemplo y su checklist: la sección que no aplica se escribe `N/A` | Regla | 2 h | T-08 | ☑ | EV-03 |

### RNF — Requisitos no funcionales

| ID | Tarea | Categoría | Est. | Estado | Ev. |
|---|---|---|:--:|---|---|
| T-10 | Anotar las tres reglas en `validadores/reglas-validables.md`, en la lista que le toque a cada una | Documentación | 1 h | ☑ | EV-04 |
| T-11 | Correr `validar.py estandar` y comprobar que la regla nueva no rompe nada | Pruebas | 1 h | ☑ | EV-04 |
| T-12 | Entrada en `CHANGELOG.md` y subida de `VERSION` (`20·M10`) | Documentación | 1 h | ☑ | EV-04 |

**Total estimado:** 19 h. Eran 13 al aprobar. Las tres primeras horas de más son las dos reglas que se separaron y su fila en el índice; las otras tres, los 11 archivos que la línea base no había contado.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-08 → T-09 → T-03b → T-04 → T-07 → T-12

**Paralelizables:** T-05 y T-06 corren junto con T-04; T-10 no depende de nada de CA-02.

> Solo se tocan los archivos declarados en §2.1 (`F8`). Descubrir uno nuevo → PAUSAR, reportar, ampliar el plan con OK, no editar por iniciativa.

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

> Un CA no se marca cumplido sin evidencia. La fase no cierra con algún CA en rojo. El detalle de casos vive en el `plan_pruebas`.

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| [CA-01](../HU-001-marca-de-espacio-por-llenar.md#ca-01--la-marca-se-ve-y-se-distingue-del-texto) | Lectura de tres plantillas señalando los huecos, sin releer con atención | EV-01 | 2026-08-14 | ☑ |
| [CA-02](../HU-001-marca-de-espacio-por-llenar.md#ca-02--todos-los-modelos-usan-la-misma-marca) | Recuento de marcas en los 30 archivos de `plantillas/`, buscando también las descartadas | EV-02 | 2026-08-14 | ☑ |
| [CA-03](../HU-001-marca-de-espacio-por-llenar.md#ca-03--un-documento-con-marcas-sin-llenar-no-se-da-por-terminado) | Llenar un modelo dejando dos marcas a propósito y presentarlo como terminado | EV-03 | 2026-08-14 | ☑ |
| [RNF-01](../HU-001-marca-de-espacio-por-llenar.md#5-requisitos-no-funcionales) | Lectura completa de una plantilla ya convertida | EV-04 | 2026-08-14 | ☑ |
| [RNF-02](../HU-001-marca-de-espacio-por-llenar.md#5-requisitos-no-funcionales) | Revisión de los casos de sintaxis de comando, uno por uno | EV-04 | 2026-08-14 | ☑ |
| [RNF-03](../HU-001-marca-de-espacio-por-llenar.md#5-requisitos-no-funcionales) | Recuento de marcas en todo el catálogo | EV-02 | 2026-08-14 | ☑ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | La regla escrita y su nota | `base/13-documentacion.md` · `notas/` |
| EV-02 | Recuento por archivo, antes y después | `resultado_pruebas.md` de esta fase |
| EV-03 | El modelo llenado a medias y qué dice la regla de él | `resultado_pruebas.md` de esta fase |
| EV-04 | Salida de la corrida | Terminal |

---

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | El propio repositorio del estándar. No hay ambiente aparte: el entregable es texto |
| Usuarios de prueba | No aplica: no hay autenticación |
| Datos precargados | Las 30 plantillas que ya existen, y una copia de una de ellas llenada a medias |

> El detalle completo va en el [plan_pruebas.md](plan_pruebas.md).

---

## 7. Reversión / rollback  ·  `F14` Q11

Todo lo de esta fase es texto y no toca datos: se revierte con la reversión del commit. Las plantillas cambian de huella, así que la copia local de cada proyecto queda marcada vieja hasta la siguiente corrida del instalador; revertir la deja marcada vieja otra vez, y eso se arregla solo al correrlo.

---

## 8. Producción y migración incremental  ·  `F10` · `F14` Q12

**Obliga.** Un proyecto al día tiene plantillas con la marca vieja, y la regla nueva le exige la acordada. La migración la hace el instalador al copiar las plantillas; lo que el proyecto haya escrito **encima** de un modelo ya llenado no se toca, porque un documento terminado no es un modelo. Por eso el cambio de versión es MAYOR y lleva su aviso de migración.

---

## 9. Reglas del estándar y del proyecto aplicadas  ·  `F14` Q13

- Base: `02·F2`, `02·F8`, `02·F12.1`, `02·F12.10`, `02·F17`, `13·DOC5`, `13·DOC11`, `13·DOC12`, `20·M5`, `20·M9`, `20·M10`, `20·M11`, `20·M13`.
- Proyecto: no aplica. Este repositorio es el estándar y no tiene catálogo de reglas propias.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Las tres dudas de §2.7 sin responder | Detenían T-02 y T-03, que son la ruta crítica | Respondidas por el usuario el 2026-08-14 y escritas en la especificación | Cerrado |
| B-02 | Que la marca elegida se confunda con la sintaxis de un comando | El programa de EP-004 contaría falsos positivos | T-03 deja escrito qué no es un hueco, antes de tocar plantillas | Abierto |
| B-03 | Que el cambio a MAYOR obligue a migrar a proyectos que hoy no lo esperan | Trabajo no previsto en otros repositorios | §8 acota la migración a las plantillas, no a los documentos ya llenados | Abierto |

---

## 11. Definition of Done

- [ ] Todos los CA de §0 verificados con evidencia (§5)
- [ ] Requisitos no funcionales validados
- [ ] Pruebas de la fase en verde (alcance quirúrgico · `F5`)
- [ ] Trazabilidad especificación → implementación sin faltantes (`DOC11`)
- [ ] Documentación e índices/mapas del proyecto actualizados (`13`)
- [ ] Señales registradas (`DOC5`)
- [ ] Rama lista para el commit único de la fase (`G1`)
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario  ·  *(opcional — equipo)*

| Fecha | Tareas cerradas | Avance CA | Bloqueos | Ajuste al plan |
|---|---|---|---|---|
| 2026-08-14 | Las trece | Los tres CA en verde | Ninguno | Dos ampliaciones aprobadas, en §2 |

---

## 13. Cierre

**Resultado:** los tres CA y los tres RNF cumplidos, con un defecto aceptado (DEF-03 del resultado de pruebas). **Esfuerzo real vs. estimado:** 19 h estimadas tras las ampliaciones; se hizo en una sesión porque la conversión de los 179 huecos la hizo un script y no la mano.

**Lecciones aprendidas:** se escriben al cerrar.

**Deuda técnica generada:**

| Descripción | Registro / ticket |
|---|---|
| Sin ejecutar | |
