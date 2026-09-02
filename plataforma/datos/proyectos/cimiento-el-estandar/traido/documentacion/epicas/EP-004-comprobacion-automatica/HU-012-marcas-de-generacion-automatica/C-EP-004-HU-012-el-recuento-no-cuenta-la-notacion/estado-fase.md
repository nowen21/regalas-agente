# Estado de fase — Fase C-EP-004-HU-012-el-recuento-no-cuenta-la-notacion (módulo Programas de comprobación)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `C-EP-004-HU-012-el-recuento-no-cuenta-la-notacion` |
| **Módulo** | Programas de comprobación |
| **Planteamiento / Épica / HU** | [prompts/cimiento-planteamiento.md](../../../../../prompts/cimiento-planteamiento.md) · [EP-004](../../epica.md) · [HU-012](../HU-012-marcas-de-generacion-automatica.md) |
| **Última actualización** | 2026-08-22 |

---

## 1. En qué estación va

**Estación actual:** 12, commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ |
| 6 | Diseñador | diseño coherente | ☑ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ |
| 8 | Implementador | implementado + pruebas verdes | ☑ |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ✅ `9b808e0` |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | Cumple |
| **CA cumplidos** | 3 de 3 exigencias de la matriz |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno. Los dos que salieron se cerraron dentro de la fase |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Hecha | Las 126 clasificadas en cuatro formas |
| T-02 | Hecha | Tres expresiones, probadas antes de conectarlas |
| T-03 | Hecha | Cuatro líneas de prosa reescritas |
| T-04 | Hecha | La decisión escrita junto a la del 2026-08-18 |
| T-05 | Hecha | 44 pruebas en verde, y la medición carpeta por carpeta |
| T-06 | Hecha | Sobre `31.15.0` |

**Hechas:** 6 de 6.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| No hubo excepción que declarar: el anexo ya decía «como inciso» y «en prosa», y el contador era más ancho que la regla | [funcionalidad_implementada.md](funcionalidad_implementada.md) §5 |
| Es la segunda vez que pasa lo mismo. La primera fue el 2026-08-18 con el punto medio de los encabezados, y quedó escrita en el propio anexo | Ídem. Vale la pena mirar si hay una tercera |
| El campo de formulario se reconoce por su valor y no por su carpeta, para que la misma línea llenada con prosa vuelva a contar | Ídem |
| Las expresiones se probaron **antes** de conectarlas, a propósito: en esta misma jornada se escribió un criterio y se midió después, y hubo que rehacerlo dos veces | Ídem |

---

## 3. Pendiente / preguntas abiertas

- Falta la autorización del usuario para el commit. Nada más.

---

## 4. Si se bloqueó

No se bloqueó.
