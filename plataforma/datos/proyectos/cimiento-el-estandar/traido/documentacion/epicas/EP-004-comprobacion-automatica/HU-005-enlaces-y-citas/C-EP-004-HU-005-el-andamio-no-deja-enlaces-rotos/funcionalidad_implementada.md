# Funcionalidad implementada — Fase «C-EP-004-HU-005-el-andamio-no-deja-enlaces-rotos» (módulo «Programas de comprobación — el andamio»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito **qué quedó hecho**, con la trazabilidad de la historia y del plan, para que quien llegue después no tenga que deducirlo del código ni del historial.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `C-EP-004-HU-005-el-andamio-no-deja-enlaces-rotos` |
| **Módulo** | Programas de comprobación — el andamio |
| **Especificación del módulo** | la del [plan_trabajo.md](plan_trabajo.md) §0 |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | [HU-005](../HU-005-enlaces-y-citas.md) (CA-05) |
| **Fecha de cierre** | 2026-08-20 |
| **Commit** | se completa al commitear; el usuario lo autoriza aparte |

## 1. Qué se implementó — resumen

El andamio traslada, al copiar cada plantilla, los enlaces que llegan a la raíz del repositorio y el marcador `«RUTA-ESTANDAR»` a la ruta que corresponde desde la carpeta de la fase. Un esqueleto recién levantado pasa el validador de enlaces sin tocarlo. Las siete fases levantadas hoy antes del arreglo se habían corregido a mano; las que vengan nacen bien.

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem de la historia | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-05 · lo que un programa escribe no nace con enlaces rotos | programa | `validadores/andamio.py` (`_reenlazar`) | ✅ | CP-001, CP-002 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-01 | `_reenlazar()` llamada por `crear()` para cada plantilla | ✅ hecha | `validadores/andamio.py` | CP-001 a CP-003 |
| T-02 | Los casos | ✅ hecha | `validadores/tests/test_el_andamio_no_deja_enlaces_rotos.py` | 3 de 3 |

**Correspondencia con el plan:** 2 tareas en el plan, 2 acá.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba**  ·  [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md): ninguno.

**Esfuerzo real contra estimado:** cerca de diez minutos contra 1 h estimada.

## 3. Qué se probó

- **Fuente:** [resultado_pruebas.md](resultado_pruebas.md) · **Veredicto:** Cumple.
- **Suites:** la de la fase (3 de 3) y las dos enteras, ver el resultado §2.
- **Defectos abiertos aceptados:** ninguno.

## 4. Cómo se usa / puntos de entrada

- **Punto de entrada:** el mismo de siempre, `python validadores/andamio.py <épica> <HU> <descripción> --aplicar`. No hay nada nuevo que pedir.

## 5. Decisiones no obvias  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Reescribir al copiar calculando el prefijo con `relpath` | Poner el marcador en la plantilla del resultado; las plantillas quedan como están | S-010 |
| Solo el prefijo que llega exactamente a la raíz; un `../` que se queda en `plantillas/` o que la pasa no se toca | Reescribir cualquier `../` | S-010 |

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino |
|---|---|---|
| Ninguna | — | — |

## 7. Índices y mapas actualizados

- [x] README de la HU y de la fase al día (la fila de la historia la escribió `veredicto.py`, recién construido en la fase `C-EP-005-HU-003`).
- N/A mapas y catálogo.

## 8. Despliegue

N/A: el andamio corre en el repositorio del estándar. Reversión: revertir el commit.
