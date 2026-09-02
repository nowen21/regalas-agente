# Resultado de Pruebas — Fase `A-EP-001-HU-035-retrodocumentar-el-capitulo-22`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. Alimenta el [estado-fase.md](estado-fase.md) y la sección «qué se probó» del [funcionalidad_implementada.md](funcionalidad_implementada.md). El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md), que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-001-HU-035-retrodocumentar-el-capitulo-22` |
| **HU** | [HU-035](../HU-035-el-capitulo-22-sistemas-que-aprenden-de-datos.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-28 |
| **Ejecutado por** | El agente, sobre este repositorio |
| **Ambiente y versión** | Windows 11 · Python 3.11 · Cimiento `35.9.0` |

---

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

---

## 2. Ejecución caso por caso

### CP-000 — El estado de las veintiuna

**El problema que resuelve:** sin saber en qué estado están las 21, cada fase sería una apuesta: se abriría sin saber si hay algo que construir.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr `t00-las-22-historias-de-capitulo.py` | Lista las 21 | Las listó, una por línea con su capítulo |
| 2 | Contar las que nombran su historia | **21 de 21** | **21 de 21** |
| 3 | Si alguna dijera «NO», parar | — | Ninguna dijo «NO» |

**Cómo se verificó que la pareja cumple:** decide el paso 2, y lo que lo hace útil es que la salida trae **los 21 nombres**, no solo el total. Un total no se puede volver a comprobar; una lista sí.

---

### CP-001 — La cabecera nombra su historia, y el enlace resuelve   ·   **el crítico**

**El problema que resuelve:** nombrar la historia y enlazarla mal es no nombrarla. Quien abra el capítulo para saber dónde baja un cambio se queda igual.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Abrir `base/22-sistemas-que-aprenden-de-datos.md` y leer su cabecera | Nombra la HU-035 | Nombra la HU-035 |
| 2 | Comprobar que el enlace apunta a un archivo que **existe** | Resuelve | `../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-035-el-capitulo-22-sistemas-que-aprenden-de-datos/HU-035-el-capitulo-22-sistemas-que-aprenden-de-datos.md` → **resuelve** |
| 3 | Correr `validar.py enlaces` sobre el estándar | Sin enlaces rotos | **Sin enlaces rotos** |
| 4 | Comprobar que dice **para qué** sirve la historia | Dice que todo cambio baja por ella | Lo dice, citando `02·F23` |

**Cómo se verificó que la pareja cumple:** decide el paso 2, no el 1. El 1 se puede pasar leyendo; **el 2 exige que el archivo del otro lado exista**, y el 3 lo comprueba a máquina sobre todo el cuerpo, no solo acá.

---

### CP-002 — Un cambio del capítulo tiene dónde bajarse

**El problema que resuelve:** una historia sin fases no es un sitio donde algo pueda bajar: es un documento suelto.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Comprobar que la HU-035 existe | Existe | Existe |
| 2 | Comprobar que tiene §8 «Fases que la implementan» | La tiene | La tiene |
| 3 | Escribir la fila de esta fase | Queda | Quedó |
| 4 | Correr `validar.py fases` | La historia deja de contar «sin fases» | Dejó de contarse |

**Cómo se verificó que la pareja cumple:** decide el paso 4, y no el 3. Escribir la fila es afirmar; **que el comprobador deje de reclamar es que la afirmación se pueda leer a máquina.**

---

### CP-003 — Las dos formas de capítulo se leen igual

**El problema que resuelve:** `base/` tiene capítulos que son archivo suelto y capítulos que son carpeta con `base.md`. Un programa que solo viera una forma diría «no se encuentra el capítulo», y eso se leería como que la historia está mal.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Ver de qué forma es este capítulo | — | **archivo suelto** |
| 2 | Comprobar que el programa lo encuentra igual | Lo encuentra | Lo encontró |
| 3 | Comprobar que ninguno de los 21 quedó «no se encuentra» | **Cero** | **Cero** |

---

| Caso | CA | Prioridad | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-000 | Previo | Alta | 2026-08-28 | los 21 listados con nombre: **21 de 21** nombran su historia | Aprobado | EV-00 | — |
| CP-001 | CA-01 | **Crítica** | 2026-08-28 | la cabecera de `base/22-sistemas-que-aprenden-de-datos.md`, y su enlace **resuelve** | Aprobado | EV-01 | — |
| CP-002 | CA-02 | Media | 2026-08-28 | la fila escrita, y `validar.py fases` que deja de reclamar | Aprobado | EV-02 | — |
| CP-003 | Transversal | Media | 2026-08-28 | este capítulo es **archivo suelto**, y se encuentra igual | Aprobado | EV-00 | — |

**Correspondencia con el plan:** 4 casos en el plan, 4 acá.

**Qué salió distinto de lo esperado:** nada.

---

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que **ningún archivo de `base/` se tocó** | `git status` sobre `base/` | Sin cambios |
| 2 | Que el capítulo tiene sus reglas donde el analizador las ve | `metareglas.reglas()` | **9 regla(s)** |



---

## 4. Defectos encontrados

| ID | Título | Caso que lo destapó | Severidad | Estado | Dónde quedó registrado |
|---|---|---|---|---|---|
| — | Ninguno | — | — | — | — |

**Defectos abiertos que se aceptan y por qué:** ninguno.

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia | Casos | Resultado | Cumple |
|---|---|---|---|
| CA-01 — el capítulo nombra su historia dueña | CP-000, CP-001 | Nombra la HU-035, y el enlace **resuelve** | Sí |
| CA-02 — un cambio tiene dónde bajarse | CP-002 | La historia recibe la fila y el comprobador deja de reclamar | Sí |

**Los que no cumplen:** ninguno.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Casos ejecutados | Plan §12 | 4 de 4 | 4 de 4 | Sí |
| **Capítulos de los 21 sin su historia nombrada** | Plan §12 | **0** | **0** | Sí |
| **Enlaces rotos en el estándar** | Plan §12 | **0** | **0** | Sí |
| Historias que siguen «sin fases» tras la fila | Plan §12 | 0 | 0 | Sí |
| **Archivos de `base/` tocados** | Plan §12 | **0** | **0** | Sí |

**Lo que no se cumplió:** nada.

---

## 6. Veredicto de la fase

**Concepto:** **Cumple**

**Justificación:** los dos criterios quedaron cubiertos por casos ejecutados. El crítico —que el enlace de la cabecera **resuelva**, no solo que el nombre esté escrito— se comprobó apuntando al archivo del otro lado y con `validar.py enlaces` sobre todo el cuerpo. **No se tocó ningún archivo de `base/`**, que era el límite de esta fase.

**Qué falta para que cumpla:** nada.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-00 | El estado de las 21, con nombres | [t00-las-22-historias-de-capitulo.py](../../../../../historico-chat/scripts/2026-08-28/t00-las-22-historias-de-capitulo.py) |
| EV-01 | La cabecera del capítulo | `base/22-sistemas-que-aprenden-de-datos.md` |
| EV-02 | La fila y el conteo | `validar.py fases` |

---

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-08-28 | 4 | 0 | Primera ejecución |
