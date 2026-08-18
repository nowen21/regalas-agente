# Plan de Pruebas — Fase A-EP-004-HU-002-retrodocumentar-la-clasificacion-de-cada-regla   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-004-HU-002 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-004-HU-002-retrodocumentar-la-clasificacion-de-cada-regla` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/planes/pruebas.md)).

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Unitario | Que toda regla de `base/` esté en el registro y que el registro no nombre reglas inexistentes | Lectura de `base/` | Sí — entra a `validadores/pruebas.py` |
| Caso borde | Que un rango escrito como «C1–C17» no cuente como diecisiete reglas clasificadas | Lectura | Sí |
| Trazabilidad | Que desde el registro se llegue al programa que comprueba cada regla | Este repositorio | No |
| Conducta | Qué avisa hoy una regla nueva sin clasificar | Copia del repositorio | No |

**Por qué la prueba va en `pruebas.py`.** El programa que vigilaría la fila 18 no tiene punto de entrada (pendiente [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md)). Arreglarlo es otro archivo y otro problema; una comprobación que no corre no comprueba nada.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los tres CA |
| Límites | ☑ | El rango, que fue un diagnóstico falso y costó una sesión |
| Negativa | ☑ | El CA-03: hoy nada frena una regla sin clasificar |
| No regresión | ☑ | La suite que ya existe, contra su número anotado antes |

### 3.3 Técnicas de diseño de casos

