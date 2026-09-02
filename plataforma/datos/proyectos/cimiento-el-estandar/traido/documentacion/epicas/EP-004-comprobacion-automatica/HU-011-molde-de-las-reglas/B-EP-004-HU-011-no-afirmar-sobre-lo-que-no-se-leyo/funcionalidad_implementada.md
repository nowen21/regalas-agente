# Funcionalidad implementada — Fase `B-EP-004-HU-011-no-afirmar-sobre-lo-que-no-se-leyo` (módulo Programas de comprobación)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-004-HU-011-no-afirmar-sobre-lo-que-no-se-leyo` |
| **Módulo** | Programas de comprobación |
| **Especificación del módulo** | La propia [HU-011](../HU-011-molde-de-las-reglas.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), abierto el 2026-08-22 |
| **HU / CA cubiertas** | [HU-011](../HU-011-molde-de-las-reglas.md): que la comprobación de meta-reglas no juzgue lo que no es el estándar |
| **Fecha de cierre** | 2026-08-27 |
| **Versión del estándar al cerrar** | `35.1.0` |
| **Commit** | `a2d839d` |

> **Se ejecutó el 2026-08-22 y este documento se escribió el 2026-08-27.** Hasta entonces **era el molde sin llenar**. El trabajo estaba hecho y probado; lo que faltaba era decir qué quedó.

---

## 1. Qué se implementó — resumen

**La comprobación de meta-reglas dejó de dar veredictos sobre carpetas que no son el estándar.** Apuntada a un proyecto con `--raiz`, juzgaba sus documentos con las reglas del cuerpo normativo y reportaba incumplimientos que no lo eran.

**Ahora reconoce si la carpeta es el estándar**, y si no lo es **dice qué usar en su lugar** en vez de callarse.

**Medido sobre un proyecto real:** en AgroSystem pasó de **una falla y cuatro avisos falsos** a **un aviso que nombra la bandera correcta**.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem | Categoría | Estado | Evidencia |
|---|---|---|---|
| No juzgar lo que no es el estándar | servicio | ✅ | Sobre AgroSystem: de 1 falla y 4 avisos falsos a 1 aviso útil |
| Reconocer el estándar | servicio | ✅ | Tiene cuerpo de reglas **y** versión |
| Y seguir comprobando donde sí corresponde | servicio | ✅ | Sobre el repositorio real, sin el aviso de carpeta ajena |

**El aviso dice qué usar en su lugar.** Callarse habría sido igual de correcto y mucho menos útil: quien apuntó mal se quedaría sin saber por qué no salió nada.

### 2.2 Plan de trabajo → ejecución

| Qué | Resultado |
|---|---|
| Lo que el plan pedía | ✅ hecho, medido sobre un proyecto real |
| Defectos propios | **Ninguno** |

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Lo que no se hizo en su momento:** este documento. **La fase quedó cinco días con su cierre en blanco.**

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Qué | Resultado |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple** |
| **Suites** | `test_metareglas_no_afirma_sobre_un_proyecto` (7) y `test_checklist_cadena` (3). Todas en verde |
| **Defectos abiertos que se aceptaron** | Ninguno |

**Seis casos, y los bordes son los que definen el reconocimiento:**

| Caso | Qué sale |
|---|---|
| Apuntar a un proyecto | Ninguna falla, y un aviso que nombra la bandera buena |
| El estándar se reconoce | Sí: tiene cuerpo de reglas y versión |
| **Cuerpo de reglas pero sin versión** | **No** es el estándar: está a medio instalar |
| Sobre el estándar sigue comprobando | Sin el aviso de carpeta ajena |
| Sin los archivos, no se reporta nada | Silencio |
| Con los archivos, sigue comprobando | Falla, y con el dato en el mensaje |

**El tercer caso es el que hace que el reconocimiento sirva.** Pedir solo el cuerpo de reglas daría por estándar a cualquier proyecto a medio instalar, y volveríamos al problema.

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

```
python validadores/validar.py metareglas
```

Sobre el estándar, comprueba. Sobre un proyecto, **avisa qué usar en su lugar**: `validar.py metareglas --catalogo <proyecto>`.

---

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué |
|---|---|
| Se reconoce por **cuerpo de reglas y versión**, no por uno solo | Un proyecto a medio instalar tiene lo primero. Pedir los dos cierra el borde |
| Cuando no es el estándar, **se avisa qué usar**, no se calla | Callarse deja a quien apuntó mal sin saber por qué no salió nada |
| Sin los archivos **no se reporta nada** | `04·R4`: no afirmar sobre lo que no se leyó |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| **El reconocimiento dejó una prueba comprobando el rechazo en vez de la regla** | **Detectado y corregido el 2026-08-26**, cuatro días después: el árbol de mentira de `test_una_regla_nueva_sin_clasificar_se_avisa` no traía `VERSION`, así que el validador se negaba a mirarlo y la prueba comprobaba esa negativa. Queda en `H-26` del resumen |
| La fase quedó con su **cierre en blanco cinco días**, contada como completa | **Corregido acá.** Es uno de los cuatro casos que destaparon `S-052` |

**La primera deuda merece leerse.** Este cambio era correcto y aun así **dejó una prueba en verde comprobando lo contrario de lo que su nombre decía**. No lo vio nadie hasta que se corrió la suite completa cuatro días después — y es exactamente el costo de que la batería de antes de publicar no corra las pruebas, que es la deuda `D-01` de [`A-EP-005-HU-006`](../../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-006-bateria-antes-de-publicar/A-EP-005-HU-006-la-bateria-antes-de-publicar/funcionalidad_implementada.md).

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] La historia [HU-011](../HU-011-molde-de-las-reglas.md): su §8 nombra esta fase.
- [x] El pendiente que la originó, en `pendientes/hecho/`.
- [x] El inventario de historias, que **ya no se mantiene a mano** desde la `35.0.0`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

- **Migraciones a correr:** ninguna.
- **Qué cambia para quien ya tenía el estándar:** apuntar `metareglas` a un proyecto **deja de dar incumplimientos falsos** y dice qué usar en su lugar.
- **Reversión:** se descarta el commit.
