# Resultado de Pruebas — Fase «A-EP-003-HU-004-el-origen-de-la-regla-de-negocio»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. El diseño de los casos vive en el [`plan_pruebas.md`](plan_pruebas.md), que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-003-HU-004-el-origen-de-la-regla-de-negocio` |
| **HU** | [HU-004 — Modelo de la especificación](../HU-004-modelo-de-la-especificacion.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-16 |
| **Ejecutado por** | El agente |
| **Ambiente y versión** | El documento · estándar 21.3.1 → 22.0.0 |

---

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

---

## 2. Ejecución caso por caso

### CA-04 · CP-001 — la regla que baja de un requisito cabe en el formato

Se escribió con el molde nuevo la regla que sí tenía origen en el caso de `shopnest-mesa`:

```
1. «Un problema registra causa raíz y solución definitiva — RF-13 — para que
   quien lo lea después sepa por qué pasaba y qué se hizo.»
```

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Escribirla con origen y porqué | Cabe en una línea legible | Cabe |
| 2 | Leerla de nuevas | Se sabe quién la pidió sin salir del documento | `RF-13` |
| 3 | Comprobar que sigue siendo lista numerada | Se puede citar por su número | Sigue |

**Veredicto:** ✅ Cumple.

---

### CA-04 · CP-002 — la regla sin procedencia no tiene dónde escribirse

Se intentó escribir con el molde nuevo la regla que destapó el pendiente:

```
1. «Un problema no se cierra sin causa raíz ni solución definitiva — ??? — porque
   cerrar es afirmar que ya no vuelve, y eso no se puede afirmar sin saber
   por qué pasaba.»
```

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Escribirla con el molde | El hueco del origen queda a la vista | Queda, y no se puede disimular: va en el medio de la frase |
| 2 | Buscarle identificador | No hay | No lo hay: ni el enunciado, ni `RF-13` —que manda *registrar*, no exigir al cerrar—, ni la épica, ni la historia |
| 3 | Leer qué manda el modelo | Que no se escribe ahí, y se sube a la historia | Lo dice, en la nota del §4 |

**Veredicto:** ✅ Cumple.

**La diferencia entre las dos es la que importa.** La del CP-001 y la del CP-002 dicen casi lo mismo y no son la misma regla: una manda **registrar** dos campos y baja de `RF-13`; la otra manda **no cerrar** sin ellos y no baja de ninguna parte. Con el molde viejo las dos se veían igual de bien escritas.

---

### No regresión · CP-003 — una especificación ya escrita no queda inválida

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Leer un §4 viejo contra el modelo nuevo | Le falta un dato, no sobra ninguno | Le falta |
| 2 | ¿Hay que reescribirlo para seguir cumpliendo? | No | No: lo cerrado queda sellado con su versión |

**Veredicto:** ✅ Cumple.

---

## 3. Defectos encontrados

Ninguno.

---

## 4. Lo que se descubrió fuera del criterio

**El cierre del pendiente 43 no cabe en esta fase.** El pendiente pide tres cosas: el molde, **el programa que lo comprueba** y mirar los §4 ya escritos. El programa vive en otro módulo, así que va en su propia fase bajo EP-004 ([`02·F11`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F11-una-fase-solo-modifica-codigo-de-su-propio-modulo.md)) — el plan ya lo declaraba fuera de alcance, pero la tarea `T-04` decía «cerrar el 43» y eso era prematuro.

**Se corrige así:** esta fase deja el molde y sube la versión; el pendiente 43 se cierra al terminar la fase del validador, que es cuando su segunda exigencia queda cumplida. Queda escrito acá y no se marca `T-04` como hecha.

---

## 5. Cobertura contra el plan de pruebas

| Exigencia | Caso | Estado |
|---|---|---|
| CA-04 — la regla que baja de un requisito cabe | CP-001 | ✅ |
| CA-04 — la regla sin procedencia no entra | CP-002 | ✅ |
| No regresión — lo ya escrito no queda inválido | CP-003 | ✅ |

**Cobertura:** 1 de 1 CA = 100%.

---

## 6. Veredicto de la fase

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 1 de 1 |
| **CA en "No"** | ninguno |
| **Defectos abiertos aceptados** | ninguno |

---

## 7. Métricas contra la meta del plan

| Métrica | Meta | Dio |
|---|---|---|
| Cobertura de CA | 100% | 100% |
| Casos ejecutados | 3 de 3 | 3 de 3 |
| Especificaciones vivas que hay que reescribir | 0 | 0 |
