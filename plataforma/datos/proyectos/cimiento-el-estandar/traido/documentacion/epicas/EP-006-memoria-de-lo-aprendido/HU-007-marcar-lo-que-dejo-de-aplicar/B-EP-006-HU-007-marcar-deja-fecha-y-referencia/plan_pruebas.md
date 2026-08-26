# Plan de Pruebas — Fase B-EP-006-HU-007-marcar-deja-fecha-y-referencia   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso** — y en este molde, eso incluye los **transversales**.

| Campo | Valor |
|---|---|
| **Código** | PP-B-EP-006-HU-007 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `B-EP-006-HU-007-marcar-deja-fecha-y-referencia` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

**Condición de arranque.** Bases temporales, con la huella de la real comparada en cada caso.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Escritura | Que los tres caminos de marcar dejen su rastro | Base temporal | Sí |
| Lectura | Que desde la marcada se llegue a la que la reemplazó | Base temporal | Sí |
| No regresión | Que nada se borre y que `pendientes` liste lo mismo | Base temporal | Sí |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | El CA-01, en su mitad que faltaba |
| Trazabilidad | ☑ | El transversal que la fase A dejó en «No» |
| Límites | ☑ | La señal marcada **antes** del cambio |
| No regresión | ☑ | Los cinco estados, el conteo y `pendientes` |

### 3.3 Técnicas de diseño de casos

- **Se comprueba lo que queda en la base, no lo que se imprime.** El defecto era justamente que la consola lo decía y nadie lo guardaba.
- **El enlace se comprueba en los dos sentidos.** La fase A midió que solo funcionaba uno.
- **Hay un caso que comprueba que algo NO pasa:** que las señales marcadas antes del cambio **sigan sin fecha**. Rellenarlas con hoy sería inventar cuándo se marcaron, y es la clase de arreglo que parece prolijo y falsea la historia.
- **Base temporal siempre**, con la huella de la real comparada.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `memoria/pruebas.py` entera.

---

## 5. Matriz de trazabilidad

