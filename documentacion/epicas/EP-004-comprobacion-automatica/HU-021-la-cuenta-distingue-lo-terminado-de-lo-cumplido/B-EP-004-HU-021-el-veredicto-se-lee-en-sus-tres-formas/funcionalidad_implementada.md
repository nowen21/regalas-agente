# Funcionalidad implementada — Fase `B-EP-004-HU-021-el-veredicto-se-lee-en-sus-tres-formas` (módulo Programas de comprobación)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-004-HU-021-el-veredicto-se-lee-en-sus-tres-formas` |
| **Módulo** | Programas de comprobación |
| **Especificación del módulo** | No hay documento aparte. `02·F19`: la redacción del CA es la especificación funcional |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-27 |
| **HU / CA cubiertas** | [HU-021](../HU-021-la-cuenta-distingue-lo-terminado-de-lo-cumplido.md): el `CA-03` |
| **Fecha de cierre** | 2026-08-27 |
| **Versión del estándar al cerrar** | `35.2.0` — **sin cambio**: no se toca `base/` ni `plantillas/`, así que `20·M10` no alcanza esta fase |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | Pendiente de aprobación del usuario |

---

## 1. Qué se implementó — resumen

**El lector del veredicto reconocía dos de las tres formas en que está escrito.** Por eso siete historias figuraban entre las que «no dicen si cumplen» **cuando sí lo dicen**.

La forma que faltaba es la más directa: **`**Cumple.**` bajo su encabezado, sin rótulo.**

| Antes | Ahora |
|---|---|
| `52 cumplen, 11 no cumplen, 22 no dicen` | `56 cumplen, 13 no cumplen, 16 no dicen` |

**Y al cerrar esta fase, `57 cumplen, 13 no cumplen y 15 no dicen`**: su propia historia pasó de «no dice» a «cumple» al ganar veredicto.

**El defecto era de la fase [`A`](../A-EP-004-HU-021-la-cuenta-mira-el-veredicto/funcionalidad_implementada.md), encontrado diez minutos después de cerrarla** — y en la dirección pesimista, que es la menos dañina, pero mal igual.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem de la historia | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| `CA-03` lo ilegible se cuenta aparte | servicio | `_VEREDICTO_BAJO_TITULO` en [validadores/fases.py](../../../../../validadores/fases.py) | ✅ | CP-001 paso 3 |
| `CA-03` **y solo** lo ilegible | servicio | El encabezado, exigido en el patrón | ✅ | CP-002, sus cuatro pasos |

### 2.2 Plan de trabajo → ejecución

| Tarea | Estado | Evidencia |
|---|---|---|
| T-01 · reconocer la forma bajo el encabezado | ✅ | CP-001 paso 3 |
| T-02 · seguir exigiendo el encabezado | ✅ | CP-002, y el sabotaje 2 |
| T-03 · un caso por forma | ✅ | 4 pruebas |
| T-04 · un caso de que **no** lea | ✅ | 4 pruebas |
| T-05 · medir antes y después | ✅ | §3 del resultado, y el §4.2 |
| T-06 · las 14 de la fase `A`, sin tocarlas | ✅ | CP-003 |
| T-07 · sabotear | ✅ | **4 de 4 cazados al primer intento** |

**Correspondencia:** 7 tareas, 7 con resultado. **Ninguna sin hacer.**

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, en el ciclo 1 |
| **Suites ejecutadas + resultado** | `python validadores/pruebas.py`: **425 de 425 verdes** |
| **Defectos abiertos que se aceptaron** | Ninguno |

**El criterio de suspensión se activó y se respetó.** El plan exigía que las «no dicen» bajaran en siete exactamente; bajaron seis según la línea, así que se paró y se investigó antes de seguir. Está contado en el §4.2 del resultado.

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

```
python validadores/validar.py fases
```

Sin cambios en el uso. `veredicto_de` y `por_veredicto` **conservan su firma**; lo único que cambió es cuántas formas saben leer.

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal |
|---|---|---|
| Un patrón **aparte** para la tercera forma | Meterla en el patrón de antes obliga a un `or` dentro de la expresión que la vuelve ilegible, y arriesga perder las dos que ya servían — que es el sabotaje 3 | El plan §2.6 |
| **Se exige el encabezado**, no basta la palabra | En un resultado «Cumple» aparece en cada fila de criterio. Sin el encabezado, se leería el primer criterio en vez del veredicto — y mentiría **en la dirección optimista** | `S-056` |
| Se agrega **la forma que existe**, no las que podrían existir | Se contaron las 129 fases: hay tres formas y 39 sin encabezado. Un lector que adivine termina leyendo veredictos donde no los hay | El plan §2.0 |
| **No se uniforman las 129** | El molde ya fija una forma para lo nuevo. Reescribir lo cerrado borra el rastro | El plan §1 |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| **Las 39 fases sin encabezado de veredicto** | **Abierta, y correctamente contada.** Esas de verdad no lo dicen. Se resuelven escribiéndolo, una por una |
| **Las 16 historias que no dicen si cumplen** | **Abierta.** Bajaron de 23, y las que quedan son reales |
| **Las 13 que no cumplen** | **Abierta.** Subieron de 11 al leerse dos veredictos que estaban escondidos. Es trabajo que ya existía y no se veía |
| El andamio crea los cinco documentos vacíos, y una fase recién abierta cuenta **terminada** (`S-053`) | **Abierta, y esta fase volvió a demostrarlo**: al levantarla, su propia historia recayó en «no dicen». Es lo que movió la base de medición |

**La última es la que queda viva, y ya cobró tres veces en el mismo día.**

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] La épica [EP-004](../../epica.md): la fase `B` en sus tablas.
- [x] El [README](../README.md) de la carpeta de la historia.
- [x] La señal `S-056`.
- [ ] `VERSION` y `CHANGELOG.md`: **no aplica**, no se toca `base/` ni `plantillas/`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

- **Migraciones a correr:** ninguna.
- **Qué cambia para quien ya tenía el estándar:** su reparto se corrige — bajan las «no dicen» y suben las otras dos. **No cambió nada de su trabajo.**
- **Reversión:** se descarta el commit.
