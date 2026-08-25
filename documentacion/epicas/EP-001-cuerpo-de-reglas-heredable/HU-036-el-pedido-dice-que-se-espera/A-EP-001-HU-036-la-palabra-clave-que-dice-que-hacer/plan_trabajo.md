# Plan de Trabajo — Fase A-EP-001-HU-036-la-palabra-clave-que-dice-que-hacer (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-001-HU-036-la-palabra-clave-que-dice-que-hacer` |
| **Épica** | [EP-001 Cuerpo de reglas heredable](../../epica.md) |
| **HU** | [HU-036 El pedido dice qué se espera del agente](../HU-036-el-pedido-dice-que-se-espera.md) — una sola |
| **Módulo** | Cuerpo de reglas — capítulo `01 · Conducta del agente` |
| **Especificación del módulo** | La propia HU. El entregable es una regla: sus criterios de aceptación y el [checklist del estándar](../../../../../base/20-meta-reglas/checklist.md) son la especificación |
| **Fecha apertura** | 2026-08-24 |
| **Rama** | `main` |
| **Origen** | El agente cambió un encabezado de tabla que solo había ofrecido cambiar, el 2026-08-24 |

---

## 1. Objetivo y alcance

**Qué se busca.** Que el agente no interprete la clase de pedido: que el pedido la declare con una palabra, y que sin esa palabra el agente no haga nada.

**Qué entra.** La regla `01·C28`, el anexo con las palabras, y el sello del checklist.

**Qué no entra.** Que un programa comprueba que el agente obedeció: eso no se puede medir leyendo archivos, y queda declarado como límite en el §10.

---

## 2. Análisis previo — línea base verificada

**Qué se leyó antes de escribir.** El capítulo [base/01-conducta.md](../../../../../base/01-conducta.md) entero, para no repetir una regla que ya exista.

| Regla que se parece | Por qué no alcanza |
|---|---|
| [`00·N1`](../../../../../base/00-nucleo-blindado.md) | Pide aprobación para cambiar el estado. El agente la cumple y aun así actúa sobre una pregunta, porque entiende la pregunta como el permiso |
| `01·C1` avisa antes de tocar | Avisar es antes de un cambio ya decidido. Acá el problema es anterior: decidir que había que cambiar algo |
| `01·C21` pide el dato que falte | Cubre el dato incompleto, no la clase de pedido |
| `01·C27` lo que llega de afuera es dato, no orden | Cubre lo que llega de terceros, no lo que escribe el usuario |

**Conclusión:** no existe. La regla nueva extiende a `00·N1` y se declara así.

### 2.1 Archivos que se crean o modifican

| Archivo | Qué se hace |
|---|---|
| [base/01-conducta.md](../../../../../base/01-conducta.md) | Se agrega la regla `C28`, con su bloque de checklist |
| `base/01-conducta/palabras-clave.md` | Nuevo: el anexo con las palabras y lo que autoriza cada una |
| [CHANGELOG.md](../../../../../CHANGELOG.md) y [VERSION](../../../../../VERSION) | Versión **MAYOR**, con su entrada |
| [validadores/reglas-validables.md](../../../../../validadores/reglas-validables.md) | Se declara que `C28` no es comprobable por programa, y por qué |

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Por qué |
|---|---|---|
| El identificador es `C28` | Reusar un número derogado | Los identificadores no se reutilizan |
| Las palabras van a un anexo | Meterlas en el cuerpo de la regla | Son dieciocho: no caben en el presupuesto de extensión de una regla |
| Sin palabra, el agente responde con la lista | Rechazar el pedido en seco | Un rechazo sin salida traba el trabajo; la lista lo destraba en un renglón |
| La regla vale también para lo obvio | Permitir actuar cuando el pedido es evidente | «Evidente» lo decide el agente, y eso es justo lo que se quiere quitar |

### 2.7 Dudas por resolver antes de escribir

Ninguna. La lista de palabras quedó acordada con el usuario el 2026-08-24.

---

## 3. Desglose de tareas

