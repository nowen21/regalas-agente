# Plan de Pruebas · Fase A-EP-026-HU-001, el registro de cambios   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP026-HU001-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-001](../HU-001-todo-cambio-guardado-en-la-base-deja-quien-cuando-antes-despues-y-por-que.md) |
| **Fecha** | 2026-10-06 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 132](../../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.historia core.proyectos core.niveles core.cuentas core.ayuda core.enganches.tests_analisis_en_curso`, que son la suite nueva y las de los módulos que la fase toca.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-001 | CA-01 | CP-001 | Funcional | Crítica | Sí | ☑ |
| HU-001 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |
| HU-001 | CA-03 | CP-003 | Funcional | Alta | Sí | ☑ |
| HU-001 | CA-04 | CP-004 | Seguridad | Crítica | Sí | ☑ |

**Cobertura:** 4 de 4 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · Crear, cambiar y borrar quedan en la historia

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-01 |
| **Tipo** | Funcional |
| **Prioridad** | Crítica |
| **Precondiciones** | La base de pruebas migrada |
| **Datos de entrada** | Un ajuste de proyecto, un grupo |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Crear un ajuste de un proyecto | Un cambio «crear» con el valor |
| 2 | Cambiarlo de 2000 a 3000 con motivo y cuenta | Un cambio «cambiar» con antes 2000, después 3000, la cuenta y el motivo |
| 3 | Borrarlo | Un cambio «borrar» con el valor de antes |
| 4 | Guardar sin cambiar nada | No se suma ningún cambio |
| 5 | Agregar una cuenta a un grupo | Un cambio en la tabla de cuentas |

### CP-002 · El estado del análisis queda en la historia

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-02 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Un proyecto registrado |
| **Datos de entrada** | La fila del análisis de una sesión |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Guardar el estado con `EstadoEnBase.guardar` | Un cambio de `proyectos.analisisprendido` con quién «agente» |
| 2 | Borrarlo con `EstadoEnBase.borrar` | Un cambio «borrar» |

### CP-003 · Deshacer desde la pantalla

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-03 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Un ajuste cambiado de 2000 a 3000 |
| **Datos de entrada** | La cuenta administradora y la de consulta |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir `/historia/` | Lista el cambio |
| 2 | Deshacerlo con la cuenta de consulta | 403, y el ajuste sigue en 3000 |
| 3 | Deshacerlo con la administradora | El ajuste vuelve a 2000 y hay un cambio nuevo que nombra el deshecho |

### CP-004 · Sin claves en la historia

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-04 |
| **Tipo** | Seguridad |
| **Prioridad** | Crítica |
| **Precondiciones** | Una cuenta |
| **Datos de entrada** | Una contraseña nueva y un motivo con una clave pegada |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Cambiar la contraseña | La historia dice «cambiada», sin el valor |
| 2 | Guardar un cambio con una clave en el motivo | La historia guarda el motivo con la clave tapada |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4; si obliga a tocar un archivo que el plan no declara, es hallazgo y se detiene la fase.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 4, en `resultado_pruebas.md`.
