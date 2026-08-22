# Funcionalidad implementada — Fase C-EP-003-HU-002-el-planteamiento-se-reconstruye-igual   ·   `[CAPA 3]`

**Para qué sirve este documento.** Es el cierre de la fase: **qué quedó hecho, qué se probó, qué se decidió y qué deuda quedó**. El plan dice lo que se iba a hacer; esto dice lo que pasó, para poder comparar los dos.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `C-EP-003-HU-002-el-planteamiento-se-reconstruye-igual` |
| **Épica / HU** | [EP-003](../../epica.md) · [HU-002](../HU-002-modelos-del-encargo.md) |
| **CA que cierra** | [CA-04](../HU-002-modelos-del-encargo.md#ca-04--el-modelo-de-la-necesidad-sirve-igual-para-un-proyecto-que-empieza-y-para-uno-que-ya-existe) |
| **Fecha de cierre** | 2026-08-22 |
| **Veredicto** | [Cumple](resultado_pruebas.md#6-veredicto-de-la-fase) |

---

## 1. Qué se implementó — resumen

El molde del planteamiento sirve ahora para un proyecto que empieza y para uno que ya está construido, sin partirse en dos. Gana el campo «Cómo se levantó», las instrucciones para reconstruir con su tabla de traducción, la advertencia de que reconstruir es auditar, y la declaración de que el encuadre es texto fijo. Y el encuadre dejó de copiar la cadena de `02·F0`: la enlaza.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Exigencia | Dónde quedó | Prueba | Evidencia |
|---|---|---|---|
| [CA-04](../HU-002-modelos-del-encargo.md#ca-04--el-modelo-de-la-necesidad-sirve-igual-para-un-proyecto-que-empieza-y-para-uno-que-ya-existe) | El recuadro de instrucciones y §0 del molde | CP-001, CP-002, CP-004 | [resultado_pruebas.md](resultado_pruebas.md) §2 |
| RN-06 | Un solo `01-planteamiento.md` | CP-005 | Ídem |
| RN-07 | «Borrar este recuadro. **Solo este recuadro**» | CP-004 | Ídem |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué decía el plan | Qué se hizo |
|---|---|---|
| T-01 | Campo «Cómo se levantó» | Hecho |
| T-02 | Apartado del proyecto ya construido | Hecho, con las fuentes nombradas |
| T-03 | Tabla de traducción con las cuatro conversiones | Hecho |
| T-04 | La advertencia de auditoría | Hecho |
| T-05 | El encuadre declarado texto fijo | Hecho |
| T-05b | **No estaba en el plan aprobado.** El encuadre enlaza `02·F0` en vez de copiarle la cadena | Hecho. Se agregó al plan antes de ejecutarla, con su análisis en §2 punto 5 |
| T-06 | Correr el plan de pruebas | Hecho. Cinco casos en verde y uno que no se pudo correr |
| T-07 | `CHANGELOG` y `VERSION` | Hecho, sobre `31.13.0` |

**Archivos tocados fuera de los declarados:** [`validadores/plantillas.py`](../../../../../validadores/plantillas.py) y su archivo de pruebas, por el defecto D-01. Se anota por [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md): no estaban en §2.1 y se editaron.

---

## 3. Qué se probó  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Los seis casos del plan, más la corrida del planteamiento reconstruido contra el molde corregido, más las once pruebas del archivo del encuadre y las tres del origen de las reglas de negocio. El recuento de marcas quedó igual, en 126.

---

## 4. Cómo se usa / puntos de entrada

El molde se copia como `prompts/<slug>-planteamiento.md`. Desde esta fase, ese nombre **sí** lo reconoce el validador:

```
python validadores/validar.py plantilla prompts/<slug>-planteamiento.md
```

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md)

**Un solo molde, no dos.** Dos moldes divergen: se corrige uno y el otro queda viejo. Y el resultado tiene que ser el mismo documento en los dos casos, así que partir el molde sugiere lo contrario de lo que se quiere.

**La procedencia va en un campo, no en un párrafo.** Ya se probó el párrafo, y fue exactamente lo que desplazó al encuadre en el planteamiento de este repositorio. Un campo tiene un solo lugar y no compite con nada.

**Reconstruir es auditar, y hubo que escribirlo.** Sin esa frase, el molde se vuelve una máquina de justificar hacia atrás cualquier cosa que ya esté en el disco: lo construido que no cabe en el alcance termina metido en el alcance para que quepa.

**El encuadre enlaza en vez de copiar.** La copia se desactualizó sin que nadie lo notara: decía «análisis → alcance → épica/HU» y `02·F0` dice «planteamiento → épica → HU». Dos versiones de la misma cadena en el mismo repositorio, y la que se lee primero era la equivocada.

**Y una que se decidió midiendo.** Al arreglar D-01, la primera versión aceptaba el sufijo del nombre en cualquier carpeta y para todas las claves. Antes de dejarla se midió: resolvía mal 29 documentos, tomando cada `resultado_pruebas.md` por un plan de pruebas y cada regla terminada en `-trabajo` por un plan de trabajo. Se acotó al planteamiento dentro de `prompts/`, que es lo que el molde nombra.

---

## 6. Deuda técnica y pendientes generados

| Qué queda | Dónde |
|---|---|
| El CP-003, la prueba con un lector que no participó, sigue sin correrse | D-03 de [resultado_pruebas.md](resultado_pruebas.md) |
| `resultado_pruebas.md` no tiene entrada en la tabla de nombres del validador, aunque tiene su propio molde | D-04, ídem. Corregirlo abre una comprobación sobre veinte documentos |
| Los otros dos modelos del encargo, la épica y la historia, no contemplan el caso del proyecto ya construido | Declarado fuera de alcance en el plan §1 |

---

## 7. Índices y mapas actualizados

- [HU-002](../HU-002-modelos-del-encargo.md): CA-04, RN-06, RN-07 y la fila de esta fase.
- El [pendiente 56](../../../../../pendientes/hecho/el-estandar-tiene-su-planteamiento.md) no se toca: cerró con el planteamiento escrito, y lo de esta fase es el molde.

---

## 8. Despliegue — si aplica

No aplica. El molde viaja con el instalador, y los planteamientos ya escritos siguen valiendo: les faltará el campo «Cómo se levantó», que se llena la próxima vez que se toquen.
