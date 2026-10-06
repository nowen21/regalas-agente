# Plan de Pruebas · Fase `A-EP-025-HU-018-la-ayuda`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU018-A |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-018: CA-01 y CA-02 |
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
| Pantallas | Ayuda, manual y cobertura | Claude | Cliente de pruebas de Django | Sí |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-01, CA-02 |

### 3.3 Técnicas de diseño de casos

- Recorrer las rutas con nombre y las plantillas, en vez de una lista escrita a mano.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-01, CA-02 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Desde `proyectos/cimiento/`: `python manage.py test core`.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-018 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-018 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |

## 6. Casos de prueba

### CP-001 · Campos y pantallas

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir «Configuración» | Cada ajuste con su «?» y su globo; los botones de ayuda de la pantalla |
| 2 | Abrir cualquier pantalla | El botón «Ayuda» y el panel de la derecha |
| 3 | Pedir `/ayuda/pantalla/?vista=proyectos:suspensiones` | La sección de suspensiones |
| 4 | Una clave sin texto, en desarrollo | El «?» rojo |

### CP-002 · Manual y cobertura

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir `/ayuda/` | Todas las secciones y el botón de imprimir |
| 2 | Recorrer las rutas con nombre | Cada pantalla tiene su sección |
| 3 | Recorrer las plantillas | Cada clave usada tiene texto |
| 4 | Una sección que no existe | 404 |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | Una pantalla deja de abrir | Antes de cerrar la fase |
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
