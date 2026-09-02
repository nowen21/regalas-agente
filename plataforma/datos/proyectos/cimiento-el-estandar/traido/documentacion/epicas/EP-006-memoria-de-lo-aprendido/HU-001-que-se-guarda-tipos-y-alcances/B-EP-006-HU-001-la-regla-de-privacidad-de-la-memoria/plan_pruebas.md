# Plan de Pruebas — Fase `B-EP-006-HU-001-la-regla-de-privacidad-de-la-memoria`   ·   `[CAPA 3]`

---

## 1. Introducción

### 1.1 Propósito

Comprobar que la regla que el criterio transversal de privacidad pedía **existe, está bien formada y está clasificada**.

### 1.2 Alcance

**Dentro:** que la regla no existiera antes, que cumpla el molde del capítulo `20`, y que quede dicho qué mitad de ella un programa no puede comprobar.

**Fuera:** construir esa comprobación, y limpiar la memoria que ya existe.

### 1.3 Documentos de referencia

- [HU-001](../HU-001-que-se-guarda-tipos-y-alcances.md)
- [Resultado de la fase A](../A-EP-006-HU-001-retrodocumentar-que-se-guarda-y-con-que-alcance/resultado_pruebas.md)
- El [checklist del estándar](../../../../../base/20-meta-reglas/checklist.md)

---

## 2. Elementos a probar

| Elemento | Por qué entra |
|---|---|
| Que la regla no existiera | Si existía, esto no era escribir sino enlazar |
| El molde de la regla nueva | Una regla mal formada no rige: la primera discusión es sobre su forma |
| Su clasificación | Una regla sin decir si es comprobable queda a la espera de un programa que nadie va a escribir |

---

## 3. Estrategia de pruebas

De ejecución sobre el propio estándar, en seco: `validar.py metareglas` comprueba el molde, el identificador, las dependencias y la clasificación.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- La decisión del usuario de que la regla se escriba, y dónde.

### 4.2 Criterios de salida

- `validar.py metareglas` sin incumplimientos.
- `validar.py versionado` sin fallas.
- El cuerpo de la regla dentro del molde, medido.

### 4.3 Criterios de suspensión y reanudación

Si el checklist diera ❌ en alguna fila, la regla se corrige antes de cerrar. Firmar el checklist sin aplicarlo es lo que le pasó a `04·S18`.

---

## 5. Matriz de trazabilidad

| CA | Caso |
|---|---|
| Transversal · Privacidad | CP-001, CP-002, CP-003 |

---

## 6. Casos de prueba

### CP-001 — La regla no existía

| Campo | Valor |
|---|---|
| **Tipo** | De análisis, ejecutado |
| **Cómo** | Buscar dato personal, credencial, clave y secreto en `13·DOC5` |
| **Resultado esperado** | Cero menciones |

### CP-002 — La regla nueva cumple su molde

| Campo | Valor |
|---|---|
| **Tipo** | De ejecución |
| **Prioridad** | **Crítica** |
| **Cómo** | `python validadores/validar.py metareglas` |
| **Resultado esperado** | Sin incumplimientos |

### CP-003 — El versionado queda consistente

| Campo | Valor |
|---|---|
| **Tipo** | De ejecución |
| **Cómo** | `python validadores/validar.py versionado` |
| **Resultado esperado** | Cero fallas |

---

## 7. Datos y ambientes de prueba

El propio repositorio. Ninguna prueba usa datos personales ni credenciales, que es lo que la regla prohíbe.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Filas del checklist en ❌ | **0** |
| Caracteres del cuerpo | 320 o menos |

---

## 15. Aprobación

Alcance y sitio de la regla aprobados por el usuario el 2026-08-30.
