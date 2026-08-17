# Plan de Pruebas — «Fase A-EP-007-HU-006: poner al día lo ya instalado»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó al correrlas va en el `resultado_pruebas.md` de la misma fase, para no perder la línea base aprobada. La lista de tareas vive en el `plan_trabajo` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-007-HU-006 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-007-HU-006-poner-al-dia-lo-ya-instalado` |
| **Fecha** | 2026-08-16 |
| **Elaborado por** | El agente |
| **Aprobado por** | Pendiente — el usuario |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12**, como pide la plantilla por proporcionalidad.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Integración | Instalar, ensuciar o envejecer la copia, reinstalar y mirar qué quedó | Carpeta temporal | Sí |
| Aceptación | Correr el instalador en `shopnest-mesa` y abrir el enlace que reportó roto | Proyecto real | No — es un clic, y lo autoriza el usuario |

**Por qué el segundo paso siempre es reinstalar.** El defecto de las dos partes no aparece al instalar: aparece al **volver** a instalar sobre algo que ya estaba. Una prueba que solo instale en carpeta vacía pasa en verde con el código roto — que es lo que pasó en la 21.1.0.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los dos CA de la HU-006 |
| No regresión | ☑ | Que no se pise lo que llena el proyecto |
| Idempotencia | ☑ | Que reinstalar sin novedad no escriba nada |
| Rendimiento | ☐ | No aplica: se instala una vez |
| Seguridad | ☐ | No aplica: no hay usuarios ni permisos |

### 3.3 Técnicas de diseño de casos

- **Partición de equivalencia** — copia sucia (marcador crudo) contra copia limpia; versión que subió contra versión igual.
- **Valores límite** — proyecto sin ningún registro de versión; proyecto cuya única diferencia es el número de versión.
- **Triangulación** — el veredicto de la parte del registro no lo da el instalador, que es quien escribe: lo da `checklist.revisar`, que es otro programa y el que reprobaba.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)):

1. La suite nueva de esta fase (`test_instalar_reparar.py`).
2. `test_instalar_marcadores.py`, la de la fase anterior — es la que se puede romper al mover el relleno a un envoltorio.
3. Las pruebas que existan de `checklist.py` y de `versiones.py`.

