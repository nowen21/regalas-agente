# Funcionalidad implementada — Fase A-EP-004-HU-011-la-comprobacion-del-molde-se-puede-correr

**Para qué sirve este documento.** Dice qué quedó hecho al cerrar la fase, con la trazabilidad hasta donde vive cada cosa.

> **Cerrada el 2026-08-22, con el estándar en la versión 31.7.0.** Es el sello que dice **bajo qué reglas** cerró este trabajo: una regla escrita después no lo reabre ([`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)).

## 0. Qué quedó, en una frase

**El molde de las reglas se comprueba corriendo una orden, y desde hoy también avisa si dos reglas comparten identificador.**

## 1. Trazabilidad ([`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md))

| Ítem de la especificación | Categoría | Ubicación esperada | Estado | Evidencia |
|---|---|---|---|---|
| Se puede correr, y no calla | código | `validar.py metareglas` | ✅ | imprime siempre; corrido a mano, muere diciendo por dónde va |
| Dos modos en un subcomando | código | `metareglas` y `metareglas --catalogo` | ✅ | el estándar en seco y el catálogo del proyecto |
| El identificador repetido se reporta | código | [`validadores/metareglas.py`](../../../../../validadores/metareglas.py) | ✅ | `_identificador_repetido`, en las dos reglas y con las dos rutas |
| El de prefijo ajeno se reporta | código | el mismo | ✅ | ya existía: el prefijo es exclusivo del capítulo |
| Los casos que lo protegen | prueba | [`test_el_identificador_no_se_repite.py`](../../../../../validadores/tests/test_el_identificador_no_se_repite.py) | ✅ | cinco, uno de ellos sobre el cuerpo real |

## 2. Lo que cambia para un proyecto que hereda

**Nada obligatorio.** El proyecto que tenga catálogo propio ya podía correr `metareglas --catalogo`; lo que gana es que, si algún día escribe reglas propias con identificadores repetidos, se le diga.

## 3. Lo que queda abierto

**Lo que sigue sin comprobarse del molde** es lo que exige leer: si la exigencia es una sola, si el ejemplo INCORRECTO es el error que se comete de verdad, si la dependencia declarada es la acertada. Está clasificado así en [`reglas-validables.md`](../../../../../validadores/reglas-validables.md) y no es deuda: es el límite entre lo que un programa puede juzgar y lo que no.
