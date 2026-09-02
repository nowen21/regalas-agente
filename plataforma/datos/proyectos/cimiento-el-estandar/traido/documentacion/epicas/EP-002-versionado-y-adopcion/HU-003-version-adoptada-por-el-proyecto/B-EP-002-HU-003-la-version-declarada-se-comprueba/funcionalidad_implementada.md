# Funcionalidad implementada — Fase `B-EP-002-HU-003-la-version-declarada-se-comprueba` (módulo Programas de comprobación)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-002-HU-003-la-version-declarada-se-comprueba` |
| **Módulo** | Programas de comprobación |
| **Especificación del módulo** | La propia [HU-003](../HU-003-version-adoptada-por-el-proyecto.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), abierto el 2026-08-22 |
| **HU / CA cubiertas** | [HU-003](../HU-003-version-adoptada-por-el-proyecto.md): el `CA-02`, que la fase `A` dejó en rojo |
| **Fecha de cierre** | 2026-08-26 |
| **Versión del estándar al cerrar** | `35.1.0` |
| **Commit** | `a2d839d` |

> **Se ejecutó el 2026-08-22 y este documento se escribió el 2026-08-26.** Hasta entonces **era el molde sin llenar**, con sus 31 marcadores por reemplazar. El trabajo estaba hecho y probado; lo que faltaba era decir qué quedó.

---

## 1. Qué se implementó — resumen

**Una versión adoptada que no existe deja de pasar sin reporte.** La fase `A` había medido que un proyecto podía declarar `99.9.9` y nadie decía nada — y peor: esa versión inventada **silenciaba el aviso de desfase**, porque al ser mayor que la vigente el proyecto parecía estar adelantado.

**Y la versión declarada se compara contra el historial de adopciones.** Si el proyecto dice una cosa y su historial dice otra, se nombra a las dos.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem de la historia | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| `CA-02` una versión que no existe se detecta | servicio | `versiones_publicadas` y `ultima_adopcion` en [validadores/version.py](../../../../../validadores/version.py) | ✅ | Copia temporal declarando `99.9.9`: falla, y dice que no está en el registro |
| Lo que la fase `A` dejó en su `D-01` (crítica) | servicio | El mismo | ✅ | El caso real que lo destapó |
| Lo que la fase `A` dejó en su `D-02` (alta) | servicio | La comparación contra el historial | ✅ | Declara `1.0.0`, el historial dice `2.0.0`: falla y nombra las dos |

**Esta fase existe para cerrar lo que la `A` dejó en rojo**, y por eso su alcance es un solo criterio.

### 2.2 Plan de trabajo → ejecución

| Qué | Resultado |
|---|---|
| Lo que el plan pedía | ✅ hecho, y comprobado sobre casos reales |
| Defectos propios | **Ninguno** |

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Lo que no se hizo en su momento:** este documento. **La fase quedó cuatro días con su cierre en blanco**, y el inventario la contaba como completa porque el archivo existía. Ver §6.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Qué | Resultado |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple** |
| **Suite** | `test_la_version_adoptada_se_comprueba`: **10 pruebas, todas en verde** |
| **Defectos abiertos que se aceptaron** | Ninguno |

**Siete casos, y buena parte son de lo que NO debe hacer:**

| Caso | Qué sale |
|---|---|
| Versión que no existe | Falla, y dice que no está en el registro |
| Declarada distinta del historial | Falla, y nombra las dos |
| Proyecto al día | Silencio |
| Proyecto atrasado | Avisa, **no falla** |
| Sin historial de adopciones | **No** falla |
| Sin registro de cambios legible | **No** acusa a nadie |
| El último registro es el mayor | Gana `10.0.0`, no el último alfabético |

**Los cuatro casos de «no hacer» son los que sostienen el veredicto.** Una comprobación que reprueba de más se apaga a la semana, y entonces no comprueba nada.

**Y el último caso es el que más fácil se escapa:** ordenar versiones como texto pone `9.0.0` por encima de `10.0.0`.

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

```
python validadores/validar.py version --raiz <proyecto>
```

Compara lo que el proyecto declara contra el registro de versiones del estándar y contra su propio historial de adopciones.

---

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué |
|---|---|
| Una versión que **no existe** falla; una **atrasada** solo avisa | Declarar algo inexistente es un error; ir atrasado es una situación |
| Un proyecto **sin historial** no falla | Uno recién instalado no tiene con qué comparar, y reprobarlo sería reprobar el arranque |
| Si el registro de cambios **no se puede leer**, no se acusa a nadie | `04·R4`: no afirmar sobre lo que no se leyó. Sin saber qué versiones existen, no se puede decir que una no existe |
| Se compara **por número**, no como texto | `9.0.0` y `10.0.0` se ordenan al revés si se comparan letra por letra |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| **No se decide qué hacer cuando la declarada y el historial difieren.** Se dice que difieren, y decidir es del usuario | **A propósito.** Lo que se pedía era que se notara, no que se resolviera solo |
| La fase quedó con su **cierre en blanco cuatro días**, contada como completa | **Corregido acá.** Es lo que `S-052` describe, y esta fase es uno de los cuatro casos que lo destaparon |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] La historia [HU-003](../HU-003-version-adoptada-por-el-proyecto.md): su §8 nombra esta fase.
- [x] El pendiente que la originó, en `pendientes/hecho/`.
- [x] El inventario de historias, que **ya no se mantiene a mano** desde la `35.0.0`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

- **Migraciones a correr:** ninguna.
- **Qué cambia para quien ya tenía el estándar:** al correr `validar.py version` sobre su proyecto, una versión declarada que no exista **ahora falla**. Si declaraba una inventada, se va a enterar.
- **Reversión:** se descarta el commit. No hay estado que reconstruir.
