# Resultado de Pruebas — Fase A-EP-004-HU-009-el-conteo-de-hallazgos-por-regla

**Para qué sirve este documento.** Registra qué se ejecutó y con qué resultado. Los casos viven en el [plan_pruebas.md](plan_pruebas.md), que no se toca al ejecutar.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-004-HU-009-el-conteo-de-hallazgos-por-regla` |
| **HU** | [HU-009 Conteo por regla](../HU-009-conteo-por-regla.md) |
| **Ciclo** | 1 · **Fecha** 2026-08-22 |
| **Ejecutado por** | El agente, por la orden del usuario de resolver el [pendiente 59](../../../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md) |

### 0.1 Las dos dudas que la detenían

| Duda | Decisión |
|---|---|
| ¿dónde vive el registro: versionado, no versionado o solo en la salida? | **No versionado**, decisión 25 del pendiente 59: [`09·G3`](../../../../../base/09-git.md) deja fuera lo generado, y su contenido cambia en cada corrida |
| ¿espera a la corrida completa de HU-008? | **No esperaba: hoy ya existe.** Se construyó en esta misma jornada, y el conteo se enganchó a ella, que es donde tiene sentido: contar exige haber corrido todo |

## 1. Resumen

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos |
|---|---:|---:|---:|---:|
| 1 | 4 del plan, 11 escritos | 11 | 11 | 0 |

## 2. Caso por caso

| Caso | Qué comprueba | Resultado |
|---|---|---|
| CP-001 · la corrida deja el conteo agrupado por regla | y la regla sale del mensaje que el validador ya escribe | ✅ Aprobado, con cuatro casos: deducción, prioridad del capítulo, regla declarada y lo que no nombra ninguna |
| CP-002 · el registro no contiene la clave del archivo revisado | **el caso que decide** | ✅ Aprobado: se guarda `04·S4` y el número; no la clave, no la ruta, no el mensaje |
| CP-003 · dos corridas con un arreglo en medio muestran la baja | para eso se guarda | ✅ Aprobado: lo que no cambió no se reporta |
| CP-004 · el campo nuevo no rompe nada | `Hallazgo` lo usan los 24 validadores | ✅ Aprobado: se imprime igual, y una línea rota del registro no se lleva el resto |

## 3. La primera corrida real, que es el dato que faltaba

```
$ python validadores/validar.py todo
…
Hallazgos por regla (3552 en total):
  00·ID8       2391
  (sin regla)  603
  F18          296
  S3            85
  F2            36
```

**Y ese primer número ya dice algo.** `00·ID8` —las marcas de generación automática— produce **dos de cada tres hallazgos del repositorio**. No es que se incumpla más: es que se mide sobre todo el árbol, incluidos el histórico y los documentos de trabajo, mientras la regla exige limpieza en lo que se **entrega**. Es exactamente la clase de conversación que este conteo vino a hacer posible, y queda anotada para quien mire la regla.

## 4. Defectos encontrados

**Ninguno del conteo.** Y una decisión de diseño que vale escribir: los hallazgos se acumulan en `comun.reportar`, por donde pasan todos, en vez de pedirle a cada validador que además los devuelva. Tocar veinticuatro archivos para saber algo que ya pasa por un solo punto habría sido el camino largo y frágil.

## 4.1 Lo que otro validador encontró sobre esta misma fase

**El comparador de plan contra lo hecho, construido media hora después, dijo que esta fase tocó tres archivos que su plan no declaraba:** `validadores/conteo.py`, su contrato y su archivo de pruebas. Es cierto: el plan, escrito el 2026-08-17, daba por hecho que el conteo viviría dentro de `validar.py`, y al construirlo se vio que convenía un módulo propio.

**La decisión fue buena y el procedimiento no:** ampliar el plan exige escribirlo antes de ejecutar ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)). Queda dicho acá, que es donde alguien lo va a buscar.

## 5. Veredicto

**Cumple.** Once casos de once.
