# Estado de fase — Fase `C-EP-014-HU-001-se-tapa-lo-que-se-teclea-no-lo-que-se-copia` (módulo Seguridad)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `C-EP-014-HU-001-se-tapa-lo-que-se-teclea-no-lo-que-se-copia` |
| **Módulo** | Seguridad |
| **Planteamiento / Épica / HU** | [documentacion/epicas/EP-014-ninguna-clave-queda-escrita/epica.md](../../epica.md) · [documentacion/epicas/EP-014-ninguna-clave-queda-escrita/HU-001-tapar-la-clave-al-escribirla/HU-001-tapar-la-clave-al-escribirla.md](../HU-001-tapar-la-clave-al-escribirla.md) |
| **Última actualización** | 2026-09-01 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ Medido: 6 caminos escriben, 1 tapaba |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ 2026-09-01: la épica entera, de una |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-014 |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ 2026-09-01 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ [documentacion/seguridad/spec.md](../../../../seguridad/spec.md), que el módulo no tenía |
| 6 | Diseñador | diseño coherente | ☑ Sin entidades; el reconocimiento no se duplica |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-09-01 |
| 8 | Implementador | implementado + pruebas verdes | ☑ 13 pruebas nuevas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ El grave se evitó midiendo antes de construir |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | N/A — la plataforma corre en la máquina del usuario |

> **El usuario autorizó la épica entera de una vez.** Lo dijo el 2026-09-01: *«haga todo y no me pregunte tanto»*. Las puertas 2 a 7 se pasaron con esa autorización, no una por una. Queda escrito porque `02·F0` pide aprobación por eslabón, y acá se dio agrupada.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 5 de 5 |
| **CA en «No»** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Terminada | **La medición que recortó el alcance** |
| T-02 | Terminada | Tapar al llenar, y decir cuántas |
| T-03 | Terminada | Contar sin tocar |
| T-04 | Terminada | El módulo como aplicación, con su orden |
| T-05 | Terminada | La especificación, que no existía |
| T-06 | Terminada | 13 pruebas |
| T-07 | Terminada | **La orden sobre los 1 002 documentos: 7 y 21, cero alterados** |

**Hechas:** 7 de 7. **Bloqueadas:** ninguna. Los tres bloqueos del plan quedaron cerrados.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Se tapa lo que se teclea, no lo que se copia: tapar lo importado alteraría 7 documentos sin vuelta atrás | [`S-106`](../../../../senales.md) |
| Una protección irreversible se mide antes de encenderla, no después | [`S-106`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **Los 7 documentos que parecen traer credenciales siguen ahí**, y está bien: son ejemplos escritos. Queda dicho para que nadie se asuste.
- **El puente sigue siendo un puente.** El día que la plataforma y el estándar vivan en repositorios distintos, es lo primero que hay que mover.
- **Sin pantalla**, como el resto de los módulos de esta etapa.

---

## 4. Si se bloqueó

No se bloqueó.
