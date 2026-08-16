# Resultado de Pruebas — Fase «A-EP-004-HU-005-el-marcador-se-resuelve-contra-el-estandar»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el `estado-fase.md` para pasar la puerta de verificación, y la fuente de la sección "qué se probó" del `funcionalidad_implementada.md`. El diseño de los casos vive en el [`plan_pruebas.md`](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar: se aprobó antes y así se queda.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-004-HU-005-el-marcador-se-resuelve-contra-el-estandar` |
| **HU** | [HU-005 — Comprobar los enlaces y las citas a reglas](../HU-005-enlaces-y-citas.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-16 |
| **Ejecutado por** | El agente |
| **Ambiente y versión** | Windows 11 · Python 3.11 · estándar 21.1.1 · carpetas temporales desechables |

**Con qué se corre:**

```
python -m unittest discover -s validadores/tests
```

---

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

Los tres primeros casos corren **dos veces**, una por cada carpeta de prueba: la de nombre normal y la de nombre con espacio y tilde (el CP-004). Por eso `unittest` reporta 6 pruebas de este archivo, y 12 contando las de la fase hermana.

**Casos no ejecutados y por qué:** ninguno.

---

## 2. Ejecución caso por caso

### CA-01 · CP-001 — que una cita que resuelve no se reporte

**El problema que resuelve:** un revisor que marca como roto lo que está bien enseña a ignorarlo. Ya pasó: un proyecto tenía el aviso siempre en rojo y por eso se le perdieron fallas de verdad durante media sesión.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Comprobar en disco que existe `base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md` | Existe. **Este es el resultado esperado, y no lo da el programa que se prueba** | Existe |
| 2 | Crear una carpeta temporal que haga de proyecto | La carpeta existe | `…\cimiento-enlaces-*\proyecto de prueba` |
| 3 | Escribir dentro un `cita.md` que enlace a esa regla con el marcador delante | El archivo queda escrito | Quedó |
| 4 | Correr `validar_enlaces` con la raíz apuntando a la carpeta del proyecto | No reporta el enlace | No lo reportó |
| 5 | Borrar la carpeta temporal | Queda borrada | Borrada |

**Cómo se verificó que la pareja cumple:** el paso 4 decide, pero solo no alcanza: un revisor que no reportara nunca nada pasaría igual. Por eso el CP-002 comprueba lo contrario con el mismo montaje. Y el paso 1 es el que hace que la prueba no envejezca mal: si esa regla se renombra, la prueba lo dice en vez de aprobar por casualidad.

### CA-01 · CP-002 — que lo que no resuelve se siga reportando

**El problema que resuelve:** el arreglo del CP-001 podría lograrse callando siempre. Sería peor que el defecto: un revisor mudo se lee como "todo bien".

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Comprobar en disco que **no** existe `base/02-flujo-de-trabajo/reglas/F99-esta-regla-no-existe.md` | No existe | No existe |
| 2 | Escribir un `cita.md` que enlace a esa regla inventada, con el marcador delante | El archivo queda escrito | Quedó |
| 3 | Correr `validar_enlaces` con la raíz en la carpeta del proyecto | Reporta exactamente 1 enlace roto | Reportó 1 |

**Cómo se verificó que la pareja cumple:** se exige el número exacto y no "al menos uno": si reportara dos, estaría contando algo que no es el enlace de prueba y el caso estaría pasando por el motivo equivocado.

### CA-01 · CP-003 — que la raíz que se revisa no cambie el veredicto

**El problema que resuelve:** es el defecto de la fase. El mismo archivo, con el mismo enlace, daba un veredicto distinto según desde qué carpeta se corriera el revisor.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Escribir el `cita.md` con el enlace bueno, como en el CP-001 | El archivo queda escrito | Quedó |
| 2 | Correr `validar_enlaces` con la raíz en la carpeta del proyecto | Da un veredicto | Ningún enlace roto |
| 3 | Correr `validar_enlaces` con la raíz en la carpeta de arriba, que también contiene el archivo y tampoco es el estándar | Da el mismo veredicto | Ningún enlace roto |
| 4 | Comparar los dos | Son iguales | Iguales |

**Cómo se verificó que la pareja cumple:** el paso 4 decide. Los pasos 2 y 3 usan dos carpetas que **ninguna** es el estándar: si la comparación se hiciera contra el propio estándar, las dos coincidirían por casualidad y el caso pasaría sin probar nada.

### RNF Compatibilidad · CP-004 — que la carpeta con espacios y tildes dé lo mismo

**El problema que resuelve:** el repositorio del estándar vive en `c:\Ing. Jose\ia\agente`, con espacio y con tilde. Un defecto que solo aparezca ahí no se vería hasta instalar en otra máquina.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Crear la carpeta temporal `proyecto de prueba ñ` | La carpeta existe | Existe |
| 2 | Correr los tres casos anteriores sobre ella | Dan lo mismo | Los tres dieron igual |

**Cómo se verificó que la pareja cumple:** el caso hereda la clase de los otros tres y solo le cambia el nombre de la carpeta, así que corre las mismas comprobaciones. Si el nombre influyera, alguna saldría distinta.

### La prueba no es vacía

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Cargar en memoria la versión vieja del programa —la que resolvía contra la raíz revisada— sin tocar el repositorio | El defecto queda puesto | Cargada |
| 2 | Correr el CP-003 | Se pone rojo | Rojo: reportó un enlace roto donde no lo hay |

### No regresión — que el veredicto sobre el propio estándar no cambie

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr `validar.py estandar` **antes** de tocar nada y guardar la salida | Queda el registro del antes | 8 líneas · `0 falla(s), 5 aviso(s)` |
| 2 | Hacer el cambio | — | Hecho |
| 3 | Correr `validar.py estandar` otra vez | — | 8 líneas · `0 falla(s), 5 aviso(s)` |
| 4 | Comparar las dos salidas línea por línea | Idénticas | **Idénticas** |

**Por qué el paso 1 no se puede saltar:** «acá no cambió nada» se comprueba comparando, no recordando. Sin la salida de antes, la afirmación no tiene con qué respaldarse.

**Correspondencia con el plan:** 4 casos en el plan, 4 acá.

**Qué salió distinto de lo esperado:** nada.

| Caso | CA | Prioridad | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Crítica | 2026-08-16 | `cita.md` con `«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F0-….md`, revisado con la raíz en `…\proyecto de prueba`: 0 reportes | Aprobado | EV-01 | — |
| CP-002 | CA-01 | Crítica | 2026-08-16 | El mismo montaje con `F99-esta-regla-no-existe.md`: 1 reporte, el esperado | Aprobado | EV-01 | — |
| CP-003 | CA-01 | Crítica | 2026-08-16 | La misma cita revisada desde `…\proyecto de prueba` y desde la carpeta de arriba: mismo veredicto, 0 reportes en las dos | Aprobado | EV-01 | — |
| CP-004 | RNF Compat. | Media | 2026-08-16 | Los tres casos repetidos sobre `proyecto de prueba ñ`: mismo resultado | Aprobado | EV-01 | — |

---

## 3. Verificaciones manuales  ·  [`08·T4`](«RUTA-ESTANDAR»/base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que la salida sobre el propio estándar no cambiara | Guardando `validar.py estandar` antes y comparándola después | **Idénticas**, línea por línea |
| 2 | Que la prueba se ponga roja con el defecto puesto | Cargando en memoria la versión vieja y corriendo el CP-003 | Se pone roja |

**El CP-004 no destapó lo del [punto 1 del pendiente 33](../../../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md)** —que el validador daría por rotos los enlaces con espacios—: la carpeta con espacio y tilde dio el mismo resultado que la normal. Ese punto sigue abierto, pero no se reprodujo acá.

---

## 4. Defectos encontrados

Ninguno.

**Defectos abiertos que se aceptan y por qué:** ninguno.

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| [CA-01 — Un enlace roto se reporta](../HU-005-enlaces-y-citas.md#ca-01--un-enlace-roto-se-reporta) | CP-001, CP-002, CP-003 | El que resuelve no se reporta, el que no resuelve sí, y el veredicto no depende de la carpeta desde donde se revise | **Sí** |
| No regresión | Comparación antes/después | Salida idéntica sobre el estándar | **Sí** |
| RNF — Compatibilidad | CP-004 | Mismo resultado con espacio y tilde | **Sí** |

**Los que no cumplen:** ninguno.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §5 | 100% | 3 de 3 con caso | Sí |
| Casos ejecutados | Plan §12 | 4 de 4 | 4 de 4 | Sí |
| Diferencia de la salida sobre el estándar | Plan §12 | 0 líneas | **0 líneas** | Sí |
| Corrida quirúrgica | Plan §3.5 | Solo lo de la fase | `validadores/tests/` y `validar.py estandar` | Sí |

**Lo que no se cumplió:** nada.

---

## 6. Veredicto de la fase

**Concepto:** **Cumple.**

**Justificación:** el criterio de aceptación, la no regresión y el requisito de compatibilidad quedaron verdes en la primera ejecución. El veredicto del revisor ya no depende de desde qué carpeta se lo corra, lo que no resuelve se sigue reportando, y la salida sobre el propio estándar es idéntica a la de antes del cambio.

**Qué falta para que cumpla:** nada. Queda el commit, que es estación posterior.

**Lo que esta fase no arregla, y está declarado:** `enlaces.py` sigue sin bloque `__main__`, así que correrlo directo no imprime nada y sale con código 0 — se lee como «sin hallazgos». Está fuera de alcance desde el plan y anotado en el [pendiente 41](../../../../../pendientes/41-el-marcador-no-se-resuelve-dentro-de-un-proyecto.md).

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Salida de `python -m unittest discover -s validadores/tests` | `Ran 12 tests in 1.336s · OK` (6 de esta fase, 6 de la hermana) |
| EV-02 | Salida de `validar.py estandar` antes y después | Las dos: `0 falla(s), 5 aviso(s)`, idénticas línea por línea |
| EV-03 | Corrida con el defecto reintroducido | El CP-003 se pone rojo: reporta un enlace roto donde no lo hay |

---

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-08-16 | 4 | 0 | Primera ejecución. No hubo reprueba |
