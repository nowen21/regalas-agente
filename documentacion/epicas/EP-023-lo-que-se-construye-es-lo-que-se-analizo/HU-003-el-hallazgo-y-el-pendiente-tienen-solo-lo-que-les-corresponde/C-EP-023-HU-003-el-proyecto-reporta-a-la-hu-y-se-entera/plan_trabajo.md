# Plan de Trabajo · Fase `C-EP-023-HU-003-el-proyecto-reporta-a-la-hu-y-se-entera` (módulo `validadores/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `C-EP-023-HU-003-el-proyecto-reporta-a-la-hu-y-se-entera` |
| **Épica** | [EP-023](../../epica.md) |
| **HU** | [HU-003](../HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde.md), una sola (`F12.1`) |
| **Módulo** | `validadores/` |
| **Especificación del módulo** | El CA-10 y el CA-11 de la HU-003 |
| **Fecha apertura** | 2026-10-03 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): tercera fase de la HU-003. Sale de los puntos 1 a 4 del [análisis 13](../../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-13.md) (acuerdos 1 a 4).

**Carencias que cierra** (`02·F14` Q3): `02·F24` no dice en qué parte del estándar nace el pendiente que reporta un proyecto, y el aviso de resuelto solo funciona con la forma vieja: lo escribe `cerrar.py` al mover el pendiente a `pendientes/hecho/`, en la carpeta `pendientes/` del proyecto.

**Aprobación** (`02·F4`): Ing. José Dúmar Jiménez Ruíz, el 2026-10-03, con la versión 52.1.2.

**Disparo** (`02·F15`, etapa 2): el usuario pidió escribir esta fase el 2026-10-03 con «Escriba».

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-003 | Estado |
|---|---|
| CA-10 · El proyecto reporta el pendiente a la HU que lo originó | ☐ |
| CA-11 · El proyecto se entera cuando su pendiente se resuelve | ☐ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que el pendiente que reporta un proyecto nazca en la HU del estándar que lo originó, y que al cumplirse su plan el proyecto reciba el aviso al lado de su pendiente de seguimiento, que cierra cuando el proyecto lo comprueba.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-10 | Dónde nace el pendiente reportado | Regla y plantilla | Baja |
| CA-11 | El aviso de resuelto y el cierre del seguimiento | Programa y enganche | Media |

**Fuera de alcance:** la regla que obliga a pasar el pendiente a su versión siguiente (análisis 14, punto 5): espera a que ese análisis se apruebe y su CA nazca en esta HU. Los pendientes viejos de `pendientes/` siguen con `cerrar.py` (análisis 1, acuerdo 38).

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medido el 2026-10-03, sobre la versión 52.1.2:

- `02·F24` manda abrir «un pendiente allá» que enlace el hallazgo del proyecto, y otro acá; no dice dónde vive el de allá.
- `plantillas/pendiente-reportado.md` y `plantillas/pendiente-de-seguimiento.md` existen; el de seguimiento dice que cierra cuando cierra el plan del padre.
- `validadores/cerrar.py` escribe el aviso en `pendientes/` del proyecto al mover el pendiente a `hecho/`. La forma nueva no mueve nada: el cierre lo calcula `pendientes.estado()`.
- `pendientes.estado()` da al seguimiento el estado de su padre, sin esperar a que el proyecto compruebe.
- `adaptadores/claude-code/hook_estacion.py` anota el commit en la fase con `estacion_commit.marcar_las_fases()`; es el momento en que se cumple el plan.
- Citan su HU 14 de 91 reglas y 33 de 107 programas (análisis 13).
- Leen los programas que cambian: las pruebas de `pendientes.py` y de `estacion_commit.py` en `validadores/pruebas.py`.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

