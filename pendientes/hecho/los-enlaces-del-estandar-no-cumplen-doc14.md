# Pendiente · Los enlaces del estándar no cumplen su propia regla

**Estado:** cerrado 2026-08-18 · anotado 2026-08-14.

| | |
|---|---|
| **Historia de usuario** | [EP-004 · HU-005 — Comprobar los enlaces y las citas a reglas](../../documentacion/epicas/EP-004-comprobacion-automatica/HU-005-enlaces-y-citas/HU-005-enlaces-y-citas.md) — es la deuda de su RN-03, que es DOC14 palabra por palabra |

## El problema

[`13·DOC14`](../../base/13-documentacion/reglas/DOC14-enlaza-cada-md-con-ruta-legible-y-destino-relativo.md) pide que el texto de un enlace sea la ruta completa desde la raíz y el destino la ruta relativa. Al escribir el validador de ese formato aparecieron **354 enlaces** del propio estándar que no lo cumplen.

No son falsos positivos. Son enlaces cuyo texto dice el nombre del archivo pero no dónde vive: `[00-nucleo-blindado.md]` en vez de `[base/00-nucleo-blindado.md]`.

| Dónde | Cuántos |
|---|---|
| `prompts/` | 106 |
| `base/` | 45 |
| `historico-chat/` | 43 |
| `documentacion/` | 42 |
| `validadores/` | 40 |
| `notas/` | 30 |
| El resto | 48 |

## Qué falta

**1. Decidir el alcance.** Las transcripciones de `historico-chat/` se copian literales del chat, así que ahí el formato no aplica. Los de `prompts/` son palabras del usuario. Quedan unos 200 reales.

**2. Corregirlos.** Es mecánico: el validador ya dice, enlace por enlace, qué texto debería tener.

**3. Decidir si el validador entra en la corrida de todos los días.** Hoy se corre aparte, porque 354 avisos sepultan cualquier otra cosa.

## Lo que se arregló, y lo que la regla no había mirado — 2026-08-18

Fase [`B-EP-004-HU-005`](../../documentacion/epicas/EP-004-comprobacion-automatica/HU-005-enlaces-y-citas/B-EP-004-HU-005-el-texto-del-enlace-dice-donde-vive), veredicto **Cumple**.

**El punto 2 está hecho: lo arregla el programa.** `enlaces.reparar_formato()` reescribe el texto —nunca el destino— y corrió sobre **284 enlaces en 89 archivos**, sin romper ninguno.

**Pero la cuenta de este archivo estaba mal repartida, y eso es lo nuevo.**

| | Cuántos |
|---|---:|
| Total, fuera de transcripciones y de `prompts/` | **1031** — eran 354 el 2026-08-14 |
| **Vecino de la misma carpeta** | **747** |
| **Entre carpetas** — arreglados | **284** |

**Los 747 no son deuda: son un caso que la regla no miró.** [`13·DOC14`](../../base/13-documentacion/reglas/DOC14-enlaza-cada-md-con-ruta-legible-y-destino-relativo.md) pide la ruta desde la raíz *«para saber dónde vive sin abrirlo»*, y para el archivo de al lado ese propósito **ya está cumplido**: quien lee está parado ahí.

Se aplicó a los 1031 para verlo. Esto es lo que quedaba en la tabla de contenidos de una fase:

```
| [documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-009-reglas-sin-checklist-al-dia/E-EP-001-HU-009-las-que-solo-sobraban-de-largo/plan_trabajo.md](plan_trabajo.md) | Qué se va a hacer |
```

**132 caracteres de media para nombrar al vecino.** Se revirtieron los 347 archivos.

### La decisión que falta

**¿`DOC14` exceptúa al enlace de la misma carpeta?**

| Salida | Qué implica |
|---|---|
| **Sí** — se le agrega la excepción a la regla | Los 747 quedan bien como están. Es un cambio de `base/`, con su versión |
| **No** — la regla se aplica literal | Se corren los 747 con `reparar_formato(incluir_vecinos=True)`, y se acepta el texto largo |

