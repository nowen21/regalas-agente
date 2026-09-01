# Plan de Trabajo — Fase `A-EP-013-HU-001-los-huecos-de-un-documento-se-ven` (módulo Ciclo de vida)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas` de esta misma fase; lo que quedó hecho, en el `funcionalidad_implementada.md` del cierre.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-013-HU-001-los-huecos-de-un-documento-se-ven` |
| **Épica** | [documentacion/epicas/EP-013-los-documentos-se-llenan-sin-salir-de-la-plataforma/epica.md](../../epica.md) |
| **HU** | [documentacion/epicas/EP-013-los-documentos-se-llenan-sin-salir-de-la-plataforma/HU-001-ver-que-le-falta-a-un-documento/HU-001-ver-que-le-falta-a-un-documento.md](../HU-001-ver-que-le-falta-a-un-documento.md) — **una sola** (`F12.1`) |
| **Módulo** | Ciclo de vida |
| **Especificación del módulo** | [documentacion/ciclo-de-vida/spec.md](../../../../ciclo-de-vida/spec.md), aprobada el 2026-09-01 |
| **Fecha apertura** | 2026-09-01 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN:**

- ✨ **Funcionalidad nueva:** `F-014`, la última obligatoria de la versión 2 sin construir.

**CA de la HU que cubre esta fase:**

