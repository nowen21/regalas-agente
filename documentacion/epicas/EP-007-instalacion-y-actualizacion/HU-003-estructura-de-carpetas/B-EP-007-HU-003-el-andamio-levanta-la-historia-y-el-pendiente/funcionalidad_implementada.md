# Funcionalidad implementada — Fase «B-EP-007-HU-003-el-andamio-levanta-la-historia-y-el-pendiente» (módulo «Instalador — el andamio»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito **qué quedó hecho**, con la trazabilidad de la historia y del plan, para que quien llegue después no tenga que deducirlo del código ni del historial.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `B-EP-007-HU-003-el-andamio-levanta-la-historia-y-el-pendiente` |
| **Módulo** | Instalador — el andamio |
| **Especificación del módulo** | la del [plan_trabajo.md](plan_trabajo.md) §0 |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | [HU-003](../HU-003-estructura-de-carpetas.md) (CA-04) |
| **Fecha de cierre** | 2026-08-20 |
| **Commit** | se completa al commitear; el usuario lo autoriza aparte |

## 1. Qué se implementó — resumen

El andamio acepta dos modos más: `hu`, que crea la historia desde `plantillas/HU.md` con su README y sus filas en el §9 de la épica y en el README de la épica; y `pendiente`, que crea el pendiente desde el molde nuevo `plantillas/pendiente.md` con su fila en el índice del backlog y su historia en el mapa. El número se lee del disco, el siguiente al mayor. No escribe contenido: los `«…»` quedan.

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem de la historia | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-04 · la historia nace con su esqueleto y sus índices | programa | `validadores/andamio.py` (`crear_hu`, `siguiente_hu`, `_agregar_fila`) | ✅ | CP-001, CP-002 |
| CA-04 · el pendiente nace con su fila y su historia en el mapa | programa | `validadores/andamio.py` (`crear_pendiente`, `_mapa`) · `plantillas/pendiente.md` | ✅ | CP-003 |
| CA-04 · sin contenido | programa | `validadores/andamio.py` | ✅ | CP-004 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-01 | `plantillas/pendiente.md` y su fila en el README de plantillas | ✅ hecha | `plantillas/pendiente.md` · `plantillas/README.md` | CP-003 |
| T-02 | `crear_hu()` | ✅ hecha | `validadores/andamio.py` | CP-001, CP-002, CP-004, CP-005 |
| T-03 | `crear_pendiente()` | ✅ hecha | `validadores/andamio.py` | CP-003 |
| T-04 | `main()` con los tres modos | ✅ hecha | `validadores/andamio.py` | CP-006 |
| T-05 | Los casos | ✅ hecha | `validadores/tests/test_el_andamio_levanta_la_historia_y_el_pendiente.py` | 7 de 7 |

**Correspondencia con el plan:** 5 tareas en el plan, 5 acá.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba**  ·  [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md): ninguno.

**Esfuerzo real contra estimado:** cerca de media hora contra 3,5 h estimadas.

## 3. Qué se probó

- **Fuente:** [resultado_pruebas.md](resultado_pruebas.md) · **Veredicto:** Cumple.
- **Suites:** la de la fase (7 de 7) y las dos enteras.
- **Defectos abiertos aceptados:** ninguno.

## 4. Cómo se usa / puntos de entrada

- **Punto de entrada:** `python validadores/andamio.py hu <épica> <slug> --aplicar` y `python validadores/andamio.py pendiente <slug> --hu <épica>/<HU> --aplicar`. Sin `--aplicar` simulan.

## 5. Decisiones no obvias  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| El número de la historia es el siguiente al mayor, no el primer hueco | Como los pendientes: se cita por número. Las fases sí toman el primer hueco, porque su letra vive dentro de la historia | S-012 |
| Los enlaces de la plantilla se trasladan antes de poner los propios | Al revés, el `../epica.md` recién puesto se trasladaba también: lo atrapó CP-005 | S-012 |
| La fila del backlog va a «Sin agrupar todavía» | Pedir la sección por argumento: agrupar es criterio | S-012 |

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino |
|---|---|---|
| El estado de la historia en su §1 y en la épica no lo toca el andamio ni `veredicto.py` | Diferido por el plan | Depende de todas sus fases; historia aparte si hace falta |

## 7. Índices y mapas actualizados

- [x] `plantillas/README.md` y el mapa del sitio con el molde nuevo (25 moldes).
- [x] README de la HU y de la fase al día.
- N/A mapas de dependencias y catálogo.

## 8. Despliegue

N/A: el andamio corre en el repositorio del estándar. Reversión: revertir el commit.
