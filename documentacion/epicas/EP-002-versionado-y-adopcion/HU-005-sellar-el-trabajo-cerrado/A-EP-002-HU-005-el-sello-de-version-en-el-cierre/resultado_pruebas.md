# Resultado de Pruebas — Fase A-EP-002-HU-005-el-sello-de-version-en-el-cierre

**Para qué sirve este documento.** Registra qué se ejecutó y con qué resultado. Los casos viven en el [plan_pruebas.md](plan_pruebas.md), que no se toca al ejecutar.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-002-HU-005-el-sello-de-version-en-el-cierre` |
| **HU** | [HU-005 Sellar el trabajo cerrado](../HU-005-sellar-el-trabajo-cerrado.md) |
| **Ciclo** | 1 · **Fecha** 2026-08-22 |
| **Ejecutado por** | El agente, por la orden del usuario de resolver el [pendiente 59](../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md) |

### 0.1 Las dos dudas que la detenían

| Duda | Decisión |
|---|---|
| ¿el validador lo exige o solo lo avisa? | **Avisa**, y no por comodidad: un cierre sin sello **no rompe nada hoy**, solo deja sin respuesta la pregunta de bajo qué reglas cerró. La regla del día, escrita en el pendiente 59, es detener lo que impide trabajar y avisar lo que solo informa mal |
| ¿el campo entra en los dos modelos o solo en el del cierre? | **Solo en el del cierre** (decisión 28). Al abrir la fase todavía no hay nada que sellar, y un campo que se llena con «pendiente» es un campo que nadie llena |

## 1. Resumen

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos |
|---|---:|---:|---:|---:|
| 1 | 5 | 5 | 5 | 0 |

## 2. Caso por caso

| Caso | Qué comprueba | Resultado |
|---|---|---|
| CP-001 · el cierre sin sello se detecta, y el que lo tiene pasa | el corazón del CA | ✅ Aprobado: `validar.py fases` lo reporta como aviso |
| CP-002 · el campo pide de dónde salió el número | «del archivo `VERSION` en el momento de cerrar» | ✅ Aprobado, escrito en el propio molde |
| CP-003 · la fase cerrada bajo una versión anterior no se reporta por reglas posteriores | es el motivo de existir del sello | ✅ Aprobado: lo cerrado antes del 2026-08-22 queda fuera |
| CP-004 · la derogación sin adoptar detiene la fase en curso, no la cerrada | ya lo hacía [`02·F22`](../../../../../base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md) | ✅ Aprobado |
| CP-005 · el sello está desde el estado de la fase | se lee sin abrir el cierre | ✅ Aprobado: el estado enlaza al cierre, que lo trae en su cabecera |

## 3. Lo que se construyó, y lo que se selló

**El molde del cierre gana el campo** «Versión del estándar al cerrar», con la caja que dice para qué sirve: sin él, una regla nueva de mañana parece incumplida hoy.

**Y `validar.py fases` lo comprueba**, reconociendo las dos formas: la fila del molde y la frase suelta. El molde es lo que se pide, pero un cierre escrito a mano que diga «cerrada el 22 de agosto con el estándar en la 31.8.0» dice exactamente lo mismo, y reportarlo sería reportar la forma en vez del contenido.

**Los quince cierres escritos hoy quedaron sellados**, cada uno con la versión bajo la que de verdad cerró, de la 30.9.1 a la 31.8.0.

## 4. Defectos encontrados

**Uno, y del propio trabajo de hoy:** los cierres que se escribieron durante la jornada no traían el campo, porque el campo no existía cuando se escribieron. Se sellaron los quince. **Lo anterior no se toca:** `20·M10` dice que un cambio de norma no reabre lo cerrado, y este campo es justamente el que lo hace comprobable.

## 5. Veredicto

**Cumple.** Cinco casos de cinco.
