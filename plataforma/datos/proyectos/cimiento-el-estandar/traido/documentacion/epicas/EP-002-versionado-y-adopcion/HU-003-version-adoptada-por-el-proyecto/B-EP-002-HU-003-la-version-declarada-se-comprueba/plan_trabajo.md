# Plan de Trabajo — Fase B-EP-002-HU-003-la-version-declarada-se-comprueba (módulo Programas de comprobación)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. Se escribe **antes** de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas` de esta misma fase; lo que quedó hecho, en el `funcionalidad_implementada.md` del cierre.

---

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-002-HU-003-la-version-declarada-se-comprueba` |
| **Épica** | `EP-002` |
| **HU** | `HU-003` |
| **Módulo** | Programas de comprobación |
| **Fecha apertura** | 2026-08-22 |
| **Rama** | `main` |

**ORIGEN:** 📝 **Modifica fase.** Cierra en rojo lo que la fase A de esta misma historia dejó al ejecutarse el 2026-08-22, anotado entonces en el [pendiente 82](../../../../../pendientes/hecho/la-version-adoptada-no-se-comprueba-contra-nada.md).

---

## 1. Objetivo y alcance

**El problema.** La versión que un proyecto declaraba no se comprobaba contra nada. Un número inventado pasaba, y **si era mayor que la vigente apagaba el aviso de desfase**: la comprobación se apagaba sola, y el que la apagaba no se enteraba. Y el historial de adopciones que el instalador escribe nunca se comparaba con lo declarado.

**Lo que entra:**

- Que la versión declarada exista en el registro de cambios del estándar.
- Que coincida con el último registro de `documentacion/versiones/`.
- Las dos fallan, y el mensaje nombra los dos números cuando difieren.

**Fuera de alcance:** no se decide qué hacer cuando las dos difieren: eso es del usuario, y lo que se pedía es que se vea. Y queda sin averiguar si el instalador escribe el registro sin actualizar la declaración, que explicaría el caso de shopnest-mesa.

---

## 2. Análisis previo — línea base verificada

**Comprobado sobre casos reales antes de dejarlo.** Una copia temporal declarando `99.9.9` ahora falla diciendo que esa versión no existe. Y shopnest-mesa, sin tocarlo, falla por lo segundo: declara `27.2.0` y su historial dice `28.0.0`, los dos del 2026-08-20. Esa contradicción llevaba dos días sin que nadie la viera.

### 2.1 Archivos que se crean o modifican

- `validadores/version.py`
- `validadores/tests/test_la_version_adoptada_se_comprueba.py`

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Las versiones se leen del registro de cambios, no de `VERSION` | Comparar contra la vigente | `VERSION` dice cuál es la última; la pregunta es si el número declarado existió alguna vez |
| Primero que exista, después que coincida | Las dos a la vez, sin orden | Mientras un número falso apague el aviso, cualquier proyecto puede quedar en silencio sin que se note |
| Cuando difieren, el mensaje nombra las dos | Decir cuál está mal | No se sabe cuál sin mirar, y un validador no opina |
| Sin registro legible no se acusa a nadie | Reportar igual | Es la lección del pendiente 81: una comprobación que no pudo leer su archivo no debe afirmar nada |

---

## 3. Verificación

Los casos del `resultado_pruebas` §2, y las suites que la fase toca. **La batería entera no**, que es lo que `02·F5` pone como INCORRECTO y que en esta misma jornada ya costó catorce minutos y once rojos que ya existían.

---

## 4. Reversión

Revertir el commit de la fase. Todo es aditivo sobre funciones que ya existían.

---

## 5. Reglas aplicadas

- [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), porque el pendiente baja a fase.
- [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md), por el alcance de la corrida.
- [`20·M19`](../../../../../base/20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md), porque se midió antes de dejar el criterio.
- `20·M10`, por la versión y el registro.

---

## 6. Cierre

**No se escribe acá.** Va en el `funcionalidad_implementada.md` de esta carpeta.
