# Plan de Pruebas — Fase B-EP-005-HU-001: la transcripción duplicada del 15

| Campo | Valor |
|---|---|
| **Código** | PP-B-EP-005-HU-001 · **Versión** 1.0 · **Fecha** 2026-08-18 |
| **Aprobado por** | Pendiente — el usuario |

---

## 3. Estrategia

**Se está borrando de un archivo que no se puede reescribir.** El histórico es transcripción literal, así que el único modo de fallar que importa es **quitar algo que se dijo**. Todos los casos miran eso.

---

## 5. Matriz de trazabilidad

| Exigencia | Caso | Estado |
|---|---|---|
| No se pierde ningún mensaje | [CP-001](#cp-001--todo-lo-que-se-quita-tiene-gemelo) | ☐ |
| Los que no tienen gemelo se quedan | [CP-002](#cp-002--los-que-no-tienen-gemelo-siguen-ahí) | ☐ |
| El archivo queda numerado seguido | [CP-003](#cp-003--numeración-seguida) | ☐ |
| Quien lo abra sabe qué horas puede creer | [CP-004](#cp-004--la-nota-advierte-de-las-horas) | ☐ |

**Cobertura:** 4 de 4 = 100%.

---

## 6. Casos

### CP-001 — Todo lo que se quita tiene gemelo

Cada bloque eliminado tiene otro, con la marca `<!-- agente: … -->`, cuyo texto es el mismo palabra por palabra.

> Es el caso que separa limpiar de borrar. Sin él, la instrucción del pendiente se lleva dieciséis mensajes.

### CP-002 — Los que no tienen gemelo siguen ahí

Los 16 bloques sin marca y sin pareja están en el archivo después de limpiar.

### CP-003 — Numeración seguida

De 1 a 48, sin saltos.

### CP-004 — La nota advierte de las horas

La cabecera dice que las horas no se pueden leer en orden y cuáles son del reloj.

---

## 12. Métricas

| Métrica | Meta |
|---|---|
| Mensajes del usuario perdidos | **0** |
| Bloques repetidos que quedan | **0** |

Un solo concepto: **Cumple** o **No cumple**.
