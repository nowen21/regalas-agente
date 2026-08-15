# Pendiente · La carpeta de plantillas mezcla modelos con procedimientos

**Estado:** abierto · anotado 2026-08-14 · nace de la fase [`A-EP-003-HU-001-marca-de-espacio-por-llenar`](../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-001-marca-de-espacio-por-llenar/A-EP-003-HU-001-marca-de-espacio-por-llenar/README.md).

## El problema

`plantillas/` dice, por su nombre, que todo lo de adentro es un modelo que alguien llena. Cuatro de sus treinta archivos no lo son:

| Archivo | Qué es en realidad |
|---|---|
| [`plantillas/retrodocumentacion.md`](../plantillas/retrodocumentacion.md) | Un procedimiento de seis pasos. Se lee y se sigue |
| [`plantillas/historico-chat.md`](../plantillas/historico-chat.md) | La explicación de cómo se escribe el histórico |
| [`plantillas/memoria.md`](../plantillas/memoria.md) | La explicación de dónde vive la memoria del agente |
| [`plantillas/prompts/prompt-base-usuario.md`](../plantillas/prompts/prompt-base-usuario.md) | El molde con que el usuario le pide trabajo al agente. Se llena escribiendo, no reemplazando huecos |

Se vio al aplicar [`13·DOC19`](../base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md): esos cuatro quedaron sin una sola marca, y hubo que declararlos como excepción en una lista para que la prueba de cobertura se pudiera juzgar.

**Esa lista es el síntoma.** Mientras los cuatro estén ahí, cada comprobación de marcas tiene que consultar una excepción escrita a mano, y un archivo nuevo sin marca se puede colar como "seguro es otro de esos".

## Qué falta

Decidir a dónde van. Dos opciones sobre la mesa:

**1. Una subcarpeta `plantillas/procedimientos/`.** Siguen instalándose igual en cada proyecto, pero el nombre ya dice que no se llenan. Es el cambio más chico y no toca qué recibe un proyecto.

**2. Sacarlos a `base/` como anexos de su capítulo**, como ya está [`render-local-de-md.md`](../base/13-documentacion/render-local-de-md.md). Más limpio, porque `plantillas/` queda solo con modelos, pero cambia qué copia el instalador y eso hay que pensarlo aparte.

Con cualquiera de las dos, la lista de excepciones desaparece: un archivo de `plantillas/` sin marca pasa a ser un defecto, siempre.

## El límite

Toca rutas que copia [`validadores/instalar.py`](../validadores/instalar.py). Un proyecto ya instalado tiene esos archivos en el sitio viejo, así que el cambio necesita su fase, con la migración escrita.
