# Plan de Pruebas — Fase `A-EP-004-HU-024-la-salida-dice-sobre-que-corrio`   ·   `[CAPA 3]`

---

## 1. Introducción

### 1.1 Propósito

Comprobar que la salida del validador dice sobre qué corrió y qué no cuenta, y que esas frases salen de lo que la corrida recorrió.

### 1.2 Alcance

**Dentro:** los tres criterios de la historia, y la prueba de que la frase no se separa del recorrido.

**Fuera:** el conteo de marcas en sí, que ya tiene sus pruebas.

### 1.3 Documentos de referencia

- [HU-024](../HU-024-el-validador-dice-que-no-comprueba.md)
- El [pendiente 91](../../../../../pendientes/91-el-validador-de-marcas-no-dice-que-no-comprueba.md)

---

## 2. Elementos a probar

| Elemento | Por qué entra |
|---|---|
| El número de archivos mirados | Es lo que hace honesta la frase |
| Un archivo fuera del alcance | Es exactamente el cero que se leyó como aprobado |
| Un árbol sin nada que mirar | Las dos respuestas se imprimían igual |
| La lista de carpetas de la frase | Para que no se separe del recorrido |

---

## 3. Estrategia de pruebas

Sobre árboles temporales, armados con archivos dentro y fuera del alcance.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- El defecto, reproducido: ya lo estaba, en un commit publicado.

### 4.2 Criterios de salida

- Las cinco pruebas en verde.
- La corrida real imprime las dos frases.

### 4.3 Criterios de suspensión y reanudación

Si la frase tuviera que escribirse a mano para pasar, se suspende: sería el
mismo defecto con otra cara.

---

## 5. Matriz de trazabilidad

| CA | Caso |
|---|---|
| CA-01 | CP-001, CP-002, CP-005 |
| CA-02 | CP-004 |
| CA-03 | CP-003 |

---

## 6. Casos de prueba

### CP-001 — Dice cuántos archivos miró

Dos archivos dentro del alcance, y la frase dice «2 archivos».

### CP-002 — No cuenta lo que está fuera de su alcance

Un archivo de `documentacion/` **con una marca** no se reporta, y la frase deja
claro que no se miró. **Es el caso que originó la historia.**

### CP-003 — El árbol sin nada que mirar lo dice

Un árbol con archivos, pero ninguno en el alcance: la frase dice que no se miró
ninguno, en vez de callar.

### CP-004 — Dice qué partes no cuenta

La segunda frase nombra lo que hay que leer para verlo.

### CP-005 — La frase y el recorrido salen del mismo sitio

**La prueba que sostiene a las otras.** Si alguien amplía el alcance y no toca
la frase, esta se cae en vez de dejar que el reporte mienta.

---

## 7. Datos y ambientes de prueba

Carpetas temporales. Ningún archivo real se toca.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Pruebas en verde | 5 de 5 |
| Frases escritas a mano en vez de derivadas | **0** |

---

## 15. Aprobación

Alcance aprobado el 2026-08-30.
