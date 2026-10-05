# Estado de fase · Fase `A-EP-004-HU-027-el-control-avisa-las-reglas-parecidas` (módulo `proyectos/cimiento/core/validadores/` y `adaptadores/claude-code/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-004-HU-027-el-control-avisa-las-reglas-parecidas` |
| **Módulo** | `proyectos/cimiento/core/validadores/`, `adaptadores/claude-code/` |
| **Planteamiento / Épica / HU** | [EP-004](../../epica.md) · [HU-027](../HU-027-una-regla-parecida-se-avisa-al-crearla.md) |
| **Última actualización** | 2026-10-05 |

## 1. En qué estación va

**Estación actual:** 12, commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ Análisis 1 del pendiente 116 |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ Acuerdo 5 del análisis |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-004 |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ HU-027, el 2026-10-04 |
| 5 | Escritor de especificación | 👤 especificación aprobada | N/A: la especificación son los CA |
| 6 | Diseñador | diseño coherente | ☑ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ Aprobados el 2026-10-04; el cambio a la tabla de palabras, el 2026-10-05 |
| 8 | Implementador | implementado + pruebas verdes | ☑ Las 4 tareas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ Sin fallas |
| 10 | Crítico | sin hallazgos graves | ☑ Ninguno |
| 11 | Cierre documental + señales | docs y señales al día | ☑ Resultado, funcionalidad, HU y registro de cambios |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

## 1.2 Avance de las tareas del plan

**Hechas:** 4 de 4. **Bloqueadas:** ninguna.

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | Cumple |
| **CA cumplidos** | 3 de 3 |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | `resultado_pruebas.md` |

## 2. Decisiones y señales generadas  ·  `13·DOC5`

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Umbral 0,85 sobre el título y la exigencia, medido sobre las 257 reglas | En el comentario de `UMBRAL`, en `parecidas.py` |
| La tabla de palabras del modelo en `memoria/diccionario.db`, para no abrir el modelo en cada aviso | En el plan de trabajo (cambio aprobado) y en la documentación de `parecidas.py` |

## 3. Pendiente / preguntas abiertas

Ninguna.

## 4. Si se bloqueó

Se detuvo el 2026-10-05 porque el enganche tardaba 3,9 s y el RNF-01 pide menos de 3. El usuario aprobó guardar la tabla de palabras en una base de datos, y se siguió.
