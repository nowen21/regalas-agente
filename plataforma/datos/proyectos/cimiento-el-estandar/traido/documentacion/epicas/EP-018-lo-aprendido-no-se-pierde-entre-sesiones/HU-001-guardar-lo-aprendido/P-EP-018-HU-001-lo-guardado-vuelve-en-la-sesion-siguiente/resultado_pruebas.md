# Resultado de Pruebas — Fase `P-EP-018-HU-001-lo-guardado-vuelve-en-la-sesion-siguiente`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**. Lo que se iba a probar está en el [plan_pruebas.md](plan_pruebas.md).

---

## 1. Identificación de la ejecución

| Campo | Valor |
|---|---|
| **Fase** | `P-EP-018-HU-001-lo-guardado-vuelve-en-la-sesion-siguiente` |
| **Fecha de ejecución** | 2026-09-01 |
| **Ejecutor** | Ing. José Dúmar Jiménez Ruíz |
| **Ambiente** | La máquina del usuario · Windows · carpetas temporales |
| **Versión del estándar** | 37.2.1 |

---

## 2. Resumen ejecutivo

**Lo guardado vuelve, y guardar no pisa.** Los tres criterios cumplen.

Lo que se midió sobre la carpeta real, sin tocarla: **los recuerdos que ya hay se leen y se separan bien entre vigentes y dados de baja**. No hubo que migrar ni reescribir ninguno, porque el formato de `01·C19` ya estaba ahí.

---

## 3. Casos ejecutados

| Caso | Qué comprobó | Resultado |
|---|---|---|
| CP-001 | Vuelve · no se mezcla · el de baja no sale entre los vigentes | ✅ |
| CP-002 | **Guardar con un nombre existente avisa y no pisa** | ✅ |
| CP-003 | Un tema sin recuerdos se dice con palabras | ✅ |

**6 pruebas nuevas.** Ninguna falló.

---

## 4. Defectos encontrados

**Ninguno en esta fase.**

---

## 5. Cobertura de los criterios de aceptación

| CA | Caso | Concepto |
|---|---|---|
| CA-01 · Lo guardado vuelve | CP-001 | ✅ Cumple |
| CA-02 · No se mezclan proyectos | CP-001 | ✅ Cumple |
| CA-03 · Un tema vacío se dice | CP-003 | ✅ Cumple |

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

- **Que lo guardado siga siendo cierto.** El módulo guarda y devuelve; **nada revisa si un recuerdo envejeció**. Está declarado como riesgo aceptado.
- **Que lo guardado sea lo que valía la pena guardar.** Eso lo decide quien escribe.
