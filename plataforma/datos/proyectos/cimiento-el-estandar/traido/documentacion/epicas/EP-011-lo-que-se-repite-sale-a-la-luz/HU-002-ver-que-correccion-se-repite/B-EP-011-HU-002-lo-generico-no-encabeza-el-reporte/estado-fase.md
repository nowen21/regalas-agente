# Estado de fase — Fase `B-EP-011-HU-002-lo-generico-no-encabeza-el-reporte` (módulo Medición)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-011-HU-002-lo-generico-no-encabeza-el-reporte` |
| **Módulo** | Medición |
| **Planteamiento / Épica / HU** | [documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/epica.md](../../epica.md) · [documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-002-ver-que-correccion-se-repite/HU-002-ver-que-correccion-se-repite.md](../HU-002-ver-que-correccion-se-repite.md) |
| **Última actualización** | 2026-08-31 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ Tres de las cinco primeras filas no eran correcciones |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ 2026-08-31 |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-011 ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ HU-002 aprobada el 2026-08-31 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ |
| 6 | Diseñador | diseño coherente | ☑ El vocabulario se calcula, no se escribe |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-08-31 |
| 8 | Implementador | implementado + pruebas verdes | ☑ 47 pruebas, 9 nuevas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ Tres defectos, todos cerrados acá |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ✅ `27dd028` |
| 13 | Publicación / despliegue | 👤 autorizado | N/A |

> **La mejora aprobada no era la que servía, y se supo antes de construirla.** El usuario aprobó ordenar por sesiones distintas; medido, dejaba «debe quedar» de primero igual. Lo que sirvió fue descartar las frases hechas con el vocabulario del propio corpus. Se construyó eso, con el mismo objetivo aprobado, y queda dicho acá en vez de entregarse lo que no funcionaba.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | El `CA-01`, y el riesgo 2 de la §9 |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-00 | Terminada | Tres formas medidas; dos descartadas con su número |
| T-01 | Terminada | 40 palabras de vocabulario, calculadas sobre 67 sesiones |
| T-02 | Terminada | La frase con una de esas palabras no entra |
| T-03 | Terminada | Las rutas pegadas fuera: dos filas menos |
| T-04 | Terminada | Mínimo de sesiones, y orden por días distintos |
| T-05 | Terminada | Con menos de ocho sesiones no se filtra |
| T-06 | Terminada | 9 pruebas nuevas, y las de la fase A repartidas en días |
| T-07 | Terminada | El reporte antes y después, escrito |

**Hechas:** 8 de 8. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| La mejora que se propuso y se aprobó no funcionaba; medirla antes de construirla costó veinte minutos y evitó entregar algo que no servía | [`S-100`](../../../../senales.md) |
| Lo que separa una corrección de la forma de redactar es qué tan común es la palabra en el propio corpus, y eso se calcula | [`S-100`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **Si de las primeras filas nace una regla.** Es el riesgo 2 de la historia, y lo juzga el usuario. Lo que la fase deja es de dónde: «estoy preguntando», ocho sesiones distintas.
- **El umbral se calibró contra este trabajo.** En un proyecto que hable de otra cosa habrá que volver a mirarlo. Queda dicho, no abierto.

---

## 4. Si se bloqueó

No se bloqueó.
