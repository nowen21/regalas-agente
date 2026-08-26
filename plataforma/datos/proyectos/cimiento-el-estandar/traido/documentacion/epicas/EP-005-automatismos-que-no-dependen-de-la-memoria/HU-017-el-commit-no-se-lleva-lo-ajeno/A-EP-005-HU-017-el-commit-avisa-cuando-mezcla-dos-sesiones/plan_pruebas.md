# Plan de Pruebas — Fase A-EP-005-HU-017, el commit avisa cuando mezcla dos sesiones   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó al correrlas va en el `resultado_pruebas.md` de la misma fase, para no perder la línea base aprobada. La lista de tareas vive en el `plan_trabajo` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-005-HU-017 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase A de HU-017, épica EP-005 |
| **Fecha** | 2026-08-22 |
| **Elaborado por** | El agente |
| **Aprobado por** | El usuario |
| **Estado** | Borrador |

**Proporcionalidad.** Una sola fase, así que van las secciones 3, 5, 6, 9 y 12.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

Unidad sobre el módulo, con carpetas temporales. Lo que entra al commit se sustituye en la prueba: depender de un repositorio de verdad la volvería lenta y frágil, y lo que se quiere probar es la decisión, no `git`.

### 3.2 Tipos de prueba

| Tipo | Para qué |
|---|---|
| Funcional positiva | Que avise cuando el commit mezcla, y que el aviso sirva para actuar |
| Funcional negativa | Que **no** avise en los cinco casos donde no hay nada que avisar |
| Límites | Sin identificador de sesión, y con un archivo de otro proyecto |

### 3.3 Técnicas de diseño de casos

**La mitad de los casos son de lo que NO tiene que avisar**, y acá esa mitad es lo que decide si la funcionalidad sirve. Un aviso que salta en el commit de todos los días se apaga en una tarde, y entonces no queda nada. Es el mismo argumento con el que se diseñó el trinquete de las marcas, y está escrito en el [pendiente 11](../../../../../pendientes/hecho/limpiar-marcadores-de-ia-del-texto-del-estandar.md).

### 3.4 Priorización

CP-001 y CP-002 son críticos: sin ellos no hay funcionalidad. CP-003 a CP-007 también, porque sin ellos la funcionalidad se apaga sola.

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

La suite propia, más las que dependen de lo que la fase toca: el instalador, que gana una línea en su `pre-commit`, y la corrida completa de `validar.py`, que gana un subcomando. **La batería entera no.**

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-017 | CA-01 | CP-001 | Funcional | Crítica | Sí | ☐ |
| HU-017 | CA-02 | CP-002 | Funcional | Crítica | Sí | ☐ |
| HU-017 | CA-03 | CP-003, CP-004, CP-005, CP-006, CP-007 | Funcional | Crítica | Sí | ☐ |
| HU-017 | Límites | CP-008, CP-009, CP-010 | No funcional | Alta | Sí | ☐ |

**Cobertura:** 4 de 4 exigencias cubiertas = 100%.

---

## 6. Casos de prueba

| ID | Título | Qué entra | Qué se espera |
|---|---|---|---|
| CP-001 | El commit que mezcla dos sesiones avisa | Dos sesiones con archivos distintos, y los dos preparados | Un aviso, con severidad de aviso y no de falla, que dice «2 sesiones» |
| CP-002 | El aviso nombra algún archivo | Lo mismo | El mensaje trae el nombre de un archivo de la sesión ajena |
| CP-003 | Una sola sesión no avisa | Dos archivos, los dos de la misma sesión | Silencio |
| CP-004 | Un commit vacío no avisa | Dos sesiones anotadas, nada preparado | Silencio |
| CP-005 | Lo ajeno que no entra al commit no avisa | Dos sesiones, pero solo se prepara lo propio | Silencio |
| CP-006 | Una sesión vieja ya no cuenta | El registro de una sesión envejecido más allá de su vigencia | Silencio |
| CP-007 | El archivo compartido no basta para callar | Las dos tocaron el índice, y cada una además lo suyo | Avisa igual: haber tocado un archivo común no vuelve propio lo demás |
| CP-008 | No se anota lo de otro proyecto | Un archivo fuera del repositorio | El registro queda vacío |
| CP-009 | Sin identificador de sesión no se anota | Una edición sin `session_id` | El registro queda vacío, y nada se rompe |
| CP-010 | El mismo archivo dos veces se anota una | La misma edición repetida | Una sola entrada |

**Un paso, una acción.** Cada caso escribe sus archivos en carpeta temporal, anota, prepara y comprueba. El detalle ejecutable vive en [`test_dos_sesiones_no_se_pisan.py`](../../../../../validadores/tests/test_dos_sesiones_no_se_pisan.py), que es la fuente; esta tabla es el índice para leerlos sin abrir el código.

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| Crítica | Avisa en un commit normal, o no avisa en el caso del 2026-08-22 |
| Alta | El aviso no dice qué sacar |
| Media | El registro crece sin límite |
| Baja | Redacción del mensaje |

### 9.2 Flujo del defecto

Se anota en el `resultado_pruebas.md` con su caso de origen. Crítico abierto, la fase no cierra.

### 9.3 Contenido mínimo de un reporte

El caso, lo que entró, qué se esperaba y qué salió.

### 9.4 Registro

En el `resultado_pruebas.md` de la fase.

---

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Meta |
|---|---|
| Exigencias con al menos un caso | 4 de 4 |
| Casos en verde | 10 de 10 |
| Casos de lo que NO debe avisar | 5 o más de 10 |
| Suites vecinas que se rompen | 0 |

### 12.2 Dónde se miden

En el `resultado_pruebas.md` de esta fase.
