# Plan de Trabajo · Fase `D-EP-004-HU-012-las-marcas-se-miden-al-escribir` (módulo Comprobación automática)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba acepta el alcance y el costo. El requisito vive en la HU, el detalle de las pruebas en el `plan_pruebas` de la misma fase, y lo que quedó hecho en el `funcionalidad_implementada.md` del cierre.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `D-EP-004-HU-012-las-marcas-se-miden-al-escribir` |
| **Épica** | [EP-004](../../epica.md) |
| **HU** | [HU-012](../HU-012-marcas-de-generacion-automatica.md), una sola (`F12.1`) |
| **Módulo** | Comprobación automática: `validadores/marcas.py`, el enganche `hook_md.py`, el molde `plantillas/sesion.md` y quien lo lee, `validadores/resumen.py` |
| **Especificación del módulo** | RN-06 y RN-07 de la HU-012 |
| **Fecha apertura** | 2026-09-28 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- Sale del [pendiente 102](../../../../../pendientes/102-las-reglas-de-redaccion-se-miden-al-escribir-el-documento.md), aprobado el 2026-09-28, y del H-4 de esa sesión. Retoma las fases `A` a `C`, que dejaron el contador de marcas y los moldes del ciclo en cero.

**CA de la HU que cubre esta fase** (trazabilidad `13·DOC11`):

