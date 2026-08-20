# Funcionalidad implementada — Fase «A-EP-005-HU-014-el-aviso-por-tramo» (módulo «Automatismos — enganches»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito **qué quedó hecho**, con la trazabilidad de la especificación y del plan, para que quien llegue después no tenga que deducirlo del código ni del historial.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-005-HU-014-el-aviso-por-tramo` |
| **Módulo** | Automatismos — enganches |
| **Especificación del módulo** | [documentacion/automatismos/spec.md](../../../../automatismos/spec.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | [HU-014](../HU-014-el-consumo-se-ve-a-tiempo.md) (CA-01, CA-02, CA-03) |
| **Fecha de cierre** | 2026-08-20 |
| **Commit** | se completa al commitear; el usuario lo autoriza aparte |

## 1. Qué se implementó — resumen

El enganche de consumo corre también en cada mensaje del usuario y avisa una vez por cada millón de fichas (entrada más salida, sin caché) que la sesión cruza, sin estado compartido. El reporte de cierre de la 27.0.0 no cambió ni de texto ni de momento, y ahora tiene historia. Instalado en los nueve proyectos.

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| RN-36 · el reporte de cierre | programa | `adaptadores/claude-code/hook_presupuesto.py` (modo `cierre`) | ✅ | CP-001 |
| RN-37 · aviso por tramo, sin estado | programa | `validadores/presupuesto.py` (`cruzo_tramo`, `aviso_de_tramo`) | ✅ | CP-002, CP-003, CP-004 |
| RN-38 · el tramo por defecto es un millón | programa | `validadores/presupuesto.py` (`TRAMO`) | ✅ | CP-006 |
| RN-39 · mide, no detiene; sin transcripción calla | programa | `adaptadores/claude-code/hook_presupuesto.py` | ✅ | CP-005 |
| RN-07 de la HU · llega por el instalador | programa | `validadores/instalar.py` (`HOOKS_CLAUDE`) | ✅ | Salida del instalador, 9 de 9 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-01 | Caso que fija el reporte de cierre | ✅ hecha | `validadores/tests/test_el_consumo_se_ve_a_tiempo.py` | CP-001 |
| T-02 | `TRAMO`, `tramo()`, `cruzo_tramo()`, `aviso_de_tramo()` | ✅ hecha | `validadores/presupuesto.py` | CP-002 a CP-006 |
| T-03 | `--modo`, y en `aviso` imprimir solo si cruzó | ✅ hecha | `adaptadores/claude-code/hook_presupuesto.py` | CP-002 a CP-005 |
| T-04 | Fila `UserPromptSubmit` en `HOOKS_CLAUDE` | ✅ hecha | `validadores/instalar.py` | CP-008 |
| T-05 | Los casos | ✅ hecha | `validadores/tests/test_el_consumo_se_ve_a_tiempo.py` | 8 de 8 |
| T-06 | Especificación y mapa del sitio | ✅ hecha | `documentacion/automatismos/spec.md` §4.6 y §13 · `anatomia/mapa-del-sitio.md` | `validar.py estandar` OK |
| T-07 | Instalar en los 9 proyectos y verificar uno | ✅ hecha | `.claude/settings.json` de cada proyecto | AgroSystem trae `--modo aviso` |

**Correspondencia con el plan:** 7 tareas en el plan, 7 acá.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba**  ·  [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md): ninguno.

**Esfuerzo real contra estimado:** cerca de veinte minutos de sesión contra 3,25 h estimadas. Se sobreestimó por lo mismo que en la fase hermana.

## 3. Qué se probó

- **Fuente:** [resultado_pruebas.md](resultado_pruebas.md) · **Veredicto:** Cumple.
- **Suites ejecutadas:** `validadores/tests/test_el_consumo_se_ve_a_tiempo.py` 8 de 8; `TestPresupuesto` de `pruebas.py` sin cambios; las dos suites enteras, ver el resultado §2.
- **Verificaciones manuales:** el instalador sobre los 9 proyectos; el tiempo sobre la transcripción real más grande (CP-007).
- **Defectos abiertos aceptados:** ninguno.

## 4. Cómo se usa / puntos de entrada

- **Punto de entrada:** el mismo enganche en dos eventos: `Stop` sin argumentos (cierre) y `UserPromptSubmit --modo aviso`. El tramo se cambia con `--umbral` en el comando instalado.
- **Permisos o datos base:** ninguno.

## 5. Decisiones no obvias  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Un millón por tramo | Salió de ocho sesiones reales; 200 mil avisaría en todas | S-009 |
| Sin estado compartido | No hay archivo del proyecto donde marcar sin crear uno solo para esto | S-009 |
| `cierre` por defecto | Cambiar el comando instalado vence el enganche en los 9 proyectos (26.0.1) | S-009 |

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino |
|---|---|---|
| El modo `aviso` no convierte fichas a dinero | Diferido por el plan | Fuera de alcance de la HU; si algún día hace falta, historia nueva |

## 7. Índices y mapas actualizados

- [x] Especificación del módulo actualizada (§4.6, §13 y la tabla de incrementos).
- [x] Mapa del sitio al día.
- [x] README de la HU, de la fase y de la épica al día.
- N/A el mapa de dependencias y el catálogo de módulos.

## 8. Despliegue

N/A en el sentido de producción: el cambio llega a cada proyecto corriendo `python validadores/instalar.py --todos --aplicar`, que ya se corrió sobre los 9 del registro. Reversión: revertir el commit y volver a correr el instalador.