| HU | Exigencia | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-007 | [CA-01](../HU-007-marcar-lo-que-dejo-de-aplicar.md#ca-01--lo-que-dejó-de-aplicar-queda-marcado-y-visible) | [CP-001](#cp-001--la-reemplazada-dice-cuál-la-reemplazó-y-cuándo) | Funcional | Crítica | Sí | ☐ |
| HU-007 | **Transversal · Trazabilidad** | [CP-002](#cp-002--los-tres-caminos-de-marcar-dejan-su-fecha) | Trazabilidad | Crítica | Sí | ☐ |
| HU-007 | **Transversal · No regresión** | [CP-003](#cp-003--marcar-sigue-sin-alterar-el-contenido-y-sin-borrar), [CP-005](#cp-005--pendientes-lista-lo-mismo-que-antes) | Regresión | Crítica | Sí | ☐ |
| HU-007 | Límites | [CP-004](#cp-004--la-señal-marcada-antes-del-cambio-sigue-sin-fecha) | Límites | Alta | Sí | ☐ |
| HU-007 | [CA-02](../HU-007-marcar-lo-que-dejo-de-aplicar.md#ca-02--lo-marcado-no-se-confunde-con-lo-vigente) | [CP-005](#cp-005--pendientes-lista-lo-mismo-que-antes) | Regresión | Alta | Sí | ☐ |

**Cobertura:** los dos CA, **los dos transversales** y los límites = 100%.

---

## 6. Casos de prueba

### CP-001 — La reemplazada dice cuál la reemplazó, y cuándo

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-007 / CA-01 |
| **Tipo** | Funcional · **Prioridad** Crítica |
| **Precondiciones** | Base temporal con dos señales |
| **Datos de entrada** | Una vieja y una nueva que la reemplaza |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Reemplazar la vieja por la nueva | Queda marcada |
| 2 | Leer la fila de la **vieja** | Dice cuál la reemplazó |
| 3 | Comprobar que dice **cuándo** | Trae la fecha de hoy |
| 4 | Comprobar que desde la **nueva** se llega a la vieja | Se llega |
| 5 | Contar el total antes y después | El mismo: nada se borró |

**Resultado esperado final:** el enlace funciona en los dos sentidos, y el dato vive en la base, no en la consola.

> **El paso 2 es la prueba de la fase A, destapada.** Si no pasa, el arreglo no era el que faltaba.

---

### CP-002 — Los tres caminos de marcar dejan su fecha

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-007 / **Transversal · Trazabilidad** |
| **Tipo** | Trazabilidad · **Prioridad** Crítica |
| **Precondiciones** | Base temporal con tres señales |
| **Datos de entrada** | Una para archivar, una para reemplazar y una para cerrar |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Archivar la primera | Deja fecha |
| 2 | Reemplazar la segunda | Deja fecha y referencia |
| 3 | Cerrar la tercera | Deja fecha y referencia, como antes |
| 4 | Comprobar que las tres dicen **qué** les pasó | El estado lo dice: archivada, reemplazada, cerrada |
| 5 | Comprobar que el estado y la fecha son datos distintos | La fecha dice **cuándo**, no qué |

**Resultado esperado final:** de cualquier señal marcada se sabe qué le pasó y cuándo.

> **El paso 5 responde al riesgo `R-01`:** reutilizar `cerrada_en` para los tres no confunde «cerrada» con «archivada», porque **quien dice qué pasó es el estado**.

---

### CP-003 — Marcar sigue sin alterar el contenido, y sin borrar

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-007 / Transversal · No regresión |
| **Tipo** | Regresión · **Prioridad** Crítica |
| **Precondiciones** | Base temporal |
| **Datos de entrada** | Una señal completa |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Guardar los siete campos de contenido | Quedan |
| 2 | Archivar | Se marca |
| 3 | Comparar los siete campos | Idénticos |
| 4 | Repetir con reemplazar | Idénticos |
| 5 | Contar el total en todo el recorrido | El mismo |

**Resultado esperado final:** agregar la fecha no toca nada más.

---

### CP-004 — La señal marcada antes del cambio sigue sin fecha

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-007 / Límites |
| **Tipo** | Límites · **Prioridad** Alta |
| **Precondiciones** | Base temporal con una señal marcada **a mano**, sin fecha, como quedaban antes |
| **Datos de entrada** | Una fila con `estado='archivada'` y `cerrada_en` vacío |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr la migración | No falla |
| 2 | Leer la fila | **Sigue sin fecha** |
| 3 | Comprobar que nada la rellenó con hoy | Nada |
| 4 | Marcar una señal nueva | Esa **sí** trae fecha |

**Resultado esperado final:** lo que no se sabe se queda vacío.

> **El paso 3 es el que importa.** Rellenar con hoy sería **inventar** cuándo se marcó, y el resultado se vería más prolijo y sería falso. Vacío dice la verdad: no se sabe.

---

### CP-005 — `pendientes` lista lo mismo que antes

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-007 / CA-02 y no regresión |
| **Tipo** | Regresión · **Prioridad** Crítica |
| **Precondiciones** | Base temporal con deuda y preguntas abiertas, y con señales marcadas |
| **Datos de entrada** | Las mismas de la fase A |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Listar lo pendiente | Solo la deuda y las preguntas **activas** |
| 2 | Archivar una deuda y volver a listar | Ya no aparece |
| 3 | Comprobar que el filtro sigue siendo por **estado**, no por fecha | Lo sigue siendo |
| 4 | Comprobar que la búsqueda deja fuera los cuatro estados no vigentes | Los deja |

**Resultado esperado final:** llenar la fecha en más filas no cambió ninguna consulta.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que la prueba toque la base real | Inmediato. Se detiene y se restaura |
| **Alta** | Que se rellene con hoy una señal marcada antes (riesgo `R-03`) | Inmediato: falsea historia |
| **Media** | Que `pendientes` cambie de resultado (riesgo `R-02`) | Se diagnostica antes de cerrar |
| **Baja** | Que otra sesión esté tocando `memoria/` | Se guarda solo lo propio |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los dos CA, **los dos transversales** y los límites |
| Casos ejecutados | 5 de 5 |
| Caminos de marcar que no dejan fecha | **0** de 3 |
| Señales viejas rellenadas con una fecha inventada | **0** |
| Señales borradas en todo el recorrido | **0** |
| Migraciones necesarias | **0** |
| Pruebas con fallo esperado en la clase, al cerrar | **0** |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
