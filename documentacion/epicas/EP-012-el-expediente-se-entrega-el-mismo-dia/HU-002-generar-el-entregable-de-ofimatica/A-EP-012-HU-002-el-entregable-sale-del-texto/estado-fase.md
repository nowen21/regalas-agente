# Estado de fase — Fase `A-EP-012-HU-002-el-entregable-sale-del-texto` (módulo Expediente)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-012-HU-002-el-entregable-sale-del-texto` |
| **Módulo** | Expediente |
| **Planteamiento / Épica / HU** | [documentacion/epicas/EP-012-el-expediente-se-entrega-el-mismo-dia/epica.md](../../epica.md) · [documentacion/epicas/EP-012-el-expediente-se-entrega-el-mismo-dia/HU-002-generar-el-entregable-de-ofimatica/HU-002-generar-el-entregable-de-ofimatica.md](../HU-002-generar-el-entregable-de-ofimatica.md) |
| **Última actualización** | 2026-08-31 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ El expediente ya se arma; falta convertirlo |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ 2026-08-31 |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-012 |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ 2026-08-31 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ [documentacion/expediente/spec.md](../../../../expediente/spec.md) |
| 6 | Diseñador | diseño coherente | ☑ Con la librería estándar, decisión mantenida con el dato nuevo a la vista |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-08-31 |
| 8 | Implementador | implementado + pruebas verdes | ☑ 20 pruebas nuevas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ Tres defectos, los tres cerrados acá |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ✅ `736f51a` |
| 13 | Publicación / despliegue | 👤 autorizado | N/A — la plataforma corre en la máquina del usuario |

> **La decisión de con qué generar se volvió a poner sobre la mesa antes de construir.** Al abrir la fase apareció que `markdown` ya está instalado en esta máquina, aunque no es dependencia declarada. Se le dijo al usuario con el argumento de los dos lados, y mantuvo la librería estándar. Queda escrito porque el dato era nuevo y podía cambiar lo decidido.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 4 de 4 |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Uno, declarado: 15 marcas de énfasis anidado en ocho millones de caracteres |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Terminada | El convertidor, con la librería estándar |
| T-02 | Terminada | 6 205 tablas y 1 697 listas dentro de celdas |
| T-03 | Terminada | La envoltura, sin nada de la red |
| T-04 | Terminada | El índice, y lo que falta dentro del archivo |
| T-05 | Terminada | Guardado con constancia y registrado |
| T-06 | Terminada | `generar_entregable`, con los avisos antes de la ruta |
| T-07 | Terminada | 20 pruebas |
| T-08 | Terminada | **Medido: 15 marcas en 8 093 097 caracteres** |

**Hechas:** 8 de 8. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Los tres defectos del convertidor salieron de contar sobre ocho millones de caracteres reales; con documentos de mentiras se veía perfecto | [`S-102`](../../../../senales.md) |
| Un convertidor de marcado se comprueba **contando lo que quedó a la vista**, no mirando un ejemplo bien elegido | [`S-102`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **Quince marcas de énfasis dentro de énfasis.** Resolverlo pide un analizador de verdad; por quince en ocho millones no se justifica hoy. Queda dicho, sin pendiente.
- **Si el archivo se ve presentable** lo decide una persona abriéndolo. Es lo único que esta fase no puede medir.

---

## 4. Si se bloqueó

No se bloqueó.
