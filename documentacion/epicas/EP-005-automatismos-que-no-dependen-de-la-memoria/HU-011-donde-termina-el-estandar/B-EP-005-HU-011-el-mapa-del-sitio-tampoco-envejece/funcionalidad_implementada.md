# Funcionalidad implementada — Fase B-EP-005-HU-011-el-mapa-del-sitio-tampoco-envejece

**Para qué sirve este documento.** Dice qué quedó hecho al cerrar la fase, con la trazabilidad de cada ítem hasta el archivo donde vive.

> **Cerrada el 2026-08-22, con el estándar en la versión 31.2.0.** Es el sello que dice **bajo qué reglas** cerró este trabajo: una regla escrita después no lo reabre ([`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)).

## 0. Qué quedó, en una frase

**El mapa del sitio ya no puede envejecer en silencio:** `validar.py sitio` reporta la carpeta que existe y no está, y avisa de la que está y ya no existe.

## 1. Trazabilidad ([`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md))

| Ítem de la especificación | Categoría | Ubicación esperada | Estado | Evidencia |
|---|---|---|---|---|
| La carpeta que existe y el mapa no nombra se reporta | prueba | `validadores/sitio.py` | ✅ | `CP-01`, y cuatro casos reales encontrados |
| La carpeta que el mapa nombra y ya no existe se avisa | prueba | el mismo | ✅ | `CP-03`, y `diplomado-ia/` encontrada |
| La comprobación se calla cuando está bien | prueba | el mismo | ✅ | `CP-04` |
| Se puede correr en una línea | doc | `validar.py sitio` | ✅ | subcomando con su ayuda |
| El mapa quedó al día | doc | `anatomia/mapa-del-sitio.md` | ✅ | 16 de 16 carpetas nombradas |
| El cambio queda versionado | doc | `CHANGELOG.md`, `VERSION` | ✅ | v31.2.0 |

## 2. Lo que cambia para un proyecto que hereda

**Nada.** El mapa del sitio es de este repositorio, no de los proyectos que heredan: `anatomia/` no viaja. Lo que un proyecto sí gana es el precedente, por si quiere comprobar sus propios mapas.

## 3. Lo que queda abierto

**El segundo nivel sigue sin comprobarse.** Una carpeta nueva dentro de `plantillas/` o de `documentacion/` no la ve nadie. Se dejó fuera a propósito, porque el ruido de reportar cada subcarpeta apagaría la comprobación; si con el uso aparece que ahí también se pierde algo, es una fase más de esta historia.
