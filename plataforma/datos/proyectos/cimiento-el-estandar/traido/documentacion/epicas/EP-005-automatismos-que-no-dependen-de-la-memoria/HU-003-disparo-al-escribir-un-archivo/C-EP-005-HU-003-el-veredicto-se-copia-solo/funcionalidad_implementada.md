# Funcionalidad implementada — Fase «C-EP-005-HU-003-el-veredicto-se-copia-solo» (módulo «Automatismos — enganches»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito **qué quedó hecho**, con la trazabilidad de la historia y del plan, para que quien llegue después no tenga que deducirlo del código ni del historial.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `C-EP-005-HU-003-el-veredicto-se-copia-solo` |
| **Módulo** | Automatismos — enganches |
| **Especificación del módulo** | la del [plan_trabajo.md](plan_trabajo.md) §0 |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | [HU-003](../HU-003-disparo-al-escribir-un-archivo.md) (CA-04) |
| **Fecha de cierre** | 2026-08-20 |
| **Commit** | se completa al commitear; el usuario lo autoriza aparte |

## 1. Qué se implementó — resumen

Al escribir el `resultado_pruebas.md` de una fase con concepto en su §6, un enganche nuevo copia el veredicto a la fila de la fase en el §8 de su historia y a los README de la fase y de la historia, y dice qué tocó. El `estado-fase.md` no se toca. `cerrar.py` deja además la fila del índice del backlog en forma de hecho. Instalado en los nueve proyectos.

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem de la historia | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-04 · el veredicto llega a los tres sitios | programa | `validadores/veredicto.py` (`propagar`) | ✅ | CP-001, CP-002 |
| CA-04 · el borrador calla; el checkpoint no se toca | programa | `validadores/veredicto.py` | ✅ | CP-003, CP-004 |
| CA-04 · la fila «hecho» | programa | `validadores/cerrar.py` (`_fila_hecha`) | ✅ | CP-005 |
| Llega por el instalador | programa | `validadores/instalar.py` (`HOOKS_CLAUDE`) | ✅ | Salida del instalador, 9 de 9 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-01 | `veredicto.py` | ✅ hecha | `validadores/veredicto.py` | CP-001 a CP-004, CP-006 |
| T-02 | `hook_veredicto.py` y su fila en `HOOKS_CLAUDE` | ✅ hecha | `adaptadores/claude-code/hook_veredicto.py` · `validadores/instalar.py` | CP-001, CP-006 |
| T-03 | `cerrar.py`: la fila «hecho» | ✅ hecha | `validadores/cerrar.py` | CP-005 |
| T-04 | Los casos | ✅ hecha | `validadores/tests/test_el_veredicto_se_copia_solo.py` | 6 de 6 |
| T-05 | Especificación §4.7 y §13, mapas, instalar en los 9 | ✅ hecha | `documentacion/automatismos/spec.md` · `anatomia/` · `.claude/settings.json` de cada proyecto | Instalador 9 de 9 |

**Correspondencia con el plan:** 5 tareas en el plan, 5 acá.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba**  ·  [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md): ninguno.

**Esfuerzo real contra estimado:** cerca de media hora contra 4 h estimadas.

## 3. Qué se probó

- **Fuente:** [resultado_pruebas.md](resultado_pruebas.md) · **Veredicto:** Cumple.
- **Suites:** la de la fase (6 de 6) y las dos enteras.
- **Verificación sobre el repositorio real:** el cierre de las cuatro fases de hoy lo propagó el propio programa.
- **Defectos abiertos aceptados:** ninguno.

## 4. Cómo se usa / puntos de entrada

- **Punto de entrada:** el enganche `PostToolUse` sobre `Write|Edit`, instalado por `instalar.py`; y `cerrar.py`, que ya se pedía por nombre.

## 5. Decisiones no obvias  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Solo se propaga con concepto `cumple` o `no cumple` | Propagar el borrador pondría «no ejecutado» en la historia a cada guardado | S-013 |
| Se reutilizan `fases._concepto` y `_CONTEO` | Dos lecturas del §6 se desincronizan, y `fases.py` es la que decide la puerta | S-013 |
| El `estado-fase.md` no se toca | Es el checkpoint, criterio del agente (HU-013) | S-013 |

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino |
|---|---|---|
| El estado de la historia en su §1 («Hecha») no se copia: depende de todas sus fases | Diferido por el plan | Historia aparte si hace falta |

## 7. Índices y mapas actualizados

- [x] Especificación del módulo (§4.7, §13 y la tabla de incrementos).
- [x] Mapa del sitio y mapa del amarre (23 de 66).
- [x] README de la HU y de la fase al día, escritos por el propio programa.

## 8. Despliegue

Llega a cada proyecto con `python validadores/instalar.py --todos --aplicar`, ya corrido sobre los 9. Reversión: revertir el commit y volver a correr el instalador.
