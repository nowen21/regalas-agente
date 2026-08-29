# Plan de Pruebas — Fase `A-EP-001-HU-015-retrodocumentar-el-capitulo-02`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** el criterio de esta fase, con qué datos y cuándo se da por aprobado. Lo que se pide vive en la [HU-015](../HU-015-el-capitulo-02-flujo-de-trabajo.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

> **Molde de veintiuna.** Lo que se apruebe acá se repite para las otras veinte historias de capítulo de `EP-001`, cambiando el número y sus cifras.

---

## 1. Introducción

### 1.1 Propósito

Comprobar que el capítulo `02` **nombra su historia dueña con un enlace que resuelve**, y que un cambio suyo **tiene dónde bajarse**.

### 1.2 Alcance

**Entra:** la cabecera del capítulo, el enlace, y que la historia exista con su §8 lista para recibir la fila de una fase.

**No entra:** el contenido de las 32 reglas del capítulo, sus checklists, ni su comprobación automática.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | La medición 21 de 21 que decidió qué clase de fase es esta |
| `13·DOC6` | Qué es retro-documentar y cuándo aplica |
| `02·F12.1` | Por qué son veintiuna fases y no una |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| La cabecera del capítulo | Que **nombre** la historia, y que el enlace **resuelva** |
| La historia | Que exista, y que su §8 reciba la fila de la fase |
| El conjunto de las 21 | Que la afirmación *«todas la nombran»* **se pueda repetir**, no creer |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

**Sobre el repositorio real**, que es lo único donde la afirmación tiene sentido.

| Tipo | Por qué |
|---|---|
| **De verificación** | Es retro-documentación: se comprueba lo que hay, no lo que se construyó |
| **Que el enlace resuelva** | Nombrar la historia y enlazarla mal es no nombrarla |
| **Repetible a máquina** | Leer 21 cabeceras a ojo da un «sí» que nadie puede volver a obtener |
| **De borde** | Un capítulo que fuera carpeta y no archivo suelto |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-001 | **Si el enlace no resuelve, el `CA-01` no se cumple aunque el nombre esté escrito** |
| Alta | CP-000 | La medición que decide qué clase de fase es esta |
| Media | CP-002, CP-003 | Que la historia reciba la fila, y que las dos formas de capítulo se lean |

### 3.3 Alcance de la ejecución automatizada  ·  `02·F5`

`validar.py enlaces` y `validar.py fases`, que son las que esta fase toca. **No se corre la suite entera**: esta fase no toca código.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- Los dos planes, aprobados.
- **La `T-00` corrida**, con su lista de 21 nombres.

### 4.2 Criterios de salida

- Los cuatro casos ejecutados.
- El enlace de la cabecera, **resuelto de verdad**, no leído.
- La fila de la fase en la §8 de la historia.

### 4.3 Criterios de suspensión y reanudación

Se suspende si:

- **El enlace de la cabecera no resuelve.** Entonces el `CA-01` no se cumple, la fase deja de ser retro-documentación y hay que replantearla.
- **Al leer el capítulo aparece que hay que cambiarlo.** Se anota y se para: corregirlo es otra fase (`02·F20`).

**El primero está escrito para que la fase pueda fracasar**, y es lo único que la separa de un trámite: si el enlace está roto, «21 de 21» era falso.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| Previo · el estado de las 21 | CP-000 | De impacto |
| CA-01 — el capítulo nombra su historia dueña | CP-001 | De verificación |
| CA-02 — un cambio tiene dónde bajarse | CP-002 | De sistema |
| Transversal — las dos formas de capítulo | CP-003 | De borde |

---

## 6. Casos de prueba

### CP-000 — El estado de las veintiuna

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `t00-las-22-historias-de-capitulo.py` | Lista las 21, una por línea |
| 2 | Contar cuántas tienen su historia nombrada en la cabecera | **21 de 21** |
| 3 | Si alguna dijera «NO», **parar y replantear esa** | — |

**Sin este caso, cada una de las veintiuna fases sería una apuesta.** Con él, se sabe antes de abrir la carpeta si hay algo que construir.

