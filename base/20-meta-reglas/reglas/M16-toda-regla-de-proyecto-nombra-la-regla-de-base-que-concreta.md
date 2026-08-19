> Regla del capítulo [`20 · Meta-reglas`](../base.md).

## M16 · Toda regla de proyecto nombra la regla de base que concreta

Cada regla del catálogo de un proyecto ([`13·DOC10`](../../13-documentacion/reglas/DOC10-registra-en-el-catalogo-del-proyecto-toda-regla-propia.md)) declara, con su enlace ([`M15`](M15-toda-cita-a-otra-regla-lleva-su-enlace.md)), la regla de `base/` cuyo criterio concreta o endurece (extiende [`M1`](M1-la-jerarquia-tiene-cuatro-niveles-y-un-solo-orden.md)). Si ningún criterio de `base/` la cubre, esa regla de base se escribe primero, agnóstica ([`M3`](M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md)) y por el procedimiento completo ([`M14`](M14-ninguna-regla-nace-fuera-del-procedimiento.md)); hasta entonces la regla de proyecto no se publica.

```
INCORRECTO: P4 · El catálogo se cachea 10 minutos · Por qué: lo acordó el equipo
CORRECTO:   P4 · El catálogo se cachea 10 minutos · Respaldo 06·R4: fija aquí el tiempo
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../checklist.md) contra **v8.0.0**, el **2026-08-12**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.** **N/A** — **16**: no tiene excepción. Fila **2**: se buscó por concepto; [`13·DOC10`](../../13-documentacion/reglas/DOC10-registra-en-el-catalogo-del-proyecto-toda-regla-propia.md) exige registrar la regla propia y numerarla, no de dónde sale, y [`M13`](M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md) enruta lo que se escribe en `base/`, no lo que se escribe en la capa 3. Fila **17**: no choca con [`M1`](M1-la-jerarquia-tiene-cuatro-niveles-y-un-solo-orden.md), que dice dónde vive la regla del equipo; esta dice de dónde sale su criterio.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
