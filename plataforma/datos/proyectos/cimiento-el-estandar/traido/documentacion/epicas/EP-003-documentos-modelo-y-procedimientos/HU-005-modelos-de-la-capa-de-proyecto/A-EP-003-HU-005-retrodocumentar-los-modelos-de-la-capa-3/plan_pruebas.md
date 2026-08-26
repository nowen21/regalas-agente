# Plan de Pruebas — Fase A-EP-003-HU-005-retrodocumentar-los-modelos-de-la-capa-3   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-003-HU-005 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-003-HU-005-retrodocumentar-los-modelos-de-la-capa-3` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/ciclo-vida-proyectos/08-plan-pruebas.md)).

**Nada se rompe en un proyecto vivo.** Las declaraciones mal escritas se arman en carpeta temporal: romper a propósito la capa 3 de un proyecto real es tocar trabajo ajeno.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Documento | Que cada dato de la capa 3 tenga un solo modelo dueño | Lectura de `plantillas/` | No |
| Unitario | Que una declaración mal escrita se detecte y una bien escrita se lea entera | Carpeta temporal | Sí |
| Silencio del revisor | Que lo que nadie declaró no se exija | Carpeta temporal | Sí |

**Cómo se prueba un silencio sin falso verde.** La prueba comprueba que el revisor **corrió** y no dijo nada, no que no corrió (riesgo `R-02`). Sin esa distinción, un programa roto pasaría el caso.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los tres CA |
| Negativa | ☑ | La declaración mal escrita tiene que salir detectada |
| Documento | ☑ | El solape entre los tres modelos |
| No regresión | ☑ | La suite que ya existe, contra su número anotado antes |

### 3.3 Técnicas de diseño de casos

