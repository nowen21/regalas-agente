# Plan de Pruebas · Fase `A-EP-025-HU-006-lectura-de-los-jsonl`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU006-A |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-006: CA-01 a CA-04 |
| **Fecha** | 2026-10-05 |
| **Elaborado por** | Claude |
| **Revisado por** | Ing. José Dúmar Jiménez Ruíz |
| **Aprobado por** | [Análisis 1 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md), el 2026-10-04 |
| **Estado** | Aprobado |

Para una fase, la plantilla pide las secciones 3, 5, 6, 9 y 12; las demás son opcionales y no se usan.

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Unitario | El lector | Claude | `.jsonl` de muestra | Sí |
| Integración | Guardado y orden | Claude | Base de pruebas en MariaDB | Sí |
| Manual | La orden sobre los registros reales | Claude | La base local | No |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-01, CA-02, CA-04 |
| Errores | ☑ | CA-03 |

### 3.3 Técnicas de diseño de casos

- Una muestra con lo que trae el formato: llamada partida, enganche con nombre y sin él, archivo leído, línea rota, línea final sin salto.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-01, CA-02 | 100% |
| Media | CA-03, CA-04 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Desde `proyectos/cimiento/`: `python manage.py test core.consumo`, y `PrepararCimiento` y la clase nueva de `tests_instalacion.py` importando `core.validadores` primero (pendiente 121).

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-006 | CA-01 | CP-001 | Funcional | Alta | Sí | ☐ |
| HU-006 | CA-02 | CP-002 | Funcional | Alta | Sí | ☐ |
| HU-006 | CA-03 | CP-003 | Errores | Media | Sí | ☐ |
| HU-006 | CA-04 | CP-004 | Funcional | Media | Sí | ☐ |

**Cobertura:** 4 de 4 criterios de esta fase.

## 6. Casos de prueba

### CP-001 · Lectura y guardado

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-01 |
| **Precondiciones** | T-01 a T-03 terminadas |
| **Datos de entrada** | Una muestra con dos llamadas (una partida en dos líneas), dos enganches y un `Read` con su resultado |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer la muestra con el lector | Dos llamadas con sus tokens y modelo; dos enganches con nombre y caracteres; un archivo con su ruta y caracteres |
| 2 | Correr la orden sobre un proyecto registrado cuya carpeta de Claude Code es la de la muestra | Lo mismo en la base, con proyecto y sesión |
| 3 | Correr la orden real | Dice lo leído por proyecto, sin error |

### CP-002 · Sin duplicar

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-02 |
| **Precondiciones** | T-04 terminada |
| **Datos de entrada** | La muestra de CP-001 |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr la orden dos veces | Las mismas cantidades |
| 2 | Agregar una llamada y correr | Una llamada más |
| 3 | Un archivo sin cambios | No se vuelve a leer |

### CP-003 · Líneas rotas

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-03 |
| **Precondiciones** | T-05 terminada |
| **Datos de entrada** | La muestra con una línea ilegible y una final sin salto |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer | Lo legible queda; el avance no incluye la línea sin salto |
| 2 | Completar la línea y leer otra vez | Se guarda la llamada de esa línea |

### CP-004 · Suma y programación

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-04 |
| **Precondiciones** | T-06 y T-07 terminadas |
| **Datos de entrada** | La muestra de CP-001 |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `consumos_de_transcripcion` de `hook_presupuesto.py` sobre la muestra | Dos consumos, no tres |
| 2 | `programar_lectura` en simulación | Lo anuncia y no corre nada |
| 3 | Aplicando en Windows, sin la tarea | Corre `schtasks /Create` con la orden de Cimiento |
| 4 | Con la tarea ya creada | «ya estaba» |
| 5 | Fuera de Windows | «OMITIDO» con cómo programarla |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | Se duplica una llamada, o se guarda texto de un mensaje | Antes de cerrar la fase |
| **Baja** | Una marca de redacción | Antes de cerrar la fase |

### 9.2 Flujo del defecto

Un defecto se anota en el resultado de las pruebas. Si es un error dentro de lo que el plan aprobó, se corrige y se vuelve a correr el caso. Si para cerrar la fase obliga a tocar algo que el plan no declara, es un hallazgo: se detiene la fase y vuelve al análisis.

### 9.3 Contenido mínimo de un reporte

- Caso y paso donde apareció.
- Resultado esperado frente al obtenido.

### 9.4 Registro

Los defectos van en el `resultado_pruebas.md` de la fase.

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Fórmula | Meta |
|---|---|---|
| Cobertura de exigencias | Criterios con caso / criterios de la fase | 100% |
| Casos ejecutados | Ejecutados / diseñados | 100% |

### 12.2 Dónde se miden

En el `resultado_pruebas.md` de la fase.
