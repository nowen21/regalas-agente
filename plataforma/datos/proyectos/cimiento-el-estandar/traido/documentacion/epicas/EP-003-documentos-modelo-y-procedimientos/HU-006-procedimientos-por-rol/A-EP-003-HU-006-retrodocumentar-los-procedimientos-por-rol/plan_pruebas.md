# Plan de Pruebas — Fase A-EP-003-HU-006-retrodocumentar-los-procedimientos-por-rol   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-003-HU-006 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-003-HU-006-retrodocumentar-los-procedimientos-por-rol` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/ciclo-vida-proyectos/08-plan-pruebas.md)).

**Ningún procedimiento se corrige acá.** Lo que les falte se numera como hueco, que es el paso 5 del procedimiento de [retro-documentación](../../../../../base/13-documentacion/retrodocumentacion.md).

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Lectura de los procedimientos | Que cada uno declare qué recibe y qué entrega | Lectura de [`skills/`](../../../../../skills/) | No |
| Conducta | Que sin la entrada, el procedimiento pida el dato en vez de inventarlo | Rama aparte de este repositorio | No |
| Repetibilidad | Que el mismo encargo entregue el mismo **tipo** de resultado | Rama aparte | No |

**Por qué el CA-03 se mide por tipo y no por texto.** Dos corridas nunca dan el mismo texto. Lo que tiene que repetirse es **qué documento sale y qué secciones trae**; comparar palabra por palabra daría un rojo que no significa nada.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Documento | ☑ | La tabla rol → entrada → salida sobre los diez |
| Funcional | ☑ | Los CA-02 y CA-03 |
| Negativa | ☑ | El CA-02: sin entrada, el procedimiento **no** arranca |
| Repetibilidad | ☑ | Dos corridas del mismo encargo |

### 3.3 Técnicas de diseño de casos

