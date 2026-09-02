# Resultado de Pruebas — Fase `U-EP-019-HU-003-el-rechazo-dice-cual-puerta-falta`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**. Lo que se iba a probar está en el [plan_pruebas.md](plan_pruebas.md).

---

## 1. Identificación de la ejecución

| Campo | Valor |
|---|---|
| **Fase** | `U-EP-019-HU-003-el-rechazo-dice-cual-puerta-falta` |
| **Fecha de ejecución** | 2026-09-01 |
| **Ejecutor** | Ing. José Dúmar Jiménez Ruíz |
| **Ambiente** | La máquina del usuario · Windows · carpetas temporales |
| **Versión del estándar** | 37.2.1 |

---

## 2. Resumen ejecutivo

**Sin la puerta cumplida no se pasa, y el rechazo dice cuál falta.** Los tres criterios cumplen.

Lo que costó decidir no fue el código: fue **cuántas puertas comprobar**. La ficha advierte que *una puerta que estorba se termina saltando*, y trece puertas comprobadas se saltan todas. Son tres: las que dejan daño.

---

## 3. Casos ejecutados

| Caso | Qué comprobó | Resultado |
|---|---|---|
| CP-006 | Las dos puertas de estación, los tres veredictos, la que no opina, y las tres de un golpe | ✅ |

**7 pruebas nuevas.** Ninguna quedó en rojo al cerrar.

---

## 4. Defectos encontrados

**Ninguno en esta fase.**

---

## 5. Cobertura de los criterios de aceptación

| CA | Caso | Concepto |
|---|---|---|
| CA-01 · Sin plan aprobado no pasa | CP-006 | ✅ Cumple |
| CA-02 · Sin veredicto no cierra | CP-006 | ✅ Cumple |
| CA-03 · El rechazo nombra la puerta | CP-006 | ✅ Cumple |

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

- **Que la puerta se cumpla de verdad.** Comprueba que esté marcada; que lo marcado sea cierto lo responde una persona.
- **A alguien que se la salte a propósito.** El archivo se escribe a mano, y esto no lo impide.
