# Resultado de Pruebas — Fase `O-EP-017-HU-003-editar-quita-la-aprobacion-y-no-borra-la-historia`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**. Lo que se iba a probar está en el [plan_pruebas.md](plan_pruebas.md).

---

## 1. Identificación de la ejecución

| Campo | Valor |
|---|---|
| **Fase** | `O-EP-017-HU-003-editar-quita-la-aprobacion-y-no-borra-la-historia` |
| **Fecha de ejecución** | 2026-09-01 |
| **Ejecutor** | Ing. José Dúmar Jiménez Ruíz |
| **Ambiente** | La máquina del usuario · Windows · carpetas temporales |
| **Versión del estándar** | 37.2.1 |

---

## 2. Resumen ejecutivo

**Las dos preguntas de la fase salieron bien.** Editar un documento aprobado **le quita la aprobación**, y **la aprobación anterior sigue ahí**.

Lo que la fase agrega y no se ve en un número: **un documento que ya no está también caduca**. Es el caso que se olvida, porque nadie edita lo que borró.

---

## 3. Casos ejecutados

| Caso | Qué comprobó | Resultado |
|---|---|---|
| CP-003 | Sin tocar sigue aprobado · editado caduca · borrado caduca · se dice cuánto cambió | ✅ |
| CP-004 | Al aprobar de nuevo quedan las dos, y manda la última | ✅ |

**6 pruebas nuevas.** Ninguna falló.

---

## 4. Defectos encontrados

**Ninguno en esta fase.**

---

## 5. Cobertura de los criterios de aceptación

| CA | Caso | Concepto |
|---|---|---|
| CA-01 · Editar quita la aprobación | CP-003 | ✅ Cumple |
| CA-02 · Se dice cuánto cambió | CP-003 | ✅ Cumple |
| CA-03 · La anterior no se borra | CP-004 | ✅ Cumple |

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

- **Si el cambio importaba.** Se sabe que el texto cambió y cuánto; no si lo que cambió altera lo que se autorizó. Eso lo mira una persona, y para eso avisa.
- **Arreglar una coma caduca la aprobación.** Está declarado en el plan y se acepta: una aprobación responde por el texto exacto.