- **Solape por dato, no por sección** — lo que no puede repetirse es el **dato del que hay una sola verdad**. Dos modelos con secciones parecidas no molestan; dos modelos que declaran el mismo dato se contradicen tarde o temprano.
- **El par mal escrita / bien escrita** — el CA-02 se cierra con los dos lados. Sin el segundo, el caso pasaría con un lector que rechaza todo.
- **Declaración a medias** — el CA-03 se prueba también con el dominio declarado **parcialmente**: se exige por lo declarado y se calla por el resto. Es el caso que distingue "no exige nada" de "exige solo lo suyo".
- **Copia, no proyecto vivo** — arriba.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/pruebas.py` entera y `validar.py declaracion` sobre las capas 3 de mentira.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-005 | [CA-01](../HU-005-modelos-de-la-capa-de-proyecto.md#ca-01--los-tres-modelos-existen-y-no-se-pisan) | [CP-001](#cp-001--cada-dato-de-la-capa-3-tiene-un-solo-modelo-dueño) | Documento | Alta | No | ☐ |
| HU-005 | [CA-02](../HU-005-modelos-de-la-capa-de-proyecto.md#ca-02--lo-que-un-programa-lee-tiene-forma-fija) | [CP-002](#cp-002--la-declaración-mal-escrita-se-detecta-y-la-bien-escrita-se-lee-entera) | Negativa | Crítica | Sí | ☐ |
| HU-005 | [CA-03](../HU-005-modelos-de-la-capa-de-proyecto.md#ca-03--lo-no-declarado-no-se-comprueba) | [CP-003](#cp-003--sin-declaración-de-stack-el-revisor-corre-y-calla), [CP-004](#cp-004--con-el-dominio-declarado-a-medias-se-exige-solo-por-lo-declarado) | Funcional | Alta | Parcial | ☐ |
| HU-005 | RNF — que la capa 3 se pueda leer sin el código | [CP-001](#cp-001--cada-dato-de-la-capa-3-tiene-un-solo-modelo-dueño) | Documento | Media | No | ☐ |

**Cobertura:** 3 de 3 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — Cada dato de la capa 3 tiene un solo modelo dueño

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-01 y RNF |
| **Tipo** | Documento |
| **Prioridad** | Alta |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | [`stack.md`](../../../../../plantillas/stack.md), [`dominio.md`](../../../../../plantillas/dominio.md) y [`mapeo-nombres.md`](../../../../../plantillas/mapeo-nombres.md) |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Listar los datos que pide cada modelo | Queda la lista, con su modelo |
| 2 | Marcar los que aparecen en más de uno | Queda el subconjunto de candidatos |
| 3 | Por cada candidato, decidir si es el mismo dato o dos distintos con nombre parecido | Cada uno con su veredicto y el párrafo que lo sostiene |
| 4 | Anotar el que tenga dos dueños de verdad | Queda numerado; cambiar un modelo sube versión y se propone |
| 5 | Comprobar que los tres modelos se entienden sin abrir el código del proyecto | Se entienden |

**Resultado esperado final:** hay una sola verdad por dato, o queda dicho dónde hay dos.

> **El paso 3 es el que evita el falso positivo.** «Nombre del módulo» en dos modelos puede ser el mismo dato o dos cosas distintas; lo decide leer, no coincidir.

---

### CP-002 — La declaración mal escrita se detecta, y la bien escrita se lee entera

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-02 |
| **Tipo** | Negativa |
| **Prioridad** | Crítica |
| **Precondiciones** | Carpeta temporal con capas 3 de mentira |
| **Datos de entrada** | Una declaración de dominio bien escrita y varias mal escritas de maneras distintas |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr el lector sobre la declaración bien escrita | La lee entera: todos los módulos y su especificación |
| 2 | Correr sobre una con la forma rota | La detecta, y el mensaje dice qué está mal |
| 3 | Repetir con las otras formas de romperla | Todas se detectan |
| 4 | Comprobar que ninguna corrida escribió en la carpeta | Ningún archivo modificado |
| 5 | Borrar la carpeta temporal | No queda rastro |

**Resultado esperado final:** un programa puede confiar en la forma, porque la forma se comprueba.

---

### CP-003 — Sin declaración de stack, el revisor corre y calla

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-03 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Carpeta temporal con un proyecto sin `stack.md` |
| **Datos de entrada** | El proyecto sin declaración de stack |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr el revisor sobre el proyecto sin stack declarado | Corre hasta el final, sin excepción |
| 2 | Comprobar que **corrió** —no que se saltó— | Queda evidencia de que la comprobación se ejecutó |
| 3 | Comprobar que no exigió nada de ningún stack | Ningún hallazgo sobre tecnología que nadie nombró |
| 4 | Declarar un stack y volver a correr | Ahora sí exige por él: la diferencia es la declaración |

**Resultado esperado final:** el silencio es una decisión, no un programa que no llegó a mirar.

> **Los pasos 2 y 4 son los que evitan el falso verde.** Sin ellos, un revisor roto pasaría este caso perfectamente.

---

### CP-004 — Con el dominio declarado a medias, se exige solo por lo declarado

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-03 |
| **Tipo** | Límites |
| **Prioridad** | Alta |
| **Precondiciones** | Carpeta temporal |
| **Datos de entrada** | Un dominio con dos módulos declarados y un tercero que existe pero no está declarado |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr el revisor | Exige por los dos declarados |
| 2 | Comprobar qué dice del tercero | No dice nada |
| 3 | Declarar el tercero y volver a correr | Ahora también exige por él |

**Resultado esperado final:** declarar es lo que enciende la exigencia, y declarar a medias no rompe el resto.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que una declaración mal escrita se lea sin error | Inmediato. El CA-02 queda en «No» |
| **Alta** | Que el revisor exija por algo que nadie declaró | Inmediato — rompe el criterio de toda la comprobación automática |
| **Media** | Que un dato tenga dos dueños entre los tres modelos (riesgo `R-01`) | Se anota y se propone: cambiar un modelo sube versión |
| **Media** | Que la prueba del silencio pase por no mirar (riesgo `R-02`) | Se corrige el caso antes de dar el CA por bueno |
| **Baja** | Que otra sesión esté tocando la especificación del módulo | Se relee justo antes de escribir |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 3 CA y los RNF con caso |
| Casos ejecutados | 4 de 4 |
| Datos con dos modelos dueños | **0**, o todos anotados |
| Formas de romper la declaración probadas | Al menos 3, todas detectadas |
| Capas 3 de proyectos vivos modificadas | **0** |
| Pruebas de la suite | Las de la línea base, más 2, todas en verde |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
