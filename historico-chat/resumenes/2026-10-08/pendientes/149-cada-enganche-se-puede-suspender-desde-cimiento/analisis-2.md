# Análisis 2: la lista de lo suspendido cae en `.agente/`, que el repositorio del estándar no ignora

> **Aprobado** por el usuario el 2026-10-09, en el turno 32, con la versión 56.8.0. Desde ese momento este análisis no se reescribe.

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
| R-1 | «Dónde más puede pasar» revisa los proyectos que heredan y lo demás que escriben los enganches |
| R-6 | Se leyó completo el análisis 1: su plan no declara `.gitignore` |
| R-15 | La ejecución se detuvo en la primera orden que lo destapó, antes de cerrar la fase C |
| Las demás | No aplican: no se cambia ninguna regla (R-3, R-4) y no hay piloto (R-16) |

---

## Hallazgo

### H-3 · El freno detuvo lo que escribió una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-09 11:14, el freno detuvo lo que escribió una orden de consola sobre `.agente/suspendidos.46f1a0bd5592a2f9.json`: el plan de la fase en curso no lo declara, o no está aprobado, y ninguna regla lo autoriza (02·F8). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | El mismo pendiente 149: se trata en su análisis 2 |

## Pendiente

**De dónde sale:** proyecto scilit, hallazgo 1 del resumen del 2026-10-08.

**El problema.** De los enganches, solo el freno se puede suspender desde Cimiento; en git la única salida es `--no-verify`.

**Por qué importa.** Un enganche que estorba no se puede apagar sin que el checklist marque la instalación como incompleta.

---

## Conversación

> La escribe el enganche en tiempo real, turno por turno, desde la transcripción de la sesión. No se escribe a mano.

### 28 · Usuario, 2026-10-09 11:16:52
> Analicemos: el pendiente 149

**Agente**, 2026-10-09 11:17:54
<!-- agente: 57b54e2b-2554-4929-925b-b630dc04fb91 -->

El análisis 2 quedó escrito en [analisis-2.md](../../../../../historico-chat/resumenes/2026-10-08/pendientes/149-cada-enganche-se-puede-suspender-desde-cimiento/analisis-2.md). **¿Se agrega `.agente/` al `.gitignore` del repositorio del estándar?** Recomiendo que sí.

Por qué:

- La carpeta `.agente/` guarda lo que los enganches anotan mientras trabajan, como la lista de lo suspendido. Esos archivos no deben subirse a git.
- Los proyectos que heredan el estándar ya la ignoran, porque el instalador la pone en su `.gitignore`.
- A este repositorio le falta esa línea. Sin ella, el freno detiene cada orden que corre una revisión de git, y un `git add` de todo subiría esa carpeta.

Con la aprobación, agrego la línea, cierro la fase C y le aviso cuando funcione.

### 29 · Usuario, 2026-10-09 11:19:48
> respondo no entiendo por qué la pregunta si eso ya está en el ignore

**Agente**, 2026-10-09 11:19:56
<!-- agente: 46300b9a-4856-42e3-b103-e16a605021d6 -->

El `.gitignore` sí tiene una regla para `.agente/`, pero no cubre esta carpeta:

- La línea 17 dice `proyectos/*/.agente/`. Eso ignora la carpeta `.agente/` que está **dentro de cada proyecto**, por ejemplo `proyectos/cimiento/.agente/`.
- La lista de lo suspendido queda en `.agente/`, en la **raíz del repositorio del estándar**. A esa carpeta no la nombra ninguna línea.

Git lo confirma. Al preguntarle si ignora `.agente/suspendidos.....json`, respondió que no, y `git status` muestra `?? .agente/` como carpeta nueva sin guardar.

**¿Agrego la línea `.agente/` para que también ignore la de la raíz?** Recomiendo que sí.

### 30 · Usuario, 2026-10-09 11:21:54
> respondo esto "proyectos/*/.agente/" no debe existir porque .agente es hermano de proyectos y además git también es hermano de proyectos

**Agente**, 2026-10-09 11:22:28
<!-- agente: c72747e3-5981-4900-bc36-6ec678e851ff -->

