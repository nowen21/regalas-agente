# Pendiente · La plantilla del plan de trabajo se puede comprobar

> Unido en el [pendiente 103](103-cada-documento-de-la-cadena-sale-del-anterior.md).

**Estado:** abierto. Espera la aprobación del usuario.

| | |
|---|---|
| **Historia de usuario** | Por asignar: nace al aprobarse este pendiente |
| **De dónde sale** | [H-11 de la sesión del 2026-09-28](../historico-chat/resumenes/2026-09-28/sesion.md), sobre por qué el agente olvida las reglas |
| **Proyecto de origen** | El estándar mismo |

## El problema

La tabla 2.1 de [plantillas/ciclo-vida-proyectos/07-plan-trabajo.md](../plantillas/ciclo-vida-proyectos/07-plan-trabajo.md) acepta filas como «`validadores/docs/`» o «Los documentos de esta fase», que un programa no puede comparar con una ruta. La plantilla no tiene un campo de quién aprobó el plan y cuándo, ni una sección para las ampliaciones aprobadas: la sección 12 del plan de la fase `C` de HU-023 se agregó a mano.

## Por qué importa

La plantilla ya dice dos veces que no se toca un archivo fuera de la tabla (`02·F8`), y el agente lo incumplió igual. Sin rutas exactas ni fecha de aprobación, el freno del [pendiente 105](105-nada-se-ejecuta-fuera-del-plan-aprobado.md) no puede saber qué está permitido ni desde cuándo.

## Qué falta

1. **Rutas exactas en la tabla 2.1**, o carpetas declaradas como carpetas.
2. **Un campo de aprobación** del plan, con quién y cuándo.
3. **Una sección fija de ampliaciones:** qué cambia, qué archivos suma, quién la aprobó y cuándo.

## El límite

- No cambia los planes ya cerrados.
- El freno que lee la plantilla es del pendiente 105.
- Depende del [pendiente 103](103-cada-documento-de-la-cadena-sale-del-anterior.md), que fija de dónde sale cada tarea del plan.

## Cómo se sabrá que cerró

- La plantilla tiene los tres cambios.
- Un programa lee la tabla 2.1 y la aprobación de un plan de prueba.
- `python validadores/validar.py estandar` termina sin incumplimientos.
