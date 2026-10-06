# Plan de Pruebas · Fase `A-EP-025-HU-014-rutas-y-hook-md`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU014-A |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-014: CA-01 y CA-02 |
| **Fecha** | 2026-10-05 |
| **Elaborado por** | Claude |
| **Revisado por** | Ing. José Dúmar Jiménez Ruíz |
| **Aprobado por** | [Análisis 2 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-2.md), el 2026-10-05 |
| **Estado** | Aprobado |

Para una fase, la plantilla pide las secciones 3, 5, 6, 9 y 12; las demás son opcionales y no se usan.

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Integración | Rutas con el ajuste | Claude | Base de pruebas en MariaDB | Sí |
| Unitario | El enganche de los `.md` | Claude | Carpetas temporales | Sí |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-01, CA-02 |

### 3.3 Técnicas de diseño de casos

- Cada valor del ajuste, con y sin registro; un `.md` con enlace roto y marca.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-01, CA-02 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Desde `proyectos/cimiento/`: `python manage.py test core.proyectos`, `python -m unittest core.enganches.tests_md core.enganches.tests_limites`, y `core.enganches.tests_freno` importando `core.validadores` primero.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-014 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-014 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |

## 6. Casos de prueba

### CP-001 · Rutas

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Proyecto registrado con «completas» | `mostrar` da la ruta completa |
| 2 | Con «relativas», o en la base pero sin registro | Relativa al proyecto |
| 3 | Una ruta de afuera | Completa, como siempre |

### CP-002 · El enganche de los `.md`

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Editar un `.md` con un enlace roto | Código 2, nombra el enlace |
| 2 | Escribir una marca de redacción | El aviso de marcas, con su línea |
| 3 | Editar algo que no es `.md`, o de otro proyecto | Código 0, sin aviso; la sesión queda anotada |
| 4 | El adaptador | No importa nada de `validadores/` |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | El enganche deja pasar un enlace roto | Antes de cerrar la fase |
| **Baja** | Una marca de redacción | Antes de cerrar la fase |

### 9.2 Flujo del defecto

Un defecto se anota en el resultado. Si se corrige dentro del plan, se vuelve a correr el caso; si pide tocar algo que el plan no declara, se resuelve en la conversación con el usuario.

### 9.3 Contenido mínimo de un reporte

- Caso y paso donde apareció.
- Resultado esperado frente al obtenido.

### 9.4 Registro

En el `resultado_pruebas.md` de la fase.

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Fórmula | Meta |
|---|---|---|
| Cobertura de exigencias | Criterios con caso / criterios de la fase | 100% |
| Casos ejecutados | Ejecutados / diseñados | 100% |

### 12.2 Dónde se miden

En el `resultado_pruebas.md` de la fase.
