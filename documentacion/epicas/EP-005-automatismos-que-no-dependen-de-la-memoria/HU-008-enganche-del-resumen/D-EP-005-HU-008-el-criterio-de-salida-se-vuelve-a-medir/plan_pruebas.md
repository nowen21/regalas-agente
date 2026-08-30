# Plan de Pruebas — Fase `D-EP-005-HU-008-el-criterio-de-salida-se-vuelve-a-medir`   ·   `[CAPA 3]`

---

## 1. Introducción

### 1.1 Propósito

Comprobar que **el criterio de salida**, que la fase `A-EP-005-HU-008-enganche-del-resumen` dejó en rojo el
2026-08-22, **hoy se cumple** — ejecutándolo, no leyéndolo.

### 1.2 Alcance

**Dentro:** el criterio que quedó en rojo, y su contraprueba.

**Fuera:** los demás criterios de la historia, que ya estaban en verde; y los
otros cuatro rojos, cada uno con su medición.

### 1.3 Documentos de referencia

- [HU-008](../HU-008-enganche-del-resumen.md)
- [Resultado de la fase roja](../A-EP-005-HU-008-enganche-del-resumen/resultado_pruebas.md)
- El medidor: `historico-chat/scripts/2026-08-29/medir-los-cinco-rojos.py`

---

## 2. Elementos a probar

| Elemento | Por qué entra |
|---|---|
| Criterio de salida · la comprobación en una sesión real | Es lo que quedó en rojo |
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
| Criterio de salida · la comprobación en una sesión real | CP-001, CP-002 |

---

## 6. Casos de prueba

### CP-001 — El criterio se cumple hoy

| Campo | Valor |
|---|---|
| **HU / CA** | HU-008 / el criterio de salida |
| **Tipo** | De ejecución |
| **Prioridad** | Alta |
| **Cómo** | Lo medible se ejecuta: que el enganche esté colgado en `.claude/settings.json`, y que la sesión real haya dejado su resumen con la línea del índice apuntándole después de renombrarla. La mitad manual la atestigua esa sesión. |
| **Resultado esperado** | Que el criterio se cumpla, con su evidencia impresa |

### CP-002 — La medición no se da por buena de más

| Campo | Valor |
|---|---|
| **HU / CA** | HU-008 / el criterio de salida, contraprueba |
| **Tipo** | Que **no** pase |
| **Prioridad** | **Crítica** |
| **Cómo** | Este es el único de los cinco cuyo criterio **un programa no puede firmar solo**: pide una sesión real. Por eso la medición dice qué comprobó y qué atestigua la transcripción, en vez de dar las dos cosas por iguales. |
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