> Cada fila lleva una o más rutas exactas entre comillas invertidas, separadas por coma.

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `base/02-flujo-de-trabajo/reglas/F24-el-defecto-del-estandar-se-reporta-no-se-corrige.md` | Modificar | Regla | Dónde nace el pendiente reportado y cuándo cierra el seguimiento, con su sello |
| `plantillas/pendiente-reportado.md`, `plantillas/pendiente-de-seguimiento.md` | Modificar | Plantilla | Dónde se crea cada uno y cuándo cierra el seguimiento |
| `validadores/aviso_resuelto.py` | Nuevo | Programa | Escribe el aviso al lado del pendiente de seguimiento, siguiendo los enlaces |
| `adaptadores/claude-code/hook_estacion.py` | Modificar | Enganche | Al anotar el commit, llama al aviso |
| `validadores/pendientes.py` | Modificar | Programa | El seguimiento cierra cuando el padre cerró y el aviso está comprobado |
| `validadores/tests/test_el_proyecto_reporta_y_se_entera.py` | Nuevo | Pruebas | Los casos del plan de pruebas || `base/reglas-por-tarea/trabajar-cadena-2.md`, `base/mapa-de-tareas.md` | Modificar | Generado | Lo vuelve a escribir `mapa_tareas.py`, si cambia la copia |
| `anatomia/mapa-del-sitio.md` | Modificar | Documentación | El programa nuevo |
| `documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde/HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde.md` | Modificar | Documentación | La fila de esta fase |
| `CHANGELOG.md`, `VERSION` | Modificar | Versión | 53.0.0 |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| `pendientes.estado()` del seguimiento | El índice de pendientes y `origen.py` | El seguimiento queda abierto hasta que el proyecto compruebe |
| `hook_estacion.py` | Todo proyecto, al anotar un commit | Si no hay pendiente reportado que cerrar, no hace nada más |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| El pendiente reportado nace en la HU que cita la regla o el programa que falla; si no la citan, en el resumen del día del estándar | Un sitio fijo para todos los reportes | Así lo acordó el usuario | Análisis 13, acuerdo 1 |
| La HU de origen se cita cuando el análisis de un pendiente decide a cuál pertenece; no se completa de una vez | Completar las 77 reglas y los 74 programas sin HU | Así lo acordó el usuario | Análisis 13, acuerdo 2 |
| El aviso sale cuando la fase que cumple el plan del pendiente anota su commit, y va al lado del pendiente de seguimiento del proyecto | Escribirlo en `pendientes/` del proyecto | Así lo acordó el usuario | Análisis 13, acuerdo 3 |
| El seguimiento cierra cuando el proyecto comprueba la corrección | Cerrarlo con el padre | Así lo acordó el usuario | Análisis 13, acuerdo 4 |
| El seguimiento se encuentra siguiendo los enlaces: el pendiente del estándar enlaza el hallazgo del proyecto, y ese hallazgo enlaza su pendiente | Un campo nuevo con la ruta | No hace falta un campo nuevo | Análisis 13, acuerdo 3 |
| El aviso es un archivo `aviso-resuelto.md` en la carpeta del seguimiento, con una línea «Comprobado: no» que el proyecto cambia a la fecha al comprobar | Marcar el seguimiento a mano | El estado se calcula del archivo, sin que nadie escriba el pendiente | Propuesta del agente |
| `aviso_resuelto.py` es un programa nuevo, no una parte de `cerrar.py` | Extender `cerrar.py` | `cerrar.py` mueve pendientes de la forma vieja; la nueva no mueve nada | Propuesta del agente |
| La versión sube a 53.0.0, MAYOR | MENOR | Cambia dónde reporta un proyecto | Propuesta del agente |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 Qué cambia técnicamente  ·  `02·F14` Q5

| Artefacto | Hoy | Después | Regla que aplica |
|---|---|---|---|
| Reporte de un proyecto | «Un pendiente allá», sin decir dónde | En la HU que originó el defecto, o en el resumen del día del estándar | `02·F24` |
| Aviso de resuelto | En `pendientes/` del proyecto, al mover a `hecho/` | Al lado del seguimiento, al anotar el commit | `02·F24` |
| Cierre del seguimiento | Con el padre | Con el padre y la comprobación del proyecto | `02·F24` |

