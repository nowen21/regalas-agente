# Resultado de Pruebas — Fase B-EP-005-HU-011-el-mapa-del-sitio-tampoco-envejece

**Para qué sirve este documento.** Dice qué se ejecutó, con qué y qué dio. El plan está en [plan_pruebas.md](plan_pruebas.md).

## 0. Veredicto

**Cumple**, ciclo 1. Ocho casos de ocho, y el programa encontró cinco defectos reales en su primera corrida.** Ejecutado el 2026-08-22 contra la versión 31.2.0, en Windows con Python 3.

## 1. Caso por caso

| Caso | Resultado | Veredicto |
|---|---|---|
| CP-01 a CP-07 | `Ran 7 tests ... OK` | ✅ |
| CP-08 · no regresión | `suite` y `estandar` sin incumplimientos | ✅ |

**Y la corrida contra el repositorio real, que es la prueba de que sirve:**

```
$ python validadores/validar.py sitio      (antes de poner al día el mapa)
4 falla(s), 1 aviso(s).
Carpetas de primer nivel: 16 · nombradas en el mapa: 12 · sin nombrar: 4

$ python validadores/validar.py sitio      (después)
OK: sin incumplimientos.
Carpetas de primer nivel: 16 · nombradas en el mapa: 16 · sin nombrar: 0
```

## 2. Lo que costó llegar al verde

**Nada que corregir, pero sí una decisión al escribirlo:** cómo reconocer que una carpeta está nombrada. Buscar el nombre suelto daba falsos aciertos (la palabra «base» sale en cada párrafo), así que se busca `nombre/`, con la barra, que es como el mapa las escribe. `CP-07` protege esa decisión.

## 3. Lo que no se probó

**Que la descripción sea la acertada ni que la zona esté bien elegida.** Que `evals/` sea herramienta y no bitácora es un juicio; el programa comprueba que esté, no dónde.
