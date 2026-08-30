# Resultado de Pruebas — Fase `C-EP-002-HU-004-el-ca-01-se-vuelve-a-medir`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `C-EP-002-HU-004-el-ca-01-se-vuelve-a-medir` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-29 |
| **Ciclo** | 1 |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** **CA-01 se cumple hoy**, comprobado ejecutándolo.
Lo que la fase `A-EP-002-HU-004-retrodocumentar-el-aviso-de-desfase` declaró en rojo el 2026-08-22 **era cierto
entonces**: el aviso **existía y decía lo que tenía que decir**, pero solo aparecía si alguien escribía el comando a mano: ni `sesion.py` ni `cargador.py` nombraban la versión, y el criterio dice «al abrir sesión». Lo resolvió después `B-EP-002-HU-004-el-aviso-llega-al-abrir-y-dice-que-cambio`, y hasta hoy nadie
había vuelto a mirarlo.

| Métrica | Meta | Real |
|---|---|---|
| Casos ejecutados | 2 de 2 | 2 de 2 |
| **Casos comprobados leyendo en vez de corriendo** | 0 | **0** |

---

## 3. Resultado por caso

### CP-001 — El criterio se cumple hoy

**Cómo se ejecutó.** Dos mitades, y hacen falta las dos: que el aviso **salga** (proyecto temporal que declara una versión vieja) y que el camino de la apertura **pase por él** (`hook_sesion` → `sesion.revisar` → `version.validar`).

**Qué salió:** sale, y `hook_sesion` -> `sesion.revisar` -> `version.validar`

**Resultado: pasa.**

### CP-002 — La medición no se da por buena de más

Que el aviso exista no era el problema: ya existía cuando se midió el rojo. Por eso la medición no se da por buena con ver el texto; comprueba el eslabón que faltaba.

**Resultado: pasa.** La medición está escrita de forma que el caso bueno solo no
alcanza para dar verde.

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Por qué esta fase existe, y no bastaba con anotarlo

El veredicto de la fase `A-EP-002-HU-004-retrodocumentar-el-aviso-de-desfase` **no se toca**: fue cierto el día que se
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
- La fase que hizo el trabajo: `B-EP-002-HU-004-el-aviso-llega-al-abrir-y-dice-que-cambio`
