# Plan de Pruebas — Fase C-EP-005-HU-001-el-historico-se-busca-por-tema

**Para qué sirve este documento.** Dice con qué se comprueba que la fase quedó bien antes de cerrarla. Lo ejecutado está en [resultado_pruebas.md](resultado_pruebas.md).

## 0. Qué se prueba, y qué no

**Se prueba** que recoge todos los hallazgos, que cada uno enlaza a su resumen, que un resumen sin hallazgos no ensucia el índice, que generar dos veces da lo mismo y que avisa sin detener.

**No se prueba** que los temas estén bien redactados: son los títulos que cada sesión escribió, y se copian tal cual.

## 1. Alcance de ejecución ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md))

La fase toca `validadores/` y `historico-chat/resumenes/`. Se corren la prueba nueva, la suite entera y la comprobación del estándar.

## 2. Trazabilidad criterio a caso

| CA | Caso | Tipo |
|---|---|---|
| CA · lo que la sesión dejó se encuentra | CP-01, CP-02 | automática |
| CA · el índice no miente sobre lo que hay | CP-03, CP-04, CP-06 | automática |
| transversal · generación estable | CP-05 | automática |
| transversal · sin resúmenes no revienta | CP-07 | automática |
| transversal · no regresión | CP-08 | automática |

## 3. Los casos

### CP-01 a CP-07 · Los siete casos del programa

```
python validadores/tests/test_el_historico_se_busca_por_tema.py
```

**Esperado:** los siete pasan. **`CP-05` es el que decide:** generado dos veces sobre lo mismo, el archivo sale idéntico.

### CP-08 · Nada de lo que ya estaba se rompe

```
python validadores/validar.py suite
python validadores/validar.py estandar
```

**Esperado:** las dos sin incumplimientos.

## 4. Criterio de cierre

La fase cierra con todos los casos en verde. Un caso rojo se corrige antes de publicar, no se anota como pendiente.
