# -*- coding: utf-8 -*-
"""Escribe el `funcionalidad_implementada.md` de las dos fases D.

Las dos cierran un rojo, pero por motivos distintos: el de EP-005-HU-001 fue
cierto y dejo de serlo; el de EP-003-HU-002 nunca lo fue.
"""
import io
import os

RAIZ = r"c:\Ing. Jose\ia\agente"

D5 = os.path.join(RAIZ, "documentacion", "epicas",
                  "EP-005-automatismos-que-no-dependen-de-la-memoria",
                  "HU-001-transcripcion-de-la-sesion",
                  "D-EP-005-HU-001-la-privacidad-ya-se-cumple-y-se-declara")
D3 = os.path.join(RAIZ, "documentacion", "epicas",
                  "EP-003-documentos-modelo-y-procedimientos",
                  "HU-002-modelos-del-encargo",
                  "D-EP-003-HU-002-el-veredicto-se-vuelve-a-medir-contra-su-criterio")


def escribir(carpeta, nombre, texto):
    with io.open(os.path.join(carpeta, nombre), "w",
                 encoding="utf-8", newline="\n") as f:
        f.write(texto)


CIERRE_5 = u"""# Funcionalidad implementada \u2014 Fase `D-EP-005-HU-001-la-privacidad-ya-se-cumple-y-se-declara` (m\u00f3dulo Enganches)   \u00b7   `[CAPA 3]`

## 0. Identificaci\u00f3n

| Campo | Valor |
|---|---|
| **Fase** (identificador \u00b7 `02\u00b7F12.6`) | `D-EP-005-HU-001-la-privacidad-ya-se-cumple-y-se-declara` |
| **M\u00f3dulo** | Enganches |
| **Especificaci\u00f3n del m\u00f3dulo** | No hay documento aparte. `02\u00b7F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-27 |
| **HU / CA cubiertas** | [HU-001](../HU-001-transcripcion-de-la-sesion.md): la exigencia transversal de **privacidad** |
| **Fecha de cierre** | 2026-08-27 |
| **Versi\u00f3n del est\u00e1ndar al cerrar** | `35.4.0` \u2014 **sin cambio**: no se toca c\u00f3digo |
| **Veredicto** | **Cumple**, copiado del \u00a72 del resultado |
| **Commit** | Pendiente de aprobaci\u00f3n del usuario |

---

## 1. Qu\u00e9 se implement\u00f3 \u2014 resumen

**Nada. Esta fase comprueba y declara.**

La fase [`A`](../A-EP-005-HU-001-retrodocumentar-la-transcripcion-de-la-sesion/resultado_pruebas.md) cerr\u00f3 en rojo el 2026-08-22 porque *\u00abnada enmascara\u00bb*, y **era cierto**. El enmascarado lo construy\u00f3 despu\u00e9s la [`HU-002`](../../HU-002-enmascarar-claves/) de esta misma \u00e9pica \u2014 que aquella fase ya nombraba como su destino.

Lo que faltaba era que **alguien volviera a mirarlo**. Nadie lo hace por su cuenta (`S-061`), y mientras tanto la historia arrastraba un \u00abno cumple\u00bb que ya no exist\u00eda.

| Antes | Ahora |
|---|---|
| La exigencia de privacidad, en rojo desde el 2026-08-22 | **Cumple**, comprobado ejecutando |

---

## 2. Trazabilidad  \u00b7  `13\u00b7DOC11`

### 2.1 Historia \u2192 implementaci\u00f3n

| \u00cdtem | Categor\u00eda | Ubicaci\u00f3n | Estado | Evidencia |
|---|---|---|---|---|
| Transversal \u00b7 Privacidad | servicio | `validadores/enmascarar.py`, llamado por `historico.py` | \u2705 | CP-001, CP-002, CP-003 |

### 2.2 Plan de trabajo \u2192 ejecuci\u00f3n

| Tarea | Estado | Evidencia |
|---|---|---|
| T-01 \u00b7 enmascara | \u2705 | Tres formas, tapadas |
| T-02 \u00b7 **no** enmascara de m\u00e1s | \u2705 | Cinco casos, intactos |
| T-03 \u00b7 est\u00e1 conectado | \u2705 | Las dos rutas, antes de escribir |
| T-04 \u00b7 el estado de la historia | \u2705 | \u2014 |
| T-05 \u00b7 declarar el veredicto | \u2705 | Este documento |

**Correspondencia:** 5 tareas, 5 con resultado.

**Archivos tocados que el plan no declaraba** (`02\u00b7F8`): ninguno.

---

## 3. Qu\u00e9 se prob\u00f3  \u00b7  `08` / `02\u00b7F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, ciclo 1 |
| **Suites ejecutadas** | Ninguna nueva: esta fase no cambia c\u00f3digo. Lo que verifica tiene sus pruebas en la `HU-002` |
| **Defectos abiertos** | Ninguno |

---

## 4. C\u00f3mo se usa / puntos de entrada  \u00b7  `13\u00b7DOC1`

Sin cambios. El enmascarado corre solo, dentro del enganche que escribe la transcripci\u00f3n.

---

## 5. Decisiones no obvias  \u00b7  `13\u00b7DOC5`

| Decisi\u00f3n | Por qu\u00e9 | Se\u00f1al |
|---|---|---|
| Una fase que **declara**, sin tocar la `A` | Aquel veredicto fue cierto. Reescribirlo borra el rastro de que la exigencia estuvo en rojo tres d\u00edas | `20\u00b7M11` |
| Se comprueba **ejecutando**, no leyendo | Existir e importarse no es tapar. Tres veces el mismo d\u00eda se afirm\u00f3 sobre lo que no se ejecut\u00f3 | `04\u00b7R4` |
| Se comprueba **que no tape de m\u00e1s** | Un enmascarador que tapa prosa se apaga, y entonces no tapa nada \u2014 y la casilla dir\u00eda que s\u00ed | `CP-002` |
| Se sigue la cadena hasta **quien escribe** | La exigencia habla de lo que queda escrito, no de lo que el m\u00f3dulo sabe hacer | `CP-003` |

---

## 6. Deuda t\u00e9cnica y pendientes generados

| Descripci\u00f3n | Estado al cerrar |
|---|---|
| La clave dicha **enteramente en prosa** sigue sin taparse | **Abierta y declarada** en la `HU-002`, con su motivo: el riesgo de tapar de m\u00e1s |
| Nadie vuelve a mirar un veredicto en rojo | **Abierta.** Es `S-061`, y esta fase es una de las dos que lo hizo a mano |

---

## 7. \u00cdndices y mapas actualizados  \u00b7  `13\u00b7DOC9` / `13\u00b7DOC13`

- [x] El `Estado` de la historia y su casilla transversal.
- [x] La \u00e9pica [EP-005](../../epica.md).
- [ ] `VERSION` y `CHANGELOG.md`: **no aplica**, no se toca `base/` ni `plantillas/`.

---

## 8. Despliegue \u2014 si aplica  \u00b7  `13\u00b7DOC4`

**Nada que desplegar.** Lo que cambia es que la historia deja de arrastrar un rojo que ya no existe.
"""

