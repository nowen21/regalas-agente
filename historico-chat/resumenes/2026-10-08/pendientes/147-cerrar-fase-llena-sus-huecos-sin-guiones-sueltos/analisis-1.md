# Análisis 1: los huecos que deja `cerrar_fase` se llenan con un guion que no está en Cimiento

> **Aprobado** por el usuario el 2026-10-09, en el turno 9, con la versión 56.8.0. Desde ese momento este análisis no se reescribe.

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
| R-1 | «Dónde más puede pasar» revisa los demás programas que dejan `«…»` y los proyectos que heredan |
| R-2 | Se reutiliza lo que ya existe: `Fase.faltan()` ya dice archivo y línea de cada hueco, y el comando `documento` de EP-030·HU-001 ya es el camino fijo para escribir documentos |
| R-19 | El plan declara todo lo que pida el cambio; se define cuando se decida dónde se construye |
| Las demás | No aplican: no se cambia ninguna regla (R-3, R-4) y no hay piloto (R-16) |

---

## Hallazgo

### H-2 · Completar el cierre de una fase se hace con un guion suelto

| Campo | Valor |
|---|---|
| Qué pasó | `manage.py cerrar_fase` deja `«…»` en lo que un programa no sabe. El 2026-10-06 esos huecos se llenaron con `historico-chat/scripts/2026-10-06/llenar_marcas.py` y 25 archivos `.txt`, uno por documento |
| Por qué importa | Cada cierre vuelve a armar los mismos archivos a mano, y el guion que ya funciona no está en Cimiento |
| Pendiente | [Pendiente 147: cerrar una fase llena sus huecos sin guiones sueltos](pendiente.md) |

## Pendiente

**De dónde sale:** H-2 de la [sesión del 2026-10-08](../../guiones-que-pasan-a-cimiento.md).

**El problema.** `manage.py cerrar_fase` (`proyectos/cimiento/core/herramientas/fase.py`) escribe los documentos de cierre y deja `«…»` en lo que un programa no puede saber: el resumen, los hallazgos, el veredicto. Cimiento no tiene cómo llenar esos huecos. El 2026-10-06 se llenaron con un guion suelto, `llenar_marcas.py`, y 25 archivos `.txt` con un valor por línea.

**Por qué importa.** Cada fase que se cierra vuelve a necesitar el guion y sus archivos sueltos. El guion ya funciona y comprueba que el número de valores coincida con el de huecos, pero vive fuera de Cimiento y cada sesión tiene que encontrarlo. Se relaciona con el pendiente 142: cada operación termina en un guion nuevo.

---

## Conversación

> La escribe el enganche en tiempo real, turno por turno, desde la transcripción de la sesión. No se escribe a mano.

### 4 · Usuario, 2026-10-09 08:08:34
> Analicemos: el pendiente 147

**Agente**, 2026-10-09 08:11:32
<!-- agente: bc73799c-8976-4ce0-93b2-efbada1f834c -->

Leo el análisis que se acaba de abrir y el código de `cerrar_fase` y del guion.

Ya encontré lo central. Reviso el comando `documento` de EP-030·HU-001, que puede cambiar la recomendación.

Ya tengo lo necesario. Escribo el análisis.

Necesito una decisión suya: **¿el llenado de los huecos se construye dentro de EP-030·HU-004, o ahora sobre los `.md`?** Le recomiendo hacerlo dentro de la HU-004.

El análisis quedó escrito en [analisis-1.md](../../../../../historico-chat/resumenes/2026-10-08/pendientes/147-cerrar-fase-llena-sus-huecos-sin-guiones-sueltos/analisis-1.md). Esto es lo principal que encontré:

- **El guion se usó una sola vez.** Fue el 2026-10-06, para cerrar varias fases juntas. En las fases cerradas el 2026-10-07 y el 2026-10-08, los huecos se llenaron editando el documento directamente, sin guion.
- **El problema real es otro.** Cada hueco aparece como `«...»`, sin decir qué va ahí. Quien lo llena tiene que leer el documento para adivinarlo.
- **La EP-030·HU-004 ya va a cambiar esto.** Esa HU pasa los documentos de la fase a la base de Cimiento, cada uno dividido en campos, y modifica el mismo programa (`fase.py`). Con ella, cada hueco queda como un campo con nombre («resumen», «hallazgos», «veredicto») y se llena con el comando fijo, sin archivos sueltos.

Por eso recomiendo sumarlo a la HU-004: si se construye hoy sobre los `.md`, ese trabajo habrá que rehacerlo cuando llegue esa HU. La otra opción es una HU nueva en la EP-025, con una opción `--llenar` en `cerrar_fase`. Sirve desde ya, pero después se reescribe.

