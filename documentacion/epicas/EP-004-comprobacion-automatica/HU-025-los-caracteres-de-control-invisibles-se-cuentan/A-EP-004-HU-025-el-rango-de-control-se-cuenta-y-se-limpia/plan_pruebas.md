# Plan de Pruebas — Fase `A-EP-004-HU-025-el-rango-de-control-se-cuenta-y-se-limpia`   ·   `[CAPA 3]`

---

## 1. Introducción

### 1.1 Propósito

Comprobar que los caracteres de control se cuentan, que la limpieza los quita sin tocar el texto visible, y que lo que sí significa algo al escribir no se toca.

### 1.2 Alcance

**Dentro:** el rango completo, la limpieza, y el árbol real después de limpiar.

**Fuera:** el histórico y la carpeta de datos de la plataforma.

### 1.3 Documentos de referencia

- [HU-025](../HU-025-los-caracteres-de-control-invisibles-se-cuentan.md)
- El [pendiente 92](../../../../../pendientes/92-hay-caracteres-de-control-invisibles-en-26-documentos.md)

---

## 2. Elementos a probar

| Elemento | Por qué entra |
|---|---|
| El carácter que rompió la fila | Es el caso que originó la historia |
| Cinco puntos del rango | Para que no se cuente solo el que apareció |
| El tabulador, el salto y el retorno | Contarlos volvería la comprobación ruido |
| El árbol real | Es el criterio de cierre |

---

## 3. Estrategia de pruebas

Cadenas armadas dentro de la prueba para los casos, y el contador real del árbol para el cierre. Ninguna prueba escribe en el repositorio.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- El árbol contado antes de tocar nada: 26 archivos con el carácter.

### 4.2 Criterios de salida

- Las cinco pruebas en verde.
- El contador del árbol, en cero para los de control.

### 4.3 Criterios de suspensión y reanudación

Si la limpieza cambiara algo más que el carácter invisible, se detiene: sería peor que el defecto.

---

## 5. Matriz de trazabilidad

| CA | Caso |
|---|---|
| CA-01 | CP-001, CP-002 |
| CA-02 | CP-004, CP-005 |
| CA-03 | CP-003 |

---

## 6. Casos de prueba

### CP-001 — El que rompió la fila se cuenta

| Campo | Valor |
|---|---|
| **Tipo** | De ejecución |
| **Prioridad** | Alta |
| **Cómo** | Una línea de tabla que empieza con el carácter invisible |
| **Resultado esperado** | Un hallazgo que lo nombra |

### CP-002 — Se cuenta el rango, no solo el que apareció

| Campo | Valor |
|---|---|
| **Tipo** | De ejecución |
| **Prioridad** | **Crítica** |
| **Cómo** | Cinco puntos distintos del rango |
| **Resultado esperado** | Los cinco contados |

### CP-003 — Lo que sí significa algo no se toca

| Campo | Valor |
|---|---|
| **Tipo** | Que **no** pase |
| **Prioridad** | **Crítica** |
| **Cómo** | Tabulador, salto de línea y retorno |
| **Resultado esperado** | Ningún hallazgo |

### CP-004 — La limpieza no cambia el texto visible

| Campo | Valor |
|---|---|
| **Tipo** | Que **no** pase |
| **Prioridad** | **Crítica** |
| **Cómo** | Comparar el antes y el después de una tabla con el carácter |
| **Resultado esperado** | Idénticos salvo el carácter que no se veía |

### CP-005 — El árbol queda en cero

| Campo | Valor |
|---|---|
| **Tipo** | De sistema |
| **Cómo** | El contador del repositorio |
| **Resultado esperado** | Ninguno |

---

## 7. Datos y ambientes de prueba

Cadenas y el árbol real, sin escribir en él desde la prueba.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Pruebas en verde | 5 de 5 |
| Caracteres de control en el árbol contado | **0** |

---

## 15. Aprobación

Alcance aprobado el 2026-08-30.
