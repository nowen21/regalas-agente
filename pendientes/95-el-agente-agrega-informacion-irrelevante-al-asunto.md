# Pendiente · El agente agrega información irrelevante al asunto que está tratando

**Estado:** **hecho** el 2026-09-27, en la misma sesión que lo anotó. Lo construyó la fase `A` de HU-038: la regla [`00·ID11`](../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md), versión 38.1.0.

| | |
|---|---|
| **Historia de usuario** | [EP-001 · HU-038 — El agente agrega información irrelevante al asunto que está tratando](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-038-el-agente-agrega-informacion-irrelevante-al-asunto/HU-038-el-agente-agrega-informacion-irrelevante-al-asunto.md) |
| **De dónde sale** | La sesión del 2026-09-27: el usuario preguntó qué aportaba al [pendiente 96](96-el-agente-no-conserva-el-espanol-colombiano.md) la frase «No entra en HU-037, que está terminada y dejó la norma fuera de su alcance». No aportaba nada, y ninguna regla lo prohibía |
| **Proyecto de origen** | El estándar mismo |

## El problema

Ninguna regla de `base/` establece que el contenido generado por el agente deba limitarse estrictamente al asunto que se está tratando.

- **00·ID9** exige expresar lo mismo en menos palabras, pero no establece que la información deba ser relevante para el tema.
- **01·C5** exige respuestas cortas, tampoco pide pertinencia, y solo rige el chat.

Por lo tanto, el agente puede cumplir ambas reglas y, aun así, agregar información breve, clara y completamente irrelevante para el asunto que está trabajando.

El problema no es la **extensión** de la información, sino su **pertinencia respecto al tema, objetivo y alcance del elemento que se está tratando**.

## Por qué importa

Cada dato que no viene al caso obliga al lector a decidir si le sirve, y un documento del repositorio lo arrastra en cada lectura.

## Qué falta

Una regla del capítulo 00 que exija que todo lo que el agente entrega trate del asunto en curso: nada de información, explicación ni comentario que no sirva a ese asunto. Rige los documentos y el chat. Borrador acordado con el usuario el 2026-09-27:

```markdown
## ID11 · Escribe solo sobre el asunto en curso

Lo que el agente entrega trata solo del asunto en curso: cada dato,
explicación o comentario sirve a ese asunto, y lo que no sirve se quita
aunque sea cierto y corto. Se relee contra esta regla junto con la lista de
marcas y el recorte de extensión (extiende `00·ID7`, `00·ID8` y `00·ID9`).

INCORRECTO: el pendiente de la norma colombiana dice "No entra en HU-037,
            que está terminada y dejó la norma fuera de su alcance"
CORRECTO:   la fila dice "Por asignar: nace al aprobarse este pendiente"
```

## El límite

No trata la extensión, que sigue en `ID9` y `C5`.

## Cómo se sabrá que cerró

- La regla existe en `base/00-identidad-y-rol/reglas/` con su checklist en **CUMPLE**.
- `python validadores/validar.py metareglas` sigue en verde, con la regla clasificada en `validadores/reglas-validables.md`.
