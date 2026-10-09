# Análisis 2: el análisis 1 no nombra la HU que construye su punto, y el freno no deja editar `manage.py`

> **Aprobado** por el usuario el 2026-10-08, en el turno 37, con la versión 56.8.0. Desde ese momento este análisis no se reescribe.

> Este análisis se redacta aplicando estas reglas.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../../../../../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](../../../../../base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Un análisis aprobado no se reescribe. Si al ejecutar el plan aparece un hallazgo que obliga a tocar algo que el plan no declara, se abre `analisis-3.md`, que trata solo lo que falló y sus implicaciones sobre lo ya hecho.

---

## Recomendaciones

| Recomendación | Cómo se aplica en este análisis |
|---|---|
| R-6 | Se leyó completo el análisis 1: su punto 1 dice «la HU de EP-026 que salga de este análisis» en «Pasó a» |
| R-15 | La ejecución se detuvo en la primera edición de `manage.py`, antes de tocar otro archivo |
| R-19 | El plan de la fase ya declara `manage.py` y la prueba; lo que faltaba era el nombre de la HU en el análisis |
| Las demás | No aplican: no se cambia ninguna regla (R-3, R-4) y no hay piloto (R-16) |

---

## Hallazgo

### H-5 · El freno detuvo una edición fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-08 22:04, el freno detuvo una edición sobre `proyectos/cimiento/manage.py`: el plan de la fase en curso no lo declara, o no está aprobado, y ninguna regla lo autoriza (02·F8). El plan sí lo declara; no cuenta como aprobado porque el análisis 1 del pendiente 145 no nombra la HU en «Lo que se tiene que hacer» (dice «la HU de EP-026 que salga de este análisis» en vez de EP-026·HU-011), y además a la aprobación del plan le faltaba la versión, que ya se corrigió |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | El mismo pendiente 145: se trata en su análisis 2 |

## Pendiente

**De dónde sale:** H-4 · La consulta de las reglas falla porque el aviso manda a usar el Python que no tiene el conector de MySQL.

**El problema.** El aviso de cada sesión manda a leer las reglas con `python "…/proyectos/cimiento/manage.py" ver_estandar <ruta>`. Ese `python` es el del computador, que no tiene el conector de MySQL, y la consulta falla. Cimiento usa su propio Python 3.11.9, en `proyectos/cimiento/.venv/`, y con ese funciona. Con el Python de Cimiento, las tildes salen dañadas en la consola de Windows.

**Por qué importa.** Toda sesión, en cualquier proyecto, recibe la orden de leer las reglas con un comando que falla; sin leerlas, trabaja sin las reglas completas.

---

## Conversación

> La escribe el enganche en tiempo real, turno por turno, desde la transcripción de la sesión. No se escribe a mano.

### 36 · Usuario, 2026-10-08 22:12:31
> Analicemos: el pendiente 145

**Agente**, 2026-10-08 22:14:14
<!-- agente: e5875eba-97f3-43bc-bafb-722fef6f2c18 -->

El [análisis 2](../../../../../historico-chat/resumenes/2026-10-08/pendientes/145-manage-py-usa-el-python-de-cimiento/analisis-2.md) quedó escrito. Ahora nombra la HU exacta que hace el trabajo: **EP-026·HU-011**. También pasé el pendiente a su versión 2, con H-5 en «De dónde sale». El plan de la fase no cambia.

**¿Está de acuerdo con que el trabajo lo haga la EP-026·HU-011, con su plan tal como está?** Para el análisis, esa respuesta es el acuerdo. Después, «Apruebo el análisis» lo deja listo, y sigo con el cambio y la prueba.

### 37 · Usuario, 2026-10-08 22:16:34
> Apruebo el análisis

**Agente**, 2026-10-08 22:23:27
<!-- agente: 6f65250a-d7fd-473a-9ece-2a49dd89a04e -->

Quedó aprobado. Ahora sí hago el cambio en `manage.py`.

El plan todavía cita el análisis 1, que no nombra la HU. Lo cambio para que cite el análisis 2, que sí la nombra y ya está aprobado.

El freno señaló `core/comun/enganches.py`, pero ese cambio no es mío: otra sesión lo modificó a las 22:17. No lo toco. Sigo con `manage.py`.

Ahora la prueba.

Las 4 pruebas pasan, y esta vez `python manage.py` arrancó con el Python del computador. Ahora la consulta real (CP-004):

La consulta del aviso ya funciona tal como está escrita, y las tildes salen bien. Cierro los documentos de la fase.

Corro los validadores de la fase y de la trazabilidad.

**Quedó funcionando.** El comando del aviso de cada sesión ya consulta las reglas sin error y escribe bien las tildes.

**Lo que cambió**
- [manage.py](../../../../../proyectos/cimiento/manage.py) revisa con qué Python lo abrieron. Si no es el de Cimiento (`.venv`), se vuelve a abrir solo con ese. Si ya es ese, o si Cimiento todavía no tiene `.venv`, sigue con el que lo abrió. Además, escribe la salida en un formato que conserva las tildes.
- [tests_arranque.py](../../../../../proyectos/cimiento/core/comun/tests_arranque.py) trae 4 pruebas, y pasaron las 4 corriéndolas con el Python del computador.
- La consulta real `python proyectos/cimiento/manage.py ver_estandar base/01-conducta/palabras-clave.md` terminó sin error, con «capítulo» y «qué» bien escritos.

**Documentación**
- La HU-011 de la EP-026 quedó como terminada.
- La fase tiene completos su plan, su resultado de pruebas, la descripción de lo hecho y su estado.
- Quedaron registradas dos lecciones aprendidas: S-355 y S-356.
- Los validadores de fases, trazabilidad y plan dieron 0 fallas. El único aviso nuevo es que falta el commit.

`proyectos/cimiento/core/comun/enganches.py` también aparece modificado, pero ese cambio es de otra sesión y no va en el commit.

**¿Aprueba el commit y la subida a git?** Llevaría solo lo de esta sesión:
- la HU-011 y su fase;
- `manage.py` y su prueba;
- los pendientes 145 y 142 con sus análisis;
- el resumen de la sesión, el índice y la transcripción.

> acá termina la conversación

---

## Lo acordado

1. La HU: el punto 1 de «Lo que se tiene que hacer» del análisis 1 lo construye la EP-026·HU-011, `manage.py` se abre siempre con el Python de Cimiento y escribe bien las tildes, con su fase `A-EP-026-HU-011-manage-py-busca-su-python`; el plan de esa fase sigue tal cual (turno 37).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `02·F8` (solo se edita lo que el plan aprobado declara) y `02·F4` (el plan que cita un análisis cuenta como aprobado solo si ese análisis nombra la HU). No choca ninguna.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| La HU-011 y su fase | Creadas con el andamio, con plan de trabajo y plan de pruebas; `manage.py` sin tocar |
| Lo que pide el freno | `PlanDeTrabajo.aprobado` (`core/enganches/plan_vs_hecho.py:136`) exige la versión en la aprobación del plan y que el análisis citado nombre `EP-026·HU-011` en «Lo que se tiene que hacer» |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| Análisis 1 del pendiente 141 | Confirma: nombra la HU exacta en «Pasó a» (`EP-029·HU-001`), y por eso sus fases se dejaron editar |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | Ninguno: el cambio queda en el análisis |
| Normas y leyes | Ninguna |
| Herramientas | El freno lee «Pasó a» buscando el patrón `EP-NNN·HU-NNN` |

### Dónde más puede pasar

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| La HU-011 | Su fase A | Se queda detenida | Punto 2 |
| Cualquier análisis que deje la HU «por crear» | Los análisis futuros | El mismo bloqueo | La lección 1 |

---

## Propuesta final: hallazgo y pendiente V2, épica y HU

### Hallazgo V2. Igual que H-5: el análisis no lo cambia

### Pendiente V2. Igual al pendiente 145, con H-5 sumado a «De dónde sale»

### Épica y HU que salen del análisis

La misma [EP-026: el estándar vive en la base de Cimiento y cada cambio queda versionado](../../../../../documentacion/epicas/EP-026-el-estandar-vive-en-la-base-de-cimiento-y-cada-cambio-queda-versionado/epica.md).

| Orden | HU | Título | Parte del problema que resuelve | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|---|---|
| 1 | 011 | `manage.py` se abre siempre con el Python de Cimiento y escribe bien las tildes | El aviso manda a leer las reglas con un comando que falla | Ninguna | Es la única | 2 |

## Lecciones aprendidas

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | Si la HU todavía no existe, el análisis le pone su número antes de aprobarse, para nombrarla en «Pasó a» | Falló | Se escribe al aprobar | Complementa R-19 |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Pasar el pendiente a su versión siguiente, con H-5 en «De dónde sale» | `13·DOC26` | Este análisis, de una y sin fase: `historico-chat/resumenes/2026-10-08/pendientes/145-manage-py-usa-el-python-de-cimiento/pendiente.md`, hecho el 2026-10-08 |
| 2 | `manage.py` revisa con qué Python lo abrieron; si no es el de `.venv` y ese existe, se vuelve a abrir con él y con los mismos argumentos; escribe la salida en UTF-8; y una prueba lo abre con el Python del computador y confirma que responde sin error y con las tildes bien | Análisis 1, acuerdo 1; acuerdo 1 | EP-026·HU-011 |

## Lo que aporta al análisis principal

**Resultado:** aclara.

**Lo que suma al análisis principal:** El análisis que manda a construir algo nombra la HU exacta que lo hace, para que el freno reconozca el plan de su fase como aprobado.
