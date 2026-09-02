# Resultado de Pruebas — Fase `F-EP-015-HU-003-la-puerta-corre-lo-que-ya-funcionaba`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó, con qué resultado y si cada criterio quedó cumplido**. Los casos están en el [plan_pruebas.md](plan_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `F-EP-015-HU-003-la-puerta-corre-lo-que-ya-funcionaba` |
| **HU** | [HU-003 No publicar lo que rompe lo anterior](../HU-003-no-publicar-lo-que-rompe-lo-anterior.md) |
| **Fecha de ejecución** | 2026-09-01 |
| **Ejecutó** | El agente, sobre este repositorio |
| **Ciclo** | 1 |

---

## 1. Resumen de la ejecución

| | Cuántos |
|---|---|
| Casos del plan | 5 |
| Ejecutados | 5 |
| Pasaron | 5 |
| Fallaron | 0 |
| Pruebas automáticas nuevas | **14** |

**La puerta sobre este repositorio:**

```
Comprobaciones: 32 corridas, 0 con fallas
Pruebas: en verde
Tardó 118.6 s

Sin verificar, y no detienen: 21 (F-004, F-005, F-006, F-007, ...)

Se puede publicar.
```

| | Cuánto |
|---|---|
| **Cuánto tarda la puerta** | **118,6 segundos** |
| Rojos falsos al final | **0** |
| Funcionalidades que obligan a rehacer | 0 |
| Sin verificar, declaradas y sin detener | 21 |
| Dependencias nuevas | **0** |

---

## 2. Ejecución caso por caso

### CP-001 — Una versión que rompió algo no se publica

**El caso que decide la fase.**

| Entrada | Salió |
|---|---|
| Comprobaciones en rojo, pruebas en verde | No pasa |
| Comprobaciones en verde, pruebas en rojo | No pasa |
| Las dos en verde | Pasa |

**Resultado: pasa.**

### CP-002 — Lo que obliga a rehacer se declara

Una funcionalidad en «no cumple» **detiene y sale nombrada**. Las que están sin verificar **se declaran y no detienen**: que no tengan prueba no quiere decir que esta versión las rompió, y detener con eso volvería la puerta inútil desde el primer día.

**Resultado: pasa.**

### CP-003 — Lo que no rompió nada pasa, sin trabajo manual

Sobre este repositorio, que está en verde: **la puerta pasa**, con una sola orden, en 118,6 segundos.

**Resultado: pasa.**

### CP-004 — Sin revisar no se publica

| Entrada | Salió |
|---|---|
| Un proyecto que no existe | No pasa, y lo dice |
| Sin veredicto | No pasa |
| Las baterías no corrieron | No pasa |

**Resultado: pasa.**

### CP-005 — Cero comprobaciones tampoco pasa

Lo hereda del veredicto: cero no es verde.

**Resultado: pasa.**

---

## 3. El rojo falso que la puerta dio en su primera corrida

**Y es el defecto exacto que esta puerta viene a evitar.**

La primera versión corría las baterías con `internas --raiz <proyecto>`. Ese subcomando corre las pruebas **del estándar donde el estándar vive**, y **no acepta `--raiz`**: el intérprete de argumentos lo rechazó y salió con código 2.

La puerta leyó ese código como **rojo** y dijo:

```
Pruebas: **con rojas**
**No se publica.**
```

**Con las 1 082 pruebas en verde.**

**Por qué importa más que un error cualquiera.** Un rojo falso no es una molestia: es lo que enseña a ignorar la puerta. La primera vez uno investiga; la tercera, la salta. Y el día que el rojo sea de verdad, ya nadie lo mira.

**Qué lo causó, en una línea:** un código de salida distinto de cero puede querer decir «las pruebas fallaron» o «no entendí lo que me pediste», y tratarlos igual convierte un error propio en un veredicto ajeno.

**Cómo quedó:** se corre `suite --raiz`, que sí apunta a un proyecto. Y el «no se pudo correr» tiene su propia respuesta, distinta de «rojo».

---

## 4. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| Qué se miró | Resultado |
|---|---|
| Que la puerta pase con el repositorio en verde | Pasa |
| Las 21 sin verificar que declara | Ninguna está construida |
| Que no se rompiera nada para probar el rojo | No se rompió: el rojo se armó en el veredicto |

---

## 5. Veredicto por criterio de aceptación

| CA | Evidencia | Veredicto |
|---|---|---|
| CA-01 | CP-001 | **Cumple** |
| CA-02 | CP-002 | **Cumple** |
| CA-03 | CP-003, §1 | **Cumple** |
| CA-04 | CP-004 | **Cumple** |

## 5.1 Lo que el plan exigía

| Lo que el plan pedía | Qué pasó |
|---|---|
| «Lo que ya funcionaba» es todo, no una lista | Hecho: comprobaciones y suite enteras |
| Un «no se pudo» no pasa | Hecho |
| Lo sin verificar se declara y no detiene | Hecho |
| La puerta corrida, con el tiempo | **118,6 s**, y pasa |
| Sin dependencias nuevas | **Cero** |

---

## 6. Veredicto de la fase

**Concepto: Cumple.**

Antes de publicar se vuelve a correr todo lo que ya funcionaba, con una sola orden. Lo que rompió algo no sale; lo que obliga a rehacer se nombra; lo que nadie comprobó se declara y no detiene.

**Con esta fase cierra `EP-015` y la vuelta de la columna:** `F-008`, publicar una versión, ya tiene su puerta.

**Lo que la fase encontró, y es lo mejor que dejó:** su propio rojo falso, en la primera corrida, por confundir «no entendí el argumento» con «las pruebas fallaron». Un rojo falso enseña a ignorar la puerta, y es el modo de falla que la vuelve inútil sin que nadie lo note.

---

## 7. Evidencias

| ID | Qué es | Dónde |
|---|---|---|
| EV-01 | Las 14 pruebas de la puerta | `plataforma/nucleo/comprobaciones/tests_puerta.py` |
| EV-02 | La puerta sobre este repositorio | §1 y §3 |

**Las dos baterías:** 733 pruebas del estándar y 353 de la plataforma, **cero rojas**.

---

## 8. Ciclos anteriores

No hay: es el primer ciclo de la fase.
