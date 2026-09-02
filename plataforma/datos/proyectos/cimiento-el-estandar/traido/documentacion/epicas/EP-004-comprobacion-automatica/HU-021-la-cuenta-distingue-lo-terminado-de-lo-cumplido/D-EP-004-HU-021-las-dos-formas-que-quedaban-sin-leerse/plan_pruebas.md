# Plan de Pruebas — Fase `D-EP-004-HU-021-las-dos-formas-que-quedaban-sin-leerse`   ·   `[CAPA 3]`

---

## 1. Introducción

### 1.1 Propósito

Comprobar que el lector del veredicto reconoce las dos formas que faltaban, y que sigue sin leer de más.

### 1.2 Alcance

**Dentro:** las dos formas nuevas, y el caso que no debe leerse.

**Fuera:** las tres formas que las fases `A`, `B` y `C` ya cubrían, que siguen con sus pruebas.

### 1.3 Documentos de referencia

- [HU-021](../HU-021-la-cuenta-distingue-lo-terminado-de-lo-cumplido.md)
- Los cinco resultados que quedaban mudos

---

## 2. Elementos a probar

| Elemento | Por qué entra |
|---|---|
| `**Concepto: Cumple.**` | Tres fases lo escriben así |
| `## N. Concepto final` con la palabra debajo | Dos fases lo escriben así |
| Una tabla de criterios antes del veredicto | Es lo que el lector **no** debe tomar |

---

## 3. Estrategia de pruebas

Sobre árboles temporales armados con el texto exacto de cada forma, y sobre el
árbol real para la línea base.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- Las cinco fases mudas, leídas: las cinco dicen su veredicto.

### 4.2 Criterios de salida

- Las 35 pruebas de la clase en verde.
- La cuenta de «sin veredicto» en cero, sin que ninguna pase de «No cumple» a «Cumple».

### 4.3 Criterios de suspensión y reanudación

Si al ampliar el lector alguna fase cambiara de «No cumple» a «Cumple», se
suspende: significaría que se está leyendo la fila de un criterio.

---

## 5. Matriz de trazabilidad

| CA | Caso |
|---|---|
| La tercera cuenta dice la verdad | CP-001, CP-002, CP-003 |

---

## 6. Casos de prueba

### CP-001 — Los dos puntos dentro de la negrita

| Campo | Valor |
|---|---|
| **Cómo** | Un resultado con `## 6. Veredicto de la fase` y `**Concepto: Cumple.**` |
| **Resultado esperado** | `(1, 0, 0)` |

### CP-002 — El encabezado que dice «Concepto»

| Campo | Valor |
|---|---|
| **Cómo** | Un resultado con `## 6. Concepto final` y `**Cumple.**` debajo |
| **Resultado esperado** | `(1, 0, 0)` |

### CP-003 — La tabla de criterios no se toma por el veredicto

| Campo | Valor |
|---|---|
| **Tipo** | Que **no** pase |
| **Prioridad** | **Crítica** |
| **Cómo** | Un resultado con una tabla de criterios en «Cumple» y el veredicto de la fase en «No cumple» |
| **Resultado esperado** | `(0, 1, 0)` |

**La CP-003 es la que sostiene a las otras dos.** Sin ella, ampliar el lector
sería aflojarlo.

---

## 7. Datos y ambientes de prueba

Carpetas temporales. Ningún resultado real se modifica.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Pruebas de la clase en verde | 35 de 35 |
| Fases que pasan de «No cumple» a «Cumple» | **0** |

---

## 15. Aprobación

Alcance aprobado el 2026-08-30.
