# Plan de Pruebas — Fase A-EP-005-HU-010-el-capitulo-llega-al-escribir-el-archivo   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-005-HU-010 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-005-HU-010-el-capitulo-llega-al-escribir-el-archivo` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/ciclo-vida-proyectos/08-plan-pruebas.md)).

**El CA-02 decide si esto se puede vivir.** El arranque ya pesa; repetir capítulos en cada escritura haría inutilizable la sesión.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Entrega | Que al escribir un documento llegue el capítulo que lo rige | Carpeta temporal | Sí |
| No repetición | Que lo ya entregado en la sesión no vuelva | Carpeta temporal | Sí |
| Silencio | Que lo que no le toca no entregue nada | Carpeta temporal | Sí |
| Robustez | Que un fallo de la entrega no tumbe la comprobación de enlaces | Carpeta temporal | Sí |

**De dónde sale la relación documento → capítulo.** De una **tabla declarada**, no del nombre del archivo: adivinar por el nombre falla con los documentos que no siguen la convención, y el estándar ya tiene varios.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los tres CA |
| Negativa | ☑ | El CA-03: lo que no le toca **no** entrega |
| Rendimiento | ☑ | Cuánto suma la entrega a la sesión |
| Recuperación | ☑ | Que los enlaces se comprueben aunque la entrega falle |

### 3.3 Técnicas de diseño de casos