- **Fotografiar, no diseñar** — la tabla se levanta **leyendo** los diez procedimientos, no escribiendo la tabla ideal y comparando. Cada fila cita el párrafo que la sostiene (riesgo `R-03`); si no, sale sesgada por lo que el revisor esperaba encontrar.
- **Inventar el dato es el fallo** — el CA-02 no se cumple con que el procedimiento diga "necesito X": se cumple con que **no siga** sin X. El caso mira si el resultado se produjo igual con un dato supuesto.
- **Dos corridas del mismo encargo** — el CA-03 se prueba con un encargo real y chico, corrido dos veces. Cuál es lo decide la duda 1.
- **Huecos numerados** — arriba.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): ninguna suite automática la cubre. Lo que se corre son los procedimientos mismos, en rama aparte, y lo que se lee son los diez archivos de `skills/`.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-006 | [CA-01](../HU-006-procedimientos-por-rol.md#ca-01--cada-rol-tiene-su-procedimiento-con-entrada-y-salida-declaradas) | [CP-001](#cp-001--cada-procedimiento-declara-qué-recibe-y-qué-entrega) | Documento | Alta | No | ☐ |
| HU-006 | [CA-02](../HU-006-procedimientos-por-rol.md#ca-02--sin-la-entrada-el-procedimiento-no-arranca) | [CP-002](#cp-002--sin-la-entrada-el-procedimiento-pide-el-dato-y-no-sigue) | Negativa | Crítica | No | ☐ |
| HU-006 | [CA-03](../HU-006-procedimientos-por-rol.md#ca-03--el-mismo-encargo-da-el-mismo-tipo-de-resultado) | [CP-003](#cp-003--el-mismo-encargo-corrido-dos-veces-da-el-mismo-tipo-de-salida) | Repetibilidad | Alta | No | ☐ |
| HU-006 | RNF — que los huecos queden citables | [CP-004](#cp-004--lo-que-falta-queda-numerado-y-citable) | Documento | Media | No | ☐ |

**Cobertura:** 3 de 3 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — Cada procedimiento declara qué recibe y qué entrega

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-01 |
| **Tipo** | Documento |
| **Prioridad** | Alta |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | Los diez procedimientos de [`skills/`](../../../../../skills/) |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Listar los procedimientos que hay | Son diez, y queda el listado con su archivo |
| 2 | Por cada uno, buscar qué declara que recibe | Cada fila cita el párrafo del que salió |
| 3 | Por cada uno, buscar qué declara que entrega | Igual, con su párrafo |
| 4 | Armar la tabla rol → entrada → salida | Diez filas, ninguna deducida |
| 5 | Marcar las celdas que hubo que deducir | Son huecos, no datos |

**Resultado esperado final:** la tabla es una fotografía de lo que hay, no un diseño de lo que debería haber.

> **El paso 5 es el que hace honesta la tabla.** Sin él, lo deducido se lee igual que lo declarado, y el CA quedaría cumplido por interpretación.

---

### CP-002 — Sin la entrada, el procedimiento pide el dato y no sigue

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-02 |
| **Tipo** | Negativa |
| **Prioridad** | Crítica |
| **Precondiciones** | Rama aparte |
| **Datos de entrada** | Dos procedimientos elegidos por tener entradas distintas entre sí |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Invocar el primero sin darle su entrada | Pide el dato |
| 2 | Comprobar si produjo salida igual | **No la produjo**: pedir y seguir no cumple el CA |
| 3 | Darle la entrada e invocarlo otra vez | Ahora sí entrega |
| 4 | Repetir los tres pasos con el segundo procedimiento | Mismo comportamiento |

**Resultado esperado final:** la entrada faltante detiene, no se rellena con un supuesto.

> **El paso 2 es el CA.** Un procedimiento que avisa que le falta el dato y entrega igual es peor que uno que se detiene: entrega algo construido sobre un supuesto que nadie revisó.

---

### CP-003 — El mismo encargo corrido dos veces da el mismo tipo de salida

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-03 |
| **Tipo** | Repetibilidad |
| **Prioridad** | Alta |
| **Precondiciones** | Duda 1 resuelta: cuál es el encargo real y chico |
| **Datos de entrada** | El mismo encargo, con la misma entrada, dos veces |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr el encargo la primera vez | Sale un documento |
| 2 | Anotar qué documento es y qué secciones trae | Queda la lista de secciones |
| 3 | Correr el mismo encargo la segunda vez | Sale un documento |
| 4 | Comparar **tipo y secciones**, no el texto | Coinciden |
| 5 | Anotar la diferencia de secciones que aparezca | Queda como hallazgo del procedimiento |

**Resultado esperado final:** el procedimiento produce una forma estable, aunque el contenido cambie.

---

### CP-004 — Lo que falta queda numerado y citable

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / RNF |
| **Tipo** | Documento |
| **Prioridad** | Media |
| **Precondiciones** | El CP-001 corrido |
| **Datos de entrada** | Las celdas deducidas de la tabla |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Tomar los procedimientos con entrada o salida sin declarar | Queda la lista |
| 2 | Numerar cada hueco | Quedan citables desde otra fase |
| 3 | Comprobar que ninguno se corrigió al pasar | `skills/` sin cambios |
| 4 | Proponer la fase que los complete | Queda escrito, no ejecutado |

**Resultado esperado final:** el trabajo que falta se puede tomar después, porque quedó nombrado.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que un procedimiento entregue resultado sin su entrada, con un dato supuesto | Inmediato. El CA-02 queda en «No» |
| **Alta** | Que a varios procedimientos les falte declarar su entrada (riesgo `R-01`) | Se numeran y se propone una fase que los complete |
| **Media** | Que las dos corridas del mismo encargo den documentos distintos | Se anota como hallazgo del procedimiento |
| **Media** | Que la tabla salga sesgada por lo que se esperaba encontrar (riesgo `R-03`) | Cada fila cita su párrafo: la que no pueda citarlo es hueco |
| **Baja** | Que el CA-03 quede con evidencia leída y no medida (riesgo `R-02`) | Se acepta y se dice: lo observable es el tipo de salida |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 3 CA y los RNF con caso |
| Casos ejecutados | 4 de 4 |
| Procedimientos leídos | 10 de 10 |
| Filas de la tabla sin párrafo que las sostenga | **0** — las que no lo tengan son huecos, no filas |
| Archivos de `skills/` modificados | **0** |
| Huecos numerados | Todos los que salgan |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
