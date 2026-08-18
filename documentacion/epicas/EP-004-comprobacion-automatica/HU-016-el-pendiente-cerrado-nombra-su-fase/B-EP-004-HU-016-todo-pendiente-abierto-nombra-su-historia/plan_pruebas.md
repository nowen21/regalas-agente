# Plan de Pruebas — Fase B-EP-004-HU-016: todo pendiente abierto nombra su historia

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó al correrlas va en el `resultado_pruebas.md` de la misma fase. La lista de tareas vive en el [plan_trabajo.md](plan_trabajo.md) de esta fase.

| Campo | Valor |
|---|---|
| **Código** | PP-B-EP-004-HU-016 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `B-EP-004-HU-016-todo-pendiente-abierto-nombra-su-historia` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Pendiente — el usuario |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12**, como pide la plantilla por proporcionalidad.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Unitarias | Que la ficha se lea bien y la historia resuelva | Carpetas temporales | Sí |
| Regresión | Que los 33 pendientes ya enrutados sigan sin reportarse | El repositorio, solo lectura | Sí |

**Acá sirven las unitarias:** todo el comportamiento vive en la lectura de un archivo de texto y se reproduce con archivos de mentira.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los `CA-05`, `CA-06` y `CA-07` |
| Límites | ☑ | Ficha vacía, sin ficha, fila duplicada, tabla que no es la ficha |
| Rendimiento | ☐ | 40 archivos de texto |
| Seguridad | ☐ | No aplica |

### 3.3 Técnicas de diseño de casos

- **Partición de equivalencia** — cuatro clases de archivo: con fila buena, sin fila, con fila que no resuelve, y declarado tema. El veredicto tiene que depender solo de la clase.
- **Valor límite** — la fila vacía, que es lo que separa una declaración de un descuido.
- **Caso histórico como caso de prueba** — el error del 18, el 19 y el 23, donde la fila cayó dentro de una tabla de contenido. Un defecto que ya ocurrió una vez es el mejor caso de prueba que hay.
- **Triangulación** — el resultado esperado no sale de correr el programa: sale de abrir el archivo y mirar si la fila está y si el destino existe en disco.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)):

