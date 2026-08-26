# Plan de Pruebas — «Fase B-EP-007-HU-001: prepara su propia salida»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de la misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-B-EP-007-HU-001 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `B-EP-007-HU-001-prepara-su-propia-salida` |
| **Fecha** | 2026-08-16 |
| **Elaborado por** | El agente |
| **Aprobado por** | El usuario, en el mismo mensaje que disparó la fase |
| **Estado** | Aprobado |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12**.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Integración | Correr la instalación entera con la salida puesta en una codificación que no admite la flecha | Carpeta temporal | Sí |

**Por qué hay que forzar la codificación.** Bajo `unittest` la salida suele venir ya en UTF-8, así que una prueba que solo llame a `instalar()` pasa en verde **con el defecto puesto**. Sin forzarla, el caso no prueba nada — y una prueba que no puede fallar es peor que ninguna, porque da confianza falsa.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Robustez | ☑ | El CA-01 de la HU-001 |
| No regresión | ☑ | Que las demás pruebas sigan pasando con la salida restaurada |

### 3.3 Técnicas de diseño de casos

- **Valores límite** — la codificación más pobre de las que se encuentran en esta máquina (`cp1252`), que es justo la que no admite `→`.
- **Prueba de la prueba** — se revierte el arreglo a propósito y el caso tiene que ponerse rojo. Es lo que cierra el riesgo `B-01`.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): la carpeta `validadores/tests/` entera, que son 18 pruebas y corre en segundos. Las dos suites de instalación se tocan en esta fase y la tercera comparte proceso, así que aislarlas más no ahorra nada.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-001 | [CA-01](../HU-001-instalar-con-una-linea.md#ca-01--una-línea-deja-el-proyecto-listo) | [CP-001](#cp-001--instalar-no-revienta-con-una-consola-que-no-admite-la-flecha) | Robustez | Alta | Sí | ☐ |
| HU-001 | CA-01 · prueba de la prueba | [CP-002](#cp-002--el-caso-se-pone-rojo-si-se-revierte-el-arreglo) | Verificación | Alta | No — se hace a mano una vez | ☐ |

**Cobertura:** 1 de 1 exigencia cubierta = 100%.

---

## 6. Casos de prueba

### CP-001 — Instalar no revienta con una consola que no admite la flecha

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-01 |
| **Tipo** | Robustez |
| **Prioridad** | Alta |
| **Precondiciones** | Carpeta temporal vacía y copia desechable del estándar |
| **Datos de entrada** | La ruta de la carpeta temporal |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Cambiar la salida del proceso por una que escriba en `cp1252` y no perdone lo que no cabe | La salida queda en esa codificación |
| 2 | Comprobar que esa salida **no** admite `→` | Al intentar escribirla directo, falla |
| 3 | Correr `instalar(...)` con `aplicar=True`, sin que nadie haya preparado la salida | Termina sin reventar |
| 4 | Leer lo que se imprimió | Está el avance de la instalación |
| 5 | Restaurar la salida del proceso | Queda como estaba |

**Resultado esperado final:** el instalador prepara su propia salida y no depende de quien lo llame.
**Postcondiciones:** la salida del proceso queda como estaba, para no arrastrar el cambio a las otras pruebas.

> **El paso 2 no sobra.** Si la salida que se armó sí admitiera la flecha, el caso pasaría siempre. Comprobar primero que no la admite es lo que le da valor al paso 3.

---

### CP-002 — El caso se pone rojo si se revierte el arreglo

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-01 · verificación del propio caso |
| **Tipo** | Verificación manual, una sola vez |
| **Prioridad** | Alta |
| **Precondiciones** | El CP-001 pasó |
| **Datos de entrada** | Ninguno |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Quitar la línea que agrega el T-01 | El arreglo queda revertido |
| 2 | Correr el CP-001 | Se pone rojo, con `UnicodeEncodeError` |
| 3 | Volver a poner la línea | El arreglo vuelve |
| 4 | Correr el CP-001 | Verde otra vez |

**Resultado esperado final:** la prueba mide lo que dice medir.

> **Por qué va.** Es el riesgo `B-01` del plan de trabajo. Una prueba de robustez que nunca se vio fallar no se sabe si comprueba algo o si el escenario que arma no reproduce el defecto.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | El instalador sigue reventando después del cambio | Inmediato |
| **Alta** | La prueba pasa en verde con el arreglo revertido | Inmediato — el caso no sirve |
| **Media** | Forzar la codificación deja rotas las otras pruebas | Antes de cerrar |

Se diagnostica, se corrige y se vuelve a correr el caso. El ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — la 1 con caso |
| Casos ejecutados | 2 de 2 |
| Pruebas del repositorio en verde | 19 de 19 |
| Llamadas a `preparar_salida()` fuera del propio programa | **0** |

El veredicto va en el `resultado_pruebas.md` de esta fase.
