# Plan de Pruebas — Fase `B-EP-001-HU-003-la-clave-dentro-de-una-frase-no-se-tapa`   ·   `[CAPA 3]`

---

## 1. Introducción

### 1.1 Propósito

Comprobar el CA-02, la clave no queda en claro con la decisión del usuario aplicada, ejecutándolo.

### 1.2 Alcance

**Dentro:** el criterio y su contraprueba.

**Fuera:** los otros criterios de la historia, que ya estaban en verde.

### 1.3 Documentos de referencia

- [HU-003](../HU-003-nucleo-que-no-se-sobrescribe.md)
- [Resultado de la fase A](../A-EP-001-HU-003-retrodocumentar-el-nucleo-blindado/resultado_pruebas.md)

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
| CA-02, la clave no queda en claro | CP-001 |

---

## 6. Casos de prueba

### CP-001 — Qué tapa y qué no, ejecutado

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-02, la clave no queda en claro |
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
