# Plan de Trabajo · Fase `A-EP-025-HU-019-la-regla-y-su-plantilla` (módulo `base/02-flujo-de-trabajo/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-019-la-regla-y-su-plantilla` |
| **Épica** | [EP-025](../../epica.md) |
| **HU** | [HU-019](../HU-019-toda-accion-trae-su-contraria.md), una sola (`F12.1`) |
| **Módulo** | `base/02-flujo-de-trabajo/` |
| **Especificación del módulo** | Los CA de la [HU-019](../HU-019-toda-accion-trae-su-contraria.md) |
| **Fecha apertura** | 2026-10-05 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): regla nueva. Sale del acuerdo 2 del [análisis 3 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-3.md).

**Carencias que cierra** (`02·F14` Q3): ninguna regla pide la contraria de lo que se construye.

**Aprobación** (`02·F4`): [análisis 3 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-3.md), el 2026-10-05, con la versión 54.3.0

**Disparo** (`02·F15`, etapa 2): el usuario pidió «continúe» el 2026-10-05, después de aprobar el análisis.

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-019 | Estado |
|---|---|
| CA-01 · La regla existe con su forma | ☑ |
| CA-02 · El plan la declara | ☑ |
| CA-03 · Queda versionado | ☑ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** la regla `02·F30`, la sección de la plantilla del plan que la declara, y la versión mayor.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | La regla | Documentación | Media |
| CA-02 | La plantilla | Documentación | Baja |
| CA-03 | La versión | Documentación | Baja |

**Fuera de alcance:** un validador (`20·M19`).

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Verificado el 2026-10-05, sobre la versión 54.4.0:

- Buscado por concepto (`20·M12`): «contraria», «deshacer», «revertir», «reversión», «desinstalar» en `base/`. Solo `03·D2` pide algo parecido, y solo para el esquema de datos (la migración con su reversión). El §7 del plan de trabajo es la reversión del cambio si sale mal, no la acción contraria que el producto ofrece.
- El capítulo `02` dice cuándo algo construido está terminado; su último ID es `F29`.
- `base/mapa-de-tareas.md` y `base/reglas-por-tarea/` los escribe `python validadores/mapa_tareas.py`.
- Las reglas no validables del `02` se listan en `validadores/reglas-validables.md`.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md` | Crear | Regla | La regla |
| `base/02-flujo-de-trabajo/base.md` | Modificar | Regla | Su fila y su detalle |
| `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md` | Modificar | Plantilla | Sección 2.8 |
| `base/mapa-de-tareas.md`, `base/reglas-por-tarea/README.md`, `base/reglas-por-tarea/cambiar-codigo-4.md`, `base/reglas-por-tarea/trabajar-cadena-2.md` | Modificar | Regla | Los escribe el programa |
| `validadores/reglas-validables.md` | Modificar | Registro | `F30` no validable |
| `CHANGELOG.md`, `VERSION` | Modificar | Registro | MAYOR |
| `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-019-toda-accion-trae-su-contraria/HU-019-toda-accion-trae-su-contraria.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md` | Modificar | Documentación | La fila de la fase y el estado |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

No aplica.

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica: es una regla.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Va en el capítulo `02` | `07` (calidad de código) o `03` (datos) | Dice cuándo algo construido está terminado, como el resto del flujo; `07` es sobre leer el código y `03·D2` es un caso de ella | Propuesta del agente (`20·M2`) |
| `03·D2` se cita como caso, no se deroga | Absorberla | `D2` pide además no tocar una migración ya corrida | Propuesta del agente (`20·M12`) |
| No validable por ahora | Validar que el plan traiga la tabla | Que la contraria sea la correcta es criterio; primero se cumple a mano | `20·M19` |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

## 3. Desglose de tareas por criterio de aceptación

### CA-01 · La regla existe con su forma

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | Escribir la regla con su ejemplo, su «Aplica a» y su checklist | `base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md` | CA-01 | Todo proyecto | 1 h | Ninguna | CP-001 |
| T-02 | Su fila y su detalle en el capítulo; el mapa de tareas; el registro de validables | `base/02-flujo-de-trabajo/base.md`, `base/mapa-de-tareas.md`, `validadores/reglas-validables.md` | CA-01 | Todo proyecto | 0,5 h | T-01 | CP-001 |

### CA-02 · El plan la declara

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-03 | Sección 2.8 en la plantilla del plan | `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md` | CA-02 | Todo proyecto | 0,5 h | T-01 | CP-002 |

### CA-03 · Queda versionado

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-04 | Entrada MAYOR y versión | `CHANGELOG.md`, `VERSION` | CA-03 | Todo proyecto | 0,5 h | T-01 a T-03 | CP-003 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-05 | Validadores y cierre con `cerrar_fase` | La HU y la épica | CA-01 a CA-03 | Documentación | 0,5 h | T-01 a T-04 | CP-001 a CP-003 |

## 4. Secuencia de ejecución

T-01 a T-05 en orden.

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-01 | `validar.py metareglas`, `estandar` e `indices`; la regla en el mapa | CP-001 |
| CA-02 | La sección en la plantilla | CP-002 |
| CA-03 | `validar.py versionado` | CP-003 |

## 6. Datos y ambiente de prueba

El repositorio del estándar.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase. La regla no se borra después de publicada: se deroga (`20·M11`).

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Los proyectos al día declaran la contraria en sus planes nuevos; las fases cerradas no se tocan.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`20·M2`, `20·M3`, `20·M4`, `20·M5`, `20·M7`, `20·M9`, `20·M10`, `20·M12`, `20·M14`, `20·M19`, `00·ID7`, `00·ID9`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Duplicar `03·D2` | Se cita como caso |

## 11. Definition of Done

- [ ] CA-01 a CA-03 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Los validadores sin fallas nuevas, y cero marcas nuevas.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Las 5 tareas quedaron hechas el 2026-10-05, con la versión 55.0.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** ninguno.

**Reabierta** el 2026-10-05: la sección 2.1 declaraba la carpeta base/reglas-por-tarea/ en vez de sus archivos, y validar.py flujo lo marca como falla (02·F8).

Cerrada otra vez el 2026-10-05, con la versión 55.0.0.