## 3. Desglose de tareas por criterio de aceptación

Cada tarea dice qué y cómo, dónde, por qué e impacto (`02·F16`).

### CA-10 · El proyecto reporta el pendiente a la HU que lo originó

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | `02·F24` dice dónde nace el pendiente reportado y que la HU de origen se cita cuando un análisis la decide; aplicar el checklist y poner su sello; las dos plantillas lo dicen; correr `mapa_tareas.py` | `base/02-flujo-de-trabajo/reglas/F24-el-defecto-del-estandar-se-reporta-no-se-corrige.md`, `plantillas/pendiente-reportado.md`, `plantillas/pendiente-de-seguimiento.md`, `base/reglas-por-tarea/trabajar-cadena-2.md`, `base/mapa-de-tareas.md` | CA-10 | Todo proyecto que adopte la versión | 1 h | Ninguna | CP-001 |

### CA-11 · El proyecto se entera cuando su pendiente se resuelve

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-02 | `aviso_resuelto.py`: para cada pendiente reportado cuyo plan se cumplió, sigue los enlaces hasta el seguimiento del proyecto y escribe ahí `aviso-resuelto.md`, una sola vez | `validadores/aviso_resuelto.py` | CA-11 | Los proyectos que reportaron | 2 h | T-01 | CP-002 |
| T-03 | `hook_estacion.py` llama al aviso después de anotar el commit | `adaptadores/claude-code/hook_estacion.py` | CA-11 | Todo commit que cierra una fase | 0,5 h | T-02 | CP-002 |
| T-04 | `pendientes.estado()` deja abierto el seguimiento hasta que su `aviso-resuelto.md` diga «Comprobado» con fecha | `validadores/pendientes.py` | CA-11 | El índice de pendientes | 1 h | T-02 | CP-003 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-05 | Escribir los casos del plan de pruebas; el programa en el mapa del sitio; la fila de la fase en la HU; subir a 53.0.0 con «⚠ obliga a migrar» | `validadores/tests/test_el_proyecto_reporta_y_se_entera.py`, `anatomia/mapa-del-sitio.md`, `documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde/HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde.md`, `CHANGELOG.md`, `VERSION` | CA-10, CA-11 | Todo proyecto adopta la versión | 1 h | T-01 a T-04 | CP-001 a CP-003 |

## 4. Secuencia de ejecución

T-01; después T-02, T-03 y T-04; al final T-05, con los validadores, las pruebas de la fase y las de los programas que cambian, y la medición de marcas (`02·F5`).

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-10 | Leer `02·F24` y las dos plantillas | CP-001 |
| CA-11 | En dos proyectos de prueba, anotar el commit de la fase que cumple el plan de un pendiente reportado; consultar el seguimiento antes y después de comprobar | CP-002, CP-003 |

## 6. Datos y ambiente de prueba

Dos carpetas temporales: un estándar con una HU, un pendiente reportado y su plan cumplido, y un proyecto con el hallazgo y su pendiente de seguimiento, enlazados entre sí.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Cada proyecto adopta la 53.0.0 al actualizar el estándar. Desde ahí reporta a la HU de origen, y su seguimiento cierra cuando comprueba el aviso.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`02·F24`, `02·F23`, `20·M5`, `20·M10`, `02·F27`, `00·ID8`, `00·ID9`, `02·F5`, `02·F18`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Que el enlace del hallazgo al seguimiento esté roto o no exista | El aviso no se escribe y el programa dice cuál falta |
| Que el proyecto no esté en el mismo equipo | No se escribe y se dice; hoy todos los proyectos están en el mismo equipo |

## 11. Definition of Done

- [ ] CA-10 y CA-11 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Los validadores y las pruebas de la fase sin fallas, y cero marcas nuevas.
- [ ] `VERSION` y `CHANGELOG.md` en 53.0.0.
- [ ] Aprobación del usuario.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Se llena al cerrar la fase.

**Hallazgos al ejecutar:** se anota al cerrar.
