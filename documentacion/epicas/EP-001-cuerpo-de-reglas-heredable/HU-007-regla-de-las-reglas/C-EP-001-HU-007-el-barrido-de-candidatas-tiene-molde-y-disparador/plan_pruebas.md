# Plan de Pruebas — Fase C-EP-001-HU-007-el-barrido-de-candidatas-tiene-molde-y-disparador

**Para qué sirve este documento.** Dice con qué se comprueba que la fase quedó bien antes de cerrarla. Lo ejecutado y su resultado están en [resultado_pruebas.md](resultado_pruebas.md).

## 0. Qué se prueba

Que el molde **sirve para el barrido que ya se hizo a mano**, que la regla nueva cumple su propio checklist, y que no rompe nada de lo que ya estaba.

## 1. Alcance de ejecución ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md))

La fase toca `base/20-meta-reglas/`, `plantillas/` y `validadores/reglas-validables.md`. Se corren las suites del estándar y la batería del `pre-push`; no se corre la de la interfaz.

## 2. Trazabilidad criterio a caso

| CA | Caso | Tipo |
|---|---|---|
| CA-06 · el molde produce las cuatro salidas | CP-01 | manual documentada |
| CA-06 · el disparo existe en el flujo | CP-02 | manual documentada |
| CA-06 · la regla cumple el molde de una regla | CP-03 | automática |
| transversal · no regresión | CP-04, CP-05 | automática |

## 3. Los casos

### CP-01 · El molde habría producido el barrido que ya existe

**Cómo se ejecuta:** tomar las 27 fichas del [barrido del 2026-08-13](../../../../../prompts/analisis/reglas-2026-08-13-candidatas-a-regla.md) y comprobar que cada salida que aquel escribió cabe en una de las cuatro del molde.

**Esperado:** las cuatro salidas del molde (cubierta, regla nueva, afinar una, no es regla) cubren las 27 sin dejar ninguna fuera y sin necesitar una quinta.

### CP-02 · El disparo no depende de que alguien se acuerde

**Cómo se ejecuta:** leer el cuerpo de `M20` y comprobar que nombra un momento que el flujo ya obliga a atravesar.

**Esperado:** dice «antes de publicar una versión», y [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md) ya obliga a parar ahí. Un disparo que dijera «cuando convenga» reprueba este caso.

### CP-03 · La regla nueva cumple el checklist

```
python validadores/validar.py metareglas
```

**Esperado:** sin fallas y sin avisos sobre `M20`: cuerpo dentro del molde, ejemplo presente, dependencia declarada en una de las tres formas y clasificada en `reglas-validables.md`.

### CP-04 · Nada de lo que ya estaba se rompe

```
python validadores/validar.py estandar
```

**Esperado:** sin incumplimientos. Cubre los enlaces del molde nuevo, la fila del índice y la cita al pendiente.

### CP-05 · El texto heredable no gana marcas de generación automática

```
python validadores/validar.py marcas --preparados
```

**Esperado:** sin fallas. El molde nuevo vive en `plantillas/`, que es texto que viaja a los proyectos.

## 4. Criterio de cierre

La fase cierra con los cinco casos en verde. Un caso rojo se corrige antes de publicar.
