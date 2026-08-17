# Resultado de Pruebas — Fase «A-EP-007-HU-006-poner-al-dia-lo-ya-instalado»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el `estado-fase.md` para pasar la puerta de verificación, y la fuente de la sección "qué se probó" del `funcionalidad_implementada.md`. El diseño de los casos vive en el [`plan_pruebas.md`](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar: se aprobó antes y así se queda.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-007-HU-006-poner-al-dia-lo-ya-instalado` |
| **HU** | [HU-006 — Poner al día lo ya instalado](../HU-006-poner-al-dia.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 2 |
| **Fecha de ejecución** | 2026-08-16 |
| **Ejecutado por** | El agente |
| **Ambiente y versión** | Windows 11 · Python 3.11 · estándar 21.1.1 → 21.2.0 · carpetas temporales desechables |

**Con qué se corre:**

```
python -m unittest discover -s validadores/tests
```

---

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 6 | 5 | 3 | 2 | 0 | 1 |
| 2 | 6 | 6 | 6 | 0 | 0 | 0 |

`unittest` reporta **6 pruebas** para 5 casos automáticos: el CP-004 se parte en dos, porque su paso 7 —que el propio estándar no se escriba registros— se comprueba llamando directo a `registrar_version` y no vale la pena instalar un proyecto entero para eso.

**Casos no ejecutados y por qué:** ninguno. El **CP-006** lo ejecutó `shopnest-mesa` por su cuenta al correr el instalador con la v21.2.0, y desde acá se verificó leyendo sus archivos, sin escribir nada en su proyecto.

---

## 2. Ejecución caso por caso

### CA-01 · CP-001 — una copia con el marcador crudo queda limpia al reinstalar

**El problema que resuelve:** un proyecto instalado antes de la 21.1.0 tiene la copia mal escrita y el sello al día. El instalador miraba solo el sello, decía «ya estaba al día» y no abría el archivo. Es lo que reportó `shopnest-mesa`.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Instalar en una carpeta temporal vacía | Termina sin preguntar | «Instalación del agente completa — 13 de 13» |
| 2 | Cambiar la ruta del estándar por `«RUTA-ESTANDAR»` en el stack y en el archivo de `.agente/` que la cita, **sin tocar el sello** | Los dos quedan con el marcador crudo y su huella sigue coincidiendo | Ensuciados `.agente/stack-instalacion.md` y `.agente/mapeo-nombres.md` |
| 3 | Volver a instalar | Reporta que los reparó | «rellenar los marcadores que quedaron crudos en …» por cada uno |
| 4 | Buscar el marcador en los dos | No aparece | No aparece |
| 5 | Comprobar que quedó la ruta del estándar | Está completa | Está |

**Cómo se verificó que cumple:** el paso 4 es el que decide, y lo comprueba leyendo el archivo escrito — no preguntándole al instalador qué cree que hizo.

**Cuál de los cuatro archivos de `.agente/` se ensucia no está clavado en la prueba:** se busca el que cite al estándar. Clavar un nombre haría que la prueba dejara de probar el día que ese archivo cambie.

**Veredicto:** ✅ Cumple.

---

### CA-01 · CP-002 — la plantilla que cambió baja al proyecto

**El problema que resuelve:** la reparación se agrega en la rama de «ya estaba al día». Este caso comprueba que la otra rama —la huella distinta, que es la que sí funcionaba— no se rompió.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Instalar desde la copia desechable del estándar | Termina sin preguntar | Completa |
| 2 | Agregar una línea a `plantillas/stack-instalacion.md` de esa copia | La huella central cambia | Cambió |
| 3 | Volver a instalar | Reporta el stack como viejo y lo reescribe | «copiar .agente/stack-instalacion.md» |
| 4 | Leer el archivo instalado | Trae la línea nueva y ningún marcador crudo | Las dos cosas |

**Veredicto:** ✅ Cumple.

---

### CA-01 · CP-003 — el hueco que llena el proyecto sobrevive

**El problema que resuelve:** es el riesgo `B-01` del plan, y la lección del `DEF-01` de la fase anterior. Los 4 archivos de `.agente/` llegan con huecos **a propósito**: son las preguntas que solo el proyecto puede responder. Si la reparación rellenara de más, borraría lo único que el estándar no sabe reponer.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Guardar el contenido de los 4 archivos | Queda el registro del antes | Guardado |
| 2 | Contar sus huecos | Mayor que cero | Mayor que cero, o el caso no probaría nada |
| 3 | Volver a instalar | Termina sin preguntar | Completa |
| 4 | Contar los huecos otra vez | El mismo número | El mismo |
| 5 | Comparar los 4 contra el registro del paso 1 | Ninguno cambió | Ninguno |

**Cómo se verificó que cumple:** el paso 2 tiene su propia comprobación —que el número sea mayor que cero— porque una prueba que compara cero contra cero pasa siempre y no prueba nada.

**Veredicto:** ✅ Cumple.

---

### CA-02 · CP-004 — sube la versión sin cambiar plantillas y queda el registro

**El problema que resuelve:** el instalador decía «nada que registrar» y la revisión decía «falta el registro». `shopnest-mesa` quedó en 12 de 13 con el aviso sonando en cada mensaje, y el desfase creció solo: usaba la `21.1.1` y su último registro decía `20.0.1`.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Instalar el proyecto temporal | Queda un primer registro | Quedó |
| 2 | Subir el `VERSION` de la copia del estándar a `99.0.0`, sin tocar ningún molde | La versión sube, ninguna huella cambia | Subió |
| 3 | Volver a instalar | Reporta que registra la actualización | «registrar documentacion\versiones\…-99.0.0.md» |
| 4 | Listar la carpeta de registros | Hay uno nuevo, con la versión nueva | Uno más, `99.0.0` |
| 5 | Abrir ese registro | Dice desde cuándo y que ningún componente cambió de huella | «Ninguno cambió de huella: solo se refrescó la instalación» |
| 6 | Correr la revisión sobre el proyecto | El componente `versiones` cumple y no queda ningún faltante | Sin faltantes |
| 7 | Llamar a `registrar_version` sobre la carpeta del propio estándar | No escribe nada | Devolvió vacío y no creó carpeta |

**Cómo se verificó que cumple:** el veredicto lo da el paso 6, y lo da `checklist` — que es **otro programa**, y justamente el que reprobaba. Si lo diera el instalador, sería el mismo que escribe diciendo que escribió bien.

**Veredicto:** ✅ Cumple. El paso 7 cierra el riesgo `B-03`.

---

### CA-02 · CP-005 — reinstalar sin novedad no agrega registro

**El problema que resuelve:** es el límite de la decisión. Lo pide el paso 3 del CA-02 de la HU: sin cambios no se agrega una entrada vacía. Lo que cambió es qué cuenta como cambio.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Contar los registros | Sale un número | Uno |
| 2 | Volver a instalar sin cambiar nada | Reporta que no hay actualización que registrar | «versiones: ni las plantillas ni la versión cambiaron, no hay actualización que registrar» |
| 3 | Contar otra vez | El mismo número | Uno |

**Veredicto:** ✅ Cumple.

---

### CA-01 · CP-006 — el enlace que `shopnest-mesa` reportó abre la regla

**Lo ejecutó el proyecto de origen, no esta casa.** `shopnest-mesa` corrió el instalador con la v21.2.0 por su cuenta, antes de que llegara el aviso, y dejó su comprobación escrita en sus pendientes `01` y `06`. Vale más que la corrida de acá: **el que reportó el defecto es el que dice si desapareció**, y nadie de este lado tocó su proyecto.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr el instalador sobre `shopnest-mesa` | Repara el stack y registra la actualización | «registrar documentacion\versiones\2026-08-16-21.2.0.md» |
| 2 | Abrir la línea 25 de su `.agente/stack-instalacion.md` | Ruta real, no `«RUTA-ESTANDAR»` | `C:/Ing. Jose/ia/agente/base/02-flujo-de-trabajo/reglas/F13-…` |
| 3 | Hacer clic en esa cita | Abre el archivo de la regla | Abre |
| 4 | Mirar el arranque de sesión | Ya no aparece «12 de 13» | «Instalación del agente completa · shopnest-mesa · 13 de 13» |

**Verificado además desde acá el 2026-08-16**, leyendo sus archivos sin escribir nada: la línea 25 lleva la ruta real, `documentacion/versiones/2026-08-16-21.2.0.md` existe, y no queda ningún marcador crudo en su `.agente/` ni en su `CLAUDE.md`.

**Veredicto:** ✅ Cumple.

> **Lo que el proyecto entendió mal, y se le corrigió al avisarle.** Concluyó que el 42 había cerrado «de rebote» —porque la plantilla del stack cambió de huella en la misma versión— y que *«un proyecto ya instalado solo se repara si la plantilla cambia de huella»*. No es así: `_reparar_marcadores` repara sin que cambie ninguna huella, y el CP-001 lo comprueba ensuciando una copia **sin tocar su sello**. El cambio de huella de la plantilla fue efecto lateral, declarado como tal en el §2.6 del plan.

---

## 3. Defectos encontrados

| ID | Caso | Qué pasó | De quién era | Estado |
|---|---|---|---|---|
| DEF-01 | CP-001 | El caso no lograba ensuciar el archivo: se había elegido el primero de los 4 de `.agente/`, y ese —`stack.md`— no cita al estándar, así que no había nada que reemplazar | De la prueba | Corregido: se busca el archivo que sí lo cita, en vez de clavar un nombre |
| DEF-02 | CP-004 | `UnicodeEncodeError` al imprimir la flecha `→` del paso de sellado | Del arranque de la prueba | Corregido: la prueba llama a `preparar_salida()`, que es lo que hace `main()` antes de correr |

**Ninguno de los dos era del cambio de esta fase.** El `DEF-01` era del caso mal diseñado y el `DEF-02` de llamar al instalador como biblioteca sin prepararle la salida. Los dos se corrigieron y se volvió a correr entero: ciclo 2, todo en verde.

**El `DEF-02` deja una pregunta abierta** que no se resuelve acá: `instalar()` revienta al imprimir si nadie llamó antes a `preparar_salida()`. Hoy solo lo llama `main()`. Queda reportado al usuario ([`02·F20`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md)).

---

## 4. Lo que se descubrió fuera del criterio

Dos cosas que no son de esta fase y no se tocaron ([`02·F20`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md), [`02·F8`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)):

1. **`plantillas/proyectos.md` tenía 99 filas de proyectos de prueba** que dejó `test_instalar_marcadores.py`, todas apuntando a carpetas temporales que ya no existen — nueve reales contra noventa y nueve muertas. El archivo está en el `.gitignore`, así que no llegó a git, pero es el registro único de proyectos: `instalar.py --todos` lo recorre entero, y la cuenta subía seis por corrida de la suite.

   **Se reportó y el usuario amplió el plan** ([`02·F8`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)): «solo deben estar los que son reales, no los de pruebas». Se hicieron las dos mitades, porque limpiar sin tapar la fuente es volver a limpiar la semana que viene ([`02·F21`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F21-un-incumplimiento-ya-identificado-no-se-repite-en-lo-nuevo.md)):

   - Se quitaron las 99 filas muertas. Quedan los 9 proyectos reales.
   - `test_instalar_marcadores.py` apunta el registro a una copia desechable, igual que la suite de esta fase. Comprobado: se corrieron las 18 pruebas y el registro quedó con 0 filas de prueba.

   Es lo que pide [`08·T4`](«RUTA-ESTANDAR»/base/08-pruebas.md#t4--protege-los-datos-reales-al-probar), así que el arreglo devuelve el código a lo que la regla ya exigía.
2. **La revisión de una instalación completa dice «13 de 13»** aunque el propio estándar no se mida con esa vara. No es defecto; se anota porque el número aparece en la salida de todos los casos.

---

## 5. Cobertura contra el plan de pruebas

| Exigencia | Caso | Estado |
|---|---|---|
| CA-01 — lo viejo se detecta y se pone al día | CP-001, CP-002, CP-006 | ✅ |
| CA-01 · no regresión — el hueco del proyecto sobrevive | CP-003 | ✅ |
| CA-02 — queda registro de qué se actualizó | CP-004 | ✅ |
| CA-02 · idempotencia — sin novedad no se registra | CP-005 | ✅ |

**Cobertura:** 4 de 4 exigencias con caso ejecutado = 100%.

---

## 6. Veredicto de la fase

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 2 de 2 (CA-01 y CA-02) |
| **CA en "No"** | ninguno |
| **Defectos abiertos aceptados** | ninguno. El `DEF-01` y el `DEF-02` eran de la prueba y quedaron corregidos |
| **Qué falta** | nada de pruebas. Queda el commit, que autoriza el usuario |

---

## 7. Métricas contra la meta del plan

| Métrica | Meta | Dio |
|---|---|---|
| Cobertura de exigencias | 100% | 100% |
| Casos ejecutados | 6 de 6 | 6 de 6 |
| Archivos reparados que conservan un marcador conocido | 0 | 0 |
| Huecos del proyecto perdidos al reparar | 0 | 0 |
| Proyecto de origen en «13 de 13» | Sí | Sí, comprobado por el propio proyecto |
