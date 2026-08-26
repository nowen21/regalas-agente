# Plan de Pruebas — Fase C-EP-004-HU-012, el recuento no cuenta la notación   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó al correrlas va en el `resultado_pruebas.md` de la misma fase. La lista de tareas vive en el `plan_trabajo` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-C-EP-004-HU-012 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase C de HU-012, épica EP-004 |
| **Fecha** | 2026-08-22 |
| **Elaborado por** | El agente |
| **Aprobado por** | El usuario |
| **Estado** | Borrador |

**Proporcionalidad.** Una sola fase: van las secciones 3, 5, 6, 9 y 12.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

Unidad sobre `marcas_de_linea()`, que es donde vive la decisión, más la medición sobre el repositorio real, que es lo que dice si el criterio sirve.

### 3.2 Tipos de prueba

| Tipo | Para qué |
|---|---|
| Funcional negativa | Que las cuatro formas de notación dejen de contarse |
| Funcional positiva | Que la prosa **siga** contándose, que es lo único que puede salir mal acá |
| No regresión | Que el trinquete y el recuento no pierdan ninguna prueba |

### 3.3 Técnicas de diseño de casos

**Cada forma se prueba con su pareja.** La misma línea en su versión de notación y en su versión de prosa: el título contra el inciso, el campo con su hueco contra el campo con prosa. Sin la pareja, una expresión demasiado ancha pasa sin que nadie lo note, y entonces la regla queda escrita y sin quien la cuente.

### 3.4 Priorización

Todos críticos: si una expresión se pasa de ancha, `00·ID8` se queda sin quien la haga cumplir.

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Las dos suites que dependen del recuento: `test_las_marcas_de_ia_se_cuentan` y `test_el_trinquete_de_las_marcas`. Nada más, porque es lo único que llama a `marcas_de_linea()`.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-012 | CA-03, la notación no se cuenta | CP-001 a CP-004 | Funcional | Crítica | Sí | ☐ |
| HU-012 | CA-01, la tipografía se cuenta | CP-005 a CP-008 | Funcional | Crítica | Sí | ☐ |
| HU-012 | No regresión | CP-009, CP-010 | No funcional | Crítica | Sí | ☐ |

**Cobertura:** 3 de 3 exigencias cubiertas = 100%.

---

## 6. Casos de prueba

**Cada caso con su pareja**, que es como se comprueba que la expresión no se pasó de ancha:

| ID | Notación, no debe contar | Pareja en prosa, sí debe contar |
|---|---|---|
| CP-001 / CP-005 | Un título o un nombre de sección con raya | Un inciso entre rayas dentro de un párrafo |
| CP-002 / CP-006 | Un identificador en negrita seguido de raya y su enunciado | Un inciso entre rayas después de una palabra en negrita |
| CP-003 / CP-007 | Una celda de tabla con raya o con punto medio | Un punto medio separando dos frases de un párrafo |
| CP-004 / CP-008 | Una viñeta con negrita cuyo valor es el espacio por llenar | La misma viñeta con prosa después de los dos puntos |

| ID | Título | Qué se espera |
|---|---|---|
| CP-009 | El recuento del repositorio baja y no sube | Menos marcas que antes en todas las carpetas, en ninguna más |
| CP-010 | El trinquete sigue haciendo lo suyo | Su suite entera en verde: sigue bloqueando lo que bloqueaba |

El detalle ejecutable vive en [`test_las_marcas_de_ia_se_cuentan.py`](../../../../../validadores/tests/test_las_marcas_de_ia_se_cuentan.py).

---

## 9. Gestión de defectos

| Severidad | Qué es acá |
|---|---|
| Crítica | Deja de contarse una marca de prosa, o el trinquete se rompe |
| Alta | Una de las cuatro formas sigue contándose |
| Media | El recuento tarda más que antes |
| Baja | Redacción de los comentarios |

Se anotan en el `resultado_pruebas.md` con su caso de origen. Con un crítico abierto, la fase no cierra.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Moldes del ciclo de vida | 0 marcas |
| Marcas de prosa que dejan de contarse | 0 |
| Pruebas del recuento y del trinquete en verde | 35 de 35 |

Se miden en el `resultado_pruebas.md` de esta fase.
