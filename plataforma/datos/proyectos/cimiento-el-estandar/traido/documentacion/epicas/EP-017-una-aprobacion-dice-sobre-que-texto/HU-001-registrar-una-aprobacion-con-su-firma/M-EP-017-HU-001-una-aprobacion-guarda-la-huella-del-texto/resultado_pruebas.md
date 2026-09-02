# Resultado de Pruebas — Fase `M-EP-017-HU-001-una-aprobacion-guarda-la-huella-del-texto`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó, con qué resultado y si cada criterio quedó cumplido**. Los casos están en el [plan_pruebas.md](plan_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `M-EP-017-HU-001-una-aprobacion-guarda-la-huella-del-texto` |
| **HU** | [HU-001 Registrar una aprobación con su firma](../HU-001-registrar-una-aprobacion-con-su-firma.md) |
| **Fecha de ejecución** | 2026-09-01 |
| **Ejecutó** | El agente |
| **Ciclo** | 1 |

---

## 1. Resumen de la ejecución

| | Cuántos |
|---|---|
| Casos del plan | 2 |
| Ejecutados | 2 |
| Pasaron | 2 |
| Fallaron | 0 |
| Pruebas automáticas nuevas | **7** |

| | Cuánto |
|---|---|
| Documentos con aprobación escrita a mano en este repositorio | **21** |
| De esas, cuántas dicen sobre qué texto | **Ninguna** |
| Aprobaciones guardadas sin huella | **0** |
| Documentos reales aprobados al probar | **0** |
| Dependencias nuevas | **0** |

---

## 2. Ejecución caso por caso

### CP-001 — Se registra quién aprobó y sobre qué

Queda quién, cuándo, la huella y el tamaño. **La huella se comparó contra el texto exacto** y coincide. La aprobación se puede consultar después, y aprobar deja su registro en la auditoría.

**Resultado: pasa.**

### CP-002 — No se aprueba lo que no existe

**El caso que decide la fase.**

| Entrada | Salió |
|---|---|
| Un documento que no está | Se rechaza |
| El mismo | **No queda nada registrado** |
| Un proyecto que no está registrado | Se rechaza |

**Aprobar algo que no está sería firmar en blanco:** cuando el documento apareciera, diría que ya se aprobó.

**Resultado: pasa.**

---

## 3. Por qué esta es la primera del módulo que guarda algo

Todos los módulos construidos hasta hoy calculan su respuesta al pedirla: el expediente, los huecos, el estado de una funcionalidad, el desfase. **Ninguno guarda, y por una razón: su respuesta está en el texto.**

Esta no. **El texto no sabe quién lo aprobó.** Aprobar es un hecho que ocurrió, y si no queda escrito no ocurrió para nadie más.

Y de ahí sale la única decisión que costó pensar: **guardar también la huella**. Sin ella la aprobación sería exactamente lo que ya hay escrito a mano en 21 documentos, con más pasos.

---

## 4. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| Qué se miró | Resultado |
|---|---|
| Las 21 marcas escritas a mano | Ninguna dice sobre qué texto se aprobó |
| Que no se aprobara nada real al probar | Ningún documento del repositorio fue aprobado |

---

## 5. Veredicto por criterio de aceptación

| CA | Evidencia | Veredicto |
|---|---|---|
| CA-01 | CP-001 | **Cumple** |
| CA-02 | CP-001 | **Cumple** |
| CA-03 | CP-002 | **Cumple** |

## 5.1 Lo que el plan exigía

| Lo que el plan pedía | Qué pasó |
|---|---|
| La huella del texto aprobado | Hecha, y comparada |
| No aprobar lo que no existe | Hecho |
| Que un intento fallido no deje registro | Comprobado |
| Sin dependencias nuevas | **Cero** |

---

## 6. Veredicto de la fase

**Concepto: Cumple.**

Una aprobación ya dice quién, cuándo y **sobre qué texto exacto**. Es la pieza de la que se sostiene el resto del gobierno, y hasta hoy no existía.

**Lo que no se hizo, a propósito:** migrar las 21 marcas escritas a mano. Cada una diría que se aprobó un texto que hoy no se puede reconstruir, y una aprobación falsa es peor que ninguna.

**Y lo que esta fase no puede decir:** si quien aprueba es quien dice ser. Se registra tal como se declara.

---

## 7. Evidencias

| ID | Qué es | Dónde |
|---|---|---|
| EV-01 | Las 7 pruebas del registro | `plataforma/nucleo/aprobaciones/tests.py` |
| EV-02 | Las 21 marcas medidas | §1 |

**Las dos baterías:** 733 pruebas del estándar y 473 de la plataforma, **cero rojas**.

---

## 8. Ciclos anteriores

No hay: es el primer ciclo de la fase.
