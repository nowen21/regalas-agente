# Análisis 1: `cerrar_fase` no reconoce los formatos de las plantillas y cierra con casos y marcas de menos

> **Aprobado** por el usuario el 2026-10-09, en el turno 22, con la versión 56.8.0. Desde ese momento este análisis no se reescribe.

> Este análisis se redacta aplicando estas reglas.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../../../../../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](../../../../../base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Un análisis aprobado no se reescribe. Si al ejecutar el plan aparece un hallazgo que obliga a tocar algo que el plan no declara, se abre `analisis-2.md`, que trata solo lo que falló y sus implicaciones sobre lo ya hecho. El hallazgo que no obliga a eso no abre análisis: se anota con su pendiente donde pertenece y el plan continúa.

---

## Recomendaciones

Se leyeron las [recomendaciones de Cimiento](../../../../../plantillas/recomendaciones-del-analisis.md); el proyecto no tiene `analisis/recomendaciones.md` propio.

| Recomendación | Cómo se aplica en este análisis |
|---|---|
| R-1 | «Dónde más puede pasar» revisa los formatos de las plantillas, las 333 fases que existen y la contraria, `reabrir_fase` |
| R-2 | Se reutiliza lo que ya existe: `Fase` y sus pruebas (`core/herramientas/tests_fase.py`, 9 casos) |
| R-19 | El plan declara todo lo que pide el cambio: `fase.py` y sus pruebas |
| Las demás | No aplican: no se cambia ninguna regla (R-3, R-4) y no hay piloto (R-16) |

---

## Hallazgo

### H-2 · `cerrar_fase` lee un solo caso de prueba por fila de la matriz

| Campo | Valor |
|---|---|
| Qué pasó | Al cerrar `A-EP-029-HU-008-danar-a-proposito`, `cerrar_fase` tomó solo CP-006 de los seis casos: la matriz del plan de pruebas pone varios casos en una fila («CP-001, CP-002») y `Fase.casos()` (`proyectos/cimiento/core/herramientas/fase.py:148`) solo reconoce una fila con un caso. Tampoco marcó esas filas ni los CA del plan de trabajo escritos como enlace. El resultado y las marcas se completaron a mano. La fase de la HU-011 de EP-026 tiene el mismo formato |
| Por qué importa | El resultado de las pruebas que escribe el cierre dice menos casos de los que hubo, y el veredicto por CA deja CA afuera, sin avisar |
| Pendiente | [Pendiente 150](pendiente.md) |

## Pendiente

**De dónde sale:** H-2, en el resumen de la sesión del 2026-10-09.

**El problema.** `cerrar_fase` arma el resultado de las pruebas desde la matriz del plan de pruebas, pero `Fase.casos()` solo reconoce las filas con un caso. Las filas con varios las salta sin avisar. Tampoco marca, en la segunda pasada: las filas de la matriz con varios casos; los CA del plan de trabajo escritos como enlace; la columna «Verificado» y el estado de la sección 5 del plan de trabajo; las casillas de la Definition of Done del plan y de la HU, y las tareas técnicas de la HU.

**Por qué importa.** El resultado de las pruebas dice menos casos de los que hubo y el veredicto deja CA afuera, sin avisar. Lo que queda sin marcar hay que encontrarlo y marcarlo a mano en cada cierre.

---

## Conversación

> La escribe el enganche en tiempo real, turno por turno, desde la transcripción de la sesión. No se escribe a mano.

### 20 · Usuario, 2026-10-09 10:19:59
> Analicemos: el pendiente 150

**Agente**, 2026-10-09 10:24:02
<!-- agente: 8f9a121a-ec6b-48bd-9063-21334f9e3fa6 -->

Reviso dónde más se lee la matriz del plan de pruebas y cómo está probado `cerrar_fase`.

Solo `fase.py` lee la matriz. Mido cuántas fases existentes usan los formatos que `cerrar_fase` no reconoce.

Necesito una decisión: **¿se construye como EP-025·HU-031, sin tocar las fases que ya están cerradas?** Recomiendo que sí. La EP-025 es la épica donde nació `cerrar_fase`, y una fase cerrada no se reescribe.

El análisis quedó escrito en [analisis-1.md](../../../../../historico-chat/resumenes/2026-10-09/pendientes/150-cerrar-fase-lee-todos-los-casos-y-marca-todo-lo-que-cierra/analisis-1.md). Esto encontré:

- **El problema no es solo de esta fase.** `cerrar_fase` no entiende el formato que piden las plantillas oficiales del estándar. La plantilla del plan de pruebas pone varios casos por fila, como enlaces, y filas de requisitos no funcionales. La del plan de trabajo escribe los CA sin nombre. `cerrar_fase` solo reconoce el formato que usan sus propias pruebas.
- **Cuántas fases afecta.** De las 333 fases que hay, 15 ponen varios casos en una fila y 160 escriben los CA como enlace. Con cualquiera de esos formatos, el cierre deja casos o CA por fuera sin avisar.
- **Lo que tampoco marca.** La columna «Verificado» del plan, las casillas de terminado del plan y de la HU, y las tareas técnicas de la HU.

La corrección:

1. Leer todos los casos de cada fila, con enlace o sin él, y también las filas de requisitos no funcionales. Cuando un CA no trae nombre, tomarlo de la HU.
2. Marcar todo lo que la fase cierra, y que `reabrir_fase` desmarque lo mismo.

### 21 · Usuario, 2026-10-09 10:28:42
> continúe

**Agente**, 2026-10-09 10:29:13
<!-- agente: adcdebc8-1f9d-44c5-a909-c968a4d63e8c -->

Tomo la recomendación y dejo anotados los acuerdos en el análisis.

Quedaron anotados tres acuerdos:

1. **Leer:** `cerrar_fase` toma todos los casos de cada fila, con enlace o sin él, y también los requisitos no funcionales. A los CA que no traen nombre se los pone desde la HU.
2. **Marcar:** el cierre marca todo lo que la fase deja terminado, y `reabrir_fase` desmarca lo mismo.
3. **Dónde y cuánto:** el trabajo va en la EP-025·HU-031, y las fases que ya están cerradas no se tocan. Esto lo tomé de la recomendación, porque la respuesta fue «continúe».

No queda ninguna decisión pendiente. **Escriba «Apruebo el análisis»**, y con eso hago la HU, el plan, el cambio y las pruebas.

### 22 · Usuario, 2026-10-09 10:30:00
> Apruebo el análisis

**Agente**, 2026-10-09 10:37:41
<!-- agente: 7417d562-02f4-48a9-9239-0595b5203f3b -->

Aprobado. Registro la lección y escribo la HU-031.

Al análisis del 146 le faltó anotar el número de su señal (S-363). Intento corregirlo.

Ahora la HU-031.

Escribo los dos planes de la fase.

Ahora el código de `fase.py`: primero la lectura.

Ahora las marcas: al cerrar y su contraria al reabrir.

El reemplazo por guion falló por el escape de las barras. Hago las ediciones con la herramienta de edición.

Corro las 9 pruebas que ya había, para comprobar que el formato viejo sigue cerrando igual.

Pasan las 9. Agrego las pruebas con el formato de las plantillas.

Las dos fallas vienen de la prueba, no de `fase.py`: la clase nueva heredó las pruebas viejas, que esperan el formato viejo. Separo la preparación común en una clase base.

Pasan las 13 (las 9 de antes y las 4 nuevas). Reviso que el archivo haya quedado bien separado.

Compruebo, solo leyendo, que ahora `cerrar_fase` toma los 6 casos de la fase del pendiente 148, que fue la que destapó el defecto.

Ahora sí toma los 6 casos y los 3 CA, con sus nombres sacados de la HU (las tildes salen dañadas solo en esta consola). Cierro la fase de la HU-031.

El cierre ya toma la fila RNF-01 con el código nuevo. Lleno los huecos.

Cerrada. Reviso que esta vez el cierre haya marcado todo solo, sin tocar nada a mano.

El pendiente 150 quedó terminado y funcionando.

- **Lee el formato de las plantillas.** Toma varios casos por fila, con enlace o sin él, y también los requisitos no funcionales. A los CA que no traen nombre se los pone desde la HU. En la fase del pendiente 148 ahora reconoce los 6 casos; antes reconocía 1.
- **Marca todo al cerrar.** Marca la columna «Verificado» del plan y las casillas de terminado del plan y de la HU. `reabrir_fase` desmarca lo mismo. Esta fase se cerró sin marcar nada a mano. Solo quedó sin marcar la casilla del commit, que es a propósito.
- **Pruebas:** pasan las 13, las 9 que ya había y 4 nuevas escritas con el formato de las plantillas. Los validadores no dan ninguna falla.
- **Documentos:** quedan cerradas la EP-025·HU-031 y su fase. La lección quedó como señal S-364.

**Para seguir con el pendiente 149, escriba «Analicemos: el pendiente 149».** Ya no hay que esperar nada antes: los cambios de `views.py` y `ajustes.py` que estaban sin guardar ya quedaron guardados en git.

> acá termina la conversación

---

## Lo acordado

1. Leer: `cerrar_fase` toma todos los casos de cada fila de la matriz, con enlace o sin él, y las filas de RNF; reconoce los CA del plan con nombre, sin nombre o como enlace, y el nombre que falte lo toma de la HU (turnos 20 y 21).
2. Marcar: la segunda pasada marca todas las filas de la matriz, los CA del plan en cualquiera de esas formas, la sección 5 del plan («Verificado» con la fecha y «Estado»), la Definition of Done del plan y, si la HU queda terminada, sus tareas técnicas y su Definition of Done; `reabrir_fase` desmarca lo mismo (turnos 20 y 21).
3. Las fases ya cerradas se dejan como están; se construye como EP-025·HU-031. Es lo recomendado: el usuario respondió «continúe» (turno 21).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `02·F7` (no se cierra una fase con trazabilidad incompleta: hoy el cierre la deja incompleta sin avisar), `02·F30` (`reabrir_fase` desmarca lo mismo que `cerrar_fase` marca), `08·T1` y `02·F11`. No choca ninguna.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| Lo que entiende `cerrar_fase` | Una fila de la matriz por caso, sin enlace (`| HU-1 | CA-01 | CP-001 | … |`), y los CA del plan como `| CA-01 · nombre | ☐ |` (`fase.py:139` y `:152`). Es el formato de sus pruebas (`tests_fase.py:29`) |
| Lo que dicen las plantillas | El plan de pruebas pone varios casos por fila y como enlace (`[CP-001](#…), [CP-002](#…)`) y filas de RNF (`plantillas/ciclo-vida-proyectos/08-plan-pruebas.md:176`). El plan de trabajo pone los CA sin nombre: `| CA-01 | ☐ |` (`07-plan-trabajo.md:51`) |
| Las 333 fases que existen | 15 tienen filas con varios casos; 160 escriben los CA del plan como enlace. Con cualquiera de esos formatos, el cierre saca casos o CA de menos sin avisar |
| Lo que no marca | La sección 5 del plan («Verificado» y «Estado»), la Definition of Done del plan y de la HU, y las tareas técnicas de la HU. 46 fases ya cerradas tienen la Definition of Done del plan sin marcar |
| Quién más lee la matriz | Nadie: solo `fase.py` (líneas 152, 327 y 429) |
| EP-030·HU-004 | Pasará los documentos de la fase a la base; reescribe `fase.py`. Lo que se construya ahora sirve hasta entonces |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| H-2 de esta sesión | Confirma el defecto con un caso real: 1 de 6 casos |
| Fase `A-EP-025-HU-030-resumen-rapido` | Confirma la causa: escrita con un caso por fila y CA con nombre, cerró bien; aun así hubo que marcar a mano la sección 5 y la Definition of Done |
| Análisis 1 del pendiente 147 | Lo que se rehace en EP-030·HU-004 no se construye antes. Aquí sí, porque el usuario pidió resolver en esta sesión lo que salga de ella y el defecto da resultados falsos hoy |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | PARCHE (`20·M10`): `cerrar_fase` entiende lo que las plantillas ya les piden |
| Normas y leyes | Ninguna |
| Herramientas | Ninguna |

### Dónde más puede pasar

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Filas con varios casos, con enlace o sin él | 15 fases y la plantilla | Casos y CA de menos en el resultado | Punto 1 |
| Filas de RNF en la matriz | La plantilla | El RNF no entra al veredicto | Punto 1 |
| CA del plan sin nombre o como enlace | 160 fases y la plantilla | La trazabilidad de la funcionalidad sale vacía y los CA quedan sin marcar | Punto 1: el nombre se toma de la HU |
| La sección 5 y las Definition of Done | Toda fase | Marcar a mano en cada cierre | Punto 2 |
| `reabrir_fase` | La contraria | Que desmarque menos de lo que el cierre marcó | Punto 2 |
| Las fases ya cerradas | 46 con la Definition of Done del plan sin marcar | Quedan como están | Acuerdo 3: no se tocan, porque una fase cerrada no se reescribe |

---

## Propuesta final: hallazgo y pendiente, épica y HU

El hallazgo H-2 y el pendiente 150 quedan como están.

### Épica y HU que salen del análisis

Se suma a la [EP-025: Cimiento se administra y muestra el gasto de tokens](../../../../../documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md), donde nació `cerrar_fase` (HU-016).

| Orden | HU | Título | Parte del problema que resuelve | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|---|---|
| 1 | 031 | `cerrar_fase` entiende los formatos de las plantillas y marca todo lo que cierra | El cierre saca casos y CA de menos y deja marcas sin poner | Ninguna | Es la única | 1, 2 |

## Lecciones aprendidas

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | Un programa que lee documentos se prueba con el formato de la plantilla, no con uno inventado para la prueba | Falló | S-364 | No aplica |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | `Fase.casos()` y `Fase.plan()` (`core/herramientas/fase.py`) leen la matriz con varios casos por fila, con enlace o sin él, y las filas de RNF; y los CA del plan con nombre, sin nombre o como enlace, tomando de la HU el nombre que falte; con pruebas escritas en el formato de las plantillas | 1, 3 | EP-025·HU-031 |
| 2 | La segunda pasada de `cerrar_fase` marca todas las filas de la matriz, los CA del plan, la sección 5 del plan y su Definition of Done, y, con la HU terminada, sus tareas técnicas y su Definition of Done; `reabrir_fase` desmarca lo mismo; con pruebas | 2, 3 | EP-025·HU-031 |

## Lo que aporta al análisis principal

**Resultado:** aclara.

**Lo que suma al análisis principal:** Cerrar una fase lee los documentos en el formato de sus plantillas y deja marcado todo lo que cierra.