---

### CP-001 — La cabecera nombra su historia, y el enlace resuelve   ·   **el crítico**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir `base/02-flujo-de-trabajo/base.md` y leer su cabecera | Nombra `EP-001 HU-015` |
| 2 | Comprobar que el enlace **apunta a un archivo que existe** | Resuelve |
| 3 | Correr `validar.py enlaces` sobre el estándar | **Sin enlaces rotos** |
| 4 | Comprobar que el texto dice **para qué** sirve la historia, no solo su nombre | Dice que todo cambio del capítulo baja por ella |

**El paso 2 es el que decide.** Nombrar la historia y enlazarla mal es no nombrarla: quien abra el capítulo para saber dónde baja un cambio se queda igual. El paso 3 lo comprueba **a máquina y sobre todo el cuerpo**, no solo acá.

---

### CP-002 — Un cambio del capítulo tiene dónde bajarse

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Comprobar que la `HU-015` existe con su documento | Existe |
| 2 | Comprobar que tiene §8 «Fases que la implementan» | La tiene |
| 3 | Escribir la fila de esta fase | Queda |
| 4 | Correr `validar.py fases` | La historia deja de contar «sin fases» |

**El paso 4 es la prueba de que sirvió**: la historia pasa de no tener dónde bajar un cambio a tenerlo.

---

### CP-003 — Las dos formas de capítulo se leen igual

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Comprobar que el programa encuentra un capítulo que es **archivo suelto** | Lo encuentra |
| 2 | Y uno que es **carpeta con `base.md`** —como el `02`— | Lo encuentra |
| 3 | Comprobar que ninguno de los 21 quedó como «no se encuentra» | **Cero** |

**Es de borde y hace falta:** `base/` tiene las dos formas, y un programa que solo viera una diría «no se encuentra el capítulo» y eso se leería como que la historia está mal.

---

## 7. Datos y ambientes de prueba

El repositorio real. **Ninguna prueba usa credenciales** (`00·N6`) y **ninguna escribe en `base/`**: esta fase lee el capítulo, no lo toca.

---

## 8. Herramientas

`validar.py enlaces`, `validar.py fases`, y el programa de la `T-00`. **Sin guion de sabotaje**: no se escribió código que sabotear. Lo que hace las veces es el `CP-001` paso 2 — si el enlace no resolviera, el caso lo dice.

---

## 9. Gestión de defectos

| Severidad | Qué la define |
|---|---|
| Crítica | El enlace de la cabecera no resuelve |
| Alta | Alguna de las 21 no nombra su historia |
| Media | La fila no queda, o `validar.py fases` sigue contando la historia sin fases |
| Baja | Redacción |

---

## 10. Cronograma

Un solo tramo. La `T-00` ya corrida, antes de abrir la carpeta.

---

## 11. Roles y responsabilidades

Una sola persona cumple los roles. El agente comprueba y escribe; el usuario aprueba.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Casos ejecutados | 4 de 4 |
| **Capítulos de los 21 sin su historia nombrada** | **0** |
| **Enlaces rotos en el estándar** | **0** |
| Historias que siguen contando «sin fases» tras la fila | 0 |
| Archivos de `base/` tocados | **0** |

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Dar por bueno el nombre sin comprobar el enlace | `CP-001` paso 2, y `validar.py enlaces` en el 3 |
| Leer 21 cabeceras a ojo | El programa de la `T-00`, que deja la lista con nombres |
| **Que la fase parezca hecha por tener sus cinco archivos** | Es `H-40`. El comprobador ya rechaza los moldes sin llenar |
| Que veintiuna fases iguales vuelvan la revisión un trámite | Se declara de frente: **el molde se aprueba una vez** |

---

## 14. Control de versiones

| Versión | Fecha | Cambio |
|---|---|---|
| 1 | 2026-08-28 | Redacción inicial, junto con el plan de trabajo |

---

## 15. Aprobación

| Rol | Estado |
|---|---|
| Usuario | **Aprobado** el 2026-08-28, **como molde de las veintiuna** |
