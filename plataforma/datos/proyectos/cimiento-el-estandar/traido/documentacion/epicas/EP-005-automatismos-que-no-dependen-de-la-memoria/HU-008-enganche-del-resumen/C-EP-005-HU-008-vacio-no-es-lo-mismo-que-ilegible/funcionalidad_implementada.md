# Funcionalidad implementada — Fase «C-EP-005-HU-008-vacio-no-es-lo-mismo-que-ilegible»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito **qué quedó hecho**, para que quien llegue después no tenga que deducirlo del código ni del historial.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `C-EP-005-HU-008-vacio-no-es-lo-mismo-que-ilegible` |
| **Épica / HU** | [EP-005](../../epica.md) · [HU-008](../HU-008-enganche-del-resumen.md) |
| **Versión del estándar** | sin cambio — no se toca `base/` ni `plantillas/` |
| **Fecha de cierre** | 2026-08-18 |

---

## 1. Qué quedó funcionando

**El enganche distingue un resumen vacío de uno que no puede leer.** Son dos avisos, con dos marcas propias, y piden trabajo distinto: uno, escribir; el otro, **renumerar lo que ya está escrito**.

**Lo destapó el propio enganche diciendo algo que parecía falso:** avisó *«el resumen de esta sesión sigue vacío»* sobre un archivo con **quince hallazgos**. No se equivocaba al mirar — estaban escritos como `### 1 ·` y el molde de [`plantillas/sesion.md`](../../../../../plantillas/sesion.md) pide `### H-1 ·`.

| Qué | Cuánto |
|---|---|
| Resúmenes del histórico | 47 |
| Escritos fuera del molde | **3**, todos del 2026-08-17 |
| Hallazgos que el programa no veía | **29** |

**Los tres son de la misma jornada.** No es un descuido repetido: es una forma que se adoptó en una sesión y se copió a la siguiente **porque nada la contradijo** — y lo que debía contradecirla era justo el aviso que se apagaba solo.

---

## 2. El defecto se tapaba a sí mismo, por tres caminos

1. **El resumen se contaba como vacío**, así que el aviso pedía escribir lo que ya estaba escrito.
2. **La comprobación del cierre nunca corría**, porque necesita encontrar un hallazgo antes de mirar. En esos tres resúmenes no se ejecutó ni una vez.
3. **El aviso se marca a sí mismo como ya dado.** Se ve una vez y después calla para siempre.

**Ninguno de los tres deja rastro.** Un aviso que no sale no aparece en ningún registro, y un resumen contado como vacío se ve igual que uno que lo está.

---

## 3. Qué se tocó

| Archivo | Qué |
|---|---|
| [`validadores/resumen.py`](../../../../../validadores/resumen.py) | `_CASI_HALLAZGO`, `MARCA_MOLDE` y `hallazgos_fuera_del_molde()` |
| [`validadores/hook_resumen.py`](../../../../../validadores/hook_resumen.py) | El aviso nuevo, **antes** del de vacío, diciendo cuántos hay |
| [`validadores/tests/test_el_resumen_ilegible_no_es_vacio.py`](../../../../../validadores/tests/test_el_resumen_ilegible_no_es_vacio.py) | 9 casos |
| `historico-chat/resumenes/2026-08-17/` | Los tres renumerados — 29 hallazgos legibles |

**No se toca `base/` ni `plantillas/`, así que no hay versión que subir.** El molde no cambia: lo que cambia es que ahora se avisa cuando no se sigue. Aflojarlo para aceptar las dos formas era la otra salida, y se descartó — 44 resúmenes lo siguen, y cambiarlo por tres es premiar al que no lo miró.

---

## 4. Las decisiones que hay que poder releer

**Dos marcas, no una.** Con una sola, avisar de un caso apagaría el otro **para siempre** — y el aviso se da una vez, así que apagarlo por error no se recupera. Tiene caso propio porque es la clase de atajo que parece limpieza al releer el código.

**El aviso dice cuántos.** Es lo que lo vuelve creíble para quien tiene el archivo lleno delante. Un aviso que se puede desmentir de un vistazo se deja de leer, y esa reacción es la correcta ante algo que afirma lo falso: **el programa no se equivocaba al mirar, se equivocaba al nombrar lo que vio.**

**Solo se mira cuando no hay ni un `H-`.** Un resumen correcto puede tener secciones numeradas que no son hallazgos; si el molde se está siguiendo, un `### 2 ·` suelto es otra cosa.

**Los tres se renumeraron después de escribir la comprobación**, para que se estrenara sobre los archivos que estaban mal.

---

## 5. Lo que no hace

**No fuerza que el próximo resumen se escriba bien, y es a propósito.** Escribir un hallazgo es criterio ([`13·DOC22`](../../../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md)): el programa crea el archivo, avisa y muestra — no escribe ni interpreta. Lo que cambió es que el molde equivocado **se dice**, en vez de convertirse en silencio.
