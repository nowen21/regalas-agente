# Resultado de Pruebas — Fase C-EP-003-HU-002-el-planteamiento-se-reconstruye-igual   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, caso por caso, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `C-EP-003-HU-002-el-planteamiento-se-reconstruye-igual` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), PP-C-EP-003-HU-002 v1.0 |
| **Fecha de ejecución** | 2026-08-22 |
| **Ejecutado por** | El agente |

---

## 1. Resumen de la ejecución

| Métrica | Meta del plan | Resultado |
|---|---|---|
| Exigencias con al menos un caso | 4 de 4 | 4 de 4 |
| Casos ejecutados | 6 de 6 | 6 de 6 |
| Casos en verde | 6 de 6 | 5 en verde, 1 no ejecutable |
| Marcas de `00·ID8` sumadas al molde | 0 | 0. El recuento quedó en 126, igual que antes de esta fase |

---

## 2. Ejecución caso por caso

| Caso | Qué se corrió | Qué salió | Concepto |
|---|---|---|---|
| CP-001 | Buscar en el molde el apartado del proyecto ya construido, sus fuentes, la tabla de traducción y la advertencia de auditoría | Los cuatro están, dentro del recuadro que se borra | Pasa |
| CP-002 | Buscar el campo «Cómo se levantó» y comprobar que la procedencia no se pida en otra parte | Está en la identificación, y pide el caso y las fuentes. No hay otro lugar que la pida | Pasa |
| CP-003 | Taparle el campo de procedencia a dos planteamientos y dárselos a un lector que no participó | **No ejecutable hoy:** no hay lector disponible que no haya participado. Estaba previsto en el `estado-fase` §3 | No ejecutado |
| CP-004 | Leer qué se borra y qué se conserva al llenar el molde | Dice «borrar este recuadro. **Solo este recuadro**», y que el encuadre de debajo es texto fijo | Pasa |
| CP-005 | Listar los moldes que empiezan por `01-` y buscar secciones propias de un solo caso | Hay uno solo, y las diez secciones son las mismas para los dos casos | Pasa |
| CP-006 | Recuento de marcas y comprobación de enlaces | 126, igual que antes. Sin enlaces rotos en el molde | Pasa |

---

## 3. Verificaciones manuales

**El planteamiento reconstruido de este repositorio se corrió contra el molde corregido**, que es la prueba de fuego de esta fase:

```
python validadores/validar.py plantilla prompts/cimiento-planteamiento.md
0 falla(s), 2 aviso(s)
```

Los dos avisos son secciones cuyo nombre el documento acortó, quitándoles el paréntesis explicativo del molde. No son fallas y no los introduce esta fase.

**Y esa corrida destapó un defecto**, que va en §4 como D-01: hasta hoy ese comando no resolvía el documento contra ninguna plantilla.

---

## 4. Defectos encontrados

| ID | Caso | Severidad | Qué pasó | Estado |
|---|---|---|---|---|
| D-01 | §3 | **Crítica** | El molde manda nombrar el archivo `prompts/<slug>-planteamiento.md`, y `deducir_plantilla()` solo reconocía el nombre pelado `planteamiento.md`. La comprobación construida en la fase B de EP-004 · HU-004 **no alcanzaba a ninguno** de los documentos que este molde produce | **Corregido.** Se resuelve el sufijo `-planteamiento`, y solo dentro de `prompts/` |
| D-02 | D-01 | **Crítica** | El primer arreglo aceptaba el sufijo en cualquier carpeta y para todas las claves. Medido, resolvía mal 29 documentos: cada `resultado_pruebas.md` como plan de pruebas, y las reglas terminadas en `-trabajo` como plan de trabajo | **Corregido** antes de quedarse. La regla se acotó al planteamiento dentro de `prompts/` |
| D-03 | CP-003 | Media | No hay lector disponible que no haya participado, así que la prueba con persona no se pudo correr | **Abierto.** Queda para cuando lo haya |
| D-04 | §3 | Baja | `resultado_pruebas.md` no tiene entrada en la tabla de nombres del validador, aunque tiene su propio molde | **Abierto.** Se anota; corregirlo abre una comprobación sobre 20 documentos y no cabe en esta fase |

---

## 5. Veredicto por criterio de aceptación

| Exigencia | Casos | Concepto |
|---|---|---|
| [CA-04](../HU-002-modelos-del-encargo.md#ca-04--el-modelo-de-la-necesidad-sirve-igual-para-un-proyecto-que-empieza-y-para-uno-que-ya-existe) | CP-001, CP-002, CP-004 | Cumple |
| RN-06, un solo molde | CP-005 | Cumple |
| RN-07, el encuadre es texto fijo | CP-004 | Cumple |
| No regresión | CP-006 | Cumple |

## 5.1 Lo que el plan exigía

El plan sumó una tarea en marcha, la T-05b: que el encuadre **enlace** `02·F0` en vez de copiarle la cadena. Salió de comprobar lo que otra sesión de la misma jornada había dado por bueno. La copia del molde decía «análisis → alcance → épica/HU → especificación → plan aprobado → implementación» y `02·F0` dice «planteamiento → épica → HU → especificación → plan → código». Ahora enlaza.

El CP-003 no se pudo correr y eso está dicho: es la única prueba de la fase que mide lo que de verdad importa, que un lector no distinga los dos casos. Sin él, el CA-04 se sostiene en la lectura del molde y no en el efecto sobre un lector.

---

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** las cuatro exigencias quedaron verdes, el molde sirve para los dos casos sin partirse, la procedencia tiene un solo dueño y el encuadre quedó declarado texto fijo. Los dos defectos críticos se cerraron dentro de la fase, y el segundo se cerró **antes de dejarlo** porque se midió su daño en vez de suponerlo.

**Con una salvedad que no se disimula:** el CP-003 no se ejecutó. El veredicto vale sobre lo que sí se comprobó.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | El molde corregido | [`plantillas/ciclo-vida-proyectos/01-planteamiento.md`](../../../../../plantillas/ciclo-vida-proyectos/01-planteamiento.md) |
| EV-02 | La corrida contra el planteamiento reconstruido | Este documento, §3 |
| EV-03 | El arreglo de la resolución y sus dos pruebas | [`validadores/plantillas.py`](../../../../../validadores/plantillas.py) y [`test_encuadre_de_la_plantilla.py`](../../../../../validadores/tests/test_encuadre_de_la_plantilla.py), clase `ElPlanteamientoConPrefijoSeResuelve` |
| EV-04 | Recuento de marcas | 126, sin cambio |

---

## 8. Ciclos anteriores

Ninguno.