### 5 · Usuario, 2026-10-09 08:15:10
> pregunta de qué huecos habla?

**Agente**, 2026-10-09 08:15:38
<!-- agente: b212b05c-20b8-4dbe-b426-3c500619ca91 -->

Los huecos son los espacios que `cerrar_fase` deja marcados con `«...»` en los tres documentos que escribe al cerrar una fase. Ahí va lo que el programa no puede saber solo, porque depende de lo que pasó en el trabajo:

- **Estado de la fase** (`estado-fase.md`): los defectos que se aceptaron, qué se decidió y en qué señal quedó anotado.
- **Resultado de las pruebas** (`resultado_pruebas.md`):
  - en qué ambiente se probó;
  - en cada caso de prueba, con qué se probó y qué salió;
  - qué salió distinto de lo esperado;
  - qué defectos aparecieron;
  - por qué la fase cumple;
  - dónde está la evidencia.
- **Funcionalidad implementada** (`funcionalidad_implementada.md`):
  - un resumen de lo que se hizo;
  - qué faltó y qué tareas no se hicieron;
  - qué archivos se tocaron sin estar en el plan;
  - cómo se usa lo que se hizo;
  - las decisiones que no son obvias y su porqué;
  - la deuda y los pendientes que quedan;
  - qué índices se actualizaron;
  - si hubo despliegue.

En una fase de cuatro casos de prueba quedan más de 20 huecos. Todos aparecen iguales, como `«...»`, sin decir qué va en cada uno. Por eso hay que leer el documento para saber qué pide cada hueco.

