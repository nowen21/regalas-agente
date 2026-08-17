# Plan de Pruebas — Fase A-EP-004-HU-008-la-corrida-completa-en-una-linea   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-004-HU-008 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-004-HU-008-la-corrida-completa-en-una-linea` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/planes/pruebas.md)).

**Esta fase construye.** Los CA-01 y CA-03 no existen hoy: no hay subcomando que corra todo ni resumen de la corrida entera. El CA-02 es lo único que ya está, y su caso existe para comprobar que **no se rompa**.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| No regresión | Que los subcomandos que ya hay sigan corriendo por separado | Este repositorio | Sí |
| Integración | Que una línea corra todo lo que aplica, y que lo que no aplica se saltee **diciendo por qué** | Este repositorio y carpetas temporales | Sí |
| Resumen | Que la corrida entera termine con un veredicto único y su código de salida | Carpetas temporales | Sí |

**Por qué el CA-02 se prueba primero.** Fija la línea base antes de tocar nada: lo que hoy funciona tiene que seguir funcionando después del cambio.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los tres CA |
| No regresión | ☑ | Los subcomandos existentes, uno por uno |
| Límites | ☑ | Comprobaciones que necesitan un proyecto real y no lo tienen |
| Legibilidad | ☑ | El resumen que se lee de un vistazo |

### 3.3 Técnicas de diseño de casos