Reviso si alguna carpeta `proyectos/*/.agente/` existe de verdad, antes de quitar esa regla.

Tiene razón: `.agente/` va en la raíz, junto a `proyectos/` y `.git`, así que la regla correcta es `.agente/` y no `proyectos/*/.agente/`.

Revisé y hoy existe una excepción. El vigilante del consumo deja `proyectos/cimiento/.agente/vigilar-consumo.pid`. Si solo se cambia la línea del `.gitignore`, ese archivo quedaría a la vista de git.

**¿Hago estas dos cosas?**

1. En `.gitignore`, cambiar `proyectos/*/.agente/` por `.agente/`.
2. Que el vigilante guarde su archivo en la `.agente/` de la raíz y no en la de `proyectos/cimiento/`.

### 31 · Usuario, 2026-10-09 11:23:00
> apruebo

**Agente**, 2026-10-09 11:25:43
<!-- agente: ded9002a-2d71-48d5-849a-7a9f43307041 -->

Quedó aprobada la propuesta. La anoto como acuerdo en el análisis. Antes busco dónde escribe el vigilante su archivo.

Escribo los acuerdos en el análisis 2.

Los tres puntos que se hacen de una los hago ahora, mientras el análisis está abierto. Primero el pendiente y el `.gitignore`.

Git ya ignora `.agente/`. Ahora el vigilante.

Para poder probar el traslado, dejo que la función reciba la carpeta de Cimiento.

Hechos los tres puntos, con las 19 pruebas del vigilante en verde:

1. **Pendiente 149:** quedó en su versión 2, con H-3 entre sus orígenes.
2. **`.gitignore`:** ahora dice `.agente/`. Git ya ignora esa carpeta y `git status` no la muestra.
3. **El vigilante:** guarda su número en la `.agente/` de la raíz. Si encuentra el archivo en el sitio viejo, lo mueve al nuevo, para no arrancar un segundo vigilante.

**Escriba «Apruebo el análisis»** y cierro la fase C.

### 32 · Usuario, 2026-10-09 11:27:49
> Apruebo el análisis

**Agente**, 2026-10-09 11:29:43
<!-- agente: 983066ad-dfcb-4364-b657-087c19f96fad -->

Aprobado. Registro la lección y cierro la fase C.

El pendiente 149 quedó terminado y funcionando. La EP-025·HU-032 cerró sus tres fases, y los validadores no dan ninguna falla.

- **Fase A, catálogo y pantalla:** cada uno de los 24 momentos de los enganches y cada revisión de git tiene su nombre. En la pantalla se puede suspender cualquiera, y junto a los que no conviene suspender aparece la advertencia.
- **Fase B, los enganches:** el primer enganche de cada mensaje consulta la base y les cuenta a los demás. El enganche suspendido sale sin hacer nada. Además se corrigió un defecto: el freno tomaba cualquier suspensión de enganche como si fuera la del freno entero.
- **Fase C, revisiones de git:** una revisión suspendida no detiene el guardado y avisa hasta cuándo está suspendida y por qué.
- **Análisis 2:** `.gitignore` ahora ignora `.agente/` en la raíz, y el vigilante guarda ahí su archivo.

Con esto quedan resueltos los cinco pendientes que pidió (145 a 149) y el 150, que salió de esta sesión. Falta confirmar el 149 en scilit, el proyecto que lo pidió: Cimiento pide una prueba allá con resultado «pasa».

**¿Aprueba el commit?** Solo llevaría lo de esta sesión:

- los análisis de los pendientes 146 a 150;
- las HU-030, HU-031 y HU-032 de la EP-025, la HU-008 de la EP-029 y el criterio CA-04 de la EP-030·HU-004;
- el código y las pruebas;
- el `.gitignore`;
- el resumen y la transcripción de la sesión.

No llevaría los archivos que otras sesiones dejaron modificados.

> acá termina la conversación

---

## Lo acordado