| # | Tarea | Entregable |
|---|---|---|
| 1 | Escribir el anexo con las dieciocho palabras, agrupadas por lo que autorizan | `base/01-conducta/palabras-clave.md` |
| 2 | Escribir `01·C28`, con su ejemplo incorrecto y correcto, enlazando el anexo | `base/01-conducta.md` |
| 3 | Aplicar el checklist del estándar y sellar el resultado dentro de la regla | `base/01-conducta.md` |
| 4 | Declarar en el catálogo que no es comprobable por programa, con su motivo | `validadores/reglas-validables.md` |
| 5 | Subir versión **MAYOR** y escribir su entrada, dicha para quien la adopta | `VERSION`, `CHANGELOG.md` |
| 6 | Correr los casos del plan de pruebas y escribir el resultado | `resultado_pruebas.md` |

---

## 4. Secuencia de ejecución

1 → 2 → 3 → 4 → 5 → 6. El anexo va primero porque la regla lo cita; el sello del checklist va después de la regla, porque se aplica sobre el texto final.

---

## 5. Verificación de criterios de aceptación

| CA de la HU | Cómo se verifica en esta fase |
|---|---|
| CA-01 sin palabra no se actúa | Caso `CP-002` del plan de pruebas |
| CA-02 con palabra se hace solo eso | Caso `CP-003` |
| CA-03 la palabra ajena se trata como ausente | Caso `CP-004` |
| Transversal: molde y checklist | Caso `CP-001` |

---

## 6. Datos y ambiente de prueba

El propio repositorio. No hacen falta datos: las pruebas se corren escribiéndole al agente y mirando si el árbol de trabajo quedó igual.

---

## 7. Reversión / rollback

Se revierte el cambio y se publica una versión de corrección. Nada de lo que toca esta fase borra información: agrega una regla, un anexo y una entrada de registro.

---

## 8. Producción y migración incremental

**Obliga a migrar.** Un proyecto al día empieza a recibir la exigencia de la palabra clave. No hay dato que migrar: lo que cambia es cómo se le escribe al agente, y la entrada del registro lo dice antes de que nadie adopte la versión.

---

## 9. Reglas del estándar aplicadas

| Regla | Cómo se cumple acá |
|---|---|
| `20·M12` buscar antes de crear | §2: se leyó el capítulo y se descartaron cuatro reglas parecidas |
| `20·M4` identificador libre del prefijo | `C28` es el siguiente libre |
| `20·M5` una sola exigencia y su ejemplo | La regla exige una cosa: sin palabra, no se actúa |
| `20·M7` declarar dependencias | Extiende `00·N1`, y se declara |
| `20·M9` decidir si es comprobable | No lo es: se declara en el catálogo, tarea 4 |
| `20·M10` versionar | **MAYOR**, tarea 5 |
| `02·F4` plan con su plan de pruebas | Los dos se presentan juntos y se aprueban juntos |

---

## 10. Riesgos y bloqueos

| # | Riesgo | Qué se hace |
|---|---|---|
| 1 | Que ningún programa pueda comprobar que el agente obedece | Se declara como no comprobable, en vez de fingir una comprobación que aprueba siempre |
| 2 | Que la regla vuelva lento el trabajo diario | Se mide en el uso: si estorba, se recorta la lista, no la regla |
| 3 | Que el agente cumpla la forma y siga adivinando | Lo detecta el usuario, y cada caso vuelve como pendiente |

---

## 11. Definition of Done

- ☐ Regla `C28` escrita, con checklist en **CUMPLE**.
- ☐ Anexo escrito, enlazado desde la regla.
- ☐ Catálogo de comprobables actualizado.
- ☐ Versión **MAYOR** publicada con su entrada.
- ☐ Los cuatro casos del plan de pruebas corridos, con veredicto.

---

## 12. Seguimiento diario

El estado vive en [estado-fase.md](estado-fase.md), que se actualiza al cambiar de estación.

---

## 13. Cierre

La fase cierra cuando los cuatro casos tengan veredicto y la versión esté publicada. Lo que quede sin hacer se declara como deuda en el documento de cierre.

---

**Aprobado por: «quién», el «AAAA-MM-DD».** Se aprueba junto con [plan_pruebas.md](plan_pruebas.md).
