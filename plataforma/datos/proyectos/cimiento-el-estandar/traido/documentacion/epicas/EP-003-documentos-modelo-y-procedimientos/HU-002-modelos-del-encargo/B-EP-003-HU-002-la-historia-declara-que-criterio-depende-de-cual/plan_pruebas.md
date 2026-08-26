# Plan de Pruebas — Fase B-EP-003-HU-002-la-historia-declara-que-criterio-depende-de-cual

**Para qué sirve este documento.** Dice con qué se comprueba que la fase quedó bien antes de cerrarla. Lo ejecutado está en [resultado_pruebas.md](resultado_pruebas.md).

## 0. Qué se prueba, y qué no

**Se prueba** que el molde sigue siendo válido y que la columna se entiende sin explicación aparte.

**No se prueba** que las dependencias declaradas sean las correctas: eso exige leer los dos criterios y es de quien escribe la historia.

## 1. Alcance de ejecución ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md))

La fase toca un archivo de `plantillas/`. Se corre la comprobación del estándar y la del texto heredable; no se corren las suites de la interfaz ni las de los validadores, que esta fase no toca.

## 2. Trazabilidad criterio a caso

| CA | Caso | Tipo |
|---|---|---|
| CA-01 · el molde dice lo que hay que llenar | CP-01, CP-02 | manual documentada |
| transversal · no regresión | CP-03, CP-04 | automática |

## 3. Los casos

### CP-01 · La columna se entiende sin ir a otro documento

**Cómo se ejecuta:** leer §8 del molde y responder, sin abrir nada más, qué se escribe en «Depende de» y qué se hace si no hay dependencia.

**Esperado:** las dos respuestas están en la frase que sigue a la tabla: se escriben criterios, no fases, y si no hay dependencia queda vacía.

### CP-02 · Una historia sin dependencias no paga nada

**Cómo se ejecuta:** tomar una historia real con criterios independientes (por ejemplo [HU-002 de esta épica](../../../../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-002-modelos-del-encargo/HU-002-modelos-del-encargo.md)) y comprobar que la columna vacía no la deja incompleta.

**Esperado:** la tabla se lee igual; ningún validador la reporta.

### CP-03 · El estándar sigue coherente

```
python validadores/validar.py estandar
```

**Esperado:** sin incumplimientos.

### CP-04 · El molde no gana marcas de generación automática

```
python validadores/validar.py marcas --preparados
```

**Esperado:** sin fallas: `plantillas/` es texto que viaja a los proyectos.

## 4. Criterio de cierre

La fase cierra con todos los casos en verde. Un caso rojo se corrige antes de publicar, no se anota como pendiente.
