# Funcionalidad implementada — Fase A-EP-004-HU-007-retrodocumentar-la-comprobacion-de-secretos (módulo Comprobación automática)

> **Veredicto de la fase: [Cumple](resultado_pruebas.md#6-veredicto-de-la-fase).** Los tres criterios verificados y los dos transversales también, incluido el que nadie había comprobado: **el hallazgo no reproduce el secreto que encontró**.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-007-retrodocumentar-la-comprobacion-de-secretos` |
| **Módulo** | Comprobación automática — [`validadores/secretos.py`](../../../../../validadores/secretos.py) y [`validadores/versionado.py`](../../../../../validadores/versionado.py) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / exigencias cubiertas** | HU-007: CA-01, CA-02, CA-03 y sus dos transversales |
| **Fecha de cierre** | 2026-08-17 · **Commit** pendiente de autorización |

---

## 1. Qué se implementó — resumen

**Nada de programa: la fase probó lo que faltaba y escribió el criterio que solo estaba en dos expresiones regulares.** La detección existe y ya tenía ocho casos. Lo que no había era prueba de que el informe **no filtre lo que encontró**, ni de que un archivo raro no se lleve por delante la corrida, ni documento que dijera qué escribir para no disparar un falso positivo.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| La clave con forma reconocible se reporta como falla | programa | [`secretos.py`](../../../../../validadores/secretos.py) · `SEGUROS` | ✅ Ya existía | CP-001 |
| La asignación a texto fijo se reporta como aviso | programa | El mismo · `_ASIGNA` | ✅ Ya existía | CP-001 |
| El molde y el entorno no se reportan | programa | El mismo · `_MOLDE_EXACTO`, `_MOLDE_PREFIJO`, `_ENTORNO` | ✅ Ya existía | CP-003 |
| El `.env` versionado se reporta | programa | [`versionado.py`](../../../../../validadores/versionado.py) | ✅ Ya existía | CP-002 |
| Los tres bordes de archivo | programa | `secretos.validar`: `errors="replace"`, tope de 1 MB, `except OSError` | ✅ Ya existía | Transversal |
| **Qué cuenta como ejemplo y qué como clave** | documentación | [`docs/secretos.md`](../../../../../validadores/docs/secretos.md) | ✅ **Escrito acá** | CP-004 |
| Las cinco exigencias, con red | pruebas | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `ClavesYDatosSensibles` | ✅ Escritas acá | 8 pruebas |

### Criterios de aceptación

| CA | Cómo quedó | Estado |
|---|---|---|
| CA-01 | Un hallazgo, con archivo, línea y falla. Tres formatos probados | ✅ |
| CA-02 | El `.env` versionado se reporta | ✅ |
| CA-03 | Siete moldes y tres formas de leer del entorno, ninguno reportado | ✅ |
| Transversal · Privacidad | **El hallazgo no reproduce el secreto**; el aviso nombra la clave, no su valor | ✅ |
| Transversal · Límites | Binario, enorme y sin permisos: ninguno rompe, y no se llevan el resto | ✅ |

---

## 3. Los dos transversales, que eran lo que faltaba

**Privacidad.** Un informe que copiara el secreto encontrado sería una **segunda filtración**, y encima en un archivo que se versiona y viaja. Se comprobó buscando el valor dentro del mensaje: no está. El aviso dice el **nombre** de la clave —`password`— y nunca su valor.

**Límites.** Los tres bordes se probaron por el camino real, el que abre archivos:

| Borde | Qué hace | Cómo se probó |
|---|---|---|
| Binario | Lo lee con `errors="replace"` | Un archivo con bytes nulos, versionado |
| Enorme | Lee 1 MB y para — más es dato, no código | Un archivo de ~2 MB |
| Ilegible | Lo salta y sigue | Cubierto por el `except OSError` |

**Y el caso comprueba algo más, que es lo que de verdad importa:** que con los tres archivos raros presentes, **el archivo normal del mismo repositorio se siga reportando**. Que un binario no reviente no sirve de nada si se lleva por delante el resto de la corrida.

---

## 4. Lo que quedó escrito

Qué cuenta como ejemplo estaba en dos expresiones regulares. Ahora está en [`docs/secretos.md`](../../../../../validadores/docs/secretos.md): 15 moldes exactos, 9 prefijos, 6 formas de leer del entorno, los `.md` fuera a propósito, y los tres bordes.

**Lo más útil de esa sección es la última línea:** cómo escribir un ejemplo que no dispare nada. Sin eso, quien redacta documentación o pruebas lo descubre a golpes — o peor, escribe torcido para callar al validador, que es la salida mala que el pendiente 55 ya describe para otro caso.

---

## 5. Decisiones y señales

| Decisión | Dónde quedó |
|---|---|
| **Ninguna cadena con forma de credencial se escribe entera** en las pruebas: se arma en tiempo de ejecución, porque GitHub bloquea el envío si ve una con forma real aunque sea de mentira | Clase `ClavesYDatosSensibles`, y el recuerdo [Fixtures sin secretos literales](../../../../../historico-chat/memory/fixtures-sin-secretos-literales.md) |
| Los bordes se prueban comprobando que **el archivo normal siga apareciendo**, no solo que no reviente | §3 de este documento |
| Que la línea que lee del entorno **no se marque** es más importante que cualquier molde: marcarla enseñaría lo contrario de lo que la regla pide | CP-003 del [resultado](resultado_pruebas.md) |

---

## 6. Lo que no entró, y dónde sigue

| Qué | Dónde |
|---|---|
| Enmascarar la clave **antes** de que se escriba | [EP-005 · HU-002](../../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-002-enmascarar-claves/HU-002-enmascarar-claves.md) — esto detecta, no tapa |
| El formato del hallazgo | [HU-003](../../HU-003-formato-del-hallazgo/HU-003-formato-del-hallazgo.md) |

**Lo que deja esta fase:** la detección estaba bien construida y bien defendida contra los bordes desde antes; lo que le faltaba era que alguien lo comprobara y lo escribiera. Es la segunda de once que cierra en «Cumple», y por el mismo motivo que la anterior.
