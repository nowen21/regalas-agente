# Plan de Pruebas · Fase `A-EP-025-HU-001-mariadb-y-plantilla-comun`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU001-A |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-001: CA-01 a CA-05 |
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
| Unitario | La página, el middleware, la orden y el paso del instalador | Claude | `.venv` de Cimiento | Sí |
| Integración | La base real y la página en el navegador | Claude | MariaDB de esta máquina | No |
| Revisión | La plantilla y la versión | Claude | Este repositorio | No |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-01 a CA-05 |
| Errores | ☑ | CA-02, CA-05 |

### 3.3 Técnicas de diseño de casos

- Partición por el estado de MariaDB: prendida o apagada.
- Partición por lo que ya existe: base creada o no, `node_modules/` instalado o no.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-01, CA-02, CA-05 | 100% |
| Media | CA-03, CA-04 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Desde `proyectos/cimiento/`: `python manage.py test core.inicio core.herramientas.tests_instalacion`; las marcas de lo que se va a guardar.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-001 | CA-01 | CP-001 | Funcional | Alta | No | ☐ |
| HU-001 | CA-02 | CP-002 | Errores | Alta | Sí | ☐ |
| HU-001 | CA-03 | CP-003 | Funcional | Media | No | ☐ |
| HU-001 | CA-04 | CP-004 | Funcional | Media | Sí | ☐ |
| HU-001 | CA-05 | CP-005 | Funcional | Alta | Sí | ☐ |

**Cobertura:** 5 de 5 criterios de esta fase.

## 6. Casos de prueba

### CP-001 · La base se crea y queda migrada

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-01 |
| **Precondiciones** | T-01 y T-02 terminadas; MariaDB prendida |
| **Datos de entrada** | El `.env` de esta máquina |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `manage.py preparar_base` | Dice que la base `cimiento` está lista |
| 2 | Repetir `manage.py preparar_base` | Lo mismo, sin errores ni cambios |
| 3 | `manage.py showmigrations` | Todas con `[X]` |
| 4 | Leer `.env.example` | Las cinco `DB_*`, sin valores |

### CP-002 · MariaDB apagada

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-02 |
| **Precondiciones** | T-02 y T-03 terminadas |
| **Datos de entrada** | `DB_PUERTO=3399`, donde no hay servidor |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `manage.py preparar_base` con `DB_PUERTO=3399` | Mensaje con `127.0.0.1:3399` y «prender MariaDB»; sale con error y sin traza de Python |
| 2 | Abrir `/` con la base que no responde (prueba automática) | Código 503 y la página dice que hay que prender MariaDB, con servidor y puerto |

### CP-003 · La plantilla Django admite npm

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-03 |
| **Precondiciones** | T-04 terminada |
| **Datos de entrada** | `plantillas/estructura-proyecto-django.md`, `CHANGELOG.md`, `VERSION` |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer el árbol y «Dependencias» | `package.json`, `package-lock.json` y `node_modules/` (no se versiona); cómo los lee Django |
| 2 | Leer `VERSION` y `CHANGELOG.md` | 54.2.0, con su entrada |

### CP-004 · La página de inicio con la plantilla común

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-04 |
| **Precondiciones** | T-05 y T-06 terminadas; `npm ci` corrido |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir `/` (prueba automática) | 200, con «Cimiento», «Inicio» en el menú, la hoja de Tabler y los guiones de htmx y ApexCharts |
| 2 | Pedir los cuatro estáticos a la vista que los sirve, con `DEBUG=True` (prueba automática) | 200 en cada uno |
| 3 | Abrir `/` en el servidor con la base real | «Base de datos: cimiento, en MariaDB 11.4.9» |

### CP-005 · La instalación prepara Cimiento

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-05 |
| **Precondiciones** | T-07 terminada |
| **Datos de entrada** | Un estándar en una carpeta temporal, con y sin `.venv` |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Simular la instalación en la carpeta del estándar | El paso «preparar Cimiento» sale antes de los enganches y no ejecuta nada |
| 2 | Aplicar sin `.venv` en Cimiento (prueba automática) | Queda como pendiente, con cómo crearlo; la instalación sigue |
| 3 | Aplicar con la orden que falla (prueba automática) | Queda como pendiente, con el mensaje de la orden |
| 4 | Aplicar en un proyecto que no es el estándar | El paso no aparece |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | Una credencial en un archivo versionado, o la instalación se cae sin MariaDB | Antes de cerrar la fase |
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
