# Resultado de Pruebas — Fase F-EP-001-HU-009-nadie-se-pasa-del-molde

**Para qué sirve este documento.** Dice **qué se ejecutó, con qué y qué dio**, para que el veredicto de la fase se pueda revisar sin repetir el trabajo. El plan está en [plan_pruebas.md](plan_pruebas.md).

## 0. Veredicto

**Cumple**, ciclo 1. Los siete casos en verde. Ejecutado el 2026-08-22 sobre la versión 30.9.1 del estándar, en Windows con Python 3.

## 1. Caso por caso

| Caso | Qué se corrió | Resultado | Veredicto |
|---|---|---|---|
| P-01 | `validar.py metareglas` | `OK: sin incumplimientos` (abría con 27 fallas) | ✅ |
| P-02 | el mismo | ningún aviso de largo (abría con 34) | ✅ |
| P-03 | el mismo | ningún sello vencido | ✅ |
| P-04 | `validar.py estandar` | `OK: sin incumplimientos` | ✅ |
| P-05 | `validar.py marcas --preparados` | sin fallas en lo preparado | ✅ |
| P-06 | `validar.py versionado` | `0 falla(s)` | ✅ |
| P-07 | revisión regla por regla | ninguna exigencia cambió | ✅ |

## 2. Lo que costó llegar al verde

**P-01 arrancó reprobando por donde no se esperaba.** Al declarar que `C1`, `S4` y `T4` extienden a `N1`, `N6` y `N4`, el validador reprobó las tres: [`20·M7`](../../../../../base/20-meta-reglas/reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md) prohíbe declarar que se extiende una regla blindada. Se cambió a «depende de», que es la forma correcta para apoyarse en el núcleo sin pretender ampliarlo.

**P-04 reprobó tres veces, y las tres por lo mismo:** mover texto rompe lo que lo citaba. Las trece citas a `F12.1`, `F12.6`, `F12.11` y `F12.13` apuntaban a sub-identificadores que dejaron de existir; pasaron a citar la regla y el punto del anexo. Los enlaces relativos del anexo cambiaron de profundidad al bajar un nivel. Y los nombres de archivo de `M10` y `M17` no eran los que este plan suponía, que es exactamente lo que [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md) manda verificar.

**P-05 detuvo la publicación dos veces, y tenía razón las dos.** El anexo de nomenclatura llegó con doce rayas y el de la tabla de trazabilidad con diez puntos medios: son la puntuación del texto que se movió, y el trinquete la cuenta como nueva porque el archivo es nuevo. La primera vez se le preguntó al usuario, que autorizó cambiar solo la puntuación del texto literal suyo; la segunda se resolvió igual, con comas.

## 3. Evidencia

**La corrida final, entera:**

```
$ python validadores/validar.py metareglas
== El estándar contra sus meta-reglas · . ==
OK: sin incumplimientos.

$ python validadores/validar.py estandar
== Coherencia del estándar ==
OK: sin incumplimientos.

$ python validadores/validar.py versionado
0 falla(s), 1 aviso(s).
```

El aviso que queda en `versionado` es viejo y está reconocido en el propio registro: la 15.4.0 tiene dos entradas porque dos sesiones numeraron a la vez, y no se renumera.

**La batería del `pre-push` corrió en cada una de las seis publicaciones** y las seis pasaron: es la que corre el enganche, no una corrida a mano.

## 4. Qué no se probó

**Que la redacción nueva se lea mejor.** No hay forma de medirlo y no se finge que la haya: lo juzga quien lee las reglas, y el material para juzgarlo está en [notas/porques-recortados-al-molde.md](../../../../../notas/porques-recortados-al-molde.md), que dice de cada regla qué salió.
