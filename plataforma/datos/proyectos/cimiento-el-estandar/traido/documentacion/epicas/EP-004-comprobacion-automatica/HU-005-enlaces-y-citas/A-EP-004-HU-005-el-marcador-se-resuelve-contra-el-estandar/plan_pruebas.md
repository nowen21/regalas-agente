# Plan de Pruebas — «Fase A-EP-004-HU-005: el marcador se resuelve contra el estándar»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó al correrlas va en el `resultado_pruebas.md` de la misma fase, para no perder la línea base aprobada. La lista de tareas vive en el `plan_trabajo` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-004-HU-005 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-004-HU-005-el-marcador-se-resuelve-contra-el-estandar` |
| **Fecha** | 2026-08-16 |
| **Elaborado por** | El agente |
| **Aprobado por** | Pendiente — el usuario |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12**, como pide la plantilla por proporcionalidad.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Unitarias | La resolución del destino con marcador, desde dos raíces distintas | Carpetas temporales | Sí |
| Regresión | Que el veredicto sobre el propio estándar no cambie | El repositorio | Sí |

**Acá sí sirven las unitarias**, al revés que en la fase hermana de EP-007: el defecto vive dentro de una sola función y se reproduce llamándola con dos raíces.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | El CA-01 de la HU-005 |
| Compatibilidad | ☑ | Rutas con espacios y tildes |
| Rendimiento | ☐ | No aplica |
| Seguridad | ☐ | No aplica |

### 3.3 Técnicas de diseño de casos

- **Partición de equivalencia** — correr sobre el estándar (las dos carpetas coinciden) contra correr sobre una carpeta ajena (no coinciden). Es la partición donde vive el defecto.
- **Tabla de decisión** — dos entradas: si la raíz es el estándar o no, y si la regla que se cita existe o no. Cuatro combinaciones, y el veredicto tiene que depender **solo de la segunda**.
- **Triangulación** — el resultado esperado no sale de correr el programa: sale de mirar si el archivo existe en disco, que es una fuente independiente ([`08`](«RUTA-ESTANDAR»/base/08-pruebas.md)).

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)):

1. La suite nueva de esta fase (`test_enlaces_marcador.py`).
2. Las pruebas que ya existan de `enlaces.py`.
3. `validar.py estandar` entero, que es el consumidor directo.

