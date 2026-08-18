# Resultado de pruebas — Fase A-EP-003-HU-005-retrodocumentar-los-modelos-de-la-capa-3

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-003-HU-005-retrodocumentar-los-modelos-de-la-capa-3` |
| **HU** | [HU-005](../HU-005-modelos-de-la-capa-de-proyecto.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) · PP-A-EP-003-HU-005 v1.0 |
| **Ciclo** | 1 · **Fecha** 2026-08-17 · **Ejecutado por** el agente, con el plan aprobado ese día |
| **Ambiente y versión** | Los modelos de `plantillas/`, y proyectos temporales recién instalados. Estándar 23.3.0 |

---

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

**Veredicto de la fase: Cumple** (§6). Los tres modelos existen, no se pisan al reinstalar, ninguno pide credenciales, y lo no declarado no genera exigencia.

---

## 2. Ejecución caso por caso

| Caso | CA | Prioridad | Con qué se probó | Resultado | Evidencia |
|---|---|---|---|---|---|
| [CP-001](plan_pruebas.md) | CA-01 | Crítica | Los tres modelos, y un proyecto reinstalado | Aprobado | EV-01 |
| [CP-002](plan_pruebas.md) | CA-02 | Alta | La parte que un programa lee | Aprobado | EV-01 |
| [CP-003](plan_pruebas.md) | CA-03 | Alta | Un proyecto que no declara su convención | Aprobado | EV-01 |

---

### Detalle de CP-001 — Los tres existen y no se pisan

| Modelo | Qué declara el proyecto |
|---|---|
| [`stack.md`](../../../../../plantillas/stack.md) | Con qué está construido |
| [`dominio.md`](../../../../../plantillas/dominio.md) | Qué palabras significan qué en este negocio |
| [`mapeo-nombres.md`](../../../../../plantillas/mapeo-nombres.md) | Cómo se traduce entre el dominio y el código |

**No se pisan al reinstalar:** se comprobó en la fase hermana [`A-EP-007-HU-005`](../../../EP-007-instalacion-y-actualizacion/HU-005-no-pisar-lo-escrito/A-EP-007-HU-005-retrodocumentar-que-no-se-pisa-lo-escrito/resultado_pruebas.md), marcando **los quince archivos** de un proyecto instalado y reinstalando. Los tres están entre los trece que conservan lo propio — y son, junto con `marco-normativo.md`, los únicos irreponibles: los llena una persona.

---

### Detalle de CP-002 — Lo que un programa lee tiene forma fija

La parte de estos documentos que un programa lee está marcada, y el resto es prosa libre. Es lo que permite que el proyecto escriba lo que necesite sin romper lo que se comprueba.

**Y recién instalados quedan con sus marcas `«…»` puestas.** No es un descuido: es la señal de que el documento **no está terminado**, y es lo que [`13·DOC20`](../../../../../base/13-documentacion/reglas/DOC20-no-entregues-como-terminado-un-documento-con-marcas.md) usa para saberlo. Un modelo que llegara sin marcas parecería lleno.

---

### Detalle de CP-003 — Lo no declarado no se comprueba

**Un proyecto que no declara su convención de nombres no recibe hallazgos de nomenclatura.**

Y es la decisión correcta, aunque suene a laxitud: exigir contra una convención que nadie escribió sería **inventarla**. El validador estaría imponiendo un criterio que el proyecto nunca aceptó, y el proyecto aprendería a ignorar sus hallazgos — que es el daño que ya está descrito en el [pendiente 55](../../../../../pendientes/55-el-validador-lee-enlaces-dentro-de-las-comillas-de-codigo.md) para otro caso.

**La contrapartida está en el checklist:** no declarar la convención sale como instalación incompleta, no como cumplimiento. No se castiga con hallazgos falsos; se cuenta como algo que falta.

---

## 3. Verificaciones manuales

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que los tres modelos existan | Buscándolos en `plantillas/` | Los tres |
| 2 | Que ninguno pida credenciales | Buscando en los tres las palabras de credencial como dato por llenar | **Ninguno** |
| 3 | Que lleguen con sus marcas puestas | Leyéndolos | Los tres las traen |
| 4 | Que no se pisen al reinstalar | La fase hermana de EP-007 | Los tres entre los 13 conservados |
| 5 | Que la suite siga verde | `python validadores/pruebas.py` | 348 pruebas · verde, con 6 fallos esperados |

---

## 4. Defectos encontrados

| ID | Severidad | Qué es | Dónde queda |
|---|---|---|---|
| D-01 | Baja | El plan de pruebas declara cobertura completa y **no le escribe caso a los dos transversales**. Se probaron igual | El plan aprobado no se modifica. Mismo defecto de molde de las 51 fases |

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos | Resultado | Cumple |
|---|---|---|---|
| [CA-01](../HU-005-modelos-de-la-capa-de-proyecto.md#ca-01--los-tres-modelos-existen-y-no-se-pisan) | CP-001 | Los tres existen y conservan lo que la persona les escriba | Sí |
| [CA-02](../HU-005-modelos-de-la-capa-de-proyecto.md#ca-02--lo-que-un-programa-lee-tiene-forma-fija) | CP-002 | La parte leída por un programa está marcada; el resto es prosa libre | Sí |
| [CA-03](../HU-005-modelos-de-la-capa-de-proyecto.md#ca-03--lo-no-declarado-no-se-comprueba) | CP-003 | Sin convención declarada no hay hallazgos de nomenclatura; sale como instalación incompleta | Sí |
| Transversal · Límites | Verificación 3 | Recién instalados quedan con sus marcas `«…»`, que es lo que dice que no están terminados | Sí |
| Transversal · Privacidad | Verificación 2 | **Ninguno pide credenciales ni datos personales** | Sí |

**Los que no cumplen:** ninguno.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Meta | Resultado | Cumple |
|---|---|---|---|
| Cobertura de exigencias | 100% | 100% de lo que el plan contó, más los dos transversales | Sí |
| Casos ejecutados | 3 de 3 | 3 de 3 | Sí |
| Modelos que pidan credenciales | **0** | **0** | Sí |
| Exigencias generadas por lo no declarado | **0** | **0** | Sí |

---

## 6. Veredicto de la fase

**Concepto:** **Cumple.**

**Justificación:** los tres criterios quedaron verificados y los dos transversales también. El que más valía escribir es el CA-03, porque su comportamiento se puede confundir con laxitud: **lo no declarado no se comprueba**, y eso es lo correcto — exigir contra una convención que nadie escribió sería inventarla, y el proyecto aprendería a ignorar los hallazgos. Lo que sí ocurre es que no declararla sale como instalación incompleta.

**Qué falta para que cumpla:** nada.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Casos automatizados | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `ModelosDeLaCapaDeProyecto`: 3 pruebas, en verde |
| EV-02 | Que no se pisan | La fase hermana [`A-EP-007-HU-005`](../../../EP-007-instalacion-y-actualizacion/HU-005-no-pisar-lo-escrito/A-EP-007-HU-005-retrodocumentar-que-no-se-pisa-lo-escrito/resultado_pruebas.md) |
| EV-03 | Lo escrito | [`documentacion/documentos-modelo/spec.md`](../../../../documentos-modelo/spec.md) §4.3 |
| EV-04 | Corrida completa | `python validadores/pruebas.py` — 348 pruebas, verde, 6 fallos esperados |

---

## 8. Ciclos anteriores

Ninguno: es el primero.
