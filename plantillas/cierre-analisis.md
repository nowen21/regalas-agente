# Cierre de análisis — «módulo» «tema»   ·   `[CAPA 3]`

> Consolida un análisis persistido (`13·DOC8`): qué se preguntó, qué se decidió, qué quedó. Se crea al terminar un análisis (`analisis/<...>.md` de `DOC6` · exploraciones · auditorías). Ruta canónica: `analisis/<modulo>-YYYY-MM-DD-cierre.md`. Reemplaza los `«…»` y borra esta caja.

---

## 0. Referencia

| Campo | Valor |
|---|---|
| **Análisis original** | [enlace al `analisis/<...>.md`] |
| **Módulo** | «…» |
| **Fecha de cierre** | AAAA-MM-DD |
| **Prompt vivo del módulo** | [enlace] |

---

## 1. Tabla de trazabilidad — pregunta/hallazgo → decisión

> Una fila por cada pregunta abierta o hallazgo detectado durante el análisis.

| Pregunta / hallazgo | Decisión tomada | Estado | Gap generado (si aplica) |
|---|---|---|---|
| (frase original) | (respuesta del usuario o decisión de diseño) | resuelta / diferida / descartada | `[gap-N]` → §Qué falta del prompt vivo |

---

## 2. Cierre

- **Banner en el análisis original** — agregar al inicio del `analisis/<...>.md`:
  `> Cerrado en <ruta-de-este-cierre> — consultar allí el estado vigente de cada decisión.`
- **Registro en el prompt vivo** — agregar a su `## Historial de análisis`:
  `YYYY-MM-DD · <tema> · <ruta-a-este-cierre>`.
- **Gaps generados** — cada `[gap-N]` queda en la §Qué falta del prompt vivo, listo para una fase futura (`DOC12` ORIGEN).
