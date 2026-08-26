# Resultado de Pruebas — Fase A-EP-005-HU-005-el-cambio-de-reglas-no-se-guarda-sin-version

**Para qué sirve este documento.** Registra qué se ejecutó y con qué resultado. El diseño de los casos está en el [plan_pruebas.md](plan_pruebas.md), que no se toca al ejecutar.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-005-HU-005-el-cambio-de-reglas-no-se-guarda-sin-version` |
| **HU** | [HU-005 Cambio de reglas con versión](../HU-005-cambio-de-reglas-con-version.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-22 |
| **Ejecutado por** | El agente, por la orden del usuario de resolver el [pendiente 59](../../../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md) |
| **Ambiente** | El repositorio del estándar en `main`, versión 31.5.0, Windows, Python 3.11 |

### 0.1 Las dos dudas que la detenían, y qué se hizo con ellas

| Duda | Decisión, y de dónde sale |
|---|---|
| ¿detiene o avisa? | **Detiene**, y no depende del tipo de cambio. Es la decisión 9 del pendiente 59, con su regla: detiene lo que se comprueba sin criterio, avisa lo que necesita juicio |
| ¿va después de HU-004 o esta crea el disparo? | **HU-004 ya creó el disparo** (el enganche del mensaje de commit) y esta se suma al que existe. Es la decisión 32 del mismo pendiente: dos enganches sobre el mismo momento se pisan |

**Y una tercera cosa que apareció al medir:** el disparo de esta comprobación no es el enganche del mensaje, sino el de `pre-commit`, que ya corre `validar.py versionado --preparados`. Sumarse ahí es exactamente lo que la decisión 32 pedía; escribir un enganche nuevo habría sido el segundo dueño del mismo momento.

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos |
|---|---:|---:|---:|---:|
| 1 | 4 del plan, 7 escritos | 7 | 7 | 0 |

Se escribieron tres casos más de los que el plan pedía: el commit vacío, varios archivos de norma a la vez, y el rechazo que distingue cuál de los dos falta.

## 2. Ejecución caso por caso

| Caso | Qué comprueba | Resultado |
|---|---|---|
| CP-001 · sin entrada ni subida no pasa; con las dos, sí | el corazón del CA-01 | ✅ Aprobado, y detiene con FALLA |
| CP-002 · el cambio mezclado se detecta igual | una regla entre archivos que no son norma | ✅ Aprobado |
| CP-003 · el cambio que no toca reglas no nota nada | el CA-02, y **el caso que decide** | ✅ Aprobado |
| CP-004 · el rechazo dice qué falta | pedir las dos cosas cuando falta una sería mentir | ✅ Aprobado: si falta solo el registro, no nombra `VERSION` |
| CP-005 · varios archivos de norma se cuentan | el mensaje no nombra solo el primero | ✅ Aprobado |
| CP-006 · un commit vacío no revienta | límite | ✅ Aprobado |
| CP-007 · no regresión de la batería | `comun.leer` y `versionado` los usan todos | ✅ Aprobado: 366 pruebas, una falla y es del pendiente 48, excluido por el usuario |

## 3. Lo que se construyó

**[`validadores/guardian_version.py`](../../../../../validadores/guardian_version.py)**, dentro de `validar.py versionado --preparados`, que es lo que el `pre-commit` ya ejecuta. Mira qué archivos entran al commit: si alguno vive en `base/` o `plantillas/`, exige `VERSION` y `CHANGELOG.md` en el mismo commit.

**Lo que no comprueba, y queda escrito** en [su contrato](../../../../../validadores/docs/guardian_version.md): si la entrada del registro dice la verdad, y si el tipo de versión es el correcto. Las dos exigen leer.

## 4. Defectos encontrados

**Ninguno.** Y una observación sobre el alcance: la comprobación mira **lo preparado**, así que un cambio guardado con `--no-verify` la esquiva. Eso no es un defecto de esta fase: un enganche local nunca es una garantía, y por eso `20·M10` sigue siendo la regla y esto solo su recordatorio mecánico.

## 5. Veredicto de la fase

**Cumple.** Siete casos de siete.

| Criterio | Veredicto |
|---|---|
| CA-01 · un cambio de reglas sin versión no se guarda | ✅ Cumple |
| CA-02 · un cambio que no toca reglas no se ve afectado | ✅ Cumple |
| RNF · el resto de los cambios no nota nada | ✅ Cumple |