1. La suite nueva de esta fase (`test_pendientes_historia.py`).
2. Las pruebas que ya existan de `pendientes.py`.
3. `validar.py pendientes` y `validar.py estandar` sobre el repositorio, que son los consumidores directos.
4. **La suite completa del repositorio**, una vez, al final: el archivo que se toca lo usa el subcomando que corre en cada sesión.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-016 | [CA-05](../HU-016-el-pendiente-cerrado-nombra-su-fase.md#ca-05--un-pendiente-abierto-sin-historia-se-reporta) | [CP-001](#cp-001--el-abierto-sin-la-fila-se-reporta), [CP-005](#cp-005--la-fila-fuera-de-la-ficha-no-cuenta-como-fila) | Funcional | Crítica | Sí | ☐ |
| HU-016 | [CA-06](../HU-016-el-pendiente-cerrado-nombra-su-fase.md#ca-06--la-historia-nombrada-existe) | [CP-002](#cp-002--la-historia-inventada-se-reporta) | Funcional | Crítica | Sí | ☐ |
| HU-016 | [CA-07](../HU-016-el-pendiente-cerrado-nombra-su-fase.md#ca-07--el-tema-declarado-no-se-reporta) | [CP-003](#cp-003--el-tema-declarado-pasa-y-la-fila-vacía-no) | Funcional | Crítica | Sí | ☐ |
| HU-016 | Transversal — Límites | [CP-005](#cp-005--la-fila-fuera-de-la-ficha-no-cuenta-como-fila), [CP-006](#cp-006--los-casos-borde-del-archivo) | Límites | Alta | Sí | ☐ |
| HU-016 | Transversal — No regresión | [CP-004](#cp-004--los-33-enrutados-siguen-en-verde) | Regresión | Crítica | Sí | ☐ |

**Cobertura:** 5 de 5 exigencias con caso = 100%. **Las dos transversales tienen caso propio**, y se cuentan en el total: el defecto de método del 2026-08-17 fue declarar «100%» sin contarlas.

---

## 6. Casos de prueba

### CP-001 — El abierto sin la fila se reporta

| Campo | Valor |
|---|---|
| **HU / CA** | HU-016 / CA-05 |
| **Tipo** | Funcional — el defecto que se corrige |
| **Prioridad** | Crítica |
| **Precondiciones** | Una carpeta temporal que hace de `pendientes/` |
| **Datos de entrada** | Dos archivos: uno con la fila y una historia real, otro sin fila. Los dos declaran `**Estado:** abierto` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir los dos archivos en la carpeta temporal | Existen |
| 2 | Abrir el segundo y confirmar a ojo que no tiene la fila | No la tiene — este es el resultado esperado, y no sale del programa |
| 3 | Correr la comprobación sobre la carpeta | Reporta **el segundo y solo el segundo**, con su nombre de archivo |
| 4 | Leer el mensaje | Dice qué fila falta y dónde escribirla, no solo que algo está mal |

**Resultado esperado final:** el abierto sin historia se reporta; el que la tiene, no.
**Postcondiciones:** la carpeta temporal se borra.

> **Este caso falla hoy:** el paso 3 no reporta nada, porque la comprobación no existe.

---

### CP-002 — La historia inventada se reporta

| Campo | Valor |
|---|---|
| **HU / CA** | HU-016 / CA-06 |
| **Tipo** | Funcional |
| **Prioridad** | Crítica |
| **Precondiciones** | La misma carpeta temporal |
| **Datos de entrada** | Un archivo cuya fila enlaza a `EP-009 · HU-042`, que no existe, y otro que enlaza a una historia real |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Comprobar en disco que `EP-009 · HU-042` no existe, y que la otra sí | Así es |
| 2 | Correr la comprobación | Reporta el primero, nombrando el identificador que no resolvió |
| 3 | Cambiar el enlace por uno real y volver a correr | No reporta nada |

**Resultado esperado final:** la inventada se reporta y la real no. **Sin esto la fila se llena con cualquier cosa y el campo pasa a ser decoración.**

---

### CP-003 — El tema declarado pasa, y la fila vacía no

| Campo | Valor |
|---|---|
| **HU / CA** | HU-016 / CA-07 |
| **Tipo** | Funcional — la excepción |
| **Prioridad** | Crítica |
| **Precondiciones** | La misma carpeta temporal |
| **Datos de entrada** | Un archivo con la fila declarando que es un tema, y el mismo archivo con la fila vacía |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr con la declaración puesta | No lo reporta |
| 2 | Borrar el texto dejando `\| **Historia de usuario** \| \|` | — |
| 3 | Correr otra vez | Lo reporta |
| 4 | Correr sobre el backlog real y mirar el 01, el 09, el 10 y el 33 | Ninguno de los cuatro se reporta |

**Resultado esperado final:** la declaración con texto pasa y la fila vacía no. **Una fila vacía no es una declaración: es un descuido con forma de declaración.**

---

### CP-004 — Los 33 enrutados siguen en verde

| Campo | Valor |
|---|---|
| **HU / CA** | HU-016 / No regresión |
| **Tipo** | Regresión |
| **Prioridad** | Crítica |
| **Precondiciones** | La salida de `validar.py pendientes` guardada **antes** del cambio (T-01) |
| **Datos de entrada** | El backlog real, **solo de lectura** |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `validar.py pendientes` después del cambio | Termina y da su salida |
| 2 | Comparar contra la guardada en T-01 | Ninguna falla nueva. Los hallazgos que ya había siguen igual |
| 3 | Correr `validar.py estandar` | Sigue en 0 fallas |
| 4 | Correr la suite completa del repositorio | Las 36 siguen pasando, más las nuevas |

**Resultado esperado final:** el enrutamiento del 2026-08-17 pasa la comprobación que se acaba de escribir. Si no pasa, o el enrutamiento estaba mal o el programa lo está leyendo mal, y hay que averiguar cuál de las dos **antes** de tocar ningún pendiente.

> **Ojo con la trampa:** editar un pendiente para que el programa lo acepte es exactamente la salida mala que describe el [pendiente 55](../../../../../pendientes/hecho/los-enlaces-de-ejemplo-no-son-enlaces.md) — redactar torcido para callar al validador. Si un archivo se reporta, primero se mira si el reporte tiene razón.

---

### CP-005 — La fila fuera de la ficha no cuenta como fila

| Campo | Valor |
|---|---|
| **HU / CA** | HU-016 / CA-05 y Límites |
| **Tipo** | Límites — **caso histórico** |
| **Prioridad** | Alta |
| **Precondiciones** | La misma carpeta temporal |
| **Datos de entrada** | Un archivo donde la fila `Historia de usuario` está dentro de una tabla de contenido con encabezados propios, y no dentro de la ficha |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir el archivo copiando la forma que tuvieron el 18, el 19 y el 23 el 2026-08-17 | Existe |
| 2 | Correr la comprobación | **Lo reporta**, porque la fila no está en la ficha |
| 3 | Mover la fila a la ficha y volver a correr | No reporta nada |

**Resultado esperado final:** el programa distingue la ficha de cualquier tabla.

> **Este caso ya ocurrió.** El 2026-08-17 el script de enrutamiento metió la fila en la tabla equivocada en tres archivos, y ningún validador lo habría visto: el enlace resolvía y el conteo daba 33 de 33. Un defecto que ya pasó una vez merece su caso.

---

### CP-006 — Los casos borde del archivo

| Campo | Valor |
|---|---|
| **HU / CA** | HU-016 / Límites |
| **Tipo** | Límites |
| **Prioridad** | Alta |
| **Precondiciones** | La misma carpeta temporal |
| **Datos de entrada** | Cinco archivos, uno por caso |

**Pasos**

| # | Caso | Resultado esperado |
|---|---|---|
| 1 | Archivo sin ninguna tabla | Se reporta: falta la fila |
| 2 | Archivo con ficha pero sin la fila | Se reporta |
| 3 | Archivo con la fila dos veces, con historias distintas | Se reporta la ambigüedad, y no se elige una en silencio |
| 4 | Archivo cerrado sin la fila | **No** se reporta por el `CA-05`: los cerrados son de la fase A |
| 5 | Carpeta de pendientes vacía | No se reporta nada, y el programa no se cae |

**Resultado esperado final:** ningún borde tumba la corrida ni pasa desapercibido.

> El caso 3 es el que más cuesta decidir y por eso está escrito: **elegir una de las dos en silencio sería el peor comportamiento posible**, porque el archivo diría una cosa y el programa creería otra.

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que un abierto sin historia pase, o que uno de los 33 se reporte sin razón | Inmediato |
| **Alta** | Que la fila fuera de la ficha cuente como fila (CP-005) | Antes de cerrar |
| **Media** | Que el mensaje no diga dónde escribir la fila | Se reporta; puede quedar para otra fase |

### 9.2 Qué se hace con un defecto

Se diagnostica, se corrige y se vuelve a correr el caso. El ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

**Y lo que aparezca fuera de estos CA se propone, no se arregla de paso** ([`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md)).

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — las 5 con caso, **transversales incluidas** |
| Casos ejecutados | 6 de 6 |
| Pendientes de los 33 reportados por el programa nuevo | **0** |
| Fallas nuevas en `validar.py estandar` | **0** |
| Pruebas del repositorio que dejan de pasar | **0** |

El veredicto de cada caso y el concepto final van en el `resultado_pruebas.md` de esta fase. **Un solo concepto, sin estado intermedio:** Cumple o No cumple.
