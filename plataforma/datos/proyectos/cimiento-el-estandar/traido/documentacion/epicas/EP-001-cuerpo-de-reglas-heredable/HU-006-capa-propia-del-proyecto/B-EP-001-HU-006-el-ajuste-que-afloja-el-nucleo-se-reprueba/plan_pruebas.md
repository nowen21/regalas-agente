# Plan de Pruebas — Fase `B-EP-001-HU-006-el-ajuste-que-afloja-el-nucleo-se-reprueba`   ·   `[CAPA 3]`

---

## 1. Introducción

### 1.1 Propósito

Comprobar el CA-03 de la HU-006: **un ajuste del proyecto que contradiga el núcleo no aplica.** El criterio quedó en rojo el 2026-08-17 sin haberse podido ejecutar.

### 1.2 Alcance

**Dentro:** una regla `P` que declara aflojar una `[BLINDADA]`, y una que declara endurecerla.

**Fuera:** la contradicción que el proyecto no declare, y los defectos `D-01` y `D-02` de la fase `A`.

### 1.3 Documentos de referencia

- [HU-006](../HU-006-capa-propia-del-proyecto.md)
- [Resultado de la fase A](../A-EP-001-HU-006-retrodocumentar-la-capa-del-proyecto/resultado_pruebas.md), defecto `D-03`
- `20·M7` y `20·M16`

---

## 2. Elementos a probar

| Elemento | Por qué entra |
|---|---|
| La regla `P` que afloja una `[BLINDADA]` | Es el caso que el CA-03 prohíbe |
| La regla `P` que endurece una `[BLINDADA]` | Es el caso que el CA-03 **permite**, y el que hace útil la capa propia |

---

## 3. Estrategia de pruebas

De ejecución, sobre carpetas temporales. La decisión 35 del pendiente 59 prohíbe provocarlo en un proyecto real, y es lo que dejó este criterio sin medir.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- La fase `A` y su defecto `D-03`, leídos.

### 4.2 Criterios de salida

- El catálogo que afloja produce **una falla que nombra la regla y la marca `[BLINDADA]`**.
- El catálogo que endurece produce **cero hallazgos**.

### 4.3 Criterios de suspensión y reanudación

Si el caso malo hubiera pasado sin reclamo desde el principio, no había nada que construir y la fase se habría cerrado declarando. Se provocó primero, y falló.

---

## 5. Matriz de trazabilidad

| CA | Caso |
|---|---|
| CA-03 | CP-001, CP-002 |

---

## 6. Casos de prueba

### CP-001 — La regla que afloja una blindada se reprueba

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-03 |
| **Tipo** | De ejecución |
| **Prioridad** | Alta |
| **Cómo** | Un `.agente/reglas-proyecto.md` temporal con `P1` cuyo respaldo dice «afloja `N2`» |
| **Resultado esperado** | Una falla que nombre `N2` y la marca `[BLINDADA]` |

### CP-002 — La regla que endurece una blindada pasa

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-03, contraprueba |
| **Tipo** | Que **no** pase |
| **Prioridad** | **Crítica** |
| **Cómo** | Un `P1` cuyo respaldo dice «concreta `N4`» |
| **Resultado esperado** | Cero hallazgos |

**La crítica es la segunda.** Una comprobación que reprobara cualquier mención de una regla del núcleo cazaría al tramposo y volvería inservible la capa propia, que existe para concretar.

---

## 7. Datos y ambientes de prueba

Carpetas temporales creadas y borradas por la propia prueba. Ninguna credencial, ni real ni inventada (`00·N6`).

---

## 8. Herramientas

`python -m unittest pruebas.ElAjusteDelProyectoNoAflojaElNucleo`

---

## 9. Gestión de defectos

Un fallo en CP-002 es más grave que uno en CP-001: significa que la comprobación rompe el uso legítimo.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Casos ejecutados | 2 de 2 |
| Casos comprobados leyendo en vez de corriendo | **0** |

---

## 15. Aprobación

Alcance aprobado el 2026-08-30.
