# Plan de Pruebas · Fase A-EP-026-HU-004, leer de la base   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP026-HU004-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-004](../HU-004-los-enganches-leen-el-estandar-de-la-base.md) |
| **Fecha** | 2026-10-06 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 132](../../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.estandar core.validadores core.niveles core.herramientas.tests_respondo core.enganches.tests_freno core.enganches.tests_sesion`, la suite nueva y las de lo que usa los lectores cambiados (§2.2 del plan).

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-004 | CA-01 | CP-001 | Funcional | Crítica | Sí | ☑ |
| HU-004 | CA-02 | CP-002 | Funcional | Crítica | Sí | ☑ |
| HU-004 | CA-03 | CP-003 | Regresión | Alta | Sí | ☑ |
| HU-004 | CA-04 | CP-004 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 4 de 4 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · Lo que dice la base es lo que se lee

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Servir el estándar desde unos documentos de la base con una regla cambiada | `CuerpoDeReglas`, las autorizaciones y el arranque leen la versión de la base |
| 2 | Pedir el orden de los documentos | Es el mismo de recorrer la carpeta |

### CP-002 · Sin base

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir las reglas de un mensaje con la base apagada | El texto dice que no hay base y que no se trabaja |
| 2 | Pedir las autorizaciones con la base apagada | Ninguna, sin romperse |

### CP-003 · Mismas reglas

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Elegir las reglas de varios mensajes leyendo de la base y del disco | Las mismas |

### CP-004 · Sincronizar con git

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Cambiar un documento en la base y sincronizar | Vuelve a lo que dice git, como un cambio de una versión nueva del estándar |
| 2 | Sincronizar sin diferencias | No sube versión |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 4, en `resultado_pruebas.md`.
