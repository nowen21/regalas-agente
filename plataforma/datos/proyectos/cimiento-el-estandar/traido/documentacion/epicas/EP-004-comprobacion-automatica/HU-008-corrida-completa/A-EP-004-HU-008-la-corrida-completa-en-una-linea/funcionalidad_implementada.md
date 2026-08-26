# Funcionalidad implementada — Fase A-EP-004-HU-008-la-corrida-completa-en-una-linea

**Para qué sirve este documento.** Dice qué quedó hecho al cerrar la fase, con la trazabilidad hasta donde vive cada cosa.

> **Cerrada el 2026-08-22, con el estándar en la versión 31.7.0.** Es el sello que dice **bajo qué reglas** cerró este trabajo: una regla escrita después no lo reabre ([`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)).

## 0. Qué quedó, en una frase

**`validar.py todo` corre las 31 comprobaciones que aplican y termina en una línea que dice cuántas fallaron.**

## 1. Trazabilidad ([`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md))

| Ítem de la especificación | Categoría | Ubicación esperada | Estado | Evidencia |
|---|---|---|---|---|
| Una sola orden corre lo que aplica | código | [`validadores/validar.py`](../../../../../validadores/validar.py) | ✅ | subcomando `todo` |
| Cada comprobación sigue corriendo sola | código | el mismo | ✅ | la corrida las **llama**: no hay una segunda versión de nada |
| Un subcomando nuevo entra solo | código | el mismo | ✅ | la lista sale del propio analizador; solo se nombra lo que queda **fuera** |
| Lo que queda fuera dice por qué | código | `FUERA_DE_LA_CORRIDA` | ✅ | siete motivos escritos, más tres que dependen de dónde se corre |
| El resumen final es único | código | el mismo | ✅ | `CP-005` |
| El código de salida sirve en integración continua | código | el mismo | ✅ | 1 si alguna falló |
| Que una comprobación reviente no se lleva las demás | código | el mismo | ✅ | se anota y la corrida sigue, como en `EP-004·HU-003` |
| Los casos que lo protegen | prueba | [`test_la_corrida_completa_en_una_linea.py`](../../../../../validadores/tests/test_la_corrida_completa_en_una_linea.py) | ✅ | siete |

## 2. Lo que cambia para un proyecto que hereda

**Gana una orden y no pierde ninguna.** `python validar.py todo` desde la carpeta del proyecto corre todo lo que aplica; los subcomandos sueltos siguen exactamente igual para quien quiera mirar una cosa.

**Lo lento sigue aparte, a propósito:** `linter`, `suite` y `audit` corren las herramientas del proyecto y salen a la red. Una corrida que tarda es una corrida que no se corre.

## 3. Lo que queda abierto

**Las tres exclusiones que dependen de dónde se corre** (`checklist`, `versiones`, `version`) se deciden mirando si la carpeta tiene `base/` y `VERSION`, o sea si **es** el estándar. Es un criterio simple y puede quedarse corto el día que un proyecto tenga su propia `base/` local; cuando pase, se verá en la corrida y se afina.

**Y lo que la primera corrida dejó claro:** este subcomando es el que encuentra lo que nadie corre a mano. Sus tres primeras fallas fueron mapas desactualizados por módulos creados el mismo día.
