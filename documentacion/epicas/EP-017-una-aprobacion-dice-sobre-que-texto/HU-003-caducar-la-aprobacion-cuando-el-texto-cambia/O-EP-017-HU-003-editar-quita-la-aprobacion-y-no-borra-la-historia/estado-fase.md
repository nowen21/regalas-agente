# Estado de fase — Fase `O-EP-017-HU-003-editar-quita-la-aprobacion-y-no-borra-la-historia` (módulo Aprobaciones)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `O-EP-017-HU-003-editar-quita-la-aprobacion-y-no-borra-la-historia` |
| **Módulo** | Aprobaciones |
| **Planteamiento / Épica / HU** | [documentacion/epicas/EP-017-una-aprobacion-dice-sobre-que-texto/epica.md](../../epica.md) · [documentacion/epicas/EP-017-una-aprobacion-dice-sobre-que-texto/HU-003-caducar-la-aprobacion-cuando-el-texto-cambia/HU-003-caducar-la-aprobacion-cuando-el-texto-cambia.md](../HU-003-caducar-la-aprobacion-cuando-el-texto-cambia.md) |
| **Última actualización** | 2026-09-01 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ El daño ya ocurrió, y está escrito en la ficha de `F-017` |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ 2026-09-01: la épica entera, de una |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-017 |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ 2026-09-01 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ [documentacion/aprobaciones/spec.md](../../../../aprobaciones/spec.md) |
| 6 | Diseñador | diseño coherente | ☑ La huella decide, no la fecha |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-09-01 |
| 8 | Implementador | implementado + pruebas verdes | ☑ 6 pruebas nuevas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | N/A: la plataforma corre en la máquina del usuario |

> **Con esta fase cierra `EP-017`.** Las tres historias, terminadas.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 3 de 3 |
| **CA en «No»** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Terminada | La comparación de huellas |
| T-02 | Terminada | La medida del cambio |
| T-03 | Terminada | La historia conservada |
| T-04 | Terminada | El documento que desapareció |
| T-05 | Terminada | 6 pruebas |

**Hechas:** 5 de 5. **Bloqueadas:** ninguna. Dos bloqueos cerrados y uno declarado.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Una aprobación que no sabe sobre qué texto se dio no caduca nunca, y por eso no sirve | [`S-111`](../../../../senales.md) |
| El caso que se olvida no es el documento editado: es el borrado | [`S-111`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **Arreglar una coma caduca la aprobación.** Declarado y aceptado.
- **No se vuelve a aprobar solo**, y así se quiere.
- **Sin pantalla**, como el resto de los módulos de esta etapa.

---

## 4. Si se bloqueó

No se bloqueó.