- **Se mide cuánto pesa** — el riesgo `R-01`: el caso del CA-02 no solo comprueba que no se repita: **anota cuánto suma** la entrega. Un número, no una impresión.
- **El documento que no está en la tabla** — el riesgo `R-02`: no entrega nada y **se reporta como hueco**, en vez de adivinar un capítulo. Adivinar mal es peor que no entregar.
- **La entrega rota, a propósito** — el riesgo `R-03`: se rompe la entrega y se comprueba que los enlaces se siguen comprobando. Perder algo que funciona por algo que no es el peor cambio posible.
- **Dos documentos distintos, dos capítulos distintos** — el caso del CA-01 usa un plan de trabajo y una regla: si entregara el mismo capítulo a los dos, no estaría eligiendo.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/pruebas.py` entera —se toca el enganche que corre en cada escritura— y los casos en carpetas temporales.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-010 | [CA-01](../HU-010-la-regla-llega-al-escribir-el-archivo.md#ca-01--al-escribir-el-documento-llega-su-capítulo) | [CP-001](#cp-001--cada-documento-recibe-el-capítulo-que-lo-rige), [CP-002](#cp-002--el-documento-que-no-está-en-la-tabla-no-recibe-nada-y-se-reporta) | Funcional | Alta | Sí | ☐ |
| HU-010 | [CA-02](../HU-010-la-regla-llega-al-escribir-el-archivo.md#ca-02--no-se-repite-lo-que-ya-llegó) | [CP-003](#cp-003--lo-ya-entregado-no-vuelve-y-se-mide-cuánto-suma) | Rendimiento | Crítica | Sí | ☐ |
| HU-010 | [CA-03](../HU-010-la-regla-llega-al-escribir-el-archivo.md#ca-03--lo-que-no-le-toca-no-dispara-nada) | [CP-004](#cp-004--lo-que-no-es-documento-del-proyecto-no-entrega-nada) | Negativa | Alta | Sí | ☐ |
| HU-010 | RNF — que la sesión no se llene de repeticiones | [CP-003](#cp-003--lo-ya-entregado-no-vuelve-y-se-mide-cuánto-suma), [CP-005](#cp-005--si-la-entrega-falla-los-enlaces-se-comprueban-igual) | Recuperación | Crítica | Sí | ☐ |

**Cobertura:** 3 de 3 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — Cada documento recibe el capítulo que lo rige

| Campo | Valor |
|---|---|
| **HU / CA** | HU-010 / CA-01 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Dudas 1 y 2 resueltas: la tabla, y si llega el capítulo o solo la regla |
| **Datos de entrada** | Un plan de trabajo y una regla del estándar |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir un plan de trabajo | Llega el capítulo de flujo |
| 2 | Escribir una regla del estándar | Llega el de meta-reglas |
| 3 | Comprobar que los dos capítulos son **distintos** | Lo son: la entrega elige |
| 4 | Comprobar que llegó lo que decidió la duda 2 | El capítulo completo, o solo la regla |
| 5 | Comprobar que la relación salió de la tabla, no del nombre del archivo | De la tabla |

**Resultado esperado final:** la regla que rige lo que se escribe llega mientras se escribe, sin que nadie tenga que acordarse de abrirla.

---

### CP-002 — El documento que no está en la tabla no recibe nada, y se reporta

| Campo | Valor |
|---|---|
| **HU / CA** | HU-010 / CA-01 |
| **Tipo** | Límites |
| **Prioridad** | Alta |
| **Precondiciones** | El CP-001 corrido |
| **Datos de entrada** | Un documento del proyecto que no está en la tabla |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir el documento que no está en la tabla | No entrega ningún capítulo |
| 2 | Comprobar que **no adivinó** uno por el nombre | No adivinó |
| 3 | Comprobar que queda reportado como hueco de la tabla | Reportado |
| 4 | Agregarlo a la tabla y volver a escribir | Ahora entrega |

**Resultado esperado final:** una tabla incompleta se nota, en vez de producir entregas equivocadas.

> **Adivinar mal es peor que no entregar.** Un capítulo equivocado se lee y se aplica.

---

### CP-003 — Lo ya entregado no vuelve, y se mide cuánto suma

| Campo | Valor |
|---|---|
| **HU / CA** | HU-010 / CA-02 y RNF |
| **Tipo** | Rendimiento |
| **Prioridad** | Crítica |
| **Precondiciones** | El CP-001 corrido |
| **Datos de entrada** | Dos escrituras del mismo tipo de documento, en la misma sesión |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir el primer plan de trabajo | Llega el capítulo |
| 2 | Escribir un segundo plan de trabajo en la misma sesión | **No** vuelve a llegar |
| 3 | Escribir una regla | Llega su capítulo, que es otro |
| 4 | Medir cuánto sumó la entrega a la sesión, en total | Queda el número anotado |
| 5 | Comparar contra lo que pesa el arranque hoy | Se ve si es vivible |

**Resultado esperado final:** la entrega ayuda sin encarecer la sesión, y hay un número para decidirlo.

> **El paso 4 es lo que convierte una impresión en un dato.** «No parece mucho» no alcanza para una entrega que ocurre en cada escritura.

---

### CP-004 — Lo que no es documento del proyecto no entrega nada

| Campo | Valor |
|---|---|
| **HU / CA** | HU-010 / CA-03 |
| **Tipo** | Negativa |
| **Prioridad** | Alta |
| **Precondiciones** | Carpeta temporal |
| **Datos de entrada** | Un archivo que no es documento del proyecto |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir el archivo que no es documento | No entrega nada |
| 2 | Comprobar que el enganche **corrió** y decidió no entregar | Corrió |
| 3 | Comprobar que las comprobaciones de enlaces siguieron su comportamiento de siempre | Sin cambios |
| 4 | Escribir uno que sí es documento | Ahora sí entrega: la diferencia es qué archivo es |

**Resultado esperado final:** la entrega no se vuelve ruido en cada escritura del proyecto.

---

### CP-005 — Si la entrega falla, los enlaces se comprueban igual

| Campo | Valor |
|---|---|
| **HU / CA** | HU-010 / RNF |
| **Tipo** | Recuperación |
| **Prioridad** | Crítica |
| **Precondiciones** | Carpeta temporal |
| **Datos de entrada** | La entrega rota a propósito, y un documento con un enlace roto |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Romper la entrega del capítulo | Queda rota |
| 2 | Escribir un documento con un enlace roto | El aviso del enlace **llega igual** |
| 3 | Comprobar que queda dicho que la entrega falló | Queda dicho |
| 4 | Comprobar que la escritura se completó | Se completó |
| 5 | Arreglar la entrega y repetir | Llegan las dos cosas |

**Resultado esperado final:** lo nuevo no se lleva puesto lo que ya funcionaba.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que un fallo de la entrega tumbe la comprobación de enlaces (riesgo `R-03`) | Inmediato. Se pierde algo que ya funcionaba |
| **Crítica** | Que la entrega se repita en cada escritura (riesgo `R-01`) | Inmediato — la sesión se vuelve inutilizable |
| **Alta** | Que se entregue un capítulo equivocado por adivinar del nombre (riesgo `R-02`) | Inmediato: un capítulo equivocado se lee y se aplica |
| **Media** | Que la tabla quede incompleta | Se reporta como hueco; llenarla lo decide quien mantiene el estándar |
| **Baja** | Que la entrega sume más de lo esperado | Se anota el número y se decide |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 3 CA y los RNF con caso |
| Casos ejecutados | 5 de 5 |
| Capítulos entregados dos veces en la misma sesión | **0** |
| Capítulos entregados por adivinar del nombre | **0** |
| Comprobaciones de enlaces perdidas por un fallo de la entrega | **0** |
| Cuánto suma la entrega a la sesión | Medido y anotado |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
