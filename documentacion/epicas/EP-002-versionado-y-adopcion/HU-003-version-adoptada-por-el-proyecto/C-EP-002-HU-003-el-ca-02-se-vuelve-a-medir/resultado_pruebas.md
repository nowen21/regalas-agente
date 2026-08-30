# Resultado de Pruebas — Fase `C-EP-002-HU-003-el-ca-02-se-vuelve-a-medir`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `C-EP-002-HU-003-el-ca-02-se-vuelve-a-medir` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-29 |
| **Ciclo** | 1 |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** **CA-02 se cumple hoy**, comprobado ejecutándolo.
Lo que la fase `A-EP-002-HU-003-retrodocumentar-la-version-adoptada` declaró en rojo el 2026-08-22 **era cierto
entonces**: `99.9.9` pasaba en silencio y, **por ser mayor que la vigente, apagaba el aviso de desfase**: declarar una versión falsa hacia adelante callaba la única comprobación que había. Lo resolvió después `B-EP-002-HU-003-la-version-declarada-se-comprueba`, y hasta hoy nadie
había vuelto a mirarlo.

| Métrica | Meta | Real |
|---|---|---|
| Casos ejecutados | 2 de 2 | 2 de 2 |
| **Casos comprobados leyendo en vez de corriendo** | 0 | **0** |

---

## 3. Resultado por caso

### CP-001 — El criterio se cumple hoy

**Cómo se ejecutó.** Se arma un proyecto de prueba en una carpeta temporal cuyo `CLAUDE.md` declara `99.9.9`, y se corre `version.validar` sobre él. Tiene que salir una **falla**, no un silencio.

**Qué salió:** el proyecto declara la v99.9.9, que no existe en el registro de cambios del estándar — mientras el número sea falso, el aviso de desfase no dice nada

**Resultado: pasa.**

### CP-002 — La medición no se da por buena de más

Se mide sobre una carpeta temporal y no sobre un proyecto real, como manda la decisión 35 del pendiente 59: tocar el `CLAUDE.md` de un proyecto vivo para probar es cambiarle el estado a alguien más.

**Resultado: pasa.** La medición está escrita de forma que el caso bueno solo no
alcanza para dar verde.

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Por qué esta fase existe, y no bastaba con anotarlo

El veredicto de la fase `A-EP-002-HU-003-retrodocumentar-la-version-adoptada` **no se toca**: fue cierto el día que se
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
- La fase que hizo el trabajo: `B-EP-002-HU-003-la-version-declarada-se-comprueba`