- **Uno por uno, no una muestra** — el CA-02 se prueba corriendo **cada** subcomando por separado después del cambio. Una muestra dejaría pasar justo el que se rompió.
- **Saltar diciendo por qué** — lo que no aplica no falla ni calla. Callar es lo que hace hoy un validador sin punto de entrada, y por eso existe el pendiente [53](../../../../../pendientes/53-enlaces-py-no-tiene-punto-de-entrada.md).
- **La lista se arma de los subcomandos registrados** — el riesgo `R-03`: si se armara a mano, la corrida completa dejaría de ser completa el día que se agregue un validador. El caso comprueba que un subcomando nuevo entra solo.
- **El detalle sobrevive al total** — el resumen único **no reemplaza** las salidas de cada comprobación: quien corre para arreglar necesita el detalle, y el total es para saber si se puede cerrar.
- **Distinguir lo propio de lo heredado** — el riesgo `R-02`: el resumen separa las fallas del cambio de las que ya estaban, o la corrida completa queda siempre en rojo y nadie la mira.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/pruebas.py` entera —se toca `validar.py`, que es el punto de entrada de todo— más cada subcomando por separado sobre este repositorio.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-008 | [CA-01](../HU-008-corrida-completa.md#ca-01--una-sola-línea-corre-todo) | [CP-002](#cp-002--una-línea-corre-todo-lo-que-aplica), [CP-003](#cp-003--lo-que-no-aplica-se-saltea-diciendo-por-qué) | Integración | Crítica | Sí | ☐ |
| HU-008 | [CA-02](../HU-008-corrida-completa.md#ca-02--se-puede-correr-una-sola) | [CP-001](#cp-001--cada-subcomando-sigue-corriendo-por-separado) | No regresión | Crítica | Sí | ☐ |
| HU-008 | [CA-03](../HU-008-corrida-completa.md#ca-03--el-resultado-de-la-corrida-es-uno-solo) | [CP-004](#cp-004--la-corrida-termina-con-un-resumen-único), [CP-005](#cp-005--una-falla-en-cualquier-comprobación-deja-la-corrida-en-1) | Funcional | Crítica | Sí | ☐ |
| HU-008 | RNF — que la corrida se pueda leer de un vistazo | [CP-004](#cp-004--la-corrida-termina-con-un-resumen-único) | Legibilidad | Media | No | ☐ |

**Cobertura:** 3 de 3 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — Cada subcomando sigue corriendo por separado

| Campo | Valor |
|---|---|
| **HU / CA** | HU-008 / CA-02 |
| **Tipo** | No regresión |
| **Prioridad** | Crítica |
| **Precondiciones** | Ninguna. **Se corre antes de tocar `validar.py`** |
| **Datos de entrada** | Todos los subcomandos registrados |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Listar los subcomandos registrados | Queda la lista, con su número y la fecha |
| 2 | Correr cada uno por separado, **antes** del cambio | Queda la línea base: qué dio cada uno |
| 3 | Aplicar el cambio de `validar.py` | Queda aplicado |
| 4 | Correr cada uno otra vez, uno por uno | Ninguno cambió de comportamiento |
| 5 | Comparar contra la línea base del paso 2 | Coinciden |

**Resultado esperado final:** agregar la corrida completa no le quita a nadie la corrida de a una.

> **El paso 4 recorre todos, no una muestra.** Una muestra dejaría pasar justo el que se rompió.

---

### CP-002 — Una línea corre todo lo que aplica

| Campo | Valor |
|---|---|
| **HU / CA** | HU-008 / CA-01 |
| **Tipo** | Integración |
| **Prioridad** | Crítica |
| **Precondiciones** | Duda 1 resuelta: si las comprobaciones lentas entran o van aparte |
| **Datos de entrada** | Este repositorio |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr la línea única | Corre hasta el final |
| 2 | Comprobar qué comprobaciones se ejecutaron | Todas las que aplican, según lo que decidió la duda 1 |
| 3 | Comparar contra la lista de subcomandos registrados | Ninguno queda fuera sin motivo |
| 4 | Registrar un subcomando nuevo de mentira y volver a correr | Entra solo, sin tocar ninguna lista a mano |

**Resultado esperado final:** la corrida completa es completa hoy y el día que se agregue un validador.

> **El paso 4 es el que la mantiene completa.** Una lista escrita a mano envejece con el primer validador nuevo.

---

### CP-003 — Lo que no aplica se saltea diciendo por qué

| Campo | Valor |
|---|---|
| **HU / CA** | HU-008 / CA-01 |
| **Tipo** | Límites |
| **Prioridad** | Alta |
| **Precondiciones** | Carpeta temporal con un proyecto al que le falta lo que alguna comprobación necesita |
| **Datos de entrada** | Ese proyecto incompleto |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr la línea única sobre el proyecto incompleto | Corre hasta el final, sin excepción |
| 2 | Comprobar qué comprobaciones se saltearon | Cada una con su motivo dicho |
| 3 | Comprobar que ninguna se salteó **en silencio** | Ninguna |
| 4 | Comprobar que ninguna falló por faltarle el proyecto | Ninguna: saltar no es fallar |
| 5 | Completar el proyecto y volver a correr | Ahora se ejecutan: la diferencia es lo que faltaba |

**Resultado esperado final:** el silencio deja de ser una forma de pasar.

---

### CP-004 — La corrida termina con un resumen único

| Campo | Valor |
|---|---|
| **HU / CA** | HU-008 / CA-03 y RNF |
| **Tipo** | Funcional |
| **Prioridad** | Crítica |
| **Precondiciones** | El CP-002 corrido |
| **Datos de entrada** | La salida de la corrida completa |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr la línea única y leer el final de la salida | Hay un resumen |
| 2 | Comprobar que dice cuántas fallas y cuántos avisos | Los dos números |
| 3 | Comprobar que dice qué comprobaciones se saltearon | Con su motivo |
| 4 | Comprobar que las salidas de cada comprobación **siguen** apareciendo | Siguen: el total no reemplaza el detalle |
| 5 | Comprobar que el resumen distingue las fallas nuevas de las heredadas | Las distingue, con su cuenta |

**Resultado esperado final:** se sabe si se puede cerrar sin leer 24 resúmenes, y sin perder el detalle para arreglar.

---

### CP-005 — Una falla en cualquier comprobación deja la corrida en 1

| Campo | Valor |
|---|---|
| **HU / CA** | HU-008 / CA-03 |
| **Tipo** | Funcional |
| **Prioridad** | Crítica |
| **Precondiciones** | Carpeta temporal donde provocar una falla controlada |
| **Datos de entrada** | Un proyecto con una sola falla, provocada en comprobaciones distintas |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Provocar una falla en la primera comprobación de la lista y correr | Código de salida 1 |
| 2 | Provocar una en la última y correr | Código de salida 1 |
| 3 | Correr sobre un proyecto sin fallas y con avisos | Código de salida 0 |
| 4 | Comprobar que en el paso 1 la corrida **siguió** hasta el final | Siguió: una falla no corta el resto |
| 5 | Borrar las carpetas temporales | No queda rastro |

**Resultado esperado final:** el veredicto de la corrida entera es uno, y no depende de dónde cayó la falla.

> **El paso 4 importa tanto como el código de salida.** Una corrida que se corta en la primera falla obliga a repetirla una vez por defecto.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que un subcomando deje de correr por separado | Inmediato. El CA-02 queda en «No» |
| **Crítica** | Que una comprobación se saltee en silencio | Inmediato — es el defecto que el pendiente [53](../../../../../pendientes/53-enlaces-py-no-tiene-punto-de-entrada.md) ya documenta |
| **Alta** | Que la corrida completa tarde tanto que nadie la use (riesgo `R-01`) | Es la duda 1: lo lento se separa o se declara aparte |
| **Alta** | Que la corrida quede siempre en rojo por fallas heredadas (riesgo `R-02`) | El resumen las distingue de las propias, con su cuenta |
| **Media** | Que la lista de qué aplica se arme a mano (riesgo `R-03`) | Se arma de los subcomandos registrados; el CP-002 paso 4 lo comprueba |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 3 CA y los RNF con caso |
| Casos ejecutados | 5 de 5 |
| Subcomandos que cambiaron de comportamiento | **0** |
| Comprobaciones salteadas sin motivo dicho | **0** |
| Listas de comprobaciones escritas a mano | **0** |
| Pruebas de la suite | Las de la línea base, más las nuevas, todas en verde |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
