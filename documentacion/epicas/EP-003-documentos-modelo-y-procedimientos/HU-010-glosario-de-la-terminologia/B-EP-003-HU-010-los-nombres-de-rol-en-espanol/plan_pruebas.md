# Plan de Pruebas — Fase B-EP-003-HU-010: los nombres de rol en español

| Campo | Valor |
|---|---|
| **Código** | PP-B-EP-003-HU-010 |
| **Versión** | 1.0 |
| **Fecha** | 2026-08-18 |
| **Aprobado por** | Pendiente — el usuario |

---

## 3. Estrategia

Traducir es reemplazar texto, y **el modo de fallar es tocar de más**: una ruta, una palabra que contiene al término, un nombre de archivo. Los casos miran eso, no que la traducción exista.

---

## 5. Matriz de trazabilidad

| Exigencia | Caso | Estado |
|---|---|---|
| `01·C20` · ningún término del inventario en inglés | [CP-001](#cp-001--ningún-nombre-del-inventario-queda-en-inglés) | ☐ |
| El reemplazo no toca de más | [CP-002](#cp-002--el-reemplazo-no-toca-rutas-ni-palabras-que-contienen-el-término) | ☐ |
| Renombrar no rompe citas | [CP-003](#cp-003--los-cuatro-renombres-no-dejan-un-enlace-roto) | ☐ |
| `20·M14` · la regla editada resella | [CP-004](#cp-004--id6-vuelve-a-pasar-su-checklist) | ☐ |
| No regresión | [CP-005](#cp-005--nada-de-lo-que-ya-estaba-deja-de-pasar) | ☐ |

**Cobertura:** 5 de 5 = 100%.

---

## 6. Casos

### CP-001 — Ningún nombre del inventario queda en inglés

Buscar cada uno de los trece con borde de palabra en `base/`, `plantillas/`, `skills/` y `notas/`. Cero, salvo el glosario, que es el inventario.

### CP-002 — El reemplazo no toca rutas ni palabras que contienen el término

Que `plantilla-spec-modulo.md` siga siendo un nombre de archivo válido dentro del texto, y que ninguna ruta quede a medio traducir.

> Es el modo de fallar de este cambio: un nombre de archivo traducido a medias no rompe nada visible hasta que alguien sigue el enlace.

### CP-003 — Los cuatro renombres no dejan un enlace roto

`validar.py estandar`, sin incumplimientos.

### CP-004 — `ID6` vuelve a pasar su checklist

Editar el texto de una regla anula su sello, aunque el cambio sea de idioma. `validar.py metareglas` no la reporta.

### CP-005 — Nada de lo que ya estaba deja de pasar

Las dos suites.

---

## 12. Métricas

| Métrica | Meta |
|---|---|
| Términos del inventario que quedan en inglés | **0** |
| Enlaces rotos | **0** |
| Reglas con el sello anulado sin reaplicar | **0** |

Un solo concepto: **Cumple** o **No cumple**.
