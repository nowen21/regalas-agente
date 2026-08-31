# Plan de Trabajo — Fase «B-EP-011-HU-002-lo-generico-no-encabeza-el-reporte» (módulo «Medición»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas` de esta misma fase; lo que quedó hecho, en el `funcionalidad_implementada.md` del cierre.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-011-HU-002-lo-generico-no-encabeza-el-reporte` |
| **Épica** | [documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/epica.md](../../epica.md) |
| **HU** | [documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-002-ver-que-correccion-se-repite/HU-002-ver-que-correccion-se-repite.md](../HU-002-ver-que-correccion-se-repite.md) — **una sola** (`F12.1`) |
| **Módulo** | Medición |
| **Especificación del módulo** | [documentacion/medicion/spec.md](../../../../medicion/spec.md) |
| **Fecha apertura** | 2026-08-31 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- 📝 **Modifica fase(s):** retoma el `CA-01` de la fase `A`. Aquella lo dejó cumplido —el reporte sale ordenado— y al leerlo con el usuario apareció el **riesgo 2** que la propia HU advertía: *que el reporte diga lo obvio*. De las diez primeras filas no nacía ninguna regla.

**CA de la HU que cubre esta fase:**

| CA de `HU-002` que cierra esta fase | Estado |
|---|---|
| [CA-01 — El reporte sale por período](../HU-002-ver-que-correccion-se-repite.md#ca-01--el-reporte-sale-por-período) | ☐ |
| Riesgo 2 de la §9 — que el reporte no diga lo obvio | ☐ |

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** que arriba del reporte queden correcciones de verdad, y no la forma en que el usuario redacta cualquier exigencia.

**Lo que se midió antes de decidir**, y por qué la primera propuesta se descartó:

| Qué se probó | Qué salió |
|---|---|
| Ordenar por **sesiones distintas** en vez de por veces | «debe quedar» sigue de primero, con 14 sesiones. **No sirve** |
| Pesar cada frase por lo **raras** que son sus palabras | Arriba quedan términos técnicos que solo aparecen juntos. **Se pasa al otro lado** |
| **Descartar las frases hechas con las palabras más comunes del propio corpus** | Arriba quedan «estoy preguntando», «español colombiano», «aplicando id9». **Sirve** |

**La primera se propuso, se aprobó y se midió antes de construirla.** No funcionó, y eso está escrito acá en vez de entregarse igual.

**Resumen de lo que se cubre:**

| Qué | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Lo genérico no encabeza; primero lo que aparece en más días | Funcional | Media |
| Riesgo 2 | De las primeras filas nace algo | **De juicio** | Alta |

**Fuera de alcance:**

- Pantalla.
- Decidir la regla que el patrón sugiera: eso entra por la cadena.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**El reporte de hoy, tal como sale:**

```
 22  debe quedar        14 sesiones
 21  meta reglas         5 sesiones
 19  puede cerrar       13 sesiones
 19  historico chat     10 sesiones
 17  debe tener         11 sesiones
```

Tres de las cinco primeras —«debe quedar», «puede cerrar», «debe tener»— no son correcciones.

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `plataforma/nucleo/medicion/repeticion.py` | Modificar | Servicio | El vocabulario de la casa, las rutas pegadas, y el orden |
| `plataforma/nucleo/medicion/tests_repeticion.py` | Modificar | Prueba | Nueve casos nuevos, y las mentiras repartidas en días distintos |

### 2.2 Matriz de dependencias del refactor

| Archivo | Cambio de contrato | Depende | Dónde rompe |
|---|---|---|---|
| `correcciones` | Un parámetro más, opcional, y **criterio nuevo**: lo repetido en un solo día ya no cuenta | `correcciones_que_se_repiten` | No rompe: el reporte llama igual |

### 2.3 Rutas · 2.4 UI · 2.5 Permisos

No aplican.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **El vocabulario de la casa se calcula sobre lo que hay** | Escribir a mano una lista con «debe», «archivo», «carpeta» | Una lista a mano acierta en las palabras que uno se imagina y envejece con el proyecto: el día que el trabajo cambie de tema, deja pasar el vocabulario nuevo y sigue tapando el viejo (`S-091`) |
| Una palabra en más del **cuarto** de las sesiones es vocabulario | Un número absoluto | Un absoluto no sirve a la vez para un proyecto de diez sesiones y para uno de mil |
| **Con pocas sesiones no se filtra**, y se dice | Filtrar siempre | Sobre tres conversaciones cualquier palabra dicha dos veces pasa el umbral, y el reporte saldría vacío — que se lee como «no hubo nada» |
| **Repetir en un solo día no cuenta** | Contar todas las repeticiones | Tres veces el mismo día es insistir en una conversación; tres días distintos es una regla que falta |
| **Una ruta pegada no es una frase** | Contarla | «ing jose» encabezaba con doce sesiones, y sale del nombre de una carpeta pegada en el mensaje. Es el mismo caso que lo que agrega el editor |
| El orden es por **días distintos** primero | Por veces | Es lo que el usuario aprobó, y solo sirve **junto con** el filtro: por sí solo no movía nada |

### 2.7 Dudas por resolver antes de codificar

Ninguna abierta. La decisión del usuario fue *«hágalo»* sobre la mejora del reporte; el mecanismo se midió antes de escribirlo.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-00 | Medir las tres formas de ordenar, antes de elegir | Medición | 2 h | — | EV-02 |
| T-01 | `vocabulario_de_la_casa`, calculada sobre el corpus | Servicio | 2 h | T-00 | EV-01 |
| T-02 | Descartar la frase que use una de esas palabras | Servicio | 1 h | T-01 | EV-01 |
| T-03 | Las rutas pegadas no cuentan | Servicio | 1 h | — | EV-01 |
| T-04 | Mínimo de sesiones distintas, y el orden nuevo | Servicio | 1 h | T-02 | EV-01 |
| T-05 | El resguardo de corpus chico | Servicio | 1 h | T-01 | EV-01 |
| T-06 | Nueve pruebas, y las de la fase A repartidas en días | Test | 3 h | T-04 | EV-01 |
| T-07 | Correrlo sobre lo real y dejar el reporte escrito | Medición | 1 h | T-04 | EV-02 |

**Total estimado:** 12 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-00 → T-01 → T-02 → T-04 → T-07.

---

## 5. Verificación  ·  Q10

| Qué | Método | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| [CA-01](../HU-002-ver-que-correccion-se-repite.md#ca-01--el-reporte-sale-por-período) | El reporte sobre lo real, antes y después | EV-01, EV-02 | | ☐ |
| Riesgo 2 | Leer las primeras filas y ver si nace algo | EV-02 | | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Las 47 pruebas del módulo | `plataforma/nucleo/medicion/tests_repeticion.py` |
| EV-02 | El reporte antes y después | `resultado_pruebas.md` §2 |

---

## 6. Datos y ambiente de prueba

Conversaciones de mentiras que la prueba escribe, y lo indexado de verdad para la corrida final.

---

## 7. Reversión / rollback  ·  Q11

Nada que revertir en datos: el módulo solo lee. El código está versionado.

---

## 8. Producción y migración incremental  ·  Q12

**Aditivo puro.** Ninguna migración.

---

## 9. Reglas aplicadas  ·  Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F19`](../../../../../base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md).
- Producto: `RN-1` y `RN-2` de la especificación del módulo.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que el filtro se lleve también lo que sí importa | Alto | Se mide sobre lo real, y «español colombiano» tiene que seguir estando | Cerrado |
| B-02 | Que en un proyecto nuevo el reporte salga vacío | Medio | Con pocas sesiones no se filtra | Cerrado |
| B-03 | Que el reporte siga diciendo lo obvio | Alto — es el motivo de la fase | Se lee la salida y se decide. **Lo juzga el usuario** | Abierto |

---

## 11. Definition of Done

- [ ] El reporte con lo genérico fuera, corrido sobre lo real
- [ ] «Español colombiano» sigue estando
- [ ] Las pruebas en verde, y las dos baterías sin regresión
- [ ] Señales registradas
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
