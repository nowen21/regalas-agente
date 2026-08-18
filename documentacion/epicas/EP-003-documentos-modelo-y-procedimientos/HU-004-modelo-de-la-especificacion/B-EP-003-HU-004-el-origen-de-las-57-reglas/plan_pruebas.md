# Plan de Pruebas — Fase B-EP-003-HU-004: el origen de las 57 reglas

| Campo | Valor |
|---|---|
| **Código** | PP-B-EP-003-HU-004 · **Versión** 1.0 · **Fecha** 2026-08-18 |
| **Aprobado por** | Pendiente — el usuario |

---

## 3. Estrategia

**Lo fácil es hacer callar al validador; lo que importa es que el origen sea cierto.** Un identificador puesto para que la comprobación pase es peor que ninguno: da por trazada una regla que nadie pidió. Los casos miran eso.

---

## 5. Matriz de trazabilidad

| Exigencia | Caso | Estado |
|---|---|---|
| Ninguna regla sin origen | [CP-001](#cp-001--el-validador-da-cero) | ☐ |
| El origen es el que el documento ya declaraba | [CP-002](#cp-002--el-origen-sale-del-propio-documento) | ☐ |
| El identificador lleva su enlace | [CP-003](#cp-003--cada-origen-lleva-su-enlace) | ☐ |
| No regresión | [CP-004](#cp-004--nada-de-lo-que-ya-estaba-deja-de-pasar) | ☐ |

---

## 6. Casos

### CP-001 — El validador da cero

`plantillas.reglas_sin_origen` sobre las dos especificaciones: 0 y 0.

### CP-002 — El origen sale del propio documento

Tomar tres reglas al azar y comprobar que la historia que declaran es la que su `### 4.N` ya decía.

> **Es el caso que separa trazar de tapar.** Un identificador inventado hace callar al validador y deja la regla igual de huérfana.

### CP-003 — Cada origen lleva su enlace

`validar.py estandar`, sin enlaces rotos ni citas sin enlazar.

### CP-004 — Nada de lo que ya estaba deja de pasar

Las dos suites.

---

## 12. Métricas

| Métrica | Meta |
|---|---|
| Reglas sin origen | **0** |
| Orígenes inventados | **0** |
| Reglas borradas | **0** — no es de esta fase |

Un solo concepto: **Cumple** o **No cumple**.
