# Estado de fase — Fase `A-EP-011-HU-001-lo-conversado-se-indexa-y-se-busca` (módulo Medición)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-011-HU-001-lo-conversado-se-indexa-y-se-busca` |
| **Módulo** | Medición |
| **Planteamiento / Épica / HU** | [documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/epica.md](../../epica.md) · [documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-001-buscar-en-lo-conversado/HU-001-buscar-en-lo-conversado.md](../HU-001-buscar-en-lo-conversado.md) |
| **Última actualización** | 2026-08-31 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ La plataforma y el histórico ya existían; faltaba unirlos |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ 2026-08-31 |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-011 ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ **Aprobada el 2026-08-31**: estaba sin aprobar, y era una de las dos puertas |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ [documentacion/medicion/spec.md](../../../../medicion/spec.md), aprobada el 2026-08-31. **No existía**, y era la otra puerta |
| 6 | Diseñador | diseño coherente | ☑ El texto no se copia: se indexa donde vive |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-08-31 |
| 8 | Implementador | implementado + pruebas verdes | ☑ 33 pruebas nuevas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ Un defecto apareció, ajeno a la fase, y se cerró acá |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ✅ `76d6ce7` |
| 13 | Publicación / despliegue | 👤 autorizado | N/A — la plataforma corre en la máquina del usuario |

> **Las dos puertas que faltaban eran del usuario, y se abrieron antes de tocar código** (`02·F2`, `02·F4`): la historia estaba sin aprobar, y el módulo Medición no tenía especificación. Escribir la especificación fue el eslabón que faltaba, no un paso de más.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 4 de 4, más el transversal |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-00 | Terminada | 329 archivos en el histórico de este repositorio |
| T-01 | Terminada | `historico.turnos`, en el estándar: quien escribe el formato lo lee |
| T-02 | Terminada | `Sesion` y `Mensaje`, el diccionario de la especificación |
| T-03 | Terminada | `indexar`: 67 sesiones y 3 720 mensajes |
| T-04 | Terminada | `buscar`: dice sesión, quién y qué dijo |
| T-05 | Terminada | `indexar_conversaciones` y `buscar_en_lo_conversado` |
| T-06 | Terminada | `reconstruir_indice`: borra entero y relee |
| T-07 | Terminada | El detector del estándar sobre los 3 720 mensajes |
| T-08 | Terminada | **Cero archivos cambiados**, medidos por huella |
| T-09 | Terminada | Los dos silencios se dicen distinto |
| T-10 | Terminada | 35,7 s sobre el volumen real |
| T-11 | Terminada | La §13 de la especificación nombra esta fase |

**Hechas:** 12 de 12. **Bloqueadas:** ninguna.

**Un archivo apareció que el plan no declaraba** (`02·F8`): `plataforma/nucleo/proyectos/tests.py`. Dos de sus pruebas estaban en rojo **por la subida de versión de esta mañana**, no por esta fase: su proyecto de mentiras declaraba una versión escrita a mano. Se reportó y se arregló acá, leyendo la versión publicada.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| La batería de la plataforma no la corre nada del estándar: una subida de versión la puso en rojo y nadie se enteró en todo el día | [`S-097`](../../../../senales.md) |
| Quien escribe un formato es quien sabe leerlo: el lector de turnos vive en el módulo que escribe las transcripciones, no en quien las consume | [`S-097`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **Nada de esta fase.** Lo que sigue es la `HU-002`, que cuenta lo repetido sobre lo que esta dejó indexado.
- **Queda dicho, sin pendiente propio:** una conversación que no pase por el enganche no se indexa y nadie se entera. Es el supuesto declarado de la historia.

---

## 4. Si se bloqueó

No se bloqueó. Estuvo detenida once días esperando dos aprobaciones, y las dos llegaron hoy.
