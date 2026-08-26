# Plan de Pruebas — Fase A-EP-006-HU-001-retrodocumentar-que-se-guarda-y-con-que-alcance   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-006-HU-001 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-006-HU-001-retrodocumentar-que-se-guarda-y-con-que-alcance` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/ciclo-vida-proyectos/08-plan-pruebas.md)).

**Condición de arranque.** Las pruebas corren sobre una **base temporal**. La base real tiene el aprendizaje del proyecto y una prueba no lo toca.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Aplicación del criterio | Que con el criterio escrito se pueda decidir qué es señal y qué no | Este repositorio, en lectura | No |
| Unitario | Que el esquema no admita una señal sin tipo, y ponga el alcance por omisión | Base temporal | Sí |
| Inventario | Qué tipos se usan de verdad y cuáles nunca | Copia de la base | Parcial |

**Con qué se prueba el criterio.** Con **decisiones reales de fases cerradas**. Las reales son las que cuesta clasificar; cinco ejemplos inventados caen siempre del lado claro y no prueban nada.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Documento | ☑ | El CA-01: el criterio aplicado a casos reales |
| Funcional | ☑ | El CA-02: el esquema rechaza y completa |
| Límites | ☑ | Señal sin tipo, sin alcance, y con un tipo que no existe |
| Inventario | ☑ | Los tipos declarados contra los usados |

### 3.3 Técnicas de diseño de casos

- **Decisiones reales, difíciles a propósito** — arriba.
- **Lo que no se pudo clasificar es el resultado** — el riesgo `R-03`: si una decisión queda ambigua, se escribe cuál y por qué. Eso dice que al criterio le falta, y es más útil que un cinco de cinco forzado.
- **Los tipos sin uso se cuentan, no se quitan** — quitar un tipo rompe las señales que ya lo tienen, y ninguna se borra. Simplificar el esquema lo decide el usuario.
- **Base temporal siempre** — arriba, y cada caso comprueba que la base real quedó intacta.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `memoria/pruebas.py` entera, sobre bases temporales.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-001 | [CA-01](../HU-001-que-se-guarda-tipos-y-alcances.md#ca-01--el-criterio-de-qué-se-guarda-está-escrito) | [CP-001](#cp-001--cinco-decisiones-reales-clasificadas-con-el-criterio) | Documento | Alta | No | ☐ |
| HU-001 | [CA-02](../HU-001-que-se-guarda-tipos-y-alcances.md#ca-02--cada-cosa-guardada-tiene-tipo-y-alcance) | [CP-002](#cp-002--la-señal-sin-tipo-no-entra-y-la-que-no-declara-alcance-entra-con-el-de-proyecto) | Funcional | Crítica | Sí | ☐ |
| HU-001 | RNF — que el criterio se pueda aplicar sin discutir cada vez | [CP-003](#cp-003--los-diez-tipos-contra-su-uso-real) | Inventario | Media | Parcial | ☐ |

**Cobertura:** 2 de 2 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — Cinco decisiones reales clasificadas con el criterio

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-01 |
| **Tipo** | Documento |
| **Prioridad** | Alta |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | Cinco decisiones tomadas en fases ya cerradas, elegidas por ser **difíciles de clasificar** |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Tomar el criterio de [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md) | Queda a la vista: lo que no se recupera leyendo el código |
| 2 | Aplicarlo a cada una de las cinco | Cada una con su veredicto: señal o no |
| 3 | Comprobar contra si esa decisión llegó a guardarse | Se ve si el criterio reproduce lo que se hizo |
| 4 | Anotar la que no se pueda clasificar, y por qué | Es hallazgo del criterio, no de la decisión |
| 5 | Si dos personas la clasificarían distinto, dejarlo escrito | Queda dicho |

**Resultado esperado final:** el criterio se puede aplicar sin discutir cada vez, o queda dicho dónde no alcanza.

> **El paso 4 vale más que un cinco de cinco.** Un criterio que no permite decidir un caso real tiene un hueco, y ocultarlo lo deja para el próximo.

---

### CP-002 — La señal sin tipo no entra, y la que no declara alcance entra con el de proyecto

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-02 |
| **Tipo** | Funcional |
| **Prioridad** | Crítica |
| **Precondiciones** | Base temporal creada desde [`memoria/esquema.sql`](../../../../../memoria/esquema.sql) |
| **Datos de entrada** | Señales sin tipo, sin alcance, y con un tipo que no existe |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Intentar guardar una señal sin tipo | No entra |
| 2 | Guardar una sin alcance | Entra, con alcance de proyecto |
| 3 | Intentar guardar una con un tipo que no existe | No entra |
| 4 | Guardar una completa | Entra, con lo que declaró |
| 5 | Comprobar que la base real no se tocó | Intacta |

**Resultado esperado final:** ninguna señal queda guardada sin saber de qué tipo es ni a qué alcanza.

> **El paso 4 es el que da valor a los tres anteriores.** Sin él, el caso pasaría con un esquema que rechaza todo.

---

### CP-003 — Los diez tipos contra su uso real

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / RNF |
| **Tipo** | Inventario |
| **Prioridad** | Media |
| **Precondiciones** | Copia de la base real, solo lectura |
| **Datos de entrada** | Los tipos declarados en el esquema y las señales guardadas |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Listar los tipos que declara el esquema | Diez |
| 2 | Contar cuántas señales hay de cada uno | Sale un número por tipo, con su fecha |
| 3 | Por cada tipo con uso, anotar un ejemplo real | Queda la tabla |
| 4 | Anotar cuál no se ha usado nunca | Queda dicho, sin quitarlo del esquema |
| 5 | Comprobar que la copia no se modificó | Sin cambios |

**Resultado esperado final:** se sabe qué parte del esquema está viva, sin romper lo que ya se guardó.

> **Los tipos sin uso no se quitan** (riesgo `R-01`): quitar uno rompería las señales que lo tienen. Simplificar el esquema lo decide el usuario.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que la prueba toque la base real (riesgo `R-02`) | Inmediato. Se detiene y se restaura: es el aprendizaje del proyecto |
| **Alta** | Que una señal sin tipo entre a la base | Inmediato. El CA-02 queda en «No» |
| **Media** | Que clasificar las cinco decisiones resulte ambiguo (riesgo `R-03`) | Es el resultado honesto: se escribe cuál no se pudo clasificar y por qué |
| **Media** | Que la mitad de los tipos no se use nunca (riesgo `R-01`) | Se anota con la cuenta; simplificar lo decide el usuario |
| **Baja** | Diferencias de criterio entre revisores | Se dejan escritas: son huecos del criterio |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 2 CA y los RNF con caso |
| Casos ejecutados | 3 de 3 |
| Señales de la base real modificadas | **0** |
| Decisiones que no se pudieron clasificar | Todas anotadas, con el motivo |
| Tipos del esquema quitados | **0** |
| Tipos sin uso | Contados, con su fecha |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
