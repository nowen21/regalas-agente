# Plan de Trabajo · Fase `A-EP-025-HU-005-el-freno-lee-los-niveles` (módulo `proyectos/cimiento/core/enganches/` y `adaptadores/claude-code/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-005-el-freno-lee-los-niveles` |
| **Épica** | [EP-025](../../epica.md) |
| **HU** | [HU-005](../HU-005-el-freno-aplica-el-nivel-guardado-y-sin-base-no-deja-modificar.md), una sola (`F12.1`) |
| **Módulo** | `proyectos/cimiento/core/enganches/`, `adaptadores/claude-code/`, `proyectos/cimiento/core/herramientas/` |
| **Especificación del módulo** | Los CA de la [HU-005](../HU-005-el-freno-aplica-el-nivel-guardado-y-sin-base-no-deja-modificar.md) |
| **Fecha apertura** | 2026-10-05 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): funcionalidad nueva. Sale del punto 14 del [análisis 1 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md) (acuerdos 13 y 15).

**Carencias que cierra** (`02·F14` Q3): el freno decide con lo que está en el código, igual en todos los proyectos.

**Aprobación** (`02·F4`): [análisis 1 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md), el 2026-10-04, con la versión 54.2.0

**Disparo** (`02·F15`, etapa 2): el usuario aprobó el análisis el 2026-10-04 y pidió seguir con «Continúe con el pendiente 119».

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-005 | Estado |
|---|---|
| CA-01 · El nivel de la regla cambia lo que hace el freno, solo en ese proyecto | ☑ |
| CA-02 · El núcleo siempre frena | ☑ |
| CA-03 · Sin base, no se modifica nada | ☑ |
| CA-04 · La instalación deja PyMySQL | ☑ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que el freno aplique el nivel de cada regla en el proyecto, leído de MariaDB sin Django, y que sin base no deje modificar.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Frena, avisa y apagada por proyecto | Programa | Alta |
| CA-02 | Núcleo | Programa | Baja |
| CA-03 | Base apagada | Programa | Media |
| CA-04 | PyMySQL en la instalación | Programa | Baja |

**Fuera de alcance:** cambiar qué reglas revisa el freno.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medido el 2026-10-05, sobre la versión 54.2.0:

- `Freno.revisar()` devuelve `(decisión, motivo, ruta)` con «deja», «detiene» o «pregunta». Los motivos terminan en la regla entre paréntesis: `(02·F8)`, `(04·S9)`, `(04·S10)`, y `(00·N1)` en lo que se publica.
- `Freno.despues()` devuelve `[(ruta, motivo)]` de lo que cambió fuera del plan; `hook_despues.py` lo entrega con `decision: block`.
- `hook_antes.py` y `hook_despues.py` importan la clase `Freno` de Cimiento y corren con el Python general de la máquina, que tiene PyMySQL.
- `tests_freno.py`: 308 pruebas, todas pasan.
- `config/ambiente.py` pone el `.env` en el ambiente del proceso; no tiene una función que solo lo lea.
- Las tablas que se leen: `proyectos_proyecto` (`id`, `ruta`, `activo`) y `niveles_nivelderegla` (`proyecto_id`, `regla`, `nivel`).

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/enganches/niveles.py` | Crear | Programa | El lector de niveles con PyMySQL |
| `proyectos/cimiento/config/ambiente.py` | Modificar | Configuración | `leer(ruta)` devuelve el `.env` sin tocar el ambiente; `cargar` la usa |
| `proyectos/cimiento/core/enganches/freno.py` | Modificar | Programa | El nivel antes y después de actuar; sin base no deja modificar |
| `adaptadores/claude-code/hook_antes.py`, `adaptadores/claude-code/hook_despues.py` | Modificar | Enganche | Entregan el aviso de «avisa» sin detener |
| `proyectos/cimiento/core/enganches/tests_freno.py` | Modificar | Pruebas | Las 308 con un lector sustituido; los casos de nivel y de base apagada |
| `proyectos/cimiento/core/niveles/tests_lectura.py` | Crear | Pruebas | El lector contra la base de pruebas |
| `proyectos/cimiento/core/herramientas/instalar.py`, `proyectos/cimiento/core/herramientas/tests_instalacion.py`, `validadores/instalar.py` | Modificar | Programa | El paso de PyMySQL |
| `proyectos/cimiento/requirements/base.txt`, `proyectos/cimiento/requirements/lock.txt` | Modificar | Dependencias | PyMySQL también en el `.venv` de Cimiento, donde corren sus pruebas |
| `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-005-el-freno-aplica-el-nivel-guardado-y-sin-base-no-deja-modificar/HU-005-el-freno-aplica-el-nivel-guardado-y-sin-base-no-deja-modificar.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md` | Modificar | Documentación | La fila de la fase y el estado |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| `Freno.revisar()` puede devolver «avisa» | `hook_antes.py` | Lo entrega como aviso, sin detener |
| `Freno` recibe un lector de niveles | `hook_antes.py`, `hook_despues.py`, `tests_freno.py` | Por defecto, el de la base; las pruebas pasan uno sustituido |
| `Freno.despues_por_nivel()` nuevo; `despues()` devuelve lo que frena | `hook_despues.py`, `tests_freno.py` | El enganche usa el nuevo |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica: los niveles se fijan en la pantalla de la HU-004.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| La regla se saca del motivo, el último `(NN·ID)` | Un campo nuevo en cada decisión | Todos los motivos ya la nombran, y así se ve en el aviso | Acuerdo 13 |
| Una consulta trae todos los niveles del proyecto, una vez por acción | Una consulta por regla | Una sola ida a la base | RNF-01 |
| La base se consulta solo si la acción modifica o si el freno la detiene | En toda acción | Leer y analizar no dependen de la base | Acuerdo 15 |
| Sin base, el motivo no nombra una regla configurable | Darle un ID | Así ningún nivel lo apaga | Acuerdo 15 |
| «Avisa» llega al agente como contexto adicional y al usuario como mensaje, sin decisión de permiso | Responder «allow» | Un «allow» saltaría la confirmación que la herramienta pide al usuario | Propuesta del agente |
| PyMySQL se instala con el Python que corre la instalación | Pedirle al usuario que lo instale | Toda herramienta se autoinstala | Acuerdo 15 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 Qué cambia técnicamente  ·  `02·F14` Q5

| Artefacto | Hoy | Después | Regla que aplica |
|---|---|---|---|
| El freno | Igual en todos los proyectos | Con el nivel de cada regla en el proyecto; sin base no deja modificar | Acuerdos 13 y 15 |

## 3. Desglose de tareas por criterio de aceptación

Cada tarea dice qué y cómo, dónde, por qué e impacto (`02·F16`).

### CA-01 · El nivel de la regla cambia lo que hace el freno, solo en ese proyecto

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | `ambiente.leer(ruta)` | `proyectos/cimiento/config/ambiente.py` | CA-01 | La conexión del lector | 0,5 h | Ninguna | CP-001 |
| T-02 | `NivelesDelProyecto`: conexión del `.env` de Cimiento, una consulta por proyecto, `BaseSinRespuesta` con el mensaje | `proyectos/cimiento/core/enganches/niveles.py` | CA-01, CA-03 | El freno | 1,5 h | T-01 | CP-001, CP-003 |
| T-03 | `Freno` aplica el nivel en `revisar` y en `despues_por_nivel` | `proyectos/cimiento/core/enganches/freno.py` | CA-01 | Toda acción en todo proyecto | 2 h | T-02 | CP-001 |
| T-04 | Los enganches entregan «avisa» | `adaptadores/claude-code/hook_antes.py`, `adaptadores/claude-code/hook_despues.py` | CA-01 | Toda acción | 1 h | T-03 | CP-001 |

### CA-02 · El núcleo siempre frena

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-05 | El núcleo no se mira en la tabla | `proyectos/cimiento/core/enganches/freno.py` | CA-02 | Toda acción | 0,5 h | T-03 | CP-002 |

### CA-03 · Sin base, no se modifica nada

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-06 | Sin base: detiene lo que modifica y deja lo que lee; después de una orden, avisa | `proyectos/cimiento/core/enganches/freno.py` | CA-03 | Toda acción | 1 h | T-03 | CP-003 |

### CA-04 · La instalación deja PyMySQL

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-07 | `Instalador.asegurar_pymysql(aplicar)`, llamado junto a `preparar_cimiento`; PyMySQL en las dependencias de Cimiento | `proyectos/cimiento/core/herramientas/instalar.py`, `validadores/instalar.py`, `proyectos/cimiento/requirements/base.txt`, `proyectos/cimiento/requirements/lock.txt` | CA-04 | La instalación del estándar | 1 h | Ninguna | CP-004 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-08 | Pruebas; fila de la fase en la HU y estado en la épica | `proyectos/cimiento/core/enganches/tests_freno.py`, `proyectos/cimiento/core/niveles/tests_lectura.py`, `proyectos/cimiento/core/herramientas/tests_instalacion.py`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-005-el-freno-aplica-el-nivel-guardado-y-sin-base-no-deja-modificar/HU-005-el-freno-aplica-el-nivel-guardado-y-sin-base-no-deja-modificar.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md` | CA-01 a CA-04 | Documentación | 1,5 h | T-01 a T-07 | CP-001 a CP-004 |

## 4. Secuencia de ejecución

T-01, T-02, T-03, T-05, T-06, T-04, T-07 y al final T-08, con las pruebas de la fase (`02·F5`).

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-01 | Frena, avisa y apagada con un lector sustituido; el lector contra la base de pruebas | CP-001 |
| CA-02 | Una fila del núcleo en «apagada» | CP-002 |
| CA-03 | El lector que no responde: escribir y leer | CP-003 |
| CA-04 | Con y sin PyMySQL | CP-004 |

## 6. Datos y ambiente de prueba

Proyectos de prueba en carpetas temporales (los de `tests_freno.py`); la base de pruebas en MariaDB para el lector.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase: el freno vuelve a decidir solo con el código.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Afecta a todo proyecto de la máquina desde que se guarda: sin niveles guardados todo frena como hoy, pero con MariaDB apagada nadie modifica. Es lo acordado.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`02·F8`, `04·S9`, `00·N1`, `00·N6`, `02·F4`, `02·F5`, `00·ID8`, `00·ID9`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Un error del lector bloquea al agente | El enganche que falla deja pasar y lo avisa, como hoy; las pruebas cubren el lector |
| MariaDB se apaga a mitad de la fase | El aviso dice cómo seguir: prenderla |

## 11. Definition of Done

- [x] CA-01 a CA-04 con veredicto y evidencia en `resultado_pruebas.md`.
- [x] Las pruebas de la fase sin fallas, y cero marcas nuevas.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Las 8 tareas quedaron hechas el 2026-10-05, con la versión 54.2.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** 1. El `.venv` de Cimiento no tenía PyMySQL; se agregó a sus dependencias, declaradas en el plan antes de tocarlas.
