# Resultado de Pruebas — Fase `J-EP-016-HU-004-sin-decir-que-cambio-no-se-publica`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó, con qué resultado y si cada criterio quedó cumplido**. Los casos están en el [plan_pruebas.md](plan_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `J-EP-016-HU-004-sin-decir-que-cambio-no-se-publica` |
| **HU** | [HU-004 Publicar una versión del cuerpo de reglas](../HU-004-publicar-una-version-del-cuerpo-de-reglas.md) |
| **Fecha de ejecución** | 2026-09-01 |
| **Ejecutó** | El agente |
| **Ciclo** | 1 |

---

## 1. Resumen de la ejecución

| | Cuántos |
|---|---|
| Casos del plan | 4 |
| Ejecutados | 4 |
| Pasaron | 4 |
| Fallaron | 0 |
| Pruebas automáticas nuevas | **13** |

| | Cuánto |
|---|---|
| Entradas del registro real | **197** |
| Órdenes en que se escribe el tipo | **2**, y los dos se leen |
| Veces que el archivo de versión cambió faltando algo | **0** |
| Dependencias nuevas | **0** |

---

## 2. Ejecución caso por caso

### CP-001 — No se publica dos veces el mismo número

Una versión ya publicada se rechaza, con el porqué escrito: dos proyectos declarando la misma versión con reglas distintas es un desorden que no se deshace desde acá. Una que no existe pasa esa comprobación.

**Resultado: pasa.**

### CP-002 — Sin decir qué cambió no se publica

**El caso que decide la fase.**

| Entrada | Salió |
|---|---|
| Sin entrada en el registro | Se rechaza |
| Con entrada, tipo delante | Se lee el tipo |
| Con entrada, **título delante** | Se lee el tipo igual |
| Con entrada sin tipo | Se rechaza |
| La entrada de una versión | Recortada hasta la siguiente |

**Los dos órdenes importan**, y no es un detalle: el registro se escribió con el tipo delante hasta que `M17` pidió que la entrada abriera contando qué pasó. Leer uno solo dejaría fuera la mitad del registro.

**Resultado: pasa.**

### CP-003 — Lo que rompe algo no se publica

Con la puerta en rojo se rechaza; con todo en verde se puede.

**Resultado: pasa.**

### CP-004 — Publicar escribe la versión

Con todo en verde, el archivo queda con el número nuevo. **Si falta algo, el archivo no cambia**, y lo que falta sale **todo junto**: de a uno obligaría a intentar tres veces.

**Resultado: pasa.**

---

## 3. Lo que esta fase cierra

**Con `F-008` se cierra la vuelta de la columna de dependencias** que apareció al abrir la versión 3:

```
F-008 (publicar) -> F-022 (comprobar que no rompio) -> F-020 (comprobar) -> F-008
```

`F-020` se pudo construir porque lo que hay que comprobar ya existía escrito. `F-022` se construyó sobre `F-020`. Y `F-008`, sobre `F-022`. **Lo que parecía un bloqueo era una columna mal leída.**

---

## 4. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| Qué se miró | Resultado |
|---|---|
| El registro real, con sus 197 entradas | Los dos órdenes conviven |
| Que publicar de verdad no se disparara al probar | Se usó un registro y un archivo de mentiras |

---

## 5. Veredicto por criterio de aceptación

| CA | Evidencia | Veredicto |
|---|---|---|
| CA-01 | CP-001, CP-004 | **Cumple** |
| CA-02 | CP-002 | **Cumple** |
| CA-03 | CP-003 | **Cumple** |

## 5.1 Lo que el plan exigía

| Lo que el plan pedía | Qué pasó |
|---|---|
| Sin entrada no se publica | Hecho |
| El tipo, en los dos órdenes | Hecho |
| La puerta detiene | Hecho |
| El archivo no cambia si falta algo | Hecho |
| Sin dependencias nuevas | **Cero** |

---

## 6. Veredicto de la fase

**Concepto: Cumple.**

Una versión se publica solo cuando el número está libre, el registro dice qué cambió con su tipo, y la puerta pasa. Lo que falta sale todo junto, y si falta algo el archivo de versión no se toca.

**Lo que esta fase cierra es más grande que ella:** la vuelta de la columna de dependencias que parecía impedir arrancar la versión 3.

**Y lo que la plataforma sigue sin hacer, a propósito:** escribir la entrada del registro. Es prosa, dice qué pasó y por qué importa, y generada diría lo mismo siempre.

---

## 7. Evidencias

| ID | Qué es | Dónde |
|---|---|---|
| EV-01 | Las 13 pruebas de la publicación | `plataforma/nucleo/reglas/tests_publicacion.py` |
| EV-02 | El registro real, con sus dos órdenes | §2 |

**Las dos baterías:** 733 pruebas del estándar y 426 de la plataforma, **cero rojas**.

---

## 8. Ciclos anteriores

No hay: es el primer ciclo de la fase.
