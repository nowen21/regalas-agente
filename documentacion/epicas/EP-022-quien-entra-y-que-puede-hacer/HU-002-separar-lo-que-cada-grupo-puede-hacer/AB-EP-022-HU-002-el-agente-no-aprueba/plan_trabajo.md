# Plan de Trabajo — Fase `AB-EP-022-HU-002-el-agente-no-aprueba` (módulo Acceso)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación. El requisito vive en la HU; las pruebas, en el `plan_pruebas`; lo que quedó hecho, en el `funcionalidad_implementada.md`.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `AB-EP-022-HU-002-el-agente-no-aprueba` |
| **Épica** | [EP-022](../../epica.md) |
| **HU** | [HU-002 Separar lo que cada grupo puede hacer](../HU-002-separar-lo-que-cada-grupo-puede-hacer.md), una sola (`F12.1`) |
| **Módulo** | Acceso |
| **Especificación del módulo** | [documentacion/acceso/spec.md](../../../../acceso/spec.md) |
| **Fecha apertura** | 2026-09-01 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN:**

- 📋 **La sección 6 del [análisis](../../../../../cvds/analisis-requisitos/README.md)**, que definió los permisos de cada actor y nadie construyó.
- 🩹 **Y un hueco medido:** `aprobar --quien "cualquier cosa"` guardaba ese texto tal cual. Una aprobación decía quién la dio y no lo probaba.

> **El usuario autorizó ejecutar sin aprobar paso por paso** el 2026-09-01.

**CA de la HU que cubre esta fase:** los tres, todos ☑.

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** que el agente no pueda aprobar lo que él mismo construyó.

**Y que las órdenes dejen de aceptar un nombre inventado.** Era el mismo hueco que `EP-017` vino a tapar en los documentos, un nivel más abajo.

**Fuera de alcance:** permisos por proyecto, y perfiles para los dos actores que no entran.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Lo verificado:** el análisis define **cuatro** actores, y solo **dos** entran a la plataforma. «Un proyecto administrado» no es una persona ni un programa que entre; «quien recibe un proyecto» tiene escrito que **no puede entrar**.

Construir cuatro grupos habría sido construir de más, y dos de ellos no los habría usado nadie.

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `plataforma/nucleo/acceso/grupos.py` | Crear | Servicio | Los dos grupos y sus permisos |
| `plataforma/nucleo/acceso/core.py` | Crear | Servicio | Quién puede qué, y el rechazo |
| `plataforma/nucleo/acceso/para_probar.py` | Crear | Prueba | Lo que una prueba necesita para entrar |
| `plataforma/nucleo/aprobaciones/core.py` | Modificar | Servicio | `quien` deja de ser texto libre |
| `plataforma/nucleo/aprobaciones/tests.py` | Modificar | Prueba | Sus nombres pasan a ser cuentas |

**Ninguna entidad propia.** Las de `django.contrib.auth`, con sus migraciones y su cifrado.

### 2.2 Matriz de dependencias del refactor

**`aprobaciones.aprobar` cambia de contrato**, y es a propósito: lo que antes aceptaba, ahora rechaza. Sus 17 pruebas se pusieron al día.

### 2.3 Rutas · 2.4 UI · 2.5 Permisos

No aplican: órdenes de consola.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **Dos grupos, no cuatro** | Un grupo por actor del análisis | Dos de los cuatro no entran: un proyecto no es una persona, y quien recibe tiene prohibido entrar |
| **El agente no aprueba** | Dejarlo aprobar y registrar que fue él | `00·N1`: la aprobación es de una persona. Un agente que se aprueba a sí mismo la vuelve un trámite |
| **El rechazo dice el porqué, no solo el permiso** | «No autorizado» | Un motivo sin porqué obliga a ir a preguntar |
| **El porqué vive con el permiso** | Escribirlo en cada sitio que rechaza | Copiado en dos lados, un día dice dos cosas |
| **Los permisos cuelgan del modelo de Proyecto** | Inventar un modelo para colgarlos | Django exige colgarlos de alguno; aprobar no es «cambiar una fila», y Proyecto es aquello sobre lo que se actúa |
| **El superusuario puede sin estar en un grupo** | Exigirle grupo también | Es la cuenta de rescate de la máquina |

### 2.7 Dudas por resolver antes de codificar

Ninguna: la tabla de permisos sale de la sección 6 del análisis.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | CA | Ev. |
|---|---|---|:--:|---|---|---|
| T-01 | Los dos grupos con sus permisos | Servicio | 1,5 h | — | CA-01 | EV-01 |
| T-02 | Preguntar si una cuenta puede algo | Servicio | 30 min | T-01 | CA-01 | EV-01 |
| T-03 | El rechazo con su porqué | Servicio | 1 h | T-02 | CA-02 | EV-01 |
| T-04 | Que `aprobar` exija una cuenta con permiso | Servicio | 1 h | T-03 | CA-03 | EV-01 |
| T-05 | Poner al día las pruebas de aprobaciones | Test | 1 h | T-04 | — | EV-01 |
| T-06 | Las pruebas de los tres CA | Test | 1,5 h | T-05 | Todos | EV-01 |

**Total estimado:** 6,5 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-03 → T-04 → T-06.

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Intentando las cuatro acciones restringidas con cada grupo | EV-01 | 2026-09-02 | ☑ |
| CA-02 | Leyendo el motivo del rechazo | EV-01 | 2026-09-02 | ☑ |
| CA-03 | Aprobando con un nombre inventado | EV-01 | 2026-09-02 | ☑ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Las pruebas de la fase | `plataforma/nucleo/acceso/tests.py` |

---

## 6. Datos y ambiente de prueba

Cuentas de mentiras de los dos grupos, en la base de pruebas, y una carpeta temporal como proyecto.

---

## 7. Reversión / rollback  ·  Q11

Quitar el middleware y la app deja la plataforma abierta como antes. **Las cuentas creadas quedan**, y eso es lo que hay que saber: se pierden si se borra la base.

---

## 8. Producción y migración incremental  ·  Q12

**Aditivo puro.** Ninguna migración, ninguna dependencia nueva.

---

## 9. Reglas aplicadas  ·  Q13

- Base: [`00·N1`](../../../../../base/00-nucleo-blindado.md), que pide aprobación de una persona para todo cambio de estado.
- Producto: las `RN-1` a `RN-5` de la historia, y la sección 8.3 del diseño.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | **Que el agente se apruebe a sí mismo** | **Alto: la aprobación se vuelve un trámite** | No tiene el permiso, y hay prueba | Cerrado |
| B-02 | **Que un rechazo deje algo a medio guardar** | Alto | Se comprueba que no quede ninguna aprobación | Cerrado |
| B-03 | Que el rechazo no se entienda | Medio | Dice el permiso, el porqué y qué grupo lo tiene | Cerrado |
| B-04 | Que hagan falta permisos por proyecto | Bajo | **Se declara:** un grupo rige en toda la plataforma |

---

## 11. Definition of Done

- [x] Los tres CA verificados con evidencia
- [x] Comprobado que el agente no aprueba
- [x] Comprobado que un rechazo no deja nada guardado
- [x] Las dos baterías en verde
- [x] Señales registradas
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
