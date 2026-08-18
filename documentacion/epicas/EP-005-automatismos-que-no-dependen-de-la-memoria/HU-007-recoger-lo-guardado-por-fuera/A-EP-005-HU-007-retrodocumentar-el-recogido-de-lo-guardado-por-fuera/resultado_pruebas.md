# Resultado de pruebas — Fase A-EP-005-HU-007-retrodocumentar-el-recogido-de-lo-guardado-por-fuera

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-005-HU-007-retrodocumentar-el-recogido-de-lo-guardado-por-fuera` |
| **HU** | [HU-007](../HU-007-recoger-lo-guardado-por-fuera.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) · PP-A-EP-005-HU-007 v1.0 |
| **Ciclo** | 1 · **Fecha** 2026-08-17 · **Ejecutado por** el agente, con el plan aprobado ese día |
| **Ambiente y versión** | Proyectos temporales con su almacén de mentira, y el almacén real **en lectura**. Estándar 23.3.0 |

---

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Veredicto de la fase: Cumple** (§6). El recogido mueve lo guardado por fuera al repositorio, deja el almacén sin archivos, y **nunca borra**: el nombre repetido entra al lado, con sufijo, y decide el usuario cuál manda.

---

## 2. Ejecución caso por caso

| Caso | CA | Prioridad | Con qué se probó | Resultado | Evidencia |
|---|---|---|---|---|---|
| [CP-001](plan_pruebas.md) | CA-01 | Crítica | Un recuerdo en el almacén de mentira | Aprobado | EV-01 |
| [CP-002](plan_pruebas.md) | CA-01 | Crítica | El almacén después de recoger, y un puntero puesto a mano | Aprobado | EV-01 |
| [CP-003](plan_pruebas.md) | CA-02 | Crítica | Un recuerdo que ya existe en el repositorio | Aprobado | EV-01 |
| [CP-004](plan_pruebas.md) | CA-02 | Crítica | Dos con el mismo nombre y contenido distinto | Aprobado | EV-01 |

---

### Detalle de CP-001 y CP-002 — Se recoge, y el almacén queda sin nada

| Qué se probó | Qué salió |
|---|---|
| Un recuerdo en el almacén local, al recoger | **Llega al repositorio** |
| El almacén después | **Sin archivos `.md`** |
| Un **puntero** puesto a mano —un archivo que solo dice dónde quedó el recuerdo— | **También se saca** |
| Correr con el almacén ya vacío | No falla, y no hace nada |
| El almacén real de esta máquina | **Vacío**, el 2026-08-17 |

**El puntero es tan malo como la copia**, y por eso el caso lo prueba aparte: un archivo que dice «esto vive en el repositorio» envejece igual que el texto. El día que el recuerdo se renombre, el puntero manda a un sitio que ya no está — y quien lo lea creerá que ahí estaba todo.

---

### Detalle de CP-003 y CP-004 — Nada se pisa, y nada se borra

| Qué se probó | Qué salió |
|---|---|
| Un recuerdo que ya existe en el repositorio, con el mismo nombre | **No se sobrescribe** |
| Dos con el mismo nombre y **contenido distinto** | El del almacén entra como `<nombre>-local.md`; **los dos quedan** |
| El almacén enlazado a la carpeta del repositorio | **No hay nada que mover**: son el mismo archivo |
| Nombres que solo difieren en mayúsculas | Se tratan como **el mismo archivo** |

**La regla es que nunca se borra: se mueve.** Y tiene una historia detrás que conviene no perder: una versión anterior **sí borraba** el archivo del almacén cuando era idéntico a uno del repositorio —«no se pierde nada, queda el del repo»— y con eso **destruyó memoria real**. Si el almacén es un enlace a la carpeta del repositorio, los dos son el mismo archivo, compararlos da idéntico siempre, y el borrado se lleva el único ejemplar.

**El caso de las mayúsculas es el transversal de límites**, y en Windows no es teórico: `MEMORY.md` y `memory.md` son el mismo archivo, y mover uno sobre otro se llevaría el índice de la memoria sin decir nada.

---

## 3. Verificaciones manuales

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Qué hay en el almacén real | Listándolo sin escribir | **Vacío**, el 2026-08-17 |
| 2 | Que el recogido nunca borre | Leyendo `recuerdos.migrar` y probándolo | Mueve; el repetido entra con sufijo |
| 3 | Que no queden dos versiones | Contando los dos lados tras recoger | 0 en el almacén, 1 en el repositorio |
| 4 | Que la suite siga verde | `python validadores/pruebas.py` | 348 pruebas · verde, con 6 fallos esperados |

---

## 4. Defectos encontrados

| ID | Severidad | Qué es | Dónde queda |
|---|---|---|---|
| D-01 | Media | El recogido **se lleva todo archivo** del almacén, no solo los recuerdos: un `config.json` acabaría en `historico-chat/memory/`. Dejarlo incumpliría `01·C19`, que exige el almacén vacío | Es el mismo `D-01` de la fase [`A-EP-006-HU-006`](../../../EP-006-memoria-de-lo-aprendido/HU-006-sacar-del-almacen-local/A-EP-006-HU-006-retrodocumentar-el-vaciado-del-almacen-local/resultado_pruebas.md), donde están las dos salidas. **Es del usuario**: toca `base/` |
| D-02 | Baja | El plan de pruebas declara cobertura completa y **no le escribe caso a los dos transversales**. Se probaron igual | El plan aprobado no se modifica. Mismo defecto de molde de las 51 fases |

**`D-01` no deja ningún CA de esta HU en «No»:** los dos criterios de aquí son que se recoja y que nada se pise, y las dos cosas ocurren. Lo que `D-01` pone en duda es qué **debería** recogerse, que es criterio de la HU-006 de EP-006.

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos | Resultado | Cumple |
|---|---|---|---|
| [CA-01](../HU-007-recoger-lo-guardado-por-fuera.md#ca-01--lo-guardado-por-fuera-se-recoge-al-abrir-sesión) | CP-001, CP-002 | Se recoge al abrir la sesión y al escribir; el almacén queda sin texto ni puntero | Sí |
| [CA-02](../HU-007-recoger-lo-guardado-por-fuera.md#ca-02--nada-se-pisa) | CP-003, CP-004 | El repetido entra al lado con sufijo; los dos quedan; nunca se borra | Sí |
| Transversal · Límites | CP-004 | Los nombres que solo difieren en mayúsculas son el mismo archivo | Sí |
| Transversal · Errores | Prueba propia, fuera del plan | Con el almacén ausente o ilegible, el recogido no falla y la sesión sigue | Sí |

**Los que no cumplen:** ninguno.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Meta | Resultado | Cumple |
|---|---|---|---|
| Cobertura de exigencias | 100% | 100% de lo que el plan contó, más los dos transversales | Sí |
| Casos ejecutados | 4 de 4 | 4 de 4 | Sí |
| Recuerdos borrados | **0** | **0** | Sí |
| Punteros que sobreviven | **0** | **0** | Sí |
| Recuerdos del almacén real tocados a mano | **0** | **0** — estaba vacío | Sí |

---

## 6. Veredicto de la fase

**Concepto:** **Cumple.**

**Justificación:** los dos criterios quedaron verificados y los dos transversales también. Lo que más se puso a prueba es el CA-02, porque es donde ya hubo daño real: una versión anterior borraba el archivo idéntico y **destruyó memoria** cuando el almacén resultó ser un enlace a la carpeta del repositorio. Hoy nunca borra —mueve, y el repetido entra con sufijo— y eso quedó probado con dos recuerdos de mismo nombre y contenido distinto.

**Qué falta para que cumpla:** nada. Queda abierto `D-01`, que no es de esta HU: qué debe hacer el recogido con lo que **no** es un recuerdo.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Casos automatizados | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clases `Recuerdos` (12) y `ElAlmacenLocalQuedaVacio` (6, escritas en `A-EP-006-HU-006`) |
| EV-02 | Lo escrito | [`documentacion/automatismos/spec.md`](../../../../automatismos/spec.md) §4.4 |
| EV-03 | Corrida completa | `python validadores/pruebas.py` — 348 pruebas, verde, 6 fallos esperados |

---

## 8. Ciclos anteriores

Ninguno: es el primero.
