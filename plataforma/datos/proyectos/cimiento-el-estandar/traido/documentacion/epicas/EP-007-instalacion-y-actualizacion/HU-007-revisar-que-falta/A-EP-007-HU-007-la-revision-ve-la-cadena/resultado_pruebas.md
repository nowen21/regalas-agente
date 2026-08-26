# Resultado de Pruebas — Fase «A-EP-007-HU-007-la-revision-ve-la-cadena»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. El diseño de los casos vive en el [`plan_pruebas.md`](plan_pruebas.md), que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-007-HU-007-la-revision-ve-la-cadena` |
| **HU** | [HU-007 — Revisar qué le falta al proyecto](../HU-007-revisar-que-falta.md) |
| **Ciclo** | 2 |
| **Fecha de ejecución** | 2026-08-16 |
| **Ejecutado por** | El agente |
| **Ambiente y versión** | Windows 11 · Python 3.11 · estándar 22.1.0 → 23.0.0 |

---

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 3 | 1 | 0 | 0 |
| 2 | 4 | 4 | 4 | 0 | 0 | 0 |

**El que falló en el ciclo 1 fue el CP-001, y falló por estar mal escrito**, no por el código.

---

## 2. Ejecución caso por caso

### CA-01 · CP-001 — la cadena vacía se nombra, y se dice cómo se arregla

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Revisar un proyecto con código y `prompts/` vacía | El punto sale como faltante | Sale |
| 2 | Leer el detalle | Dice que no hay ningún planteamiento | Lo dice, y dice dónde va |
| 3 | Leer cómo se arregla | Dice que no lo pone el instalador | Lo dice |
| 4 | Leer el resumen | **No** dice «instalación completa» | **Ciclo 1: rojo por el caso.** Ciclo 2: `INSTALACIÓN INCOMPLETA · proyecto · 3 de 14` |

**Veredicto:** ✅ Cumple.

---

### CA-02 · CP-002 — el punto se apaga al escribir el planteamiento

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Escribir el planteamiento y una épica | La cadena arrancó | Arrancó |
| 2 | Revisar otra vez | El punto ya no aparece | No aparece |

**Veredicto:** ✅ Cumple.

---

### CA-01 · CP-003 — la épica solo se exige si hay código

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Revisar con planteamiento y `proyectos/` vacía | El punto no aparece | No aparece |
| 2 | Poner código y revisar | Aparece, pidiendo la épica | Aparece, y el detalle nombra la épica |

**Veredicto:** ✅ Cumple.

---

### CA-01 · CP-004 — el caso se pone rojo si se quita el punto

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Quitar la fila del punto de la lista de componentes | Queda como antes de la fase | Quedó |
| 2 | Correr la suite de la fase | Se pone roja | `unexpectedly None : el punto de la cadena no está en la lista de componentes` — 1 falla y 2 errores |
| 3 | Devolver la fila y correr todo | Verde | 32 de 32 |

**Veredicto:** ✅ Cumple.

---

## 3. Defectos encontrados

| ID | Caso | Qué pasó | De quién era | Estado |
|---|---|---|---|---|
| DEF-01 | CP-001 | El caso buscaba la palabra «completa» en el resumen para afirmar que **no** decía que estaba completa. Pero «in**completa**» la contiene, así que daba rojo contra un resumen correcto | Del caso | Corregido: se busca la frase entera «instalación completa», y se agrega que la cuenta llegue a 14 |
| DEF-02 | Suite anterior | El `CP-004` de `test_instalar_reparar` exigía que después de instalar **no faltara nada**, y el punto nuevo no lo instala nadie por diseño | De la prueba anterior, que quedó desactualizada por este cambio | Corregido: se excluye el punto no instalable, con el motivo escrito en el propio caso |

**El `DEF-02` es una ampliación de plan ([`02·F8`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).** El §2.2 del plan decía que `instalar.py` no se veía afectado, y era cierto del programa pero no de su prueba: al agregar un punto que el instalador no puede poner, la afirmación «no falta nada después de instalar» dejó de ser correcta. Se ajustó la afirmación, no la exigencia: sigue comprobando que el instalador deje puesto todo lo que sí instala.

---

## 4. Lo que se descubrió fuera del criterio

**Este repositorio reprueba su propio punto nuevo.** Es el riesgo `B-02` del plan, y se materializó:

```
INSTALACIÓN INCOMPLETA · agente · 6 de 14 · falta: f13, claude-md, gitignore, agente-config y 4 más
cadena -> FALTA | no hay ningún planteamiento en `prompts/`
```

Hay que leerlo con cuidado antes de sacar conclusiones: **el estándar no se instala a sí mismo** —no tiene `CLAUDE.md` heredado ni `.agente/`, y por eso reprueba ocho puntos que no le aplican—, así que ese «6 de 14» no dice lo mismo que en un proyecto. Pero el punto de la cadena **sí** aplica: `prompts/` de esta casa tiene 40 archivos y ninguno es un planteamiento, y el trabajo del estándar sí es desarrollo.

No se tocó acá porque no es de esta fase: escribir el planteamiento del estándar es una decisión de qué es este proyecto, no una tarea de código. Queda anotado.

---

## 5. Cobertura contra el plan de pruebas

| Exigencia | Caso | Estado |
|---|---|---|
| CA-01 — la cadena vacía se nombra | CP-001 | ✅ |
| CA-02 — el punto se apaga al escribirlo | CP-002 | ✅ |
| CA-01 · límites — la épica solo si hay código | CP-003 | ✅ |
| CA-01 · prueba de la prueba | CP-004 | ✅ |

**Cobertura:** 2 de 2 CA = 100%.

---

## 6. Veredicto de la fase

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 2 de 2 |
| **CA en "No"** | ninguno |
| **Defectos abiertos aceptados** | ninguno. Los dos eran de las pruebas y quedaron corregidos |

---

## 7. Métricas contra la meta del plan

| Métrica | Meta | Dio |
|---|---|---|
| Cobertura de CA | 100% | 100% |
| Casos ejecutados | 4 de 4 | 4 de 4, en dos ciclos |
| Pruebas del repositorio en verde | 29 + las nuevas | 32 de 32 |
| Puntos de la revisión | 14 | 14 |