CIERRE_3 = u"""# Funcionalidad implementada \u2014 Fase `D-EP-003-HU-002-el-veredicto-se-vuelve-a-medir-contra-su-criterio` (m\u00f3dulo Documentos modelo)   \u00b7   `[CAPA 3]`

## 0. Identificaci\u00f3n

| Campo | Valor |
|---|---|
| **Fase** (identificador \u00b7 `02\u00b7F12.6`) | `D-EP-003-HU-002-el-veredicto-se-vuelve-a-medir-contra-su-criterio` |
| **M\u00f3dulo** | Documentos modelo |
| **Especificaci\u00f3n del m\u00f3dulo** | No hay documento aparte. `02\u00b7F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-27 |
| **HU / CA cubiertas** | [HU-002](../HU-002-modelos-del-encargo.md): el `CA-01` |
| **Fecha de cierre** | 2026-08-27 |
| **Versi\u00f3n del est\u00e1ndar al cerrar** | `35.4.0` \u2014 **sin cambio**: no se toca c\u00f3digo |
| **Veredicto** | **Cumple**, copiado del \u00a72 del resultado |
| **Commit** | Pendiente de aprobaci\u00f3n del usuario |

---

## 1. Qu\u00e9 se implement\u00f3 \u2014 resumen

**Nada. Esta fase vuelve a medir un criterio contra lo que el criterio pide.**

La fase [`A`](../A-EP-003-HU-002-retrodocumentar-los-modelos-del-encargo/resultado_pruebas.md) cerr\u00f3 con \u00abNo cumple\u00bb porque *\u00abel planteamiento de esta casa est\u00e1 vac\u00edo\u00bb*. **Su `CA-01` no pide eso**: pide que existan los tres modelos y que la cadena se recorra en los dos sentidos \u2014 y **la propia fase `A` midi\u00f3 eso y le dio verde**.

**Se reprob\u00f3 a s\u00ed misma por algo de al lado.**

| Antes | Ahora |
|---|---|
| \u00abNo cumple\u00bb, por un hueco que el criterio no menciona | **Cumple**: 0 fallas sobre 11 \u00e9picas y 119 historias |

**El hallazgo de la fase `A` no se descarta.** Que la casa no tuviera su planteamiento era cierto y val\u00eda; lo mal puesto era la factura. Y hoy **ni siquiera sigue abierto**.

---

## 2. Trazabilidad  \u00b7  `13\u00b7DOC11`

### 2.1 Historia \u2192 implementaci\u00f3n

| \u00cdtem | Categor\u00eda | Ubicaci\u00f3n | Estado | Evidencia |
|---|---|---|---|---|
| `CA-01` los tres modelos existen | documento | `plantillas/ciclo-vida-proyectos/` | \u2705 | CP-001 |
| `CA-01` y la cadena se recorre en los dos sentidos | servicio | `validar.py trazabilidad` sobre el \u00e1rbol real | \u2705 | CP-002 |

### 2.2 Plan de trabajo \u2192 ejecuci\u00f3n

| Tarea | Estado | Evidencia |
|---|---|---|
| T-01 \u00b7 los tres modelos | \u2705 | CP-001 |
| T-02 \u00b7 la cadena, **corrida** | \u2705 | CP-002, y el hallazgo del ciclo 1 |
| T-03 \u00b7 el hueco que la `A` se\u00f1al\u00f3 | \u2705 | CP-003 |
| T-04 \u00b7 declarar el veredicto | \u2705 | Este documento |

**Correspondencia:** 4 tareas, 4 con resultado.

**Archivos tocados que el plan no declaraba** (`02\u00b7F8`): **uno**, la tabla de `EP-001`, con **una fila**. Se par\u00f3, se report\u00f3, y el usuario ampli\u00f3 el alcance. Est\u00e1 en el \u00a74.1 del resultado.

---

## 3. Qu\u00e9 se prob\u00f3  \u00b7  `08` / `02\u00b7F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, ciclo 2 |
| **Suites ejecutadas** | Ninguna nueva: esta fase no cambia c\u00f3digo |
| **Defectos abiertos** | Ninguno. `DEF-01` corregido |

**El \u00fanico defecto no era de esta fase ni de la `A`:** `HU-036` no estaba en la tabla de `EP-001`, y lo mismo hab\u00eda pasado con dos historias de `EP-005` el mismo d\u00eda. Es `S-064`.

---

## 4. C\u00f3mo se usa / puntos de entrada  \u00b7  `13\u00b7DOC1`

```
python validadores/validar.py trazabilidad
```

Sin cambios. Es la comprobaci\u00f3n que ya exist\u00eda, corrida sobre el \u00e1rbol real.

---

## 5. Decisiones no obvias  \u00b7  `13\u00b7DOC5`

| Decisi\u00f3n | Por qu\u00e9 | Se\u00f1al |
|---|---|---|
| **Se corre, no se cita** | Apoyarse en la medici\u00f3n de la `A` habr\u00eda heredado su resultado de hace diez d\u00edas \u2014 y la falla de hoy habr\u00eda pasado invisible | `S-064` |
| El veredicto de la `A` **no se toca** | El error ense\u00f1a m\u00e1s que la conclusi\u00f3n. Es lo mismo que se decidi\u00f3 con `H-34` | `20\u00b7M11` |
| **El hallazgo se conserva**, y se dice d\u00f3nde deb\u00eda cobrarse | Era cierto y val\u00eda. Borrarlo por estar mal ubicado perder\u00eda algo \u00fatil | `S-063` |
| Se comprueba si el hueco **sigue abierto**, aunque no sea del `CA-01` | Decir \u00abya no aplica\u00bb sin mirarlo ser\u00eda el defecto del d\u00eda | `CP-003` |

---

## 6. Deuda t\u00e9cnica y pendientes generados

| Descripci\u00f3n | Estado al cerrar |
|---|---|
| Una historia se crea y nadie vuelve a la tabla de su \u00e9pica | **Las tres del d\u00eda, corregidas.** La detecci\u00f3n ya exist\u00eda y funcionaba: el problema es que su aviso convive con otros cuarenta y cuatro. Es `S-064` |
| Nadie vuelve a mirar un veredicto en rojo | **Abierta.** Es `S-061`, y esta fase es una de las dos que lo hizo a mano |

---

## 7. \u00cdndices y mapas actualizados  \u00b7  `13\u00b7DOC9` / `13\u00b7DOC13`

- [x] La tabla de [EP-001](../../../EP-001-cuerpo-de-reglas-heredable/epica.md), con la `HU-036`.
- [x] La \u00e9pica [EP-003](../../epica.md).
- [ ] `VERSION` y `CHANGELOG.md`: **no aplica**, no se toca `base/` ni `plantillas/`.

---

## 8. Despliegue \u2014 si aplica  \u00b7  `13\u00b7DOC4`

**Nada que desplegar.** Lo que cambia es que la historia deja de arrastrar un rojo que su criterio no sostiene.
"""

escribir(D5, "funcionalidad_implementada.md", CIERRE_5)
escribir(D3, "funcionalidad_implementada.md", CIERRE_3)
print("los dos cierres, escritos")
