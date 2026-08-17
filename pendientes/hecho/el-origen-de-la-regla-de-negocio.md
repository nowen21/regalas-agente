# Hecho · Toda regla de negocio dice de dónde baja

Origen: pendiente 43, abierto y cerrado el 2026-08-16, versiones **22.0.0** y **22.1.0**.

| | |
|---|---|
| **Proyecto de origen** | **`shopnest-mesa`** · `C:/DesarrollosClaude/personales/shopnest-mesa` |
| **Su pendiente de seguimiento** | `pendientes/05-la-plantilla-de-spec-no-pide-la-fuente.md` — **falta avisarle** para que lo cierre |
| **Dónde se construyó** | Dos fases, una por módulo (`02·F11`): [`A-EP-003-HU-004`](../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-004-modelo-de-la-especificacion/A-EP-003-HU-004-el-origen-de-la-regla-de-negocio/) el molde, y [`A-EP-004-HU-004`](../../documentacion/epicas/EP-004-comprobacion-automatica/HU-004-forma-de-los-documentos/A-EP-004-HU-004-la-regla-de-negocio-declara-su-origen/) el programa que lo comprueba |

## Qué pasaba

El §4 de la plantilla de especificación pedía `«Regla — por qué existe.»`. **El porqué, nunca el de dónde.**

Una regla de negocio no se inventa en la especificación de un módulo: baja de un requisito, de una historia o de una decisión. Como nadie lo preguntaba, una regla con buena justificación y ninguna procedencia entraba sin resistencia y sin dejar rastro de que entró.

## El caso que lo destapó

En `shopnest-mesa`, la regla 5 de `documentacion/problemas/spec.md`:

> **Un problema no se cierra sin causa raíz ni solución definitiva.** Cerrar un problema es afirmar que ya no va a volver, y eso no se puede afirmar sin saber por qué pasaba ni qué se hizo.

Impecable como justificación, y no la pedía nadie: ni el enunciado del taller, ni `RF-13` —que manda *registrar* esos campos, no exigirlos al cerrar—, ni la épica, ni la historia. **Nació en la especificación del módulo**, y de ahí bajó sola a una decisión, una fila de trazabilidad, dos escenarios de prueba y un criterio de aceptación. Tardó un día en verse, y solo porque alguien preguntó de dónde salía.

## Cómo cerró

**1 · El molde pide las dos cosas** (v22.0.0, MAYOR): `«Regla — de dónde baja (el identificador del requisito, la historia o la decisión) — por qué existe.»`, con la nota de que la regla sin procedencia no se escribe ahí — se sube a la historia que corresponda y baja desde allá. Se pide un identificador y no una frase: «lo pidió el cliente» no se puede seguir hasta ninguna parte.

**2 · Un programa lo comprueba** (v22.1.0, MENOR): `reglas_sin_origen()` en [`validadores/plantillas.py`](../../validadores/plantillas.py) marca como **falla** cada regla del §4 sin identificador. Es falla y no aviso porque una regla sin fuente ya llegó hasta un criterio de aceptación; lo que avisa, se ignora.

**Un hallazgo que no buscaba nadie:** un archivo `spec.md` **no se comparaba contra ninguna plantilla**. El programa no sabía cuál le tocaba, así que el documento más importante de un módulo era invisible para el validador de forma. Se arregló acá, porque sin eso la comprobación nueva no se habría disparado nunca.

**3 · Cuántas hay ya escritas:** era la tercera exigencia del pendiente, y la respuesta duele. Las dos especificaciones de este repositorio traen **31 reglas sin origen** — 16 en `automatismos/spec.md` y 15 en `documentos-modelo/spec.md`. **No se calló la comprobación para que el número diera cero**; quedaron en el [pendiente 47](../47-las-reglas-de-negocio-del-estandar-no-dicen-de-donde-bajan.md).

## Cómo se supo que cerró

El §4 de la plantilla pide la procedencia, una regla sin ella reprueba en un validador con tres casos que se vieron fallar a propósito, y falta el aviso a `shopnest-mesa`.