1. `.agente/` es hermana de `proyectos/` y de `.git`: en `.gitignore`, `proyectos/*/.agente/` se cambia por `.agente/` (turnos 30 y 31).
2. El vigilante del consumo deja su número de proceso en la `.agente/` de la raíz y no en `proyectos/cimiento/.agente/`; si encuentra el archivo en el sitio viejo, lo pasa al nuevo, para no arrancar un segundo vigilante (turno 31).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `02·F8` (solo se edita lo que el plan aprobado declara) y `09·G3` (no entra al repositorio lo que no es del repositorio). No choca ninguna.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| Dónde queda la lista | `.agente/suspendidos.«sesión».json` en la raíz del proyecto (`core/enganches/suspendidos.py`, fase B). Git usa la sesión «git» |
| Los proyectos que heredan | El instalador pone `.agente/` en su `.gitignore` (`IGNORADOS`, `core/comun/enganches.py`), y el checklist lo revisa: ahí no pasa nada |
| El repositorio del estándar | Su `.gitignore` ignora `proyectos/*/.agente/` y `historico-chat/.tocado/`, no `.agente/` de la raíz. `git status` muestra `?? .agente/` |
| `proyectos/cimiento/.agente/` | Solo tiene `vigilar-consumo.pid`, que escribe el vigilante (`core/consumo/vigilante.py:36`) |
| El freno | Compara `git status` antes y después de cada orden de consola: un archivo nuevo sin ignorar que el plan no declara lo detiene |
| Los enganches de Claude Code | Escriben su lista por fuera de las órdenes de consola: no lo disparan. Las revisiones de git corren dentro de una orden (`git commit`, `validar.py`): lo disparan siempre |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| `IGNORADOS` | Confirma: `.agente/` es estado de trabajo que no va al repositorio; al estándar solo le falta decirlo para sí mismo |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | Ninguno: ya ignoran `.agente/` |
| Normas y leyes | Ninguna |
| Herramientas | Git respeta `.gitignore` en `status`, y el freno lee `status` |

### Dónde más puede pasar

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Cada commit del estándar | Este repositorio | El freno detiene la orden y la lista puede subirse con `git add` | Punto 2 |
| Un proyecto instalado antes de `IGNORADOS` | Proyectos viejos | Lo mismo | No hace falta: el checklist de cada mensaje exige `.agente/` en su `.gitignore` |
| Los demás archivos que los enganches dejan en `.agente/` | Este repositorio | Lo mismo | Punto 2: se ignora la carpeta entera |

---

## Propuesta final: hallazgo y pendiente V2, épica y HU

### Hallazgo V2. Igual que H-3: el análisis no lo cambia

### Pendiente V2. Igual al pendiente 149, con H-3 sumado a «De dónde sale»

### Épica y HU que salen del análisis

La misma EP-025·HU-032. Los puntos 2 y 3 se hacen de una y sin fase; después la fase C se cierra como está.

## Lecciones aprendidas

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | Lo que un enganche escribe en el proyecto se prueba también en el repositorio del estándar, que no se instala como los demás | Falló | S-368 | No aplica |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Pasar el pendiente a su versión siguiente, con H-3 en «De dónde sale» | `13·DOC26` | Este análisis, de una y sin fase: `historico-chat/resumenes/2026-10-08/pendientes/149-cada-enganche-se-puede-suspender-desde-cimiento/pendiente.md`, hecho el 2026-10-09 |
| 2 | Cambiar `proyectos/*/.agente/` por `.agente/` en `.gitignore` | 1 | Este análisis, de una y sin fase: `.gitignore`, hecho el 2026-10-09 |
| 3 | El vigilante deja su número en la `.agente/` de la raíz y pasa ahí el del sitio viejo, con su prueba | 2 | Este análisis, de una y sin fase: `proyectos/cimiento/core/consumo/vigilante.py` y `proyectos/cimiento/core/consumo/tests_vigilante.py`, hecho el 2026-10-09 |
| 4 | Cerrar la fase C de la HU-032 | Análisis 1, acuerdo 4 | EP-025·HU-032 |

## Lo que aporta al análisis principal

**Resultado:** aclara.

**Lo que suma al análisis principal:** El estado de trabajo que dejan los enganches en `.agente/` no entra a ningún repositorio, tampoco al del estándar.
