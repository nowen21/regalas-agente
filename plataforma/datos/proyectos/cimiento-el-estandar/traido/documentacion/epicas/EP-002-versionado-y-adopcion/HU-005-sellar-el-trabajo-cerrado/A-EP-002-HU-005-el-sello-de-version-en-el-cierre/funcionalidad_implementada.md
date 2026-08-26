# Funcionalidad implementada — Fase A-EP-002-HU-005-el-sello-de-version-en-el-cierre

**Para qué sirve este documento.** Dice qué quedó hecho al cerrar la fase, con su trazabilidad.

> **Cerrada el 2026-08-22, con el estándar en la versión 31.9.0.** Es el sello que dice **bajo qué reglas** cerró este trabajo: una regla escrita después no lo reabre ([`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)).

## 0. Qué quedó, en una frase

**Todo cierre dice bajo qué versión del estándar cerró**, así que una regla nueva ya no puede hacer parecer incumplido un trabajo viejo.

## 1. Trazabilidad ([`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md))

| Ítem | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| El molde del cierre pide el sello | doc | [`plantillas/ciclo-vida-proyectos/11-funcionalidad-implementada.md`](../../../../../plantillas/ciclo-vida-proyectos/11-funcionalidad-implementada.md) | ✅ | campo y caja del porqué |
| El cierre sin sello se detecta | código | [`validadores/fases.py`](../../../../../validadores/fases.py) | ✅ | `cierre_sin_sello`, como aviso |
| Se reconocen las dos formas de escribirlo | código | el mismo | ✅ | la fila del molde y la frase suelta |
| Nada se exige hacia atrás | código | el mismo | ✅ | corte en el 2026-08-22 |
| Los cierres de hoy quedaron sellados | doc | quince fases | ✅ | de la 30.9.1 a la 31.8.0 |

## 2. Lo que cambia para un proyecto que hereda

**Un cierre nuevo lleva una línea más.** La escribe quien cierra, con el número que tenga `VERSION` en ese momento. Los cierres anteriores no se tocan.

## 3. Lo que queda abierto

**El sello no se pone solo.** Podría: el número está en `VERSION` y el momento es el cierre. No se automatizó porque, según [`20·M19`](../../../../../base/20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md), primero tiene que cumplirse a mano y verse cuántas veces se olvida; hoy lleva un día de vida.
