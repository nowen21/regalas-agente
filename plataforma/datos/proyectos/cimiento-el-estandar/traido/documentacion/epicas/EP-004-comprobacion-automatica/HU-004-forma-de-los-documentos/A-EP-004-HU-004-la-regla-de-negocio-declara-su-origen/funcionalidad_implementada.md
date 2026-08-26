# Funcionalidad implementada — Fase «A-EP-004-HU-004-la-regla-de-negocio-declara-su-origen»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito **qué quedó hecho**, para que quien llegue después no tenga que deducirlo del código ni del historial.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-004-HU-004-la-regla-de-negocio-declara-su-origen` |
| **Épica / HU** | [EP-004](../../epica.md) · [HU-004](../HU-004-forma-de-los-documentos.md) |
| **Versión del estándar** | 22.0.0 → **22.1.0** (MENOR) |
| **Fecha de cierre** | 2026-08-16 |

---

## 1. Qué quedó funcionando

**Una regla de negocio sin procedencia se reporta como falla.** `reglas_sin_origen()` lee el §4 de una especificación de módulo y marca cada regla que no traiga un identificador (`RF-13`, `HU-001`, `D-22`). La falla dice de qué regla habla, en qué línea, y qué hacer con ella: subirla a la historia que corresponda.

**Y algo que no estaba en el plan de nadie: un `spec.md` ahora se reconoce.** Antes de esta fase, un documento con ese nombre no se comparaba contra ninguna plantilla — el programa no sabía cuál le tocaba. La comprobación nueva no se habría disparado nunca, y las otras tres tampoco lo miraban.

Lo que **no** hace: comprobar que el identificador apunte a algo real. Eso es trazabilidad y es otra fase.

---

## 2. Qué se tocó

| Archivo | Qué |
|---|---|
| [`validadores/plantillas.py`](../../../../../validadores/plantillas.py) | `spec` en la tabla de moldes, y `reglas_sin_origen()` como cuarta comprobación |
| [`validadores/tests/test_plantillas_origen_regla.py`](../../../../../validadores/tests/test_plantillas_origen_regla.py) | **Nuevo.** Tres casos, con las dos reglas reales del caso de `shopnest-mesa` |
| [`validadores/docs/plantillas.md`](../../../../../validadores/docs/plantillas.md) | La cuarta comprobación, y por qué está atada a un molde concreto |
| [`HU-004-forma-de-los-documentos.md`](../HU-004-forma-de-los-documentos.md) | El `CA-04`, la fase en §8 y la bitácora |
| [`CHANGELOG.md`](../../../../../CHANGELOG.md) · `VERSION` | 22.1.0 |

---

## 3. Cómo se comprueba

```
python -m unittest discover -s validadores/tests
```

29 pruebas, 29 en verde. Los tres casos nuevos están en `ReglaDeNegocioSinOrigen`, y se vieron fallar a propósito con la comprobación desactivada.

---

## 4. Qué quedó fuera, y con número

**31 reglas de negocio de este repositorio no dicen de dónde bajan** — 16 en `documentacion/automatismos/spec.md` y 15 en `documentacion/documentos-modelo/spec.md`. Es la exigencia 3 del pendiente 43, que pedía averiguar cuántas había: ya se sabe, y son las del propio estándar.

No se corrigieron acá porque no es trabajo mecánico: hay que decidir de dónde baja cada una, y algunas seguramente no bajen de ninguna parte — que es justamente lo que la regla nueva quiere hacer visible. Queda en un pendiente propio.

**No se apagó la comprobación para que el número diera cero.** Un validador que se calla cuando molesta no sirve para nada.

Tampoco entra: comprobar que el identificador exista de verdad, y la columna `Origen` de la tabla de campos del §5.1.
