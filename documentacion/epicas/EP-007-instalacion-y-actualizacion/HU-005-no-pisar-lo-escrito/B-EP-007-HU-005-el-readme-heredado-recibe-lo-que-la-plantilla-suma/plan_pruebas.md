# Plan de Pruebas — Fase B-EP-007-HU-005-el-readme-heredado-recibe-lo-que-la-plantilla-suma

**Para qué sirve este documento.** Dice con qué se comprueba que la fase quedó bien antes de cerrarla. Lo ejecutado está en [resultado_pruebas.md](resultado_pruebas.md).

## 0. Qué se prueba, y qué no

**Se prueba** que la sección nueva llega, que lo del proyecto sobrevive, que sin novedad no se toca nada, y que el sello queda al día.

**No se prueba** contra un proyecto real en esta corrida: las pruebas arman un estándar de mentira en carpeta temporal, porque editar la plantilla de verdad para probar sería tocar el estándar ([`00·N4`](../../../../../base/00-nucleo-blindado.md)).

## 1. Alcance de ejecución ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md))

La fase toca `validadores/instalar.py` y `plantillas/`. Se corre la prueba nueva, la suite entera y la comprobación del estándar.

## 2. Trazabilidad criterio a caso

| CA | Caso | Tipo |
|---|---|---|
| CA-01 · instalar no borra lo escrito | CP-02 | automática |
| CA-01 · lo que el estándar suma llega | CP-01, CP-04, CP-06 | automática |
| transversal · sin novedad no se toca nada | CP-03 | automática |
| transversal · el sello queda al día | CP-05 | automática |
| transversal · no regresión | CP-07 | automática |

## 3. Los casos

### CP-01 a CP-06 · Los seis casos del instalador

```
python validadores/tests/test_instalar_agrega_al_readme_heredado.py
```

**Esperado:** los seis pasan. **`CP-02` es el que decide**: se instala, el proyecto escribe su propia sección, la plantilla del estándar gana otra, se reinstala, y lo del proyecto sigue palabra por palabra.

### CP-07 · Nada de lo que ya estaba se rompe

```
python validadores/validar.py suite
python validadores/validar.py estandar
```

**Esperado:** las dos sin incumplimientos. Importa porque `instalar.py` lo tocan seis fases distintas.

## 4. Criterio de cierre

La fase cierra con todos los casos en verde. Un caso rojo se corrige antes de publicar, no se anota como pendiente.
