# Plan de Pruebas · Fase A-EP-027-HU-004, el estándar se lee como página   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP027-HU004-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-004](../HU-004-la-pantalla-lista-las-reglas-por-capitulo-con-sus-relaciones-y-enlaces-que-abren.md) |
| **Fecha** | 2026-10-07 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 136](../../../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.estandar core.ayuda`: la prueba nueva y las suites de las pantallas y la ayuda que cambian.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-004 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-004 | CA-02 | CP-002, CP-003 | Funcional | Alta | Sí | ☑ |
| HU-004 | CA-03 | CP-004 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 3 de 3 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · La lista va por capítulo y por nombre

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir la lista con un capítulo de un archivo, uno de carpeta y su regla | Los grupos llevan el nombre del capítulo; cada regla, su código y su título; ninguna ruta |
| 2 | Pulsar una regla de un capítulo de un archivo | Lleva a su sección dentro del capítulo |

### CP-002 · El documento se lee como página

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir una regla con ejemplo, tabla y lista | Tarjeta «Incorrecto» y tarjeta «Correcto», tabla de Tabler, lista; sin `#`, `|---|`, `**` ni tres comillas invertidas |

### CP-003 · El texto no entra como HTML

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Convertir un texto con `<script>` | Sale escapado |

### CP-004 · Los enlaces abren y las relaciones se ven

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir una regla que depende de otra y nombra una tercera | El enlace lleva a la página de la otra regla en Cimiento; el espacio de relaciones muestra la dependencia, la que nombra y la que la nombra por separado |
| 2 | Un enlace a un archivo que no está en la base | Se ve como texto, sin enlace |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 4, en `resultado_pruebas.md`.
