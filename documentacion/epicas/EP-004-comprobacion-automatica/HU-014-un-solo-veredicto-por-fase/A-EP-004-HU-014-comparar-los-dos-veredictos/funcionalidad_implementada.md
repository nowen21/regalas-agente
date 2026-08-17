# Funcionalidad implementada — Fase «A-EP-004-HU-014-comparar-los-dos-veredictos»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito **qué quedó hecho**, para que quien llegue después no tenga que deducirlo del código ni del historial.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-004-HU-014-comparar-los-dos-veredictos` |
| **Épica / HU** | [EP-004](../../epica.md) · [HU-014](../HU-014-un-solo-veredicto-por-fase.md) |
| **Versión del estándar** | 23.0.0 → **23.1.0** (MENOR) |
| **Fecha de cierre** | 2026-08-16 |

---

## 1. Qué quedó funcionando

**Una fase ya no puede tener dos veredictos distintos sin que se note.** `veredicto()` en [`validadores/fases.py`](../../../../../validadores/fases.py) compara, para cada fase que tenga los dos documentos:

- **El concepto** — si el `resultado_pruebas` dice una cosa y el `estado-fase` otra, es falla, y el hallazgo nombra los dos valores y recuerda cuál mira la puerta de verificación.
- **Las exigencias en «No»** — si el §5 del resultado tiene un criterio o un requisito en «No» y el `estado-fase` da la fase por cumplida, se nombra esa exigencia.
- **El conteo** — si los dos documentos cuentan criterios distintos, se dicen los dos números.

**Lo que no hace, y no puede:** decir si el veredicto es **cierto**. Un programa no sabe si un criterio de verdad cumple; sabe que dos documentos dicen cosas distintas.

---

## 2. Qué se tocó

| Archivo | Qué |
|---|---|
| [`validadores/fases.py`](../../../../../validadores/fases.py) | `veredicto()` y sus ayudantes, llamados desde el recorrido de fases que ya existía |
| [`validadores/tests/test_fases_veredicto.py`](../../../../../validadores/tests/test_fases_veredicto.py) | **Nuevo.** Cuatro casos |
| [`validadores/docs/fases.md`](../../../../../validadores/docs/fases.md) | La comprobación nueva |
| [`HU-014-un-solo-veredicto-por-fase.md`](../HU-014-un-solo-veredicto-por-fase.md) | La fase en §8 y la bitácora |
| [`CHANGELOG.md`](../../../../../CHANGELOG.md) · `VERSION` | 23.1.0 |

---

## 3. Cómo se comprueba

```
python -m unittest discover -s validadores/tests
```

36 pruebas, 36 en verde. Los cuatro casos nuevos están en `UnSoloVeredictoPorFase`.

---

## 4. La decisión que esta fase tomó

El pendiente dejaba **dos salidas** y ninguna elegida. Se tomó la primera:

| Salida | Qué pasó con ella |
|---|---|
| Un programa compara los dos y avisa | **Elegida.** No cambia ningún molde, no obliga a reescribir ninguna fase cerrada y cabe entera en EP-004 |
| El `estado-fase` no escribe el veredicto: lo enlaza | Descartada por ahora. Quita la copia de raíz, pero cambia el molde, obliga a migrar todas las fases escritas y cambia lo que lee la puerta de verificación |

Si algún día se hace la segunda, **esta comprobación sobra y se retira**. Queda dicho para que nadie tenga que deducirlo.

---

## 5. Lo que hay que saber para leer su resultado

**No encontró ninguna contradicción en este repositorio, y no es una buena noticia por sí sola:** el único caso conocido se corrigió unas horas antes, al cerrar el pendiente 27. La comprobación llegó tarde a su propio caso.

Su valor no es lo que encuentra hoy: es que la próxima contradicción no dependa de que alguien reescriba un resultado de pruebas y note la diferencia — que fue exactamente como se encontró esta.
