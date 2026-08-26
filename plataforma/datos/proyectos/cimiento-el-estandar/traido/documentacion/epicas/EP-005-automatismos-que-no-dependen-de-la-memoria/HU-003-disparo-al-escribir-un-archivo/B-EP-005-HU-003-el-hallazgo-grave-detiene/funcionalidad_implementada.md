# Funcionalidad implementada — Fase B-EP-005-HU-003-el-hallazgo-grave-detiene

**Para qué sirve este documento.** Dice qué quedó hecho al cerrar la fase, con la trazabilidad hasta donde vive cada cosa.

> **Cerrada el 2026-08-22, con el estándar en la versión 31.6.0.** Es el sello que dice **bajo qué reglas** cerró este trabajo: una regla escrita después no lo reabre ([`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)).

## 0. Qué quedó, en una frase

**Un documento que queda con un enlace roto no se puede dejar así: el enganche lo devuelve para que se corrija, y el archivo no se toca.**

## 1. Trazabilidad ([`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md))

| Ítem de la especificación | Categoría | Ubicación esperada | Estado | Evidencia |
|---|---|---|---|---|
| La falla detiene | código | [`adaptadores/claude-code/hook_md.py`](../../../../../adaptadores/claude-code/hook_md.py) | ✅ | código 2, comprobado por el camino real |
| El aviso no detiene | código | el mismo | ✅ | código 0 sobre un archivo sano |
| El archivo queda entero | código | el mismo | ✅ | el enganche no escribe ni revierte |
| Lo que no es del proyecto no dispara nada | código | el mismo | ✅ | los dos transversales anteriores siguen pasando |

## 2. Lo que cambia para un proyecto que hereda

**Nada que instalar aparte:** el enganche ya viajaba. Lo que esta fase deja es la comprobación de que **hace lo que dice**, hecha por el camino real y no llamando a la función.

## 3. Lo que queda abierto

**El alcance de lo que mira.** Hoy son enlaces e índices. Ampliarlo a otras comprobaciones del documento es posible y no se hizo: cada cosa que se agregue sube el ruido, y un enganche ruidoso se apaga. Cuando haya evidencia de que algo más se está escapando, se suma con su medición, como pide [`20·M19`](../../../../../base/20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md).

**El precedente que deja:** esta fase contesta, con un caso corrido, la pregunta que el pendiente 59 hacía en cuatro sitios distintos —¿detiene o avisa?—. Detiene lo que se comprueba sin criterio.
