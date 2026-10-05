# Plan de Pruebas · Fase `A-EP-025-HU-010-segunda-tanda`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU010-A |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-010: CA-01 a CA-03 |
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
| Unitario | Lector, trabajo y palabra | Claude | Muestras | Sí |
| Integración | Guardado y tablero | Claude | Base de pruebas en MariaDB | Sí |
| Manual | Volver a leer y abrir el tablero con el gasto real | Claude | La base local | No |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-01, CA-02, CA-03 |
| Rendimiento | ☑ | La parte que se recarga, con el gasto real |

### 3.3 Técnicas de diseño de casos

- Un turno partido en dos lecturas; un mensaje sin palabra clave; un turno que no toca archivos de una fase.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-01 | 100% |
| Media | CA-02, CA-03 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Desde `proyectos/cimiento/`: `python manage.py test core.consumo`, y `python -m unittest core.enganches.tests_limites` por el cambio del lector.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-010 | CA-01 | CP-001 | Funcional | Alta | Sí | ☐ |
| HU-010 | CA-02 | CP-002 | Funcional | Media | Sí | ☐ |
| HU-010 | CA-03 | CP-003 | Funcional | Media | Sí | ☐ |

## 6. Casos de prueba

### CP-001 · Mensajes, palabra y trabajo

| Campo | Valor |
|---|---|
| **HU / CA** | HU-010 / CA-01 |
| **Precondiciones** | T-01 a T-03 terminadas |
| **Datos de entrada** | Un `.jsonl` con «Hágalo» que edita un `plan_trabajo.md` de una fase, «Analicemos» que edita un `analisis-2.md`, y un mensaje sin palabra que no toca nada |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer y guardar | Tres mensajes con «Hágalo», «Analicemos» y vacío; trabajos: la fase, «análisis 2 del pendiente N» y vacío; cada llamada con su mensaje; ningún texto guardado |
| 2 | Partir el segundo turno en dos lecturas | Las llamadas de la segunda lectura quedan con el mismo mensaje |
| 3 | Leer otra vez | Nada duplicado |

### CP-002 · Herramientas y auxiliares

| Campo | Valor |
|---|---|
| **HU / CA** | HU-010 / CA-02 |
| **Precondiciones** | T-04 terminada |
| **Datos de entrada** | Bash y Edit con sus resultados; un auxiliar con su meta; un envío de telemetría con `prompt.id` y un `tool_result` de Bash |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer y guardar | Bash y Edit con el tamaño de su resultado; las llamadas del auxiliar con su tipo |
| 2 | Recibir el envío | La herramienta queda; la llamada queda con su mensaje si ya existe |

### CP-003 · Tablero

| Campo | Valor |
|---|---|
| **HU / CA** | HU-010 / CA-03 |
| **Precondiciones** | T-05 terminada |
| **Datos de entrada** | La muestra de CP-001 y CP-002 |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Sumar con `GastoDelPeriodo` | Por palabra, trabajo, herramienta, agente, modelo, tipo de token, contexto y últimos mensajes, con los números de la muestra |
| 2 | Abrir `/gasto/` | Las secciones nuevas |
| 3 | Volver a leer el gasto real y medir `/gasto/datos/` | Menos de un segundo |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | Se guarda el texto de un mensaje, o un número no coincide | Antes de cerrar la fase |
| **Baja** | Una marca de redacción | Antes de cerrar la fase |

### 9.2 Flujo del defecto

Un defecto se anota en el resultado de las pruebas. Si es un error dentro de lo que el plan aprobó, se corrige y se vuelve a correr el caso. Si para cerrar la fase obliga a tocar algo que el plan no declara, se resuelve en la conversación con el usuario.

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
