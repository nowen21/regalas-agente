# Resultado de Pruebas — Fase `V-EP-008-HU-005-lo-obligatorio-no-se-apaga`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**. Lo que se iba a probar está en el [plan_pruebas.md](plan_pruebas.md).

---

## 1. Identificación de la ejecución

| Campo | Valor |
|---|---|
| **Fase** | `V-EP-008-HU-005-lo-obligatorio-no-se-apaga` |
| **Fecha de ejecución** | 2026-09-01 |
| **Ejecutor** | Ing. José Dúmar Jiménez Ruíz |
| **Ambiente** | La máquina del usuario · Windows · carpetas temporales |
| **Versión del estándar** | 37.2.1 |

---

## 2. Resumen ejecutivo

**Lo opcional se enciende y se apaga por proyecto, y lo obligatorio no se puede apagar.** Los tres criterios cumplen.

**Y el defecto que apareció era el que ponía en riesgo la funcionalidad entera.** La primera versión buscaba `*opt-in*` en todo el archivo, y eso contagia a todas las reglas que lo acompañan: daba **52 reglas opcionales** en vez de 49, y entre ellas **`02·F0`**, que es la cadena completa del flujo de trabajo. Con esa lista, la plataforma habría dejado apagar la cadena entera. **No se ve en el número** —52 y 49 se parecen—: se ve leyendo la lista nombre por nombre.

---

## 3. Casos ejecutados

| Caso | Qué comprobó | Resultado |
|---|---|---|
| CP-001 | De fábrica apagado · encender y apagar con fecha · sin filas repetidas | ✅ |
| CP-002 | **Apagar una obligatoria no se hace** · la desconocida también es obligatoria | ✅ |
| CP-003 | Lo de un proyecto no llega al otro · el que no configuró se dice así | ✅ |
| CP-004 | **La palabra suelta no contagia · la cabecera sí rige · la marca vale para su regla** | ✅ |

**14 pruebas nuevas.** Ninguna quedó en rojo al cerrar.

---

## 4. Defectos encontrados

| # | Qué pasó | Severidad | Estado |
|---|---|---|---|
| 1 | **Buscar `*opt-in*` en todo el archivo marcaba 52 reglas como opcionales**, entre ellas `02·F0`, la cadena del flujo de trabajo. También entraban `R7` y `R8`, que no son reglas sino los **ejemplos** con que el capítulo 20 explica cómo se escribe una | **Crítica** | **Corregido**, con cuatro pruebas propias |

---

## 5. Cobertura de los criterios de aceptación

| CA | Caso | Concepto |
|---|---|---|
| CA-01 · Se prende y se apaga | CP-001 | ✅ Cumple |
| CA-02 · Lo obligatorio no se apaga | CP-002 | ✅ Cumple |
| CA-03 · Cada proyecto recibe lo suyo | CP-003 | ✅ Cumple |

**3 de 3.**

---

## 6. Concepto

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 3 de 3 |
| **Defectos abiertos aceptados** | Ninguno |

---

## 7. Las dos baterías completas

| Batería | Pruebas | Resultado |
|---|---|---|
| La plataforma | 552 | ✅ En verde |
| El estándar | 733 | ✅ En verde |
| Los validadores | 32 | ✅ Sin fallas |

---

## 8. Lo que esta ejecución NO comprueba

- **Si apagar muchas reglas aleja dos proyectos.** Está en la ficha, y no lo mide ninguna prueba.
- **Si el estándar marcó bien lo opcional.** Se lee lo que está escrito; que esté bien marcado lo responde el capítulo 20.