**No** se corre la suite completa del repositorio.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-005 | [CA-01](../HU-005-enlaces-y-citas.md#ca-01--un-enlace-roto-se-reporta) | [CP-001](#cp-001--el-mismo-enlace-da-el-mismo-veredicto-desde-las-dos-raíces), [CP-002](#cp-002--el-marcador-que-apunta-a-lo-que-no-existe-se-reporta) | Funcional | Crítica | Sí | ☐ |
| HU-005 | No regresión | [CP-003](#cp-003--el-veredicto-sobre-el-propio-estándar-no-cambia) | Regresión | Crítica | Sí | ☐ |
| HU-005 | RNF — Compatibilidad | [CP-004](#cp-004--la-raíz-con-espacios-y-tildes-resuelve-igual) | Compatibilidad | Media | Sí | ☐ |

**Cobertura:** 3 de 3 exigencias cubiertas = 100%.

---

## 6. Casos de prueba

### CP-001 — El mismo enlace da el mismo veredicto desde las dos raíces

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-01 |
| **Tipo** | Funcional — el defecto que se corrige |
| **Prioridad** | Crítica |
| **Precondiciones** | Dos carpetas temporales: una que hace de proyecto y el estándar en su sitio |
| **Datos de entrada** | Un `.md` con un enlace con marcador a una regla **que sí existe** |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir el `.md` de prueba dentro de la carpeta que hace de proyecto | El archivo existe con su enlace |
| 2 | Comprobar en disco que la regla citada existe en el estándar | Existe — este es el resultado esperado, y no sale del programa |
| 3 | Correr la comprobación con la raíz apuntando al estándar | No reporta el enlace |
| 4 | Correr la comprobación con la raíz apuntando a la carpeta del proyecto | No reporta el enlace |
| 5 | Comparar los dos veredictos | Son iguales |

**Resultado esperado final:** el veredicto no depende de desde dónde se corra.
**Postcondiciones:** las carpetas temporales se borran.

> **Este caso falla hoy.** Con el código de ahora el paso 4 reporta el enlace como roto, porque busca la regla dentro del proyecto. Es la prueba que demuestra el defecto antes de arreglarlo.

---

### CP-002 — El marcador que apunta a lo que no existe se reporta

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-01 |
| **Tipo** | Funcional — caso negativo |
| **Prioridad** | Crítica |
| **Precondiciones** | Las mismas dos carpetas |
| **Datos de entrada** | Un `.md` con un enlace con marcador a una regla **inventada** |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir el `.md` con el enlace a la regla inventada | El archivo existe |
| 2 | Comprobar en disco que esa regla no existe | No existe |
| 3 | Correr la comprobación con la raíz en el estándar | Reporta el enlace, con su archivo y su línea |
| 4 | Correr la comprobación con la raíz en el proyecto | Reporta el mismo enlace |

**Resultado esperado final:** lo roto se sigue reportando desde las dos raíces. **El arreglo no puede volverse una excusa para callar.**

---

### CP-003 — El veredicto sobre el propio estándar no cambia

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / No regresión |
| **Tipo** | Regresión |
| **Prioridad** | Crítica |
| **Precondiciones** | La salida de `validar.py estandar` guardada **antes** del cambio (T-01 del plan de trabajo) |
| **Datos de entrada** | El repositorio del estándar tal como está |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `validar.py estandar` después del cambio | Termina y da su salida |
| 2 | Comparar esa salida contra la guardada antes | Son idénticas: mismas fallas, mismos avisos, mismo conteo |

**Resultado esperado final:** dentro del estándar no cambió nada, que es lo que se afirma en el plan.

> **Sin el paso 2 la afirmación no vale.** «No cambió nada» se comprueba comparando, no recordando.

---

### CP-004 — La raíz con espacios y tildes resuelve igual

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / RNF Compatibilidad |
| **Tipo** | Compatibilidad — valor límite |
| **Prioridad** | Media |
| **Precondiciones** | Una carpeta temporal con espacio y tilde en el nombre |
| **Datos de entrada** | El mismo `.md` del CP-001 |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Copiar el `.md` de prueba a la carpeta con espacio y tilde | El archivo existe ahí |
| 2 | Correr la comprobación con la raíz en esa carpeta | Da el mismo veredicto que el CP-001 |

**Resultado esperado final:** el nombre de la carpeta no cambia el veredicto.

> El repositorio del estándar vive en una ruta con espacios y tilde, así que este caso cubre la máquina donde se desarrolla. Ojo: el [punto 1 del pendiente 33](../../../../../pendientes/hecho/lo-que-quedo-abierto-en-las-sesiones-viejas.md) ya reportó que el validador da por rotos los enlaces con espacios. Si aparece acá, **se reporta y no se arregla en esta fase**: es otro defecto.

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que el veredicto siga dependiendo de la raíz, o que lo roto deje de reportarse | Inmediato |
| **Alta** | Que la salida sobre el estándar cambie sin explicación | Antes de cerrar |
| **Media** | Que la ruta con tilde dé distinto | Se reporta; puede quedar para el pendiente 33 |

### 9.2 Qué se hace con un defecto

Se diagnostica, se corrige y se vuelve a correr el caso. El ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — las 3 con caso |
| Casos ejecutados | 4 de 4 |
| Diferencia entre la salida de antes y la de después sobre el estándar | **0 líneas** |

El veredicto de cada caso y el concepto final van en el `resultado_pruebas.md` de esta fase.