| CA de `HU-001` que cierra esta fase | Estado |
|---|---|
| [CA-01 — Se dice qué molde sigue el documento](../HU-001-ver-que-le-falta-a-un-documento.md#ca-01--se-dice-qué-molde-sigue-el-documento) | ☐ |
| [CA-02 — Se listan los huecos, con cuántos son y dónde](../HU-001-ver-que-le-falta-a-un-documento.md#ca-02--se-listan-los-huecos-con-cuántos-son-y-dónde) | ☐ |
| [CA-03 — Solo el hueco cierto entra en la cuenta](../HU-001-ver-que-le-falta-a-un-documento.md#ca-03--solo-el-hueco-cierto-entra-en-la-cuenta) | ☐ |
| [CA-04 — Lo que llena la instalación no se cuenta como pendiente](../HU-001-ver-que-le-falta-a-un-documento.md#ca-04--lo-que-llena-la-instalación-no-se-cuenta-como-pendiente) | ☐ |
| [CA-05 — Un documento de tipo desconocido lo dice](../HU-001-ver-que-le-falta-a-un-documento.md#ca-05--un-documento-de-tipo-desconocido-lo-dice) | ☐ |

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** que de cualquier documento del ciclo se pueda pedir qué molde sigue y qué huecos le faltan, con la cuenta y con dónde está cada uno.

**Solo mira.** Escribir es la fase de la `HU-002`. Se separan porque contar y escribir fallan de formas distintas: contar mal da un número equivocado, escribir mal daña un documento.

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | El molde del tipo | Funcional | Baja |
| CA-02 | La cuenta y la ubicación | Funcional | Media |
| CA-03 | **La cuenta y la lista aparte** | Funcional | Media |
| CA-04 | **La clase que no se pregunta** | Funcional | Baja |
| CA-05 | El tipo desconocido | Funcional | Baja |

**Fuera de alcance:**

- Escribir en el documento.
- Pantalla: se termina con orden de consola, como Medición y Expediente.
- Juzgar si lo ya escrito es bueno.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Lo que ya existe y se reutiliza:**

| Pieza | Qué aporta |
|---|---|
| `plataforma/nucleo/importacion/moldes.py` | `tipo_de(nombre, relativa)`, que reconoce **19 tipos** por nombre, por forma y por ubicación |
| `plataforma/nucleo/expediente/core.py` | Ya cuenta la marca `«…»` para decir qué documento está incompleto |
| `plataforma/nucleo/proyectos/` | Dice dónde vive el proyecto en el disco |

**Lo que hay que resolver, contado sobre lo real el 2026-09-01:**

| Qué se contó | Cuánto |
|---|---|
| Huecos con nombre en `plantillas/` | 2 079 |
| Huecos sin nombre `«…»` | 707 |
| Marcas en las 130 historias reales | 341 |
| De esas, las que están en el molde | 75 |
| **De esas, las que siguen en la línea del molde** | **0** |
| Huecos que llena la instalación | 134 |
| Moldes del ciclo | 22 archivos en `plantillas/ciclo-vida-proyectos/` |
| Tipos reconocidos con molde | 17 de 19 |

**Se midió antes de construir, y la medición cambió el plan.** La idea era contar también los huecos con nombre. No se puede: en un documento escrito **no se distinguen de una cita**, porque acá se cita con esas mismas comillas. De las 341 marcas de las 130 historias, 75 están en el molde y ninguna sigue en su línea; son etiquetas del autor.

**Entonces la cuenta de esta fase coincide con la del expediente**, y eso es bueno: las dos dicen lo mismo porque salen del mismo sitio. Los de nombre se listan aparte, porque cuando `F-011` cree documentos desde el molde sí van a ser ciertos.

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `plataforma/nucleo/ciclo_de_vida/__init__.py` | Nuevo | Módulo | |
| `plataforma/nucleo/ciclo_de_vida/apps.py` | Nuevo | Config | |
| `plataforma/nucleo/ciclo_de_vida/moldes.py` | Nuevo | Servicio | La §5.2: qué molde le toca a cada tipo |
| `plataforma/nucleo/ciclo_de_vida/huecos.py` | Nuevo | Servicio | Encontrar y clasificar la marca |
| `plataforma/nucleo/ciclo_de_vida/core.py` | Nuevo | Servicio | `que_le_falta(documento)` |
| `plataforma/nucleo/ciclo_de_vida/management/commands/que_le_falta.py` | Nuevo | Orden | Pedirlo desde la consola |
| `plataforma/nucleo/ciclo_de_vida/tests.py` | Nuevo | Prueba | Los cinco CA |
| `plataforma/config/settings/base.py` | Modificar | Config | `nucleo.ciclo_de_vida` en la lista de aplicaciones |
| `documentacion/ciclo-de-vida/spec.md` | Modificar | Especificación | Solo su §13, para nombrar la fase |

**Ninguna entidad y ninguna migración:** los huecos se calculan al pedirlos, según la §5 de la especificación.

### 2.2 Matriz de dependencias del refactor

No aplica: todo es nuevo. Lee `moldes.py` de Importación y no lo modifica.

### 2.3 Rutas · 2.4 UI · 2.5 Permisos

No aplican en esta fase.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **La tabla de moldes se declara, no se deduce** | Deducirla del nombre del tipo | Tres de los 17 moldes viven fuera de `ciclo-vida-proyectos/`, y dos tipos no tienen. Deducir fallaría en cinco de 19 |
| **Un hueco se ubica por línea y por su contexto** | Solo por posición | La `HU-002` va a escribir en esa ubicación. Si el documento cambió, la posición sola apunta a otra parte |
| **Solo el hueco cierto entra en la cuenta** | Contar también los que tienen nombre | Medido: ninguna de las 341 marcas reales es un hueco con nombre sin llenar. Contarlas daría por incompleto un documento bien escrito |
| **Las tres cuentas se devuelven aparte** | Una sola cuenta | `RN-3`: lo que no se le pregunta al usuario tampoco desaparece en silencio |
| **Se lee el molde cuando se pide** | Copiarlo dentro del módulo | Un molde copiado envejece en cuanto el estándar cambie el original |
| **Un tipo sin molde se devuelve como reconocido y sin molde** | Devolver que no se reconoce | Son dos cosas distintas, y confundirlas esconde la que se puede arreglar |

### 2.7 Dudas por resolver antes de codificar

Ninguna abierta.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | CA | Ev. |
|---|---|---|:--:|---|---|---|
| T-01 | El módulo, y su registro en las aplicaciones | Config | 1 h | — | — | EV-01 |
| T-02 | La tabla de moldes, con los cinco casos que no son directos | Servicio | 2 h | T-01 | CA-01, CA-05 | EV-01 |
| T-03 | Encontrar la marca y clasificarla: cierto, posible, de instalación | Servicio | 3 h | T-01 | CA-03, CA-04 | EV-01 |
| T-04 | La línea y el contexto de cada hueco | Servicio | 2 h | T-03 | CA-02 | EV-01 |
| T-05 | `que_le_falta`, con las cuentas separadas | Servicio | 2 h | T-02, T-04 | CA-02, CA-04 | EV-01 |
| T-06 | La orden de consola | Orden | 1 h | T-05 | Todos | EV-02 |
| T-07 | Las pruebas de los cinco CA | Test | 3 h | T-06 | Todos | EV-01 |
| T-08 | Correrlo sobre los documentos de este repositorio y **contar** | Medición | 2 h | T-06 | CA-02 | EV-02 |

**Total estimado:** 16 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-03 → T-04 → T-05 → T-06 → T-08.

T-02 va en paralelo desde T-01: la tabla de moldes no depende de cómo se encuentra la marca.

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Con un `plan_trabajo.md` y un `epica.md` reales, y con los tres moldes que viven fuera de la carpeta del ciclo | EV-01 | | ☐ |
| CA-02 | **Contar sobre los documentos de este repositorio**, y comparar con contar la marca a mano | EV-01, EV-02 | | ☐ |
| CA-03 | **Sobre las 130 historias reales**: que la cuenta de ciertos no incluya los de nombre, y que coincida con la del expediente | EV-01, EV-02 | | ☐ |
| CA-04 | Contar con y sin la marca de instalación, donde aparece 134 veces | EV-01, EV-02 | | ☐ |
| CA-05 | Con un archivo de nombre inventado | EV-01 | | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Las pruebas del módulo | `plataforma/nucleo/ciclo_de_vida/tests.py` |
| EV-02 | Lo contado sobre este repositorio | `resultado_pruebas.md` §1 |

---

## 6. Datos y ambiente de prueba

Documentos de mentiras que la prueba escribe en carpetas temporales, y **los documentos reales de este repositorio** para la medición del `CA-02`. Esta fase **solo lee**, así que no puede dañar nada.

---

## 7. Reversión / rollback  ·  Q11

Nada que revertir: el módulo no escribe. El código está versionado.

---

## 8. Producción y migración incremental  ·  Q12

**Aditivo puro.** Ninguna migración, ninguna dependencia nueva, ninguna entidad.

---

## 9. Reglas aplicadas  ·  Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F19`](../../../../../base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md), [`13·DOC19`](../../../../../base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md), que es la convención que se busca.
- Producto: `DA-01`, y las `RN-1` a `RN-3` y `RN-8` de la especificación del módulo.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que la cuenta infle con marcas que no son huecos | **Alto** | Ya pasó: contar `«texto»` daba 559 documentos incompletos en vez de 31. Se cuenta sobre lo real y se compara con la cuenta a mano | Abierto hasta T-08 |
| B-02 | Que un tipo quede sin molde y se le asigne el parecido | Medio | La tabla se declara, y los dos sin molde se devuelven como tales | Cerrado por diseño |
| B-03 | Que esta cuenta y la del expediente se separen | Medio | Las dos cuentan lo mismo: `«…»`. **Se comprueba corriendo las dos y comparando el número** | Abierto hasta T-08 |

---

## 11. Definition of Done

- [ ] Los cinco CA verificados con evidencia
- [ ] Corrido sobre los documentos de este repositorio, **con los huecos contados**
- [ ] Comprobado que ningún documento cambió al mirarlo
- [ ] Las dos baterías en verde
- [ ] Señales registradas
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
