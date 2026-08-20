# Pendiente · El consumo de la sesión se ve cuando ya se gastó

**Estado:** abierto · anotado 2026-08-20.

| | |
|---|---|
| **Historia de usuario** | [EP-005 · HU-014 — El consumo de la sesión se ve mientras se puede actuar](../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-014-el-consumo-se-ve-a-tiempo/HU-014-el-consumo-se-ve-a-tiempo.md) — el aviso de consumo es un automatismo de sesión, y hasta hoy ninguna historia lo tenía |
| **De dónde sale** | El H-1 del resumen [../historico-chat/resumenes/2026-08-20/core-del-agente-en-la-herramienta.md](../../historico-chat/resumenes/2026-08-20/core-del-agente-en-la-herramienta.md): la comparación contra `notas/estructura.md` §3.2 (`Budget`) |
| **Proyecto de origen** | El estándar mismo |

## El problema

[adaptadores/claude-code/hook_presupuesto.py](../../adaptadores/claude-code/hook_presupuesto.py) nació en la 27.0.0 para que "esta sesión salió cara" dejara de ser una impresión. Corre en el evento de cierre de cada respuesta y suma lo consumido. La suma es correcta; el momento no: el total aparece cuando la respuesta ya terminó, y el usuario lo ve cuando ya pagó.

Y nació sin historia de usuario: se construyó por orden directa, sin cadena, y quedó escrito así en el resumen del 2026-08-19. Este pendiente también le da dueño.

## Por qué importa

Medido el 2026-08-20 sobre las ocho sesiones más recientes de este repositorio: entre 144 mil y 12,7 millones de fichas sin caché por sesión. Una sesión de doce millones no avisa nada hasta que termina. La factura sorpresa que la 27.0.0 quiso evitar sigue siendo sorpresa, solo que ahora con el número.

## Qué falta

Que el mismo enganche corra también en cada mensaje del usuario y avise **una vez por cada tramo** de consumo que la sesión cruce. El tramo por defecto sale de la medición: un millón de fichas. Sin estado compartido: se compara el total con y sin el último turno, y se avisa solo cuando el tramo cambió.

## El límite

No detiene la sesión ni decide cuánto es mucho. El corte lo pone la herramienta, y un enganche que bloquea al usuario es peor que el gasto (la 26.0.1 lo comprobó).

## Cómo se sabrá que cerró

Una transcripción de prueba cuyo último turno cruza el millón produce el aviso; la misma transcripción con un turno más, dentro del mismo tramo, no lo produce. Las dos con caso automatizado.
