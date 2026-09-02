# Resultado de Pruebas — Fase `Z-EP-021-HU-001-lo-vacio-se-dice`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**. Lo que se iba a probar está en el [plan_pruebas.md](plan_pruebas.md).

---

## 1. Identificación de la ejecución

| Campo | Valor |
|---|---|
| **Fase** | `Z-EP-021-HU-001-lo-vacio-se-dice` |
| **Fecha de ejecución** | 2026-09-01 |
| **Ejecutor** | Ing. José Dúmar Jiménez Ruíz |
| **Ambiente** | La máquina del usuario · Windows · carpetas temporales |
| **Versión del estándar** | 37.2.1 |

---

## 2. Resumen ejecutivo

**Las cinco pantallas responden, lo vacío se dice y ningún «no se sabe» sale como cero.** Los tres criterios cumplen.

**Lo que costó no fue mostrar los datos: fue el caso vacío.** Son cinco, y cada uno se dice distinto — no tener fases no es lo mismo que no tener aprobaciones, y ninguna de las dos es un error de la plataforma. Un proyecto recién conectado ve las cinco pantallas vacías, y esa es la primera impresión que se lleva.

---

## 3. Casos ejecutados

| Caso | Qué comprobó | Resultado |
|---|---|---|
| CP-001 | Las cinco responden · se llega desde la ficha y la cabecera · 404 para el que no existe | ✅ |
| CP-002 | **Los cuatro casos vacíos, cada uno con su frase** | ✅ |
| CP-003 | «Sin datos» en el tablero · «no lo dice» en las fases · los tres estados separados | ✅ |
| CP-004 | El otro modelo · no son todos los documentos · «vencida» es de acá · lo de baja no se borra | ✅ |

**15 pruebas nuevas.** Ninguna quedó en rojo al cerrar.

---

## 4. Defectos encontrados

**Ninguno en el código.** Al escribir las rutas se vio a tiempo lo que habría sido el defecto de la fase: la ruta `proyecto/<id>/<que>/` de Proyectos se traga cualquier segmento, y las cinco nuevas puestas después de ella no habrían respondido nunca. Van antes, y hay una prueba que lo comprueba.

---

## 5. Cobertura de los criterios de aceptación

| CA | Caso | Concepto |
|---|---|---|
| CA-01 · Las cinco responden y se llega | CP-001 | ✅ Cumple |
| CA-02 · Lo vacío se dice | CP-002 | ✅ Cumple |
| CA-03 · Nada se escribe como cero | CP-003 | ✅ Cumple |

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

- **Si las pantallas se entienden.** Se comprueba que las frases estén, no que alguien las lea y sepa qué hacer.
- **Cómo se ven.** No hay ninguna prueba de diseño: se lee el texto que sale.
- **Los seis módulos que siguen sin pantalla.** Auditoría, Medición, Expediente, Reglas, Seguridad y Almacén.
