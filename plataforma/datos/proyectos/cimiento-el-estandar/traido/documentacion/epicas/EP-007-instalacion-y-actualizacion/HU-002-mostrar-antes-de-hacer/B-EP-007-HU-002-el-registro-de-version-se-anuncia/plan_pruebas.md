# Plan de Pruebas — Fase `B-EP-007-HU-002-el-registro-de-version-se-anuncia`   ·   `[CAPA 3]`

---

## 1. Introducción

### 1.1 Propósito

Comprobar el CA-02 de la HU-002: **cada archivo que la simulación anuncia aparece al aplicar, y no aparece ninguno que no se hubiera anunciado.**

### 1.2 Alcance

**Dentro:** la corrida simulada y la corrida aplicada sobre el mismo proyecto de prueba, comparadas archivo por archivo.

**Fuera:** el defecto `D-02` de la fase `A`, y el CA-01, que ya cumplía y solo se cuida de no romper.

### 1.3 Documentos de referencia

- [HU-002](../HU-002-mostrar-antes-de-hacer.md)
- [Resultado de la fase A](../A-EP-007-HU-002-retrodocumentar-el-mostrar-antes-de-hacer/resultado_pruebas.md), defecto `D-01`

---

## 2. Elementos a probar

| Elemento | Por qué entra |
|---|---|
| Los archivos nuevos tras aplicar, contra lo anunciado | Es lo que el CA-02 mide |
| Que simular siga sin escribir nada | El arreglo toca el mismo código; romper el CA-01 sería peor que el defecto |
| Que un proyecto al día siga sin anunciar trabajo | La huella prevista es igual a la que hay, y no debe inventar cambios |

---

## 3. Estrategia de pruebas

De sistema: se corre el instalador de verdad, dos veces, sobre un proyecto de
prueba que la prueba arma y borra.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- El defecto, reproducido: la prueba existía como fallo esperado.

### 4.2 Criterios de salida

- Ningún archivo aparece sin haberse anunciado.
- Las cuatro pruebas de la clase en verde, **sin ningún fallo esperado**.

### 4.3 Criterios de suspensión y reanudación

Si al arreglar el anuncio la simulación empezara a escribir, se suspende: el
CA-01 pesa más que el CA-02.

---

## 5. Matriz de trazabilidad

| CA | Caso |
|---|---|
| CA-02 | CP-003 |
| CA-01 (no romper) | CP-002, CP-004 |

---

## 6. Casos de prueba

### CP-003 — Lo que muestra es lo que hace

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-02 |
| **Tipo** | De sistema |
| **Prioridad** | **Crítica** |
| **Cómo** | Simular sobre un proyecto nuevo, guardar la salida, aplicar, y comprobar que el nombre de cada archivo nuevo aparece en la salida simulada |
| **Resultado esperado** | Ninguno sin anunciar |

### CP-002 — El modo que muestra no escribe ni un archivo

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-01 |
| **Tipo** | Que **no** pase |
| **Prioridad** | **Crítica** |
| **Cómo** | Simular y comparar el árbol antes y después |
| **Resultado esperado** | Idéntico |

### CP-004 — Un proyecto al día no anuncia trabajo

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / transversal de límites |
| **Tipo** | De borde |
| **Prioridad** | Alta |
| **Cómo** | Aplicar y volver a simular |
| **Resultado esperado** | Ninguna línea «(simulado) crear» |

---

## 7. Datos y ambientes de prueba

Un proyecto de prueba temporal, armado y borrado por la propia prueba.

---

## 8. Herramientas

`python -m unittest pruebas.MostrarAntesDeHacer`

---

## 9. Gestión de defectos

Un fallo en CP-002 detiene la fase: significa que el arreglo del anuncio rompió
la promesa de no tocar nada.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Pruebas de la clase en verde | 4 de 4 |
| Pruebas marcadas como fallo esperado | **0** |
| Archivos que aparecen sin anunciarse | **0** |

---

## 15. Aprobación

Alcance aprobado el 2026-08-30.
