# Plan de Pruebas · Fase `A-EP-025-HU-008-tablero-en-vivo`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU008-A |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-008: CA-01 a CA-03 |
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
| Integración | Sumas, vistas y filtros | Claude | Base de pruebas en MariaDB | Sí |
| Manual | La página con el gasto real | Claude | La base local | No |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-01, CA-02, CA-03 |
| Rendimiento | ☑ | La parte que se recarga, con el gasto real |

### 3.3 Técnicas de diseño de casos

- Dos proyectos, gasto de hoy y de hace 10 días, un enganche y un archivo con varias lecturas.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-01, CA-03 | 100% |
| Media | CA-02 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Desde `proyectos/cimiento/`: `python manage.py test core.consumo`.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-008 | CA-01 | CP-001 | Funcional | Alta | Sí | ☐ |
| HU-008 | CA-02 | CP-002 | Funcional | Media | Sí | ☐ |
| HU-008 | CA-03 | CP-003 | Funcional | Alta | Sí | ☐ |

## 6. Casos de prueba

### CP-001 · El tablero

| Campo | Valor |
|---|---|
| **HU / CA** | HU-008 / CA-01 |
| **Precondiciones** | T-01 a T-03 terminadas |
| **Datos de entrada** | La muestra de dos proyectos |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Sumar con `GastoDelPeriodo` | Totales, proyectos, días, sesiones, enganches y archivos con los números de la muestra |
| 2 | Abrir `/gasto/` con una cuenta de consulta | 200, con los totales con punto de miles y los datos de las gráficas |
| 3 | Abrir `/gasto/` sin cuenta | Manda a entrar |
| 4 | Abrir «Gasto» con el gasto real | Se ven los números y las gráficas |

### CP-002 · Filtros

| Campo | Valor |
|---|---|
| **HU / CA** | HU-008 / CA-02 |
| **Precondiciones** | T-04 terminada |
| **Datos de entrada** | La muestra de CP-001 |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `?proyecto=«id»` | Solo ese proyecto |
| 2 | `?dias=30` frente a `?dias=7` | Con 30 entra lo de hace 10 días; con 7, no |
| 3 | `?dias=99&proyecto=x` | Se ignoran: 7 días y todos los proyectos |

### CP-003 · En vivo

| Campo | Valor |
|---|---|
| **HU / CA** | HU-008 / CA-03 |
| **Precondiciones** | T-05 terminada |
| **Datos de entrada** | La muestra de CP-001 y un `.jsonl` |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir `/gasto/datos/`, crear una llamada y pedirla otra vez | El total sube |
| 2 | La página trae `hx-get` a `/gasto/datos/` cada 10 segundos | Está |
| 3 | Abrir `/gasto/` con un `.jsonl` sin leer | Lo del `.jsonl` queda en la base |
| 4 | Medir `/gasto/datos/` con el gasto real | Menos de un segundo |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | Un número no coincide con la base | Antes de cerrar la fase |
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
