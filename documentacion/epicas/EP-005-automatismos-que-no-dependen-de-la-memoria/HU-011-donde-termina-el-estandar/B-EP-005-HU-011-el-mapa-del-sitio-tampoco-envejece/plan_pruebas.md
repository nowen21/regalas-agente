# Plan de Pruebas — Fase B-EP-005-HU-011-el-mapa-del-sitio-tampoco-envejece

**Para qué sirve este documento.** Dice con qué se comprueba que la fase quedó bien antes de cerrarla. Lo ejecutado está en [resultado_pruebas.md](resultado_pruebas.md).

## 0. Qué se prueba, y qué no

**Se prueba** que reporta la carpeta que falta, que avisa de la que sobra, que se calla cuando el mapa está bien, y que no confunde lo local con lo del estándar.

**No se prueba** que la descripción del mapa sea buena: eso lo lee una persona.

## 1. Alcance de ejecución ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md))

La fase toca `validadores/` y `anatomia/`. Se corre la prueba nueva, la suite completa y la comprobación del estándar; no se corren las de la interfaz.

## 2. Trazabilidad criterio a caso

| CA | Caso | Tipo |
|---|---|---|
| CA-03 · lo escrito sobre la anatomía no envejece | CP-01, CP-02, CP-03 | automática |
| CA-03 · la comprobación sirve, o sea que se calla | CP-04, CP-05, CP-07 | automática |
| transversal · se puede mirar sin abrir el mapa | CP-06 | automática |
| transversal · no regresión | CP-08 | automática |

## 3. Los casos

### CP-01 a CP-07 · Los siete casos del programa

```
python validadores/tests/test_el_mapa_del_sitio_no_envejece.py
```

**Esperado:** los siete pasan. `CP-01` la carpeta que falta es falla; `CP-02` sin mapa es falla; `CP-03` la carpeta que ya no existe es aviso, no falla; **`CP-04` nombrada la carpeta, se calla**; `CP-05` lo local y lo generado no cuentan; `CP-06` el recuento se lee sin abrir el mapa; `CP-07` un nombre parecido no cuenta por la carpeta real.

### CP-08 · Nada de lo que ya estaba se rompe

```
python validadores/validar.py suite
python validadores/validar.py estandar
```

**Esperado:** las dos sin incumplimientos.

## 4. Criterio de cierre

La fase cierra con todos los casos en verde. Un caso rojo se corrige antes de publicar, no se anota como pendiente.
