# Funcionalidad implementada — Fase B-EP-003-HU-002-la-historia-declara-que-criterio-depende-de-cual

**Para qué sirve este documento.** Dice qué quedó hecho al cerrar la fase, con la trazabilidad de cada ítem hasta el archivo donde vive.

> **Cerrada el 2026-08-22, con el estándar en la versión 31.1.0.** Es el sello que dice **bajo qué reglas** cerró este trabajo: una regla escrita después no lo reabre ([`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)).

## 0. Qué quedó, en una frase

**Una historia puede decir qué criterio depende de cuál**, en la misma tabla donde ya dice qué fase cubre cada uno.

## 1. Trazabilidad ([`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md))

| Ítem de la especificación | Categoría | Ubicación esperada | Estado | Evidencia |
|---|---|---|---|---|
| La tabla de fases admite declarar dependencia entre criterios | doc | `plantillas/ciclo-vida-proyectos/04-HU.md` | ✅ | columna «Depende de» y su fila de ejemplo |
| Queda escrito cómo se llena | doc | el mismo archivo | ✅ | la frase que sigue a la tabla: criterios, no fases; vacía si no hay |
| El cambio queda versionado | doc | `CHANGELOG.md`, `VERSION` | ✅ | v31.1.0 |

## 2. Lo que cambia para un proyecto que hereda

**Nada que hacer.** La columna es aditiva y vacía es correcta. Una historia nueva la trae; una vieja la gana cuando alguien la toque.

## 3. Lo que queda abierto

**Sin validador, a propósito.** Si con el uso aparece que la columna se llena mal (con fases en vez de criterios), eso sí se puede contar y entonces valdría automatizarlo, según [`20·M19`](../../../../../base/20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md).
