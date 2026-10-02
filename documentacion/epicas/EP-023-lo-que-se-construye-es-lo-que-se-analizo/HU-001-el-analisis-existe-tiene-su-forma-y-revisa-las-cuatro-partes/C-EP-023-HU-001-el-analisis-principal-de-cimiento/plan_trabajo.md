# Plan de Trabajo · Fase `C-EP-023-HU-001-el-analisis-principal-de-cimiento` (módulo `analisis/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `C-EP-023-HU-001-el-analisis-principal-de-cimiento` |
| **Épica** | [EP-023](../../epica.md) |
| **HU** | [HU-001](../HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes.md), una sola (`F12.1`) |
| **Módulo** | `analisis/` |
| **Especificación del módulo** | La regla de negocio RN-03 de la HU-001 y `13·DOC25` |
| **Fecha apertura** | 2026-10-02 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): funcionalidad nueva. Depende de la [fase `A`](../A-EP-023-HU-001-el-analisis-tiene-regla-plantilla-y-validador/funcionalidad_implementada.md), que escribió `13·DOC25`.

**Carencias que cierra** (`02·F14` Q3): Cimiento no tiene un análisis principal que el análisis individual pueda alimentar (análisis 1 del pendiente 103, conclusión 49).

**Aprobación** (`02·F4`): el usuario aprobó este plan y el de pruebas el 2026-10-02.

**Disparo** (`02·F15`, etapa 2): el usuario pidió escribir esta fase el 2026-10-02 con «Escriba».

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-001 | Estado |
|---|---|
| CA-08 · Existe el análisis principal de Cimiento | ☐ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que Cimiento tenga en `analisis/` su análisis principal, que diga lo que se va a construir hoy y lleve la lista de cambios que lo trajeron hasta ahí.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-08 | El análisis principal existe, se basa en todo el proyecto y en el análisis 1, y lleva su lista de cambios | Documentación | Media |

**Fuera de alcance:**

- Reescribir el planteamiento o las épicas: el análisis principal los enlaza, no los copia.
- Mover o cambiar `analisis/base-2026-08-07-cumplimiento-meta-reglas.md`, que queda con la forma vieja (análisis 1, conclusión 38).

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medido el 2026-10-02:

- `analisis/` tiene un solo análisis, `base-2026-08-07-cumplimiento-meta-reglas.md`, y su `README.md`.
- El `README.md` dice que un análisis es una «fotografía» y que se nombra `<ámbito>-AAAA-MM-DD-<tema>.md`. Lo primero es lo que pedía `13·DOC8`, derogada en la 40.0.0.
- `planteamiento.md` dice la necesidad, el objetivo, el alcance y las restricciones de Cimiento, y nombra las épicas que salen de él.
- `documentacion/epicas/README.md` lista las 23 épicas con su estado.
- Los análisis individuales que cambiaron lo que se construye son los análisis 1, 2, 4 y 5 del pendiente 103. El 3 no cambió nada.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `analisis/proyecto-2026-10-02-analisis-principal.md` | Nuevo | Documentación | El análisis principal de Cimiento |
| `analisis/README.md` | Modificar | Documentación | El índice lo nombra, y el texto deja de decir que el análisis es una fotografía |
| Los documentos de esta fase, la HU-001 y el resumen de la sesión | Modificar | Documentación | Cierre |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

No aplica: no se cambia ningún contrato.

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El análisis principal enlaza el planteamiento y las épicas | Copiar su contenido | Un registro en dos sitios se queda atrás (S-064) |
| Se nombra con la forma del `README.md` de `analisis/` | Un nombre nuevo | No se inventa una convención; la fecha es la de creación |
| La lista de cambios arranca con los análisis 1, 2, 4 y 5 del pendiente 103 | Incluir el 3 | El 3 no cambió lo que se construye |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 Qué cambia técnicamente  ·  `02·F14` Q5

| Artefacto | Hoy | Después | Regla que aplica |
|---|---|---|---|
| Análisis principal | No existe | Qué es Cimiento, qué se construye hoy y su lista de cambios | `13·DOC25` |
| `analisis/README.md` | Habla de fotografías y de un solo análisis | Nombra el principal y dice cómo cambia | `13·DOC17`, `13·DOC25` |

## 3. Desglose de tareas por criterio de aceptación

Cada tarea dice qué y cómo, dónde, por qué e impacto (`02·F16`).

### CA-08 · Existe el análisis principal de Cimiento

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | Crear el análisis principal: qué es Cimiento y qué se construye hoy, enlazando el planteamiento y el índice de épicas, y su lista de cambios con la fecha y el enlace de cada análisis individual que la cambió | `analisis/proyecto-2026-10-02-analisis-principal.md` | CA-08 | Ninguno | 1 h | Ninguna | CP-001, CP-002 |
| T-02 | Agregarlo al índice y cambiar el texto que habla de fotografías por lo que piden `13·DOC24` y `13·DOC25` | `analisis/README.md` | CA-08 | Ninguno | 0,3 h | T-01 | CP-003 |

## 4. Secuencia de ejecución

T-01 y T-02. Al final, `validar.py estandar` y la medición de marcas (`02·F5`).

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-08 | Leer el análisis principal y su lista de cambios; leer el índice | CP-001 a CP-003 |

## 6. Datos y ambiente de prueba

El repositorio del estándar.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

No aplica: `analisis/` es del estándar y no viaja a los proyectos que heredan. No cambia `base/` ni `plantillas/`, así que no sube la versión.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`13·DOC17`, `13·DOC24`, `13·DOC25`, `00·ID8`, `02·F5`, `02·F8`, `02·F18`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Que el análisis principal repita lo que ya dicen el planteamiento y las épicas | Los enlaza; solo dice lo que no está en ningún otro sitio |

## 11. Definition of Done

- [ ] El CA-08 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] `validar.py estandar` sin fallas y cero marcas nuevas.
- [ ] Aprobación del usuario.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Se llena al cerrar la fase.
