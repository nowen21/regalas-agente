# Pendiente · Nada se ejecuta fuera del plan aprobado

> Unido en el [pendiente 103](103-cada-documento-de-la-cadena-sale-del-anterior.md).

**Estado:** abierto. Espera la aprobación del usuario.

| | |
|---|---|
| **Historia de usuario** | Por asignar: nace al aprobarse este pendiente |
| **De dónde sale** | [H-10 de la sesión del 2026-09-28](../historico-chat/resumenes/2026-09-28/sesion.md), sobre por qué el agente olvida las reglas |
| **Proyecto de origen** | El estándar mismo |

## El problema

En la fase `C` de HU-023 el agente cambió el código seis veces después de aprobado el plan, sin escribir antes la ampliación: tocó archivos que el plan no declaraba y borró `leidas.py`. [`02·F8`](../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`01·C4`](../base/01-conducta.md#c4--no-decidas-por-tu-cuenta) y [`00·N1`](../base/00-nucleo-blindado.md#n1--ningún-cambio-de-estado-sin-aprobación-explícita-blindada) lo prohíben. El freno de `01·C28` impide actuar sin la palabra, pero después de «Hágalo» nada revisa que el agente se quede dentro de lo aprobado.

## Por qué importa

Cumplir el plan depende de que el agente se acuerde, y en esta sesión no se acordó.

## Qué falta

1. **Un freno antes de cada escritura** que compare la ruta con la tabla 2.1 del plan aprobado de la fase activa, y **antes de correr pruebas**, que compare las suites con las del `plan_pruebas`.
2. **La fase activa**, marcada en su `estado-fase.md`. Sin fase activa solo se escriben documentos de trabajo: el resumen, los pendientes y el propio plan.
3. **Un camino para ampliar el plan:** el agente escribe la ampliación y el freno no la deja pasar hasta que el usuario escribe «Apruebo», que el enganche de cada mensaje anota.
4. **Excepciones fijas:** el histórico, el resumen de la sesión, los guiones de `historico-chat/scripts/` y el mismo plan.
5. **Al guardar:** el commit se rechaza si trae archivos que el plan no declara.
6. **Cada detención queda anotada** sola como hallazgo en el resumen de la sesión.

## El límite

- No revisa si lo escrito dentro de un archivo permitido es lo que el plan pedía.
- Depende de los pendientes [103](103-cada-documento-de-la-cadena-sale-del-anterior.md) y [104](104-la-plantilla-del-plan-se-puede-comprobar.md).

## Cómo se sabrá que cerró

- Escribir un archivo que el plan aprobado no declara se detiene y pide ampliar el plan.
- Después de «Apruebo» sobre la ampliación, la misma escritura pasa.
- Un commit con un archivo fuera del plan se rechaza.
- Correr una suite que el `plan_pruebas` no declara se detiene.
