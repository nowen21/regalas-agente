# Plan de Pruebas · Fase `A-EP-025-HU-009-avisos-por-limite`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU009-A |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-009: CA-01 a CA-03 |
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
| Unitario | Turno, límites y aviso | Claude | Transcripciones de muestra | Sí |
| Integración | El enganche entero | Claude | Proceso aparte con la entrada estándar | Sí |
| Manual | Un límite bajo en el registro real | Claude | La base local | No |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-01, CA-02, CA-03 |
| Errores | ☑ | Sin base, sin transcripción |

### 3.3 Técnicas de diseño de casos

- Valores límite: justo en el límite no avisa; uno más, sí.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-01, CA-02 | 100% |
| Media | CA-03 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Desde `proyectos/cimiento/`: `python -m unittest core.enganches.tests_limites`, y `python manage.py test core.consumo core.proyectos` por el cambio del lector y de los límites.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-009 | CA-01 | CP-001 | Funcional | Alta | Sí | ☐ |
| HU-009 | CA-02 | CP-002 | Funcional | Alta | Sí | ☐ |
| HU-009 | CA-03 | CP-003 | Funcional | Media | Sí | ☐ |

## 6. Casos de prueba

### CP-001 · Aviso

| Campo | Valor |
|---|---|
| **HU / CA** | HU-009 / CA-01 |
| **Precondiciones** | T-01 a T-03 terminadas |
| **Datos de entrada** | Una transcripción con dos mensajes; en el turno del primero, un enganche y un archivo por encima del límite, y otros por debajo |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `turno_anterior` con el segundo mensaje escrito y sin respuesta | Solo lo del turno del primero |
| 2 | `turno_anterior` sin que el segundo esté escrito | Lo mismo |
| 3 | `pasados_del_limite` con límites 100 y 1000 | El enganche y el archivo grandes; el que está justo en el límite, no |
| 4 | Correr `hook_presupuesto.py --modo aviso` con esa transcripción | El aviso, y sale con 0 |

### CP-002 · Una vez

| Campo | Valor |
|---|---|
| **HU / CA** | HU-009 / CA-02 |
| **Precondiciones** | T-01 terminada |
| **Datos de entrada** | La transcripción de CP-001 con un tercer mensaje y un turno sin excesos |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Revisar con el tercer mensaje | Sin aviso |

### CP-003 · Límites del proyecto

| Campo | Valor |
|---|---|
| **HU / CA** | HU-009 / CA-03 |
| **Precondiciones** | T-04 terminada |
| **Datos de entrada** | Lecturas falsas de la base |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `LimitesDelProyecto` con una fila | Esos límites |
| 2 | Sin fila | 2000 y 10 000 |
| 3 | Sin base | 2000 y 10 000, sin error |
| 4 | Límite por enganche de 100 en el registro de este proyecto; correr el enganche sobre la sesión real | Aviso con el límite 100; después se devuelve el límite a 2000 |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | El enganche falla o detiene algo; un exceso se avisa dos veces | Antes de cerrar la fase |
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