**No** se corre la suite entera del repositorio.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-006 | [CA-01](../HU-006-poner-al-dia.md#ca-01--lo-viejo-se-detecta-y-se-pone-al-día) | [CP-001](#cp-001--una-copia-con-el-marcador-crudo-queda-limpia-al-reinstalar), [CP-002](#cp-002--la-plantilla-que-cambió-baja-al-proyecto), [CP-006](#cp-006--el-enlace-que-shopnest-mesa-reportó-abre-la-regla) | Funcional | Crítica | CP-001 y CP-002 sí · CP-006 no | ☐ |
| HU-006 | CA-01 · No regresión | [CP-003](#cp-003--el-hueco-que-llena-el-proyecto-sobrevive) | No regresión | Crítica | Sí | ☐ |
| HU-006 | [CA-02](../HU-006-poner-al-dia.md#ca-02--queda-registro-de-qué-se-actualizó) | [CP-004](#cp-004--sube-la-versión-sin-cambiar-plantillas-y-queda-el-registro) | Funcional | Crítica | Sí | ☐ |
| HU-006 | CA-02 · Idempotencia | [CP-005](#cp-005--reinstalar-sin-novedad-no-agrega-registro) | Idempotencia | Alta | Sí | ☐ |

**Cobertura:** 4 de 4 exigencias cubiertas = 100%.

---

## 6. Casos de prueba

### CP-001 — Una copia con el marcador crudo queda limpia al reinstalar

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-01 |
| **Tipo** | Funcional — el defecto que reportó el proyecto |
| **Prioridad** | Crítica |
| **Precondiciones** | Una carpeta temporal donde ya corrió la instalación |
| **Datos de entrada** | La misma ruta |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Instalar en una carpeta temporal vacía | Termina sin preguntar |
| 2 | Escribir `«RUTA-ESTANDAR»` a mano dentro de `.agente/stack-instalacion.md` y dentro de uno de los 4 archivos de `.agente/`, **sin tocar su sello** | Los dos archivos tienen el marcador crudo y su huella sellada sigue coincidiendo con la central |
| 3 | Volver a instalar sobre la misma carpeta | Reporta que reparó esos archivos |
| 4 | Buscar `«RUTA-ESTANDAR»` en los dos | No aparece en ninguno |
| 5 | Comprobar que en su lugar quedó la ruta del estándar | La ruta está completa |

**Resultado esperado final:** el marcador que quedó crudo se repara sin bandera y sin que cambie la plantilla.
**Postcondiciones:** la carpeta temporal se borra.

> **Este es el caso del pendiente 42.** El paso 2 reproduce exactamente el estado en que quedó `shopnest-mesa`: archivo mal escrito, sello al día.

---

### CP-002 — La plantilla que cambió baja al proyecto

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-01 |
| **Tipo** | Funcional — el camino que ya existía |
| **Prioridad** | Alta |
| **Precondiciones** | Una carpeta temporal ya instalada |
| **Datos de entrada** | Una copia del estándar en carpeta temporal, para poder editarle una plantilla sin tocar el real |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Instalar desde la copia del estándar | Termina sin preguntar |
| 2 | Cambiar una línea de `plantillas/stack-instalacion.md` en esa copia | La huella central cambia |
| 3 | Volver a instalar | Reporta el stack como viejo y lo reescribe |
| 4 | Leer el archivo instalado | Trae la línea nueva, y ningún marcador crudo |

**Resultado esperado final:** la detección por huella sigue funcionando, y lo que baja llega relleno.

> **Por qué va.** El envoltorio se agrega en el camino de «ya estaba al día». Este caso comprueba que el otro camino, el que sí funcionaba, no se rompió.

---

### CP-003 — El hueco que llena el proyecto sobrevive

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-01 · No regresión |
| **Tipo** | No regresión — es el riesgo `B-01` del plan de trabajo |
| **Prioridad** | Crítica |
| **Precondiciones** | Una carpeta temporal ya instalada |
| **Datos de entrada** | Ninguno |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Guardar el contenido de los 4 archivos de `.agente/` | Queda el registro del antes |
| 2 | Contar los huecos `«…»` que traen a propósito | Sale un número mayor que cero |
| 3 | Volver a instalar | Termina sin preguntar |
| 4 | Contar los huecos otra vez | El mismo número |
| 5 | Comparar los 4 archivos contra el registro del paso 1 | Ninguno cambió |

**Resultado esperado final:** reparar no borra lo que el estándar no sabe reponer.

> **Es la lección del `DEF-01`** de la fase anterior: los cuatro archivos de `.agente/` llegan con huecos **a propósito**, y una prueba que exija cero huecos está mal escrita, no el código.

---

### CP-004 — Sube la versión sin cambiar plantillas y queda el registro

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-02 |
| **Tipo** | Funcional — el defecto que reportó el proyecto |
| **Prioridad** | Crítica |
| **Precondiciones** | Una copia del estándar en carpeta temporal y un proyecto temporal ya instalado desde ella |
| **Datos de entrada** | Un número de versión mayor |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Instalar el proyecto temporal desde la copia del estándar | Queda un primer registro en `documentacion/versiones/` |
| 2 | Subir el `VERSION` de la copia del estándar **sin tocar ninguna plantilla** | La versión sube; ninguna huella cambia |
| 3 | Volver a instalar | Reporta que registra la actualización |
| 4 | Listar `documentacion/versiones/` | Hay un registro nuevo, con la versión nueva |
| 5 | Abrir ese registro | Dice desde cuándo el proyecto usa esa versión y que ningún componente cambió de huella |
| 6 | Correr `checklist.revisar` sobre el proyecto | El componente `versiones` cumple, y no queda ningún faltante |
| 7 | Correr el instalador sobre la carpeta del propio estándar | **No** le escribe ningún registro |

**Resultado esperado final:** el proyecto llega a completo corriendo el instalador, sin que nadie edite nada a mano.

> **Este es el caso del pendiente 44.** El paso 6 es el veredicto de verdad, y lo da `checklist`, que es el programa que reprobaba. El paso 7 cubre el riesgo `B-03`.

---

### CP-005 — Reinstalar sin novedad no agrega registro

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-02 · Idempotencia |
| **Tipo** | Idempotencia |
| **Prioridad** | Alta |
| **Precondiciones** | El CP-004 pasó y la carpeta temporal no se borró |
| **Datos de entrada** | La misma ruta, la misma versión |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Contar los registros de `documentacion/versiones/` | Sale un número |
| 2 | Volver a instalar sin cambiar nada | Reporta que no hay actualización que registrar |
| 3 | Contar otra vez | El mismo número |

**Resultado esperado final:** sin cambio de versión ni de huella, la carpeta no crece.

> **Es el límite de la decisión del 44.** Lo pide el paso 3 del CA-02 de la HU: «actualizar otra vez sin cambios → no se agrega una entrada vacía». Lo que cambió es qué cuenta como cambio: ahora subir de versión cuenta.

---

### CP-006 — El enlace que `shopnest-mesa` reportó abre la regla

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-01 |
| **Tipo** | Aceptación — verificación manual sobre el proyecto de origen |
| **Prioridad** | Crítica |
| **Precondiciones** | Los cinco casos anteriores pasaron. **El usuario autoriza correr el instalador sobre `shopnest-mesa`** |
| **Datos de entrada** | `C:/DesarrollosClaude/personales/shopnest-mesa` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr el instalador sobre `shopnest-mesa` | Reporta que reparó el stack y que registró la actualización |
| 2 | Abrir la línea 25 de su `.agente/stack-instalacion.md` | La cita a `02·F13` trae una ruta real, no `«RUTA-ESTANDAR»` |
| 3 | Hacer clic en esa cita | Abre el archivo de la regla |
| 4 | Mirar el arranque de sesión de ese proyecto | Ya no aparece «INSTALACIÓN INCOMPLETA · 12 de 13» |

**Resultado esperado final:** los dos reportes que hizo el proyecto quedan cerrados en el proyecto que los hizo.

> **Por qué va a mano y sobre lo real.** Es el único paso que prueba que el defecto reportado desapareció donde se reportó. Corre **una vez**, al final, y sobre un proyecto que está en git — lo que escriba se puede revisar y revertir.

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Reparar borra un hueco que llenaba el proyecto | Inmediato — se detiene la fase |
| **Crítica** | Después del cambio, la copia sucia sigue sucia al reinstalar | Inmediato |
| **Alta** | El registro se escribe también sin cambio de versión | Antes de cerrar |
| **Media** | El propio estándar se escribe registros | Antes de cerrar |
| **Baja** | La salida no dice qué archivo se reparó | Se anota como deuda |

### 9.2 Qué se hace con un defecto

Se diagnostica, se corrige y se vuelve a correr el caso. El ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior ([`02·F15`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F15-no-saltes-ni-reordenes-las-once-etapas-de-la-fase.md), etapa 7).

Si el defecto resulta ser del **plan** y no del código —como pasó en la fase anterior con el `DEF-01`— se para, se reporta y lo corrige el usuario. El agente no reescribe el criterio que le está fallando.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — las 4 con caso |
| Casos ejecutados | 6 de 6 |
| Archivos reparados que conservan un marcador conocido | **0** |
| Huecos del proyecto perdidos al reparar | **0** |
| Proyecto de origen en «13 de 13» | Sí |

El veredicto de cada caso y el concepto final **no van acá**: van en el `resultado_pruebas.md` de esta fase. Este plan dice qué se va a medir; aquel dirá cuánto dio.
