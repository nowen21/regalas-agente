# Funcionalidad implementada — Fase «XX» «slug» (módulo «M»)   ·   `[CAPA 3]`

> Documento de **cierre de una fase** (`02·F6`/`F7`). Consolida qué se implementó, la **trazabilidad spec → código** (`13·DOC11`), qué se probó y qué quedó. Se escribe en la estación de cierre, **antes del commit** de la fase. Se guarda en `documentacion/<modulo>/fase-<XX>-<slug>/funcionalidad_implementada.md`. Reemplaza los `«…»` y borra esta caja.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | «XX» · slug `«slug»` |
| **Módulo** | «M» |
| **Spec del módulo** | [enlace · `02·F2`] |
| **Plan de trabajo** | [enlace · `plan_trabajo.md`] |
| **HU / CA cubiertas** | HU-«NNN» (CA-01, CA-02) · HU-«NNN» (CA-01) |
| **Fecha de cierre** | AAAA-MM-DD |
| **Commit** | [hash — se completa al commitear] |

---

## 1. Qué se implementó — resumen

[2–4 líneas en lenguaje claro: qué quedó funcionando y para quién. Sin detalle de código.]

---

## 2. Trazabilidad spec → implementación  ·  `13·DOC11`

> Una fila por **afirmación técnica del spec**. No se cierra con faltantes sin justificar.
>
> **Estados:** ✅ implementado · ❌ pendiente (con destino explícito) · N/A (con motivo) · parcial (qué queda y a dónde va). Si aparece un faltante que **debía** estar en esta fase, se corrige in situ — no se difiere como N/A.

| Ítem del spec | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| (frase literal o resumida) | esquema · modelo · servicio · vista · prueba · permiso · ruta · doc | `[ruta real]` | ✅ / ❌ / N/A / parcial | (prueba concreta o commit) |

**Faltantes / diferimientos** (si hay `❌` o parcial): [qué queda y a qué fase se traslada].

---

## 3. Qué se probó  ·  `08` / `02·F5`

- **Suites corridas + resultado:** «X/X verdes» (alcance quirúrgico — solo las suites que la fase toca).
- **Verificaciones manuales** — lo que el entorno automático **no** reproduce (`08·T4`):
  - [Lista de comprobaciones hechas a mano y su resultado.]

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

- **Punto de entrada** (UI / endpoint / comando): [dónde y cómo se accede].
- **Permisos o datos base sembrados:** [si aplica].

---

## 5. Decisiones no obvias  ·  `13·DOC2` / `DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| | | [id / enlace en la memoria] |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Destino (fase futura / ticket / `pendientes/`) |
|---|---|
| | |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `DOC13`

- [ ] Mapa de dependencias vivo actualizado (`DOC9`).
- [ ] Catálogo de módulos actualizado, si se creó o cambió un módulo (`DOC13`).
- [ ] Índice `README.md` de la carpeta de docs actualizado (`DOC15`).
- [ ] Spec del módulo actualizado con lo realmente implementado.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

Pasos **auto-suficientes y ejecutables** para producción (quien despliega lo hace leyendo esto, sin mirar el código):

- Cambios de esquema / migraciones a correr: [orden].
- Datos base / permisos a sembrar: [comandos].
- Comandos post-deploy: [si aplica].
- Reversión: [rollback previsto · ver §7 del `plan_trabajo`].
