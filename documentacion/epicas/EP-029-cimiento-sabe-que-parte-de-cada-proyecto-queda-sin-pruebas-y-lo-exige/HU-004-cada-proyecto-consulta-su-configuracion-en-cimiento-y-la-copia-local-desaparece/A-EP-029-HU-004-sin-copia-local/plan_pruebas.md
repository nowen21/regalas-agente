# Plan de Pruebas · Fase A-EP-029-HU-004, sin copia local   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP029-HU004-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-004](../HU-004-cada-proyecto-consulta-su-configuracion-en-cimiento-y-la-copia-local-desaparece.md) |
| **Fecha** | 2026-10-08 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 141](../../../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.proyectos core.ayuda core.herramientas.tests_instalacion`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-004 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-004 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 2 de 2 exigencias cubiertas = 100%.

## 6. Casos de prueba

### CP-001 · Ya no se escribe la copia

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Guardar un proyecto y la configuración común | En la carpeta del proyecto no hay `.agente/configuracion.md` |
| 2 | Buscar la copia en la ayuda | No aparece |

### CP-002 · Volver a instalar borra la copia vieja

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Paso del instalador sobre una carpeta con `.agente/configuracion.md` | El archivo ya no está y el paso lo dice |
| 2 | El mismo paso sin el archivo | No hace nada |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 2, en `resultado_pruebas.md`.
