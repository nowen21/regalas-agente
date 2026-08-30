# Resultado de Pruebas — Fase `D-EP-005-HU-003-el-ca-03-se-vuelve-a-medir`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `D-EP-005-HU-003-el-ca-03-se-vuelve-a-medir` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-29 |
| **Ciclo** | 1 |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** **CA-03 se cumple hoy**, comprobado ejecutándolo.
Lo que la fase `A-EP-005-HU-003-retrodocumentar-el-disparo-al-escribir` declaró en rojo el 2026-08-17 **era cierto
entonces**: el disparo corría en el momento y callaba con lo que no le tocaba, pero **todo avisaba**: nada distinguía el hallazgo grave del que solo informa. Lo resolvió después `B-EP-005-HU-003-el-hallazgo-grave-detiene`, y hasta hoy nadie
había vuelto a mirarlo.

| Métrica | Meta | Real |
|---|---|---|
| Casos ejecutados | 2 de 2 | 2 de 2 |
| **Casos comprobados leyendo en vez de corriendo** | 0 | **0** |

---

## 3. Resultado por caso

### CP-001 — El criterio se cumple hoy

**Cómo se ejecutó.** El enganche de escritura se corre **dos veces**, con un documento que deja un enlace roto y con uno sano. Las dos respuestas tienen que ser distintas: 2 y 0.

**Qué salió:** el enlace roto devuelve 2 y el documento sano devuelve 0

**Resultado: pasa.**

### CP-002 — La medición no se da por buena de más

Comprobar solo el caso grave no dice nada: un enganche que devuelve 2 siempre también lo pasaría, y detendría el trabajo en cada edición hasta que alguien lo apague.

**Resultado: pasa.** La medición está escrita de forma que el caso bueno solo no
alcanza para dar verde.

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Por qué esta fase existe, y no bastaba con anotarlo

El veredicto de la fase `A-EP-005-HU-003-retrodocumentar-el-disparo-al-escribir` **no se toca**: fue cierto el día que se
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
- La fase que hizo el trabajo: `B-EP-005-HU-003-el-hallazgo-grave-detiene`
