# Funcionalidad implementada — Fase `A-EP-001-HU-006-retrodocumentar-la-capa-del-proyecto` (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

> **Veredicto de la fase: [No cumple](resultado_pruebas.md).** El `CA-03` salió en rojo **por no haberse podido comprobar**, no por estar roto: ningún proyecto real tiene un ajuste que contradiga el núcleo, y escribir uno para provocarlo estaba prohibido. Se cierra declarándolo.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-001-HU-006-retrodocumentar-la-capa-del-proyecto` |
| **Módulo** | Cuerpo de reglas |
| **Especificación del módulo** | La propia [HU-006](../HU-006-capa-propia-del-proyecto.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | [HU-006](../HU-006-capa-propia-del-proyecto.md): `CA-01`, `CA-02` y `CA-03` |
| **Fecha de cierre** | 2026-08-27 |
| **Versión del estándar al cerrar** | `35.1.0` |
| **Commit** | `f10729c` |

> **Se ejecutó el 2026-08-22 y se cierra el 2026-08-27.** Entre las dos fechas no se tocó nada de esta fase.

---

## 1. Qué se implementó — resumen

**Nada nuevo: esta fase midió la capa propia de un proyecto real, AgroSystem.**

**Dos criterios cumplieron.** El ajuste del proyecto manda sobre la convención sin tocar el cuerpo central, y una regla propia sin respaldo se detecta.

**El tercero quedó en rojo, y la razón importa: no se pudo comprobar.** El criterio dice que un ajuste que contradiga el núcleo no aplica. Para verlo hay que tener uno — y **ningún proyecto real lo tiene**, porque el propio archivo escribe la prohibición. Escribir uno a propósito en un proyecto ajeno estaba fuera de lo permitido.

**Se marcó en rojo en vez de darlo por bueno**, que es lo que `04·R4` pide: no afirmar sobre lo que no se observó.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem de la historia | Categoría | Estado | Evidencia |
|---|---|---|---|
| `CA-01` el ajuste manda sobre la convención | norma | ✅ | La declaración de precedencia de la capa propia: `00` núcleo primero, y el cuerpo central sin cambios |
| `CA-02` una regla propia sin respaldo no se acepta | comprobación | ✅ | La comprobación corre y encuentra **56 de 56** |
| `CA-03` el ajuste que contradice el núcleo no aplica | norma | ❌ **No cumple** | **Solo por lectura.** No se pudo provocar sin escribir en un proyecto real |

**El `CA-02` no dio verde por salir limpio: dio verde porque encontró las 56.** Una comprobación que no encuentra nada no demuestra que funciona.

### 2.2 Plan de trabajo → ejecución

| Qué | Resultado |
|---|---|
| Lo que el plan pedía | ✅ hecho, sobre un proyecto real |
| Lo que se encontró | Dos criterios verdes, uno **no comprobable** con lo disponible |

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Lo que no se hizo en su momento:** este documento. **La fase quedó cinco días sin cerrar.**

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Qué | Resultado |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **No cumple** — uno de tres sin poder comprobarse |
| **Defectos** | `D-01` y `D-02` altas, `D-03` media, `D-04` cerrada al comprobarla |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

```
python validadores/validar.py metareglas --catalogo <proyecto>
```

Comprueba las reglas propias de un proyecto contra su respaldo en el estándar.

---

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué |
|---|---|
| El `CA-03` se marcó **en rojo** por no poder comprobarse, en vez de verde por lectura | `04·R4`: no afirmar sobre lo que no se observó. Un verde por lectura habría dicho «comprobado» sin serlo |
| **No se escribió un ajuste que contradijera el núcleo** en un proyecto real para provocarlo | Habría sido meter una regla mala en un proyecto ajeno para probar un criterio propio |

**La primera es la decisión de la fase.** Es más cómodo marcar verde y anotar «se verificó por lectura»; el rojo obliga a que alguien vuelva.

---

## 6. Deuda técnica y pendientes generados

| Descripción | Severidad | Estado al cerrar |
|---|---|---|
| **`D-01` · `metareglas --raiz <proyecto>` reporta una falla y cuatro avisos falsos:** corre las comprobaciones del estándar contra un proyecto | Alta | **Resuelta** en [`B-EP-004-HU-011`](../../../EP-004-comprobacion-automatica/HU-011-molde-de-las-reglas/B-EP-004-HU-011-no-afirmar-sobre-lo-que-no-se-leyo/funcionalidad_implementada.md), el 2026-08-22 |
| **`D-02` · Las 56 reglas `P` de AgroSystem no declaran respaldo** | Alta | **Abierta, y no es del estándar**: es de ese proyecto, y va por el canal de defectos de vuelta |
| **`D-03` · El `CA-03` no se pudo provocar** | Media | **Abierta.** Hace falta un proyecto de prueba desechable donde sí se pueda escribir un ajuste malo |
| **`D-04` · El plan daba por inexistente la comprobación de `M16`**, construida cinco días antes de ejecutarlo | Baja | **Cerrada al comprobarlo** |

**`D-03` es la que queda, y tiene salida conocida:** un proyecto de mentira en carpeta temporal, como el que se usó el 2026-08-26 para probar el instalador. Provocar el caso ahí no toca a nadie.

**Y `D-04` es, otra vez, el plan afirmando sobre el producto sin verificar** — esta vez dando por inexistente algo construido cinco días antes.

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] La historia [HU-006](../HU-006-capa-propia-del-proyecto.md): su §8 nombra esta fase.
- [x] El inventario de historias, que **ya no se mantiene a mano** desde la `35.0.0`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

- **Migraciones a correr:** ninguna. Esta fase no cambió nada: midió.
- **Reversión:** no aplica.