- **El caso del rango, escrito como prueba** — «C1–C17» en el registro no clasifica diecisiete reglas. Ese error ya produjo un diagnóstico falso que costó una sesión. La prueba existe para que no vuelva, no porque se sospeche que está.
- **Cruce en los dos sentidos** — regla sin entrada en el registro, y entrada del registro que nombra una regla que no existe. Con un solo sentido, el registro podría envejecer sin que nadie lo note.
- **La prueba que espera fallar** — el CP-004 del CA-03 se escribe sabiendo que hoy **nada frena** una regla sin clasificar. El resultado esperado es ese, y sirve de evidencia.
- **Distinguir el hueco de la clasificación correcta** — el riesgo `R-02`: la tabla regla → programa separa «no la comprueba nadie **porque es humana**» de «debería y no está». Sin esa distinción, la tabla se lee como llena de agujeros.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/pruebas.py` entera y `validar.py estandar` como línea base.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-002 | [CA-01](../HU-002-marca-de-comprobable-en-cada-regla.md#ca-01--toda-regla-aparece-clasificada) | [CP-001](#cp-001--toda-regla-está-en-el-registro-y-el-registro-no-inventa-reglas), [CP-002](#cp-002--un-rango-no-clasifica-las-reglas-que-abarca) | Límites | Crítica | Sí | ☐ |
| HU-002 | [CA-02](../HU-002-marca-de-comprobable-en-cada-regla.md#ca-02--la-regla-comprobada-dice-quién-la-comprueba) | [CP-003](#cp-003--desde-el-registro-se-llega-al-programa-que-comprueba-la-regla) | Trazabilidad | Alta | No | ☐ |
| HU-002 | [CA-03](../HU-002-marca-de-comprobable-en-cada-regla.md#ca-03--una-regla-nueva-no-se-publica-sin-clasificar) | [CP-004](#cp-004--hoy-nada-frena-una-regla-nueva-sin-clasificar) | Negativa | Alta | No | ☐ |
| HU-002 | RNF — que la clasificación se pueda revisar de una corrida | [CP-001](#cp-001--toda-regla-está-en-el-registro-y-el-registro-no-inventa-reglas) | Funcional | Media | Sí | ☐ |

**Cobertura:** 3 de 3 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — Toda regla está en el registro, y el registro no inventa reglas

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-01 y RNF |
| **Tipo** | Funcional |
| **Prioridad** | Crítica |
| **Precondiciones** | El número de pruebas de la suite anotado antes de tocarla |
| **Datos de entrada** | Las reglas de `base/` y el registro [`reglas-validables.md`](../../../../../validadores/reglas-validables.md) |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Recoger los identificadores de todas las reglas de `base/` | Queda la lista, con su número y la fecha |
| 2 | Recoger los identificadores del registro | Queda la lista |
| 3 | Comprobar que toda regla está en el registro | Ninguna sin clasificar |
| 4 | Comprobar que el registro no nombra reglas que no existen | Ninguna sobrante |
| 5 | Listar las que falten en cualquiera de los dos sentidos | Se anotan; clasificarlas es de otra fase |

**Resultado esperado final:** la clasificación se revisa de una corrida, y en los dos sentidos.

---

### CP-002 — Un rango no clasifica las reglas que abarca

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-01 |
| **Tipo** | Límites |
| **Prioridad** | Crítica |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | Una entrada de registro escrita como rango, del estilo «C1–C17» |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir en copia una entrada con forma de rango | Queda escrita |
| 2 | Correr la comprobación del CP-001 sobre esa copia | Las reglas del rango **siguen** contando como sin clasificar |
| 3 | Escribirlas una por una y volver a correr | Ahora sí cuentan |
| 4 | Comprobar que el registro real no tiene rangos | O queda anotado cuáles |

**Resultado esperado final:** un rango no vale como clasificación, y la prueba lo sostiene.

> **Este caso existe porque el error ya pasó.** Un rango leído como diecisiete clasificaciones produjo un diagnóstico falso que costó una sesión.

---

### CP-003 — Desde el registro se llega al programa que comprueba la regla

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-02 |
| **Tipo** | Trazabilidad |
| **Prioridad** | Alta |
| **Precondiciones** | La tabla regla → programa levantada (T-03) |
| **Datos de entrada** | Tres reglas validables, y los subcomandos que existen |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Listar los subcomandos disponibles | Queda el listado, con su número |
| 2 | Por cada una de las tres reglas, buscar en el registro qué programa la comprueba | Se llega al programa **leyendo solo el registro** |
| 3 | Correr ese programa y comprobar que efectivamente la mira | La mira |
| 4 | Marcar en la tabla las reglas que no comprueba nadie | Distinguiendo «es humana» de «debería y no está» |
| 5 | Comprobar que la columna quedó en el registro y no en un documento nuevo | En el registro |

**Resultado esperado final:** el CA-02 deja de resolverse deduciendo de `validadores/docs/`.

> **El paso 4 es el que hace útil la tabla.** Sin la distinción, una casilla vacía se lee como un hueco cuando muchas veces es la clasificación correcta.

---

### CP-004 — Hoy nada frena una regla nueva sin clasificar

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-03 |
| **Tipo** | Negativa — estado del arte |
| **Prioridad** | Alta |
| **Precondiciones** | Una copia del repositorio. **No se edita el repositorio vivo** |
| **Datos de entrada** | Una regla de mentira escrita en la copia, sin entrada en el registro |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir la regla en la copia, sin clasificarla | Queda escrita |
| 2 | Correr las comprobaciones disponibles | Se anota cuál avisa y cuál no |
| 3 | Intentar correr el programa de la fila 18 | No tiene punto de entrada; queda la evidencia |
| 4 | Dejar escrito que la vigilancia depende de ese programa | Atado al pendiente [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md) |
| 5 | Borrar la copia | No queda rastro |

**Resultado esperado final:** el CA-03 queda en «No» con la evidencia de por qué, que es lo que la fase que lo arregle necesita.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que un rango cuente como clasificación | Inmediato — es el error que ya produjo un diagnóstico falso |
| **Alta** | Que aparezcan reglas sin clasificar otra vez (riesgo `R-01`) | Se listan y se anotan. Clasificarlas es de la fase de [EP-001 · HU-009](../../../EP-001-cuerpo-de-reglas-heredable/HU-009-reglas-sin-checklist-al-dia/A-EP-001-HU-009-clasificar-las-que-faltan/README.md) |
| **Media** | Que la tabla regla → programa quede con casillas vacías sin explicar (riesgo `R-02`) | Se distingue «es humana» de «debería y no está» |
| **Media** | Que el registro nombre reglas que no existen | Se anota; el registro se corrige en la fase que corresponda |
| **Baja** | Que otra sesión esté tocando `validadores/pruebas.py` | Se guarda solo lo propio |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 3 CA y los RNF con caso |
| Casos ejecutados | 4 de 4 |
| Reglas sin clasificar | **0**, o todas listadas |
| Entradas del registro que nombran reglas inexistentes | **0**, o todas listadas |
| Rangos en el registro | **0**, o todos anotados |
| Reglas validables sin programa identificado | Todas anotadas, distinguiendo el hueco de la clasificación correcta |
| Pruebas de la suite | Las de la línea base, más 2, todas en verde |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
