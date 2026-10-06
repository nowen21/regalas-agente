# Plan de Pruebas · Fase `A-EP-025-HU-015-tercera-tanda`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU015-A |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-015: CA-01 y CA-02 |
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
| Integración | Lector, guardado y tablero | Claude | Base de pruebas en MariaDB | Sí |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-01, CA-02 |
| Privacidad | ☑ | Ningún comando completo |

### 3.3 Técnicas de diseño de casos

- Muestras con y sin texto al modelo; repeticiones en el borde de tres.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-01, CA-02 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Desde `proyectos/cimiento/`: `python manage.py test core.consumo`.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-015 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-015 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |

## 6. Casos de prueba

### CP-001 · Sin tokens

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer una muestra con un enganche que entrega contexto y otro que no | Dos ejecuciones guardadas; leer otra vez no duplica |
| 2 | «Lo que corre sin tokens» | Los dos, con sus veces, el segundo con cero tokens |

### CP-002 · Candidatos

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Comandos `git status --short`, `python manage.py test x`, `python -m unittest y` | Órdenes `git status`, `python manage.py`, `python -m unittest`; nada más del comando |
| 2 | Un archivo leído tres veces, otro dos | Solo el primero, con lo que se ahorraría |
| 3 | Un enganche en todos los mensajes, otro en uno | Solo el primero |
| 4 | Un comando tres veces | Aparece con lo que se ahorraría |
| 5 | La página | Trae las dos secciones |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | Se guarda un comando completo | Antes de cerrar la fase |
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
