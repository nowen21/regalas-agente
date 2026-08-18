# Funcionalidad implementada — Fase A-EP-007-HU-002-retrodocumentar-el-mostrar-antes-de-hacer (módulo Instalación)

> **Veredicto de la fase: [No cumple](resultado_pruebas.md#6-veredicto-de-la-fase).** El modo que muestra existe, es el comportamiento por omisión y **no escribe ni un archivo**. Falla el CA-02: la simulación dice que no hay registro de versión que escribir, y al aplicar lo escribe.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-007-HU-002-retrodocumentar-el-mostrar-antes-de-hacer` |
| **Módulo** | Instalación — [`validadores/instalar.py`](../../../../../validadores/instalar.py) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / exigencias cubiertas** | HU-002: CA-01, CA-02 y sus dos transversales |
| **Fecha de cierre** | 2026-08-17 · **Commit** pendiente de autorización |

---

## 1. Qué se implementó — resumen

**Nada de programa: la fase comprobó una promesa que nadie había medido.** El instalador simula por omisión desde que existe, y hasta hoy «no toca nada» era algo que se creía. Ahora está comprobado listando el proyecto entero antes y después.

Y comparar lo anunciado con lo hecho destapó que **no coinciden**.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| Simular es lo que pasa por omisión | programa | [`instalar.py`](../../../../../validadores/instalar.py) · `main()` | ✅ Ya existía | CP-002 |
| Decirlo antes de empezar | programa | `MODO SIMULACIÓN — no se modifica nada` | ✅ Ya existía | CP-001 |
| No escribir nada al simular | programa | El parámetro `aplicar` en cada paso | ✅ Ya existía | CP-002 |
| **Anunciar todo lo que se va a escribir** | programa | El paso del registro de versión decide sobre un estado que aún no existe | ❌ **No se cumple** | CP-003 |
| Las cuatro exigencias, con red | pruebas | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `MostrarAntesDeHacer` | ✅ Escritas acá | 4 pruebas |

### Criterios de aceptación

| CA | Cómo quedó | Estado |
|---|---|---|
| CA-01 | Simular no escribe ni un archivo, y lo dice en su primera línea | ✅ |
| CA-02 | 12 de 13 anunciados; el registro de versión aparece sin anunciarse | ❌ |
| Transversal · Límites | Un proyecto al día no anuncia trabajo, y lo dice | ✅ |
| Transversal · Claridad | Cada línea dice qué se hace y sobre qué | ✅ |

---

## 3. Lo que la fase midió

| Medición, 2026-08-17, sobre un proyecto vacío con git | Valor |
|---|---:|
| Archivos escritos **al simular** | **0** |
| Líneas que anuncia la simulación | **27** |
| Archivos que aparecen **al aplicar** | **13** |
| De esos, **anunciados** | 12 |
| **Sin anunciar** | **1** — `documentacion/versiones/<fecha>-<version>.md` |
| Líneas de «crear» al simular sobre un proyecto ya instalado | **0** |

---

## 4. El defecto, y por qué no es un detalle

La simulación no se limita a olvidar el archivo: **dice lo contrario**.

> `(simulado) versiones: ni las plantillas ni la versión cambiaron, no hay actualización que registrar`

**La causa:** el registro se decide comparando huellas. Al simular todavía no se copió nada, así que la comparación no ve cambios; al aplicar, los archivos ya están y la comparación sí los ve.

**Por qué importa:** el archivo que aparece sin anunciarse es **el que deja constancia de qué se instaló**, y va en `documentacion/`, que es carpeta del proyecto. Quien lea la simulación para decidir si autoriza no lo va a ver.

**Mostrar mal es peor que no mostrar**, porque quien lee decide creyendo que ya vio todo.

**No se arregló acá:** `instalar.py` no está en los archivos que §2.1 del plan declara.

---

## 5. Decisiones y señales

| Decisión | Dónde quedó |
|---|---|
| El CA-01 se comprueba **listando el proyecto entero** antes y después, no leyendo la salida: la salida es justamente lo que se está poniendo a prueba | CP-002 |
| El CA-02 se comprueba comparando **conjuntos de archivos**, no líneas de texto: lo que importa es qué aparece, no cómo se dijo | CP-003 |
| «Cancelar» no es un aviso interactivo sino **no escribir `--aplicar`**, y se deja dicho por qué es mejor: un «¿seguro?» se contesta que sí sin leerlo | CP-004 del [resultado](resultado_pruebas.md) |

---

## 6. Lo que no entró, y dónde sigue

| Qué | Dónde |
|---|---|
| Que la simulación anuncie el registro de versión (`D-01`) | Fase `B-EP-007-HU-002`, propuesta |
| Instalar con una sola línea | [HU-001](../../HU-001-instalar-con-una-linea/HU-001-instalar-con-una-linea.md), ya cerrada |
| No pisar lo escrito | [HU-005](../../HU-005-no-pisar-lo-escrito/HU-005-no-pisar-lo-escrito.md) |

**La advertencia que deja esta fase:** el modo que muestra estaba bien hecho y nadie lo había comprobado. Lo que falla no es que escriba de más: es que **afirma que no va a escribir algo que escribe**, y esa clase de error solo se ve comparando las dos corridas.
