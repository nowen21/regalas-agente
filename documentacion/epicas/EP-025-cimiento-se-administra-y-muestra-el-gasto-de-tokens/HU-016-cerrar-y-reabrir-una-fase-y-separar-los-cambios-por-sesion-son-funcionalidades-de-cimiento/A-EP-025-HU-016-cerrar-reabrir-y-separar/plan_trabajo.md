# Plan de Trabajo · Fase `A-EP-025-HU-016-cerrar-reabrir-y-separar` (módulo `proyectos/cimiento/core/herramientas/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-016-cerrar-reabrir-y-separar` |
| **Épica** | [EP-025](../../epica.md) |
| **HU** | [HU-016](../HU-016-cerrar-y-reabrir-una-fase-y-separar-los-cambios-por-sesion-son-funcionalidades-de-cimiento.md), una sola (`F12.1`) |
| **Módulo** | `proyectos/cimiento/core/herramientas/` |
| **Especificación del módulo** | Los CA de la [HU-016](../HU-016-cerrar-y-reabrir-una-fase-y-separar-los-cambios-por-sesion-son-funcionalidades-de-cimiento.md) |
| **Fecha apertura** | 2026-10-05 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): funcionalidad nueva. Sale del acuerdo 6 del [análisis 2 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-2.md) y del acuerdo 2 del [análisis 3](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-3.md).

**Carencias que cierra** (`02·F14` Q3): cada fase se cierra a mano o con un guion casi igual al anterior; no hay cómo reabrirla; lo de cada sesión se separa con otro guion.

**Aprobación** (`02·F4`): [análisis 3 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-3.md), el 2026-10-05, con la versión 54.3.0

**Disparo** (`02·F15`, etapa 2): el usuario pidió «continúe» el 2026-10-05, después de aprobar el análisis.

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-016 | Estado |
|---|---|
| CA-01 · Cerrar una fase | ☑ |
| CA-02 · Reabrir una fase | ☑ |
| CA-03 · Separar los cambios por sesión | ☑ |
| CA-04 · Lo que no se puede hacer se dice | ☑ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** tres órdenes de `manage.py`: `cerrar_fase`, `reabrir_fase` y `cambios_por_sesion`.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Cerrar | Programa | Alta |
| CA-02 | Reabrir | Programa | Media |
| CA-03 | Separar por sesión | Programa | Media |
| CA-04 | Rechazos y simulación | Programa | Baja |

**Fuera de alcance:** el commit y la interfaz.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Verificado el 2026-10-05, sobre la versión 54.3.0:

- Los guiones `cerrar_hu_006.py` a `cerrar_hu_010.py` de `historico-chat/scripts/2026-10-05/` escriben el estado, el resultado y la funcionalidad completos, el cierre del plan, la fila de la fase en la HU y el estado en la épica. Cambian solo los datos de cada fase.
- `Sesiones` (`core/validadores/sesiones.py`) guarda en `historico-chat/.tocado/<sesión>.txt` lo que tocó cada sesión, y `registros()` da las vivas. El control del commit (`SesionesMezcladas`) solo avisa.
- El andamio ya sabe leer la épica y la HU de una fase (`EP-025·HU-020`).

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/herramientas/fase.py`, `proyectos/cimiento/core/herramientas/tests_fase.py` | Crear | Programa | Cerrar y reabrir |
| `proyectos/cimiento/core/herramientas/cambios.py`, `proyectos/cimiento/core/herramientas/tests_cambios.py` | Crear | Programa | Separar por sesión |
| `proyectos/cimiento/core/proyectos/management/commands/cerrar_fase.py`, `proyectos/cimiento/core/proyectos/management/commands/reabrir_fase.py`, `proyectos/cimiento/core/proyectos/management/commands/cambios_por_sesion.py` | Crear | Programa | Las órdenes |
| `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-016-cerrar-y-reabrir-una-fase-y-separar-los-cambios-por-sesion-son-funcionalidades-de-cimiento/HU-016-cerrar-y-reabrir-una-fase-y-separar-los-cambios-por-sesion-son-funcionalidades-de-cimiento.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md` | Modificar | Documentación | La fila de la fase y el estado |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

No aplica: todo es nuevo.

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

Desde `proyectos/cimiento/`: `python manage.py cerrar_fase «carpeta»`, `reabrir_fase «carpeta» --motivo «…»` y `cambios_por_sesion [«sesión»] [--preparar | --soltar]`, todas con `--aplicar`.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Cerrar en dos pasadas: la primera escribe con `«…»` lo humano, la segunda cierra si ya no hay marcas | Pedir todo por argumentos | Lo humano es texto largo; escribirlo en el documento es más simple y el validador de marcas ya lo vigila | Propuesta del agente |
| Solo se escribe un documento de cierre que sigue en plantilla | Regenerarlo siempre | No pisa lo escrito a mano (RNF-01) | Propuesta del agente |
| La lógica vive en `core/herramientas/` sin Django; las órdenes de `manage.py` solo la llaman | Toda la lógica en la orden | Se prueba sin base y se puede llamar desde otra herramienta | Análisis 2, acuerdo 5 |
| Las órdenes van en la aplicación `core.proyectos` | Una aplicación nueva | Es la que administra los proyectos; las herramientas no son una aplicación de Django | Propuesta del agente |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 Qué cambia técnicamente  ·  `02·F14` Q5

| Artefacto | Hoy | Después | Regla que aplica |
|---|---|---|---|
| Cierre de fase | A mano o con guion | `cerrar_fase` y su contraria `reabrir_fase` | Análisis 2, acuerdo 6; análisis 3, acuerdo 2 |
| Commit por sesión | Guion | `cambios_por_sesion` | Análisis 2, acuerdo 6 |

## 3. Desglose de tareas por criterio de aceptación

### CA-01 · Cerrar una fase

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | Leer de la fase: el plan (CA, tareas, módulo, aprobación, versión) y el plan de pruebas (casos) | `proyectos/cimiento/core/herramientas/fase.py` | CA-01 | Nuevo | 1 h | Ninguna | CP-001 |
| T-02 | Escribir el estado, el resultado y la funcionalidad si siguen en plantilla, con `«…»` en lo humano; si quedan marcas, decir dónde y parar | `proyectos/cimiento/core/herramientas/fase.py` | CA-01 | Nuevo | 2 h | T-01 | CP-001 |
| T-03 | Cerrar: matriz del plan de pruebas, cierre del plan, fila en la HU, estado de la HU y de la épica; `--pruebas` | `proyectos/cimiento/core/herramientas/fase.py` | CA-01 | Nuevo | 1,5 h | T-02 | CP-001 |

### CA-02 · Reabrir una fase

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-04 | Reabrir: estación 8, filas en «En curso», motivo, ciclo nuevo por llenar | `proyectos/cimiento/core/herramientas/fase.py` | CA-02 | Nuevo | 1 h | T-03 | CP-002 |

### CA-03 · Separar los cambios por sesión

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-05 | Cruzar el registro de sesiones con `git status`; preparar y soltar lo de una sesión | `proyectos/cimiento/core/herramientas/cambios.py` | CA-03 | Nuevo | 1,5 h | Ninguna | CP-003 |

### CA-04 · Lo que no se puede hacer se dice

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-06 | Las tres órdenes de `manage.py`, con simulación sin `--aplicar` y error claro | `proyectos/cimiento/core/proyectos/management/commands/` | CA-04 | Nuevo | 1 h | T-03 a T-05 | CP-004 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-07 | Pruebas; cerrar esta misma fase con `cerrar_fase` | `proyectos/cimiento/core/herramientas/tests_fase.py`, `proyectos/cimiento/core/herramientas/tests_cambios.py`, la HU y la épica | CA-01 a CA-04 | Documentación | 1 h | T-01 a T-06 | CP-001 a CP-004 |

## 4. Secuencia de ejecución

T-01 a T-06 en orden y al final T-07, con las pruebas de la fase (`02·F5`).

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-01 | Fase de muestra en una carpeta temporal: primera pasada con marcas, segunda que cierra | CP-001 |
| CA-02 | Reabrir la fase cerrada | CP-002 |
| CA-03 | Repositorio git temporal con dos sesiones | CP-003 |
| CA-04 | Carpeta ajena, pruebas que fallan, simulación | CP-004 |

## 6. Datos y ambiente de prueba

Carpetas temporales con una épica, una HU y una fase de muestra; un repositorio git temporal.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Aditiva: tres órdenes nuevas.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`02·F4`, `02·F5`, `02·F6`, `02·F7`, `02·F8`, `13·DOC11`, `03·D6`, `00·ID8`, `00·ID9`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Pisar lo escrito a mano | Solo se escribe lo que sigue en plantilla |
| Preparar lo de otra sesión | Lo compartido no se prepara |

## 11. Definition of Done

- [ ] CA-01 a CA-04 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Las pruebas de la fase sin fallas, y cero marcas nuevas.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Las 7 tareas quedaron hechas el 2026-10-05, con la versión 54.4.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** ninguno.