Las rutas de la lista son las de [fase.py:167-286](../../../../../proyectos/cimiento/core/herramientas/fase.py#L167-L286).

### 6 · Usuario, 2026-10-09 08:16:32
> pregunta y qué se propone para soluciónar eso?

**Agente**, 2026-10-09 08:16:47
<!-- agente: 0efd1b8f-0567-4395-a00f-a4b92c2aa495 -->

La propuesta es que cada hueco diga qué hay que poner en él y que se llene con un comando de Cimiento, sin guiones sueltos.

Hoy el cierre de una fase es como un formulario con 20 casillas en blanco y sin título: para saber qué va en cada una hay que leer todo el documento.

**Lo que cambia:**

1. **Cada hueco lleva un nombre.** En vez de `«...»`, dice «resumen», «qué salió distinto», «defectos», «cómo se usa», etc. Así `cerrar_fase` puede avisar: «falta el resumen y la deuda», en lugar de «falta algo en la línea 47».
2. **Se llena con un comando de Cimiento.** Por ejemplo: «poner en el resumen de esta fase este texto». El comando revisa que el texto no dañe las tablas del documento, y ya no hacen falta el guion ni los archivos `.txt`.

**Cuándo hacerlo.** Hay dos opciones:

- **Recomendada: dentro de EP-030·HU-004.** Esa HU pasa los documentos de cada fase a la base de Cimiento, dividido cada uno en campos. Al hacer ese paso, cada hueco ya queda como un campo con nombre, y se llena con el comando `documento` que ya existe. Mientras tanto, los huecos se siguen llenando como en las fases del 2026-10-07 y del 2026-10-08: editando el documento directamente.
- **Ahora, sobre los archivos `.md`.** Funciona desde ya, pero cuando llegue la HU-004 ese trabajo hay que hacerlo de nuevo, porque esa HU cambia el mismo programa.

### 7 · Usuario, 2026-10-09 08:17:47
> hágalo en la que recomienda

**Agente**, 2026-10-09 08:19:33
<!-- agente: 82785f26-eb34-4947-bf28-9431087e839b -->

Anoto la decisión en el análisis y preparo la fila que suma el criterio a EP-030·HU-004.

Edito "Lo acordado", la propuesta y "Lo que se tiene que hacer".

Ahora sumo el CA-04 a la HU-004, que es la ruta que nombra la fila 1.

El freno no reconoció la ruta porque iba guardada en una variable del comando. Hago la misma edición con la ruta escrita completa.

**Para cerrar el pendiente 147, falta que escriba «Apruebo el análisis».**

Esto es lo que dejé hecho:

- **En el [análisis](../../../../../historico-chat/resumenes/2026-10-08/pendientes/147-cerrar-fase-llena-sus-huecos-sin-guiones-sueltos/analisis-1.md)** quedaron dos acuerdos:
  - la solución: cada hueco lleva el nombre de lo que pide y se llena con un comando de Cimiento;
  - dónde se construye: dentro de EP-030·HU-004.
- **En la [HU-004](../../../../../documentacion/epicas/EP-030-los-documentos-de-cimiento-viven-en-su-base/HU-004-las-epicas-las-hu-y-los-documentos-de-cada-fase-viven-en-la-base/HU-004-las-epicas-las-hu-y-los-documentos-de-cada-fase-viven-en-la-base.md)** agregué el criterio CA-04, «Cerrar una fase dice qué falta y se llena con un comando de Cimiento», y lo anoté en su bitácora.

El código no se toca ahora. Se construye cuando se trabaje la HU-004, que todavía no ha empezado. Hasta entonces, los huecos se siguen llenando editando el documento directamente.

Al anotar la bitácora, el freno detuvo un comando porque la ruta del archivo iba dentro de una variable y no la pudo leer. Hice la misma edición con la ruta escrita completa.

### 8 · Usuario, 2026-10-09 08:20:37
> pregunta osea que ya quedo claro el análisis del pendiente 147?

**Agente**, 2026-10-09 08:20:47
<!-- agente: 47c9d750-3875-4d4b-90b7-5afd013a2d02 -->

Sí, el análisis está completo y no queda ninguna decisión abierta. Se acordaron dos cosas:

1. **La solución:** cada hueco del cierre de una fase lleva el nombre de lo que pide, y se llena con un comando de Cimiento, sin guiones sueltos.
2. **Dónde se construye:** dentro de EP-030·HU-004, cuando los documentos de cada fase pasen a la base de Cimiento. Ya quedó escrito en esa HU como criterio CA-04.

Lo único que falta es la aprobación formal del documento. El programa que marca el análisis como aprobado solo reconoce la frase exacta «Apruebo el análisis». Con esa aprobación el pendiente 147 queda resuelto, y seguimos con el 148.

### 9 · Usuario, 2026-10-09 08:22:04
> Apruebo el análisis

**Agente**, 2026-10-09 08:23:47
<!-- agente: e3cfca30-1812-4d64-beca-6e43795d4a55 -->

Quedó aprobado. Registro la lección del análisis como señal.

El análisis del pendiente 147 quedó aprobado y ya está resuelto. **Para seguir, escriba «Analicemos: el pendiente 148».**

- **El análisis:** quedó marcado como aprobado y su resumen se agregó al análisis principal del proyecto.
- **La HU-004 de la EP-030:** ya tiene el criterio CA-04. El cambio en el código se hace cuando se construya esa HU.
- **La lección** («un hueco sin nombre obliga a leer el documento para saber qué va en él») quedó registrada como señal S-360.

Todavía no hay commit. Le pregunto por él cuando terminemos los pendientes de esta sesión.

> acá termina la conversación

---

## Lo acordado

1. La solución: cada hueco que deja `cerrar_fase` (y `reabrir_fase`) lleva el nombre de lo que pide, `cerrar_fase` dice por nombre cuáles faltan, y se llenan con un comando de Cimiento que revisa que el texto no dañe el documento; sin guion ni archivos `.txt` (turnos 6 y 7).
2. Dónde: se construye dentro de EP-030·HU-004, cuando los documentos de la fase pasen a la base partidos en campos; cada hueco es un campo y se llena con el comando `documento`. Mientras tanto, los huecos se llenan editando el documento (turno 7).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `02·F0` (el cambio recorre la cadena), `04·S9` (los guiones de apoyo quedan en el repositorio, pero lo que se repite pasa a ser funcionalidad), `08·T1` (el cambio lleva su prueba) y `02·F11` (la fase toca solo su módulo). No choca ninguna.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| `cerrar_fase` | Dos pasadas. La primera escribe `estado-fase.md`, `resultado_pruebas.md` y `funcionalidad_implementada.md` con `«…»` en lo que no sabe; mientras quede uno, no cierra y dice `archivo:línea` de cada hueco (`Fase.faltan()`, `fase.py:287`). La segunda cierra |
| `llenar_marcas.py` | 30 líneas en `historico-chat/scripts/2026-10-06/`. Reemplaza en orden cada `«…»` y `«se llena al cerrar»` por una línea de un `.txt`; si sobran o faltan valores, no escribe. Se usó una sola vez, con 21 `.txt`, para cerrar varias fases juntas |
| Los cierres de después | Las fases cerradas el 2026-10-07 y el 2026-10-08 (entre ellas EP-026·HU-011) llenaron los huecos editando los documentos directamente, sin guion |
| Lo que falta | Que `cerrar_fase` diga **qué** va en cada hueco, no solo dónde está: hoy el hueco es `«…»` sin nombre, y quien lo llena tiene que leer el documento para saber qué le piden |
| EP-030·HU-004 | Pendiente. Pasa las épicas, las HU y los documentos de cada fase a la base, partidos en campos, y cambia `fase.py` para que lea y escriba la base (CA-03). Con eso cada hueco pasa a ser un campo con nombre |
| El comando `documento` | Terminado en EP-030·HU-001: crea, ve y edita documentos por un camino fijo, y el cambio queda como propuesta |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| Análisis 2 del pendiente 119, acuerdo 6 (citado en `fase.py`) | Confirma: «lo que se repite es una funcionalidad de Cimiento, no un guion». Así nació `cerrar_fase`, y este pendiente es su parte que quedó afuera |
| Análisis 1 del pendiente 142 | Muestra que los documentos de la fase pasan a la base. Lo que se construya hoy sobre los `.md` se reescribe en EP-030·HU-004 |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | MENOR (`20·M10`): una opción nueva de un comando que ya tienen; no les pide nada |
| Normas y leyes | Ninguna |
| Herramientas | Un valor puede traer `\|` o saltos de línea y romper la tabla del documento; el guion actual no lo revisa |

### Dónde más puede pasar

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| `reabrir_fase` | Suma un ciclo con dos `«…»` en el resultado | El mismo guion para llenarlos | Lo que se decida para `cerrar_fase` vale igual: los dos usan `Fase.faltan()` |
| El andamio de la fase | Deja `«…»` en el plan de trabajo y el de pruebas | Llenarlos también a mano | No hace falta: el plan lo escribe el agente completo, no por huecos |
| Las plantillas del análisis, la HU y la épica | `plantillas/` | Lo mismo | No hace falta: se llenan escribiendo el documento, no con valores sueltos |
| Los proyectos que heredan | Toda fase que se cierre con `cerrar_fase` | El mismo guion en cada proyecto | Lo que se decida llega por `instalar.py`, porque es Cimiento |

---

## Propuesta final: hallazgo y pendiente, épica y HU

El hallazgo H-2 y el pendiente 147 quedan como están.

### Épica y HU que salen del análisis

Se suma a la [EP-030: los documentos de Cimiento viven en su base](../../../../../documentacion/epicas/EP-030-los-documentos-de-cimiento-viven-en-su-base/epica.md), dentro de su HU-004 (acuerdo 2). Se descartó construirlo ahora sobre los `.md`, porque la HU-004 reescribe el mismo `fase.py`.

1. **Elegido: se suma a EP-030·HU-004.** Cuando los documentos de la fase pasen a la base, cada hueco es un campo con nombre («resumen», «hallazgos», «veredicto»), y `cerrar_fase` dice qué campo falta. Se llena con el comando fijo, sin archivos sueltos. Mientras tanto, los huecos se siguen llenando editando el documento, como en los cierres del 2026-10-07 y 2026-10-08. Construir hoy sobre los `.md` se reescribe en esa HU, que ya cambia `fase.py`.
2. **Descartado, ahora sobre los `.md`:** una HU nueva en la épica de `cerrar_fase` (EP-025), con una opción `--llenar` que recibe los valores, comprueba que el número coincida y que ninguno rompa una tabla, y escribe. Sirve ya, y se reescribe en EP-030·HU-004.

| Orden | HU | Título | Parte del problema que resuelve | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|---|---|
| 1 | 004 (existente) | Las épicas, las HU y los documentos de cada fase viven en la base, partidos en campos | Los huecos del cierre se llenan con un guion suelto y no dicen qué piden | EP-030·HU-001 | Ya está en la épica; este análisis le suma un criterio | 1 y 2 |

## Lecciones aprendidas

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | Un hueco sin nombre obliga a leer el documento para saber qué va en él; el programa que deja el hueco dice qué pide | Falló | S-360 | No aplica |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Sumar a EP-030·HU-004 el criterio CA-04: cada hueco de los documentos de cierre de una fase es un campo con el nombre de lo que pide; `cerrar_fase` y `reabrir_fase` dicen por nombre cuáles faltan; se llenan con el comando `documento`, que rechaza el texto que dañe el documento; y ya no hace falta `llenar_marcas.py` | 1, 2 | Este análisis, de una y sin fase: `documentacion/epicas/EP-030-los-documentos-de-cimiento-viven-en-su-base/HU-004-las-epicas-las-hu-y-los-documentos-de-cada-fase-viven-en-la-base/HU-004-las-epicas-las-hu-y-los-documentos-de-cada-fase-viven-en-la-base.md`, hecho el 2026-10-09 |
| 2 | Construir el CA-04 | 1, 2 | EP-030·HU-004 |

## Lo que aporta al análisis principal

**Resultado:** amplía.

**Lo que suma al análisis principal:** Cerrar una fase no deja nada para llenar por fuera de Cimiento: cada hueco dice qué pide y se llena con un comando suyo.
