# Resultado de Pruebas — Fase `R-EP-009-HU-002-la-auditoria-se-puede-preguntar`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**. Lo que se iba a probar está en el [plan_pruebas.md](plan_pruebas.md).

---

## 1. Identificación de la ejecución

| Campo | Valor |
|---|---|
| **Fase** | `R-EP-009-HU-002-la-auditoria-se-puede-preguntar` |
| **Fecha de ejecución** | 2026-09-01 |
| **Ejecutor** | Ing. José Dúmar Jiménez Ruíz |
| **Ambiente** | La máquina del usuario · Windows · base de pruebas |
| **Versión del estándar** | 37.2.1 |

---

## 2. Resumen ejecutivo

**La auditoría ya se puede preguntar.** Los tres criterios cumplen, y con esta fase **`EP-009` queda completa**: la primera mitad registra, esta consulta.

**El caso de borde salió a la luz probando, no leyendo.** La fecha se guarda como texto, y un rango armado con el `hasta` tal cual **deja por fuera el último día entero**: todo lo registrado después de la medianoche de ese día queda invisible. Es decir, justo lo más reciente, que es lo que uno busca.

---

## 3. Casos ejecutados

| Caso | Qué comprobó | Resultado |
|---|---|---|
| CP-001 | Los tres filtros, juntos y por separado · el orden · los tipos sacados de lo registrado | ✅ |
| CP-002 | **Un registro de las once de la noche del último día entra** | ✅ |
| CP-003 | Sin coincidencias se dice, y se distingue de una falla | ✅ |
| CP-004 | La respuesta trae cuántos y en cuántos segundos · avisa si recortó | ✅ |

**14 pruebas nuevas.** Ninguna falló.

---

## 4. Defectos encontrados

| # | Qué pasó | Severidad | Estado |
|---|---|---|---|
| 1 | **El rango dejaba por fuera el último día completo.** La fecha es texto con la hora pegada, así que comparar contra el `hasta` tal cual corta a la medianoche | **Crítica** | **Corregido**, y con prueba propia (CP-002) |

---

## 5. Cobertura de los criterios de aceptación

| CA | Caso | Concepto |
|---|---|---|
| CA-01 · Los tres filtros | CP-001 | ✅ Cumple |
| CA-02 · Sin coincidencias se dice | CP-003 | ✅ Cumple |
| CA-03 · El tiempo medido | CP-004 | ✅ Cumple |

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

- **Un año de registros de verdad.** El CA-03 pide menos de un segundo con ese volumen; **se midió con lo que hay y el número que salió es el que está escrito**, no una promesa. Cuando la auditoría real acumule un año, hay que volver a medir.
- **Que lo registrado sea completo.** Eso lo garantiza la fase `D`, no esta.