| CA de HU-012 que cierra esta fase | Estado |
|---|---|
| [CA-05](../HU-012-marcas-de-generacion-automatica.md#ca-05--lo-que-se-escribe-se-mide-al-escribirlo) | ☐ |
| [CA-06](../HU-012-marcas-de-generacion-automatica.md#ca-06--el-molde-del-resumen-de-sesión-no-produce-marcas-al-llenarse) | ☐ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que el agente se entere de las marcas de lo que escribe en el mismo turno en que lo escribe, y que llenar un resumen de sesión deje de producirlas por la forma del molde.

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-05 | Al escribir un `.md`, llegan en ese turno las marcas de lo recién escrito | Funcional | Media |
| CA-06 | El molde del resumen, lleno, da cero marcas y sigue legible para `resumen.py` | Funcional | Media |
| RNF | Versionado y pruebas | No funcional | Baja |

**Fuera de alcance:**

- Corregir los documentos ya escritos y las transcripciones, que son literales.
- Cambiar qué cuenta la lista de marcas.
- La caja de reglas copiada en las plantillas, que es de H-3.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Revisado el 2026-09-28:

- `hook_md.py` corre en cada `Write|Edit` (`validadores/instalar.py`, línea 266) y revisa enlaces. Si hay fallas sale con código 2 y la herramienta se las devuelve al modelo. No cuenta marcas.
- El `pre-commit` cuenta las marcas nuevas, solo como aviso y solo al guardar.
- `marcas.py` ya tiene `marcas_de_linea` y `_cuenta`, que saltan código y sellos.
- `plantillas/sesion.md` llena cada campo del hallazgo como `- **Campo:** valor`. El anexo de marcas dice que ese rótulo, lleno, es marca.
- `resumen.py` lee dos campos con esa forma: `Estado` (`_ESTADO`, línea 36) y `Con qué se retoma` (`_retoma`). Los usan `hallazgos()`, `sin_resolver()` y `proposito()`, que alimentan el aviso del resumen.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/marcas.py` | Modificar | Validador | Una función que mide un texto suelto y devuelve cada marca con su línea |
| `adaptadores/claude-code/hook_md.py` | Modificar | Adaptador | Mide lo recién escrito (`content` de `Write`, `new_string` de `Edit`) y se lo devuelve al agente |
| `plantillas/sesion.md` | Modificar | Estándar | Los campos del hallazgo pasan a una tabla |
| `validadores/resumen.py` | Modificar | Validador | Lee `Estado` y `Con qué se retoma` en la tabla y en la forma vieja |
| `validadores/pruebas.py` y `validadores/tests/` | Modificar y crear | Pruebas | Los casos del enganche, del molde y de la lectura |
| `validadores/docs/hook_md.md` | Modificar | Documentación | Lo que hace ahora |
| `CHANGELOG.md` y `VERSION` | Modificar | Estándar | `39.5.0`, MENOR |
| Los documentos de esta fase, HU-012, el pendiente 102 y el resumen de la sesión | Modificar | Documentación | Cierre |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Archivo a refactorizar | Cambio de contrato | Archivos que dependen (rompen) | Dónde rompe |
|---|---|---|---|
| `plantillas/sesion.md` | Los campos cambian de forma | `resumen.py` y `hook_resumen.py` | `resumen.py` aprende la forma nueva sin olvidar la vieja, porque los resúmenes ya escritos no se tocan |
| `hook_md.py` | Suma un aviso | Ninguno | El aviso va aparte de las fallas de enlaces, que siguen como están |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica: el aviso le llega al agente al escribir.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Se extiende `hook_md.py` | Un enganche nuevo | Ya corre en cada escritura de un `.md` (`01·C23`) |
| Se mide el texto recién escrito | Medir el archivo entero | El archivo trae marcas viejas; repetirlas en cada edición es ruido y se deja de leer |
| El aviso no detiene: sale por el contexto del agente | Salir con código 2 | Todo hallazgo de marcas es aviso (RN-04); el código 2 queda para los enlaces rotos |
| Los campos del hallazgo van en tabla de dos columnas, y «Qué lo soluciona» usa `<br>` dentro de la celda, como dice `plantillas/README.md` | Dejar la viñeta y permitirla en el anexo | Decidido por el usuario: no cambia qué exige `00·ID8` |
| `resumen.py` lee las dos formas | Convertir los resúmenes viejos | Los resúmenes son registro de lo que pasó y no se reescriben |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

## 3. Desglose de tareas por criterio de aceptación

### CA-05 · Lo que se escribe se mide al escribirlo

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | `marcas.py`: medir un texto suelto, saltando código y sellos, con la línea de cada marca | Validador | 0,5 h | — | CP-001 |
| T-02 | `hook_md.py`: tomar lo recién escrito, medirlo y devolver las marcas al agente sin detener | Adaptador | 1 h | T-01 | CP-001 |
| T-03 | Pruebas del enganche: con marcas, sin marcas, archivo que no es `.md` | Pruebas | 0,7 h | T-02 | CP-001 |

### CA-06 · El molde del resumen no produce marcas al llenarse

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-04 | `plantillas/sesion.md`: los dos moldes de hallazgo en tabla | Estándar | 0,5 h | — | CP-002 |
| T-05 | `resumen.py`: leer `Estado` y `Con qué se retoma` en tabla y en viñeta | Validador | 0,7 h | — | CP-002 |
| T-06 | Pruebas: un hallazgo lleno con el molde nuevo da cero marcas, y `resumen.py` lee el nuevo y el viejo | Pruebas | 0,7 h | T-04, T-05 | CP-002 |

### RNF · Requisitos no funcionales

| ID | Tarea | Categoría | Est. | Ev. |
|---|---|---|:--:|---|
| T-07 | `validadores/docs/hook_md.md`, `CHANGELOG.md` y `VERSION` en `39.5.0` | Trazabilidad | 0,3 h | CP-003 |
| T-08 | Cerrar HU-012, el pendiente 102 y el H-4 | Trazabilidad | 0,2 h | — |

**Total estimado:** 4,6 h.

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03, T-07, T-08.
**Paralelizables:** T-04 a T-06 no dependen de las del enganche.

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-05 | Pruebas del enganche con entradas como las que manda la herramienta | CP-001 | | ☐ |
| CA-06 | Recuento sobre un hallazgo lleno y lectura con `resumen.py` | CP-002 | | ☐ |
| RNF | `versionado`, `estandar` y las pruebas tocadas | CP-003 | | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| CP-001 a CP-003 | Resultado de cada caso | [resultado_pruebas.md](resultado_pruebas.md) |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | El repositorio y carpetas temporales |
| Usuarios de prueba | No aplica |
| Datos precargados | Un resumen viejo de `historico-chat/resumenes/` y uno nuevo hecho con el molde |

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit de la fase. Los resúmenes escritos con el molde nuevo se siguen leyendo con la versión anterior de `resumen.py` solo si se revierte también el molde; por eso los dos van en el mismo commit.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Un proyecto no tiene que hacer nada: el enganche ya está instalado y el molde nuevo se usa en los resúmenes que nacen después de actualizar. Los viejos se siguen leyendo. Por eso es MENOR.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

- Base: `00·ID8` y su anexo, `01·C23` (extender antes de crear), `02·F5` (solo las pruebas tocadas), `02·F8`, `02·F23`, `20·M10` (versionar), `00·ID9`, `00·ID11` e `00·ID12` en todo lo que se escribe.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que la tabla del hallazgo sea incómoda de llenar con «Qué lo soluciona», que es largo | El molde se llena mal | Se prueba llenando un hallazgo real de esta sesión | Abierto |
| B-02 | Que el aviso en cada edición sea ruido | Se deja de leer | Solo sale cuando lo recién escrito tiene marcas | Abierto |

## 11. Definition of Done

- [ ] CA-05 y CA-06 verificados con evidencia en la sección 5
- [ ] Las pruebas tocadas y `validar.py estandar` sin fallas
- [ ] HU-012, el pendiente 102 y el H-4 cerrados, sin nada pendiente
- [ ] Commit autorizado por el usuario

## 13. Cierre

El cierre va en [funcionalidad_implementada.md](funcionalidad_implementada.md).
