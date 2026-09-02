# Funcionalidad implementada — Fase `B-EP-007-HU-002-el-registro-de-version-se-anuncia` (módulo Instalación)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-007-HU-002-el-registro-de-version-se-anuncia` |
| **Módulo** | Instalación |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-30 |
| **HU / CA cubiertas** | [HU-002](../HU-002-mostrar-antes-de-hacer.md): el CA-02 |
| **Fecha de cierre** | 2026-08-30 |
| **Versión del estándar al cerrar** | `35.10.0`, **sin cambio**: no se toca `base/` ni `plantillas/` |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | Pendiente de autorización |
| **Reemplaza el veredicto de** | `A-EP-007-HU-002-retrodocumentar-el-mostrar-antes-de-hacer` |

> **Por qué se declara el reemplazo:** el defecto `D-01` de aquella fase quedó cerrado, con su prueba fuera del fallo esperado. Aquel rojo era cierto el 2026-08-22. **El veredicto de aquella fase no se toca** (`20·M11`).

---

## 1. Qué se implementó — resumen

**Que la simulación del instalador anuncie el registro de versión.**

Anunciaba 12 de 13 archivos. El que faltaba era el que deja constancia de qué se
instaló. La causa: `registrar_version` comparaba el proyecto **consigo mismo**,
y en simulación todavía no se ha copiado nada, así que no había ningún cambio
que ver.

| Antes | Ahora |
|---|---|
| «ni las plantillas ni la versión cambiaron, no hay actualización que registrar» | `registrar documentacion/versiones/<fecha>-<versión>.md` |
| Al aplicar, el registro aparecía sin anunciarse | Aparece el que se anunció |

Dos cambios, y los dos hacían falta: comparar la huella **prevista** para que la
simulación sepa que va a registrar, y nombrar **el archivo** para que lo diga.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| CA-02 | servicio | `validadores/instalar.py`, `validadores/versiones.py` | ✅ | CP-003 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Estado | Evidencia |
|---|---|---|
| T-01 · reproducir el defecto | ✅ | La prueba, escrita como fallo esperado |
| T-02 · comparar la huella prevista | ✅ | `_huellas_previstas` |
| T-03 · anunciar el archivo | ✅ | `versiones.nombre_previsto` |
| T-04 · sacar la prueba del fallo esperado | ✅ | 4 de 4 en verde |

**Correspondencia:** 4 tareas, 4 con resultado.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, ciclo 1 |
| **Suites ejecutadas** | `pruebas.MostrarAntesDeHacer`: 4 pruebas, 4 en verde, 0 fallos esperados |
| **Defectos abiertos** | Ninguno nuevo |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Sin punto de entrada nuevo:

```
python validadores/instalar.py <proyecto>              ← simula, y ahora lo dice completo
python validadores/instalar.py <proyecto> --aplicar    ← instala
```

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué |
|---|---|
| Al simular se compara la huella **prevista** | Simular no escribe, así que mirar el proyecto de ahora es mirarse en el espejo equivocado |
| Se anuncia el archivo, no la carpeta | Anunciar el sitio deja la cosa fuera de lo que después se compara |
| El nombre se predice con la función que lo elige | Calculado en dos sitios, el anuncio y el archivo se separan el día que uno cambie |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| El defecto `D-02` de la fase `A`: una línea del anuncio es la orden literal de git | **Abierto.** No deja ningún CA en «No» |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] El `Estado` de la historia y su tabla de fases.
- [ ] `VERSION` y `CHANGELOG.md`: **no aplica**, no se toca `base/` ni `plantillas/`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**Nada que desplegar.** Se nota la próxima vez que alguien corra el instalador
sin `--aplicar`.
