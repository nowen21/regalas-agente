# Plan de Pruebas · Fase `A-EP-025-HU-007-recepcion-de-la-telemetria`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU007-A |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-007: CA-01 a CA-04 |
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
| Unitario | Leer el envío | Claude | Envíos de muestra | Sí |
| Integración | La ruta y el guardado | Claude | Base de pruebas en MariaDB | Sí |
| Manual | Un envío a Cimiento prendido | Claude | La base local | No |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-01, CA-03, CA-04 |
| Errores | ☑ | CA-02 |

### 3.3 Técnicas de diseño de casos

- Envíos con los nombres de atributos de la documentación, con números como `intValue` en texto y como `doubleValue`.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-01, CA-03 | 100% |
| Media | CA-02, CA-04 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Desde `proyectos/cimiento/`: `python manage.py test core.consumo`, y la clase nueva de `tests_instalacion.py` importando `core.validadores` primero.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-007 | CA-01 | CP-001 | Funcional | Alta | Sí | ☐ |
| HU-007 | CA-02 | CP-002 | Errores | Media | Sí | ☐ |
| HU-007 | CA-03 | CP-003 | Funcional | Alta | Sí | ☐ |
| HU-007 | CA-04 | CP-004 | Funcional | Media | Sí | ☐ |

## 6. Casos de prueba

### CP-001 · Recepción y guardado

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-01 |
| **Precondiciones** | T-01 a T-03 terminadas; un proyecto registrado con `«sesión».jsonl` en su carpeta de Claude Code |
| **Datos de entrada** | Un envío con un `api_request` y un `tool_result` de `Read` de esa sesión |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer el envío con `EventosDeTelemetria` | Una llamada con modelo, tokens y solicitud; un archivo con ruta y tamaño |
| 2 | Mandarlo por `POST /v1/logs` | 200 con `{}`; la llamada y el archivo en la base, con su proyecto |
| 3 | Mandar un envío a Cimiento prendido, con `curl` | La llamada aparece en la base local |

### CP-002 · Envíos rechazados

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-02 |
| **Precondiciones** | T-04 terminada |
| **Datos de entrada** | El envío de CP-001 |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Mandarlo desde otra dirección | 403 y nada guardado |
| 2 | Mandar un JSON roto | 400 y nada guardado |
| 3 | Mandar un evento de una sesión sin proyecto | 200 y nada guardado |

### CP-003 · Los dos caminos

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-03 |
| **Precondiciones** | T-05 terminada |
| **Datos de entrada** | Un `.jsonl` y un envío con la misma solicitud |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Telemetría y después `leer_consumo` | Una llamada, con el `message.id` del `.jsonl` |
| 2 | `leer_consumo` y después telemetría | Una llamada |
| 3 | El mismo envío dos veces | Una llamada y un archivo |

### CP-004 · Activar en la instalación

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-04 |
| **Precondiciones** | T-06 terminada |
| **Datos de entrada** | Una configuración en una carpeta temporal |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Activar sobre una configuración sin `env` | Las variables quedan, con la dirección `http://127.0.0.1:«PUERTO»/v1/logs`; las demás claves siguen |
| 2 | Activar con una clave `OTEL_*` ya puesta por el usuario | Esa clave no cambia |
| 3 | Activar otra vez | «ya estaba» y el archivo no cambia |
| 4 | En simulación | Lo anuncia y no escribe |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | Se duplica una llamada, se guarda texto o se acepta un envío de otra máquina | Antes de cerrar la fase |
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
