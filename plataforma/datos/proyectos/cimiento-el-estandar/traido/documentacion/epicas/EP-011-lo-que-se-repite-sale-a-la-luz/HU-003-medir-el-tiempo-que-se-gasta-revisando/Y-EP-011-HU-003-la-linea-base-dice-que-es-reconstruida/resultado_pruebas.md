# Resultado de Pruebas — Fase `Y-EP-011-HU-003-la-linea-base-dice-que-es-reconstruida`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**. Lo que se iba a probar está en el [plan_pruebas.md](plan_pruebas.md).

---

## 1. Identificación de la ejecución

| Campo | Valor |
|---|---|
| **Fase** | `Y-EP-011-HU-003-la-linea-base-dice-que-es-reconstruida` |
| **Fecha de ejecución** | 2026-09-01 |
| **Ejecutor** | Ing. José Dúmar Jiménez Ruíz |
| **Ambiente** | La máquina del usuario · Windows · carpetas temporales |
| **Versión del estándar** | 37.2.1 |

---

## 2. Resumen ejecutivo

**El tiempo de revisión se mide solo, de las horas que ya están escritas, y la línea base dice siempre que es reconstruida.** Los dos criterios cumplen.

**Medido contra el histórico real: 1615 revisiones, 144 horas y una mediana de 99 segundos** — y todo dentro de **un solo mes**. Con un mes no hay contra qué comparar, y el módulo **se niega a hacerlo** en vez de inventar un porcentaje.

La parte que más costó de esta fase no fue el cálculo: fue la frase que dice lo que el cálculo no puede. La medición inicial debió tomarse antes de empezar y no se tomó, y ninguna reconstrucción la reemplaza.

---

## 3. Casos ejecutados

| Caso | Qué comprobó | Resultado |
|---|---|---|
| CP-001 | El hueco, los dos mensajes seguidos, el sin hora y el «si» de dos segundos | ✅ |
| CP-002 | **La base es la más vieja, viene marcada, y la comparación lo dice** | ✅ |
| CP-003 | Las cuatro horas se descartan y se cuentan; la hora sí cuenta | ✅ |
| CP-004 | Con un mes no se compara · sin nada no se devuelve cero · con dos sí | ✅ |

**14 pruebas nuevas.** Ninguna quedó en rojo al cerrar.

---

## 4. Defectos encontrados

**Ninguno en esta fase.** Lo que quedó es una **restricción declarada**, no un defecto: la medición inicial no existe.

---

## 5. Cobertura de los criterios de aceptación

| CA | Caso | Concepto |
|---|---|---|
| CA-01 · Hay una línea base contra la cual comparar | CP-002 | ✅ Cumple, **con la advertencia de que es reconstruida** |
| CA-02 · Medir no obliga a anotar nada | CP-001 | ✅ Cumple |

**2 de 2.**

---

## 6. Concepto

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 2 de 2 |
| **Defectos abiertos aceptados** | Ninguno. Queda una restricción declarada: la medición inicial no existe |

---

## 7. Las dos baterías completas

| Batería | Pruebas | Resultado |
|---|---|---|
| La plataforma | 552 | ✅ En verde |
| El estándar | 733 | ✅ En verde |
| Los validadores | 32 | ✅ Sin fallas |

---

## 8. Lo que esta ejecución NO comprueba

- **Que la línea base sea comparable con el proyecto antes de empezar.** No lo es, y no hay cómo hacerla serlo.
- **Si el tiempo bajó porque el estándar sirvió.** Bajar puede ser eso, o mensajes más cortos, o costumbre.
