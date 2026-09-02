# Plan de Pruebas — Fase `C-EP-004-HU-003-el-transversal-de-errores-se-vuelve-a-medir`   ·   `[CAPA 3]`

---

## 1. Introducción

### 1.1 Propósito

Comprobar que **el transversal de errores**, que la fase `A-EP-004-HU-003-retrodocumentar-el-formato-del-hallazgo` dejó en rojo el
2026-08-17, **hoy se cumple** — ejecutándolo, no leyéndolo.

### 1.2 Alcance

**Dentro:** el criterio que quedó en rojo, y su contraprueba.

**Fuera:** los demás criterios de la historia, que ya estaban en verde; y los
otros cuatro rojos, cada uno con su medición.

### 1.3 Documentos de referencia

- [HU-003](../HU-003-formato-del-hallazgo.md)
- [Resultado de la fase roja](../A-EP-004-HU-003-retrodocumentar-el-formato-del-hallazgo/resultado_pruebas.md)
- El medidor: `historico-chat/scripts/2026-08-29/medir-los-cinco-rojos.py`

---

## 2. Elementos a probar

| Elemento | Por qué entra |
|---|---|
| Transversal de errores · un `.md` ilegible no tumba la corrida | Es lo que quedó en rojo |
| La contraprueba del mismo criterio | Una medición que solo mira el caso bueno da verde sobre cualquier cosa |

---

## 3. Estrategia de pruebas

**De ejecución.** Se corre el criterio contra carpetas temporales que el propio
medidor crea y borra. Nada se afirma leyendo código.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- La fase roja y su resultado, leídos.
- El medidor, escrito y corriendo.

### 4.2 Criterios de salida

- El criterio sale **CUMPLE** al ejecutarlo.
- La contraprueba también.

### 4.3 Criterios de suspensión y reanudación

**Suspensión:** si la medición sale NO CUMPLE, **esta fase no se escribe**. El
criterio de suspensión vive dentro del guion, no en la buena voluntad de quien
lo corre.

---

## 5. Matriz de trazabilidad

| CA | Caso |
|---|---|
| Transversal de errores · un `.md` ilegible no tumba la corrida | CP-001, CP-002 |

---

## 6. Casos de prueba

### CP-001 — El criterio se cumple hoy

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / el transversal de errores |
| **Tipo** | De ejecución |
| **Prioridad** | Alta |
| **Cómo** | Una carpeta con dos archivos: uno con bytes que no son UTF-8 y otro con dos rayas largas en prosa. La corrida tiene que terminar en 0, sin volcado, **y seguir contando las dos marcas del legible**. |
| **Resultado esperado** | Que el criterio se cumpla, con su evidencia impresa |

### CP-002 — La medición no se da por buena de más

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / el transversal de errores, contraprueba |
| **Tipo** | Que **no** pase |
| **Prioridad** | **Crítica** |
| **Cómo** | No basta con que no se caiga. Un programa que se traga el error y deja de mirar el resto también «no se cae», y sería peor: diría cero marcas sobre un árbol sin revisar. |
| **Resultado esperado** | Que la medición distinga el caso bueno del malo |

---

## 7. Datos y ambientes de prueba

Carpetas temporales. Ningún proyecto real se toca, y ninguna prueba usa
credenciales (`00·N6`).

---

## 8. Herramientas

`historico-chat/scripts/2026-08-29/medir-los-cinco-rojos.py`, que imprime la
evidencia caso por caso y devuelve distinto de cero si alguno sigue en rojo.

---

## 9. Gestión de defectos

Un NO CUMPLE no es un defecto de esta fase: es el rojo que sigue vivo. La fase
no se escribe y la historia se queda como está.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Casos ejecutados | 2 de 2 |
| **Casos comprobados leyendo en vez de corriendo** | **0** |

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Acción |
|---|---|
| Declarar cumplido lo que no se ejecutó | El medidor imprime la evidencia de cada caso |
| Medir sobre un proyecto real y cambiarle el estado | Todo va en carpetas temporales |

---

## 15. Aprobación

El molde se aprobó **una sola vez** para las cinco fases, y este plan lo dice de
frente: pedir cinco aprobaciones de un texto idéntico convierte la puerta en
trámite, y una puerta que es trámite deja de mirar.
