# Pendiente: `cerrar_fase` lee todos los casos de prueba y marca todo lo que cierra

| | |
|---|---|
| **De dónde sale** | [H-2 · `cerrar_fase` lee un solo caso de prueba por fila de la matriz](../../cerrar-pendientes-145-a-149.md), en el resumen de la sesión del 2026-10-09 |

## El problema

`cerrar_fase` (`proyectos/cimiento/core/herramientas/fase.py`) arma el resultado de las pruebas desde la matriz del plan de pruebas, pero `Fase.casos()` (`fase.py:148`) solo reconoce las filas con un caso («CP-001»). Las filas con varios («CP-001, CP-002») las salta sin avisar. Al cerrar `A-EP-029-HU-008-danar-a-proposito` tomó 1 de 6 casos y dejó afuera dos de sus tres CA; el resultado se completó a mano. La fase `A-EP-026-HU-011-manage-py-busca-su-python` usa el mismo formato.

Tampoco marca, en la segunda pasada:

- las filas de la matriz con varios casos;
- los CA del plan de trabajo escritos como enlace (`| [CA-01](…) | ☐ |`);
- la columna «Verificado» y el estado de la sección 5 del plan de trabajo;
- las casillas de la Definition of Done del plan y de la HU, y las tareas técnicas de la HU.

En las fases de EP-029·HU-008 y EP-025·HU-030 se marcaron a mano.

## Por qué importa

El resultado de las pruebas dice menos casos de los que hubo y el veredicto deja CA afuera, sin avisar. Lo que queda sin marcar hay que encontrarlo y marcarlo a mano en cada cierre.
