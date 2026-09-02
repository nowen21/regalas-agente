# Plan de Trabajo — Fase «A-EP-012-HU-001-el-expediente-se-arma-y-dice-que-le-falta» (módulo «Expediente»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas` de esta misma fase; lo que quedó hecho, en el `funcionalidad_implementada.md` del cierre.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-012-HU-001-el-expediente-se-arma-y-dice-que-le-falta` |
| **Épica** | [documentacion/epicas/EP-012-el-expediente-se-entrega-el-mismo-dia/epica.md](../../epica.md) |
| **HU** | [documentacion/epicas/EP-012-el-expediente-se-entrega-el-mismo-dia/HU-001-armar-el-expediente-de-un-proyecto/HU-001-armar-el-expediente-de-un-proyecto.md](../HU-001-armar-el-expediente-de-un-proyecto.md) — **una sola** (`F12.1`) |
| **Módulo** | Expediente |
| **Especificación del módulo** | [documentacion/expediente/spec.md](../../../../expediente/spec.md), aprobada el 2026-08-31 |
| **Fecha apertura** | 2026-08-31 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- ✨ **Funcionalidad nueva:** `F-025`, la primera de las dos obligatorias de la versión 2 que no tenían nada construido.

**CA de la HU que cubre esta fase:**

| CA de `HU-001` que cierra esta fase | Estado |
|---|---|
| [CA-01 — El expediente se arma en el orden del ciclo](../HU-001-armar-el-expediente-de-un-proyecto.md#ca-01--el-expediente-se-arma-en-el-orden-del-ciclo) | ☐ |
| [CA-02 — Lo que falta se lista, y no se inventa](../HU-001-armar-el-expediente-de-un-proyecto.md#ca-02--lo-que-falta-se-lista-y-no-se-inventa) | ☐ |
| [CA-03 — Lo que está a medio llenar se marca](../HU-001-armar-el-expediente-de-un-proyecto.md#ca-03--lo-que-está-a-medio-llenar-se-marca) | ☐ |
| [CA-04 — La auditoría y la memoria no entran](../HU-001-armar-el-expediente-de-un-proyecto.md#ca-04--la-auditoría-y-la-memoria-no-entran) | ☐ |
| [CA-05 — Se puede pedir hasta cierto alcance](../HU-001-armar-el-expediente-de-un-proyecto.md#ca-05--se-puede-pedir-hasta-cierto-alcance) | ☐ |

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** que el expediente de un proyecto se arme al pedirlo, en el orden del ciclo, y que **diga qué le falta y qué está a medio llenar** antes de que alguien lo entregue.

**La línea base, medida antes de escribir el plan:**

| Lo medido | Cuánto |
|---|---|
| Documentos traídos de este repositorio | **1 002** |
| Tipos distintos | 19 |
| Formas de juntarlos hoy | ninguna |

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | El orden del ciclo, no el del disco | Funcional | Media |
| CA-02 | Lo que falta, con nombre | Funcional | Alta |
| CA-03 | Lo incompleto, marcado | Funcional | Media |
| CA-04 | La auditoría y la memoria fuera | **Que NO pase** | Baja |
| CA-05 | Alcance acotado, diciendo qué dejó fuera | Funcional | Media |

**Fuera de alcance:**

- Generar el archivo de ofimática, que es la `HU-002`.
- Pantalla. La especificación lo permite en su §7: se entrega con orden de consola, como se hizo en Medición.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Lo que ya existe, comprobado contra el código real:**

| Pieza | Dónde | Qué aporta |
|---|---|---|
| Los documentos traídos y su tipo | `Traido` en [plataforma/nucleo/importacion/models.py](../../../../../plataforma/nucleo/importacion/models.py) | `proyecto`, `origen`, `tipo`, `guardado_en` |
| Qué tipo es cada archivo | [plataforma/nucleo/importacion/moldes.py](../../../../../plataforma/nucleo/importacion/moldes.py) | Los 19 tipos y las siete etapas |
| El texto de cada documento | `leer` en [plataforma/nucleo/almacen/core.py](../../../../../plataforma/nucleo/almacen/core.py) | Para contar los huecos sin llenar |

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `plataforma/nucleo/expediente/__init__.py` · `apps.py` | Nuevo | Módulo | |
| `plataforma/nucleo/expediente/orden.py` | Nuevo | Servicio | El orden del ciclo de la §5.1, y qué espera cada grupo |
| `plataforma/nucleo/expediente/core.py` | Nuevo | Servicio | `armar`, con sus tres listas |
| `plataforma/nucleo/expediente/management/commands/armar_expediente.py` | Nuevo | Orden | Pedirlo desde la consola |
| `plataforma/nucleo/expediente/tests.py` | Nuevo | Prueba | Los cinco CA |
| `plataforma/config/settings/base.py` | Modificar | Config | `nucleo.expediente` en la lista |

**Sin modelo y sin migración:** la especificación decide que el expediente **se calcula al pedirlo**.

### 2.2 Matriz de dependencias del refactor

No aplica: todo es nuevo y no cambia ningún contrato. Lee `Traido` y el almacén.

### 2.3 Rutas · 2.4 UI · 2.5 Permisos

No aplican en esta fase.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **El orden vive en su propio archivo**, como una lista declarada | Repartirlo en el código que arma | Es lo que la `HU-001` pedía declarar, y lo que hay que mirar el día que aparezca un tipo nuevo |
| **Lo que falta se calcula contra lo que el ciclo espera**, no contra una lista escrita al lado | Escribir a mano qué documentos debería tener un proyecto | Una lista escrita aparte envejece con el proyecto (`S-091`). Las siete etapas y los cinco documentos de una fase ya están escritos en el estándar |
| **Lo incompleto se cuenta leyendo el texto guardado** | Confiar en una marca del índice | El índice no guarda el contenido; contar los huecos exige abrir el documento, y es barato porque ya está en `datos/` |
| **La auditoría y la memoria se excluyen por su tipo**, no por su ruta | Excluir por carpeta | La ruta cambia entre proyectos; el tipo lo asigna Importación y es el mismo en todos |
| **Lo que no encaja se lista aparte** | Meterlo en el grupo más parecido | Acomodarlo convierte un dato en una suposición |
| Sin pantalla en esta fase | Construirla ahora | La §7 de la especificación lo permite, y el valor para el usuario lo cobra la `HU-002` |

### 2.7 Dudas por resolver antes de codificar

Ninguna abierta. Las dos que había —el alcance del expediente y el orden del ciclo— quedaron resueltas antes de escribir este plan.

---

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | CA | Ev. |
|---|---|---|:--:|---|---|---|
| T-00 | Contar lo traído de este repositorio: la línea base | Medición | 1 h | — | — | EV-02 |
| T-01 | `orden.py`: los nueve grupos y qué tipo va en cada uno | Servicio | 2 h | T-00 | CA-01 | EV-01 |
| T-02 | `armar`: juntar y agrupar en ese orden | Servicio | 3 h | T-01 | CA-01 | EV-01 |
| T-03 | Lo que falta, calculado contra lo que el ciclo espera | Servicio | 3 h | T-02 | CA-02 | EV-01 |
| T-04 | Lo incompleto, contando los huecos del texto | Servicio | 2 h | T-02 | CA-03 | EV-01 |
| T-05 | La auditoría y la memoria fuera, por tipo | Servicio | 1 h | T-02 | CA-04 | EV-01 |
| T-06 | Lo que no encaja, listado aparte | Servicio | 1 h | T-02 | CA-01 | EV-01 |
| T-07 | Acotar por alcance, diciendo qué queda fuera | Servicio | 2 h | T-02 | CA-05 | EV-01 |
| T-08 | La orden de consola | Orden | 1 h | T-07 | — | EV-02 |
| T-09 | Las pruebas de los cinco CA | Test | 3 h | T-07 | Todos | EV-01 |
| T-10 | Armarlo sobre este repositorio y dejar la salida escrita | Medición | 1 h | T-08 | Todos | EV-02 |

**Total estimado:** 20 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-00 → T-01 → T-02 → T-03 → T-08 → T-10
**Paralelizables:** T-04, T-05, T-06 y T-07 cuelgan de T-02 y no entre sí.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| [CA-01](../HU-001-armar-el-expediente-de-un-proyecto.md#ca-01--el-expediente-se-arma-en-el-orden-del-ciclo) | Armar el de este repositorio y comparar el orden con el ciclo | EV-01, EV-02 | | ☐ |
| [CA-02](../HU-001-armar-el-expediente-de-un-proyecto.md#ca-02--lo-que-falta-se-lista-y-no-se-inventa) | Quitar un documento de un proyecto de prueba | EV-01 | | ☐ |
| [CA-03](../HU-001-armar-el-expediente-de-un-proyecto.md#ca-03--lo-que-está-a-medio-llenar-se-marca) | Un documento con huecos sin llenar | EV-01 | | ☐ |
| [CA-04](../HU-001-armar-el-expediente-de-un-proyecto.md#ca-04--la-auditoría-y-la-memoria-no-entran) | Sobre este repositorio, que tiene las dos | EV-01, EV-02 | | ☐ |
| [CA-05](../HU-001-armar-el-expediente-de-un-proyecto.md#ca-05--se-puede-pedir-hasta-cierto-alcance) | Completo contra acotado | EV-01 | | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Las pruebas del módulo | `plataforma/nucleo/expediente/tests.py` |
| EV-02 | El expediente de este repositorio, armado | `resultado_pruebas.md` §2 |

---

## 6. Datos y ambiente de prueba

Proyectos de mentiras que la propia prueba crea, y **lo traído de verdad** para la corrida final. Nada se escribe: el módulo solo lee.

---

## 7. Reversión / rollback  ·  Q11

Nada que revertir en datos: no se guarda nada. El código está versionado.

---

## 8. Producción y migración incremental  ·  Q12

**Aditivo puro.** Una aplicación más en la lista, sin tablas y sin migración.

---

## 9. Reglas aplicadas  ·  Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F19`](../../../../../base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md), [`13·DOC19`](../../../../../base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md) para contar los huecos.
- Producto: `RN-1` a `RN-7` de la especificación del módulo.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que «lo que falta» dé una lista enorme y deje de leerse | Alto | Se calcula contra lo que el ciclo espera de verdad, no contra un ideal. Y se mide sobre este repositorio antes de darlo por bueno | Abierto hasta T-10 |
| B-02 | Que un tipo nuevo quede fuera del orden sin que nadie lo note | Medio | Lo que no encaja **se lista aparte**, con su tipo | Cerrado |
| B-03 | Que armar toque algún documento | Alto | El módulo solo lee, y la prueba compara la carpeta antes y después | Cerrado |

---

## 11. Definition of Done

- [ ] Los cinco CA verificados con evidencia
- [ ] El expediente de este repositorio armado, con su salida escrita
- [ ] Comprobado que la auditoría y la memoria no entraron
- [ ] Las dos baterías en verde
- [ ] Señales registradas
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
