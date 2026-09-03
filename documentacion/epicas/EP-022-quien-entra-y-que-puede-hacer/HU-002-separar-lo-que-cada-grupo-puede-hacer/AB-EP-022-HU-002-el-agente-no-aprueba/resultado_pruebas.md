# Resultado de Pruebas — Fase `AB-EP-022-HU-002-el-agente-no-aprueba`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**. Lo que se iba a probar está en el [plan_pruebas.md](plan_pruebas.md).

---

## 1. Identificación de la ejecución

| Campo | Valor |
|---|---|
| **Fase** | `AB-EP-022-HU-002-el-agente-no-aprueba` |
| **Fecha de ejecución** | 2026-09-01 |
| **Ejecutor** | Ing. José Dúmar Jiménez Ruíz |
| **Ambiente** | La máquina del usuario · Windows · carpetas temporales |
| **Versión del estándar** | 37.2.1 |

---

## 2. Resumen ejecutivo

**El agente no aprueba, y una cuenta que no existe se rechaza.** Los tres criterios cumplen.

**Y lo que se cerró acá es el mismo hueco que `EP-017` vino a tapar, un nivel más abajo.** Aquella épica arregló que una aprobación escrita a mano dijera quién sin decir sobre qué texto. Pero su propia orden aceptaba `--quien "cualquier cosa"`: seguía diciendo quién **sin probarlo**. Hoy `quien` es una cuenta con permiso.

---

## 3. Casos ejecutados

| Caso | Qué comprobó | Resultado |
|---|---|---|
| CP-003 | Dos grupos y no cuatro · el usuario todo · el agente ninguna · al día dos veces | ✅ |
| CP-004 | **El agente no aprueba · el nombre inventado se rechaza · cero aprobaciones tras los rechazos** | ✅ |

**10 pruebas nuevas.** Ninguna quedó en rojo al cerrar.

---

## 4. Defectos encontrados

**Ninguno en esta fase.**

---

## 5. Cobertura de los criterios de aceptación

| CA | Caso | Concepto |
|---|---|---|
| CA-01 · El agente no aprueba ni publica ni deroga | CP-003 y CP-004 | ✅ Cumple |
| CA-02 · El rechazo dice qué permiso falta | CP-004 | ✅ Cumple |
| CA-03 · Una cuenta que no existe se rechaza | CP-004 | ✅ Cumple |

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
| La plataforma | 610 | ✅ En verde |
| El estándar | 733 | ✅ En verde |
| Los validadores | 32 | ✅ Sin fallas |

---

## 8. Lo que esta ejecución NO comprueba

- **A quien pueda editar la base o el código.** Estos permisos los comprueba la plataforma, no el sistema operativo.
- **Si los dos grupos alcanzan.** Hoy sí; el día que entre alguien más, la tabla se revisa.
