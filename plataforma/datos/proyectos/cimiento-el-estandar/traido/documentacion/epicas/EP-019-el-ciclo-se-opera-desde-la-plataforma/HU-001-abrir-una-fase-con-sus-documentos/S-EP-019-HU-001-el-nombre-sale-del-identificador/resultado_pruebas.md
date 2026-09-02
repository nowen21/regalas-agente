# Resultado de Pruebas — Fase `S-EP-019-HU-001-el-nombre-sale-del-identificador`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**. Lo que se iba a probar está en el [plan_pruebas.md](plan_pruebas.md).

---

## 1. Identificación de la ejecución

| Campo | Valor |
|---|---|
| **Fase** | `S-EP-019-HU-001-el-nombre-sale-del-identificador` |
| **Fecha de ejecución** | 2026-09-01 |
| **Ejecutor** | Ing. José Dúmar Jiménez Ruíz |
| **Ambiente** | La máquina del usuario · Windows · carpetas temporales |
| **Versión del estándar** | 37.2.1 |

---

## 2. Resumen ejecutivo

**Una fase se abre con sus cinco documentos, y el nombre lo pone la plataforma.** Los tres criterios cumplen.

Lo que no se ve en un número: **la fase se define por aquello a lo que se niega**. Sin historia no se abre, y sobre una carpeta que ya existe no escribe nada.

---

## 3. Casos ejecutados

| Caso | Qué comprobó | Resultado |
|---|---|---|
| CP-001 | Sin historia no se abre · con ella sí · el proyecto sin conectar se dice distinto | ✅ |
| CP-002 | **Abrir dos veces no toca lo escrito** · los cinco documentos con su molde · queda registrado | ✅ |
| CP-003 | El nombre coincide con los que ya existen · tildes y eñes bajadas · el título vacío se rechaza | ✅ |

**12 pruebas nuevas.** Ninguna quedó en rojo al cerrar.

---

## 4. Defectos encontrados

**Ninguno en esta fase.**

---

## 5. Cobertura de los criterios de aceptación

| CA | Caso | Concepto |
|---|---|---|
| CA-01 · Los cinco documentos con el molde | CP-002 | ✅ Cumple |
| CA-02 · Sin historia no se abre | CP-001 | ✅ Cumple |
| CA-03 · El nombre sale del identificador | CP-003 | ✅ Cumple |

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

- **Si los moldes son cómodos de llenar.** La ficha advierte que es donde más se nota; las pruebas usan moldes de mentiras.
- **Si la fase que se abrió hacía falta.** Eso lo decide quien la abre.
