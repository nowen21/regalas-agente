# Plan de Pruebas · Fase A-EP-029-HU-001, ajustes y estado de la revisión   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP029-HU001-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-001](../HU-001-la-configuracion-de-cada-proyecto-dice-que-tan-estricta-es-la-revision-de-pruebas.md) |
| **Fecha** | 2026-10-08 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 141](../../../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.pruebas core.proyectos core.ayuda core.enganches`: la suite nueva y las de lo que lee el catálogo de ajustes.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-001 | CA-01 | CP-001, CP-002 | Funcional | Alta | Sí | ☑ |
| HU-001 | CA-02 | CP-003 | Funcional | Alta | Sí | ☑ |
| HU-001 | CA-03 | CP-004, CP-005 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 3 de 3 exigencias cubiertas = 100%.

## 6. Casos de prueba

Los valores esperados salen de la HU (RN-02 y RN-03), no del código (`08·T8`).

### CP-001 · Sin valores propios, vale lo de fábrica

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer los ajustes efectivos sin base ni proyecto | Revisión: «solo avisar»; días: 7; capa: fábrica |
| 2 | Leerlos con «no dejar guardar» y 3 en el proyecto | Valen esos, con capa proyecto |
| 3 | Leerlos con 5 en la base y nada en el proyecto | Días: 5, capa base |

### CP-002 · Lo que no es válido se rechaza

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Limpiar «avisar siempre» | `ValueError` |
| 2 | Limpiar 0 en los días | `ValueError` |

### CP-003 · Los dos ajustes salen en los formularios, con su ayuda

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Armar el formulario de un proyecto y el de «Configuración» | Los dos traen los dos campos |
| 2 | Buscar la ayuda de cada clave | Existe, y su texto no trae las palabras «cobertura», «coverage» ni «commit» |

### CP-004 · Se guarda una revisión y es la última

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Guardar dos revisiones de un proyecto, una de ayer y una de hoy | La última es la de hoy, con su herramienta, sus archivos y el resultado del navegador |

### CP-005 · Un proyecto sin revisiones

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir la última revisión de un proyecto nuevo | Ninguna |
| 2 | Preguntar si tiene la parte que revisa | No |
| 3 | Marcar que la tiene | Sí |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 5, en `resultado_pruebas.md`.
