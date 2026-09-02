# Plan de Trabajo — Fase `B-EP-013-HU-002-el-hueco-se-llena-sin-tocar-lo-demas` (módulo Ciclo de vida)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas` de esta misma fase; lo que quedó hecho, en el `funcionalidad_implementada.md` del cierre.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-013-HU-002-el-hueco-se-llena-sin-tocar-lo-demas` |
| **Épica** | [EP-013](../../epica.md) |
| **HU** | [HU-002 Llenar un hueco desde la plataforma](../HU-002-llenar-un-hueco-desde-la-plataforma.md) — **una sola** (`F12.1`) |
| **Módulo** | Ciclo de vida |
| **Especificación del módulo** | [documentacion/ciclo-de-vida/spec.md](../../../../ciclo-de-vida/spec.md), aprobada el 2026-09-01 |
| **Fecha apertura** | 2026-09-01 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN:**

- ✨ **Funcionalidad nueva:** `F-014`, la segunda mitad. La primera cerró en la fase A.

**CA de la HU que cubre esta fase:**

| CA de `HU-002` que cierra esta fase | Estado |
|---|---|
| [CA-01 — Se llena un hueco y queda en el archivo](../HU-002-llenar-un-hueco-desde-la-plataforma.md#ca-01--se-llena-un-hueco-y-queda-en-el-archivo) | ☐ |
| [CA-02 — Lo que no es el hueco no cambia](../HU-002-llenar-un-hueco-desde-la-plataforma.md#ca-02--lo-que-no-es-el-hueco-no-cambia) | ☐ |
| [CA-03 — La cuenta de huecos baja](../HU-002-llenar-un-hueco-desde-la-plataforma.md#ca-03--la-cuenta-de-huecos-baja) | ☐ |
| [CA-04 — Si el archivo cambió por fuera, se avisa](../HU-002-llenar-un-hueco-desde-la-plataforma.md#ca-04--si-el-archivo-cambió-por-fuera-se-avisa) | ☐ |
| [CA-05 — Queda registrado](../HU-002-llenar-un-hueco-desde-la-plataforma.md#ca-05--queda-registrado) | ☐ |

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** que un hueco se llene desde la plataforma y lo escrito quede en el archivo del proyecto, sin que nada más cambie.

**Es la primera vez que la plataforma escribe fuera de `datos/`.** Hasta hoy lee los proyectos y escribe solo sus propias copias. Se decidió con el usuario el 2026-09-01: escribir en la copia dejaría el proyecto igual, y la copia se rehace al importar, así que lo escrito ahí se perdería a la primera.

**Eso cambia el peso de la fase.** Un error acá no da un número equivocado: toca el repositorio del usuario. Por eso el `CA-02` compara el archivo entero y el `CA-04` no escribe encima de un cambio ajeno.

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Lo escrito queda en el archivo | Funcional | Media |
| CA-02 | **Nada cambia fuera del hueco** | Funcional | **Alta** |
| CA-03 | La cuenta baja en uno | Funcional | Baja |
| CA-04 | **El cambio ajeno no se pisa** | Funcional | **Alta** |
| CA-05 | Queda registrado | Funcional | Baja |

**Fuera de alcance:**

- Redactar libre, y editar fuera de un hueco.
- Crear documentos nuevos (`F-011`, versión 5).
- Pantalla: se termina con orden de consola, como la fase A.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Lo que ya existe y se reutiliza:**

| Pieza | Qué aporta |
|---|---|
| `plataforma/nucleo/ciclo_de_vida/huecos.py` | Encuentra cada hueco con su línea, su columna y su contexto |
| `plataforma/nucleo/ciclo_de_vida/core.py` | `que_le_falta`, y la cuenta que tiene que bajar |
| `plataforma/nucleo/auditoria/` | `con_constancia`, que registra antes del efecto |
| `plataforma/nucleo/importacion/core.py` | Trae un documento; sirve para que la copia no se separe |
| `plataforma/nucleo/proyectos/models.py` | `ruta_codigo`, que dice dónde vive el proyecto de verdad |

**Lo verificado sobre el código real el 2026-09-01:**

| Qué se comprobó | Resultado |
|---|---|
| Sitios donde la plataforma escribe hoy | **Dos**, los dos dentro de `datos/` |
| Sitios donde escribe en un proyecto | **Ninguno**. Esta fase abre el primero |
| Documentos con huecos que se pueden llenar | 54, con 77 huecos |

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `plataforma/nucleo/ciclo_de_vida/escritura.py` | Nuevo | Servicio | Reemplazar un hueco y guardar sin dejar el archivo a medias |
| `plataforma/nucleo/ciclo_de_vida/core.py` | Modificar | Servicio | `llenar(proyecto, origen, hueco, texto)` |
| `plataforma/nucleo/ciclo_de_vida/management/commands/llenar_hueco.py` | Nuevo | Orden | Pedirlo desde la consola |
| `plataforma/nucleo/ciclo_de_vida/tests_escritura.py` | Nuevo | Prueba | Los cinco CA |
| `documentacion/ciclo-de-vida/spec.md` | Modificar | Especificación | Solo su §13, para nombrar la fase |

**Ninguna entidad y ninguna migración.**

### 2.2 Matriz de dependencias del refactor

`core.py` crece con una función nueva; lo que ya tiene no se toca. Las 26 pruebas de la fase A lo comprueban.

### 2.3 Rutas · 2.4 UI · 2.5 Permisos

No aplican en esta fase.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **Se escribe en el archivo original del proyecto** | Escribir en la copia de `datos/` | Decidido con el usuario el 2026-09-01. La copia se rehace al importar y el proyecto quedaría igual |
| **Se escribe completo aparte y se pone en su sitio de un golpe** | Escribir encima del archivo | Si el guardado se interrumpe, el archivo queda a medias. Acá o está el de antes o está el de después |
| **Se compara la huella del contenido leído antes de escribir** | Confiar en que nadie lo tocó | Es lo único que distingue «nadie lo tocó» de «alguien más escribió» |
| **El hueco se ubica por línea, columna y contexto** | Solo por posición | Si el documento se movió, la posición apunta a otra parte, y ahí se escribiría sobre lo que no era |
| **Después de escribir se vuelve a traer ese documento** | Dejar la copia vieja | Si no, la cuenta seguiría mostrando el hueco que ya se llenó |
| **Se registra antes del efecto** | Registrar después | Es como ya trabaja la auditoría: un efecto sin constancia es un efecto que nadie puede auditar |
| **Llenar con texto vacío no hace nada** | Guardar el vacío | Borrar la marca sin poner nada deja el documento peor: ya no se ve que falta |

### 2.7 Dudas por resolver antes de codificar

Ninguna abierta. La de dónde se escribe se resolvió antes de abrir la fase.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | CA | Ev. |
|---|---|---|:--:|---|---|---|
| T-01 | Reemplazar un hueco en el texto, sin tocar nada más | Servicio | 2 h | — | CA-02 | EV-01 |
| T-02 | Guardar de un golpe, sin dejar el archivo a medias | Servicio | 2 h | T-01 | CA-01 | EV-01 |
| T-03 | La huella, y el aviso si el archivo cambió por fuera | Servicio | 2 h | T-02 | CA-04 | EV-01 |
| T-04 | `llenar`, con el registro antes del efecto | Servicio | 2 h | T-03 | CA-05 | EV-01 |
| T-05 | Volver a traer el documento, para que la copia no se separe | Servicio | 1 h | T-04 | CA-03 | EV-01 |
| T-06 | La orden de consola | Orden | 2 h | T-05 | Todos | EV-02 |
| T-07 | Las pruebas de los cinco CA | Test | 3 h | T-06 | Todos | EV-01 |
| T-08 | **Llenar un documento real de punta a punta** y comparar el archivo entero | Medición | 2 h | T-06 | CA-02 | EV-02 |

**Total estimado:** 16 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-04 → T-06 → T-08.

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Llenar y leer el archivo por fuera de la plataforma | EV-01, EV-02 | | ☐ |
| CA-02 | **Comparar el archivo entero antes y después**, con el hueco descontado, sobre un documento largo y con tablas | EV-01, EV-02 | | ☐ |
| CA-03 | La cuenta de la fase A, antes y después | EV-01 | | ☐ |
| CA-04 | Leer, cambiar el archivo por fuera, y guardar | EV-01 | | ☐ |
| CA-05 | Llenar uno y leer el registro | EV-01 | | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Las pruebas de la escritura | `plataforma/nucleo/ciclo_de_vida/tests_escritura.py` |
| EV-02 | Un documento real llenado de punta a punta | `resultado_pruebas.md` §3 |

---

## 6. Datos y ambiente de prueba

Carpetas temporales para las pruebas automáticas. **Para el `T-08`, un documento real de este repositorio**, que está versionado: si algo sale mal, el control de versiones lo devuelve. No reemplaza al `CA-04`: avisar antes vale más que poder deshacer después.

---

## 7. Reversión / rollback  ·  Q11

Todo lo que esta fase escribe queda en archivos versionados. **El código nuevo se revierte solo**; lo escrito en un documento se revierte con el control de versiones del proyecto.

---

## 8. Producción y migración incremental  ·  Q12

**Aditivo puro.** Ninguna migración, ninguna dependencia nueva. Lo que cambia es que la plataforma pasa a escribir en el proyecto, y eso está declarado en la especificación.

---

## 9. Reglas aplicadas  ·  Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F19`](../../../../../base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md), y [`03`](../../../../../base/03-datos.md) por el guardado que no puede quedar a medias.
- Producto: `DA-01`, `DA-08` y `DA-12`, y las `RN-1` a `RN-7` de la especificación del módulo.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | **Que guardar reformatee el documento** | **Alto — hunde la historia** | El `CA-02` compara el archivo entero, sobre un documento con tablas | Abierto hasta T-08 |
| B-02 | Que se escriba encima de un cambio ajeno | **Alto — se pierde trabajo de otro** | La huella se compara antes de escribir | Abierto hasta T-03 |
| B-03 | Que un guardado interrumpido deje el archivo a medias | Alto | Se escribe aparte y se pone en su sitio de un golpe | Abierto hasta T-02 |
| B-04 | Que la copia y el original se separen | Medio | Se vuelve a traer el documento después de escribir | Abierto hasta T-05 |
| B-05 | Que el hueco se ubique mal y se escriba sobre lo que no era | Alto | Se comprueba el contexto además de la posición | Abierto hasta T-01 |

---

## 11. Definition of Done

- [ ] Los cinco CA verificados con evidencia
- [ ] **Un documento real llenado de punta a punta**, con el archivo comparado entero
- [ ] Comprobado que un cambio ajeno no se pisa
- [ ] Las dos baterías en verde
- [ ] Señales registradas
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
