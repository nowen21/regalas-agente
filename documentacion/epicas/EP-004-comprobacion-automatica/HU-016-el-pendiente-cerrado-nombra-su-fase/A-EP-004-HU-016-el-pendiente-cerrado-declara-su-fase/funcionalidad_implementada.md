# Funcionalidad implementada — Fase A-EP-004-HU-016-el-pendiente-cerrado-declara-su-fase

**Para qué sirve este documento.** Dice qué quedó hecho al cerrar la fase, con su trazabilidad.

> **Cerrada el 2026-08-22, con el estándar en la versión 31.8.0.** Es el sello que dice **bajo qué reglas** cerró este trabajo: una regla escrita después no lo reabre ([`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)).

## 0. Qué quedó, en una frase

**Un pendiente cerrado que no dice en qué fase se hizo ya no pasa inadvertido:** la corrida lo nombra.

## 1. Trazabilidad ([`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md))

| Ítem | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| El cerrado sin fase se reporta | código | [`validadores/pendientes.py`](../../../../../validadores/pendientes.py) | ✅ | `cerrado_declara_su_fase`, como aviso |
| La fase nombrada tiene que existir | código | el mismo | ✅ | se busca su carpeta en `documentacion/epicas/` |
| Lo cerrado por decisión queda fuera | código | el mismo | ✅ | no hubo desarrollo |
| Lo anterior al 2026-08-16 queda fuera | código | el mismo | ✅ | la norma no se aplica hacia atrás |
| Los casos | prueba | [`test_pendientes_historia.py`](../../../../../validadores/tests/test_pendientes_historia.py) | ✅ | ocho, con los dos sentidos |

## 2. Lo que cambia para un proyecto que hereda

**Gana la comprobación en su propia carpeta de pendientes**, con el mismo corte: solo se le exige a lo que cierre de ahora en adelante.

## 3. Lo que queda abierto

**24 pendientes cerrados desde el corte siguen sin declarar su fase.** Está medido y a la vista en cada corrida; se llena cuando cada uno se toque, porque reconstruir la fase de veinticuatro de memoria es el camino directo a escribir una que no fue.
