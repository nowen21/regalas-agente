# Resultado de Pruebas — Fase `D-EP-005-HU-008-el-criterio-de-salida-se-vuelve-a-medir`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `D-EP-005-HU-008-el-criterio-de-salida-se-vuelve-a-medir` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-29 |
| **Ciclo** | 1 |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** **el criterio de salida se cumple hoy**, comprobado ejecutándolo.
Lo que la fase `A-EP-005-HU-008-enganche-del-resumen` declaró en rojo el 2026-08-22 **era cierto
entonces**: los siete criterios de aceptación quedaron cubiertos y las métricas dieron por encima de la meta; lo que faltaba era **la corrida manual en una sesión de verdad**, y la fase prefirió esperar antes que darse por buena. Lo resolvió después `la sesión `2026-08-28-plantilla-manual-instalacion``, y hasta hoy nadie
había vuelto a mirarlo.

| Métrica | Meta | Real |
|---|---|---|
| Casos ejecutados | 2 de 2 | 2 de 2 |
| **Casos comprobados leyendo en vez de corriendo** | 0 | **0** |

---

## 3. Resultado por caso

### CP-001 — El criterio se cumple hoy

**Cómo se ejecutó.** Lo medible se ejecuta: que el enganche esté colgado en `.claude/settings.json`, y que la sesión real haya dejado su resumen con la línea del índice apuntándole después de renombrarla. La mitad manual la atestigua esa sesión.

**Qué salió:** colgado, y la sesion real dejo resumen e indice coherentes tras renombrar

**Resultado: pasa.**

### CP-002 — La medición no se da por buena de más

Este es el único de los cinco cuyo criterio **un programa no puede firmar solo**: pide una sesión real. Por eso la medición dice qué comprobó y qué atestigua la transcripción, en vez de dar las dos cosas por iguales.

**Resultado: pasa.** La medición está escrita de forma que el caso bueno solo no
alcanza para dar verde.

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Por qué esta fase existe, y no bastaba con anotarlo

El veredicto de la fase `A-EP-005-HU-008-enganche-del-resumen` **no se toca**: fue cierto el día que se
escribió, y reescribirlo borraría el rastro de que el criterio estuvo en rojo.

Pero **nadie vuelve a mirar un rojo por su cuenta** (`S-061`). Sin una fase que
lo declare, la historia arrastra un «no cumple» que ya no existe, y quien lo lea
después va a buscar un trabajo que ya está hecho.

### 4.2 Rastros

Ninguno. Las carpetas temporales las borra el propio medidor, y no se tocó
ningún proyecto real.

---

## 5. Defectos encontrados

**Ninguno.**

---

## 6. Evidencias

- El medidor: `historico-chat/scripts/2026-08-29/medir-los-cinco-rojos.py`
- El generador de esta fase: `historico-chat/scripts/2026-08-29/cerrar-los-cinco-rojos.py`
- La fase que hizo el trabajo: `la sesión `2026-08-28-plantilla-manual-instalacion``
