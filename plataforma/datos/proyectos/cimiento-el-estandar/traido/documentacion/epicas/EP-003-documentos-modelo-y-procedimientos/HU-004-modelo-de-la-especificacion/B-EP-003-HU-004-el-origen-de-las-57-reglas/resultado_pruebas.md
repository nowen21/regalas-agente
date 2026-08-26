# Resultado de Pruebas — Fase B-EP-003-HU-004: el origen de las 57 reglas

| Campo | Valor |
|---|---|
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md) v1.0 · **Ciclo** 1 · **Fecha** 2026-08-18 |

---

## 1. Casos

| Caso | Veredicto |
|---|---|
| CP-001 · el validador da cero | ✅ **Pasa** — 0 y 0 |
| CP-002 · el origen sale del propio documento | ✅ **Pasa** |
| CP-003 · cada origen lleva su enlace | ✅ **Pasa** |
| CP-004 · no regresión | ✅ **Pasa** — `tests/` 187 · `pruebas.py` 357 · `estandar` limpio |

**4 de 4.**

---

## 2. Qué se midió

**57 reglas sin origen, no las 31 que decía el pendiente.** Se contaron el 2026-08-16; desde entonces se escribieron más.

| Especificación | Antes | Después |
|---|---:|---:|
| `documentacion/automatismos/spec.md` | 30 | **0** |
| `documentacion/documentos-modelo/spec.md` | 27 | **0** |

---

## 3. El origen no hubo que inventarlo

**Ya estaba escrito, una vez por sección.** Cada `### 4.N` de las dos especificaciones declara en qué fase se escribió, con su enlace. Lo que faltaba era **bajarlo de la sección a la regla**, que es donde un programa lo busca.

> Es la diferencia entre una regla huérfana y una regla cuya procedencia estaba a tres líneas de distancia y nadie la había puesto donde se lee.

---

## 4. Lo que **no** se hizo, y es lo que más importa · [`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md)

El pendiente daba tres salidas por regla: escribirle el origen, subirla a la historia que corresponda, **o borrarla porque no hace falta**. Y decía: *«alguna de esas seguramente no la pidió nadie»*.

**Esta fase hizo la primera para las 57.** Ninguna se borró.

**Que una regla tenga procedencia no la vuelve necesaria**, y el pendiente lo dice mejor que esto: la tercera salida es la razón de ser de todo el ejercicio. Pero borrar una regla vigente quita algo del estándar, y esa decisión no es del agente.

**Queda medible:** hoy las 57 declaran de qué historia bajan, así que revisarlas una por una ya no obliga a averiguar de dónde salieron — solo a decidir si siguen haciendo falta.

---

## 5. Veredicto

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **Defectos abiertos aceptados** | uno: cuáles de las 57 no las pidió nadie |
| **Ciclos** | 1 |
