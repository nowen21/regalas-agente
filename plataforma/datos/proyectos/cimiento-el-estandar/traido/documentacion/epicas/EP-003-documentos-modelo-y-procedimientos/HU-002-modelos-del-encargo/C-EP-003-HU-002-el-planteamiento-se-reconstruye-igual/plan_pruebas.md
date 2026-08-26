# Plan de Pruebas — Fase C-EP-003-HU-002, el planteamiento se reconstruye igual   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó al correrlas va en el `resultado_pruebas.md` de la misma fase, para no perder la línea base aprobada. La lista de tareas vive en el `plan_trabajo` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-C-EP-003-HU-002 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase C de HU-002, épica EP-003 |
| **Fecha** | 2026-08-22 |
| **Elaborado por** | El agente |
| **Aprobado por** | El usuario |
| **Estado** | Borrador |

**Proporcionalidad.** El formato completo del molde es para un release o una épica. Esta es una sola fase, así que van las secciones 3, 5, 6, 9 y 12, que es lo que el molde autoriza para este tamaño.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

Un solo nivel, el de aceptación documental: se lee el molde corregido y se llena con un caso real. No hay unidad ni integración porque no hay código.

### 3.2 Tipos de prueba

| Tipo | Para qué |
|---|---|
| Funcional positiva | Que el molde traiga lo que el CA-04 exige |
| Funcional negativa | Que el molde impida lo que ya falló una vez, sustituir el encuadre |
| Prueba con persona | Que un lector no distinga un planteamiento reconstruido de uno escrito antes de construir |
| No funcional | Que el molde no sume marcas de generación automática |

### 3.3 Técnicas de diseño de casos

Partición: los dos casos de uso del molde, proyecto que empieza y proyecto ya construido. El caso interesante es el segundo, que es el que hoy no existe; el primero se prueba por no regresión, porque el molde no debe cambiar para quien ya lo usaba.

### 3.4 Priorización

