# Plan de Pruebas · Fase `A-EP-025-HU-004-niveles-por-proyecto`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU004-A |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-004: CA-01 a CA-04 |
| **Fecha** | 2026-10-04 |
| **Elaborado por** | Claude |
| **Revisado por** | Ing. José Dúmar Jiménez Ruíz |
| **Aprobado por** | [Análisis 1 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md), el 2026-10-04 |
| **Estado** | Aprobado |

Para una fase, la plantilla pide las secciones 3, 5, 6, 9 y 12; las demás son opcionales y no se usan.

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Unitario | El catálogo de reglas | Claude | El `base/` real | Sí |
| Integración | Pantalla, guardado, historial y permisos | Claude | Base de pruebas en MariaDB | Sí |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-01, CA-03 |
| Validación | ☑ | CA-02 |
| Seguridad | ☑ | CA-04 |

### 3.3 Técnicas de diseño de casos

- Partición del envío: regla del catálogo, del núcleo, inventada; nivel válido e inválido.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-01, CA-02, CA-04 | 100% |
| Media | CA-03 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Desde `proyectos/cimiento/`: `python manage.py test core.niveles core.proyectos core.cuentas core.inicio`.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-004 | CA-01 | CP-001 | Funcional | Alta | Sí | ☐ |
| HU-004 | CA-02 | CP-002 | Validación | Alta | Sí | ☐ |
| HU-004 | CA-03 | CP-003 | Funcional | Media | Sí | ☐ |
| HU-004 | CA-04 | CP-004 | Seguridad | Alta | Sí | ☐ |

**Cobertura:** 4 de 4 criterios de esta fase.

## 6. Casos de prueba

### CP-001 · Cambiar el nivel en un proyecto

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / CA-01 |
| **Precondiciones** | T-01 a T-03 terminadas |
| **Datos de entrada** | Dos proyectos; una cuenta administradora |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer el catálogo | Trae `02·F8`; ninguna del núcleo ni derogada; agrupado por capítulo |
| 2 | Abrir las reglas del primer proyecto | Todas en «frena» |
| 3 | Enviar `02·F8` en «avisa» | `02·F8` en «avisa» en el primero |
| 4 | Abrir las del segundo | `02·F8` en «frena» |
| 5 | Enviar sin cambios | Ninguna fila nueva |

### CP-002 · Núcleo y nivel inválido

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / CA-02 |
| **Precondiciones** | T-04 terminada |
| **Datos de entrada** | Un proyecto; una cuenta administradora |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir las reglas | `00·N1` no aparece |
| 2 | Enviar `00·N1` en «apagada» junto con `02·F8` en «avisa» | Mensaje de error; nada guardado, tampoco `02·F8` |
| 3 | Enviar una regla inventada | Mensaje de error; nada guardado |
| 4 | Enviar `02·F8` en un nivel que no existe | Mensaje de error; nada guardado |

### CP-003 · Historial

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / CA-03 |
| **Precondiciones** | T-05 terminada |
| **Datos de entrada** | Un cambio guardado |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir el historial | `02·F8`, «frena», «avisa», la cuenta y la fecha |

### CP-004 · Consulta solo ve

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / CA-04 |
| **Precondiciones** | T-06 terminada |
| **Datos de entrada** | Una cuenta de consulta |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir las reglas | 200, con los niveles y sin «Guardar» |
| 2 | Enviar un cambio | 403; nada guardado |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | Se guarda un nivel del núcleo, o consulta cambia un nivel | Antes de cerrar la fase |
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
