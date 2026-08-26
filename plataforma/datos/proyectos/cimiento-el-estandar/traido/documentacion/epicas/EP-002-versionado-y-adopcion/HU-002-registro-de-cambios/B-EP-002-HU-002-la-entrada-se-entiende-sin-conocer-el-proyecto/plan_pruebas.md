# Plan de Pruebas — Fase B-EP-002-HU-002: la entrada se entiende sin conocer el proyecto

| Campo | Valor |
|---|---|
| **Código** | PP-B-EP-002-HU-002 · **Versión** 1.0 · **Fecha** 2026-08-18 |
| **Aprobado por** | Pendiente — el usuario |

---

## 3. Estrategia

**La prueba que importa la hace una persona, no un programa.** Un programa no sabe si algo se entiende; lo que sabe es si el texto abre con palabras que solo significan algo adentro. Por eso hay dos niveles: **un lector real** para el `CA-03`, y la comprobación mecánica para que no vuelva a pasar.

**Y el riesgo del programa es apagarse.** Si reportara las 83 entradas, nadie volvería a mirar la salida.

---

## 5. Matriz de trazabilidad

| Exigencia | Caso | Estado |
|---|---|---|
| `CA-03` · se entiende sin haber seguido el trabajo | [CP-001](#cp-001--un-lector-real-lee-una-entrada) | ☐ |
| Se reporta la apertura con identificador, ruta o jerga | [CP-002](#cp-002--lo-que-se-reporta) | ☐ |
| No se reporta la entrada llana ni el detalle de abajo | [CP-003](#cp-003--lo-que-no-se-reporta) | ☐ |
| Solo la versión vigente | [CP-004](#cp-004--las-viejas-no-se-reportan) | ☐ |
| No regresión | [CP-005](#cp-005--nada-de-lo-que-ya-estaba-deja-de-pasar) | ☐ |

---

## 6. Casos

### CP-001 — Un lector real lee una entrada

Se le muestra a alguien que no siguió el trabajo una entrada del registro y se le pregunta **qué cambió y por qué**. Si no lo sabe decir, el caso falla.

> **Es la única prueba que vale para este criterio.** Quien escribió la entrada ya sabe de qué habla, así que releerla uno mismo no comprueba nada.

### CP-002 — Lo que se reporta

Tres aperturas, una por motivo: con identificador de regla, con ruta de archivo, con palabras de la casa. Y una con dos motivos, para que el mensaje los junte.

### CP-003 — Lo que no se reporta

La entrada llana; y la que abre en llano **y lleva el detalle debajo**, con su identificador y su ruta.

> El detalle no sobra: solo estaba en el lugar equivocado.

### CP-004 — Las viejas no se reportan

Una entrada anterior mal escrita, con la vigente bien: no se reporta.

### CP-005 — Nada de lo que ya estaba deja de pasar

Las dos suites y `validar.py estandar`.

---

## 12. Métricas

| Métrica | Meta |
|---|---|
| Entradas viejas reportadas | **0** |
| Detalle perdido al reescribir | **0** |
| Comprensión medida por un programa | **0** — no se mide, se declara |

Un solo concepto: **Cumple** o **No cumple**.
