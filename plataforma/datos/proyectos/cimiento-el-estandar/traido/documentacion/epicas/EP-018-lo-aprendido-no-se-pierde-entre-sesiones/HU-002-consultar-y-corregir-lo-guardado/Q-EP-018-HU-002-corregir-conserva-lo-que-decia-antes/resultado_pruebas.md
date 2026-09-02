# Resultado de Pruebas — Fase `Q-EP-018-HU-002-corregir-conserva-lo-que-decia-antes`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**. Lo que se iba a probar está en el [plan_pruebas.md](plan_pruebas.md).

---

## 1. Identificación de la ejecución

| Campo | Valor |
|---|---|
| **Fase** | `Q-EP-018-HU-002-corregir-conserva-lo-que-decia-antes` |
| **Fecha de ejecución** | 2026-09-01 |
| **Ejecutor** | Ing. José Dúmar Jiménez Ruíz |
| **Ambiente** | La máquina del usuario · Windows · carpetas temporales |
| **Versión del estándar** | 37.2.1 |

---

## 2. Resumen ejecutivo

**Corregir conserva lo anterior y dar de baja no borra.** Los tres criterios cumplen.

Con esta fase **el módulo Memoria queda cerrado**, y con él la versión 4: 16 pruebas propias, ningún archivo borrado, ninguna entidad en la base.

---

## 3. Casos ejecutados

| Caso | Qué comprobó | Resultado |
|---|---|---|
| CP-004 | Buscar con coincidencias y sin ellas | ✅ |
| CP-005 | **Corregir deja el texto nuevo y el anterior, dos veces seguidas** | ✅ |
| CP-006 | **Dar de baja deja el archivo y lo saca de los vigentes** | ✅ |

**10 pruebas nuevas.** Ninguna falló.

---

## 4. Defectos encontrados

**Ninguno en esta fase.**

---

## 5. Cobertura de los criterios de aceptación

| CA | Caso | Concepto |
|---|---|---|
| CA-01 · Se busca por palabra | CP-004 | ✅ Cumple |
| CA-02 · Corregir conserva lo anterior | CP-005 | ✅ Cumple |
| CA-03 · Dar de baja no borra | CP-006 | ✅ Cumple |

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
| La plataforma | 473 | ✅ En verde |
| El estándar | 733 | ✅ En verde |
| Los validadores | 32 | ✅ Sin fallas |

---

## 8. Lo que esta ejecución NO comprueba

- **Que un recuerdo con muchas correcciones siga siendo legible.** Se probó con dos; uno real puede acumular más. Declarado y aceptado.
- **Que lo corregido sea más cierto que lo anterior.** El módulo conserva las dos versiones; cuál vale lo decide quien corrige.
