# Plan de Pruebas — Fase `B-EP-006-HU-006-se-lleva-todo-y-el-almacen-queda-vacio`   ·   `[CAPA 3]`

---

## 1. Introducción

### 1.1 Propósito

Comprobar el CA-01, el almacén local queda vacío con la decisión del usuario aplicada, ejecutándolo.

### 1.2 Alcance

**Dentro:** el criterio y su contraprueba.

**Fuera:** los otros criterios de la historia, que ya estaban en verde.

### 1.3 Documentos de referencia

- [HU-006](../HU-006-sacar-del-almacen-local.md)
- [Resultado de la fase A](../A-EP-006-HU-006-retrodocumentar-el-vaciado-del-almacen-local/resultado_pruebas.md)

---

## 2. Elementos a probar

| Elemento | Por qué entra |
|---|---|
| El criterio, con la decisión aplicada | Es lo que la fase viene a cerrar |
| Su contraprueba | Sin ella, el criterio pasaría con cualquier cosa |

---

## 3. Estrategia de pruebas

De ejecución. Nada se afirma leyendo el código.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- La decisión del usuario, escrita.

### 4.2 Criterios de salida

- El criterio pasa, y la contraprueba también.
- Ninguna prueba de la clase queda marcada como fallo esperado.

### 4.3 Criterios de suspensión y reanudación

Si la contraprueba fallara, la fase se detiene: significaría que aplicar la
decisión rompió algo que ya funcionaba.

---

## 5. Matriz de trazabilidad

| CA | Caso |
|---|---|
| CA-01, el almacén local queda vacío | CP-001 |

---

## 6. Casos de prueba

### CP-001 — Se lleva todo, y el almacén queda vacío

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-01, el almacén local queda vacío |
| **Tipo** | De ejecución |
| **Prioridad** | **Crítica** |
| **Resultado esperado** | Que lo ejecutado coincida con lo que la decisión dice que debe pasar, y que la contraprueba siga en pie |

---

## 7. Datos y ambientes de prueba

Lo que la propia prueba arma y borra. Ninguna credencial real (`00·N6`).

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Casos comprobados leyendo en vez de corriendo | **0** |
| Pruebas marcadas como fallo esperado | **0** |

---

## 15. Aprobación

Alcance aprobado el 2026-08-30, con la decisión del usuario.
