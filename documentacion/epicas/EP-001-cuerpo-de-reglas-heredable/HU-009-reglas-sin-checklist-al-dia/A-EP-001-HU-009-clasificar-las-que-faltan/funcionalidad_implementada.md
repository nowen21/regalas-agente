# Funcionalidad implementada — Fase «A-EP-001-HU-009-clasificar-las-que-faltan»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito **qué quedó hecho**, para que quien llegue después no tenga que deducirlo del código ni del historial.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-001-HU-009-clasificar-las-que-faltan` |
| **Épica / HU** | [EP-001](../../epica.md) · [HU-009](../HU-009-reglas-sin-checklist-al-dia.md) |
| **Versión del estándar** | 23.1.0 → **23.1.1** (PARCHE) |
| **Fecha de cierre** | 2026-08-16 |

---

## 1. Qué quedó funcionando

**Ninguna regla del estándar queda fuera del registro de lo validable.** De 33 sin clasificar a **cero**, y el total de hallazgos del validador de meta-reglas bajó exactamente 33 — de 269 a 236.

Cómo quedaron repartidas:

| Grupo | Cuántas | Dónde quedaron |
|---|---:|---|
| Conducta del agente (`C2`–`C16`) | 15 | 🔴 no validables. **Ya lo estaban**, escritas como rango |
| Despliegue (`DP1`–`DP8`) | 8 | 5 🟡 contra proyecto real · 3 🔴 |
| Observabilidad (`OB1`–`OB6`) | 6 | 3 🟡 contra proyecto real · 3 🔴 |
| `20·M15` y `02·F12` | 2 | ✅ ya construidas, y no figuraban |
| `02·F4` y `09·G9` | 2 | 🟡, con qué le falta a cada una |

---

## 2. Qué se tocó

| Archivo | Qué |
|---|---|
| [`validadores/reglas-validables.md`](../../../../../validadores/reglas-validables.md) | Las 33 filas, dos secciones nuevas y el conteo del principio |
| [`HU-009-reglas-sin-checklist-al-dia.md`](../HU-009-reglas-sin-checklist-al-dia.md) | La fase en §8, la tarea marcada y la bitácora |
| [`pendientes/19-...`](../../../../../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md) | Al día con lo que sigue faltando. **Sigue abierto** |
| [`CHANGELOG.md`](../../../../../CHANGELOG.md) · `VERSION` | 23.1.1 |

**Ninguna regla cambió de texto.** Esta fase clasifica, no reescribe.

---

## 3. Cómo se comprueba

```
python validadores/validar.py estandar --raiz .
```

El validador de meta-reglas no reporta ninguna regla sin clasificar.

---

## 4. Lo que se supo, y que cambia el diagnóstico

**Quince de las 33 ya estaban clasificadas.** El registro decía `C1–C17` y el programa busca cada identificador literal, así que quince reglas de conducta figuraban como sin clasificar desde el 2026-08-05.

Entonces la tercera deuda del pendiente 19 no era «33 reglas que nadie clasificó»: eran **18 de verdad** y **15 escritas de una forma que el validador no puede leer**.

**La lección es del propio registro:** un documento que alimenta a un programa se escribe **como el programa lee**. El rango ahorraba cuatro líneas y costaba quince hallazgos que nadie sabía si eran reales — y un hallazgo del que se duda se termina ignorando, junto con los que sí eran ciertos.

---

## 5. Qué falta de esta historia

La HU-009 tiene tres criterios y esta fase cubre **uno**. Siguen abiertos:

- **Las siete publicadas en «no cumple»** (`F4`, `F5`, `F12`, `M2`, `M4`, `M7`, `M8`). No lo decide el agente: corregirlas cambia lo que el estándar exige. Y `F12` tiene el texto congelado por decisión del usuario, así que ahí el camino sería legalizar la congelación en `M5`.
- **Las 121 sin bloque de checklist**, que es trabajo por capítulo.

**El pendiente 19 no se cierra.** Queda al día, diciendo qué se resolvió y qué no.