**Mientras no se decida, el número no baja de 747** — y no por falta de trabajo.

### Y el punto 1 quedó resuelto en el camino

El alcance ya está en el programa, con su motivo escrito y un caso cada uno: las transcripciones del chat no, `prompts/` no —son palabras del usuario—, y el texto descriptivo tampoco, que la propia regla lo permite.

### Un punto ciego que apareció

``[`ruta`](destino)`` **no lo ve nadie**: `comun.enlaces()` borra los trozos entre comillas invertidas antes de buscar enlaces, y con eso el texto queda vacío. No es de esta fase —tocarlo cambia cómo se leen los enlaces en todo el repositorio— y quedó **declarado en un caso de prueba**, para que no se descubra dentro de un año contando por qué el número no llega a cero.

---

## El límite

El validador solo mira el enlace cuyo texto ya tiene forma de ruta. El de texto descriptivo no se toca: la propia regla lo permite.

## De acá nació [`02·F21`](../../base/02-flujo-de-trabajo/reglas/F21-un-incumplimiento-ya-identificado-no-se-repite-en-lo-nuevo.md)

Este pendiente se estaba usando como permiso. El 2026-08-14, con los 354 ya contados, los documentos escritos ese mismo día sumaron 122 incumplimientos nuevos de la misma familia: la deuda dejaba de ser deuda y pasaba a ser costumbre.

De ahí salió la regla: **desde que un incumplimiento queda registrado, lo que se escriba de ahí en adelante nace cumpliendo.** El usuario lo dijo así: *"yo antes escribía sin ortografía, pero a partir de que aprendí ya escribo con ortografía, no importa el contexto"*.

Para este pendiente eso significa dos cosas:

- **La cuenta ya no crece.** Los 354 son los de antes del 2026-08-14; si aparecen más, no es deuda vieja, es un incumplimiento nuevo de `F21`.
- **Limpiarlos sigue siendo trabajo aparte**, y es lo que este pendiente guarda.


---

# Cómo cerró — 2026-08-18

**Los 354 que el pendiente contó se repararon; los 747 que quedaban resultaron no ser incumplimientos.**

| | Qué pasó |
|---|---|
| **284 entre carpetas** | ✅ **Reparados** — el texto dice la ruta desde la raíz. Lo hizo `enlaces.reparar_formato`, no la mano |
| **747 de la misma carpeta** | ✅ **Exentos** — [`13·DOC14`](../../base/13-documentacion/reglas/DOC14-enlaza-cada-md-con-ruta-legible-y-destino-relativo.md) lo dice ahora en su excepción |

## Por qué exentos, y no «porque son muchos»

**La excepción sale del propio texto de la regla.** `DOC14` pide la ruta completa *«para saber dónde vive sin abrirlo»*. **Para un archivo de la misma carpeta ese propósito ya está cumplido**: quien lee está parado ahí.

Exigirla igual producía textos de unos 130 caracteres para nombrar el archivo de al lado — el trámite **después de que el motivo se agotó**. Y la mayoría eran los cinco documentos de una fase citándose entre sí.

**El límite es estrecho a propósito:** la misma carpeta y nada más. Un enlace a la carpeta vecina sigue llevando su ruta entera, porque ahí el lector sí necesita saber adónde va.

## Lo que se intentó primero, y se revirtió

**Se aplicó `DOC14` al pie de la letra sobre los 1 031**, y quedó ilegible: textos de 132 caracteres para decir `plan_pruebas.md`. **Se revirtieron los 347 archivos** y se aplicaron solo los 284 de entre carpetas.

Esa reversión es la que destapó que el problema no eran los enlaces: **era la regla**, que no había previsto el caso más común.

## Lo que queda comprobado

`enlaces.validar_formato` reporta el enlace entre carpetas mal escrito y **calla** el del vecino. `cerrar.py` repara las dos partes al mover un archivo, para no volver a desordenarlo al cerrar un pendiente.
