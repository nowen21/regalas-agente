# Plan de Pruebas — Fase `B-EP-006-HU-002-las-senales-viven-en-la-base-de-cimiento`   ·   `[CAPA 3]`

---

## 1. Introducción

### 1.1 Propósito

Comprobar el CA-01, lo guardado vive en el repositorio con su historial después de aplicar la decisión del usuario.

### 1.2 Alcance

**Dentro:** contar lo que hay en cada sitio, y comprobar el resultado de aplicar la decisión.

**Fuera:** los otros criterios de la historia, que ya estaban en verde.

### 1.3 Documentos de referencia

- [HU-002](../HU-002-guardar-en-el-repositorio.md)
- [Resultado de la fase A](../A-EP-006-HU-002-retrodocumentar-el-guardado-en-el-repositorio/resultado_pruebas.md)

---

## 2. Elementos a probar

| Elemento | Por qué entra |
|---|---|
| Lo que hay en cada sitio | El criterio habla de dónde vive cada cosa |
| El resultado de aplicar la decisión | Una decisión escrita y no aplicada no cierra nada |

---

## 3. Estrategia de pruebas

De ejecución: se cuenta sobre el árbol y sobre la base, no se lee el documento de la fase anterior.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- La decisión del usuario, escrita.

### 4.2 Criterios de salida

- Las cuentas de cada sitio, tomadas.
- La decisión, aplicada y comprobada.

### 4.3 Criterios de suspensión y reanudación

Si al contar apareciera algo que la decisión no cubre, la fase se detiene y se pregunta.

---

## 5. Matriz de trazabilidad

| CA | Caso |
|---|---|
| CA-01, lo guardado vive en el repositorio con su historial | CP-001 |

---

## 6. Casos de prueba

### CP-001 — Qué hay en cada sitio, contado

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-01, lo guardado vive en el repositorio con su historial |
| **Tipo** | De ejecución |
| **Prioridad** | Alta |
| **Resultado esperado** | Que lo contado coincida con lo que la decisión dice que debe pasar |

---

## 7. Datos y ambientes de prueba

El repositorio y la base de señales, tal como están.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cuentas tomadas leyendo en vez de contando | **0** |

---

## 15. Aprobación

Alcance aprobado el 2026-08-30, con la decisión del usuario.
