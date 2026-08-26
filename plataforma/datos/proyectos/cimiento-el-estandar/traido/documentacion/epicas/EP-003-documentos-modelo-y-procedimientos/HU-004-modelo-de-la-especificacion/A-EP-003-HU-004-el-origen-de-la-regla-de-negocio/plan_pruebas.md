# Plan de Pruebas — «Fase A-EP-003-HU-004: el origen de la regla de negocio»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de la misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-003-HU-004 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-003-HU-004-el-origen-de-la-regla-de-negocio` |
| **Fecha** | 2026-08-16 |
| **Elaborado por** | El agente |
| **Aprobado por** | El usuario, en la orden de resolver los ocho pendientes `P1` |
| **Estado** | Aprobado |

> Fase chica y de documento: se llenan las secciones **3, 5, 6, 9 y 12**.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Aceptación manual | Llenar el modelo y ver si deja pasar una regla sin procedencia | El documento | No |

**Por qué no se automatiza acá.** Lo que esta fase entrega es un **modelo de documento**: lo que se puede automatizar es comprobar los documentos que se escriban con él, y eso es la fase del validador, en EP-004. Automatizar sobre el modelo mismo sería comprobar que un texto contiene un texto.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Aceptación | ☑ | El `CA-04` |
| No regresión | ☑ | Que una especificación ya escrita siga siendo legible contra el modelo nuevo |

### 3.3 Técnicas de diseño de casos

- **El caso real que lo destapó** — la regla 5 de `documentacion/problemas/spec.md` de `shopnest-mesa`, que nació en la especificación y no bajaba de ninguna parte.
- **Caso contrario** — una regla que sí baja de un requisito, para ver que el formato la admite sin estorbar.

### 3.5 Alcance de la corrida

No hay suite que correr. Se ejecuta el llenado del modelo y se compara con lo que el `CA-04` exige.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-004 | CA-04 | [CP-001](#cp-001--la-regla-que-baja-de-un-requisito-cabe-en-el-formato) | Aceptación | Alta | No | ☐ |
| HU-004 | CA-04 · el caso que lo destapó | [CP-002](#cp-002--la-regla-sin-procedencia-no-tiene-dónde-escribirse) | Aceptación | Alta | No | ☐ |
| HU-004 | No regresión | [CP-003](#cp-003--una-especificación-ya-escrita-no-queda-inválida) | No regresión | Media | No | ☐ |

**Cobertura:** 1 de 1 CA = 100%.

---

## 6. Casos de prueba

### CP-001 — La regla que baja de un requisito cabe en el formato

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / CA-04 |
| **Tipo** | Aceptación |
| **Prioridad** | Alta |
| **Precondiciones** | El §4 del modelo ya pide las dos cosas |
| **Datos de entrada** | Una regla que baja de un requisito con identificador |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir la regla con su origen y su porqué, siguiendo el molde | Cabe en una línea legible |
| 2 | Leerla como quien la encuentra por primera vez | Se sabe quién la pidió sin salir del documento |
| 3 | Comprobar que el número de la regla sigue sirviendo para citarla | Sigue siendo una lista numerada |

**Resultado esperado final:** el formato agrega un dato sin romper la forma de citar.

---

### CP-002 — La regla sin procedencia no tiene dónde escribirse

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / CA-04 |
| **Tipo** | Aceptación |
| **Prioridad** | Alta |
| **Precondiciones** | Las del CP-001 |
| **Datos de entrada** | La regla 5 de `shopnest-mesa`: «un problema no se cierra sin causa raíz ni solución definitiva» |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Intentar escribirla con el molde nuevo | El hueco del origen queda a la vista |
| 2 | Buscarle un identificador de origen | No hay: no la pide el enunciado, ni el requisito, ni la épica, ni la historia |
| 3 | Leer qué manda el modelo en ese caso | Dice que no se escribe ahí: se sube a la historia que corresponda |

**Resultado esperado final:** lo que antes entraba sin resistencia ahora tiene que pasar por la historia.

> **Este es el caso, no un ejemplo.** Esa regla bajó sola a una decisión, una fila de trazabilidad, dos escenarios de prueba y un criterio de aceptación, y tardó un día en verse — solo porque alguien preguntó de dónde salía.

---

### CP-003 — Una especificación ya escrita no queda inválida

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / no regresión |
| **Tipo** | No regresión |
| **Prioridad** | Media |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | Un §4 escrito con el formato viejo |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leerlo contra el modelo nuevo | Le falta un dato, no sobra ninguno |
| 2 | Preguntarse si hay que reescribirlo para seguir cumpliendo | No: lo cerrado queda sellado con su versión |

**Resultado esperado final:** el cambio obliga hacia adelante, no hacia atrás.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Alta** | Que el formato nuevo rompa la forma de citar una regla por su número | Inmediato |
| **Media** | Que el molde quede tan largo que nadie lo llene | Antes de cerrar |

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de CA | 100% — el 1 con caso |
| Casos ejecutados | 3 de 3 |
| Especificaciones vivas que hay que reescribir | **0** |

El veredicto va en el `resultado_pruebas.md` de esta fase.
