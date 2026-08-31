# Estado de fase — Fase `D-EP-004-HU-008-ningun-programa-nuevo-se-cuela-en-silencio` (módulo Comprobación automática)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `D-EP-004-HU-008-ningun-programa-nuevo-se-cuela-en-silencio` |
| **Módulo** | Comprobación automática |
| **Planteamiento / Épica / HU** | [documentacion/epicas/EP-004-comprobacion-automatica/epica.md](../../epica.md) · [documentacion/epicas/EP-004-comprobacion-automatica/HU-008-corrida-completa/HU-008-corrida-completa.md](../HU-008-corrida-completa.md) |
| **Última actualización** | 2026-08-31 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ Cuatro fallas de la batería, con su causa medida |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ 2026-08-31 |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-004 ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ HU-008 ya existía |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ (`02·F19`) |
| 6 | Diseñador | diseño coherente | ☑ El guardián nombra al corredor de verdad |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-08-31 |
| 8 | Implementador | implementado + pruebas verdes | ☑ |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ Dos defectos aparecieron y se cerraron acá |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | N/A — el estándar no se despliega |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 2 de 2 |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Terminada | `no_es_punto_de_entrada` acepta nombrar al corredor; el camino viejo queda igual |
| T-02 | Terminada | Los dos programas, cada uno con su corredor real |
| T-03 | Terminada | La prueba exige nombrar al corredor, no un nombre concreto |
| T-04 | Terminada | El conteo por regla sube; el resumen queda de último |
| T-05 | Terminada | Batería interna sin fallas de estas causas |

**Hechas:** 5 de 5. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Dos reglas ya puestas se rompieron por el mismo camino: algo nuevo se agregó sin pasar por donde la regla vigila, y la prueba lo decía sin que nadie la corriera | [`S-096`](../../../../senales.md) |
| Al ampliar la comprobación que reporta un defecto hay que **sabotearla**: es la forma de que el rojo desaparezca sin que nada se arregle | [`S-096`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

Ninguna.

---

## 4. Si se bloqueó

No se bloqueó.
