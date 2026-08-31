# Estado de fase — Fase `B-EP-005-HU-021-la-bateria-de-la-plataforma-tambien-se-corre` (módulo Pruebas)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-005-HU-021-la-bateria-de-la-plataforma-tambien-se-corre` |
| **Módulo** | Pruebas |
| **Planteamiento / Épica / HU** | [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/epica.md](../../epica.md) · [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-021-las-pruebas-que-existen-se-corren/HU-021-las-pruebas-que-existen-se-corren.md](../HU-021-las-pruebas-que-existen-se-corren.md) |
| **Última actualización** | 2026-08-31 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ 724 pruebas corridas, 187 sin correr |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ 2026-08-31 |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-005 ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ HU-021 ya existía |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ (`02·F19`) |
| 6 | Diseñador | diseño coherente | ☑ Se le pide por su punto de entrada; las cifras van aparte |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-08-31 |
| 8 | Implementador | implementado + pruebas verdes | ☑ 9 pruebas nuevas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ Un defecto apareció al escribir las pruebas y se cerró acá |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | N/A — el estándar no se despliega |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 3 de 3 |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Terminada | `correr_la_plataforma`, por el punto de entrada de la plataforma |
| T-02 | Terminada | Su cifra aparte en el resumen de la corrida |
| T-03 | Terminada | Cero es falla; no tenerla es aviso |
| T-04 | Terminada | Con `--solo` la otra batería no corre |
| T-05 | Terminada | 9 pruebas |
| T-06 | Terminada | **Cazado**: 188 pruebas, 1 falla |

**Hechas:** 6 de 6. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| La fase `A` dio el trabajo por hecho contando una batería de dos; lo que faltaba no era arreglar el corredor sino **preguntarse cuántas hay** | [`S-097`](../../../../senales.md) |
| Una prueba que llama a la corrida completa se mete dentro de sí misma, y la orden no termina | [`S-098`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **Lo que se lee es la línea que imprime el corredor de la plataforma.** Si cambia de marco, esa línea cambia y hay que volver acá. Queda dicho, no abierto.

---

## 4. Si se bloqueó

No se bloqueó.