CP-001 a CP-004 son críticos: sin ellos el CA-04 no está cumplido. CP-005 y CP-006 son altos y se corren igual, porque miden lo que el molde le hace al resto del estándar.

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Se corre `python validadores/marcas.py --raiz plantillas/ciclo-vida-proyectos` y `python validadores/validar.py enlaces`, que son los que tocan lo que la fase cambia. El resto de la batería no se corre: la fase no toca código ni otros documentos.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-002 | [CA-04](../HU-002-modelos-del-encargo.md#ca-04--el-modelo-de-la-necesidad-sirve-igual-para-un-proyecto-que-empieza-y-para-uno-que-ya-existe) | [CP-001](#cp-001--el-molde-dice-qué-hacer-cuando-el-proyecto-ya-está-construido), [CP-002](#cp-002--la-procedencia-se-declara-una-sola-vez), [CP-003](#cp-003--el-lector-no-distingue-cuál-de-los-dos-casos-fue), [CP-004](#cp-004--intentar-sustituir-el-encuadre-queda-prohibido-por-escrito) | Funcional | Crítica | No | ☐ |
| HU-002 | RN-06 | [CP-005](#cp-005--el-molde-sigue-siendo-uno-solo) | No funcional | Alta | Sí | ☐ |
| HU-002 | RN-07 | [CP-004](#cp-004--intentar-sustituir-el-encuadre-queda-prohibido-por-escrito) | Funcional | Crítica | No | ☐ |
| HU-002 | Transversal, no regresión | [CP-006](#cp-006--el-molde-no-suma-marcas-de-generación-automática) | No funcional | Alta | Sí | ☐ |

**Cobertura:** 4 de 4 exigencias cubiertas = 100%.

---

## 6. Casos de prueba

### CP-001 — El molde dice qué hacer cuando el proyecto ya está construido

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-04 |
| **Tipo** | Funcional, camino feliz |
| **Prioridad** | Crítica |
| **Precondiciones** | El molde `plantillas/ciclo-vida-proyectos/01-planteamiento.md` con los cambios de la fase aplicados |
| **Datos de entrada** | Ninguno |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir el molde y buscar el apartado del proyecto ya construido | Está, dentro del recuadro de instrucciones |
| 2 | Leer de dónde dice que se saca la información | Nombra fuentes concretas: el README, los pedidos guardados, la documentación y el código |
| 3 | Buscar la tabla de traducción | Está, y trae las cuatro conversiones con lo que uno encuentra y lo que va escrito |
| 4 | Buscar la advertencia sobre lo construido que no cabe en el alcance | Está, y dice que se anota como hallazgo y lo decide el usuario |

**Resultado esperado final:** el molde le dice a quien reconstruye qué hacer, sin que tenga que inventarlo.

---

### CP-002 — La procedencia se declara una sola vez

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-04 |
| **Tipo** | Funcional, camino feliz |
| **Prioridad** | Crítica |
| **Precondiciones** | El molde con los cambios aplicados |
| **Datos de entrada** | Ninguno |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir la tabla de identificación del molde | Tiene el campo «Cómo se levantó» |
| 2 | Leer su marca de espacio por llenar | Pide dos cosas: el caso, entrevista o reconstrucción, y de qué fuentes |
| 3 | Buscar en el resto del molde otro lugar que pida la procedencia | No hay ninguno |

**Resultado esperado final:** la procedencia tiene un solo dueño en el documento.

---

### CP-003 — El lector no distingue cuál de los dos casos fue

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-04 |
| **Tipo** | Prueba con persona |
| **Prioridad** | Crítica |
| **Precondiciones** | El molde con los cambios aplicados |
| **Datos de entrada** | El planteamiento reconstruido de este repositorio, `prompts/cimiento-planteamiento.md`, y un planteamiento escrito antes de construir, de otro proyecto |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Tapar el campo «Cómo se levantó» de los dos documentos | Quedan las diez secciones a la vista, sin el dato |
| 2 | Dárselos a leer a alguien que no participó en ninguno de los dos | Los lee completos |
| 3 | Preguntarle cuál se escribió sobre algo ya construido | No lo puede decidir por la redacción, o se equivoca |

**Resultado esperado final:** la voz del documento es la misma en los dos casos.
**Postcondiciones:** si el lector acierta, se le pregunta con qué frase lo supo. Esa frase es el defecto y vuelve a la tabla de traducción.

---

### CP-004 — Intentar sustituir el encuadre queda prohibido por escrito

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-04 y RN-07 |
| **Tipo** | Funcional, caso negativo |
| **Prioridad** | Crítica |
| **Precondiciones** | El molde con los cambios aplicados |
| **Datos de entrada** | Un intento deliberado de llenar el molde reemplazando el encuadre por una nota de procedencia, que es lo que ya ocurrió una vez |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer en el molde qué se borra al llenarlo | Dice que se borra el recuadro de instrucciones, y solo ese |
| 2 | Buscar qué dice del renglón del encuadre | Dice que es texto fijo y que se conserva |
| 3 | Llenar el molde reemplazando el encuadre por una nota de procedencia | El documento contradice una instrucción escrita del propio molde, y quien lo revise la puede citar |

**Resultado esperado final:** sustituir el encuadre deja de ser una interpretación posible del molde.

---

### CP-005 — El molde sigue siendo uno solo

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / RN-06 |
| **Tipo** | No funcional |
| **Prioridad** | Alta |
| **Precondiciones** | La fase cerrada |
| **Datos de entrada** | Ninguno |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Listar los archivos de `plantillas/ciclo-vida-proyectos/` que empiecen por `01-` | Hay uno solo, `01-planteamiento.md` |
| 2 | Buscar dentro de él una sección que exista solo para uno de los dos casos | No hay: las diez secciones son las mismas para los dos |

**Resultado esperado final:** no nació una segunda variante del molde.

---

### CP-006 — El molde no suma marcas de generación automática

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / no regresión |
| **Tipo** | No funcional |
| **Prioridad** | Alta |
| **Precondiciones** | La fase construida y sin commitear |
| **Datos de entrada** | El recuento previo, tomado el 2026-08-22: 197 marcas en los 10 moldes del ciclo de vida |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `python validadores/marcas.py --raiz plantillas/ciclo-vida-proyectos` | Devuelve un total |
| 2 | Compararlo con el recuento previo | Es igual o menor que 197 |
| 3 | Correr `python validadores/validar.py enlaces` | Ningún enlace roto en el molde |

**Resultado esperado final:** el texto nuevo entra limpio, aunque la deuda vieja del molde siga ahí.

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| Crítica | El molde permite volver a escribir un planteamiento descriptivo, o permite sustituir el encuadre |
| Alta | Una de las cuatro traducciones falta o está mal explicada |
| Media | La redacción del molde se entiende a medias y hay que preguntar |
| Baja | Erratas, enlaces con texto impreciso |

### 9.2 Flujo del defecto

Se anota en el `resultado_pruebas.md` de esta fase con su caso de origen. Si es crítico, la fase no cierra. Si es alto o menor y se decide diferirlo, baja a `pendientes/` con su archivo, y el `resultado_pruebas` dice cuál.

### 9.3 Contenido mínimo de un reporte

El caso que lo destapó, qué se esperaba, qué pasó, y la línea del molde donde está.

### 9.4 Registro

En el `resultado_pruebas.md` de la fase. No hay herramienta de tiquetes en este proyecto.

---

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Meta |
|---|---|
| Exigencias cubiertas por al menos un caso | 4 de 4 |
| Casos ejecutados | 6 de 6 |
| Casos en verde | 6 de 6 para cerrar la fase |
| Marcas de `00·ID8` sumadas al molde | 0 |

### 12.2 Dónde se miden

En el `resultado_pruebas.md` de esta fase, que es el único documento donde se anota lo que pasó al correr.
