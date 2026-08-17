# Pendiente · `enlaces.py` termina en silencio sin comprobar nada

**Estado:** abierto · anotado 2026-08-16.

| | |
|---|---|
| **De dónde sale** | El hallazgo H-4 del [resumen de la sesión 7](../historico-chat/resumenes/2026-08-16/sesion-7.md) |
| **Proyecto de origen** | El estándar mismo |

## El problema

```
python validadores/enlaces.py --raiz .
→ (nada)
código de salida: 0
```

No tiene bloque de arranque. **No comprobó nada**, y lo dice con el mismo silencio con el que un validador dice «está todo bien».

## Por qué es `P1`

Un validador que calla sin haber mirado es peor que ninguno: el que no existe se nota, este **afirma**. La fase `B-EP-005-HU-008` se lo creyó el 2026-08-16 y escribió «cero enlaces rotos» en su resultado de pruebas; el entrypoint real —`validar.py estandar`— reportaba veinte. La métrica se corrigió el mismo día, pero pudo haber cerrado así.

## Qué falta

1. Que `enlaces.py` **tenga punto de entrada**, o que se muera diciendo por dónde se corre.
2. **Revisar los demás.** Son unos treinta programas en `validadores/`; no se sabe cuántos tienen el mismo hueco, y esa es media gracia de este pendiente.

## Con qué se cruza

- El [55](55-el-validador-lee-enlaces-dentro-de-las-comillas-de-codigo.md) y el punto 1 del [33](33-defectos-que-destaparon-los-resumenes-viejos.md), que son del mismo archivo: los tres hacen que sus hallazgos no se puedan creer, unos por callar y otros por hablar de más.

## Cómo se sabrá que cerró

Correr cualquier validador suelto o dice lo que encontró, o dice cómo se corre. Ninguno termina en silencio con código 0 sin haber mirado.
