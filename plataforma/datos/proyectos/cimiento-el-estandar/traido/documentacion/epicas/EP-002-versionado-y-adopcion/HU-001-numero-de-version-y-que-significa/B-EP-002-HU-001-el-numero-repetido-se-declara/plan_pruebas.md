# Plan de Pruebas — Fase `B-EP-002-HU-001-el-numero-repetido-se-declara`   ·   `[CAPA 3]`

---

## 1. Introducción

### 1.1 Propósito

Comprobar el CA-01 de la HU-001 con la exigencia que el registro sí sostiene: **un número repetido queda declarado**, con sus dos entradas a la vista.

### 1.2 Alcance

**Dentro:** la secuencia de números del registro real, y una secuencia inventada con un repetido callado.

**Fuera:** renumerar nada, y el resto de criterios de la historia, que ya estaban en verde.

### 1.3 Documentos de referencia

- [HU-001](../HU-001-numero-de-version-y-que-significa.md)
- [Resultado de la fase A](../A-EP-002-HU-001-retrodocumentar-el-numero-de-version/resultado_pruebas.md)
- Las dos entradas `15.4.0` del `CHANGELOG.md`

---

## 2. Elementos a probar

| Elemento | Por qué entra |
|---|---|
| La secuencia del registro real | Es lo que el CA-01 mide |
| Un repetido **sin** declarar | Es el defecto de verdad, y en el registro real no ocurre |

---

## 3. Estrategia de pruebas

La comprobación se saca a un método propio que recibe la secuencia. Así el caso que no existe en el registro real se puede probar igual, sin inventar nada en el `CHANGELOG.md`.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- Las dos entradas `15.4.0` y su motivo, leídos.

### 4.2 Criterios de salida

- El registro real no produce ningún reclamo.
- El repetido callado produce exactamente uno.
- El mismo repetido, declarado, no produce ninguno.

### 4.3 Criterios de suspensión y reanudación

Si el registro real hubiera traído un repetido **sin** declarar, la fase no cierra: eso es un defecto y no una excepción.

---

## 5. Matriz de trazabilidad

| CA | Caso |
|---|---|
| CA-01 | CP-001, CP-002 |

---

## 6. Casos de prueba

### CP-001 — El registro real avanza, y lo repetido está declarado

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-01 |
| **Tipo** | De ejecución |
| **Prioridad** | Alta |
| **Cómo** | Recorrer las entradas del `CHANGELOG.md` de la más vieja a la más nueva |
| **Resultado esperado** | Cero reclamos |

### CP-002 — El repetido que no se declara sí falla

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-01, contraprueba |
| **Tipo** | Que **no** pase |
| **Prioridad** | **Crítica** |
| **Cómo** | Una secuencia inventada con `1.1.0` dos veces, primero callada y después declarada |
| **Resultado esperado** | Un reclamo en la callada, ninguno en la declarada |

---

## 7. Datos y ambientes de prueba

El registro real, sin modificarlo, y una lista escrita dentro de la prueba.

---

## 8. Herramientas

`python -m unittest pruebas.NumeroDeVersion`

---

## 9. Gestión de defectos

Un fallo en CP-001 significa que alguien pisó un número en silencio, y eso se arregla declarándolo, no renumerando.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Pruebas de la clase en verde | 5 de 5 |
| Pruebas marcadas como fallo esperado | **0** |

---

## 15. Aprobación

Alcance y lectura del CA-01 aprobados el 2026-08-30.
