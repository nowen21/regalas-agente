# Funcionalidad implementada — Fase B-EP-004-HU-016-todo-pendiente-abierto-nombra-su-historia

**Para qué sirve este documento.** Dice qué quedó hecho al cerrar la fase, con su trazabilidad.

> **Cerrada el 2026-08-22, con el estándar en la versión 31.8.0.** Es el sello que dice **bajo qué reglas** cerró este trabajo: una regla escrita después no lo reabre ([`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)).

## 0. Qué quedó, en una frase

**Un pendiente abierto que no nombra su historia rompe la corrida**, así que el enrutamiento deja de depender de que alguien se acuerde.

## 1. Trazabilidad ([`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md))

| Ítem | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| El abierto sin la fila detiene | código | [`validadores/pendientes.py`](../../../../../validadores/pendientes.py) | ✅ | `abierto_nombra_su_historia`, con FALLA |
| La fila vacía también | código | el mismo | ✅ | o nombra la historia, o dice por qué no la tiene |
| Lo que no es un pendiente numerado no cuenta | código | el mismo | ✅ | el índice de la carpeta queda fuera |
| Los casos | prueba | [`test_pendientes_historia.py`](../../../../../validadores/tests/test_pendientes_historia.py) | ✅ | ocho, los dos sentidos juntos |

## 2. Lo que cambia para un proyecto que hereda

**Un pendiente nuevo tiene que decir a qué historia baja.** Si todavía no lo sabe, la fila lo dice con esas palabras: eso pasa, y es lo que distingue una idea de un pendiente listo para ejecutar.

## 3. Lo que queda abierto

**Nada de esta fase.** Lo que sigue abierto es del otro sentido: los 24 cerrados que no declaran su fase, medidos en la fase `A`.
