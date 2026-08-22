# `plan_vs_hecho.py` — lo hecho contra el plan aprobado

**Qué hace.** Compara dos cosas que hasta ahora solo se comprobaban leyendo:

1. Los archivos que la fase **tocó** contra los que su plan **declaró** en la §2.1.
2. Los criterios que el plan dice cubrir contra los casos que el plan de pruebas escribió.

## Contra qué se compara lo tocado

**Contra el commit del que salió la fase**, que se pasa con `--desde`. Es la decisión 22 del [pendiente 59](../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md): la rama arrastra trabajo ajeno y lo que está sin guardar cambia mientras se mira; el commit de origen es el único punto fijo.

Sin `--desde` no se inventa nada: se dice que falta el dato.

## Qué avisa

| Situación | Qué dice |
|---|---|
| Un archivo tocado que el plan no declara | «o el plan se amplió sin escribirlo, o se editó de más» |
| El plan no tiene §2.1, o no está escrita como el molde | que no hay contra qué comparar |
| Un criterio que el plan dice cubrir y ningún caso nombra | que nadie lo comprueba |
| Un plan de pruebas sin ningún caso | lo mismo, dicho de una vez |

**Y qué no cuenta como archivo de más:** los cinco documentos de la propia fase y su `README`. Escribir el resultado de las pruebas **es** ejecutar la fase; pedir que el plan se declare a sí mismo daría un aviso en todas, y ninguno se leería.

## Por qué avisa y nunca detiene

Un archivo de más puede ser un **descubrimiento legítimo** que se reportó y se aprobó, y eso no se ve desde el disco: [`02·F8`](../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md) admite ampliar el plan, lo que prohíbe es hacerlo en silencio. El programa dice que **la lista no cuadra**; si la explicación cuadra, lo lee una persona.

## Lo que no compara, y se declara

**Si los pasos que el resultado dice haber ejecutado son los que el plan de pruebas escribió.** Eso exige leer los dos textos y decidir si dicen lo mismo con otras palabras. Es criterio humano (decisión 10 del pendiente 59) y así está registrado en [`reglas-validables.md`](../reglas-validables.md).

## Cómo se corre

```
python validadores/validar.py plan                       # los criterios de todas las fases
python validadores/validar.py plan --fase <carpeta> --desde <commit>
```

Queda **fuera de la corrida completa** porque su mitad más útil necesita el commit de origen, que solo sabe quien abrió la fase.

## Casos que lo protegen

[`validadores/tests/test_el_plan_contra_lo_hecho.py`](../tests/test_el_plan_contra_lo_hecho.py), once. El que decide es `CP-004`: los documentos de la propia fase no cuentan como archivo de más.
